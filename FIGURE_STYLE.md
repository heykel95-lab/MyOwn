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
  \input{figures/<name>.tex}
  \caption{Short noun phrase.}
  \label{fig:<name>}
\end{figure}
```

`config/packages.tex` already loads `tikz` with `arrows.meta`, `calc` and
`positioning`, plus `siunitx` and `needspace`. Do not load packages from inside
a figure file or set a font family. The figure inherits the document's Latin
Modern; local size declarations may be used for labels.

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
- **Physical quantities and measured series are solid.** A dashed line is
  reserved for a configured, projected, modelled, or bounded reference when
  that distinction carries the meaning of the figure. Figure 1.1 therefore
  draws every physical or configured object solid -- the configured surface in
  red, the physical surface in blue, the tool face in green -- and reserves the
  dash for its one construction line. Never use a dash pattern merely to
  distinguish otherwise identical objects. A construction datum that carries a direction to
  where it is needed is **dashed black and thinner** than the objects compared
  against it, so it joins the black annotation layer rather than the coloured
  objects: Figure 1.1 draws its desired tool direction at \(0.8\,\mathrm{pt}\)
  against their \(1.1\,\mathrm{pt}\).

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

**A supporting figure uses the exact symbols defined beside it.** Use
\(f_{\mathrm{contact}}\) directly in the drawing and nearby definition; do not
expand it into paired action-direction aliases. Do not replace
\(M_{t_1,\mathrm{contact}}\) with a second action-direction index. The
professor-email contact figure uses \(f_{\mathrm{contact}}\),
\(r_{\mathrm{contact/TCP}}\), \(M_{t_1,\mathrm{contact}}\),
\(M_{t_1,\mathrm{cmd}}\), and \(M_{t_1,\mathrm{est}}\) in both the equations
and the drawing. Define the action side in prose once rather than encoding it
again through different symbols.

**Name an averaging interval, not only its final position.** When a value panel
shows means over the grey stationary interval, title it ``Stationary-interval
moment means'' rather than the ambiguous ``Endpoint signals''.

**Moment arcs sharing one point take disjoint sectors, and a radius apart where
a third is needed.** Two arcs about the same point drawn over the same sector
cross each other, their arrowheads collide, and the labels land on the wrong
arc; an arc drawn through the sector a lever or a face occupies crosses that
line as well. Give each moment its own sector — upper and lower for an
opposing pair, with the sum drawn at a smaller radius inside them where three
are shown — and place each label outside its own arc on the free side. Choose
the sectors after the levers are drawn, since it is the lever that decides
which directions are already taken. This was settled on the professor-email
moment figures, where the commanded and estimated arcs had been drawn across
the tool face, the plane and each other.

**A baseline-referenced wrench signal is not drawn as a physical moment acting
on the tool.** When a commanded moment is compared with a model-estimated
change from a stored baseline, place the two values on an axis with positive
and negative values or in separate value rows. Draw any preceding pose change
in a separate panel. This
prevents an endpoint signal from being read as the cause of the motion or as
an action--reaction pair.

**An unobserved contact point is schematic.** A contact-mechanism drawing may
show an effective point, its TCP lever and the resulting physical moment, but
the point is labelled `schematic` and carries no measured coordinate. The
selected geometric tool point is not substituted for an unobserved pressure
centre.

**A right-angle marker spans the two things it marks, and the rotation that
places it is the first of them.** The direction-rule figure drew its square
inside `\begin{scope}[rotate=\ra]`, where `\ra` is the *lever* direction, so
the square occupied the quadrant beyond \(r_{c,t}\) instead of the one
between \(\theta_{\mathrm{offset}}\) and \(r_{c,t}\) — in the `about t_1`
panel it sat between \(+t_2\) and \(-t_1\), where nothing is
perpendicular to anything. Rotating by the *first* of the two directions,
`\ua`, puts the local \(x\) axis on one vector and the local \(y\) axis on
the other, so the square lands between them. Corrected on 2026-08-27.

Where a third ray lies inside the marked angle — a surface tangent in the two
diagonal panels — it passes through the square. That is the geometry and is
left alone: the square is read against the two thick coloured vectors it spans,
and moving or shrinking it to dodge the axis would misplace the thing it
marks. Check the placement panel by panel in the compiled document, since a
marker drawn from a rotated scope is correct in three panels and wrong in the
fourth without anything warning.

### Routing

**Orthogonal only.** A diagonal line in a block diagram reads as a different
kind of connection and is almost always an accident.

**Every signal arrow in a block diagram carries a brief label.** Name the
quantity or physical transfer on the arrow itself, even when the neighbouring
boxes imply it. Use the established symbol where one exists and a short noun
phrase otherwise. Apply this to every arrow in the same diagram; partially
labelled signal paths make the unlabelled connections ambiguous.

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

**An arrow approaches a box from outside and ends on its boundary.** Never put
the penultimate routing coordinate inside the destination, since that reverses
the final segment and makes the arrowhead point back out of the box. Feedback
paths leave their source at the appropriate corner. Where a side connection
would otherwise share the exact midpoint, place it slightly above or below the
midpoint while keeping the endpoint on the box border.

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

**Every in-figure name occupies one line at most.** Use the shortest
unambiguous noun phrase or an established symbol, and never wrap a name across
two lines. Any additional line may contain only a symbol, value, short
instruction, or qualifier. Put definitions and explanatory wording in the
caption or body text instead of lengthening a box, line label, panel label, or
annotation. Shortening must preserve distinctions that carry the figure's
meaning. Use `Configured reference` rather than the longer `Configured surface
reference`. `Configured surface` is permitted only in a shared legend that
also names the contrasting `Physical surface`, as in Figure 1.1; elsewhere it
can be mistaken for the physical surface.

### Scale the picture, do not resize it

**A TikZ diagram is sized by `scale=` inside `\begin{tikzpicture}[...]`, not by
wrapping the `\input` in `\resizebox`.** `scale=` moves the coordinates and
leaves node text at the size it was declared; `\resizebox` magnifies the text
along with the drawing, so a diagram drawn at 7 cm and stretched to the text
width comes out with labels about twice the size of the body text. It also
multiplies every clearance, which is how a label that looked separated in the
source ends up on an arrowhead.

This was found on the three Chapter 3 diagrams, where the symbols were visibly
larger than the surrounding prose and two labels overlapped each other. Draw the
picture at whatever size is convenient, then pick the `scale=` that brings it to
the width it should occupy, and include it with a plain `\input`.

The rule holds in the other direction too. A wide diagram shrunk to fit by
`\resizebox` has labels *smaller* than the body text, which is the same fault
and is easier to miss.

**Explanatory sentences do not go inside the picture.** A two-line note added
beside a diagram widens its bounding box, and `\resizebox` then shrinks the
whole drawing to fit the page, so the geometry becomes unreadable to buy room
for prose that belongs in the body text. Keep the drawing to the geometry and
its symbols; say the rest in the paragraph before or after it.

**Flow-chart boxes and conditions stay short.** A box contains only the state
name, never an explanatory sentence or paragraph. Write each transition as a
brief `if` condition and use a symbol already defined in the thesis when that
makes the condition shorter. Put the condition beside a clear arrow segment,
not over the line or a box border. Short display labels such as `Pre-Contact
Hold` and `Pre-Grinding Hold` may stand for longer state names that the body
text gives in full. The Tool Orientation arrow carries
\(\theta_{\mathrm{app,err}}\leq\varepsilon_{\mathrm{app}}\lor\)
the `8.0 s timeout`; the worded form `angular error within
tolerance` is withdrawn, because Section 3.3 now defines both symbols.
**A disjunction in a chart condition is written \(\lor\), never the word
`or`**, so that one drawing states the same relation one way: the shared stop
condition already read `if stop requested \(\lor\) robot error/reflex`, and
the orientation condition was the only place left carrying the word. The orientation condition is set on one
line: it measures \(3.73\,\mathrm{cm}\) against the \(4.07\,\mathrm{cm}\)
between its anchor and the stop rail, so it needs `text width=3.90cm` to
override the \(3.8\,\mathrm{cm}\) the `cond` style would otherwise wrap it
at. Where \(\lor\) does end a line, as in the stop condition, it needs an
explicit space before it, since TeX gives a trailing binary operator none.
The Contact Establishment arrow uses `5.0 s timeout`. The body text
retains the complete minimum-time, orientation, moment-change and timeout
logic. Put the clearance condition beside the direct arrow into Pre-Contact
Hold.
Keep Pre-Contact Hold and Pre-Grinding Hold on the single main path. Do not draw
or label separate `hold enabled` and `hold disabled` branches; the body text
explains that a disabled hold advances without waiting. Operator confirmation
labels the outgoing arrow from each hold.

**A stop condition names the principal event rather than saying `fault`.** The
shared controller-chart label reads only `stop requested` or `robot
error/reflex`; the body text carries the run-duration limit and application-side
exceptions. In the program-level chart, the shared rail descends through the
centre into Stop. Place its short label beside that vertical path so the text
does not interrupt the arrow. A recovery-failure label sits over the
unobstructed left part of its own path, away from the controller-selection
branches and the Contact Sequence box. Its vertical red rail remains
visibly left of that box and never touches its border.

**A label is never filled.** A white fill behind the text erases whatever it
sits on, and on a label placed `above` a run it erases the top of that run, so
the connection reads as broken exactly where the reader is looking for its
name. Give the label room instead.

If a label crowds something, move the run rather than nudging the label. The
spacing between runs is what creates room for their labels.

### Node text begins with a capital

Every line of text inside a box starts with an uppercase letter — `Tool face
seated flat`, `Record one EE pose`, `Estimate the tool-face normal`. This applies to the
second line of a two-line node as well, because the two lines read as parallel
labels rather than as a sentence running on.

**Write the lines as parallel labels, not as one sentence broken across
them.** `Tool face seated flat on the surface; record one EE pose` forces the
second line to open in lower case or to be recased into nonsense. Two label
lines, `Tool face seated flat` and `Record one EE pose`, satisfy the rule and
read better.

**A line that begins with a symbol keeps the symbol**, unchanged and
uncapitalised: `$T_1$--$T_3$`, `$p_s,\ R_{\mathrm{surface}}$`,
`$\varepsilon_{\mathrm{plane}}$`, `$0.50^\circ$`. Notation is not prose and
must not be recased to satisfy a typographic rule.

The same holds for row headings and for a label placed beside an arrow, except
that a bare symbol carried by an arrow — `$n_{\mathrm{EE}}$`, `$n_s$` — is
notation and stays as it is.

Widening a box to fit a capitalised or lengthened line can close the gap its
arrows need. Move the columns apart rather than shortening the text, and check
the arrow runs in the compiled figure afterwards.

### Fixing a box width: use `text width`, not `minimum width`

`minimum width` sets a floor and lets a long line push past the frame, so the
text overflows the rounded rectangle and adjacent boxes collide.

Set `text width` instead. It fixes the box width and wraps the content inside
the frame, so a box can only grow downwards, which the row spacing can absorb.
Then check the line count of every box in the row: a box with one more line
than its neighbours is taller, and it is what reaches the row heading above it.
Where an equation is too wide for the column, set that line in `\scriptsize`
rather than widening one box out of line with the others.

### A diagram of parallel chains names each chain

Where a diagram runs two or more chains as separate rows, each row carries a
short heading naming what it produces. Put the heading above the row rather
than in a label column, which widens the picture and reduces the available
space for the diagram itself. A heading must not overstate what the row
establishes.

**Delete a complete diagram when it only repeats adjacent prose.** The former
Chapter 4 calibration flowchart repeated the procedures stated immediately in
Sections 4.2.1 and 4.2.2 and was removed. A cleaner redraw would not have added
information, so the figure must not be restored without a new conceptual
distinction that requires a visual explanation.

### What does not belong in the drawing

- An internal title. The caption identifies the figure; a title repeats it.
- A legend inside a narrow panel, where it lands on the data or an axis label.
- Anything not discussed in the text.

**The Chapter 3 selected-tool-point figure shows principal outcomes rather than
an exhaustive case set.** Its three panels are the leading corner,
leading-edge midpoint and tool-face centre. The tolerance-based selector can
also admit a three-corner group, so neither the drawing nor its caption claims
that these are the only possible groups. The visible caption and
List-of-Figures entry are both `Principal selected tool points for the
rectangular tool face.`; the panel labels name the three outcomes. Every panel draws the minimum tool height
\(h_{\mathrm{Tool}}\) as a green dimension from a minimum-height corner to its
projection on the configured surface. The black \(-n_s\) arrow remains the
approach-direction marker and is not used as the height dimension.

**The Chapter 3 controller flow uses two state-machine drawings.** The first
starts directly with Robot Recovery and then shows Controller Selection, followed by the
Contact Sequence, Cartesian Pose Hold, Contact-Impedance Hold and Manual Guidance
branches. Label these selections `if operator types s`, `if operator types h`,
`if operator types t`, and `if operator types g`, respectively, so the drawing
exposes the implemented keyboard mapping. The second
shows the surface-contact states from Tool Orientation through Grinding. Its
common start is the blue rectangular box `Move to Stored
\(q_{\mathrm{init}}\)`, whose orthogonal path enters the top edge of Tool
Orientation and reads `\(q_{\mathrm{init}}\) reached`. **The
`Initial Configuration` box is withdrawn**, as of 2026-08-31, and so is the
separate `start sequence` arrow that followed it. The box named the value the
robot moves to and the arrow named the motion, which put a stored parameter and
a reached configuration in the same column and left the reader looking for what
performed the move. One box now performs it, named for the function that does
so, and the arrow carries the arrival condition like every other arrow in the
chart. **Manual Guidance is not drawn as a second route into the sequence**,
withdrawn on the same day together with its `s: start` label: the box carries
the runtime interaction only, so `g` enters Manual Guidance from an active
contact sequence and `p` recaptures the reached pose and restarts at Tool
Orientation. Section 3.2 still states that `s` starts the sequence from the
current guided configuration. **Contact-Impedance Hold is drawn as a state, in the same black capsule as
the sequence states**, on the left return branch beside the contact-state
column. It was a blue rectangle until 2026-08-31; that made the one chart
disagree with Figure 3.1, which had always drawn it as a state, and it is a
controller state in the implementation, entered by input `t` and holding the
captured Cartesian pose under its own impedance. Its
incoming arrow states that `t` enters it from the contact sequence. Its name is
\(3.83\,\mathrm{cm}\) wide, so this capsule alone carries
`text width=3.95cm` rather than the shared \(3.80\,\mathrm{cm}\); the
adjustable parameter families sit in a label beneath it rather than on a second
line inside it, so the capsule keeps the state height the other six use. It holds
the captured Cartesian pose while \(K_p\), \(K_R\), or \(r_c\) is set, then
returns to Tool Orientation on an outgoing arrow labelled `s: start sequence`.
**No Manual Guidance box is attached to that loop.** Withdrawn on 2026-08-31
with its `g` and `p` connectors: guidance from the hold is a runtime
interaction the body text carries, and drawing it a second time doubled the
box and crowded the column. Keep the `s` and `t` labels immediately beside the
Contact-Impedance Hold loop; a long return rail with an isolated condition
label is not acceptable.
`State` is the canonical node term, and the contact-press state is `Contact
Establishment`; no alternative state name is used.

**The Chapter 4 surface-reference geometry keeps three orientations distinct.**
The physical surface is blue, the configured surface reference is red, and the
tool face at the start of Contact Establishment is dark green. The inner arc
shows the achieved pose-based initial angular offset \(\theta_{0,t_1}\), drawn from the
configured reference to the achieved tool face. No angle is drawn from the
physical surface, and no symbol is assigned to its unknown difference from the
configured reference. The drawing is a principal-tangent cross-section and
carries no numerical value.

**The Chapter 1 surface-entry concept figure is one first-reader cross-section.**
It separates two contributions to the angular relation at surface entry, and
**each contribution carries its own arc and its own label.** The solid red
line is the configured surface. The solid blue physical surface has a potential
difference from it, marked by a black arc labelled `Configured--physical
difference`. The desired parallel tool direction is drawn separately, as a
black dashed datum through the tool, and the dark-green tool face lies at a
schematic angular difference from it, marked by a second black arc labelled
`Desired--achieved difference`. The two labels are parallel in form because
they name the two contributions the figure exists to separate.

**The configured surface is drawn as a continuous line.** Agreed 2026-09-01,
superseding the dashed red line the figure carried until then. Once the
desired-direction datum was added, the drawing held two dashed elements and the
dash no longer said anything: it is now the property of the one construction
line in the figure, and the three objects are separated by colour alone, which
the legend names. The general rule above was rewritten to match.

**The desired direction is not drawn in red.** It was carried by the red dashed
line until 2026-09-01, which left the achieved--desired contribution as an
unmarked tilt while the other contribution had an arc and a name. Repeating the
red dash at the tool would state the relation correctly and still read as a
second configured surface, so the datum is black and takes the colour of the
arcs that annotate it. Nothing in the legend changes: the legend names the
three objects, and a construction datum is not one of them.

The tool tilt is drawn at \(10^\circ\) against the physical surface's
\(19^\circ\). Both are schematic. The tilt was \(6^\circ\), which is too
shallow to mark: its arc compiled as a tick that read as a stray mark rather
than an angle. Keep the tool angle visibly smaller than the physical one, so
the drawing does not suggest the two contributions are equal, and visibly large
enough for an arc. The figure contains no panel letters, local tangent-axis
symbols, angular quantity symbols, or numerical angles. A single legend above
the geometry names `Configured surface`, `Physical surface`, and `Tool face`.

**The three Chapter 3 flowcharts use one visual grammar.** Figures 3.1, 3.3 and
3.7 draw every operating or controller state as the same black rounded capsule.
Operator input, initialisation, capture, selection and selectable
controller configurations use blue rectangular boxes. Normal state progression
uses black arrows, operator and tuning paths use blue arrows, and stop or
failure paths use red arrows. Conditions are written directly beside clear
arrow segments rather than placed in decision diamonds. The three drawings use
the same text size, arrowhead size, border weight and state height.

Figure 3.7 treats Cartesian Pose Hold as the controller state. Its four
null-space modes are blue configuration boxes rather than additional states.
Figure 3.2 is not part of this state-chart grammar: it uses ordinary black
rectangular functional blocks and crossed circular junctions.

**A crossed junction's cross spans the whole circle.** Draw it between opposite
node anchors — `(sum.45) -- (sum.225)` and `(sum.135) -- (sum.315)` — so each
arm ends exactly on the circumference at whatever diameter the circle is given.
A cross drawn from fixed offsets about the centre shrinks to a mark floating
inside a large ring, which is what the first version of Figure 3.2 showed.

**Every sign sits inside the circle, in the wedge its own arrow points into,
and every arrow points at its own sign.** The reference input, the feedback
input and each additive torque term therefore arrives on the radius that leads
to its sign, so a reader traces the arrow inward and meets the sign that
qualifies it. An input must land inside a wedge and never on an arm of the
cross: the two additive terms of Figure 3.2 enter at \(115^\circ\) and
\(65^\circ\), not at \(135^\circ\) and \(45^\circ\).

**The junction diameter is set by what its fullest wedge has to hold, not
chosen first.** Where two signs share one wedge they must clear both arms and
each other, which fixes a lower bound: at `\scriptsize` a
\(+\) is about \(2\,\mathrm{mm}\) across, and Figure 3.2's torque
junction needs \(1.25\,\mathrm{cm}\) for two of them in the top wedge.
Junctions at \(0.80\) and \(1.10\,\mathrm{cm}\) were both tried and both
put a sign on an arm. Keep the junction visibly smaller than a functional
block, and check the fit in the compiled figure rather than in the
coordinates — the arithmetic is close enough that it has to be seen.

The junction name goes on the side no signal uses, and never where a path runs
through it.

Figures 3.1, 3.3 and 3.7 are structurally settled. Do not redesign them or add
further conditions and controller detail; their deliberate simplification is
part of the final visual hierarchy.

Every arrow carries its transition condition. A shared red termination rail
may carry conditions that apply from every active state, provided the
accompanying text names those conditions explicitly. Keep that rail thinner
than the main progression so it does not dominate the state sequence. Use a
red capsule for Stop. **The chart carries no `Reported endpoint` marker.**
Withdrawn on 2026-08-31: the drawing shows the implemented state machine, and
which state the campaign stopped in is a result rather than a transition. The
body text states it in Sections 3.2 and 5.2 and in the Grinding entry of the
state list, so nothing is lost by removing it from the figure. Source identifiers and numerical gain-group annotations stay out
of both state-machine drawings; the Contact-Impedance Hold loop names only the
adjustable parameter families \(K_p\), \(K_R\), and \(r_c\).

**Figure 3.2 is drawn as a classical Cartesian feedback loop.** Its functional
blocks remain ordinary rectangles and do not use the capsule state shape.
Cartesian Error and Torque Sum are crossed circular junctions rather than
rectangles. The error junction marks the desired-reference input with `+` in
the left wedge and the measured-feedback input with `-` in the lower wedge.
Every input to the torque junction is marked `+`. A block names only the operation; the arrow names the transmitted
signal. Every connection leaves and enters a rectangular block perpendicular
to that block's border. A route may turn only after this normal segment; no
connection starts at a rectangle corner or departs diagonally. The dominant
path reads from left to right as Cartesian Error, the Cartesian impedance
controller, the Jacobian-transpose mapping, Torque Sum and Joint Motors.
`Robot / Joint Motors` was shortened on 2026-08-31: the block is the actuated
hardware the torque command reaches, and `Robot` added a second name for it.
The feedback arrow out of it reads `Joint motion sensors`. The compact visible labels `Impedance Controller` and \(J^\top F\)
are used where the full names would close the gaps between blocks; the mapping
block names the operation it performs rather than being called `Mapping`, which
is shorter and leaves the width the junctions need. A Desired Cartesian
Reference enters the error junction **from the left**, so that the dominant
path is one straight run and the feedback is the only input arriving from
below. This ordering
must be readable before any secondary branch is followed.

The desired-reference arrow carries \(p_d\), \(R_d\), and \(\dot p_d\). The
measured Cartesian feedback carries \(p_{\mathrm{EE}}\),
\(R_{\mathrm{EE}}\), \(\dot p_{\mathrm{EE}}\), and
\(\omega_{\mathrm{EE}}\). The main controller path exposes
\((e_p,e_R)\to F\to\tau_{\mathrm{cart}}\to\tau_{\mathrm{cmd}}\). Do not add
a commanded angular velocity: the implemented rotational damping acts against
the measured \(\omega_{\mathrm{EE}}\).

Robot Model and Null-Space Term are secondary blocks. The measured joint state
\(q,\dot q\) enters the model; the model supplies \(J(q)\) to the
Jacobian-transpose mapping and \(\tau_c(q,\dot q)\) to Torque Sum. A short
robot-state/model input supplies the Null-Space Term, which contributes only
\(\tau_{\mathrm{null}}\) to Torque Sum. Do not expand this branch with the
SVD, \(N_\tau\), \(v_7\), \(k_\sigma\), or other Chapter 2 details.

Sensing and modelling remain distinct. The end-effector pose and velocities
come from the robot state rather than being reconstructed by the Robot Model,
and sensing is not presented as a model transformation from torque to joint
angle. Keep the control frequency out because the whole drawing is one loop.
Every arrow is labelled, every secondary route stays visually subordinate, and
every box, arrowhead and label retains visible separation after compilation.

**Figure 4.1 does not identify the configured normal with the physical plane.**
Panel (b) draws the physical surface and its conceptual normal
\(n_{\mathrm{phys}}\) separately from the configured surface reference and its
frame \((t_1,n_s)\). It assigns no measured angle to the unknown difference.

**Figure 4.2 is the only calibration-related figure retained in Section 4.2.**
It shows the distinction between the configured reference, the unmeasured
physical surface and the contact-entry angle. The separate calibration
flowchart is withdrawn because it duplicated the two procedure subsections.

The upper selection block is named `Controller State`. Do not append `Logic`.
Its outgoing arrows show its parameter-selection role without another word in
the box. Main-row blocks retain conspicuous gaps in the compiled page; short
connectors squeezed between neighbouring boxes are not acceptable.

**The Chapter 3 Cartesian pose-hold diagram shows the four operator-selectable
modes.** Use the same
initialisation motif as the surface-contact chart: one blue `Move to Stored
\(q_{\mathrm{init}}\)` box leads into `Capture Current EE Pose` on an arrow
reading `\(q_{\mathrm{init}}\) reached`. Its `Initial Configuration` box,
the `start hold` arrow, the guided start route and its `h: start` label are all
withdrawn as of 2026-08-31, matching the surface-contact chart. Runtime
input `g` enters Manual Guidance from Cartesian Pose Hold, while `p` recaptures
the reached configuration and pose before returning through pose capture.
Runtime recapture is not specific to pose hold; the same `g` then `p`
interaction restarts an active surface-contact sequence at Tool Orientation.
**Manual Guidance is drawn as a state, in the same black capsule as the
sequence states, and carries its name and nothing else** in both charts.
`Enter with g` is withdrawn, because the incoming `g: guide` arrow already
states how the state is entered; the blue rectangle is withdrawn too, on
2026-09-01, for the reason that retired the blue Contact-Impedance Hold — it is
a controller state, and Figure 3.1 had always drawn it as one. Its name is
\(2.71\,\mathrm{cm}\) wide, so both capsules carry `text width=2.90cm`
rather than the width their chart gives the sequence states: the routes that
leave and enter Manual Guidance run close to its sides, and a full-width
capsule would swallow the turn each of them needs. The
path then captures the current end-effector pose and enters Cartesian Pose
Hold, on an arrow that states the assignment the capture makes,
\(p_d=p_{\mathrm{EE}}\) and \(R_d=R_{\mathrm{EE}}\), on two lines. The
bare pair \(p_d,R_d\) was replaced on 2026-08-31 because it named the
quantities without saying where they came from. **The reference is assigned
from the measurement, never the reverse**: the controller sets
`p_start = p_EE` and `R_d = R_EE`, so writing
\(p_{\mathrm{EE}}=p_d\) would state position control rather than the capture
of a hold reference. Cartesian Pose Hold
uses the shared black capsule state shape; pose capture,
operator selection and the four modes use blue rectangular configuration boxes.
Operator input 0, 1,
2, or 3 selects no
null-space torque, projected damping, singular-value conditioning, or both
terms together. The selector remains active, so entering another number
switches directly from any active mode to the selected one. Mode 1 exposes
\(d_{\mathrm{null}}\), mode 2 exposes \(k_\sigma\), and mode 3 exposes both.
Keep the numerical mapping visible and distinguish the selectable software
modes from the four settings compared experimentally. Do not replace mode 3
with a second conditioning-gain setting. The compact box descriptions are
`No Null-Space Torque`, `Damping`, `Conditioning`, and `Together`; each stays
on one line. `No Torque` was withdrawn on 2026-08-31 as inaccurate: Mode 0
switches off the null-space contribution alone, and the Cartesian torque is
still commanded. Keeping the name on one line fixes the mode boxes at
\(3.45\,\mathrm{cm}\), which is what sets their spacing.

## Generated plots (matplotlib)

Plots come from the scripts in `analysis/` in the controller repository, are
written to its `figures/` directory, and are copied into `figures/` here as
vector PDF.

**The active contact-result plots report configured orientation offsets about
\(t_1\) only.** Remove every \(\gamma_{t_2}\), \(\theta_{0,t_2}\), and
configured-orientation-offset-about-\(t_2\) series from figures included by the thesis. The symbol
\(t_2\) remains on an active plot only when it is the perpendicular input
coordinate of a \(t_1\) experiment, such as \(K_{p,t_2}\) or
\(r_{c,t_2}\). Archived, non-included figure files and raw data are not
deleted by this reporting-scope decision.

**The archived direction-comparison plot uses the configured-offset name.** Its
horizontal axis reads `Configured Orientation-Offset Direction,
\(\theta_{\mathrm{offset}}\) [°]`. The withdrawn commanded-rotation wording and
\(\theta_{\mathrm{cmd}}\) symbol must not return when the plot is regenerated.

**Figure 5.3 uses the same \(0^\circ\) to \(10^\circ\) response scale as
Figure 5.2.** Its measured span is only \(0.03^\circ\), so a narrow axis around
the three means would visually exaggerate the cross-axis stiffness effect.

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
generator at all. The active Case-A, Case-B, Case-C and Case-D figures and the
supporting tool-axis comparison are drawn directly in `pgfplots` from the
values in their own tables. They are `\input` as `.tex`, so they take the document font and
need no `
esizebox`.

This is not a licence to invent data. **The only numbers a redrawn figure may
contain are ones already reported in the thesis**, and where the table carries
standard deviations they are drawn as error bars, as in the supporting
tool-axis series.

The main Case-D plot carries the sample standard deviation at every setting as
an error bar. The earlier `MAIN_D_sign.pdf` appendix plot duplicated that
information and is not included in the thesis.

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

**Every visible figure caption occupies one rendered line at most, and its
List-of-Figures entry does the same.** Shorten the name to the plotted
quantity, comparison, geometry, or parameter set. Move panel descriptions,
procedures, interpretations, and qualifications into the surrounding text. A
concise list entry does not compensate for a multi-line caption beneath the
figure, and a short visible caption does not permit a wrapped list entry.

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
| `MAIN_G_magnitude.pdf` | Supporting initial angular-offset magnitude check; retained file identifier |
| `MAIN_F_toolaxis.pdf` | Supporting tool-axis check; retained file identifier |
| `MAIN_H_direction.pdf` | Withdrawn intermediate-direction check; retained archive identifier |
| `MAIN_DQ_descent.pdf`, `MAIN_DQ_metric_comparison.pdf`, `MAIN_DQ_metric_summary.pdf` | Data quality |
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

  **A single bar series is blue, not black.** The curve rule starts at black
  and the bar rule starts at blue, and a lone bar series follows the bar rule:
  the Case-A bars set the precedent, and the net-displacement panel of the
  null-space figure follows it. A filled black bar prints as a block of ink
  where a black curve prints as a line.

- **Print the value above each bar where the series spans orders of
  magnitude.** The net redundant displacement runs from \(0.131\) rad down to
  about \(10^{-4}\), so on a linear axis the two conditioning bars are the
  height of the axis line — which is the finding, but leaves a reader unable to
  tell a suppressed value from a missing one. The printed value resolves it
  without a second axis. A log axis does not: one of the four values is
  negative, and taking magnitudes would discard the sign the quantity exists to
  carry. The Case-A bars print their values for the same reason, so the two bar
  figures agree. Choose the precision from the values rather than fixing one
  format — three decimals above \(0.01\) and four below it keeps `0.131` and
  `0.0003` both readable — and write the sign with the typographic minus the
  tick labels use, not an ASCII hyphen.

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
- **A time series is drawn at a bounded number of points.** A contact-establishment log holds
  about five thousand samples and a panel is a few centimetres wide, so the
  full rate paints a band rather than a curve. Around nine hundred points keeps
  a curve legible at printed width.
- **A time-history figure says whether a trace is one repetition or an
  average**, in the body text where the figure is introduced. Every other
  figure in the thesis plots a mean over three repetitions, so a reader meeting
  a time history assumes the same unless told otherwise. `plot_coc_case.py`
  takes named trials on the command line and the reported Case-D mechanism
  figure passes `r01` of each condition, so its three curves are one recorded
  repetition each, and Chapter 5 states that. This is provenance rather than
  uncertainty: it goes in the text, not in the caption, which stays a short noun
  phrase.
- **Grid is horizontal only.** It exists to compare values across panels.
- **Every plotted series is identified by one legend below the complete plot.**
  The Chapter 5 plots and the supporting comparison in Appendix D place a
  borderless, transparent legend centrally below the axes and above the figure
  caption. Multi-panel figures use one figure-level legend, including when
  different panels contribute different entries. A legend never occupies an
  axis, and a white cover is never placed over the data. Check the rendered
  figure, because the space required by a long entry changes when the plot is
  scaled.
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
  `pgfplots`. The caption then names what the figure shows and stops; what each
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
  examples: `Contact-Establishment Rotation About \(t_1\), \(\gamma_{t_1}\) [°]`,
  `Rotational Stiffness About \(t_1\), \(K_{R,t_1}\) [N m/rad]`,
  `Cross-Axis Translational Stiffness, \(K_{p,t_2}\) [N/m]`,
  `Tangential CoC Position, \(r_{c,t_2}\) [mm]`,
  `Achieved Initial Angular Offset, \(\theta_{0,t_1}\) [°]`,
  `Commanded Normal Force, \(F_n\) [N]`,
  `Commanded TCP Moment About \(t_1\), \(M_{t_1}\) [N m]`.

  **Figure 5.5 uses the first form exactly on its upper axis.** `Set-Up
  Rotation About \(t_1\)` is withdrawn from the plot; the axis reads
  `Contact-Establishment Rotation About \(t_1\), \(\gamma_{t_1}\) [°]`.

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
  Settled forms: `Achieved Initial Offset, \(\theta_{0,t_1}=+9.32^\circ\)` for an
  achieved contact-entry condition; `Projected Damping, \(d_{\mathrm{null}}=2\,\mathrm{N\,m\,s/rad}\)`
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
  this set the active contact axes to \(r_{c,t_2}\),
  \(\gamma_{t_1}\), \(\theta_{0,t_1}\), \(E_N\) and
  \(\Delta\sigma_{\min,\mathrm{dist}}\). The pose-based appendix comparison
  uses descriptive labels instead of promoting its local quantities to the
  thesis-wide symbol list.

  **Response axes pair words with the symbol.** Write `Measured contact-establishment rotation
  about \(t_1\), \(\gamma_{t_1}\) [°]`, not a bare symbol. A parameter axis
  likewise names the varied quantity before its symbol, for example
  `Rotational stiffness about \(t_1\), \(K_{R,t_1}\)` or
  `Tangential CoC position along \(t_2\), \(r_{c,t_2}\)`. Wrench panels follow
  the same pattern: `Commanded normal force, \(F_n\) [N]` and `Commanded TCP
  moment about \(t_1\), \(M_{t_1}\) [N m]`.

  **Where no symbol is assigned to what the axis means, the words stay.** Three
  axes kept their prose for that reason: the supporting tool-axis comparison, whose \(x\)
  carries a tangential displacement on one series and a tool-axis displacement
  on the other, so no single component symbol covers it; the categorical axis of
  the Case-A bars, whose ticks name three different initial conditions that no
  one symbol spans; and the time
  axes, which the author prefers as they read. Do not invent a symbol to
  satisfy this rule.

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
- the figure has no internal title and its caption is a one-line noun phrase.
