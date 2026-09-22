# Portuguese Local Adaptation — Post-Merge Evidence Addressability Fix

Status: **POST-MERGE MECHANICAL ADDRESSABILITY REPAIR**  
Date: 2026-09-18  
Merged Portuguese track: `aa80ab21813f070ce302c21226943454bb920794`

## Defect

`skills/marketing-agent-skills/references/local-adaptation-portuguese-evidence.md` used headings of the form:

```text
## PTLA01 — ...
```

while `scripts/get-knowledge.py --source <ID>` discovers evidence only from bracketed source headings matching:

```text
## [PTLA01] ...
```

Therefore the main adaptation route remained addressable, but deterministic source lookup for `PTLA01–PTLA12` did not.

## Repair

Change only the twelve runtime evidence headings:

```text
## PTLA01 ...  →  ## [PTLA01] ...
...
## PTLA12 ...  →  ## [PTLA12] ...
```

No evidence wording, scope, runtime semantics, controller behavior, route, index binding, or loader behavior changes.

## Architecture

```text
SKILL.md                              unchanged
Chapter 07                            unchanged
routing-index.json                    unchanged
scripts/get-knowledge.py              unchanged
adapt-localization.relationship-realization unchanged
PT-LANG-ADDR-01 semantics             unchanged
```

This is a mechanical addressability repair, not a new evidence or adaptation decision.
