# Архив мёртвых механизмов

Механизмы E&F / PSC / `ld_*`, которые ни на что не влияли (не вызывались или были заглушены), — вынуты из мода, чтобы
игра их не читала, и сохранены здесь на случай, если пригодятся. Игра эту папку не грузит; в живую копию и мастерскую
она не попадает. Не нужен — папку механизма можно удалить.

Правила — `CLAUDE.md` форка, раздел «Мёртвое — `_archive/`». Устройство папки механизма:

```
_archive/<механизм>/
  README.md                 что делал; кто вызывал; переменные; интерфейс; удалённые вызовы и элементы GUI (файл, ключ, текст)
  common/.../<файл>.txt     вырезанные определения, по исходному пути (в начале — откуда, строки)
  gui/..., localization/... то же для GUI и локализации
```

## Механизмы

| механизм | папка | что удалено из живых файлов |
| --- | --- | --- |
| Архивы `.zip`/`.rar` E&F (старый ИИ-форекс, ИИ-стратегии, PM, события) | `ef_zip_archives/` | ничего — файлы целиком |
| Резервные копии `.backup` GUI и локализации | `ef_backups/` | ничего — файлы целиком |
| Рабочие остатки автора: `test.txt`, `00_ef_dev_tips.gui`, дубль `.yaml`, генераторы `nw_*.py` | `ef_dev_leftovers/` | ничего — файлы целиком |
| Месячная раздача/покупка металла ЦБ: `storing_gold_1`/`storing_silver_1`, пустая обёртка `stockpiling_central_bank_metal_reserves_state`, `zz_ef_cb_metal_purchase_step` | `ef_cb_metal_reserves_storing/` | вызов обёртки в `00_on_action_main.txt`; три определения из `01_economic_scripted_effects.txt`; файл `ld_cb_stockpile_track.txt` |
| Разовый пересчёт металла субъектов `zz_ef_subject_metal_step` (+ `zz_ef_metal_in_gold`, `zz_ef_metal_target_in_gold`) | `ef_subject_metal_step/` | определение из `ld_subject_metal.txt`, два значения из `ld_reference_currency_values.txt` |
| Значения денежной модели без ссылок (25 штук) | `ef_unused_money_values/` | определения из `ld_money_model_values.txt` |
| Заказы запаса за золото (`*_order_in_gold`) и `buy_<g>_budget_panel` | `ef_stockpile_gold_orders/` | 58 блоков `if` в `01_stockpile_scripted_effects.txt`; 29 scripted_gui в `00_stockpile_scripted_guis.txt` |
| Перемасштаб валютных запасов `zz_ef_fx_stock_rescale` | `ef_fx_stock_rescale/` | файл `ld_fx_stock_rescale.txt`; закомментированный вызов в `ld_money_model.txt` |
| Хронометрия чеканки ЦБ (`zz_ef_mint_*`) | `ef_mint_timing/` | 7 значений из `ld_money_model_values.txt` (обнуления `zz_ef_f_mint*` остались — их читают логи) |
| Деньги за металл по Юму (`zz_ef_hume_money_on`) | `ef_hume_money/` | ветка `if` в `zz_ef_cb_hume_step`; два значения |
| Зонды EFJ / EFD | `ef_probes_efj_efd/` | два вызова и два эффекта в `ld_money_model.txt`; 4 значения |
| Приказы валюты по уровням `buy_sell_currency_order` (вызывали несуществующие эффекты `buy_<cur>_N`) | `ef_currency_orders_numbered/` | определение `buy_sell_currency_order` и его вызов в `central_bank_ef_on_half_yearly_pulse_country` (`00_on_action_main.txt`) |
| ПМ потребления металла банка: тела `central_bank_production_methods`, `_3`, `_4` (ПМ не существуют) | `ef_central_bank_pm_consuption/` | тела трёх эффектов в `01_economic_scripted_effects.txt` (определения остались пустыми) |
| ПМ `pm_privately_owned_building_arms_industry` (вне групп, несуществующий модификатор) | `ef_arms_industry_pm/` | определение из `00_ef_market_liquidity.txt` |
| Пустой модификатор `zz_ef_business_cash` | `ef_business_cash_modifier/` | файл `ld_business_cash.txt`; снятие в `zz_ef_money_week_start` |
| Проверочные значения валют (`money_supply_verification_<cur>`, `sell_<cur>_market_panel_verification`, `buy_<cur>_order`, `*_spe_to_add_*`, `buy_/sell_<cur>_market_panel` и др.) | `ef_currency_verification_values/` | 765 определений из `01_economic_currency_scripted_value.txt` (252 626 строк) |
| Значения и триггер валют без ссылок (`zz_ef_reserves_money`, `*_neg`, `zz_ef_cb_rule_*_pp`, `is_valid_country_for_currency_accumulation`) | `ef_unused_currency_values/` | 6 значений из `ld_reference_currency_values.txt` / `ld_cb_rate_values.txt`, триггер из `00_ef_custom_trigger.txt` |
| Остатки выдачи местной валюты (`zz_ef_local_currency_*`, `zz_ef_lc_curve_*`) | `ef_local_currency_issuance/` | четыре файла `ld_local_currency_*` целиком (в т.ч. on_action очистки модификатора) |
| Контроллер ставки E&F `base_rate_change` | `ef_base_rate_change/` | пустое определение из `01_economic_scripted_effects.txt`; вызов (`if is_ai`) в `00_on_action_main.txt` |
| Арбитраж частных банков E&F (`privat_bank_*_currency`, тела `buy/sell_currency_privat_bank`, флаги `attack_on_currency` и др.) | `ef_privat_bank_arbitrage/` | 5 `if` в `00_on_action_main.txt` (месяц, полугодие, год); 2 пустые обёртки, 2 тела, 6 осиротевших помощников из `01_economic_scripted_effects.txt`; `sell_currency_privat_bank_variable_list` из `08_list_effect.txt` |
| Печать/изъятие валюты по резерву `money_creation/destruction_in_foreign_exchange_reserve` | `ef_fx_reserve_money/` | два определения (3077 строк) из `01_economic_scripted_effects.txt` |
| Пустой `stockpile_finacial_product` | `ef_stockpile_finacial_product/` | определение из `01_financial_scripted_effects.txt`; `if` в месячном пульсе финцентра |
| Учёт финпродуктов `stockpiling_<вид>_1` (+ `_2_state`, 5 видов) | `ef_stockpiling_financial_1/` | 10 определений и баннер из `01_financial_scripted_effects.txt` |
| Годовой снимок индекса `fluctuations_country_indice_value_year(_clear)` | `ef_index_year_snapshot/` | два определения из `01_financial_scripted_effects.txt` |
| Группа PM `pmg_currency_type` (+ `pm_no_currency_type`, `pm_currency_liquidity_currency`) | `ef_pmg_currency_type/` | группа, два PM, закомментированная строка в `ef_15_bank.txt`, 3 ключа локализации |
| ИИ-стройка E&F `ai_building_strategy` (закомментированное тело, вызов отсутствующего `ai_build_privat_building_gold_mining`) | `ef_ai_building_strategy/` | 3304 строки из тела эффекта в `00_on_action_main.txt` (живые — частные ж/д ИИ — на месте) |
| Здание-пустышка `building_ef_private_construction`, 4 PM `pm_*_buildings_private`, PMG, кнопки `speculative_share_9..13` (ветка ИИ и снос), модификаторы, текстиконка, меши | `ef_private_construction_building/` | 3 файла целиком; эффект и вызов `building_ef_private_construction_modifier`; 5 scripted_button и sgui 13; 4 строки JE; обёртка в виджете; 2 static_modifier, тип модификатора, texticon, 6 строк `city_types`, ключи локализации |
| Товары национальных валют `<cur>_c` (закомментированы), их цвета, модификаторы `goods_input/output_<cur>_c_*` (300 типов), `bond_usa` | `ef_goods_currencies/` | 1 тыс. строк комментариев в `ef_00_goods.txt`; 95 цветов; 300 типов модификаторов и их ключи локализации; `bond_usa` |
| Значения PSC без ссылок (`command_economy_spending_mult`, `oversupply_limit`, `state_oversupply_limit`, `construction_price_weeks`, `construction_sector_efficiency_multiplier`) | `psc_unused_values/` | пять определений из `PSC_set_values.txt` / `PSC_construction_values.txt` |
| Вызов `initialize_historic_macro_facilities_ns` (эффекта нет) | `ef_initialize_macro_facilities/` | блок `if` в `history/buildings/00_ef_building.txt`; закомментированное определение; абзац комментария |
| `central_bank_production_methods_2` (+ `_2_act`) | `ef_central_bank_pm_subject_2/` | 2 определения (2682 строки) из `01_economic_scripted_effects.txt`; `if` в годовом шаге ЦБ; вызовы в двух sgui (`09_ef_other.txt`); закомментированные вызовы |
| Сбор очистки контрактов `contract_1_year` | `ef_contract_1_year/` | определение из `00_on_action_main.txt` |
| Месячный `ef_on_monthly_pulse_reset` | `ef_monthly_pulse_reset/` | закомментированные определение и вызов |
| События `.36`, `.37` (серебряный стандарт, внутренний долг) | `ef_events_silver_crisis_36_37/` | 2 события, 8 ключей локализации |
| События `.97 .971 .98 .981 .982 .100–.105` и их сообщения | `ef_events_97_105/` | 11 событий, 5 сообщений, 36 ключей локализации |
| Сообщения `unstable_currency_toast/_message` | `ef_messages_unstable_currency/` | 2 сообщения, 3 ключа локализации |
| Военные PM `pm_government_aid_*` (5), тип модификатора `goods_input_war_bond_add` | `ef_government_aid_pm/` | 5 PM, 2 строки в `unlocking_production_methods` (`pm_privately_owned_building_arms_industry` остался), тип модификатора и его ключи локализации |
| Группа зданий `bg_national_stockpile` | `ef_bg_national_stockpile/` | определение с баннером |
| Модификатор `modifier_test_supply` | `ef_modifier_test_supply/` | определение из `00_ef_dynamic_modifier_building.txt` |
| Триггеры без ссылок (95 `law_<cur>_monetary_system_FS_trigger` + 19 прочих) | `ef_unused_triggers/` | 114 определений из `00_ef_custom_trigger.txt` |
| Значения без ссылок в `00_economic_scripted_value.txt` (71) | `ef_unused_economic_values/` | 71 определение |
| Закомментированные алерты `buy_sell_<good>_order` | `ef_alerts_buy_sell_order/` | 29 закомментированных блоков, 87 ключей локализации |
| Пустой `on_monthly_pulse` журнала `financial_center_je_2` | `ef_je_empty_monthly_pulse/` | блок из `00_ef_financial_center_je.txt` |
| Тестовые окна `panel_*` (80), `currency_reserve_window`, хаб `ef_custom_windows` + кнопка «1» вкладки «Экономика», дубли `maj/{budget,market,states}_panel`, `maj/NonEssential/companies_panel` | `ef_dev_custom_windows/` | 82 `default_popup` из `ef_custom_windows.gui` (остался `gold_reserve_window`), кнопка `Panel_1` и закомментированная кнопка резервов в `ld_economy_panel.gui`, 4 файла `maj/`, 4 ключа локализации (en+ru) |
| Отладочный режим `EF_debug_mode` | `ef_debug_mode/` | виджет `00_ef_debug_widget.gui`, `EF_scripted_widgets.txt`, `00_ef_debug_decisions.txt`, 3 sgui из `09_ef_other.txt` |
| Скриптовые GUI без ссылок | `ef_unused_scripted_guis/` | 914 sgui из 4 файлов `common/scripted_guis/` + `com_local_goods_sgui.txt` |
| Осиротевшие после выноса GUI (значения, эффекты, sgui) | `ef_gui_orphans/` | 115 script_values, 24 эффекта `test_*_variable_list`, 37 sgui |
| Мёртвое в GUI и журналах E&F | `ef_gui_dead_leftovers/` | 6 типов `vo_plotline_*`, 2 виджета журнала, 4 пустые кнопки, 2 прогресс-бара, 2 понятия |
| Месячный торговый резерв `zz_ef_rc_step` | `ef_reserve_trade_step/` | закомментированный вызов в `ld_money_model.txt`; эффекты и 6 значений из генератора `regen_ef_reserve_trade` |
| Несортированная таблица валют ЦБ `zz_ef_cbfx_update` | `ef_cbfx_update/` | определение в `ld_cbfx.txt` и генераторе `regen_ef_clearing` |
| Строка расходов эмитента `zz_ef_foreign_bond_interest` | `ef_foreign_bond_interest/` | снятие модификатора в `ld_bond_ledger.txt` (и генераторе), значение `zz_ef_bond_interest_due_week` |
| Значения покупки металла населением `zz_ef_pop_gold_goods` / `_silver_goods` | `ef_pop_metal_goods_values/` | ничего — формула перенесена в `zz_ef_metal_week_step` (оптимизация) |
| Стартовые условия для Historical Map Mod (ветка `always = no`) | `ef_hmm_history/` | блок ~6000 строк в `99_ef_history_global_variable.txt` |
