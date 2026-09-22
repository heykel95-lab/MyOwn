# Main-presentation null-space plots in the thesis

These are exact copies of the three plots on main presentation slides 20–22
as of 2026-09-21. Only the null-space experiment was synchronized. The other
thesis plots and all presentation files are unchanged.

Run `python sources/make_nullspace_narrative.py` in an environment matching
sources/requirements-nullspace.txt, then copy the three generated PDFs into
figures/ch05. The sibling helper and compressed measured samples make the
default rebuild independent of the raw-log archive. Do not use `--refresh`
without adapting the original acquisition paths. The six-condition helper
retains its original documentation for provenance, while the thesis selects
only the four conditions listed in nullspace_narrative_analysis.json.

The old MAIN_NS_nullspace_automatic.pdf and joint_motion_time.pdf are archived
in figures/withdrawn/nullspace_20260921 and excluded from the thesis. No raw
measurements were removed. The raw-log verification, exact source hashes and
asset comparison are recorded in synchronization_20260921.json.
