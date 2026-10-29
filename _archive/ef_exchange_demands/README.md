---
type: code
description: "Спрос финцентра на акции E&F (R9в.4): финцентр E&F (bg_financial_centre) каждый месяц вешал на своё здание модификаторы «спроса» на четыре вида акций — manufacture_stock_deemande,…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_exchange_demands/**"]
---
# Спрос финцентра на акции E&F (R9в.4)

**Что было:** финцентр E&F (`bg_financial_centre`) каждый месяц вешал на своё здание модификаторы «спроса» на четыре
вида акций — `manufacture_stock_deemande`, `agricultural_stock_deemande`, `mining_stock_deemande`,
`railroad_stock_deemande` (`goods_input_<акция>_mult`), — по отклонению продаж акций на рынке от базового входа
(`target_demand_<акция>_for_modifier`, база `base_demande_<акция>_fix`). У методов финцентра входов этих акций нет
(вход — только облигации), поэтому множитель ничего не умножал; база — вход метода — была 0, и «стоимость» спроса на
акции в недельном балансе финцентра (`<акция>_price_by_demand_fc` в `total_cost_fcc`) тоже 0.

**Почему снято:** мёртвый механизм (R9в, «спросы» E&F — множители входов, которых у метода нет). Спрос на облигации
(`bond_deemande`) и выпуск паёв (`mutual_fund_supply`) остаются: у метода финцентра есть вход облигаций и выход паёв.

**Вырезано** (по исходным путям этой папки; в начале каждого куска — откуда):
- `common/static_modifiers/00_ef_dynamic_modifier_building.txt` — четыре модификатора;
- `common/scripted_effects/09_introduction_building_lvl.txt` — их снятие и наложение в `financial_center_modifier` (главный
  и прочие финцентры), запись баз в `financial_center_modifier_fixed_var`;
- `common/scripted_effects/10_new_country_var.txt` — начальные базы (0);
- `common/script_values/00_financial_scripted_value.txt` — `base_demande_<акция>`, `_fix`, `target_demand_<акция>`,
  `_ajusted`, `_for_modifier`, `<акция>_price_by_demand_fc` и их строки в `total_cost_fcc`;
- `localization/` — названия модификаторов (en, ru; девять языков — копия английской, `ld_loc_langs.py`).

**Вернуть:** только вместе с входами акций у метода финцентра; модификаторы и значения — из этой папки, строки
`total_cost_fcc` — обратно, локализация — en/ru и `ld_loc_langs.py`.
