# Better Presentations

Reusable AI skills for clearer demos, stronger stories, and more useful presentation feedback.

## Choose a skill

| Skill | Purpose | Downloads |
| --- | --- | --- |
| [Enterprise Tech Next-Gen Presentation](skills/enterprise-tech-nextgen-presentation/SKILL.md) | Build a branded HTML deck with diagrams, slide navigation, and presenter notes. | [ZIP](https://github.com/fullerc/better-presentations/raw/refs/heads/main/downloads/enterprise-tech-nextgen-presentation.zip) · [.skill](https://github.com/fullerc/better-presentations/raw/refs/heads/main/downloads/enterprise-tech-nextgen-presentation.skill) |
| [Demo Script Review](skills/demo-script-review/SKILL.md) | Improve a demo script, talk track, storyboard, or presenter notes with a few specific, high-impact edits. | [ZIP](https://github.com/fullerc/better-presentations/raw/refs/heads/main/downloads/demo-script-review.zip) · [.skill](https://github.com/fullerc/better-presentations/raw/refs/heads/main/downloads/demo-script-review.skill) |

Use either skill independently. Together, the deck builder creates the presentation and the reviewer improves its story and delivery. The reviewer also works on live product demos that have no deck. Installing one skill does not require the other.

The review uses eight storytelling lenses: analogy, concretization, demonstration, rapport, framing, redefinition, soul, and showmanship. It preserves the presenter's voice and checks that the words match what the audience can actually observe. Expect three to five prioritized edits with concrete wording or scene changes, rather than a required score for every technique.

## Try them

For a deck, supply your audience, intended outcome, approved content, and customer website:

> Use the Enterprise Tech Next-Gen Presentation skill to build an HTML deck for a 15-minute solution discussion, with a clear story, an architecture diagram, and presenter notes.

For a review, attach your script:

> Review this demo script for a 10-minute presentation to operations leaders. Preserve the product qualifications and suggest the three most useful changes. For any rewritten demo beat, show what I say, what I do, and what the audience sees.

You can ask for a full rewrite, or use the [self-review checklist](skills/demo-script-review/references/self-review-checklist.md) without an AI assistant. To build a deck by hand, copy [starter-deck.html](skills/enterprise-tech-nextgen-presentation/references/starter-deck.html) and follow the [framework guide](skills/enterprise-tech-nextgen-presentation/references/PRESENTATION-FRAMEWORK.md).

The HTML deck has no build step; external fonts and Mermaid diagrams may need network access. Presenter notes are part of the HTML source, so include only material suitable for anyone who receives the file.

## Install

### Codex

Ask Codex to install the skill you want:

```text
Use $skill-installer to install the skill at
https://github.com/fullerc/better-presentations/tree/main/skills/demo-script-review
```

For the deck builder, use `https://github.com/fullerc/better-presentations/tree/main/skills/enterprise-tech-nextgen-presentation` instead. Then invoke the installed skill with `$demo-script-review` or `$enterprise-tech-nextgen-presentation`.

### Claude Code

Copy either complete folder from `skills/` into `~/.claude/skills/` for personal use, or `.claude/skills/` in your project. Then use `/demo-script-review` or `/enterprise-tech-nextgen-presentation`. Copy the individual skill folders, not this entire repository, into the skills directory. See the [Claude Code skills documentation](https://code.claude.com/docs/en/skills).

### Claude

Download the ZIP for the skill you want and upload it through Claude's custom skill upload flow, when available for your account. Each ZIP contains a single skill folder with `SKILL.md` and its supporting files. See [Claude's skills guide](https://support.claude.com/en/articles/12512176-what-are-skills) for current availability and setup. Each `.skill` download contains the same ZIP data for tools that accept that extension.

### ChatGPT

For demo script review:

1. Copy [CHATGPT_INSTRUCTIONS.md](skills/demo-script-review/CHATGPT_INSTRUCTIONS.md) into a ChatGPT Project's instructions or a custom GPT's Instructions field.
2. Add [techniques.md](skills/demo-script-review/references/techniques.md) as a project file or GPT knowledge file.
3. Attach your script and ask for a review.

See the official guides for [Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) and [creating GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts). This is a copy-and-paste adaptation; the skill folder remains the maintained version.

For the deck builder, the existing [AI instructions](skills/enterprise-tech-nextgen-presentation/references/AI-INSTRUCTIONS.md) and [framework guide](skills/enterprise-tech-nextgen-presentation/references/PRESENTATION-FRAMEWORK.md) accompany the HTML template. They require an assistant that can create and inspect HTML files; they are not a condensed ChatGPT instruction profile.

## Repository layout

```text
skills/
  enterprise-tech-nextgen-presentation/
    SKILL.md
    ORIGIN.md
    agents/openai.yaml
    references/             HTML template, framework, prompts, original license
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

Each skill lives in its own folder under `skills/`, so more can be added independently. See [CONTRIBUTING.md](CONTRIBUTING.md) for the conventions and packaging commands.

## Existing deck-skill users

The [original repository](https://github.com/fullerc/enterprise-tech-nextgen-presentation) remains available. This collection imports its deck skill as a separate folder; it does not change existing installations. To move to this collection, update your existing `enterprise-tech-nextgen-presentation` skill folder from `skills/enterprise-tech-nextgen-presentation/` here. Keep one installed copy of that skill name. Cloning this entire collection directly into a single skill folder is not the same as the original repository's installation method.

## Source and license

Demo Script Review was developed from a supplied transcript titled *The Storytelling Genius Of Steve Jobs*. The eight lens names come from that video's analysis; the workflow and practical guidance are adaptations. This is not a formal rubric authored by Steve Jobs. The original transcript and video are not distributed here. See the [techniques reference](skills/demo-script-review/references/techniques.md#source-and-interpretation).

The deck framework originates with [Charles Ensley and contributors](https://github.com/charles-ensley/enterprise-tech-nextgen-presentation), with changes from the [fullerc repository](https://github.com/fullerc/enterprise-tech-nextgen-presentation). Its original MIT copyright notice is preserved in [references/LICENSE](skills/enterprise-tech-nextgen-presentation/references/LICENSE). The imported revision is recorded in [ORIGIN.md](skills/enterprise-tech-nextgen-presentation/ORIGIN.md).

The collection includes portable ChatGPT instructions and a checklist adapted from the original demo review sharing package. All downloads are rebuilt from the maintained source and include the applicable license.

[MIT License](LICENSE). References to third-party works do not grant rights to those works or imply endorsement.
