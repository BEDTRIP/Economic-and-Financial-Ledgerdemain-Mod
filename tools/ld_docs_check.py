"""Формат заметок понятий форка — правило форка поверх `v3 docs check` (он зовёт эту проверку из `docs-check.toml`).

Заметка понятия (`docs/понятия/`, кроме `_*`, заметок с тегом `обзор`; у тега `использование` — только «## Рабочее») —
разделы «## Подсказка», «## Рабочее», «### Целевое значение», «### Что в коде» по порядку; подсказка не пустая, без кода
в обратных кавычках и номеров решений, абзац и пункт списка — одной строкой: подсказка уходит в игру текстом
(Д.R10.8). Шапки, ссылки, пути `paths`, покрытие `common/` и `events/`, номера решений в коде — `v3 docs check`.

    python tools/ld_docs_check.py [--fork <путь>]

Код выхода 1 — заметки не по формату. Ничего не меняет.
"""
import argparse
import os
import re
import sys

FORK = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fork", default=FORK)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    bad = notes_format(a.fork)
    for x in bad:
        print("  формат заметки:", x)
    sys.exit(1 if bad else 0)


ITEM_LINE = re.compile(r"^(- |\d+\. )")
HEADS = ("## Подсказка", "## Рабочее", "### Целевое значение", "### Что в коде")


def notes_format(fork):
    """Заметки понятий: разделы по порядку; подсказка без кода и номеров решений."""
    d = os.path.join(fork, "docs", "понятия")
    bad, n = [], 0
    for f in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if not f.endswith(".md") or f.startswith("_"):
            continue
        text = open(os.path.join(d, f), encoding="utf-8").read()
        if re.search(r"^tags:.*\bобзор\b", text, re.M):
            continue
        if re.search(r"^tags:.*\bиспользование\b", text, re.M):  # «<понятие игры> в форке»: подсказки нет (Д.ДОК.15)
            if "## Рабочее" not in text.split("\n"):
                bad.append(f"{f}: нужен раздел ## Рабочее")
            continue
        n += 1
        lines = text.split("\n")
        pos = [lines.index(h) if h in lines else -1 for h in HEADS]
        if -1 in pos or pos != sorted(pos):
            bad.append(f"{f}: нужны разделы {' → '.join(HEADS)}")
            continue
        tip = "\n".join(lines[pos[0] + 1:pos[1]])
        if not tip.strip():
            bad.append(f"{f}: пустая подсказка")
        elif "`" in tip or re.search(r"Д\.(?:R|П|Г|\d)", tip):
            bad.append(f"{f}: в подсказке код или номер решения")
        elif any(len(p.split("\n")) > 1 and not all(ITEM_LINE.match(x) for x in p.split("\n"))
                 for p in tip.strip().split("\n\n")):
            bad.append(f"{f}: абзац подсказки — не одной строкой (ld_md_wrap.py склеит)")
    print(f"формат заметок понятий: проверено {n}, не по формату {len(bad)}")
    return bad


if __name__ == "__main__":
    main()
