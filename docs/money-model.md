# Денежная модель и счета
Недельная двойная запись в деньгах движка: счета страны (казна, пул банков, наличные бизнеса, сбережения и вклады
населения, касса ЦБ), агрегаты M0–M3, кредит ЦБ банкам, потребительский и бизнес-кредит, ставка правительства.
Рядом — счета металла (золото/серебро у ЦБ, банков, населения) и запасы валют E&F («stockpile»). Нацзапас товаров E&F
вынесен в `_archive/ef_national_stockpile/`. Игрок видит результат в карточках денежной массы и ЦБ (разметка в `gui/ld_economy_panel.gui`, переменные читает она).

## Файлы
- `common/on_actions/ld_money_model_on_actions.txt` — подвеска на `on_monthly_pulse_country`; цепочка недельного шага (`zz_ef_money_model_weekly`, самоперезапуск через 7 дней); дневной зонд старта цепочки.
- `common/scripted_effects/ld_money_model.txt` — недельный шаг, приёмник GUI-моста, ежемесячный шаг, сбережения/вклады, кредиты, кольца истории, ставка правительства, перемасштаб металла ЦБ, выкуп валюты в кризис, зонды.
- `common/script_values/ld_money_model_values.txt` — все формулы: счета, M0–M3, кредитные лимиты, ставки, платёжный баланс, кольца роста (почти все ключи `zz_ef_*`).
- `common/scripted_effects/ld_metal_accounts.txt` — старт металла, недельные покупки/продажи ЦБ/банков/населения, выкуп у населения, сверка металла ЦБ, мировая линия металла.
- `common/script_values/ld_metal_accounts_values.txt` — единицы металла, нормы резерва, покупки через модификаторы зданий, продажа ЦБ, выкуп, мировые суммы.
- `common/scripted_effects/ld_money_log_rest.txt` — сгенерированный `debug_log` «прочее» карточек (`EFO`); не править (генератор `tools/regen_ef_money_supply_loc.py`).
- `common/scripted_guis/ld_money_hook.txt` + `gui/ld_money_hook.gui` — мост GUI→скрипт: строки бюджета, доступные только GUI, передаются в `zz_ef_money_hook_receive`.
- `common/scripted_effects/ld_currency_intro_metal.txt` — обёртка вокруг введения валюты E&F (`introduction_new_currency`): металл столицы возвращается как был.
- `common/scripted_effects/ld_subject_metal.txt` — `zz_ef_cb_state_owner_step` (металл ушедшего ЦБ-региона возвращается прежнему владельцу).
- `common/scripted_effects/ld_stockpile_state_var_seed.txt`, `common/on_actions/ld_stockpile_state_var_init.txt`, `common/history/global/zz_ef_init_stockpiling_state_vars.txt` — засев 5 переменных `stockpiling_*_var_state_1` и двух вспомогательных на регионах (`financial_center_site_var`, `looted_state`); GLOBAL-блок истории (новая кампания), `on_game_started_after_lobby` и месячная страховка (раз за игру по глобальной `zz_ef_stockpile_state_vars_seeded`).
- `common/pop_needs/ld_metal_hoard.txt` — потребность населения: серебро/золото как накопление (по 0.5).
- `common/production_methods/ld_gold_mine_minting_off.txt` — INJECT в методы золотых шахт: обнуляет `country_minting_add`.
- `common/static_modifiers/ld_metal_trade.txt` — модификаторы зданий: покупка металла банками/ЦБ, продажа ЦБ (`zz_ef_bank_gold_buy`, `zz_ef_bank_silver_buy`, `zz_ef_cb_metal_buy`, `zz_ef_cb_gold_sell`, `zz_ef_cb_silver_sell`).
- `common/static_modifiers/ld_consumer_credit.txt` — `zz_ef_consumer_credit` (`state_dependent_wage_add`).
- `common/static_modifiers/ld_debt_service.txt` — `zz_ef_debt_service` (+1% взноса в пул у слоёв).
- E&F вне списка, но пишут те же счета: `common/scripted_effects/01_economic_scripted_effects.txt` (`stockpiling_currency` → `stockpiling_currency_type_1` ×95; `investement_pool_borrowing`), `common/scripted_effects/00_on_action_main.txt` (месячный запуск запасов валют, арбитраж частных банков).

## Поток / порядок
1. **Месяц** (`on_monthly_pulse_country`, все страны): `zz_ef_money_model_monthly` → `zz_ef_money_model_monthly_step` (зона валюты, курс серебра, сила валюты, торговый модификатор, январская выплата процентов частных банков `zz_ef_privbank_interest_pay`, `zz_ef_dependents`, `zz_ef_money_ledger_delta ACC=cb`, цена политики ставки, ставка правительства `zz_ef_gov_rate_step`, `zz_ef_mp_step`, модификатор частного строительства) и `zz_ef_money_week_start` (запуск цепочки, если нет `zz_ef_week_alive`/`zz_ef_week_probe`).
2. **Старт цепочки**: дневной зонд (`zz_ef_money_week_probe`, ≤8 дней) ждёт смены казны (бюджетный тик движка), затем `zz_ef_money_model_weekly`; первый вызов назначает стране день недели (`zz_ef_week_slot`, 0..6) и сдвигает её цепочку на столько дней — шаги стран разнесены по неделе.
3. **Неделя** `zz_ef_money_model_step` (+ перезапуск через 7 дней): суммы наличных зданий и банков → обновление валютных резервов (`zz_ef_fx_metal_update`, `zz_ef_cbfx_week_step`) → `zz_ef_cb_state_owner_step` → `zz_ef_bond_ledger_step` → счётчик недель → единожды: версия паритета (старт металла `zz_ef_metal_start_step`, `zz_ef_fx_liab_trim`) / повторный перемасштаб на 12-й неделе → снимок бюджета → кредит ЦБ банкам (`zz_ef_cb_borrow/repay/interest` в пул и `zz_ef_bank_cb_debt`, проценты в казну) → `zz_ef_consol_step` → излишек казны в пул (`zz_ef_f_tr_pool`) → `zz_ef_business_credit_step` → **`zz_ef_metal_week_step`** (счета металла, модификаторы зданий на следующую неделю) → кольца истории M0–M3 (w1..4, q1..13, r1..20) → поток ЦБ (переоценка, Юм, запас) → `zz_ef_money_ledger_delta` по каждому счёту → строка `EFW` → окна `zz_ef_money_window_roll` → постановка страны в глобальный список `zz_ef_hook_countries`.
4. **Приёмник GUI-моста** (`zz_ef_money_hook_receive`, из `gui/ld_money_hook.gui` по `trigger_when`, раз в неделю на страну): читает `scope:ext`, `scope:abr`, `scope:g_*`, считает утечку, затем по порядку: `zz_ef_pop_savings_step` → `zz_ef_cb_hume_step` (клиринг `zz_ef_clr_step`, `zz_ef_world_acc`) → `zz_ef_nr_dep_step` → `zz_ef_consumer_credit_step` → `zz_ef_pop_extra_income_step` → логи `EFR`/`EFO`.
5. **Год**: `central_bank_ef_on_yearly_pulse_country` (E&F) → `investement_pool_borrowing` (после замены: только проценты частных банков в пул).

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `zz_ef_week_alive`, `zz_ef_week_probe(_value)`, `zz_ef_weeks_run` | жизнь цепочки (10 дней), зонд, число недель | `zz_ef_money_week_start/probe_step/model_step` | те же; условия «первые N недель» |
| `zz_ef_pop_savings`, `zz_ef_pop_deposits` | сбережения населения (S), вклады в банках (D); наличные = S−D | `zz_ef_pop_savings_step`, `zz_ef_metal_week_step` (выкуп), `ld_consols.txt` | `zz_ef_pop_cash`, M0–M3, карточки |
| `zz_ef_bank_cb_debt` | долг банков перед ЦБ | `zz_ef_money_model_step` | `zz_ef_cb_credit_target`, кредитные лимиты |
| `zz_ef_cc_debt`, `zz_ef_bc_debt`, `zz_ef_bc_svc` | потребительский / бизнес-долг, обслуживание | `zz_ef_consumer_credit_step`, `zz_ef_business_credit_step` | значения `zz_ef_cc_*`, `zz_ef_bc_*`, модификатор `zz_ef_debt_service` |
| `zz_ef_f_<F>` (`budget`, `contrib`, `transfer`, `cb_borrow`, `cb_repay`, `cb_interest`, `tr_pool`, `ext`, `abr`, `leak`, `inflow`, `dep_in/out/int`, `trade`, `div`, …) | поток недели по статье | недельный шаг и приёмник | `zz_ef_v_f_<F>` (значения для GUI), окна `zz_ef_w_<F>` (`zz_ef_money_window_roll`) |
| `zz_ef_prev_<ACC>`, `zz_ef_<ACC>_w1..4/q1..13/r1..20` | прошлая неделя и кольца истории счета (`pool`, `buildings`, `tc`, `treasury`, `bonds`, `tbonds`, `m2`, `cbm`, `abroad`, `agg0..3`, `circ`, `gdp`, `price`, `govlv`, `savings`, `deposits`, `cb`) | `zz_ef_money_ledger_delta`, `zz_ef_ring_*_push` | `zz_ef_v_d_<ACC>`, `zz_ef_agg<N>_pct_*`, `zz_ef_circ_growth_year`, `zz_ef_price_index` |
| `zz_ef_t_led` | временная: значение счёта, посчитанное один раз в `zz_ef_money_ledger_delta` (снимается там же) | `zz_ef_money_ledger_delta` | оно же |
| `zz_ef_bcash`, `zz_ef_bkcash` | наличные бизнеса и банков за неделю | `zz_ef_money_model_step` | `zz_ef_building_cash`, `zz_ef_agg_m0..m3` |
| `zz_ef_parity_version`, `zz_ef_parity_hist`, `zz_ef_metal_rescale(_due)`, `zz_ef_metal_started` | версия паритета, историческое значение, коэффициент перемасштаба, флаг старта металла | `zz_ef_money_model_step`, `zz_ef_metal_start_step`, `zz_ef_metal_rescale_step` | `zz_ef_cb_cover_ref`, `zz_ef_cover_normal` |
| `gold_state_1`, `silver_state_1` (регион ЦБ с `central_bank_historic_place`) | металл ЦБ (переменные E&F) | `zz_ef_metal_week_step`, `zz_ef_metal_rescale_step`, `zz_ef_metal_start_step`, `zz_ef_cb_state_owner_step`, `zz_ef_cur_intro_after`; E&F: forex-GUI `<cur>_buy/sell_in_gold` (`00_economic_scripted_guis.txt`), `stockpiling_currency_type_1`, арбитраж частных банков (`00_on_action_main.txt:954-1036`), `introduction_*` | `gold_state_native_for_stockpile`, `central_bank_reserves`, `zz_ef_cbm_gold/silver`, `zz_ef_cb_cover` |
| `zz_ef_popm_gold/silver`, `zz_ef_bankm_gold/silver` | металл населения и банков (единицы резерва) | `zz_ef_metal_start_step`, `zz_ef_metal_start_banks`, `zz_ef_metal_week_step` | `zz_ef_popm_money`, `zz_ef_bankm_money`, `zz_ef_wm_sum_*` |
| `zz_ef_f_mt_<cb_in/cb_out/bank_in/pop_in>_<g/s>`, `zz_ef_f_mt_buyback(_money)`, `zz_ef_f_mt_oth_<g/s>`, `zz_ef_mt_prev_<g/s>`, `zz_ef_mt_start_adj_<g/s>`, `zz_ef_cb_stock_acc` | покупки/продажи недели, выкуп, невязка сверки, снимок, поправка старта, изменение резервов ЦБ | `zz_ef_metal_week_step`, `zz_ef_metal_reconcile`, `zz_ef_metal_start_cb_after` | сверка следующей недели, карточка ЦБ (`zz_ef_v_f_cb_stock`) |
| `zz_ef_t_cb_in_<g/s>`, `zz_ef_t_bank_in_<g/s>` | временные: вход зданий ЦБ и банков (товары), посчитанный один раз за шаг; из них `zz_ef_f_mt_cb_in/bank_in` и часть населения (потребление штатов − они, не ниже 0; та же формула, что `zz_ef_pop_<gold/silver>_goods`) | `zz_ef_metal_week_step` | он же |
| `zz_ef_mt_bank_mult_g/s`, `zz_ef_mt_cb_mult`, `zz_ef_mt_cb_sell` | множители модификаторов `ld_metal_trade` на следующую неделю | `zz_ef_metal_week_step` | `add_modifier` на зданиях `building_zz_ef_bank` (только при `zz_ef_mt_bank_levels > 0`) / `building_bank` |
| глобальные `zz_ef_wm_<start/buy/sell/oth>_<gold/silver>` | мировая линия металла (накопительно) | `zz_ef_wm_add` | `zz_ef_wm_v_*`, `zz_ef_wm_rest_*`, лог `EFV` |
| глобальные `zz_ef_hook_countries` (список), `zz_ef_hook_calls`, `zz_ef_hook_probe_calls` | очередь моста, счётчики вызовов | `zz_ef_money_model_step`, `zz_ef_money_hook_receive`, `zz_ef_money_hook_probe_sg` | `gui/ld_money_hook.gui`, `zz_ef_hook_ok` |
| `stockpiling_<cur>_state_1`, `stockpiling_<cur>_reserve_currency_state_1` (регион, E&F) | запас валюты `<cur>` в регионе ЦБ | E&F `stockpiling_currency_type_1`, `buy_/sell_<g>_order_in_currency` | `money_supply_state`, `zz_ef_fx_reserves_metal`, `zz_ef_fx_liab_all` |
| `<cur>_c_no_own` (значение, 95 валют) | запас валюты минус `money_supply` | — (значения) | `currency_no_own` → `gui/ld_economy_panel.gui` (текст «currency_no_own») |

## Вызовы и связи
- Из модели вызываются другие подсистемы: `zz_ef_cur_zone_step`, `zz_ef_silver_rate_update`, `zz_ef_reference_strength_step`, `zz_ef_currency_trade_step`, `zz_ef_rate_policy_costs`, `zz_ef_mp_step`, `zz_ef_clr_step`, `zz_ef_nr_dep_step`, `zz_ef_fx_liab_trim`, `zz_ef_consol_step`, `zz_ef_bond_ledger_step`, `zz_ef_cbfx_week_step` (клиринг, облигации, зона валюты, денежная политика).
- Модель вызывается: `zz_ef_cur_intro_before/after` из `common/scripted_effects/09_introduction_building_lvl.txt:34332/34463` (обёртка `introduction_new_currency`).
- Значения модели читают GUI и локализация: `gui/ld_economy_panel.gui`, `localization/<язык>/replace/ld_money_supply_replace_l_<язык>.yml`, `ld_cb_rate_panel_*`, `ld_monetary_policy_*`; `gui/ld_money_hook.gui` — единственный GUI-узел модели (виджет `zz_ef_money_hook`, скрытый, на `GetGlobalList('zz_ef_hook_countries')`).
- Металл ЦБ меняется только покупкой зданием ЦБ (`zz_ef_cb_metal_buy`): раздачи металла E&F из рынка в `gold_state_1` нет.
- Ручные операции E&F, меняющие счета мимо недельной записи (попадают в «прочее»/невязку `EFQ`): forex-кнопки `<cur>_buy/sell_in_gold` (`gold_state_1`), `stockpiling_currency_type_1` (девальвация/ревальвация: металл ↔ валютный запас), арбитраж частных банков (`private_bank_arbitrage_gold_drain`), `reset_law_event_currency` (пул −`private_bank_funds`, `government_loan` = 0), `global_monetary_reference_reset`, `transfer_gold_to_central_bank_metal_reserves`.

## Логи
- `EFW` — недельная строка страны: M0..M3, счета (игрок и страны с ВВП > 20 млн).
- `EFR` — приёмник: внешний поток, утечка, прочее; `EFO` — «прочее» карточек (`zz_ef_money_log_rest`).
- `EFG|…|WORLD` — мировая линия потоков (клиринг); `EFV|…|WORLD` — мировая линия металла.
- `EFT` — недельные покупки металла ЦБ/банков/населения (`zz_ef_metal_week_step`); `EFQ` — невязка металла ЦБ > 1000 золота / 10000 серебра.
- `EFM` — события: `metal_start`, `cb_state_lost`, `cur_intro`, `privbank_interest`; `EFA` — доп. доходы/расходы > 1000; `EFX` — валюта раз в месяц; `EFC` — выкуп валюты в кризис.
