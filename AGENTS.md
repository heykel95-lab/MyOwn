# Working rules for this repository

**These instructions apply to every coding agent working in this repository —
Claude, Codex, Cursor, Copilot, or any other.**

`CLAUDE.md` holds the same text, regenerated from this file by
`sync_agent_docs.ps1` and by the pre-commit hook, so an agent that reads either
file gets the same rules. **Edit this file, never `CLAUDE.md`** — changes made
there are overwritten on the next commit.

The hook lives in `.githooks/` and is enabled per clone, so in a fresh clone
run `git config core.hooksPath .githooks` once. Until that is done the copies
are kept in step only by running `./sync_agent_docs.ps1` by hand.

A robotics master's thesis: LaTeX document plus the Franka Emika Panda
Cartesian-impedance controller and analysis scripts it reports on.

Load the rules for the kind of file being touched, not all of them at once.

| Working on | Read first |
|---|---|
| Thesis prose (`chapters/`, `frontmatter/`, `backmatter/`) | [THESIS_VOICE.md](THESIS_VOICE.md), then [THESIS_WRITING_GUIDE.md](THESIS_WRITING_GUIDE.md) |
| Figures (`figures/`, plot scripts) | [FIGURE_STYLE.md](FIGURE_STYLE.md) |
| Controller and analysis code (`code/`) | [code/AGENTS.md](code/AGENTS.md) |

## Thesis prose: mandatory reading on every writing turn

Before writing, rewriting, extending, or editing any prose in `chapters/`,
`frontmatter/`, or `backmatter/`:

1. Open and read [THESIS_VOICE.md](THESIS_VOICE.md) completely.
2. Then open and read [THESIS_WRITING_GUIDE.md](THESIS_WRITING_GUIDE.md)
   completely.
3. Do this again on every new thesis-prose turn, even for a one-sentence edit.
   Never rely on memory, a prior conversation, or a summary of either file.
4. Tell the user at the start of the turn that both files are being opened to
   recover the thesis's required voice, evidence rules, and writing style.

The **Register** section at the top of `THESIS_VOICE.md` takes precedence over
older style advice wherever the two conflict, and the **Measured from the
settled chapter** section at its end takes precedence over both. Chapter 5 is
revised and green, so it, not the guidance written against earlier drafts, is
the authority on the register: a mean of about sixteen words per sentence, a
quarter of them under twelve, almost none over twenty-eight, and determiner
openers at about half. New prose is measured against those figures before it is
offered. Results sections report what was set and what was measured; sampling
strategy, predictions, held-out checks, extrapolations and unresolved questions
do not appear there. Plain technical statements, never
compressed slogans; interpretations cross-referenced to the table or figure they
rest on; certainty bounded to one configuration and three repetitions; varied
paragraph architecture rather than varied openers. Follow its rewrite procedure
and final prose scan before accepting an edit.

This applies to new text, rewrites, and edits alike. If the user asks to
"rewrite this" or "make this less AI", the answer is the rewrite procedure in
that file, never synonym substitution.

`THESIS_WRITING_GUIDE.md` governs what a chapter contains, what a claim may
assert, and the terminology and unit conventions.

## Keep TODOS.md current, every turn

**`TODOS.md` is the standing record of everything agreed but not yet done, and
it is updated in the same turn the situation changes** — without being asked.
Add an entry the moment work is deferred, blocked, or requested and not
completed. Remove or amend an entry the moment it is finished or overtaken.
Never let it describe a state that has passed: a todo file that lags is worse
than none, because it is trusted.

**A finished entry is deleted, not marked done.** Whoever completes the work —
this agent, another agent, or the user — removes the entry in the same turn.
A file that accumulates completed items invites the next session to redo work
that is already in the document, and to argue with a state that no longer
exists. The record of what was done is the document itself.

An entry says what is wrong, what the fix is, and what is blocking it. Where a
task is partly done, say which part, so the next session does not redo it or
assume it whole. Detailed specifications stay in the guide they belong to and
are referenced from here rather than duplicated.

Finishing a turn with deferred work not written down is a failure of the turn,
even when everything attempted succeeded.

## Record new style rulings as they are given

**When the user states an editorial preference, a terminology decision, a
naming ban, or a rule about what a claim may assert, write it into
`THESIS_WRITING_GUIDE.md` in the same turn** — or into `THESIS_VOICE.md` when
it governs how sentences sound, or `FIGURE_STYLE.md` when it governs how a
figure is drawn. Do not wait to be asked, and do not apply the ruling only to
the passage under discussion: an instruction given once has to bind every later
turn and every other agent, and the guides are the only thing that carries it
there.

This applies whether the ruling arrives as a rule (`never use "workpiece"`) or
as a correction to one sentence, where the general rule has to be extracted
first. Record it in the section it belongs to, in the same voice as the
surrounding text, with the reason where the reason is what makes it
followable. Where it overturns something already written, replace that text
rather than appending a contradiction, and say in the reply which file changed
and what it now says.

Two things do not go in: anything the user framed as a one-off for a single
sentence, and anything not yet settled. When a ruling is superseded later,
remove the old wording rather than leaving both. A rule that is suspended
rather than dropped keeps its reasoning, marked as suspended, so it can be
restored.

The objective is natural, defensible engineering prose grounded in this thesis's
implementation and measurements. Do not imitate generic AI prose, but do not
game AI detectors either: never add deliberate errors, casual filler, unusual
synonyms, invented observations, or unsupported reasoning. Preserve the required
impersonal voice, British spelling, plain technical register, and
one-main-claim-per-sentence preference.

## Review-draft colour coding

`config/review_annotations.tex` defines two kinds of mark, both invisible in
`Thesis.pdf` and `Professor_Draft.pdf` and visible only in `Review_Draft.pdf`.

`\ReviewMark{...}{...}` is an assessment box placed after a heading. It judges
the section that follows and does not change the text. A sufficient assessment
is rendered orange.

`\Revised{...}` (green), `\Comment{...}` and `\Added{...}` (blue) mark the
text itself:

- **Green revised text is frozen. Never change a word inside `\Revised{}`.** Not a
  reword, not a tightened clause, not an added qualifier, not a restructure.
  The passage has been controlled and found correct and already satisfies what
  the thesis requires. A revised chapter that comes back unchanged is the
  correct outcome, not a missed opportunity.
- **The one permitted exception is a change without which the document will
  not compile** — for example boxing `\mbox{et al.\ }` so the highlighter can
  reconstruct the line. Make the smallest fix that restores the build, change
  no words, and say so. Nothing else qualifies: not a typo, not a wrong unit,
  not a contradiction. Those are reported, not fixed.
- **If a settled passage seems to need something, do not edit it — raise it.**
  Either say so and wait for a decision, or place a `\Comment{...}` next to the
  passage. It renders as `comment: "…"` in the review draft and is suppressed
  entirely in the clean builds, so the submitted text is untouched.
- **Do not add, remove, recolour or reword a `\ReviewMark` box in a chapter
  that has not been declared revised.** Assessment boxes are the user's
  judgement of their own work, not yours to reconcile.
- **Only when it is genuinely necessary** — the context or the reasoning is
  incomplete without it, a crucial fact is missing, a logical step is broken.
  Never for polish, flow, or style. When in doubt, leave it and say nothing.
- **`\Added{}` is for text in sections not yet revised**, marking new writing
  as a whole sentence or whole word. It is never used inside a green revised passage;
  a comment goes there instead.

### Marking a chapter as revised

When the user says a chapter is revised, do all three without asking again:

1. **Delete every `\ReviewMark` assessment box in that chapter** — orange,
   yellow, red and grey alike. A settled chapter is no longer being judged, so
   the assessments retire with it. Say afterwards which concerns those boxes
   were carrying, so a real objection is not lost silently.
2. **Add one green revised-status box directly under `\chapter{...}`**, before
   the first `\section`, framing the whole chapter. The legacy
   `\ReviewMark{purple}{...}` source key renders this green box. Not one per
   section.
3. **Wrap every prose paragraph in `\Revised{...}`** — one wrapper per
   paragraph, since a span cannot cross a paragraph break. Do not wrap headings,
   labels, the `\ReviewMark` box, or float contents.

Then build `Review_Draft.tex` and a clean document, and fix only what blocks
the build. Report the wrapper counts and every build-required fix by name.

Three mechanical rules, because the highlight is typeset character by
character:

- Inline maths, citations, cross-references and control spaces inside a marked
  span must be wrapped in `\mbox{}` — `\mbox{\(J^\top\)}`,
  `\mbox{\citep{Key}}`, `\mbox{\Cref{fig:x}}`, `\mbox{et al.\ }`. Wrapping them
  in a helper macro instead does **not** work, and `\soulregister` does not
  survive natbib's optional argument.
- A span may not cross a paragraph break. Mark each paragraph separately.
- A soul "Reconstruction failed" error means an unboxed construct of this kind
  is inside a span; the log line number points at the closing brace, so look
  through the whole paragraph, not just that line.

## Building

- `./build_professor.ps1` — builds `Professor_Draft.pdf` (three pdflatex passes
  plus bibtex) and opens it. `build_professor_commit.ps1` also commits.
- `Review_Draft.tex` is built the same way (pdflatex, bibtex, pdflatex ×2); it
  has no script of its own.
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
