#!/usr/bin/env python3
"""Typeset the A--D calibrated-normal angular-error endpoint comparisons.

Reads grouped results produced from archived terminal endpoints (0.01 degree
recording precision). Every point is the mean endpoint error over three repetitions and every
error bar is the sample standard deviation. No subtraction of finite rotation
angles is used. The saved sources are included directly by the thesis.
"""
import argparse
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent

def load_summary(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        groups = {r['run_id']: r for r in csv.DictReader(f)}
    return groups

def fvalue(groups, run, column):
    row = groups[run]
    if int(row['n']) != 3:
        raise ValueError(f'{run}: expected exactly three repetitions')
    return float(row[column])

def point(groups, run, x):
    mean = fvalue(groups, run, 'final_t1_deg_mean')
    sd = fvalue(groups, run, 'final_t1_deg_sd')
    return f'  ({x},{mean:.9f}) +- (0,{sd:.9f})'

YLABEL = r'Angular Error About \(t_1\), \(\theta_{\mathrm{err},t_1}\) [\(^\circ\)]'
COMMON = r'''    ymajorgrids=true, xmajorgrids=false,
    grid style={gray!25, very thin},
    tick label style={font=\footnotesize},
    label style={font=\footnotesize},
    legend style={font=\scriptsize, draw=none, fill=none,
                  cells={anchor=west}, at={(0.5,-0.24)}, anchor=north},
    every axis plot/.append style={thick, mark size=2.3pt},
'''

def make_sources(groups):
    sources = {}
    a_runs = ['P6_zero_p000', 'P2_t1_pos_p000', 'P2_t1_neg_p000']
    ticks = ', '.join(r'\('+f'{fvalue(groups,r,"entry_t1_deg_mean"):.2f}'+r'\)' for r in a_runs)
    a = r'''% Generated from the archived contact-error endpoint summary.
% Values are means with sample standard deviations over three repetitions.
\begin{tikzpicture}
\definecolor{barblue}{HTML}{0057B8}
\begin{axis}[
    width=9.5cm, height=6.2cm,
    ybar, bar width=14pt,
    xtick=data, symbolic x coords={none,p10t1,m10t1},
    xticklabels={@TICKS@},
    ymin=0, ymax=2.4, ytick={0,0.5,1,1.5,2},
    xlabel={Measured Angular Offset, \(\theta_{\mathrm{meas},t_1}\) [\(^\circ\)]},
    ylabel={@YLABEL@},
    nodes near coords,
    nodes near coords style={font=\scriptsize, yshift=5pt, /pgf/number format/fixed,
                             /pgf/number format/precision=2},
@COMMON@  ]
\addplot[draw=black, fill=barblue, error bars/.cd, y dir=both, y explicit]
coordinates {
@POINTS@};
\end{axis}
\end{tikzpicture}
'''
    sources['results_case_a_bars.tex'] = a.replace('@TICKS@', ticks).replace('@POINTS@', '\n'.join(point(groups,r,x) for r,x in zip(a_runs,['none','p10t1','m10t1'])))
    line = r'''% Generated from the archived contact-error endpoint summary.
% Each point is a mean with sample standard deviation over three repetitions.
\begin{tikzpicture}
\begin{axis}[
    width=12.5cm, height=7.0cm,
    @LIMITS@, ymin=0, ymax=10,
    xtick={@XTICKS@}, ytick={0,2,4,6,8,10},
    xlabel={@XLABEL@},
    ylabel={@YLABEL@},
@COMMON@  ]
\addplot[black, mark=o, mark options={fill=white},
         error bars/.cd, y dir=both, y explicit] coordinates {
@POINTS@};
\addlegendentry{Measured Angular Offset, \(\theta_{\mathrm{meas},t_1}=(@ENTRYMIN@\text{--}@ENTRYMAX@)^\circ\)}
\end{axis}
\end{tikzpicture}
'''
    for key,runs,xs,limits,xlabel in [
        ('b',['P2_t1_pos_p000','A_rot_t1_15','A_rot_t1_50'],[5,15,50],'xmin=2, xmax=53',r'Rotational Stiffness About \(t_1\), \(K_{R,t_1}\) [N\,m/rad]'),
        ('c',['B_trans_t1_0300','B_trans_t1_0800','P2_t1_pos_p000'],[300,800,2000],'xmin=220, xmax=2080',r'Translational Stiffness Along \(t_2\), \(K_{p,t_2}\) [N/m]')]:
        entry = [fvalue(groups,r,'entry_t1_deg_mean') for r in runs]
        text = line.replace('@LIMITS@',limits).replace('@XTICKS@',','.join(map(str,xs))).replace('@XLABEL@',xlabel).replace('@POINTS@','\n'.join(point(groups,r,x) for r,x in zip(runs,xs))).replace('@ENTRYMIN@',f'{min(entry):.2f}').replace('@ENTRYMAX@',f'{max(entry):.2f}')
        sources[f'results_case_{key}_stiffness.tex']=text
    d=r'''% Generated from the archived contact-error endpoint summary.
% Error bars show sample standard deviations across three repetitions.
\begin{tikzpicture}
\begin{axis}[
    width=11.5cm, height=7.0cm,
    xmin=-88, xmax=88, ymin=-11, ymax=11,
    xtick={-80,-40,-20,-10,0,10,20,40,80}, ytick={-10,-8,-6,-4,-2,0,2,4,6,8,10},
    xlabel={Tangential CoC Position, \(r_{c,t_2}\) [mm]},
    ylabel={@YLABEL@},
@COMMON@  ]
@SERIES@
\end{axis}
\end{tikzpicture}
'''
    series=[]
    for sign,colour,marker in [('pos','black','o'),('neg','blue!55!black','square')]:
        runs=[f'P2_t1_{sign}_{suffix}' for suffix in ['m080','m040','m020','m010','p000','p010','p020','p040','p080']]
        entry=f'{sum(fvalue(groups,r,"entry_t1_deg_mean") for r in runs)/len(runs):.2f}'
        points='\n'.join(point(groups,r,x) for r,x in zip(runs,[-80,-40,-20,-10,0,10,20,40,80]))
        series.append(r'\addplot['+colour+', mark='+marker+r''', mark options={fill=white},
         error bars/.cd, y dir=both, y explicit] coordinates {
'''+points+'};\n'+r'\addlegendentry{Measured Angular Offset, \(\theta_{\mathrm{meas},t_1}='+entry+r'^\circ\)}')
    d=d.replace('@COMMON@',COMMON.replace('xmajorgrids=false','xmajorgrids=true') + '    x grid style={gray!65, thin, densely dotted},\n    xticklabel style={rotate=0, anchor=north, font=\\fontsize{8}{10}\\selectfont},\n    xlabel style={yshift=0pt},\n')
    sources['results_case_d_panels.tex']=d.replace('@SERIES@','\n'.join(series))
    return {name:text.replace('@YLABEL@',YLABEL).replace('@COMMON@',COMMON) for name,text in sources.items()}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir',type=Path,default=HERE/'contact_angular_error')
    parser.add_argument('--summary',type=Path,default=None,
                        help='Override grouped_results.csv under --data-dir')
    parser.add_argument('--out-dir',type=Path,default=HERE/'../../../figures/ch05')
    args=parser.parse_args()
    args.out_dir.mkdir(parents=True,exist_ok=True)
    for name,text in make_sources(load_summary(args.summary or args.data_dir/'grouped_results.csv')).items():
        output=args.out_dir/name
        output.write_text(text,encoding='utf-8')
        print(output.resolve())

if __name__=='__main__':
    main()
