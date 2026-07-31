# Working rules for this repository

A robotics master's thesis: LaTeX document plus the Franka Emika Panda
Cartesian-impedance controller and analysis scripts it reports on.

Load the rules for the kind of file being touched, not all of them at once.

| Working on | Read first |
|---|---|
| Thesis prose (`chapters/`, `frontmatter/`, `backmatter/`) | [THESIS_VOICE.md](THESIS_VOICE.md), then [THESIS_WRITING_GUIDE.md](THESIS_WRITING_GUIDE.md) |
| Figures (`figures/`, plot scripts) | [FIGURE_STYLE.md](FIGURE_STYLE.md) |
| Controller and analysis code (`code/`) | [code/CLAUDE.md](code/CLAUDE.md) |

## Thesis prose

Read [THESIS_VOICE.md](THESIS_VOICE.md) before writing or rewriting any prose —
every time, not from memory of an earlier session. It carries the sentence-level
voice rules written from a detector pass over Chapters 1 and 2: the flagged
patterns, the weak-verb replacement table, the paragraph rewrite procedure, and
the originality rules.

This applies to new text, rewrites, and edits alike. If the user asks to
"rewrite this" or "make this less AI", the answer is the rewrite procedure in
that file, never synonym substitution.

[THESIS_WRITING_GUIDE.md](THESIS_WRITING_GUIDE.md) governs what a chapter
contains, what a claim may assert, and the terminology and unit conventions.

## Building

- `./build_professor.ps1` — builds `Professor_Draft.pdf` (three pdflatex passes
  plus bibtex) and opens it. `build_professor_commit.ps1` also commits.
- `./build.ps1` — builds the full `Thesis.tex`.
- Judge a build by the **final** pass. Passes 1–2 always report undefined
  citations and references; only warnings surviving the last pass matter.

Known environment issue: the installed siunitx (3.5.3, 2026-04-09) is newer than
the MiKTeX 24.4 expl3 layer (2024-10-09), so `\SI` and `\qty` fail with an
undefined `\l_siunitx_quantity_prefix_mode_str`. The thesis uses no siunitx
macros — write units as `\(1\,\mathrm{kHz}\)`, matching existing text.

## Repository-wide conventions

- British spelling: `centre`, `behaviour`, `optimisation`. Exception: literal
  software identifiers.
- Do not mention Git, branches, commits, drafts, or development history in
  thesis text.
- Never invent measurements, repetitions, fitted values, or intervals.
