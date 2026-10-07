# Точки входа и порядок шага
Мод подключается к движку через ванильные хуки `on_actions` (месячный/полугодовой/годовой/5-летний пульс страны, старт игры, создание страны, смена PM, бой) и через GLOBAL-блоки `common/history/*`. E&F вешает на хуки по одному «корневому» on_action, `ld_*` и PSC добавляют свои. Недельного пульса страны в движке нет: недельную цепочку модели денег ведёт самовозобновляемый on_action (`trigger_event = { on_action = ... days = 7 }`).

## Файлы
- `common/on_actions/00_ef_on_action.txt` — корневые on_action E&F (`ef_on_*_pulse_country`, `ef_on_production_method_changed`, `ef_on_battle_ended`, `com_topbar_setup_ef`).
- `common/on_actions/PSC_on_actions.txt` — PSC: распределение очков стройки по дням месяца, пересчёт метода конверсии при смене PM/технологии/постройке сектора.
- `common/on_actions/ld_*_on_actions.txt` — `ld_bank`, `ld_bubble`, `ld_capitalization`, `ld_cb_rate`, `ld_money_model` — месячные хуки модели; `common/on_actions/ld_new_country_immediate_init.txt`, `ld_stockpile_state_var_init` — инициализация переменных; `ld_pb_ai_sector_downsize`, `ld_pb_overbuild_counter` — штраф перестройки (PSC). Имена on_action и эффектов внутри сохранили префикс `zz_ef_*` / `zz_pb_ef_*`.
- `common/scripted_effects/00_on_action_main.txt` — 15 тыс. строк: все эффекты, которые зовут `ef_on_*`: пульсы ЦБ/ФЦ, ИИ-торговля валютой, ИИ-стройка, инфляция, исторические события по датам, сбросы счётчиков кризисов.
- `common/scripted_effects/10_new_country_var.txt` — `new_country_var_ef`: заводит все переменные страны и её штатов (34 тыс. строк).
- `common/history/global/*.txt`, `common/history/states/01_ef_states.txt`, `common/history/buildings/*.txt` — стартовые данные (см. «Старт игры»).
- `events/ld_new_country_immediate_init_events.txt` — скрытое событие `zz_ef_newcountry.1` (контекст для `new_country_var_ef` у освобождённой страны).
- `events/00_ef_economic_event.txt` — события E&F (запускаются из `ef_on_yearly_pulse_event_at_date` и эффектов); описаны в подсистеме ef-core.

## Поток / порядок
Все хуки списочные: порядок выполнения on_action из разных файлов не гарантирован (имена файлов не задают порядок; `ld_capitalization_on_actions.txt` собирает шаги в ОДИН on_action именно ради порядка). Пульсы размазаны по дням: месячный пересчитывает ~1/30 стран в день, годовой — ~1/365.

### При старте игры (новая кампания)
Порядок обработки: `common/history/buildings/*` (до global!) → `history/global/*` (по имени файла) → `history/states`.
| шаг | файл | что делает |
|---|---|---|
| 1 | `history/buildings/00_a_ef_history_var_init.txt` | заводит `country_already_financial_center=0`, `gdp_view_fc=5`, пока global ещё не отработал (иначе `financial_center_modifier` читает пустую переменную) |
| 1а | `central_bank_modifier`, `financial_center_modifier` (`09_introduction_building_lvl.txt`) | вызываются из истории до global: `central_bank_modifier` в историческом вызове не делает ничего, пока нет `base_demande_currency_fix` (модификаторы ставит первый месячный пульс `update_modifiers_bc_fc_ns`); `financial_center_modifier` вызывает `*_fixed_var` через сохранённую страну `scope:financial_center_country` (в истории `root` пуст) |
| 2 | `history/buildings/00_ef_building.txt` (4250 строк) | `BUILDINGS = { every_country }`: сначала `establish_bank_and_ef_compagnie` (компании-банки до центробанков), затем 221 `create_building` (ЦБ `building_bank`, финцентры, шахты), `financial_center_modifier`, `is_valid_country_hmm`; PM исторических шахт (`pm_no_explosives`, `pm_no_steam_automation`) |
| 3 | `history/buildings/PSC_buildings.txt` | при технологии `urbanization` — `building_construction_regulator` в каждом штате, `set_point_conversion_method_from_tech` |
| 4 | `history/global/00_ef_economic_global_variable.txt` (55 тыс.) | `GLOBAL = every_country`: ~6300 `set_variable` на страну (тестовые, золото/серебро, инфляция, кредитный рейтинг, переменные по каждой из 95 валют `<cur>`), ~3900 `set_global_variable` (флаги валют, `<cur>_global_monetary_reference_order_limitation`), ~1800 `add_to_global_variable_list` (`monetary_systeme_list`, `financial_product_list`, списки по валютам). Эффектов не зовёт. Блок `#begin_copy…#end_copy` копируется генератором в `10_new_country_var.txt` |
| 5 | `history/global/00_ef_financial_global_variable.txt` (2 тыс.) | переменные облигаций/акций/займов по странам (436 `set_variable`) |
| 6 | `history/global/00_ef_stockpile_global_variable.txt` | `looting_1_year` (счётчик грабежа ЦБ), `zz_ef_country_vars_set` (признак «страна уже инициализирована») |
| 7 | `history/global/01_ef_state_global_variable.txt` | `GLOBAL = every_state`: переменные штатов (`gold_state_1`, `silver_state_1`, `test_var_*`, `stockpiling_*_state_1`) |
| 8 | `history/global/99_ef_history_global_variable.txt` (2,7 тыс.) | исторические начальные условия: 312 `activate_law` (денежные системы, валюта страны), стартовые `gold_state_1`/`silver_state_1` через `var:central_bank_location`, `set_institution_investment_level`, `add_amendment` (биметаллические коэффициенты FRA/USA/NET и др.), 3 `create_pop`, `add_ideology = ideology_monetary_*` для ИГ |
| 9 | `history/global/PSC_global.txt` | `trigger_event = { on_action = set_construction_start }` — запуск PSC-стройки |
| 10 | `history/global/zz_ef_currency_fix.txt` | после 99: валюта WUR; страны без валюты → `law_no_market_liquidity`; `currency_standards` странам с подушным налогом |
| 11 | `history/global/zz_ef_init_stockpiling_state_vars.txt` | заводит 7 переменных `stockpiling_*_var_state_1` штатам (охрана `has_variable`) |
| 12 | `history/states/01_ef_states.txt` | `s:STATE_X = add_modifier silver_mine_max_level` (60 штатов, множитель = макс. уровень серебряной шахты) |
После лобби `on_game_started_after_lobby`: `com_topbar_setup_ef` (E&F: добавляет 7 элементов верхней панели `com_topbar_element_inflation / law_*_standard / law_subject` и ставит их всем странам в `com_topbar_second_line`) и `zz_ef_init_stockpile_state_vars` (`ld_stockpile_state_var_init.txt`: `zz_ef_seed_stockpile_state_vars` — проход `every_state` для старых сейвов). PSC: `set_construction_start` (из history) → `set_construction_weekly_on_action` + `set_construction_country` для каждой страны.

### При создании страны
| ванильный хук | эффекты | подсистема |
|---|---|---|
| `on_country_formed`, `on_become_independent` | `zz_ef_newcountry_on_*` → если нет `var:zz_ef_country_vars_set` → `new_country_var_ef` | инициализация переменных |
| `on_country_released_as_independent / _own_subject / _company_subject / _overlord_subject` | `zz_ef_newcountry_on_*` → `scope:target = trigger_event zz_ef_newcountry.1` (скрытое событие, ROOT = новая страна) → `new_country_var_ef` | то же (в событии, чтобы ROOT был новой страной, а не сюзереном) |
| месячный пульс (страховка) | `ef_on_monthly_pulse_recurence` (строки 20–242 `00_on_action_main.txt`): для не инициализированной страны (нет `zz_ef_country_vars_set`) → `new_country_var_ef`; при отсутствии банка — `law_no_monetary_system` + `law_no_market_liquidity`; при наличии — `remove_building building_bank`, `central_bank_modifier`, те же законы; `foreign_exchange_controls` на 23 месяца. Для `is_revolutionary` — такой же блок первым | инициализация / валютный режим |
Идемпотентность: все вызовы защищены `not has_variable = zz_ef_country_vars_set` (флаг ставит сам `new_country_var_ef`). Порядок внутри `new_country_var_ef`: состояния, экономика, финансы, грабёж (`looting_1_year`).

### Месячный пульс страны (`on_monthly_pulse_country`)
Список on_action на хуке (порядок между файлами не гарантирован):
| on_action | эффекты по порядку | подсистема |
|---|---|---|
| `ef_on_monthly_pulse_country` (E&F) | 1) `ef_on_monthly_pulse_recurence`: `update_modifiers_bc_fc_ns`, `com_topbar_save_game_compatibility_EF`, `remove_suject_currency`/`subject_currency` (валюта сюзерена для подданных), `is_at_war_monthly_pulse`, `is_in_revolution_monthly_pulse`, `maximum_number_companies_exceeded_monthly_pulse`, блоки «новая страна» (см. выше); 2) если `has_central_bank`: `central_bank_ef_on_monthly_pulse_country` (ниже) | ядро E&F |
| `central_bank_ef_on_monthly_pulse_country` (порядок) | `currency_strength_modifier`, `government_loan_month`, `inflation_modifier`, 5× `inflation_on_*_market_value_fluctuations` (потребит./энерг./сырьё/промтовары/воен.), `money_value_dif_01_market_value_fluctuations`; страна №1 по рангу: `global_gold_silver_production` и при нулевой медиане `currency_law_list`+`money_value_global_var`+`median_currency_value`; держатель `global_monetary_reference`: `global_monetary_reference_global_var_fixe`; игрок: `monetary_policy_inflation_base_rate`, `monetary_policy_inflation`/`_reset`/`_reset_law`; рынок свой: `stockpiling_currency`, `trade_balance`; при `foreign_exchange_controls`: `devaluation_on`/`revaluation_on` | ЦБ / инфляция |
| `zz_ef_bank_monthly` (`ld_bank`) | `zz_ef_bank_seed_step` — посев частных банков при первом пульсе | модель денег: банки |
| `zz_ef_bubble_monthly` (`ld_bubble`, условие: JE `financial_center_je_2` и `var:speculative_share_1`) | пузырь `speculative_share_1`, модификаторы `speculative_bubble_*`, уведомление `zz_ef_bubble_rising` | фин. центр / пузырь |
| `zz_ef_capitalization_monthly` (`ld_capitalization`) | `zz_ef_stock_issue_update`, `zz_ef_listing_update`, `zz_ef_cap_monthly_update`, `zz_ef_listing_log`, `zz_ef_cap_monthly_crash_check`, затем `zz_ef_mass_shareholding` (модификатор по `zz_ef_msh_points`) | акции / капитализация |
| `zz_ef_cb_rate_monthly` (`ld_cb_rate`) | `zz_ef_risk_monthly`; счётчик `zz_ef_cb_rate_month` 0..2, на 3 — `zz_ef_cb_rate_step` (квартальный шаг ставки ЦБ); сид `zz_ef_rate_bias` | ставка ЦБ |
| `zz_ef_money_model_monthly` (`ld_money_model`) | `zz_ef_money_model_monthly_step` (порядок: `zz_ef_cur_zone_step`, `zz_ef_silver_rate_update`, `zz_ef_reference_strength_step`, `zz_ef_currency_trade_step`, `zz_ef_privbank_interest_pay`, `zz_ef_rate_policy_costs`, `zz_ef_gov_rate_step`, `zz_ef_mp_step`; лог EFX), затем `zz_ef_money_week_start` (перезапуск недельной цепочки) | модель денег |
| `zz_pb_ef_ai_sector_downsize` (`ld_pb_ai_sector_downsize`; условие: ИИ, `base_rate_percentage`) | таймер `zz_pb_ef_ai_downsize_timer`, раз в 3 мес. при `speculative_share_2>=10` и избытке секторов — `zz_pb_ef_css_downsize_one` | PSC: перестройка |
| `zz_pb_ef_overbuild_counter` (`ld_pb_overbuild_counter`) | индекс `speculative_share_2` (шаг `zz_pb_ef_overbuild_step`), модификатор `zz_pb_ef_overbuilt_economy`, уведомление `zz_pb_ef_overbuild_rising`, полоса JE | PSC: перестройка |
| `zz_ef_init_stockpile_state_vars_monthly_backstop` (`ld_stockpile_state_var_init`) | `zz_ef_seed_stockpile_state_vars_backstop` — один проход за игру по глобальной переменной | инициализация |
Хук `on_monthly_pulse` (не страновый) — PSC: `set_construction_weekly_on_action` (раскладывает `set_construction_country` и `set_spending_value` по дням месяца через `delay_event_switch`).

### Недельная цепочка модели денег
`zz_ef_money_week_start` (из месячного шага; если нет `zz_ef_week_alive`) → `zz_ef_money_week_probe` ежедневно до смены `zz_ef_budget_position` (бюджетный тик, не более 8 дней) → `zz_ef_money_model_weekly`: при первом вызове — `zz_ef_money_week_slot_assign` (день недели страны `var:zz_ef_week_slot` = счётчик стран `global_var:zz_ef_week_slot_n` по модулю 7; слот 0 — шаг сейчас, слот N — через N дней), дальше `zz_ef_money_model_step` + повторный запуск через 7 дней. Так шаги и приёмники моста ~269 стран разнесены по 7 дням; окна клиринга и мировых сумм — глобальные по 7 дней, каждая страна попадает в окно один раз. Перезапуск цепочки зондом снимает слот — страна получает его заново. Порядок в `zz_ef_money_model_step` (`ld_money_model.txt` 101–464): `zz_ef_probe_newyear_cash`, `zz_ef_fx_metal_update`, `zz_ef_cbfx_week_step`, `zz_ef_cb_state_owner_step`, `zz_ef_bond_ledger_step`, `zz_ef_metal_start_step` (+ `_cb_before`, `zz_ef_metal_rescale_step`, `_cb_after`, `zz_ef_metal_start_log`), `zz_ef_consol_step`, `zz_ef_business_credit_step`, `zz_ef_metal_week_step`, далее агрегаты M0..M3 и лог EFW; `zz_ef_money_hook_receive` вызывается из хуков E&F.
PSC-хук: `on_production_method_changed`, `on_building_built`, `on_acquired_technology` (см. PSC).

### Полугодовой пульс (`on_half_yearly_pulse_country`)
`ef_on_half_yearly_pulse_country`:
| условие | эффекты |
|---|---|
| всегда | `ef_on_half_yearly_pulse_recurence`: `ai_building_strategy` (ИИ строит частные железные дороги в штатах с `state_market_access < 0.80`), `fluctuations_gdp_1_year`, `economic_sentiment_index_base_JE_fixe_half_year_pulse`, `law_no_monetary_system` |
| `has_central_bank` | `central_bank_ef_on_half_yearly_pulse_country`: игрок — `monetary_policy_ideology_dynamic`; `has_central_bank_SS_BS_GS_GES_NISO` — `fluctuations_money_value_1_year`, `leading_producer_of_oil`; ИИ — `ai_credit_at_central_bank`, `ai_refund_central_bank`; золотой обменный — `reference_currency_in_gold_fixe`; береговые порты — `is_treaty_port_disable_pm_market_liquidity`; ранг №1 — `fluctuations_silver_to_gold_rate_1_year`, `global_arbitrage_bank_variable_list`; ИИ — `base_rate_change` (пустое тело); `crisis_general_reset_count`; держатель `global_monetary_reference` — `privat_bank_buy_currency` (пустое) |
| `has_financial_center` | `financial_center_ef_on_half_yearly_pulse_country`: только `interest_per_month_from_foreign_debt_investment` (снимок/крах капитализации вынесены в месячный `zz_ef_cap_monthly_*`) |
| `global_monetary_reference` | `money_value_global_var` |

### Годовой пульс (`on_yearly_pulse_country`)
`ef_on_yearly_pulse_country` по порядку: (держатель `global_monetary_reference`) `national_capacity_variable_list`, `country_index_variable_list`, `central_bank_debt_variable_list`, `currency_law_list`, `median_currency_value`, `global_monetary_reference_1` → `ef_on_yearly_pulse_recurence` (`fluctuations_gdp_5_year`, `_10_year`, `is_at_war_years_pulse`) → `ef_on_yearly_pulse_reset` (сбросы лимитов, `looting_1_year_on_action` — `common/scripted_effects/01_stockpile_scripted_effects.txt`, обнуление годового счётчика грабежа, 29× `clear_<good>_contract_1_year`) → `central_bank_ef_on_yearly_pulse_country` (проценты ЦБ в золоте, `investement_pool_borrowing`, накопленная инфляция, `ai_buy_sell_currency`+`monetary_systeme_transition` для ИИ, `credit_at_central_bank_interest_per_week[_off]`, `central_bank_production_methods`, `_3` для золотого обменного стандарта, `money_value_target_modification`, `extreme_weak_currency_solution[_player]`, `establish_bank_and_ef_compagnie` для ИИ, `*_count_reset_condition`, арбитраж биметаллизма до 1873 `private_bank_arbitrage_gold_drain/_silver_drain`) → `financial_center_ef_on_yearly_pulse_country` (`private_ownership_production_stocks`, `financial_center_production_methods`, `ai_buy_central_bank_debt`, `sovereign_bond_yields`, `bond_maturity_on_action`, `financial_crash_count_reset_condition`) → `country_credit_rating` (ранг ≥ unrecognized_power) → `gdp_view_on_action`, `macro_facilities_on_action_bc`, `has_tech_central_bank_but_no_building_central_bank`, `has_currency_law_but_no_building_central_bank`, `gdp_view_on_action_fc`, `has_tech_financial_center_but_no_building_financial_center`, `has_second_financial_center` → `ef_on_yearly_pulse_event_at_date` (исторические события по датам: объединение Германии/Италии, события `00_ef_economic_event.5..65`, `silver_crisis_progress`).

### 5-летний пульс
- `on_five_year_pulse_country` → `ef_on_five_year_pulse_country`: ЦБ — `central_bank_ef_on_five_year_pulse_country` (ИИ не подданный: `money_value_target_modification`; страна №1: `scandinavian_leader_list_1_list`); ФЦ — `fiancial_center_ef_on_five_year_pulse_country` (`position_regulator`).

### Прочие хуки
| хук | on_action → эффекты |
|---|---|
| `on_production_method_changed` | `ef_on_production_method_changed`: владелец → `financial_center_production_methods` (если ФЦ), `private_ownership_production_stocks`; PSC `on_construction_sector_method_changed` → `set_new_point_conversion_method` (если сектор) |
| `on_battle_ended` | `ef_on_battle_ended` → `enemy_stats_is_occuped` при `enemy_stats_is_occuped >= 1` |
| `on_acquired_technology` (PSC) | `on_acquired_construction_tech` → `set_point_conversion_method_from_tech` |
| `on_building_built` (PSC) | `on_construction_sector_built` → `set_new_point_conversion_method` |
| решение `00_ai_loooting_decisions_1` (ИИ) | `enemy_capital_is_occuped` (грабёж ЦБ-штата), событие `00_ef_economic_event.35` игрокам; `looting_1_year_on_action` годом |

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `zz_ef_country_vars_set` | страна уже инициализирована E&F | `new_country_var_ef` (рядом с `looting_1_year`), history `00_ef_stockpile_global_variable` | `ef_on_monthly_pulse_recurence`, `zz_ef_newcountry_*`, `ld_new_country_immediate_init` |
| `base_rate_percentage` | ставка ЦБ (признак инициализации для `zz_pb_ef_*`) | `new_country_var_ef`, `zz_ef_cb_rate_step` | `zz_pb_ef_overbuild_counter`, `zz_pb_ef_ai_sector_downsize` |
| `zz_ef_week_slot`, `global_var:zz_ef_week_slot_n` | день недели шага страны (0..6) / счётчик выданных слотов | `zz_ef_money_week_slot_assign` | `zz_ef_money_model_weekly` |
| `zz_ef_week_alive`, `zz_ef_week_probe[_value]` | жив ли недельный цикл / зонд бюджетного тика | `zz_ef_money_week_start`, `_probe_step`, `zz_ef_money_model_step` | те же |
| `zz_ef_cb_rate_month` | счётчик месяцев до шага ставки (0..2) | `zz_ef_cb_rate_monthly` | оно же |
| `speculative_share_1` / `_2` | пузырь (0..100) / индекс перестройки (0..100) | `zz_ef_bubble_monthly` / `zz_pb_ef_overbuild_counter` | JE `financial_center_je_2`, модификаторы |
| `last_construction_run` | дата последнего PSC-пересчёта | `set_construction_country` | PSC |
| `country_already_financial_center`, `gdp_view_fc` | стартовые флаги ФЦ | `00_a_ef_history_var_init`, history global | `financial_center_modifier` |
| `global_monetary_reference` (модификатор) | единственная страна — держатель общих списков/медианы | `global_monetary_reference_1` | `ef_on_*` гейты |

## Вызовы и связи
- Модель денег `ld_*`: месячные хуки зовут эффекты из `common/scripted_effects/ld_*.txt`; из тел E&F зовутся `zz_ef_cb_rate_step`, `zz_ef_std_switch_before/after`, `zz_ef_privbank_interest_pay`, `zz_ef_mp_init/_clear`, `zz_ef_crisis_redeem` (в `01_economic_scripted_effects.txt`), `zz_ef_cur_intro_after` (в `09_introduction_building_lvl.txt`).
- Эффекты E&F, пишущие `gold_state_1` / `silver_state_1` ЦБ-штата (счета модели): арбитраж `private_bank_arbitrage_*_drain` (годовой), `enemy_capital_is_occuped`, `buy_/sell_<cur>_currency` (через `ai_buy_sell_currency`), стартовые значения `99_ef_history_global_variable.txt`.
- GUI: верхняя панель — `com_topbar_setup_ef`; пульсы GUI не вызывают, но scripted_guis зовут `reset_*`, `stockpiling_capital_state_transfert`, `reset_debt_in_national_currency_player`.

## Логи
Логи пишутся `debug_log` в `game.log`/`debug.log`, формат `EFx|дата|страна|метка|поле значение|…`. **Все записи — только при условии `zz_ef_logs_on`** (`common/scripted_triggers/ld_logs_triggers.txt`): правило игры «Ledgerdemain: отладочные журналы» (`common/game_rules/ld_game_rules.txt`, по умолчанию выключено; локализация `ld_game_rules_l_*.yml`) или глобальная переменная `zz_ef_logs_on` — её ставит скрытое событие `zz_ef_logs.1` (`events/ld_logs_events.txt`, консоль `event zz_ef_logs.1`; скрипт прогона песочницы шлёт его сам). Каждая строка обёрнута: `if = { limit = { zz_ef_logs_on = yes } debug_log = "…" }`; эффект `zz_ef_money_log_rest` (только строки лога) — условием в месте вызова. Гейтов-флагов нет, кроме отмеченных. Эффекты ниже — единицы кода, на каком шаге вызываются указано в колонке «шаг».
| префикс | файл:строка | что пишет | шаг |
|---|---|---|---|
| EFE | `common/scripted_effects/08_list_effect.txt:210,267,288` | великие державы: рейтинг (`country_credit_note_fixe`), покрытие, резервы в золоте; кандидаты на эталонную валюту; выбранная (`pick`) | годовой, `national_capacity_variable_list` (держатель `global_monetary_reference`) |
| EFL | `common/scripted_effects/ld_listing.txt:79` | уровни HQ, доля листинговых, дивиденды, капитализация, `cap_gdp`, дисконт | месячный `zz_ef_capitalization_monthly` → `zz_ef_listing_log` |
| — (`ZZEF crash`) | `common/scripted_effects/ld_capitalization_crash.txt:112` | `debug_log` + `debug_log_scopes`: капитал упал более чем вдвое за год | месячный `zz_ef_cap_monthly_crash_check` |
| EFK | `common/scripted_effects/ld_bank_seed.txt:36` | рынок: уровни банков (`zz_ef_bank_l`), `tc` (`zz_ef_bank_w`) | месячный `zz_ef_bank_seed_step` |
| EFK | `common/scripted_effects/ld_bank_seed.txt:570` | штат: желаемое число банков (`zz_ef_bank_n`) | `zz_ef_bank_seed_state` |
| EFM | `common/scripted_effects/ld_money_model.txt:48` | уплата процента частным банкам (`zz_ef_f_pbi_paid`) | месячный, `zz_ef_privbank_interest_pay` |
| EFM | `common/scripted_effects/ld_monetary_policy.txt:65,130,179` | `done` (завершение девальвации/ревальвации: покрытие, цель), `step` (шаг: направление, взведён ли), `ai_parity` (ИИ меняет паритет) | месячный `zz_ef_mp_step`; `zz_ef_mp_complete` |
| EFM | `common/scripted_effects/ld_standard_switch.txt:130` | смена денежного стандарта: старый/новый паритет | на смене закона, `zz_ef_std_switch_after` (из `01_economic_scripted_effects.txt:27974`) |
| EFM | `common/scripted_effects/ld_metal_accounts.txt:126` | `metal_start`: начальный металл ЦБ, что сделано | недельный, `zz_ef_metal_start_log` |
| EFM | `common/scripted_effects/ld_subject_metal.txt:40` | `cb_state_lost` (ЦБ-штат потерян) | недельный `zz_ef_cb_state_owner_step` |
| EFM | `common/scripted_effects/ld_currency_intro_metal.txt:62` | `cur_intro`: ввод новой валюты, металл | `zz_ef_cur_intro_after` (из `09_introduction_building_lvl.txt:34463`) |
| EFT | `common/scripted_effects/ld_metal_accounts.txt:351` | потоки металла ЦБ/банков/населения за неделю | недельный `zz_ef_metal_week_step` |
| EFV | `common/scripted_effects/ld_metal_accounts.txt:358` | WORLD: суммы металла по ЦБ/банкам/населению, баланс закупок/продаж | недельный `zz_ef_world_metal_log` (из `ld_money_model.txt:742`) |
| EFQ | `common/scripted_effects/ld_metal_accounts.txt:400` | сверка металла (`oth_g/oth_s`, ЦБ, стандарт) | `zz_ef_metal_reconcile` |
| EFB | `common/scripted_effects/ld_bond_ledger.txt:95` | книга облигаций страны: принципал, на руках, проценты, погашение, списание | недельный `zz_ef_bond_ledger_step` |
| EFP | `common/scripted_effects/ld_bond_ledger.txt:571` | слот облигаций без продавца (`no_seller`) | `zz_ef_pb_no_seller` (слот `$N$`) |
| EFS | `common/scripted_effects/ld_consols.txt:52` | консоли: долг, продажа, проценты, цена, цель ставки | недельный `zz_ef_consol_step` |
| EFN | `common/scripted_effects/ld_nr_deposits.txt:118` | обрезка обязательств иностранных вкладов (`trim`) | `zz_ef_fx_liab_trim` |
| EFW | `common/scripted_effects/ld_money_model.txt:392` | M0..M3, оборот, ЦБ, заграница, дельты (только игрок или ВВП > 20 млн) | недельный `zz_ef_money_model_step` |
| EFG | `common/scripted_effects/ld_money_model.txt:743` | WORLD: потоки валюты по миру, клиринг | недельный (через `zz_ef_world_acc`) |
| EFA | `common/scripted_effects/ld_money_model.txt:504` | проценты, ЦБ, прямые инвестиции | `zz_ef_money_hook_receive` |
| EFR | `common/scripted_effects/ld_money_model.txt:540` | внешние потоки, сбережения, депозиты, пул банков | `zz_ef_money_hook_receive` |
| EFX | `common/scripted_effects/ld_money_model.txt:1033` | стандарт, ЦБ, `money_value_0`, цель, покрытие, металл, M2 | месячный `zz_ef_money_model_monthly_step` |
| EFC | `common/scripted_effects/ld_money_model.txt:1305,1307` | кризисный выкуп валюты: должно/выплачено; эмитент | `zz_ef_crisis_redeem` (из `buy_/sell_<cur>_currency_crisis`) |
| EFO / EFF | `common/scripted_effects/ld_money_log_rest.txt:5` / `6–10` | остаток баланса / статьи по зданиям, банкам, заграничные, казна, ЦБ | недельный `zz_ef_money_log_rest` (из `ld_money_model.txt:544`) |
Других `debug_log` в `common/` и `events/` нет (grep по `debug_log` и `log =`).
