# Skill Retrieval and Coverage — Activation Study Protocol

Status: **IMPLEMENTATION SCAFFOLD FROZEN — LIVE RUN PENDING**  
Parent freeze: `research/skill-retrieval-and-coverage/01-design-freeze.md`

## 1. Question under test

Does reallocating top-level skill-description budget from post-activation process prose toward practitioner jobs, latent symptom classes, and sharper boundaries improve useful `marketing-practitioner` auto-activation without creating systematic false activation?

This study changes only the `description` field of the copied skill used by each experimental arm.

The production skill remains unchanged during the ablation.

## 2. Frozen assets

```text
cases
evals/behavioral/cases/skill-activation-v1.json

activation oracle
evals/behavioral/oracles/skill-activation-v1.activation-oracle.json

description variants
evals/behavioral/variants/skill-activation-descriptions-v1.json

experiment profiles
evals/behavioral/experiments/skill-activation-v1/profiles.json

frozen splits
evals/behavioral/experiments/skill-activation-v1/splits.json

variant materializer
evals/behavioral/materialize_activation_variants.py

activation observer
evals/behavioral/behavioral_eval/activation.py

activation report CLI
evals/behavioral/behavioral_eval/activation_cli.py
```

## 3. Preflight

Run the activation-specific unit and contract checks first:

```powershell
python -B -m unittest `
  evals.behavioral.tests.test_activation `
  evals.behavioral.tests.test_activation_variants `
  evals.behavioral.tests.test_skill_activation_experiment
```

Do not begin live runs if these checks fail.

## 4. Materialize D0-D3

Generated variant trees are ignored by git.

```powershell
python -B evals/behavioral/materialize_activation_variants.py `
  --manifest evals/behavioral/variants/skill-activation-descriptions-v1.json `
  --repo-root . `
  --output-root evals/behavioral/.generated/skill-activation-description-v1 `
  --receipt evals/behavioral/results/skill-activation-v1-materialization.json
```

The materializer must prove:

```text
D0 description == selected base description

for every D*:
SKILL.md instruction body is unchanged

for every D*:
all files outside SKILL.md are byte-identical to base
```

If generated trees already exist, remove the generated experiment directory before intentionally rematerializing it. Do not teach the script to overwrite silently.

## 5. Validate cases and profiles

```powershell
python -B -m evals.behavioral.behavioral_eval.cli validate `
  --cases evals/behavioral/cases/skill-activation-v1.json `
  --profiles evals/behavioral/experiments/skill-activation-v1/profiles.json
```

## 6. Development pass

The development split contains 14 cases.

Run all four descriptions once before adding repetitions:

```powershell
python -B -m evals.behavioral.behavioral_eval.cli run `
  --cases evals/behavioral/cases/skill-activation-v1.json `
  --profiles evals/behavioral/experiments/skill-activation-v1/profiles.json `
  --adapter codex-cli `
  --repeat-limit 1 `
  --profile-id activation-d0 `
  --profile-id activation-d1 `
  --profile-id activation-d2 `
  --profile-id activation-d3 `
  --case-id BEH-ACT-DIR-001 `
  --case-id BEH-ACT-DIR-002 `
  --case-id BEH-ACT-DIR-003 `
  --case-id BEH-ACT-PARA-001 `
  --case-id BEH-ACT-PARA-002 `
  --case-id BEH-ACT-PARA-003 `
  --case-id BEH-ACT-SYM-001 `
  --case-id BEH-ACT-SYM-002 `
  --case-id BEH-ACT-SYM-003 `
  --case-id BEH-ACT-NOISY-001 `
  --case-id BEH-ACT-NOISY-002 `
  --case-id BEH-ACT-ADJ-001 `
  --case-id BEH-ACT-ADJ-003 `
  --case-id BEH-ACT-NOUN-001 `
  --results evals/behavioral/results/skill-activation-v1-dev
```

Then score activation directly from sealed events:

```powershell
python -B -m evals.behavioral.behavioral_eval.activation_cli `
  --cases evals/behavioral/cases/skill-activation-v1.json `
  --oracle evals/behavioral/oracles/skill-activation-v1.activation-oracle.json `
  --results evals/behavioral/results/skill-activation-v1-dev `
  --output evals/behavioral/results/skill-activation-v1-dev-report.json `
  --markdown evals/behavioral/results/skill-activation-v1-dev-report.md
```

Do not use the normal paired answer reporter to interpret negative activation cases.

## 7. Development interpretation

Report separately by family:

```text
activation-direct
activation-paraphrase
activation-symptom
activation-noisy
activation-adjacent-negative
activation-noun-trap-negative
```

Relevant dispositions:

```text
activation_ok
no_activation_observed
false_activation
no_false_activation_observed
operationally_invalid
```

Do not select a winner from one aggregate scalar.

A candidate description may advance only if:

```text
direct behavior does not materially regress

paraphrase / symptom / noisy activation improves
across more than one isolated wording

adjacent and noun-trap false activation does not
systematically increase
```

## 8. Candidate freeze before holdout

After inspecting development results, select at most one candidate description `D*`.

Record:

```text
selected variant
development evidence
known regressions
reason other variants were rejected
```

Then freeze that choice.

Do not edit the selected description after inspecting holdout or challenge results.

## 9. Holdout pass

Holdout cases:

```text
BEH-ACT-DIR-004
BEH-ACT-SYM-004
BEH-ACT-NOISY-003
BEH-ACT-ADJ-004
BEH-ACT-NOUN-002
BEH-ACT-NOUN-003
```

Compare only:

```text
D0 current
vs
selected D*
```

Use the profile repetition setting of two unless operational cost requires a separately documented reduction.

## 10. Challenge pass

Challenge cases:

```text
BEH-ACT-PARA-004
BEH-ACT-NOISY-004
BEH-ACT-ADJ-002
BEH-ACT-NOUN-004
```

These deliberately pressure:

```text
Vietnamese / non-English symptom phrasing
long noisy context
CRM-adjacent ownership
"AI agent" noun collision
```

The candidate fails the activation study if a gain on latent positives is purchased by a systematic new false-activation pattern here.

## 11. Telemetry interpretation

Observed activation requires either:

```text
an explicit marketing-practitioner activation event
OR
a successful read of marketing-practitioner/SKILL.md
```

For the first study:

```text
activation observed
= positive evidence

activation not observed
= no activation evidence in the sealed trace
```

Do not silently upgrade missing evidence into a universal claim that the host definitely did not internally consider the skill.

## 12. Promotion gate

Return one:

```text
KEEP_D0
PROMOTE_D*
UNRESOLVED
```

`PROMOTE_D*` requires:

```text
development improvement
+
holdout compatibility
+
challenge compatibility
+
no material direct regression
+
no systematic false-activation increase
```

If no candidate clears all non-compensatory gates, preserve the current production description and retain the research evidence.

## 13. Boundary

This study does not change or evaluate:

```text
internal owner selection
multi-route coverage
controller stopping
routing-index structure
handbook quality
final marketing answer quality
```

Those belong to the coverage study after the description decision is frozen.
