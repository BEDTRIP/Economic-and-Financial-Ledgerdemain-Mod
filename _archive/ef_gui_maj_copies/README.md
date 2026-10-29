---
type: code
description: "Копии ванильных панелей E&F (`gui/ef_dev_and_custom_windows/maj/`): 18 файлов — копии ванильных панелей (maj/Essential: building_browser_panel, building_details_panel, goods_panel, goods_state_panel, production_methods; maj/NonEssential:…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_gui_maj_copies/**"]
---
# Копии ванильных панелей E&F (`gui/ef_dev_and_custom_windows/maj/`)

**Что это:** 18 файлов — копии ванильных панелей (`maj/Essential`: `building_browser_panel`, `building_details_panel`,
`goods_panel`, `goods_state_panel`, `production_methods`; `maj/NonEssential`: `company_panel`, `console`,
`goods_local_prices_panel`, `graph_tooltips`, `map_list_panel`, `market_food_security_panel`, `market_states_panel`,
`outliner_pinnable_types`, `panel_military`, `pop_details_panel`, `strait_panel`, `table_tooltips`,
`world_market_panel`), 281 тип и 79 шаблонов.

**Почему вынесено (R12 Л.2, [[Д.R12.1 — Копии ванильных панелей E&F в gui ef_dev_and_custom_windows maj|Д.R12.1]]):** игра не применяла ни одного — `gui.log` прогона r1016_203107: все 360 «Type /
Template '…' already registered at …» (тип регистрирует первый файл по имени, ванильный и CMF лежат ближе к корню
`gui/`). В игре видны ванильные и CMF-панели; без папки ничего не меняется.

**Что в них было своего (кандидаты, если вернуть):** сверка с ванилью 1.13 (16.10): из 360 — 330 совпадают с ванилью до
символа; 30 отличаются: ~18 — правки E&F, ~12 — ваниль прежней версии. Правки E&F:
- символ национальной валюты `GetCustom('currency_symbol')` в ценах товаров, зданий, импорта и экспорта (`goods_panel`,
  `goods_state_panel`, `building_details_panel`);
- скрытие групп методов финансового центра (`pmg_market_liquidity` …) и группы `bg_financial_centre` в панели здания и в
  списке производителей (`building_details_panel`, `building_browser_panel`, `production_methods`). Вернуть — подменой
  ванильного файла по пути (`gui/<имя>.gui`) с правкой поверх текущей ванили и CMF; сравнить —
  `tools/ld_vanilla_diff.py` (путь к копии — здесь).

**Удалено из живых файлов:** папка `gui/ef_dev_and_custom_windows/maj/` целиком (здесь, по исходным путям); строки
[[mechanisms]], [[interface]].
