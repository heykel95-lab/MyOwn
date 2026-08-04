# Instructions for Codex and other coding agents

These instructions apply to the entire repository.

## Thesis prose: mandatory reading on every writing turn

Before writing, rewriting, extending, or editing any prose in `chapters/`,
`frontmatter/`, or `backmatter/`:

1. Open and read `THESIS_VOICE.md` completely.
2. Then open and read `THESIS_WRITING_GUIDE.md` completely.
3. Do this again on every new thesis-prose turn, even for a one-sentence edit.
   Never rely on memory, a prior conversation, or a summary of either file.
4. Tell the user at the start of the turn that both files are being opened to
   recover the thesis's required voice, evidence rules, and writing style.

The `Register` section at the beginning of `THESIS_VOICE.md` takes precedence
over older style advice where the rules conflict. Follow its rewrite procedure
and final prose scan before accepting an edit. Also follow the terminology,
chapter-role, evidence, measurement, unit, and certainty requirements in
`THESIS_WRITING_GUIDE.md`.

The objective is natural, defensible engineering prose grounded in this
thesis's implementation and measurements. Do not imitate generic AI prose, but
do not game AI detectors either: never add deliberate errors, casual filler,
unusual synonyms, invented observations, or unsupported reasoning. Preserve
the required impersonal voice, British spelling, plain technical register, and
one-main-claim-per-sentence preference.

## Other file types

- For figures and plot scripts, read `FIGURE_STYLE.md` first.
- For controller or analysis code under `code/`, read `code/CLAUDE.md` first.
- `CLAUDE.md` contains the repository-wide routing, build, and consistency
  rules and remains applicable alongside this file.
