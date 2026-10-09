# Символ валюты по закону — купюра E&F (`currency_symbol_generic`, `currency_symbol_<cur>`)

**Что делало:** 96 custom loc `currency_symbol_<cur>` (по одной на валюту закона E&F, условие `var:zz_ef_cur ?= flag:<cur>`,
текст — `<cur>_texture`, текстиконка купюры `@<cur>!`) и `currency_symbol_generic` (нет `var:zz_ef_cur` — `spe_uni_texture`).
Их читали 96 текстбоксов символа в верхней панели (тот вынесен раньше — `_archive/ef_topbar_currency_symbols/`); тело
`currency_symbol` вело на те же купюры.

**Почему вынесено:** Д.R8а.8 — символ у каждого тега свой: «<две буквы страны> <знак слова>» (`currency_symbol`, генератор
`../vic3_mods/tools/regen_ld_currency_symbol.py`). Ссылок на эти записи в живых файлах не было; генератор
`regen_ld_currency_data.py` их больше не пишет.

**Вырезано (текст — по тем же путям):** `common/customizable_localization/00_ef_localization_ custom.txt` —
`currency_symbol_generic` и 95 `currency_symbol_<cur>`. Купюры (`<cur>_texture`, текстиконки `@<cur>!`
в `gui/00_ef_texticons.gui`) остались: ими подписаны чужие валюты в таблицах и `overlord_currency_symbol`,
`global_monetary_reference_texture`.

**Вернуть:** записи — в тот же файл; в `regen_ld_currency_data.py` — их вывод (`custom_text`).
