"""Two or more runs side by side, by year: the numbers the stage checks compare (R9б.16 -- the run's noise).

Usage:  py tools/ld_noise.py <data.jsonl> <data.jsonl> [...]

<data.jsonl> -- a run's data (`ld_run_report.py <run> <out.html> --data <data.jsonl>`). For each year (the months'
average of a flow, the year's last month of a stock): construction points a week of the world (the sum over the
countries with monthly series -- the largest by GDP) and of Britain, the CB cover of the largest countries, «прочее»
and its share of M2, the banks' capital, the exchanges' deals a week, M2 and GDP. The last column -- the spread of the
runs: (max - min) / mean, %.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ld_run_report import load_data, yearly  # noqa: E402

GB = 'Великобритания'
COVER = ('Великобритания', 'Франция', 'Россия', 'Пруссия', 'Великая Цин')


def rows(D):
    S, C, t = D['S'], D['C'], D['S']['t']
    out = {}

    def put(name, ys):
        for y, v in ys.items():
            out.setdefault(name, {})[y] = v
    world = {}
    for c, cs in C.items():
        for y, v in yearly(t, cs.get('psc_pts'), 'avg').items():
            world[y] = world.get(y, 0) + v
    put('очки стройки мира', world)
    put('очки стройки Британии', yearly(t, C.get(GB, {}).get('psc_pts'), 'avg'))
    for c in COVER:
        put(f'покрытие: {c}', yearly(t, C.get(c, {}).get('cover'), 'last'))
    oth, m2 = yearly(t, S.get('w.other'), 'last'), yearly(t, S.get('w.m2'), 'last')
    put('«прочее», млн', {y: v / 1e6 for y, v in oth.items()})
    put('«прочее», % M2', {y: 100 * v / m2[y] for y, v in oth.items() if m2.get(y)})
    put('капитал банков, млн', {y: v / 1e6 for y, v in yearly(t, S.get('w.bkcap'), 'last').items()})
    put('капитал банков Британии, млн', {y: v / 1e6 for y, v in yearly(t, C.get(GB, {}).get('bkcap'), 'last').items()})
    put('сделки бирж в неделю', yearly(t, S.get('o.deals'), 'avg'))
    put('M2, млн', {y: v / 1e6 for y, v in m2.items()})
    put('ВВП, млн', {y: v / 1e6 for y, v in yearly(t, S.get('w.gdp'), 'avg').items()})
    put('пул Британии, млн', {y: v / 1e6 for y, v in yearly(t, C.get(GB, {}).get('pool'), 'last').items()})
    return out


def main():
    runs = sys.argv[1:]
    data = [rows(load_data(p)) for p in runs]
    names = [os.path.basename(os.path.dirname(os.path.abspath(p))) or p for p in runs]
    keys = list(data[0])
    print('ряд | год | ' + ' | '.join(names) + ' | разброс, %')
    for k in keys:
        years = sorted(set().union(*(d.get(k, {}).keys() for d in data)))
        for y in years:
            vs = [d.get(k, {}).get(y) for d in data]
            have = [v for v in vs if v is not None]
            spread = ''
            if len(have) > 1 and abs(sum(have)) > 1e-9:
                spread = f'{100 * (max(have) - min(have)) / abs(sum(have) / len(have)):.1f}'
            cells = ' | '.join('—' if v is None else f'{v:.3f}' if abs(v) < 10 else f'{v:.1f}' for v in vs)
            print(f'{k} | {y} | {cells} | {spread}')


if __name__ == '__main__':
    main()
