# Build a skill upload package

Download the [v2.2.1 `skill.zip`](https://github.com/quocbao201104/marketing-agent-skills/releases/download/v2.2.1/skill.zip), or build from the tagged source using the command below. The host-specific import limits below still apply.

Use the release asset named exactly `skill.zip` for skill upload. Do **not** use GitHub's automatically generated **Source code (zip)** or **Source code (tar.gz)** downloads: those archives contain the whole repository rather than the single distributable skill and can include more than one `SKILL.md` entrypoint.

Publishing a release triggers `.github/workflows/release.yml`, which builds from that release tag and attaches `skill.zip`. Ordinary pushes do not rebuild release assets, except changes to the release workflow itself. Existing ZIP assets are not overwritten; fixes ship under a new release tag.

From a Git checkout, run:

```text
python -B scripts/package_skill.py <new-output-path.zip>
```

The builder validates the skill and packages current bytes of Git-tracked files under `skills/marketing-practitioner`, plus the root license and third-party notices. It preserves one `marketing-practitioner/` directory with `SKILL.md` immediately inside it. Existing output files are never overwritten. Stage any newly added runtime files before packaging; untracked files are not included. No Codex plugin manifest, local configuration, research reports, or evaluation results are bundled.

This layout follows Claude's [custom skill ZIP instructions](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills). Upload the resulting ZIP through Claude's custom Skills controls and enable it.

ChatGPT documents **Plugins > Skills > Create > Upload from your computer** for eligible accounts. This ZIP is a candidate for that uploader, not a confirmed ChatGPT-compatible import: the [official upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) do not specify the archive layout. Confirm acceptance in the target account before claiming compatibility.

Uploading the ZIP into an ordinary conversation does not by itself install a skill. This package also does not register a public plugin-directory entry. The Codex plugin remains a separate packaging surface over the same source files.
