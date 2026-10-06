"""Summarise peaks of the exact joint-1 means plotted in the main figure.

Use common recorded timestamps, onset-reference each trial, and average before
taking the absolute peak. No interpolation, smoothing, or new trial selection.
"""
import csv
import gzip
import hashlib
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'combined_joint_samples.csv.gz'
CONDITIONS = [
    'MAIN_NS7_baseline_20N_200mm',
    'MAIN_NS7_damping_2p0_20N_200mm',
    'MAIN_NS8_ksigma_2p0_20N_200mm',
    'MAIN_NS9_combined_ksigma_2p0_dnull_2p0_20N_200mm',
]


def calculate():
    with gzip.open(SOURCE, 'rt', newline='') as stream:
        rows = list(csv.DictReader(stream))
    results = []
    for condition in CONDITIONS:
        runs = []
        for repetition in ['r01', 'r02', 'r03']:
            run = [r for r in rows if r['condition'] == condition
                   and r['repetition'] == repetition]
            time = np.array([float(r['phase_time_s']) for r in run])
            angle = np.array([float(r['q1_deg']) for r in run])
            assert len(time) == 81 and time[0] == 5 and time[-1] == 9
            assert np.all(np.diff(time) > 0)
            runs.append((time, angle - angle[0]))
        common = runs[0][0]
        for time, _ in runs[1:]:
            common = np.intersect1d(common, time)
        values = np.array([angle[np.searchsorted(time, common)]
                           for time, angle in runs])
        mean = values.mean(axis=0)
        peak = int(np.argmax(np.abs(mean)))
        results.append({
            'condition': condition,
            'common_samples': len(common),
            'peak_abs_mean_deg': float(abs(mean[peak])),
            'peak_time_s': float(common[peak] - 5),
            'sample_sd_at_peak_deg': float(values[:, peak].std(ddof=1)),
        })
    for result in results:
        result['peak_reduction_vs_zero_percent'] = 100 * (
            1 - result['peak_abs_mean_deg'] / results[0]['peak_abs_mean_deg'])
    return {
        'source': SOURCE.name,
        'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'metric': 'Peak absolute pointwise three-trial mean joint-1 angle change',
        'display_interval_s': [0, 4],
        'interpolation': False,
        'smoothing': False,
        'conditions': results,
        'combined_peak_reduction_vs_conditioning_percent': 100 * (
            1 - results[3]['peak_abs_mean_deg'] / results[2]['peak_abs_mean_deg']),
    }


if __name__ == '__main__':
    report = json.dumps(calculate(), indent=2) + '\n'
    (HERE / 'joint1_peak_analysis.json').write_text(report, encoding='utf-8')
    print(report, end='')
