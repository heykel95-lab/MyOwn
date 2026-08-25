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
moment-bookkeeping figure \(r_c\) is blue and \(r_{\mathrm{Tool}}\) is green in both panels,
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

**Nothing in a figure intersects anything else.** A label, a symbol or a name
never touches or overlaps an arrow, a line, an arc, a box, an axis, another
label, or the drawing it belongs to, and two drawn elements do not cross where
the crossing carries no meaning. Curved arrows are the usual offender, because
an arc swings away from the coordinate that placed it and reaches a label that
looked clear in the source. Place a symbol on the side of its arrow that the
arc leaves free. This is the rule that gets broken most often, because a label placed
a small offset from its arrow looks separated in the source and lands on the
arrowhead once `\resizebox` has scaled the picture. Offsets of one or two
millimetres are not clearance; give a symbol beside an arrow roughly a third of
its own width of space, and check the result in the compiled document rather
than in the coordinates.

Leave a visible gap between a label and any box: aim for at least half a line
of text, and never let a label sit inside a node's bounding box.

### Scale the picture, do not resize it

**A tikz diagram is sized by `scale=` inside `egin{tikzpicture}[...]`, not by
wrapping the `\input` in `
esizebox`.** `scale=` moves the coordinates and
leaves node text at the size it was declared; `
esizebox` magnifies the text
along with the drawing, so a diagram drawn at 7 cm and stretched to the text
width comes out with labels about twice the size of the body text. It also
multiplies every clearance, which is how a label that looked separated in the
source ends up on an arrowhead.

This was found on the three Chapter 3 diagrams, where the symbols were visibly
larger than the surrounding prose and two labels overlapped each other. Draw the
picture at whatever size is convenient, then pick the `scale=` that brings it to
the width it should occupy, and include it with a plain `\input`.

The rule holds in the other direction too. A wide diagram shrunk to fit by
`
esizebox` has labels *smaller* than the body text, which is the same fault
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

### Node text begins with a capital

Every line of text inside a box starts with an uppercase letter — `One seated
pose`, `Complete tool face flat`, `Re-seated check`, `Invariant-direction fit`.
This applies to the second line of a two-line node as well, because the two
lines read as parallel labels rather than as a sentence running on.

**A line that begins with a symbol keeps the symbol**, unchanged and
uncapitalised: `$T_1$--$T_3$`, `$p_s,\ R_{\mathrm{surface}}$`,
`$\varepsilon_{\mathrm{plane}}$`, `$0.50^\circ$`. Notation is not prose and
must not be recased to satisfy a typographic rule.

The same holds for row headings and for a label placed beside an arrow, except
that a bare symbol carried by an arrow — `$n_{\mathrm{EE}}$`, `$n_s$` — is
notation and stays as it is.

Widening a box to fit a capitalised or lengthened line can close the gap its
arrows need. The calibration flow lost almost all of the first run in its top
row this way. Move the columns apart rather than shortening the text, and check
the arrow runs in the compiled figure afterwards.

### A diagram of parallel chains names each chain

Where a diagram runs two or more chains as separate rows, each row carries a
heading naming what it produces. The calibration flow needed this because both
of its chains begin with the tool face seated flat, so the top row read as tool
calibration until it was labelled; the reader could not tell which row was
which.

**The heading is capitalised and centred over its row's first box** —
`Surface plane`, `Tool normal` — set in `\footnotesize` with `anchor=south`, a
third of a line above the box. Centring over the first box rather than
left-aligning at its edge is what makes the heading read as belonging to the
row rather than floating beside it.

Put the headings above the rows, not to the left of them. A label column widens
the picture, and `\resizebox{\textwidth}` then shrinks every other label to buy
the room, which is the fault the scaling rule above describes. Headings above
cost height, which is free. Where the lower heading has no clearance, move the
rows apart rather than tightening the gap around it.

A row heading is not the internal title banned below. A title restates the
caption; a heading names one chain of several, which the caption cannot do
without describing the whole drawing.

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

### How to regenerate a plot, in practice

Every step below was needed to regenerate a figure on this machine, and each
one failed the first time it was skipped.

**A script runs from a directory that has the data beside it, not from
`code/python/figures/`.** Each generator resolves its input relative to its own
location — `HERE/../experiments/derived/metrics.csv` for the
compliance-centre plots, `HERE/../experiments/results/` for the ones that read
logged runs. Copy the script into a scratch directory whose parent holds an
`experiments` symlink to the right repository, and run it there. Running it in
place finds nothing.

**Take the helper modules with it.** The generators import `figure_style`, and
several also import `extract_metrics`; `make_nullspace_figure.py` additionally
imports `make_figures`. A `ModuleNotFoundError` here means a helper was left
behind, not that the script is broken.

**Which repository each script needs:**

| Script | Data it reads |
| --- | --- |
| `make_coc_figures.py` | `Thesis_Final_Control/experiments/derived/metrics.csv` |
| `plot_coc_case.py`, `plot_setup_diagnostics.py` | `Thesis_Final_Control/experiments/results/` |
| `compare_angle_metrics.py` | `Thesis_Final_Control/experiments/results/` |
| `make_nullspace_figure.py` | `MyController/experiments/`, in that repository's own `analysis/` + `experiments/` layout |

`make_nullspace_figure.py` detects which layout it is sitting in, so give it
`<root>/analysis/` for the script and `<root>/experiments/` for the data.

**`--out-dir` is not obeyed by every script.** `make_nullspace_figure.py`
writes to `figures/` and `derived/` beside its resolved data root regardless.
Find the file it actually wrote before copying anything.

**`plot_coc_case.py` takes its trials on the command line**, and the three the
reported figure uses are listed in `code/python/figures/README.md`. Its legend
text comes from those arguments, so the legend convention is applied at the
call, not in the script.

**Rename on the way in.** The scripts still write the old case letters; the map
is in `code/python/figures/README.md`. Copying a fresh output into `figures/`
under its generated name leaves the figure the thesis includes untouched and
adds an orphan.

**Check the result before trusting it.** `pdftotext` on the output shows the
axis and legend strings, which is the fastest way to confirm a label change
landed — a `sub` that silently matched nothing is the usual failure. Then
`pdffonts` should show `LMRoman*` and `Cmr/Cmmi/Cmsy`, and the numbers printed
by the script should match the values the thesis reports. A regenerated figure
that differs from the committed one in anything but the intended label is a
signal to stop, not to install it.

### Result figures may be drawn from the reported means

A figure whose content is already tabulated in the thesis does not need a
generator at all. Four result figures were redrawn directly in `pgfplots`
from the means in their own tables: the Case-A bars, the two-panel Case-D
variation, the Case-D comparison with the supporting tool-axis check, and the
two-panel Case-E plot. They are `\input` as `.tex`, so they take the document font and
need no `
esizebox`.

This is not a licence to invent data. **The only numbers a redrawn figure may
contain are ones already reported in the thesis**, and where the table carries
standard deviations they are drawn as error bars, as in the supporting
tool-axis series.

The main Case-D plot carries the sample standard deviation at every setting as
an error bar. The earlier `MAIN_D_sign.pdf` appendix plot duplicated that
information and is not included in the thesis.

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
subject. Main-study figures use their current A--D case letter. Supporting
figures use a descriptive subject in the thesis even where a retained binary
file name still carries its acquisition-campaign identifier:

| File | Belongs to |
| --- | --- |
| `MAIN_A_contact.pdf` | Case A |
| `MAIN_B_KR.pdf` | Case B |
| `MAIN_C_KP.pdf` | Case C |
| `MAIN_D_sign.pdf`, `MAIN_D_wrench.pdf`, `MAIN_D_diagnostics.pdf` | Case D |
| `MAIN_G_magnitude.pdf` | Supporting orientation-offset-magnitude check; retained file identifier |
| `MAIN_E_frame.pdf` | Supporting definition-frame check; retained file identifier |
| `MAIN_F_toolaxis.pdf` | Supporting tool-axis check; retained file identifier |
| `MAIN_H_direction.pdf` | Supporting intermediate-direction check; retained file identifier |
| `MAIN_DQ_descent.pdf`, `MAIN_DQ_metric_comparison.pdf` | Data quality |
| `MAIN_NS_nullspace_automatic.pdf` | Null-space results |

A figure spanning several main cases carries their letters in order. A figure
that serves a section rather than a case carries a two-letter tag for that
section (`DQ`, `NS`). Main-case labels use
`\label{fig:results_case_<letter>}`. Supporting-check and section labels use a
descriptive subject and never retain a former case letter. The script that
writes a generated file names it, so regeneration must preserve this mapping.

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
- **A bar chart skips the red and pairs black with the bar blue.** The order
  above is written for curves, where red is a thin line. A filled red bar
  carries far more ink than a red curve, reads as a warning beside the black bar
  next to it, and prints heavy. The direction comparison and the frame
  comparison both dropped it on this ground. Beyond two bar series, continue
  with yellow and then the extended order, still skipping red.

  **The bar blue is `SERIES_BLUE`, `#0057B8` — the same blue a curve takes.**
  All three bar figures carry it: the two written by `make_coc_figures.py` as
  `BAR_FILL_BLUE`, and the Case-A bars, which name it with
  `\definecolor{barblue}{HTML}{0057B8}`.

  **In `pgfplots`, put a bar fill on the `\addplot`, never on
  `every axis plot`.** The `ybar` cycle list sets its own fill at thirty per
  cent of the plot colour and is applied *after* an axis-level append style, so
  `every axis plot/.append style={fill=…}` is silently overridden. The Case-A
  bars spent a long time rendering `#B2B2FF` — thirty per cent of pure blue —
  while their source read `fill=blue!20!white`, which resolves to `#CCCCFF`.
  Neither value was what the source asked for. Sample the compiled page when
  checking a fill; do not trust the specification.
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
  The metric-comparison figure was rewritten this way — its caption had grown to four lines
  describing both panels, which is exactly the material the body text is for.
- **An axis label names which quantity is plotted, not its kind.** `Angle [°]`
  was the y-axis of the metric-comparison figure's first panel, where both curves are the
  alignment angle obtained two different ways, so the label left the reader to
  guess. It now reads `Pose-based alignment error [°]` and the legend separates the two
  routes to it.
- **Every numerical axis reads `Descriptive Name, Symbol [Unit]`, in Title
  Case.** The English description comes first so a reader who does not remember
  the symbol list can still read the figure; the symbol follows so the figure
  ties back to the notation; the unit closes it in square brackets. Settled
  examples: `Set-Up Rotation About \(t_1\), \(\Delta\theta_1\) [°]`,
  `Rotational Stiffness, \(K_{R,t_i}\) [N m/rad]`,
  `Cross-Axis Translational Stiffness, \(K_{p,t_j}\) [N/m]`,
  `Tangential CoC Position, \(r_{c,t_2}\) [mm]`,
  `Tangential CoC Position, \(r_{c,t_1}\) [mm]`,
  `Commanded Orientation Offset, \(\theta_{t_i}\) [°]`,
  `Commanded Normal Force, \(F_n\) [N]`,
  `Commanded TCP Moment About \(t_i\), \(M_{t_i}\) [N m]`.

  **Mathematical symbols keep their own casing.** Title Case applies to the
  English words only: \(t_1\), \(r_{c,t_2}\), \(K_{R,t_1}\) and \(F_n\)
  are never recased to match the surrounding capitals.

  **Time is singular and carries its symbol:** `Time, \(t\) [s]` for an
  ordinary controller or contact history, and
  `Time After Disturbance Onset, \(t_d\) [s]` wherever time is shifted so the
  disturbance begins at zero. Never `Times [s]`, and do not invent a third time
  symbol for one plot.

  Where no symbol is assigned to what the axis means, the words stay and the
  unit still closes the label — the Case-F comparison axis and the categorical
  axes are the standing examples.
- **A legend names the experimental condition, and gives its symbol and value
  where one exists:** `Descriptive Condition, Symbol = Value`. It never repeats
  the \(y\)-axis quantity and never carries a unit already on the axis.
  Settled forms: `Commanded Offset, \(\theta_{t_1}=+10^\circ\)` for a
  commanded condition; `Projected Damping, \(d_{\mathrm{null}}=2\,\mathrm{N\,m\,s/rad}\)`
  for a controller parameter; `CoC Position, \(r_{c,t_2}=+40\,\mathrm{mm}\)`
  and `CoC at TCP, \(r_{c,t_2}=0\)` for a compliance-centre position. A bare
  `+10°` or `40 mm` entry does not say what the number is, and is what this rule
  replaces.
- **An axis carries the symbol the symbol list assigns to the quantity.** A
  reader who has met \(r_{c,t_2}\) in the text should not have to work out that
  `Centre position along t_2` is the same thing. Where a symbol exists, the
  axis is that symbol and its unit; a descriptive phrase may stay in front of it
  where the symbol alone would be cryptic, as in
  `Cumulative projected null-space motion \(E_N\) [°]`. The pass that applied
  this set the axes to \(r_{c,t_1}\), \(r_{c,t_2}\),
  \(\Delta\theta_i\), \(\theta_{t_i}\), \(E_N\) and
  \(\Delta\sigma_{\min,\mathrm{dist}}\). The pose-based appendix comparison
  uses descriptive labels instead of promoting its local quantities to the
  thesis-wide symbol list.

  **Response axes pair words with the symbol.** Write `Measured set-up rotation
  about \(t_1\), \(\Delta\theta_1\) [°]`, not a bare symbol. A parameter axis
  likewise names the varied quantity before its symbol, for example
  `Rotational stiffness about the investigated tangent, \(K_{R,t_i}\)` or
  `Tangential CoC position along \(t_2\), \(r_{c,t_2}\)`. Wrench panels follow
  the same pattern: `Commanded normal force, \(F_n\) [N]` and `Commanded TCP
  moment about \(t_1\), \(M_{t_1}\) [N m]`.

  **Where no symbol is assigned to what the axis means, the words stay.** Three
  axes kept their prose for that reason: the supporting tool-axis comparison, whose \(x\)
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
