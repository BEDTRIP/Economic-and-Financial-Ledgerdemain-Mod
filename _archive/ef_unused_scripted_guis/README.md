# Скриптовые GUI без ссылок (914 + 1)

**Что это.** sgui, на которые нет ссылок (`refs=0`): имя не встречается в `GetScriptedGui(...)` ни в одном `.gui`, ни в скриптах и локализации,
и не собирается динамически (все вызовы `GetScriptedGui` в `gui/` — со строковым литералом, без `Concatenate`/`+`/`$param$`).
Семейства (по валютам): `choose_currency_type_<cur>_on/_off`, `money_value_<cur>_visible`, `stockpiling_<cur>_visibility`/`_state_visibility`,
`law_<cur>_*`/`<cur>SS_visible`/`GS_BS_GES_visible`, `<cur>_sell_in_gold_on/_v`, `<cur>_currency_in_gold`, `*_budget_panel_visible`/`_panel`,
плюс одиночные: `seller_/buyer_country_general_XY_oclick/_visible`, `gold_/gold_exchange_standard_standard_law`, `devaluation_currency`, `revaluation_currency`,
`bond_in_currency_always_no`, `update_import_export_value_in_currency_in_reeserve_liste(_debug)`, `ai_quantity_purchasing_1_visibility`, `sell_limit_var_show(_0)`,
`exclusion_buiding_gui`, `law_*_standard_country_top_bar`/`_market_panel`, `infamy_international_trade(_pariah)`, `is_national_stockpile`,
`global_player_help_on/_off(_visible)` и др.; `com_add_local_good` (файл `com_local_goods_sgui.txt` целиком: добавлял `scope:local_good` в список `com_local_goods`, вызова нет).

**Кто вызывал:** никто. **Переменные, интерфейс:** нет (эффекты тел писали переменные, которых никто не читает ниже по цепочке; осиротевшее от выноса — в `ef_gui_orphans/`).

**Удалено из живых файлов** (определения из `common/scripted_guis/`, тот же путь в архиве):
`00_economic_scripted_guis.txt` — 297; `00_stockpile_scripted_guis.txt` — 221; `09_ef_other.txt` — 391 (в т. ч. `financial_product_panel_list_gerenation_ordered`: его тело вызывало неопределённые эффекты `bond_variable_list`, `manufacture_stock_variable_list`, `agricultural_stock_variable_list`, `mining_stock_variable_list`, `railroad_stock_variable_list`; стояло после `reference_currency_in_gold_fixe_ac`); `00_financial_scripted_guis.txt` — 5;
`com_local_goods_sgui.txt` — файл целиком. Вызовов и элементов GUI удалять не пришлось.

**Оставлено:** `zz_ef_cbfx_update` (`ld_cbfx.txt` — ведёт генератор `regen_ef_clearing`, мёртв: заменён `_sorted`), `EF_room_gui_1` (упомянут в комментарии живого окна резервов; `_2…_N` живые),
`gdp_sort_by_country_gdp`, `si_sort_by_country_indice`.

**Вернуть:** вставить определения обратно в исходные файлы.
