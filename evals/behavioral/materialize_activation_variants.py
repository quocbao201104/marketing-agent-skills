from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any


DESCRIPTION_RE = re.compile(r'^description:\s*(?P<value>.+)$', re.MULTILINE)
FRONTMATTER_RE = re.compile(r'\A---\n(?P<frontmatter>.*?)\n---\n', re.DOTALL)


class MaterializationError(ValueError):
    pass


def _load_manifest(path: Path) -> dict[str, Any]:
    document = json.loads(path.read_text(encoding="utf-8"))
    expected = {
        "schema_version",
        "experiment_id",
        "base_skill",
        "base_commit",
        "constraint",
        "variants",
    }
    if not isinstance(document, dict) or set(document) != expected:
        raise MaterializationError("activation variant manifest has unexpected fields")
    if document["schema_version"] != 1:
        raise MaterializationError("activation variant manifest schema_version must equal 1")
    variants = document["variants"]
    if not isinstance(variants, dict) or not variants:
        raise MaterializationError("activation variant manifest requires variants")
    for variant_id, spec in variants.items():
        if not re.fullmatch(r"D\d+", str(variant_id)):
            raise MaterializationError(f"unsupported variant id: {variant_id!r}")
        if not isinstance(spec, dict) or set(spec) != {"label", "description"}:
            raise MaterializationError(
                f"variant {variant_id} requires only label and description"
            )
        if not isinstance(spec["description"], str) or not spec["description"].strip():
            raise MaterializationError(f"variant {variant_id} description is empty")
        if "\n" in spec["description"]:
            raise MaterializationError(
                f"variant {variant_id} description must remain one line"
            )
    return document


def _replace_description(text: str, description: str) -> str:
    match = FRONTMATTER_RE.match(text)
    if match is None:
        raise MaterializationError("SKILL.md must begin with YAML frontmatter")
    frontmatter = match.group("frontmatter")
    matches = list(DESCRIPTION_RE.finditer(frontmatter))
    if len(matches) != 1:
        raise MaterializationError("SKILL.md frontmatter must contain one description")
    quoted = json.dumps(description, ensure_ascii=False)
    new_frontmatter = DESCRIPTION_RE.sub(
        lambda _: f"description: {quoted}",
        frontmatter,
        count=1,
    )
    return (
        "---\n"
        + new_frontmatter
        + "\n---\n"
        + text[match.end():]
    )


def _extract_description(text: str) -> str:
    match = FRONTMATTER_RE.match(text)
    if match is None:
        raise MaterializationError("SKILL.md must begin with YAML frontmatter")
    description_match = DESCRIPTION_RE.search(match.group("frontmatter"))
    if description_match is None:
        raise MaterializationError("SKILL.md description is missing")
    raw = description_match.group("value").strip()
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise MaterializationError(
            "SKILL.md description must use JSON-compatible quoted text"
        ) from exc
    if not isinstance(parsed, str):
        raise MaterializationError("SKILL.md description must be text")
    return parsed


def _body_after_frontmatter(text: str) -> str:
    match = FRONTMATTER_RE.match(text)
    if match is None:
        raise MaterializationError("SKILL.md must begin with YAML frontmatter")
    return text[match.end():]


def _file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _tree_manifest(root: Path, *, exclude_skill: bool = False) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root).as_posix()
        if exclude_skill and relative == "SKILL.md":
            continue
        result[relative] = _file_hash(path)
    return result


def materialize(
    *,
    manifest_path: Path,
    repo_root: Path,
    output_root: Path,
    selected: tuple[str, ...] = (),
) -> dict[str, Any]:
    document = _load_manifest(manifest_path)
    base_skill = (repo_root / document["base_skill"]).resolve()
    if not base_skill.is_dir():
        raise MaterializationError(f"base skill not found: {base_skill}")
    base_skill_file = base_skill / "SKILL.md"
    base_text = base_skill_file.read_text(encoding="utf-8")
    base_body = _body_after_frontmatter(base_text)
    base_non_skill = _tree_manifest(base_skill, exclude_skill=True)

    variants = document["variants"]
    requested = selected or tuple(variants)
    unknown = sorted(set(requested) - set(variants))
    if unknown:
        raise MaterializationError(f"unknown activation variant: {unknown[0]}")

    output_root = output_root.resolve()
    output_root.mkdir(parents=True, exist_ok=True)
    receipts: list[dict[str, Any]] = []

    for variant_id in requested:
        spec = variants[variant_id]
        destination = output_root / variant_id / "marketing-practitioner"
        if destination.exists():
            raise MaterializationError(
                f"refusing to overwrite activation variant: {destination}"
            )
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(base_skill, destination)

        skill_file = destination / "SKILL.md"
        variant_text = _replace_description(base_text, spec["description"])
        skill_file.write_text(variant_text, encoding="utf-8", newline="\n")

        if _body_after_frontmatter(variant_text) != base_body:
            raise MaterializationError(
                f"variant {variant_id} changed the SKILL.md instruction body"
            )
        if _tree_manifest(destination, exclude_skill=True) != base_non_skill:
            raise MaterializationError(
                f"variant {variant_id} changed bundled files outside SKILL.md"
            )
        receipts.append(
            {
                "variant_id": variant_id,
                "label": spec["label"],
                "skill_source": destination.relative_to(repo_root).as_posix()
                if destination.is_relative_to(repo_root)
                else str(destination),
                "description_words": len(spec["description"].split()),
                "description_sha256": hashlib.sha256(
                    spec["description"].encode("utf-8")
                ).hexdigest(),
                "skill_tree_sha256": hashlib.sha256(
                    json.dumps(
                        _tree_manifest(destination),
                        sort_keys=True,
                        separators=(",", ":"),
                    ).encode("utf-8")
                ).hexdigest(),
            }
        )

    return {
        "schema_version": 1,
        "experiment_id": document["experiment_id"],
        "base_commit": document["base_commit"],
        "base_skill": document["base_skill"],
        "variants": receipts,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Materialize activation-description skill variants"
    )
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--variant", action="append", default=[])
    parser.add_argument("--receipt", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    try:
        args = _parser().parse_args(argv)
        receipt = materialize(
            manifest_path=args.manifest,
            repo_root=args.repo_root.resolve(),
            output_root=args.output_root,
            selected=tuple(args.variant),
        )
        rendered = json.dumps(receipt, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
        if args.receipt:
            if args.receipt.exists():
                raise MaterializationError(
                    f"refusing to overwrite receipt: {args.receipt.resolve()}"
                )
            args.receipt.parent.mkdir(parents=True, exist_ok=True)
            args.receipt.write_text(rendered, encoding="utf-8", newline="\n")
        else:
            print(rendered, end="")
        return 0
    except (MaterializationError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
