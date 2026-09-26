# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is not an application and has no development server. It is a research-first marketing decision skill for AI agents. The installable runtime lives under `skills/marketing-agent-skills/`; research provenance, evaluation infrastructure, and repository tooling remain outside that package.

Use formal, plain English in repository content. Preserve UTF-8, Unicode, and existing line endings. Python uses four-space indentation, `snake_case` functions, and `PascalCase` classes. Knowledge files generally use kebab-case names; numbered handbook chapters retain their prefixes.

## Commands

Run commands from the repository root on Windows PowerShell. CI uses Python 3.13. Always use `python -B` so Python does not create cache artifacts.

```powershell
# Complete local/CI verification gate
.\scripts\verify.ps1

# Package validation only
.\scripts\verify.ps1 -PackageOnly

# Validate the package directly
python -B scripts/validate_skill.py skills/marketing-agent-skills

# Test retrieval mechanics and validate every route/source binding
python -B skills/marketing-agent-skills/scripts/test-knowledge-routing.py
python -B skills/marketing-agent-skills/scripts/get-knowledge.py --validate

# Unit-test suites
python -B -m unittest discover -s evals/behavioral/tests -v
python -B -m unittest discover -s evals/pressure-discovery/pilot/tests -v
python -B -m unittest discover -s evals/work-episodes/episode-01/tests -v

# One test module or one test method
python -B -m unittest evals.behavioral.tests.test_validation -v
python -B -m unittest evals.behavioral.tests.test_validation.ValidationTests.test_duplicate_case_identity_fails_closed -v

# Episode 01 deterministic preflight
python -B evals/work-episodes/episode-01/preflight.py

# Create a portable ZIP; the destination must not already exist
python -B scripts/package_skill.py ../skill.zip
```

There is no separate formatter or linter. `verify.ps1` is the authoritative gate: it runs package and routing validation, corpus validation, all harness test suites, Episode 01 preflight, UTF-8 checks, and generated-artifact checks. `-PackageOnly` stops after package validators.

To inspect one logical knowledge route or evidence source:

```powershell
python -B skills/marketing-agent-skills/scripts/get-knowledge.py <route-id>
python -B skills/marketing-agent-skills/scripts/get-knowledge.py --source <source-id>
```

Behavioral corpus contracts can be validated without a live model run:

```powershell
python -B -m evals.behavioral.behavioral_eval.cli validate --cases evals/behavioral/cases/<corpus>.json --profiles evals/behavioral/profiles
```

Do not treat fixture runs as behavioral evidence; they verify orchestration and report plumbing only. Generated behavioral results belong under `evals/behavioral/results/` and must not be tracked.

## Architecture

### Runtime package

`skills/marketing-agent-skills/` is the complete distributable unit:

- `SKILL.md` is the compact runtime controller and universal behavioral contract. It identifies one of seven jobs (`WRITE`, `DECIDE`, `DIAGNOSE`, `RESEARCH / UNDERSTAND`, `ADAPT`, `TEST`, `LEARN`), retains settled decisions, localizes open decision surfaces, routes only when specialist knowledge can change the result, and defines useful completion.
- `routing-index.json` is the physical address table for stable logical knowledge IDs. Logical IDs are deliberately distinct from file paths. Do not duplicate handbook prose in routing metadata.
- `handbook/` owns governed shared knowledge. Chapters 08 (content environments), 09 (commerce), and 10 (Commercial Design) are especially high-blast-radius shared semantic surfaces.
- `platforms/` contains time-sensitive, system-specific social and commerce modules. Platform-local facts normally remain local rather than becoming shared theory.
- `adaptations/` specializes an already-open decision through bounded local evidence. It is not a country-profile or culture-pack layer and does not create a new decision owner.
- `frameworks/` provides optional practitioner records and qualitative review rubrics; they are not mandatory runtime forms or validated scores.
- `references/` holds operating/work-coordination guidance, report planning, bibliography, and evidence ledgers. A source establishes provenance, not a runtime rule by itself.
- `scripts/get-knowledge.py` retrieves the smallest indexed section or evidence entry; `test-knowledge-routing.py` tests that retrieval contract.

The key runtime flow is:

1. Preserve supplied and already adopted state.
2. Identify the current job and only the unresolved questions that could materially change its useful result.
3. Use supplied state directly when sufficient; otherwise route by decision dependency, not by topic, platform name, or artifact noun.
4. Resolve indexed knowledge through `routing-index.json` and retrieve the smallest useful section.
5. Keep observations, interpretations, hypotheses, decisions, and evidence scope distinct; retain unsupported questions as unknown.
6. Complete all active requested outcomes without reopening settled choices merely to improve them.

### Non-runtime layers

- `research/` preserves methodology, theory lineage, audits, rejected hypotheses, and pre-promotion evidence. It is provenance, not agent runtime instruction.
- `evals/behavioral/` compares isolated no-skill and skill conditions, seals raw records, and creates condition-blind review packets. Its `trace` reports reads, `report` handles semantic judgments, and `coverage` evaluates independently judged decision surfaces; none is a single quality score.
- `evals/pressure-discovery/pilot/` tests evaluation infrastructure for pressure/diagnostic cases.
- `evals/work-episodes/` contains deterministic, stateful multi-phase work scenarios and preflight checks.
- Root `scripts/` validates, packages, and builds assets. `package_skill.py` packages only Git-tracked runtime files plus `LICENSE` and `THIRD_PARTY_NOTICES.md`, using current working-tree bytes and deterministic ZIP metadata.
- `.claude-plugin/` and `.codex-plugin/` are distribution metadata. `.github/workflows/verify.yml` runs `verify.ps1`; release automation packages the same runtime ZIP.

## Change discipline

Follow `CONTRIBUTING.md`: change the smallest surface that corrects a demonstrated problem.

- Level 0 editorial/mechanical changes remain local.
- Level 1 bounded knowledge/evidence changes must preserve source, product, market, population, and time scope.
- Level 2 runtime/shared-semantic changes require a concrete chain: `INPUT / TASK → CURRENT REPRESENTATION OR ROUTE → FAILURE → WHY THE FAILURE CHANGES THE DECISION → SMALLEST CORRECTION`, plus a targeted regression, smoke case, or counterexample.
- Level 3 boundary or architecture expansions require explicit research and architecture review before runtime promotion.

Treat these as protected surfaces:

- Change `SKILL.md` only when cross-task behavior or routing boundaries must change, not merely because handbook knowledge changed.
- Before expanding Chapters 08–10, first test whether existing primitives and owners can represent the case.
- Keep provider/platform mechanics in the relevant platform owner unless a cross-platform failure justifies promotion.
- Keep `logical knowledge ID != physical location`, `semantic route != evidence source ID`, and `routing metadata != handbook prose`.
- When editing indexed guidance, inspect the actual excerpt returned by `get-knowledge.py` together with `SKILL.md`; a syntactically valid selector may still omit a decision-changing qualification.

For substantive empirical claims, prefer primary or authoritative evidence, record both what it supports and does not support, preserve applicable scope, and do not convert correlation into causation, qualitative recurrence into prevalence, attribution into incrementality, or stated willingness-to-pay into an optimal price.

Do not commit `__pycache__/`, `.pyc`, or generated behavioral results. Preserve delivered logo kits byte-for-byte. The verification gate also requires valid UTF-8 and the `≠` and `→` sentinel characters in `SKILL.md`.
