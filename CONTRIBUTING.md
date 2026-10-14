# Contributing

Keep skills focused, self-contained, and useful to a presenter.

## Add or update a skill

1. Use `skills/<skill-name>/SKILL.md` with YAML frontmatter containing `name` and `description`. Match the name to the folder and use lowercase words separated by hyphens.
2. Put supporting guidance in `references/` and link to it from the skill. Add `agents/openai.yaml` when Codex display metadata is useful.
3. Keep product qualifications, source attribution, and the distinction between proposed demonstrations and verified outcomes. Use fictional or permission-cleared examples.
4. Add the skill to the README table. If you provide a ChatGPT adaptation, keep it consistent with the main skill.
5. Rebuild and check the downloads with Python 3.9 or newer:

```sh
python3 scripts/package_skills.py
python3 scripts/package_skills.py --check
```

Commit the source and refreshed downloads together. The packager includes `.md` files and `agents/openai.yaml` from each skill, plus the repository license. If a future skill needs executable helpers or other assets, extend the explicit packaging rules and review those files before publishing.

## Review quality

Try a realistic script and check that the suggestions preserve its meaning, fixed wording, and capability limits. A working archive and valid metadata do not prove that a review is useful. Prefer a few actionable edits over a generic scorecard.

Keep customer scripts, private links, credentials, local environment files, and raw third-party transcripts out of contributions.
