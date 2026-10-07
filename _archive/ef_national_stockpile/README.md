# Национальный запас товаров E&F (нацзапас)

**Что делало.** Страна-владелец рынка с технологиями `stockpiling_goods` → `national_stockpile` копила и выпускала
29 товаров (`ammunition small_arms artillery tanks aeroplanes grain fabric wood groceries clothes paper silk dye sulfur
coal iron lead hardwood rubber oil engines steel fertilizer tools explosives automobiles telephones radios opium`):
модификаторы штата `storing_<g>` / `releasing_<g>` (приказы покупки/продажи на рынке через типы
`state_buy_/sell_orders_<g>_add`), счёт товара в `stockpiling_<g>_state_1` столичного штата, месячный поток
`flow_storing_<g>` / `storing_<g>_1` / `releasing_<g>_1`. Игрок управлял запасом во вкладке «Запас» бюджета и в разделе
товаров окна рынка (заказы за валюту `buy_/sell_<g>_order_in_currency`, продажа запаса `sell_<g>_market_panel`); ИИ раз
в год торговал на международном рынке (`buy_sell_<g>_on_international_market`, все `add_treasury` закомментированы —
товар из ничего), раз в 10 лет менял резерв (`ai_set_stockpile_reserve_limit`). Статья договора `material_supply`
(поставки со склада). Денег модели не касалось. Вынесено решением 7.10 (этап R0 реструктуризации): переработка
нацзапаса под новую модель — последний этап (R13).

**Кто вызывал.** `ef_on_monthly_pulse_country` → `national_stockpile_ef_on_monthly_pulse_country` (→
`flow_storing_on_action`, `storing_releasing_on_action`) и `financial_center_ef_on_monthly_pulse_country`
(→ `RMSA_MMSA_order_trigger`, заказы игрока); `ef_on_half_yearly_pulse_country` →
`national_stockpile_ef_on_half_yearly_pulse_country` (→ `national_stockpile_state_modifier_clean`);
`ef_on_yearly_pulse_country` → 29× `buy_sell_<g>_on_international_market`; `ef_on_decade_pulse_country` →
`ai_set_stockpile_reserve_limit`; `ef_on_monthly_pulse_recurence` → `national_stockpile_state_modifier_clean_subject`;
`update_modifiers_bc_fc_ns` → `national_stockpile_modifier` (модификаторы `has_national_stockpile`,
`national_stockpile_place`, `national_stockpile_historic_place`); GUI — кнопки и окна.

**Переменные.** Страна: на товар ~40 (`<g>_store_quantity`, `<g>_store_month`, `<g>_store_status`,
`<g>_release_*`, `store_/release_<g>_time`, `buy_/sell_<g>_1`, `buy_/sell_<g>_in_gold_1`, `ef_ai_set_<g>_reserve`,
`trade_<g>_var`, `trade_<g>_budget_panel`, `<g>_market_panel_quantity`), `country_already_national_stockpile`,
`current_order`; штат: `stockpiling_<g>_state_1`, `release_<g>_var_1`; глобальные: `stocked_<g>_flag_global_variable`,
список `stocked_goods_global_variable_list`. Признак «страна инициализирована» был `coal_release_quantity` (переменная
запаса угля) — теперь `zz_ef_country_vars_set` (ставят history `00_ef_stockpile_global_variable.txt` и
`new_country_var_ef`; читают `ef_on_monthly_pulse_recurence`, `ld_new_country_immediate_init`, событие
`zz_ef_newcountry.1`).

**Не входит и осталось живым.** `looting_1_year_on_action` (грабёж ЦБ, жил в `01_stockpile_scripted_effects.txt` —
этот файл остался ради него), `looting_1_year`; валютные переключатели `<cur>_buy_on/_sell_on(_v)` в
`00_stockpile_scripted_guis.txt`; запасы валют ЦБ `stockpiling_<cur>_state_1`; посев переменных штатов
`zz_ef_seed_stockpile_*` (финпродукты, место финцентра, грабёж). Раньше вынесено: заказы за золото —
`_archive/ef_stockpile_gold_orders/`, группа зданий — `_archive/ef_bg_national_stockpile/`.

## Что лежит здесь

По исходным путям; в начале каждого куска — `# из <файл>, строки a–b (на 2026-10-07)`. Номера строк — в файле на
момент выреза: куски одного файла, вырезанные позже (второй и третий проход), считаны после предыдущих.

- Файлы целиком: `common/scripted_effects/01_stockpile_scripted_effects.txt` (кроме `looting_1_year_on_action`),
  `common/script_values/00_stockpile_scripted_value.txt`, `common/treaty_articles/15_supply_agreement.txt`.
- Графика: 29 иконок алертов `alert_icons/stockpile_<g>.dds`, `building_icons/national_stockpile/` (с вариантами
  `Other/`), `invention_icons/stockpiling_goods.dds`, `national_stockpile.dds`,
  `timed_modifier_icons/national_stockpile_place.dds`, `diplomatic_treaties_articles_icons/material_supply.dds`,
  `button_icons/infinit.dds`, `reset_value_icon.dds`.
- Локализация — английская и русская (остальные девять языков — копия английской; вернуть английскую и запустить
  `../vic3_mods/tools/ld_loc_langs.py`).

## Удалено из живых файлов

| файл | что |
| --- | --- |
| `common/on_actions/00_ef_on_action.txt` | хук `on_decade_pulse_country { ef_on_decade_pulse_country }` и on_action `ef_on_decade_pulse_country` целиком; в `ef_on_monthly_pulse_country` — строка примечания `# - stockpiling_goods -> …`, блоки `#has_financial_center` (`financial_center_ef_on_monthly_pulse_country = yes`) и `#stockpiling_goods` (`national_stockpile_ef_on_monthly_pulse_country = yes`); в `ef_on_half_yearly_pulse_country` — блок `#has_national_stockpile` (`national_stockpile_ef_on_half_yearly_pulse_country = yes`); в `ef_on_yearly_pulse_country` — блок `#has_national_stockpile` (29× `buy_sell_<g>_on_international_market = yes`) |
| `common/scripted_effects/00_on_action_main.txt` | в `ef_on_monthly_pulse_recurence` — блок `#national_stockpile_state_modifier_clean` (`if` по `stockpiling_goods`, чужой рынок, 58 модификаторов → `national_stockpile_state_modifier_clean_subject = yes`); определения `financial_center_ef_on_monthly_pulse_country`, `national_stockpile_ef_on_monthly_pulse_country`, `national_stockpile_ef_on_half_yearly_pulse_country`, `flow_storing_on_action`, `storing_releasing_on_action`, `RMSA_MMSA_order_trigger`, `ai_set_stockpile_reserve_limit`; в `update_modifiers_bc_fc_ns` — ветка `if` (`national_stockpile` + `building_bank` → `national_stockpile_modifier = yes`) |
| `common/scripted_effects/09_introduction_building_lvl.txt` | определение `national_stockpile_modifier`; в `remove_country_building_modifier` — `if` снятия `has_national_stockpile`; в `destroy_building_not_allowed` — закомментированный `if` сноса `building_national_stockpile` |
| `common/scripted_effects/01_economic_scripted_effects.txt` | в эффекте грабежа штата — 2 строки снятия `national_stockpile_place` / `_historic_place` |
| `common/scripted_effects/10_new_country_var.txt` | `set_variable country_already_national_stockpile`; раздел STOCK GOODS (переменные 29 товаров) до `#end_past_stockpile_event`; переменные `trade_<g>_budget_panel`, `trade_<g>_var`, `<g>_market_panel_quantity` в финансовом разделе |
| `common/history/global/00_ef_stockpile_global_variable.txt` | всё, кроме `looting_1_year` (флаги и список запасаемых товаров, переменные 29 товаров); добавлен `zz_ef_country_vars_set` |
| `common/history/global/00_ef_financial_global_variable.txt` | переменные `trade_<g>_budget_panel`, `trade_<g>_var`, `<g>_market_panel_quantity` |
| `common/history/global/00_ef_economic_global_variable.txt` | `set_variable country_already_national_stockpile` |
| `common/history/global/99_ef_history_global_variable.txt` | блок GOODS: стартовые запасы (`stockpiling_<g>_state_1` в столице) 17 стран и `national_stockpile_modifier = yes` |
| `common/scripted_guis/00_stockpile_scripted_guis.txt` | все sgui товаров (~55 на товар: `increase/reduce_<g>_*`, `set_store/release_<g>*`, `store/release_<g>_*`, `<g>_buy_on/_sell_off(_v)`, `buy/sell_<g>_market_panel(_enabled)`, `trade_<g>_budget_panel(_show)`, `default_<g>`, `set_<g>_0`, …), `update_stocked_goods_global_variable_list` |
| `common/scripted_guis/09_ef_other.txt` | `buy_sell_good_visibility`, `no_buy_sell_good_visibility`; раздел `#national_stockpile`: `has_tech_national_stockpile`, `not_has_tech_national_stockpile`, `…_and_subject` (2), `has_national_stockpile`, `not_is_national_stockpile`; `national_stockpile_historic_place` |
| `common/scripted_guis/00_economic_scripted_guis.txt` | в `transfert_loot_state` — 2 строки `has_modifier = national_stockpile_place` / `_historic_place` |
| `common/scripted_triggers/00_ef_custom_trigger.txt` | `has_national_stockpile`, `country_already_national_stockpile`, `ai_set_stockpile_reserve_limit_spe_country` |
| `common/script_values/00_economic_scripted_value.txt` | 58 значений `store_/release_<g>_time_rest` |
| `common/script_values/00_financial_scripted_value.txt` | раздел `# goods`: `<g>_price`, `buy_/sell_<g>_market_panel`, `buy_/sell_<g>_in_gold_market_panel`; `sell_limit_var_0` |
| `common/script_values/01_economic_currency_scripted_value.txt` | `money_supply_state_market_panel`, `money_supply_state_market_owner` |
| `common/customizable_localization/00_ef_localization_ custom.txt` | `stokpiling_<g>_status`, `buy_/sell_<g>_1` |
| `common/static_modifiers/00_ef_dynamic_modifier_country.txt` | `has_national_stockpile` |
| `common/static_modifiers/00_ef_dynamic_modifier_state.txt` | `national_stockpile_place`, `national_stockpile_historic_place`, 58 `storing_<g>` / `releasing_<g>` |
| `common/static_modifiers/00_ef_dynamic_modifier_building.txt` | раздел STOCKPILING: `release_/store_<g>_1` (19 шт., не применялись) |
| `common/modifier_type_definitions/00_ef_state_modifier_types.txt` | раздел STOCKPILING GOODS: 51 тип `state_buy_/sell_orders_<g>_add` |
| `common/technology/technologies/ef_technology.txt` | технологии `stockpiling_goods`, `national_stockpile` |
| `common/alert_types/00_ef_alert_types.txt` | 29 алертов `store_release_<g>` |
| `gui/budget_panel.gui` | вкладка «Запас»: 6 `blockoverride "fifth_button*"` (`STOCKPILE`, `InformationPanel.SelectTab('stockpile')`) и виджет `budget_panel_stockpile_panel_content = { visible = "[InformationPanel.IsTabSelected('stockpile')]" }` |
| `gui/00_ef_deported_gui_1.gui` | в `market_global_panel_content` — раздел `#buy_sell_good_visibility` (заголовок `r_m_s_a`, заказы и продажа товаров); `types market_states_panel` с типом `budget_panel_stockpile_panel_content` целиком; в `state_panel_currency_panel_content` — блок `#Stockpile` (`NATIONAL_STOCKPILE_TITLE`, запасы 29 товаров штата) |
| `localization/*/` (11 языков) | 845 ключей: окна и кнопки запаса, `storing_/releasing_<g>`, `release_/store_<g>_1`, `state_buy_/sell_orders_<g>_add`, технологии, `material_supply`, `<g>_price`, `<g>_flag_status*`, `<g>_flag_var_state*`, `<g>_flag_green_arow_bellow*`, `no_order` / `release_on` / `store_on` |

**Вернуть.** Файлы и куски — на исходные места (порядок кусков в файле архива — по строкам), признак
инициализации можно оставить `zz_ef_country_vars_set`. В живом коде на имена отсюда ссылок нет (проверено
`ld_index.py` и сверкой слов: сирот, висячих ссылок, переменных «пишется — не читается» и «читается — не пишется» нет).
