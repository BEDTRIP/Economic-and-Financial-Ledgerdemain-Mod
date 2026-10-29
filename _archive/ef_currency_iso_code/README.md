---
type: code
description: "Код валюты E&F (`currency_ISO_4217`): пользовательская локализация currency_ISO_4217 (страна) выбирала по var:zz_ef_cur ключ <cur>_ISO_4217 — трёхбуквенный код одной из 95 валют E&F (DZD, GBP…); у страны без…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_currency_iso_code/**"]
---
# Код валюты E&F (`currency_ISO_4217`)

**Что делало:** пользовательская локализация `currency_ISO_4217` (страна) выбирала по `var:zz_ef_cur` ключ
`<cur>_ISO_4217` — трёхбуквенный код одной из 95 валют E&F (`DZD`, `GBP`…); у страны без валюты E&F — `spe_uni_ISO_4217`.
В окнах шёл рядом со знаком: «1 GBP (GB £) = …».

**Почему ушло:** код валюты теперь генерируется для каждой страны — две буквы страны + первая буква слова (Д.R8в.20,
`currency_code`, `tools/regen_ld_currency_symbol.py`), а `currency_symbol` показывает знак у выбранных кодов и код у
остальных; пара «код (знак)» в окнах стала одним `currency_symbol`, пары валют на бирже — `currency_code`.

**Вырезано:** `currency_ISO_4217` (`common/customizable_localization/00_ef_localization_ custom.txt`). Ключи
`<cur>_ISO_4217` в `01_ef_currency_name_localization_l_*.yml` остаются — их читает
`global_monetary_reference_currency_ISO_4217` (подпись валюты-эталона E&F).
