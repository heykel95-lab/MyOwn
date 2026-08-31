# First-plot Contact Establishment repeat

This repeat uses the same `P2_t1_pos_p000` configuration as the first
professor-email plot.  Its Contact Establishment gains are

- `Kp = [2000, 2000, 350] N/m`;
- `KR = [5, 5, 50] N m/rad`;
- automatic damping; and
- `r_c = [0, 0, 0] m`.

The zero lever makes the point-shift transform the identity, so the virtual
translation--rotation coupling is zero.

## Run

```sh
cd ~/Desktop/Thesis_Final_Control
./experiments/run.sh P2_t1_pos_p000 4
```

Select `s`.  Do not push or rotate the robot by hand.  The controller performs
Tool Orientation, Surface Approach and Contact Establishment automatically.
When the terminal prints `[GATE] Set up finished`, type `e` and press Enter to
stop before Grinding.  Wait for the archive confirmation.

## Analyse

```sh
cd ~/Desktop/MyOwn-thesis
python3 professoremail/analyse_contact_moment_diagnostic.py \
  ../Thesis_Final_Control/experiments/results/P2_t1_pos_p000/r04
```

The analysis writes the absolute TCP-referenced moment and the
clearance-referenced change as separate quantities.  It does not infer an
unmeasured pressure centre or local contact couple.
