# Main-presentation null-space plots in the thesis

These are the three shared plots on main presentation slides 23–25 and in
thesis Figures 5.9–5.11. The 2026-09-30 rendering matches the thin boxed axes,
inward ticks and Latin Modern labels of Figures 5.4 and 5.6. Figure 5.11 uses
equal panel widths and heights, aligned labels and identical 0–4 s intervals.
Its right panel retains the enlarged vertical scale. Curves, uncertainty bands,
colours, markers and numerical limits are unchanged. Both documents use the
same generated assets; the earlier synchronization audit remains below.

The grid follows Figure 5.7 throughout: light solid horizontal lines and
darker dotted vertical lines at the existing ticks. The sibling
`sources/results_grid.py` helper sets the colours and physical line weights.
Its copy under the parent figure directory must remain identical.

Run `python sources/make_nullspace_narrative.py` in an environment matching
sources/requirements-nullspace.txt, then copy the three generated PDFs into
figures/ch05. The sibling helper and compressed measured samples make the
default rebuild independent of the raw-log archive. Do not use `--refresh`
without adapting the original acquisition paths. The six-condition helper
retains its original documentation for provenance, while the thesis selects
only the four conditions listed in nullspace_narrative_analysis.json.

The generator renders both text and mathematics with LaTeX and `lmodern`,
using `latex` and `dvipng` from the local TeX installation. This avoids mixing
Latin Modern text with Matplotlib maths. Figures render at the final 160 mm
width, so the optical font sizes also match. Axis labels and ticks print at
10 pt, and legends at 8 pt, when included at the thesis text width. Keep the
generated PDF, PNG and SVG together and replace the matching embedded
presentation images when changing these figures. See styling_20260930.json
for data-invariance and document checks.
The follow-up ylabels_20260930.json records the exact font faces and printed
sizes in the final thesis, alongside the matching presentation update.

The old MAIN_NS_nullspace_automatic.pdf and joint_motion_time.pdf are archived
in figures/withdrawn/nullspace_20260921 and excluded from the thesis. No raw
measurements were removed. The raw-log verification, exact source hashes and
asset comparison are recorded in synchronization_20260921.json.
