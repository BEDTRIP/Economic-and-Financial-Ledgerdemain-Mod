# Значения E&F без ссылок (ночь 8.10, запас)

**Что это:** 382 script value E&F, на которые нет ни одной ссылки: `ld_index.py` — 0, и во всём тексте форка (`common/`,
`gui/`, `localization/`) имя встречается только в своём определении. В основном — значения окон, вынесенных раньше
(`buy_/sell_<cur>_in_gold_market_panel`, 190; `financial_centre_<tag>_input_bond` и другие значения финцентров), счётчики
инфляции `inflation_on_*_market_value_abs`, остатки здания-пустышки `building_ef_private_construction_*`. Игра их не
вычисляла — поведение не меняется.

## Вырезано (текст — по тем же путям)
- `common/script_values/01_economic_currency_scripted_value.txt` — 285 определений;
- `common/script_values/00_financial_scripted_value.txt` — 92;
- `common/script_values/00_economic_scripted_value.txt` — 5.
Список и исходные строки — в файлах архива.

**Вернуть:** определение — в тот же файл.
