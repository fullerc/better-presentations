# Better Presentations

Reusable AI skills for clearer demos, stronger stories, and more useful presentation feedback.

## Available skills

| Skill | What it does | Downloads |
| --- | --- | --- |
| [Demo Script Review](skills/demo-script-review/SKILL.md) | Reviews a demo script, talk track, storyboard, or presenter notes and suggests a few specific, high-impact changes. | [ZIP](https://github.com/fullerc/better-presentations/raw/refs/heads/main/downloads/demo-script-review.zip) · [.skill](https://github.com/fullerc/better-presentations/raw/refs/heads/main/downloads/demo-script-review.skill) |

The review uses eight storytelling lenses: analogy, concretization, demonstration, rapport, framing, redefinition, soul, and showmanship. It preserves the presenter's voice and checks that the words match what the audience can actually observe. Expect three to five prioritized edits with concrete replacement wording or scene changes, rather than a required score for every technique.

## Try it

Attach your script and ask:

> Review this demo script for a 10-minute presentation to operations leaders. Preserve the product qualifications and suggest the three most useful changes. For any rewritten demo beat, show what I say, what I do, and what the audience sees.

You can also ask for a full rewrite or use the [self-review checklist](skills/demo-script-review/references/self-review-checklist.md) without an AI assistant.

## Install

### Codex

Ask Codex:

```text
Use $skill-installer to install the skill at
https://github.com/fullerc/better-presentations/tree/main/skills/demo-script-review
```

Then invoke it with `Use $demo-script-review to review this script.`

### Claude Code

Copy the complete `skills/demo-script-review` folder into `~/.claude/skills/` for personal use, or `.claude/skills/` in your project. Then use `/demo-script-review` with your script. See the [Claude Code skills documentation](https://code.claude.com/docs/en/skills).

### Claude

Download the skill ZIP linked above and upload it through Claude's custom skill upload flow, when available for your account. The ZIP contains a single skill folder with `SKILL.md` and its supporting references. See [Claude's skills guide](https://support.claude.com/en/articles/12512176-what-are-skills) for current availability and setup. The `.skill` download contains the same ZIP data for tools that accept that extension.

### ChatGPT

1. Copy [CHATGPT_INSTRUCTIONS.md](skills/demo-script-review/CHATGPT_INSTRUCTIONS.md) into a ChatGPT Project's instructions or a custom GPT's Instructions field.
2. Add [techniques.md](skills/demo-script-review/references/techniques.md) as a project file or GPT knowledge file.
3. Attach your script and ask for a review.

See the official guides for [Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) and [creating GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts). This is a copy-and-paste adaptation of the skill; the source folder remains the maintained version.

## Repository layout

```text
skills/
  demo-script-review/
    SKILL.md
    CHATGPT_INSTRUCTIONS.md
    agents/openai.yaml
    references/
      techniques.md
      self-review-checklist.md
downloads/                  Generated ZIP and .skill packages
scripts/package_skills.py   Rebuild or check the downloads
```

Each skill lives in its own folder under `skills/`, so more can be added independently. See [CONTRIBUTING.md](CONTRIBUTING.md) for the small set of conventions and packaging commands.

## Source and license

The first skill was developed from a supplied transcript titled *The Storytelling Genius Of Steve Jobs*. The eight lens names come from that video's analysis; the review workflow and practical guidance are adaptations. This is not a formal rubric authored by Steve Jobs. The original transcript and video are not distributed here. More context is in the [techniques reference](skills/demo-script-review/references/techniques.md#source-and-interpretation).

The repository combines the demo review skill with the useful portable instructions and checklist from the original sharing package. Both downloads are rebuilt from the maintained source and include the license.

[MIT License](LICENSE). References to third-party works do not grant rights to those works or imply endorsement.
