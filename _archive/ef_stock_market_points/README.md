---
type: code
description: "Пункты фондового индекса E&F (Д.R4б.11): «фондовый индекс» страны в пунктах — var:base_index_value = капитализация товаров-«акций» (zz_ef_equity_capitalization) / ВВП × 1000, не меньше 1, не больше 100 000,…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_stock_market_points/**"]
---
# Пункты фондового индекса E&F (Д.R4б.11)

**Что делало:** «фондовый индекс» страны в пунктах — `var:base_index_value` = капитализация товаров-«акций»
(`zz_ef_equity_capitalization`) / ВВП × 1000, не меньше 1, не больше 100 000, пересчёт раз в месяц в
`zz_ef_cap_monthly_update` (`common/scripted_effects/ld_capitalization_average.txt`); «пункты за год»
`var:base_index_value_dif` — разница с отметкой 12 месяцев назад (`zz_ef_cap_idx_prev`, таймер `zz_ef_cap_idx_timer`).
Значение `stock_market_index` (`00_financial_scripted_value.txt`) читало переменную. Начальное значение 10 у новой
страны (`10_new_country_var.txt`), 33 исторических значения у стран с финцентрами (`99_ef_history_global_variable.txt`).
Меню показывали пункты и «изменение за год» (`country_indice_value_dif_01`), таблица стран по пунктам
(`country_index_variable_in_pts_list`, `08_list_effect.txt`) — у стран с модификатором `has_financial_center`.

**Почему в архив:** Д.R4б.11 (пользователь 12.10) — после снятия выпуска «акций» (Д.R4б.8) у всех было по 1, считалось и
у стран без биржи; пункты не нужны — биржи сравнивают по обороту, капитализации требований и перегреву цен
(`zz_ef_xch_month_roll`, `ld_exchange_trade.txt`; понятие «Биржа»). `country_indice_value_dif_01` остаётся — его
пишет и читает механизм краха (`ld_capitalization_crash.txt`, R6).

**Вырезано из живых файлов** (вырезанное — здесь по исходным путям):
```
common/scripted_effects/ld_capitalization_average.txt:157: блок «### Index» в конце zz_ef_cap_monthly_update
common/script_values/00_financial_scripted_value.txt:2518: stock_market_index = { value = var:base_index_value max = 100000 }
common/scripted_effects/10_new_country_var.txt:761: set_variable base_index_value = 10, base_index_value_dif = 0
common/history/global/99_ef_history_global_variable.txt: 33 блока set_variable base_index_value (строки и значения — в архивном файле)
```

**Заменено в живых файлах** (вернуть — поставить старый текст):
```
gui/ld_cb_rate_panel.gui (2 места, Country и GetPlayer):
  raw_text = "[Localize('stock_market_index')]"   -> zz_ef_xch_to_label
  raw_text = "[Country.MakeScope.ScriptValue('stock_market_index')|0+]pts ([Country.MakeScope.Var('country_indice_value_dif_01').GetValue|%|=+])"
  raw_text = "[GetPlayer.MakeScope.ScriptValue('stock_market_index')|0+]pts ([GetPlayer.MakeScope.Var('country_indice_value_dif_01').GetValue|%|=+])"
gui/ld_cb_rate_panel.gui (#country_indice):
  raw_text = "[Localize('stock_market_index')] [GetPlayer.MakeScope.ScriptValue('stock_market_index')|0+]pts ([GetPlayer.MakeScope.Var('country_indice_value_dif_01').GetValue|%|=+])"
gui/ld_cb_rate_panel.gui (#country_index_pts, таблица):
  text = "STOCK_MARKET_01" -> zz_ef_xch_table_title; колонки "pts", "var", "pts_year" -> zz_ef_xch_col_to_y / _cap / _heat
  ячейки: [Country.MakeScope.ScriptValue('stock_market_index')|0]pts; [Country.MakeScope.Var('country_indice_value_dif_01').GetValue|%|+=];
          [Country.MakeScope.Var('base_index_value_dif').GetValue|D=+]pts
gui/00_ef_deported_gui_1.gui:
  raw_text = "[Localize('stock_market_index')] [State.GetOwner.MakeScope.ScriptValue('stock_market_index')|0+]pts ([State.GetOwner.MakeScope.Var('country_indice_value_dif_01').GetValue|%|=+])"
common/scripted_effects/08_list_effect.txt (country_index_variable_in_pts_list):
  limit = { has_modifier = has_financial_center NOT = { stock_market_index = 1000 } } -> zz_ef_has_exchange = yes
  order_by = stock_market_index -> zz_ef_xlm_rank_v
```
Ключи локализации `stock_market_index`, `STOCK_MARKET_01`, `pts`, `var`, `pts_year` в файлах E&F остались (не читаются).
