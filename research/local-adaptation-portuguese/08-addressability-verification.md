# Portuguese Evidence Addressability Verification

Status: **MECHANICAL VERIFICATION NOTE**

The repaired runtime evidence headings now follow the exact source-heading contract consumed by `scripts/get-knowledge.py`:

```text
## [PTLA01] ...
...
## [PTLA12] ...
```

The loader's source scanner matches bracketed IDs with the existing pattern and therefore can discover `PTLA01–PTLA12` without changing `routing-index.json`, controller logic, or loader semantics.

The owner-aligned runtime route remains:

```text
adapt-localization.relationship-realization
```

No Portuguese-specific route is introduced.
