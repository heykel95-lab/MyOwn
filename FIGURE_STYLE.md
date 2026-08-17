# Figure Style

How figures are drawn for this thesis. Companion to
[THESIS_WRITING_GUIDE.md](THESIS_WRITING_GUIDE.md), which owns captions,
wording and evidence rules. Update this file when a new convention is agreed.

**The principle: a figure is typeset, not pasted.** Diagrams are TikZ source in
`figures/`, so they carry the document's fonts, scale with the text, and stay
editable. Data plots are generated to vector PDF with the same faces. A raster
screenshot is a last resort and never carries text the reader must read.

## Drawn diagrams (TikZ)

Write the diagram as `figures/<name>.tex` containing one `tikzpicture`, with no
preamble of its own, and include it with

```tex
\begin{figure}[H]
  \centering
  \resizebox{\textwidth}{!}{\input{figures/<name>.tex}}
  \caption{Short noun phrase.}
  \label{fig:<name>}
\end{figure}
```

`config/packages.tex` already loads `tikz` with `arrows.meta`, `calc` and
`positioning`, plus `siunitx` and `needspace`. Do not load packages from inside
a figure file and do not set a font: the figure inherits the document's Latin
Modern, which is the point of drawing it this way.

### Styles first, then nodes, then routing

Define every style at the top of the `tikzpicture` so the file reads as a
description of the drawing rather than a list of coordinates. The established
set:

```tex
blk/.style={draw=gray!70!black, fill=gray!8,    rounded corners=2pt, ...}  % computed
src/.style={draw=gray!60,       fill=blue!6,    rounded corners=2pt, ...}  % input
sel/.style={draw=gray!70!black, fill=orange!12, rounded corners=2pt, ...}  % selected
sig/.style={-{Latex[length=2mm]}, thick, gray!55!black}                    % signal
lbl/.style={font=\footnotesize, inner sep=2pt, fill=white}                 % label
```

Colour carries meaning and only meaning: blue for what enters from outside,
orange for what a parameter selects, grey for what is computed, red reserved
for a stop or an abort path. A figure that uses colour decoratively is harder
to read in print, where the fills are close in tone.

### Routing

**Orthogonal only.** A diagonal line in a block diagram reads as a different
kind of connection and is almost always an accident.

**Use absolute coordinates for the corners.** `++(0,1.35)` is relative to the
node anchor, not to the origin, so a run written that way silently becomes a
diagonal when the anchor is not where it was assumed to be. Write
`(model.north) -- (0.0,1.45) -- (13.8,1.45) -- (jt.north)`.

**One horizontal run per height.** Give each long connection its own `y` and
keep a list of them in a comment, so a new run cannot be added on top of an
existing one. The control-loop diagram uses, top to bottom: the Jacobian above
the chain, the measured pose and the active gains just below it, the mass
matrix, the null-space torque, the Coriolis term, and the loop closure last.

**Route around boxes, not through them.** Check the vertical extent of every
node the run passes, not just its centre.

### Clearance

Leave a visible gap between a label and any box: aim for at least half a line
of text, and never let a label sit inside a node's bounding box.

**A label is never filled.** A white fill behind the text erases whatever it
sits on, and on a label placed `above` a run it erases the top of that run, so
the connection reads as broken exactly where the reader is looking for its
name. Give the label room instead.

If a label crowds something, move the run rather than nudging the label. The
spacing between runs is what creates room for their labels.

### What does not belong in the drawing

- An internal title. The caption identifies the figure; a title repeats it.
- A legend inside a narrow panel, where it lands on the data or an axis label.
- Anything not discussed in the text.

## Generated plots (matplotlib)

Plots come from the scripts in `analysis/` in the controller repository, are
written to its `figures/` directory, and are copied into `figures/` here as
vector PDF.

### Naming

`MAIN_<INDEX>_<subject>.pdf`, uppercase prefix, uppercase index, lower-case
subject. The index is the case letter the figure belongs to, so the file name
sorts next to the section that discusses it and a figure whose case is dropped
is found by its name alone:

| File | Belongs to |
| --- | --- |
| `MAIN_A_KR.pdf` | Case A |
| `MAIN_B_KP.pdf` | Case B |
| `MAIN_C_general_pole.pdf` | Case C |
| `MAIN_D_contact.pdf` | Case D |
| `MAIN_E_sign.pdf`, `MAIN_E_wrench.pdf`, `MAIN_E_diagnostics.pdf` | Case E |
| `MAIN_G_toolaxis.pdf` | Case G |
| `MAIN_H_magnitude.pdf` | Case H |
| `MAIN_DQ_descent.pdf`, `MAIN_DQ_metric_comparison.pdf` | Data quality |
| `MAIN_NS_nullspace_automatic.pdf` | Null-space results |

A figure spanning several cases carries their letters in order. A
figure that serves a section rather than a case carries a two-letter tag for
that section (`DQ`, `NS`). The label follows the file:
`\label{fig:results_case_<letter>}`, or `\label{fig:results_<subject>}` for a
section figure. The script that writes the file names it, so regenerating the
plots cannot reintroduce an old name.

- **Fonts match the document.** `FONT_STYLE = "latex"` selects Latin Modern
  with Computer Modern maths. Verify in the output, not the configuration:
  `pdffonts` on the result should show `LMRoman*` and `Cmr/Cmmi/Cmsy`.
  `usetex` is deliberately not used; it needs `dvipng`, which is not installed,
  and it would tie every plot to a preamble kept elsewhere.
- **Ticks sit at the settings that were tested.** A sweep of three values does
  not justify a log scale, and a log decade fills itself with minor labels that
  collide at printed width. Linear spacing ticked at the tested values shows
  the sample as it is.
- **Categorical colours begin in one fixed order:** black, red, blue, then
  yellow. A plot with one series uses black; a second series adds red; a third
  adds blue; and a fourth adds yellow. When more than four curves are genuinely
  required, add green, purple, cyan, and orange in that order. Grey is reserved
  for reference lines and excluded data. Continuous fields may use a continuous
  colour map where a categorical palette would misrepresent the quantity.
- **Measured points use open markers with restrained connecting lines.** Use a
  white marker face, a coloured edge of approximately \(1.1\) points, and a
  line width of approximately \(1.25\) points. Marker shape repeats the series
  distinction so the plot remains legible in monochrome.
- **Every line is solid.** A dashed or dotted line reads as a different kind of
  quantity — a model, a bound, a projection — so a broken line drawn merely to
  separate two measured series misleads. Series are distinguished by colour and
  by marker shape, never by dash pattern.
- **A time series is drawn at a bounded number of points.** A set-up log holds
  about five thousand samples and a panel is a few centimetres wide, so the
  full rate paints a band rather than a curve. Around nine hundred points keeps
  a curve legible at printed width.
- **Grid is horizontal only.** It exists to compare values across panels.
- **Every plot has a legend.** A multi-panel figure has one shared legend below
  the panels, assembled from every panel so that no series is omitted. A
  single-panel legend may remain inside the axes only where it does not cover
  data. Reserve layout space for a legend below the axes; do not rely on a
  tight bounding box to prevent overlap with axis labels or the caption.
- **A reference line belongs only where it means something.** A zero line on a
  load axis forces the axis down to zero and squashes the data.
- **Excluded runs are omitted from the plots.** They remain in the source data
  and are excluded from every plotted mean and uncertainty interval. A
  scientifically material exclusion is documented in the accompanying text or
  table rather than added as a diagnostic series to each figure.
- **No internal title**, for the same reason as a drawn diagram.

## Checking a figure

Inspect the compiled document, not the standalone file. Whether a label
collides depends on the final scale, and `\resizebox` changes it.

```bash
pdflatex Thesis.tex
pdftoppm -png -r 130 -f <page> -l <page> Thesis.pdf out
```

Then look at the rendered page and check:

- no line crosses a box, and no two lines run at the same height;
- no label touches a box, a line, or another label;
- every arrowhead lands on the node it belongs to;
- the smallest text is still legible at final printed size;
- the figure has no internal title and its caption is a short noun phrase.
