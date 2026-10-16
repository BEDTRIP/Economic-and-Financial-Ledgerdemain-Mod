"""Rebuild <run>/eflog.txt from the run's debug parts (as Close-And-Collect of vic3_tools bridge/game/vic3_ui_lib.ps1 does).

Usage:  py tools/ld_build_eflog.py <run> [--before <run0>]

For a run whose collection was cut (the script stopped while writing eflog.txt): the parts <run>/dbgparts/*.log
(oldest first, by name) and <run>/debug.log, each part once (by its content), the mod's log lines (': EF?|') with the
prefix cut, into <run>/eflog.txt. --before: <run> continues <run0> from its autosave (the player's country gone, a run
cut) -- <run0>/eflog.txt's lines dated before <run>'s first line go first, so the report reads the two as one game.
"""
import glob
import hashlib
import os
import re
import sys

LINE = re.compile(r'^.*?: (EF[A-Z]\|)')
DATE = re.compile(r'^EF[A-Z]\|(\w+) (\d+), (\d{4})\|')
MON = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
       'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}


def day(ln):
    m = DATE.match(ln)
    if not m or m.group(1) not in MON:
        return None
    return int(m.group(3)) * 372 + MON[m.group(1)] * 31 + int(m.group(2))


def main():
    run = sys.argv[1]
    before = sys.argv[sys.argv.index('--before') + 1] if '--before' in sys.argv else None
    parts = sorted(glob.glob(os.path.join(run, 'dbgparts', '*.log')), key=os.path.basename)
    if os.path.exists(os.path.join(run, 'debug.log')):
        parts.append(os.path.join(run, 'debug.log'))
    seen = set()
    n = 0
    lines = []
    for p in parts:
        h = hashlib.md5(open(p, 'rb').read()).hexdigest()
        if h in seen:
            continue
        seen.add(h)
        for ln in open(p, encoding='utf-8', errors='replace'):
            m = LINE.match(ln)
            if m and ': EF' in ln:
                lines.append(ln[m.start(1):])
    first = next((d for d in map(day, lines) if d), None)
    n0 = 0
    with open(os.path.join(run, 'eflog.txt'), 'w', encoding='utf-8') as out:
        if before and first:
            for ln in open(os.path.join(before, 'eflog.txt'), encoding='utf-8', errors='replace'):
                d = day(ln)
                if d is not None and d >= first:
                    break
                out.write(ln)
                n0 += 1
        out.writelines(lines)
        n = len(lines)
    print(f'{len(seen)} parts, {n} lines (+{n0} of {before} before them) -> {os.path.join(run, "eflog.txt")}')


if __name__ == '__main__':
    main()
