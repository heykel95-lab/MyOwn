<!-- GENERATED FILE - DO NOT EDIT.
     Regenerated from AGENTS.md by sync_agent_docs.ps1 and by the
     pre-commit hook. Edit AGENTS.md instead; any change made here
     is overwritten on the next commit. The two files are kept identical
     so that an agent reading either one gets the same rules. -->

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

## Legacy source annotations

`config/review_annotations.tex` keeps the existing `\ReviewMark`, `\Revised`,
`\Comment`, and `\Added` wrappers compilable in `Thesis.pdf`. The thesis build
suppresses assessment marks and comments while preserving the thesis text
inside the inline wrappers. Do not add new annotation wrappers. Removing the
compatibility file requires first unwrapping or deleting every existing use.

## Building

- `./build.ps1` builds `Thesis.pdf` from `Thesis.tex`.
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
