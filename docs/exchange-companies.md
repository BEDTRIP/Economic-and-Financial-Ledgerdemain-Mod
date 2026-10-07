# Биржа, компании, финансовый центр
Национальная биржа (здание `building_financial_centre*`, 42 вида) даёт стране модификатор `has_financial_center` и слоты компаний.
Раз в месяц по стране: считается доля публичных штаб-квартир (ШК) компаний, капитализация рынка акций, скользящие
средние, индекс рынка, проверка краха, «пузырь», массовое владение акциями. Компании E&F — в основном банки
(105 типов), связаны со зданиями `building_company_<ключ>` и биржевыми зданиями.

## Файлы
Все ключи `ld_*` файлов начинаются с `zz_ef_` (имя файла `ld_`, ключ `zz_ef_`); комментарии внутри ссылаются на старые имена файлов `zz_ef_*.txt`.
- `common/company_types/00_ef_companies.txt` — 105 типов компаний E&F (банки по странам + `company_PennsylvaniaRailroad`, `company_standard_oil`, `company_private_construction`, `company_basic_gold_and_silver_mining_2`, `company_basic_gold_mining_rus`, `company_basic_silver_mining_mex`); `replaces_company` — подмена старых ключей; `building_types` — `building_zz_ef_bank` (98 раз, `common/buildings/ld_bank.txt`) или `building_financial_centre_<код>`.
- `common/game_rules/00_EF_unique_companies_game_rules.txt` — правила `unique_companies_banks`/`unique_companies_newspapers` (по умолчанию `*_disabled`, флаги).
- `common/script_values/01_economic_company_value.txt` (99849 строк) — НЕ биржа, а фонды частных банков: `total_bank_funds`, `funds_from_foreign_debt(_total)`, `company_<банк>_fund` (99 штук, по одному на банк), `private_bank_*_reserve*`, `ai_privat_bank_{bond_quantity,bond_value,interest_calculated}_<1..25>_from_list` (по ~700 строк на шаблон). Подсистема банков; здесь — только связь.
- `common/scripted_effects/ld_listing.txt` — `zz_ef_listing_update` (месячный перевод ШК в «публичные/частные»), `zz_ef_listing_log` (лог `EFL|`).
- `common/scripted_effects/ld_listing_switch.txt` — ГЕНЕРИРУЕТСЯ (`tools/regen_ef_listing.py` в vic3_mods): `zz_ef_listing_go_public`, `zz_ef_listing_go_private` — диспетчер по 271 типу ШК (`building_company_*` ванили и E&F; `activate_production_method` берёт тип литералом).
- `common/script_values/ld_listing_values.txt` — `zz_ef_hq_levels/_count/_div_week`, `zz_ef_listed_hq_levels`, `zz_ef_listed_share`, `zz_ef_listed_div_year`, `zz_ef_equity_premium` (0.04), `zz_ef_cap_discount`, `zz_ef_cap_listed_snapshot`, `zz_ef_cap_to_gdp`.
- `common/scripted_triggers/ld_listing_triggers.txt` — `zz_ef_listing_allowed` (биржа ур.≥1 + технология `joint_stock_companies` + не традиционализм/командная/кооперативная экономика).
- `common/production_methods/ld_company_hq_publicly_traded.txt` + `common/production_method_groups/ld_company_hq_publicly_traded.txt` — `pm_company_headquarter_publicly_traded`, добавлен INJECT в `pmg_ownership_building_company_headquarter`.
- `common/scripted_effects/ld_capitalization_average.txt` — `zz_ef_cap_monthly_update`: 4 скользящих средних, `zz_ef_cap_half`, индекс `base_index_value`, `base_index_value_dif`.
- `common/scripted_effects/ld_capitalization_crash.txt` — `zz_ef_cap_monthly_crash_check`: 12 месячных отметок, `country_indice_value_dif_01`, вызов `financial_crash`.
- `common/script_values/ld_capitalization_snapshot.txt` — `zz_ef_cap_weeks`(520), веса средних, `zz_ef_crash_floor`(5 млн), `zz_ef_cap_state_output_*_stock`, `zz_ef_cap_qty_*`, `zz_ef_cap_snap_*`, `zz_ef_equity_capitalization`.
- `common/on_actions/ld_capitalization_on_actions.txt` — `zz_ef_capitalization_monthly` (в `on_monthly_pulse_country`), задаёт порядок шагов.
- `common/on_actions/ld_bubble_on_actions.txt` + `common/script_values/ld_bubble_values.txt` + `common/messages/ld_bubble_messages.txt` — «пузырь» `speculative_share_1`: `zz_ef_bubble_monthly`, `zz_ef_bubble_step(_eff)`, `zz_ef_bb_band_*`, сообщение `zz_ef_bubble_rising`.
- `common/script_values/ld_mass_shareholding_values.txt` + `common/static_modifiers/ld_mass_shareholding.txt` — `zz_ef_mass_shareholding_points/_max`, модификатор `zz_ef_mass_shareholding` (`building_company_worker_dividends_add`).
- `common/scripted_effects/ld_stock_issue_literacy.txt` + `common/script_values/ld_stock_issue_literacy_values.txt` + `common/static_modifiers/ld_stock_issue_literacy.txt` — `zz_ef_stock_issue_update`, `zz_ef_stock_issue_cut_points`, модификатор `zz_ef_stock_issue_literacy` (−выпуск 4 видов акций).
- `common/script_values/ld_company_slots.txt` — `zz_ef_slots_rating/_cb/_cap`, `zz_ef_cap_total`; читаются в `value_for_has_financial_center` (`common/script_values/00_economic_scripted_value.txt:4617`).
- `common/buildings/ef_16_financial_centre.txt` — `building_financial_centre` (общий) + 41 национальный вид `building_financial_centre_<код>` (по столице/региону, `bg_financial_centre`, технология `financial_center`).
- `common/production_methods/16_ef_financial_centre.txt` + `common/production_method_groups/16_ef_financial_centre.txt` — 5 групп: `pmg_{manufacture,agricultural,mining,railroad}_stock_exchange` (`pm_no_*` / `pm_*_stock_exchange`, вход `goods_input_<вид>_stock_add`), `pmg_bond_exchange` (`pm_bond_exchange`).
- `common/journal_entries/00_ef_financial_center_je.txt` — `financial_center_je_1` (выдаёт технологии `stock_exchange`/`financial_center` по `gdp_var` 2.5 млн / 5 млн), `financial_center_je_2` («Управление финансовой стабильностью»: шкала пузыря, кнопки `speculative_share_N_button`, виджеты `gui/scripted_widgets/ld_pb_fso_widgets.gui`; `on_monthly_pulse` пустой — пузырь двигает on_action).
- `common/production_methods/ld_trade_center_settlements.txt` — INJECT в `pm_trade_center` и `pm_trade_center_principle_external_trade_2`: `goods_output_liquidity_currency_add = 60` (расчёты-ликвидность).
- Биржевая часть E&F вне перечисленного: `common/script_values/00_financial_scripted_value.txt` (`country_indice`, `stock_market_index`, `<вид>_stock_price/_index`, `stockpiling_<вид>_var_state` — переписаны на скользящие средние), `common/scripted_effects/01_financial_scripted_effects.txt` (`financial_crash` 33541, `financial_crash_consequences` 34007, `bankrupt_company` 34260), `common/scripted_effects/09_introduction_building_lvl.txt:22135` (`financial_center_modifier`, вешает `has_financial_center` с множителем), `common/scripted_effects/00_on_action_main.txt:626` (`financial_center_ef_on_half_yearly_pulse_country`, сейчас без биржевой логики).

## Поток / порядок
`on_monthly_pulse_country` → `zz_ef_capitalization_monthly` (`ld_capitalization_on_actions.txt`), страна, по порядку:
1. `zz_ef_stock_issue_update` — один проход по попам: `zz_ef_literate_rich_share`, `zz_ef_rich_literacy`; пересадка модификатора `zz_ef_stock_issue_literacy` (множитель `zz_ef_stock_issue_cut`).
2. `zz_ef_listing_update` — если `zz_ef_listing_allowed`: ШК (`bg_company_headquarter`) по возрастанию уровня переводятся в `pm_company_headquarter_publicly_traded`, пока накопленные уровни < всех уровней ШК × `zz_ef_rich_literacy`; остальные — `pm_company_headquarter_privately_owned`. Без разрешения — все ШК в частные.
3. `zz_ef_cap_monthly_update` — снимок = `zz_ef_cap_listed_snapshot` (дивиденды публичных ШК за год ÷ (ставка правительства `zz_ef_gov_rate_target` + 4 п.п.), min 0.02) делится по 4 акциям пропорционально выпуску (`zz_ef_cap_snap_*`), обновляются `zz_ef_cap_avg_{ms,as,mn,rr}` (вес 0.0833), `zz_ef_cap_half` (вес 0.1667), `base_index_value` = капитализация/ВВП × 1000, раз в 12 мес. `base_index_value_dif`.
4. `zz_ef_listing_log` — строка `EFL|`.
5. `zz_ef_cap_monthly_crash_check` — отметки `zz_ef_cap_m1..m12`, `country_indice_value_dif_01 = half/m12 − 1`; крах (`financial_crash`), если < −50%, нет `zz_ef_cap_crash_cooldown` (15 мес), есть `has_financial_center`, капитализация > `zz_ef_crash_floor`, дата ≥ 1838.1.1.
6. Массовое владение: `remove_modifier`/`add_modifier zz_ef_mass_shareholding` с множителем `zz_ef_msh_points` (= капитализация/ВВП, max 1 × `literacy_rate` × 25).
Отдельный on_action `zz_ef_bubble_monthly` (`ld_bubble_on_actions.txt`, `on_monthly_pulse_country`; условие: есть `financial_center_je_2` и `speculative_share_1`): сдвиг пузыря −3..+3 по `fiancial_center_week_balance_in_ratio`, прогресс-бар, сообщение при входе в новую десятку, модификаторы `speculative_bubble_modifier` и `speculative_bubble_character_modifier` (на исполнителей).
Слоты компаний: `has_financial_center` с множителем `value_for_has_financial_center` = `zz_ef_slots_rating` (0..5, из `country_credit_note_fixe`/2) + `zz_ef_slots_cb` (0..5, от ставки ЦБ `zz_ef_money_rate`) + `zz_ef_slots_cap` (0..10, +1 за каждые 10% ВВП).
Прочее: `financial_center_je_1` (месячный пульс) выдаёт технологии биржи по ВВП; крах → `economic_instability`; при втором кризисе в `01_financial_scripted_effects.txt:33782` — `financial_crash_consequences` (разрушает биржи, `government_loan`, `add_investment_pool`, `bankrupt_company`).

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `zz_ef_literate_rich_share` | доля грамотных богатых (wealth ≥15) среди всех попов | `zz_ef_stock_issue_update` | `zz_ef_stock_issue_cut_points` |
| `zz_ef_rich_literacy` | грамотность самих богатых, 0..1 | `zz_ef_stock_issue_update` | `zz_ef_listing_update`, лог |
| `zz_ef_stock_issue_cut` | процентные пункты срезa выпуска акций | `zz_ef_stock_issue_update` | модификатор |
| `zz_ef_cap_avg_ms/_as/_mn/_rr` | годовая средняя капитализации (производство/сельхоз/добыча/ж.д. акции) | `zz_ef_cap_monthly_update` | `stockpiling_<вид>_var_state`, `zz_ef_cap_total` |
| `zz_ef_cap_half` | средняя за полгода по всем акциям | `zz_ef_cap_monthly_update` | краш-проверка |
| `zz_ef_cap_m1..m12` | месячные отметки `zz_ef_cap_half` | `zz_ef_cap_monthly_crash_check` | она же |
| `zz_ef_cap_crash_cooldown` | таймер 15 мес после краха | краш-проверка | она же |
| `country_indice_value_dif_01` | изменение капитализации за год (E&F читает в `financial_crash`) | краш-проверка | меню E&F, `financial_crash` |
| `base_index_value`, `base_index_value_dif`, `zz_ef_cap_idx_prev`, `zz_ef_cap_idx_timer` | индекс рынка (пункты), прирост за год | `zz_ef_cap_monthly_update` | `stock_market_index`, `gui/ld_cb_rate_panel.gui` |
| `zz_ef_msh_points` | пункты `building_company_worker_dividends_add` | `zz_ef_capitalization_monthly` | модификатор |
| `speculative_share_1` | пузырь 0..100 | `zz_ef_bubble_monthly`, кнопки `speculative_share_N_button` (E&F) | JE, `ld_pb_fso_sguis.txt`, `zz_ef_bubble_step_eff` |
| `zz_ef_bb_old` | пузырь до шага (для уведомления) | `zz_ef_bubble_monthly` | `zz_ef_bb_band_old` |
| локальные `zz_lst_*`, `zz_s_*`, `zz_lr_*` | счётчики внутри эффектов | listing/average/issue | они же |

## Вызовы и связи
- Читает чужое: `zz_ef_gov_rate_target`, `zz_ef_money_rate` (подсистема ставки ЦБ), `country_credit_note_fixe` (рейтинг), `gdp`, `literacy_rate`, `weekly_profit` ШК (доход ШК = дивиденды), `<вид>_stock_price` (E&F), `fiancial_center_week_balance_in_ratio` (E&F).
- Пишет в чужое: `has_financial_center` (слоты), `financial_crash`/`economic_instability` (E&F), `building_company_worker_dividends_add` и выпуск акций на всю страну.
- `stockpiling_<вид>_var_state` (`00_financial_scripted_value.txt:2904`…) переведены с накопления на `zz_ef_cap_avg_*` / цену — их читают `country_indice`, меню E&F, рейтинг финансовой мощи.
- GUI: `gui/ld_cb_rate_panel.gui` (`stock_market_index`, `country_indice`, `value_for_has_financial_center`), `gui/ef_dev_and_custom_windows/ef_custom_windows.gui`, `gui/scripted_widgets/ld_pb_fso_widgets.gui` (пузырь), `common/scripted_guis/ld_pb_fso_sguis.txt`; панель компаний `gui/companies_panel.gui` (интерфейс-агент).
- Подсистема банков читает `company_<банк>_fund` и `ai_privat_bank_*_from_list` из `01_economic_company_value.txt`.

## Логи
- `EFL|дата|страна|hq|listed|lshare|nhq|hqdiv|lit|div|snap|cap|cap_gdp|disc` — `zz_ef_listing_log` (игрок или ВВП > 20 млн).
- `ZZEF crash: equity fell by more than half in a year` + `debug_log_scopes` — краш в `zz_ef_cap_monthly_crash_check`.

## Известные несоответствия
- `financial_crash_consequences` перечисляет не все национальные биржи (нет `_dei`, `_han`, `_sax`, `_usa_2`, `_gbr_2`; `_TUS` в другом регистре).
- `bankrupt_company` и `08_list_effect.txt` ссылаются на ключи компаний, которых нет в диспетчере `ld_listing_switch.txt` (диспетчер знает только 271 тип); ссылки на ключи, которых нет ни в ванили, ни в CMF/ETF, ни в форке, удалены.
