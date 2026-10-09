# Окно обмена валют E&F и кнопки форекса игрока (95 валют)

**Что делало:** вкладка рынка «global» (`InformationPanel` `'msa'`, тип `market_global_panel_content`), раздел
«exchange_currency»: выбор валюты (`choose_currency_type_<cur>`, переменные `choose_currency_type_<cur>` страны), курс,
запас валюты ЦБ игрока, количество (`currency_quantity_increase/_reduce`), кнопки покупки и продажи валюты владельца
рынка за металл (`<cur>_buy_in_gold` / `<cur>_sell_in_gold`, условия `buy/sell_<cur>_in_gold_market_panel_enabled`,
переключатели `<cur>_buy_on` / `<cur>_sell_on` и `_v`). Кнопка двигала металл ЦБ игрока и эмитента (`gold_state_1` /
`silver_state_1`) и запас валюты `stockpiling_<cur>_state_1`; обёртки `zz_ef_fxb_before` / `zz_ef_fxb_after`
(`ld_fx_buttons.txt`) проводили это через учёт: металл — известное движение сверки (`zz_ef_mt_fx_g/_s`), купленная
валюта — вклад в банках эмитента (`zz_ef_nr_fx_pend` → `zz_ef_nr_dep_step`).

**Почему вынесено:** Д.R8а (очередь R8а, п. 8): валюта — у каждого тега своя, окна E&F «по одной на валюту» и форекс
за металл уходят; заявки игрока вернутся биржей (R8б, словари требований). Осталось во вкладке «global» — сравнение
страны игрока с владельцем рынка и покупка облигаций владельца рынка.

**Кто вызывал:** только GUI (`gui/00_ef_deported_gui_1.gui`, тип `market_global_panel_content`); всё остальное здесь —
определения, на которые после выреза окна не осталось ссылок (вынесены по цепочке: окно → sgui → значения, триггеры,
custom loc → локализация).

## Вырезано (текст — по тем же путям)
- `gui/00_ef_deported_gui_1.gui`: в `market_global_panel_content`, во флоуконтейнере `is_ai` — строка-комментарий
  `#currency_exchange_panel_visibility` и `flowcontainer = { … }` целиком (заголовок `exchange_currency`; внутри —
  `currency_exchange_panel_visibility` / `no_currency_exchange_panel_visibility`), между блоком
  `comparison_of_countries` и комментарием `#purchase_of_bond_debt_visibility` (80 913 строк).
- `common/scripted_guis/00_economic_scripted_guis.txt`: `<cur>_buy_in_gold`, `<cur>_sell_in_gold`,
  `buy_<cur>_in_gold_market_panel_enabled`, `sell_<cur>_in_gold_market_panel_enabled`, `choose_currency_type_<cur>_visible`,
  `choose_currency_type_<cur>` (по 95), `buy_sell_currency_in_gold_on_button_visibility`, `currency_quantity_increase`,
  `currency_quantity_reduce`, `has_gold_exchange_standard_tech_more_button_visibility`,
  `has_gold_standard_no_gold_exchange_standard_tech_market_panel_visibility`, `is_global_monetary_reference_more_button_visibility`,
  `selection_changed_for_currency`.
- `common/scripted_guis/00_stockpile_scripted_guis.txt` — файл целиком (`<cur>_buy_on`, `<cur>_sell_on`, `<cur>_buy_v`,
  `<cur>_sell_v`, по 95).
- `common/scripted_guis/09_ef_other.txt`: `currency_exchange_panel_visibility`, `no_currency_exchange_panel_visibility`,
  `law_<cur>_monetary_system_SS_visible`, `law_<cur>_monetary_system_GS_BS_GES_visible` (по 95).
- `common/scripted_triggers/00_ef_custom_trigger.txt`: `law_<cur>_monetary_system_SS_trigger`, `_BS_trigger`,
  `_GS_GES_trigger`, `_GS_BS_GES_trigger` (по 95).
- `common/script_values/01_economic_currency_scripted_value.txt`: `money_value_<cur>_target`, `valid_<cur>_metal_reserve_type`
  (по 95), `buy_sell_currency_in_metal_market_panel`.
- `common/scripted_effects/01_economic_scripted_effects.txt`: `choose_currency_type_reset_all`,
  `reset_debt_in_national_currency_player`.
- `common/scripted_effects/ld_fx_buttons.txt` — файл целиком (`zz_ef_fxb_before`, `zz_ef_fxb_after`, `zz_ef_fxb_metal_known`).
- `common/scripted_effects/ld_metal_accounts.txt`, `zz_ef_metal_reconcile`: чтение `zz_ef_mt_fx_g/_s` (вычет из «oth») и их
  снятие в конце.
- `common/scripted_effects/ld_nr_deposits.txt` (генератор `regen_ef_nr_deposits.py`), `zz_ef_nr_dep_step`: приём
  `zz_ef_nr_fx_pend`.
- `common/scripted_effects/10_new_country_var.txt`, `new_country_var_ef_economy`: 95 `set_variable =
  { name = choose_currency_type_<cur> value = 0 }`.
- `common/customizable_localization/00_ef_localization_ custom.txt`: `monetary_system_partiel_<cur>`,
  `monetary_system_partiel_name_<cur>` (по 95), `currency_name_mk`, `currency_ISO_4217_mk`, `currency_good_mk`,
  `currency_symbol_mk`.
- `localization/<11 языков>/00_ef_gui_localization_l_<язык>.yml`: `<cur>_on_foreign_exchange_reserve`,
  `quantity_of_currency_market_panel_<cur>` (по 95), `exchange_currency`, `in_gold`, `in_currency`,
  `market_owner_no_currency_exchange_panel_visibility`, `player_no_currency_exchange_panel_visibility`;
  `01_ef_currency_name_localization_l_<язык>.yml`: `dollar_united_states_dollar_short`, `gulden_south_german_gulden_short`.

**Вернуть:** вставить блок GUI на место, определения — в те же файлы; в `zz_ef_metal_reconcile` и генератор
`regen_ef_nr_deposits.py` — чтения `zz_ef_mt_fx_*` / `zz_ef_nr_fx_pend`; переменные выбора — в `new_country_var_ef_economy`.
