# Working rules for this repository

**The rules live in [AGENTS.md](AGENTS.md). Open and read it in full now,
before doing anything else in this repository.**

This file exists because Claude Code loads `CLAUDE.md` automatically. It is a
router, not a second set of rules: `AGENTS.md` is canonical and applies to every
agent equally. Keeping the rules in one file is deliberate — two copies would
drift apart, and an agent that had read only the stale one would act on rules
the user had already changed.

If a rule needs to change, change it in `AGENTS.md`. Do not copy rules here.

Directory-specific rules, also agent-neutral:

| Working on | Read |
|---|---|
| Thesis prose (`chapters/`, `frontmatter/`, `backmatter/`) | [THESIS_VOICE.md](THESIS_VOICE.md), then [THESIS_WRITING_GUIDE.md](THESIS_WRITING_GUIDE.md) |
| Figures (`figures/`, plot scripts) | [FIGURE_STYLE.md](FIGURE_STYLE.md) |
| Controller and analysis code (`code/`) | [code/AGENTS.md](code/AGENTS.md) |
