#!/usr/bin/env python3
"""Audit and synchronize knowledge routing index against Markdown headings."""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "routing-index.json"

ROUTE_ID_RE = re.compile(r"^[a-z0-9]+(?:[.-][a-z0-9]+)*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(\S.*)$")
FENCE_OPEN_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")

PREFIX_RE = re.compile(
    r"^(?P<prefix>(?:\d+(?:\.\d+)*\.?)|(?:[A-Z]{1,4}\d*\s*—)|(?:Layer\s+\d+\s*—)|(?:(?:Step|Phase)\s+\d+\s*[:—]))\s*(?P<title>.*)$",
    re.UNICODE,
)

MARKER_ID_RE = re.compile(
    r"^<!--\s*route:(?:id|start)\s+(?P<id>[a-z0-9]+(?:[.-][a-z0-9]+)*)\s*-->$"
)


class RoutingSyncError(RuntimeError):
    pass


class DriftStatus(str, Enum):
    CLEAN = "CLEAN"
    MARKER_MATCH = "MARKER_MATCH"
    RENAMED_HEADING = "RENAMED_HEADING"
    RENUMBERED = "RENUMBERED"
    AMBIGUOUS = "AMBIGUOUS"
    UNRESOLVED = "UNRESOLVED"
    MISSING_TARGET = "MISSING_TARGET"


@dataclass(frozen=True)
class HeadingNode:
    raw: str
    level: int
    line_number: int
    prefix: str
    title: str
    clean_tokens: frozenset[str]
    attached_marker: str | None


@dataclass
class RouteAudit:
    namespace: str
    section: str
    route_id: str
    current_selector: str | dict[str, str]
    status: DriftStatus
    proposed_selector: str | dict[str, str] | None
    confidence: float
    line_number: int | None
    message: str


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    obj: dict[str, Any] = {}
    for key, value in pairs:
        if key in obj:
            raise RoutingSyncError(f"duplicate JSON key in routing manifest: {key}")
        obj[key] = value
    return obj


def load_manifest(path: Path | None = None) -> dict[str, Any]:
    manifest_file = path or MANIFEST_PATH
    try:
        data = json.loads(
            manifest_file.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_keys,
        )
    except FileNotFoundError as exc:
        raise RoutingSyncError(f"routing manifest not found: {manifest_file}") from exc
    except json.JSONDecodeError as exc:
        raise RoutingSyncError(f"invalid routing manifest JSON: {exc}") from exc

    if data.get("version") != 2:
        raise RoutingSyncError(f"unsupported routing manifest version: {data.get('version')!r}")
    if not isinstance(data.get("namespaces"), dict):
        raise RoutingSyncError("routing manifest must contain an object named 'namespaces'")
    return data


def resolve_path(relative_path: str, skill_root: Path | None = None) -> Path:
    base = skill_root or ROOT
    candidate = (base / relative_path).resolve()
    try:
        candidate.relative_to(base.resolve())
    except ValueError as exc:
        raise RoutingSyncError(f"route escapes skill root: {relative_path}") from exc
    return candidate


def iter_unfenced_lines(lines: list[str]):
    fence_char: str | None = None
    fence_len = 0

    for index, line in enumerate(lines):
        raw = line.rstrip("\r\n")

        if fence_char is not None:
            closing = re.match(
                rf"^ {{0,3}}{re.escape(fence_char)}{{{fence_len},}}[ \t]*$",
                raw,
            )
            if closing:
                fence_char = None
                fence_len = 0
            continue

        opening = FENCE_OPEN_RE.match(raw)
        if opening:
            token = opening.group(1)
            info = opening.group(2)
            if token[0] == "`" and "`" in info:
                yield index, line
                continue
            fence_char = token[0]
            fence_len = len(token)
            continue

        yield index, line


def tokenize_text(text: str) -> frozenset[str]:
    words = re.findall(r"\w+", text.lower(), re.UNICODE)
    return frozenset(words)


def scan_file_headings(file_path: Path) -> list[HeadingNode]:
    text = file_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    visible_lines = list(iter_unfenced_lines(lines))

    headings: list[HeadingNode] = []
    last_marker: str | None = None
    last_marker_line: int | None = None

    for index, line in visible_lines:
        raw_line = line.rstrip("\r\n")
        line_num = index + 1

        marker_match = MARKER_ID_RE.match(raw_line)
        if marker_match:
            last_marker = marker_match.group("id")
            last_marker_line = line_num
            continue

        match = HEADING_RE.match(raw_line)
        if not match:
            if last_marker_line is not None and (line_num - last_marker_line) > 2:
                last_marker = None
                last_marker_line = None
            continue

        hashes, rest = match.group(1), match.group(2)
        level = len(hashes)

        prefix = ""
        title = rest.strip()
        prefix_match = PREFIX_RE.match(title)
        if prefix_match:
            prefix = prefix_match.group("prefix").strip()
            title = prefix_match.group("title").strip()

        tokens = tokenize_text(title)
        attached = last_marker if (last_marker_line is not None and (line_num - last_marker_line) <= 2) else None
        last_marker = None
        last_marker_line = None

        headings.append(
            HeadingNode(
                raw=raw_line,
                level=level,
                line_number=line_num,
                prefix=prefix,
                title=title,
                clean_tokens=tokens,
                attached_marker=attached,
            )
        )

    return headings


def compute_heading_similarity(
    old_node: HeadingNode,
    cand_node: HeadingNode,
) -> tuple[float, DriftStatus]:
    # 0. Marker match
    if cand_node.attached_marker and old_node.attached_marker == cand_node.attached_marker:
        return 1.0, DriftStatus.MARKER_MATCH

    same_level = old_node.level == cand_node.level
    same_prefix = bool(old_node.prefix and old_node.prefix == cand_node.prefix)

    seq_ratio = difflib.SequenceMatcher(
        None, old_node.title.lower(), cand_node.title.lower()
    ).ratio()

    union = old_node.clean_tokens | cand_node.clean_tokens
    inter = old_node.clean_tokens & cand_node.clean_tokens
    jaccard = (len(inter) / len(union)) if union else 1.0

    if same_level and same_prefix and old_node.prefix:
        score = 0.50 + 0.35 * seq_ratio + 0.15 * jaccard
        return score, DriftStatus.RENAMED_HEADING

    if same_level and seq_ratio >= 0.88:
        score = 0.40 + 0.60 * seq_ratio
        return score, DriftStatus.RENUMBERED

    level_score = 0.20 if same_level else 0.0
    score = level_score + 0.50 * seq_ratio + 0.30 * jaccard
    return score, DriftStatus.RENAMED_HEADING


def parse_heading_selector(selector_raw: str, line_num: int = 0) -> HeadingNode:
    match = HEADING_RE.match(selector_raw)
    if not match:
        return HeadingNode(
            raw=selector_raw,
            level=0,
            line_number=line_num,
            prefix="",
            title=selector_raw,
            clean_tokens=tokenize_text(selector_raw),
            attached_marker=None,
        )
    level = len(match.group(1))
    rest = match.group(2).strip()
    prefix = ""
    title = rest
    prefix_match = PREFIX_RE.match(title)
    if prefix_match:
        prefix = prefix_match.group("prefix").strip()
        title = prefix_match.group("title").strip()

    return HeadingNode(
        raw=selector_raw,
        level=level,
        line_number=line_num,
        prefix=prefix,
        title=title,
        clean_tokens=tokenize_text(title),
        attached_marker=None,
    )


def audit_namespace_routes(
    namespace: str,
    group_data: dict[str, Any],
    skill_root: Path | None = None,
    threshold: float = 0.70,
) -> list[RouteAudit]:
    base = skill_root or ROOT
    relative_path = group_data.get("path")
    sections = group_data.get("sections", {})

    audits: list[RouteAudit] = []

    if not isinstance(relative_path, str) or not relative_path:
        for sec in sections:
            audits.append(
                RouteAudit(
                    namespace=namespace,
                    section=sec,
                    route_id=f"{namespace}.{sec}",
                    current_selector=sections[sec],
                    status=DriftStatus.MISSING_TARGET,
                    proposed_selector=None,
                    confidence=0.0,
                    line_number=None,
                    message=f"namespace {namespace} missing valid path",
                )
            )
        return audits

    target_file = resolve_path(relative_path, base)
    if not target_file.is_file():
        for sec in sections:
            audits.append(
                RouteAudit(
                    namespace=namespace,
                    section=sec,
                    route_id=f"{namespace}.{sec}",
                    current_selector=sections[sec],
                    status=DriftStatus.MISSING_TARGET,
                    proposed_selector=None,
                    confidence=0.0,
                    line_number=None,
                    message=f"target file not found: {relative_path}",
                )
            )
        return audits

    available_headings = scan_file_headings(target_file)
    heading_count: dict[str, int] = {}
    for h in available_headings:
        heading_count[h.raw] = heading_count.get(h.raw, 0) + 1

    for section_key, selector in sections.items():
        route_id = f"{namespace}.{section_key}"

        # Marker selector: {"marker": "..."}
        if isinstance(selector, dict) and "marker" in selector:
            marker_id = selector["marker"]
            matches = [h for h in available_headings if h.attached_marker == marker_id]
            if len(matches) == 1:
                audits.append(
                    RouteAudit(
                        namespace=namespace,
                        section=section_key,
                        route_id=route_id,
                        current_selector=selector,
                        status=DriftStatus.CLEAN,
                        proposed_selector=selector,
                        confidence=1.0,
                        line_number=matches[0].line_number,
                        message="marker matches exactly once",
                    )
                )
            else:
                audits.append(
                    RouteAudit(
                        namespace=namespace,
                        section=section_key,
                        route_id=route_id,
                        current_selector=selector,
                        status=DriftStatus.UNRESOLVED,
                        proposed_selector=None,
                        confidence=0.0,
                        line_number=None,
                        message=f"marker {marker_id!r} found {len(matches)} times",
                    )
                )
            continue

        if not isinstance(selector, str):
            audits.append(
                RouteAudit(
                    namespace=namespace,
                    section=section_key,
                    route_id=route_id,
                    current_selector=selector,
                    status=DriftStatus.UNRESOLVED,
                    proposed_selector=None,
                    confidence=0.0,
                    line_number=None,
                    message=f"unsupported selector type: {selector!r}",
                )
            )
            continue

        # Exact match check
        exact_matches = [h for h in available_headings if h.raw == selector]
        if len(exact_matches) == 1:
            audits.append(
                RouteAudit(
                    namespace=namespace,
                    section=section_key,
                    route_id=route_id,
                    current_selector=selector,
                    status=DriftStatus.CLEAN,
                    proposed_selector=selector,
                    confidence=1.0,
                    line_number=exact_matches[0].line_number,
                    message="exact match",
                )
            )
            continue
        elif len(exact_matches) > 1:
            audits.append(
                RouteAudit(
                    namespace=namespace,
                    section=section_key,
                    route_id=route_id,
                    current_selector=selector,
                    status=DriftStatus.AMBIGUOUS,
                    proposed_selector=None,
                    confidence=1.0,
                    line_number=exact_matches[0].line_number,
                    message=f"heading appears {len(exact_matches)} times (non-unique)",
                )
            )
            continue

        # Exact match failed -> compute similarity against all headings
        old_node = parse_heading_selector(selector)
        old_node_with_marker = HeadingNode(
            raw=old_node.raw,
            level=old_node.level,
            line_number=old_node.line_number,
            prefix=old_node.prefix,
            title=old_node.title,
            clean_tokens=old_node.clean_tokens,
            attached_marker=route_id,
        )

        candidates: list[tuple[float, DriftStatus, HeadingNode]] = []
        for cand in available_headings:
            # Candidate must be unique in file
            if heading_count.get(cand.raw, 0) != 1:
                continue
            sim, st = compute_heading_similarity(old_node_with_marker, cand)
            if sim >= threshold:
                candidates.append((sim, st, cand))

        candidates.sort(key=lambda x: x[0], reverse=True)

        if not candidates:
            audits.append(
                RouteAudit(
                    namespace=namespace,
                    section=section_key,
                    route_id=route_id,
                    current_selector=selector,
                    status=DriftStatus.UNRESOLVED,
                    proposed_selector=None,
                    confidence=0.0,
                    line_number=None,
                    message="no candidate heading meets confidence threshold",
                )
            )
            continue

        best_score, best_status, best_node = candidates[0]
        if len(candidates) > 1:
            second_score, _, _ = candidates[1]
            if (best_score - second_score) < 0.12:
                audits.append(
                    RouteAudit(
                        namespace=namespace,
                        section=section_key,
                        route_id=route_id,
                        current_selector=selector,
                        status=DriftStatus.AMBIGUOUS,
                        proposed_selector=best_node.raw,
                        confidence=best_score,
                        line_number=best_node.line_number,
                        message=f"competing candidates within safety margin ({best_score:.2f} vs {second_score:.2f})",
                    )
                )
                continue

        audits.append(
            RouteAudit(
                namespace=namespace,
                section=section_key,
                route_id=route_id,
                current_selector=selector,
                status=best_status,
                proposed_selector=best_node.raw,
                confidence=round(best_score, 3),
                line_number=best_node.line_number,
                message=f"drift matched to line {best_node.line_number}: {best_node.raw!r}",
            )
        )

    return audits


def format_manifest(manifest: dict[str, Any]) -> str:
    """Format manifest in canonical grouped-semantic-routing style (2-space, single-line namespaces)."""
    lines: list[str] = [
        "{",
        f'  "version": {manifest.get("version", 2)},',
        f'  "format": {json.dumps(manifest.get("format", "grouped-semantic-routing"))},',
        f'  "notes": {json.dumps(manifest.get("notes", ""))},',
        '  "namespaces": {',
    ]
    namespaces = manifest.get("namespaces", {})
    ns_keys = list(namespaces.keys())
    for index, ns_key in enumerate(ns_keys):
        comma = "," if index < len(ns_keys) - 1 else ""
        group_data = namespaces[ns_key]
        group_json = json.dumps(group_data, ensure_ascii=False)
        lines.append(f'    "{ns_key}": {group_json}{comma}')
    lines.append("  }")
    lines.append("}\n")
    return "\n".join(lines)


def run_audit(
    manifest_path: Path | None = None,
    skill_root: Path | None = None,
    target_namespace: str | None = None,
    threshold: float = 0.70,
) -> tuple[dict[str, Any], list[RouteAudit]]:
    base = skill_root or ROOT
    manifest = load_manifest(manifest_path)
    namespaces = manifest["namespaces"]

    audits: list[RouteAudit] = []
    keys = [target_namespace] if target_namespace else list(namespaces.keys())

    for ns in keys:
        if ns not in namespaces:
            raise RoutingSyncError(f"unknown namespace: {ns}")
        audits.extend(
            audit_namespace_routes(
                ns,
                namespaces[ns],
                skill_root=base,
                threshold=threshold,
            )
        )

    return manifest, audits


def apply_sync(
    manifest: dict[str, Any],
    audits: list[RouteAudit],
) -> tuple[dict[str, Any], int]:
    namespaces = manifest["namespaces"]
    repaired_count = 0

    for a in audits:
        if a.status in (DriftStatus.RENAMED_HEADING, DriftStatus.RENUMBERED, DriftStatus.MARKER_MATCH):
            if a.proposed_selector and a.proposed_selector != a.current_selector:
                namespaces[a.namespace]["sections"][a.section] = a.proposed_selector
                repaired_count += 1

    return manifest, repaired_count


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit and synchronize knowledge routing index against Markdown headings."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check for route drift (default mode). Exit 0 if clean, 1 if drift detected.",
    )
    parser.add_argument(
        "--sync",
        "--fix",
        dest="sync",
        action="store_true",
        help="Synchronize routing-index.json with repaired headings.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show proposed changes without writing to disk.",
    )
    parser.add_argument(
        "--namespace",
        type=str,
        default=None,
        help="Scope check/sync to a specific namespace.",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=MANIFEST_PATH,
        help="Path to routing-index.json (default: skill root manifest).",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.70,
        help="Minimum confidence threshold for auto-repair (default: 0.70).",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed per-route audit output.",
    )

    args = parser.parse_args(argv)

    try:
        manifest, audits = run_audit(
            manifest_path=args.manifest,
            skill_root=args.manifest.parent,
            target_namespace=args.namespace,
            threshold=args.threshold,
        )
    except RoutingSyncError as exc:
        print(f"FAIL\t{exc}", file=sys.stderr)
        return 1

    clean_count = sum(1 for a in audits if a.status == DriftStatus.CLEAN)
    drift_items = [
        a for a in audits
        if a.status in (DriftStatus.RENAMED_HEADING, DriftStatus.RENUMBERED, DriftStatus.MARKER_MATCH)
    ]
    problem_items = [
        a for a in audits
        if a.status in (DriftStatus.AMBIGUOUS, DriftStatus.UNRESOLVED, DriftStatus.MISSING_TARGET)
    ]

    if args.verbose or drift_items or problem_items:
        for a in audits:
            if a.status == DriftStatus.CLEAN and not args.verbose:
                continue
            status_indicator = "PASS" if a.status == DriftStatus.CLEAN else "DRIFT"
            if a.status in (DriftStatus.AMBIGUOUS, DriftStatus.UNRESOLVED, DriftStatus.MISSING_TARGET):
                status_indicator = "FAIL"
            print(
                f"{status_indicator}\t{a.route_id}\t[{a.status.value}] conf={a.confidence:.2f} line={a.line_number}: {a.message}"
            )
            if a.proposed_selector and a.proposed_selector != a.current_selector:
                print(f"  Old: {a.current_selector}")
                print(f"  New: {a.proposed_selector}")

    # Sync / Fix mode
    if args.sync or args.dry_run:
        updated_manifest, repaired_count = apply_sync(manifest, audits)
        formatted = format_manifest(updated_manifest)

        if args.dry_run:
            print(f"DRY-RUN\twould repair {repaired_count} drifting route(s)")
            if problem_items:
                print(f"DRY-RUN\t{len(problem_items)} route(s) require manual inspection", file=sys.stderr)
                return 1
            return 0

        args.manifest.write_text(formatted, encoding="utf-8")
        print(f"SYNC\trepaired {repaired_count} drifting route(s) in {args.manifest.name}")
        if problem_items:
            print(f"SYNC\t{len(problem_items)} route(s) could not be resolved automatically", file=sys.stderr)
            return 1
        return 0

    # Default / Check mode
    if drift_items or problem_items:
        print(
            f"FAIL\troute drift detected: {len(drift_items)} repairable, {len(problem_items)} unresolved (total routes: {len(audits)})",
            file=sys.stderr,
        )
        return 1

    print(f"PASS\t{clean_count} routes in sync across {len(manifest.get('namespaces', {}))} namespace(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
