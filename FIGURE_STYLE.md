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

**The drawn palette is black, red, blue and green, with yellow only if a fifth
is unavoidable.** This was settled on the moment-bookkeeping figure and applies
to every hand-drawn diagram, not only to plots. Three consequences follow, and
they override the greyscale conventions above wherever the two disagree:

- **Grey is not a drawing colour.** A quantity that is present but inactive in
  one panel is drawn thin in its own colour, not faint grey. Grey remains
  available only for reference lines and excluded data in plots.
- **White is not a colour either.** Do not fill a shape white to hide what
  passes behind it; order the drawing so nothing needs hiding, and leave the
  shape unfilled.
- **Every line is solid**, in diagrams as in plots. A dashed or dotted line
  reads as a different kind of quantity — a model, a bound, a projection — so
  it must not be spent on marking one of two otherwise identical objects.
  Distinguish by colour first and by line weight second.

**One quantity, one colour, across every panel of a figure.** In the
moment-bookkeeping figure \(r_c\) is blue and \(r_T\) is green in both panels,
which is what lets a reader see that the same two levers are being shown twice
with different ones acting. Give the label the colour of the thing it names.

**Pure `green` is too light to print on white.** Use `green!60!black`, which
still reads as green beside blue and red. The same caution applies to `yellow`
if a fifth colour is ever needed.

**A drawn moment carries its symbol.** An arc with no label states that a
moment exists but not which one, and the reader cannot match it to the relation
in the annotation. Label the arc with the symbol the surrounding text uses.

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

**No symbol touches anything.** A label, a symbol or a name never touches or
overlaps an arrow, a line, a box, an axis, another label, or the drawing it
belongs to. This is the rule that gets broken most often, because a label placed
a small offset from its arrow looks separated in the source and lands on the
arrowhead once `\resizebox` has scaled the picture. Offsets of one or two
millimetres are not clearance; give a symbol beside an arrow roughly a third of
its own width of space, and check the result in the compiled document rather
than in the coordinates.

Leave a visible gap between a label and any box: aim for at least half a line
of text, and never let a label sit inside a node's bounding box.

### Scale the picture, do not resize it

**A tikz diagram is sized by `scale=` inside `egin{tikzpicture}[...]`, not by
wrapping the `\input` in `esizebox`.** `scale=` moves the coordinates and
leaves node text at the size it was declared; `esizebox` magnifies the text
along with the drawing, so a diagram drawn at 7 cm and stretched to the text
width comes out with labels about twice the size of the body text. It also
multiplies every clearance, which is how a label that looked separated in the
source ends up on an arrowhead.

This was found on the three Chapter 3 diagrams, where the symbols were visibly
larger than the surrounding prose and two labels overlapped each other. Draw the
picture at whatever size is convenient, then pick the `scale=` that brings it to
the width it should occupy, and include it with a plain `\input`.

The rule holds in the other direction too. A wide diagram shrunk to fit by
`esizebox` has labels *smaller* than the body text, which is the same fault
and is easier to miss.

**Explanatory sentences do not go inside the picture.** A two-line note added
beside a diagram widens its bounding box, and `\resizebox` then shrinks the
whole drawing to fit the page, so the geometry becomes unreadable to buy room
for prose that belongs in the body text. Keep the drawing to the geometry and
its symbols; say the rest in the paragraph before or after it.

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

### Every generated plot has a generator, kept in `code/python/figures/`

The scripts are in the repository, with a name map and running instructions in
`code/python/figures/README.md`. Read that file before changing a figure.

They had looked lost, and the reason is worth keeping. **The figures were
renamed by hand after they were generated**, so a search of either experiment
repository for a current file name returns nothing. `MAIN_B_KR.pdf` is written
by the script as `MAIN_A_KR.pdf`, `MAIN_D_wrench.pdf` as `MAIN_E_wrench.pdf`,
and so on for seven of the nine. Search for the old case letter, or for a
legend string, not for the name the thesis uses.

Five of the nine come from `make_coc_figures.py`, which needs no data at all:
its values are the means already reported in Chapter 5, written into the file.
The other four read logged CSV and only run beside `experiments/results/` in
the repository they came from.

A plot can therefore be corrected by editing its script and re-running it. A
data series, an axis, or a case letter is now changeable, which a direct PDF
edit could never do.

One caution when re-running. The scripts still write the old case letters, so
the output has to be renamed on the way into `figures/` here, and a script run
straight into `figures/` will leave the old names behind rather than replacing
the figure it was meant to update.

### Result figures may be drawn from the reported means

A figure whose content is already tabulated in the thesis does not need a
generator at all. Four Chapter 5 figures were redrawn directly in `pgfplots`
from the means in their own tables: the Case-A bars, the
two-panel Case-D sweep, the Case-D-against-Case-F comparison, and the two-panel
Case-G plot. They are `\input` as `.tex`, so they take the document font and
need no `esizebox`.

This is not a licence to invent data. **The only numbers a redrawn figure may
contain are ones already reported in the thesis**, and where the table carries
standard deviations they are drawn as error bars, as in the Case-F series.

Where the original plot carried information the table does not, redrawing loses
it, and the original is kept rather than discarded. `MAIN_D_sign.pdf` showed
the per-setting spread of the Case-D sweep, which appears in no table, so it
moved to the supporting-plots appendix instead of being deleted.

**Check every legend against the data in the compiled figure.** Three of the
four redrawn figures first placed a legend on top of a curve, in a corner that
looked empty when the coordinates were written. `legend pos` is chosen per
panel from where that panel's data actually are, not once for the figure.

### Correcting a label in a plot that has no generator

The metric-comparison legend read `EE-inferred angular deviation` after the term
was banned everywhere else, and it was recorded here as unpatchable. **That was
wrong, and the reason it was wrong is worth keeping.** The search had been for
the plain ASCII bytes. The generator has since been found, and its label was
corrected to match, so this figure no longer depends on the patch; the account
below stands for the next figure whose generator is genuinely gone.

The text is drawn through an `Identity-H`
`CIDFontType2`, so every character occupies two bytes and the string sits in the
content stream as UTF-16BE. Searching for `text.encode("utf-16-be")` finds it
immediately. It now reads `Alignment angle from end-effector pose`.

Editing a label this way is legitimate when the generator is lost, but only
after three checks, in this order:

1. **Decode `/CIDToGIDMap`** and confirm every character of the replacement has
   a non-zero glyph. A missing glyph renders blank, and nothing warns you.
2. **Check the `/W` array** covers the same code points. A code with no width
   falls back to `/DW` and the spacing goes visibly wrong.
3. **Look at where the label sits.** Length changes are not reflowed, so a
   longer string simply runs on. Here the entry below it in the same legend
   column was already half as long again, so the replacement had room.

The stream length changes, which moves every later object, so the cross-
reference table has to be rebuilt from the new offsets rather than patched.
Keep the original alongside as `.orig` until the replacement has been seen in
the compiled thesis — not in the standalone figure, which proves only that the
file still opens.

This is a repair, not a substitute for the plotting code. It cannot change a
data series, an axis, or a case letter.

### Captions and in-figure text are never questions

A caption, a panel sub-label, or any text inside the drawing is a declarative
noun phrase. `Which lever pairs with which force to give which moment.` was a
real caption in this thesis and had to be replaced. The full rule, with the
list of banned openers and the grep that finds them, is under *Scientific
narrative* in `THESIS_WRITING_GUIDE.md`; it covers captions, headings and
appendix titles alike.

Writing a caption to say what a figure *explains* is what produces the question
form. Say what it *shows*.

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
- **Every plot has a legend, in its own upper right corner.** Each panel names
  the series it shows, so a panel can be read without looking away from it.
  Give the axes about a quarter of headroom (`ax.margins(y=0.3)`) so the legend
  sits above the data rather than on it, and check the rendered figure: a
  corner that looks empty at one scale is not empty at another. Where a figure
  is a single panel the rule is the same.
- **Commanded and estimated quantities go in separate panels** when their
  magnitudes differ by an order or their signs disagree. Overlaying them makes
  the smaller unreadable and invites reading one curve as the other.
- **A reference line belongs only where it means something.** A zero line on a
  load axis forces the axis down to zero and squashes the data.
- **Excluded runs are omitted from the plots.** They remain in the source data
  and are excluded from every plotted mean and uncertainty interval. A
  scientifically material exclusion is documented in the accompanying text or
  table rather than added as a diagnostic series to each figure.
- **No internal title**, for the same reason as a drawn diagram.
- **A multi-panel figure labels its panels `(a)`, `(b)`, … and the body text
  refers to them by those labels.** This is not the internal title the rule
  above bans: a title restates the caption, whereas a panel label is the only
  way the text can point at one half of a figure. Set it with
  `ax.set_title("(a)")` in matplotlib and `title={\footnotesize (a) …}` in
  `pgfplots`, where the Case-D panels already carry a short description after
  the letter. The caption then names what the figure shows and stops; what each
  panel carries is a sentence in the text, not a second caption paragraph.
  Figure D.2 was rewritten this way — its caption had grown to four lines
  describing both panels, which is exactly the material the body text is for.
- **An axis label names which quantity is plotted, not its kind.** `Angle [°]`
  was the y-axis of Figure D.2's first panel, where both curves are the
  alignment angle obtained two different ways, so the label left the reader to
  guess. It now reads `Alignment angle [°]` and the legend separates the two
  routes to it.
- **An axis carries the symbol the symbol list assigns to the quantity.** A
  reader who has met \(d_{c,t_2}\) in the text should not have to work out that
  `Centre position along t_2` is the same thing. Where a symbol exists, the
  axis is that symbol and its unit; a descriptive phrase may stay in front of it
  where the symbol alone would be cryptic, as in
  `Cumulative projected null-space motion \(E_N\) [°]`. The pass that applied
  this set the axes to \(d_{c,t_1}\), \(d_{c,t_2}\),
  \(\Delta\theta_{\mathrm{set},t_i}\), \(\phi_{\mathrm{tilt}}\),
  \(\theta_{\mathrm{align}}\), \(\phi_{\mathrm{set}}\),
  \(|\Delta\theta_{\mathrm{align}}|\), \(E_N\) and
  \(\Delta\sigma_{\min,\mathrm{dist}}\).

  **Where no symbol is assigned to what the axis means, the words stay.** Three
  axes kept their prose for that reason: the Case-F comparison, whose \(x\)
  carries a tangential displacement on one series and a tool-axis displacement
  on the other, so no single component symbol covers it; the categorical axes of
  the Case-A bars and the direction comparison, which list conditions rather
  than plot a quantity; and the time axes, which the author prefers as they
  read. Do not invent a symbol to satisfy this rule.

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
