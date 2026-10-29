---
type: code
description: "Четыре типа Ротшильдов E&F (R9а.3, Д.R9а.5): E&F держал пять типов компании Ротшильдов — company_Rothschild_Bank_gbr (Лондон) и _fra (Париж), _ger (Франкфурт, страна FRM), _aus (Вена), _ita (Неаполь, SIC), — каждый…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_rothschild_types/**"]
---
# Четыре типа Ротшильдов E&F (R9а.3, Д.R9а.5)

**Что было:** E&F держал пять типов компании Ротшильдов — `company_Rothschild_Bank_gbr` (Лондон) и `_fra` (Париж),
`_ger` (Франкфурт, страна FRM), `_aus` (Вена), `_ita` (Неаполь, SIC), — каждый со своей историей, уровнями (стройсекторы,
железные дороги в чужих странах), запасами металла E&F (`company_Rothschild_Bank_<x>_gold/silver_stockpile`,
глобальные `…_fix`), строками в списках компаний (`08_list_effect.txt`), подписями (`00_ef_localization_ custom.txt`)
и иконками. К 1841 в прогонах выживали два: `_gbr` и `_ger`.

**Почему снято ([[Д.R9а.5 — Ротшильды — одна компания|Д.R9а.5]]):** Ротшильды — одна компания со штабом в Лондоне; присутствие в Париже, Вене, Франкфурте и
Неаполе — её «Банк» там (5 уровней, `PRESENCE` генератора `regen_ef_bank_seed.py`, история `zz_ef_bank_company_seed`);
межрыночный субъект с одним капиталом — R9а.4.

**Вырезано** (по исходным путям этой папки; в начале каждого файла — откуда):
- `common/company_types/00_ef_companies.txt` — четыре определения типов;
- `common/history/buildings/00_ef_building.txt` — `add_company` и блоки `company:company_Rothschild_Bank_<x>` (FRM, NGF, GER,
  SIC, ITA, FRA, AUS);
- `common/scripted_effects/01_financial_scripted_effects.txt` — ветки `establish_bank_and_ef_compagnie` четырёх типов;
- `common/scripted_effects/08_list_effect.txt` — строки `type = company_type:…` в списках банков;
- `common/history/global/00_ef_economic_global_variable.txt` — `set_global_variable` запасов металла `…_fix`;
- `common/script_values/01_economic_company_value.txt` — значения запасов металла и их ветки в суммах по компании;
- `common/customizable_localization/00_ef_localization_ custom.txt` — блоки `text` четырёх типов;
- `localization/{english,russian}/01_ef_company_localization_l_*.yml` — названия (11 языков);
- `gfx/interface/icons/company_icons/bank/company_Rothschild_Bank_{fra,ger,aus,ita}.dds`.

**Изменено в живых файлах:** уровни четырёх типов в истории (`00_ef_building.txt`, 33 блока `company = { … }`:
стройсекторы, железные дороги, рудники в чужих странах) — на `company_Rothschild_Bank_gbr`, страна `c:GBR`; засев
«Банков» (`regen_ef_bank_seed.py`: 94 банковские компании вместо 98), листинг (`regen_ef_listing.py` — по типам форка).

**Вернуть:** определения, ветки и строки — на прежние места (файлы архива — в порядке вырезания); уровни в истории —
прежние типы и страны (git: коммит R9а.3).

**Поправка:** в `history/buildings/00_ef_building.txt` архивного файла ветки стран NGF, GER, ITA, FRA, AUS вырезаны
целиком; в истории форка они возвращены без строк Ротшильдов (остальные компании — Прусская морская торговля, Банк
Франции, Creditanstalt, Banca d'Italia и др.), в архиве по-прежнему лежат целиком.
