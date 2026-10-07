# Банки и вклады
Частный «Банк» (`building_zz_ef_bank`) — здание-услуга: производит «расчёты» (товар `liquidity_currency`), покупает услуги, бумагу, немного
золота/серебра. Стартовые банки сеются один раз по рынку страны (40% — банковская компания E&F владельца, остальное — государство).
Центральный банк (`building_bank`) — государственное здание E&F без продажи валюты как товара. Вклады чужих ЦБ в наших банках — `nr_dep`.
Частные банки E&F (`privat_bank_*`) — это банковские компании E&F; их «счёт» — `investment_pool` страны (`private_bank_funds`).
Ключи в `ld_*` файлах имеют префикс `zz_ef_` (не `ld_`); в комментариях файлов старые имена `zz_ef_*.txt`.

## Файлы
- `common/buildings/ld_bank.txt` — `building_zz_ef_bank` (группа `bg_zz_ef_banking`, PMG `pmg_zz_ef_bank_base`, `ownership_type = self`, `ai_nationalization_desire = -5`).
- `common/building_groups/ld_banking_group.txt` — `bg_zz_ef_banking` (дочерняя `bg_trade`).
- `common/production_method_groups/ld_bank_pmg.txt` — `pmg_zz_ef_bank_base` (5 методов по эпохам).
- `common/production_methods/ld_bank_pm.txt` — `pm_zz_ef_bank_money_changer … _modern`: выход `goods_output_liquidity_currency_add` 300…1600, вход services/paper/telephones/electricity + базовые 0.01 золота и 0.02 серебра на рабочего (покупку металла регулируют модификаторы `zz_ef_bank_gold_buy`/`zz_ef_bank_silver_buy`, см. `ld_metal_accounts.txt:281-289`, `static_modifiers/ld_metal_trade.txt`). Комментарии называют их `zz_ef_bank_metal_buy` — такого ключа нет.
- `common/script_values/ld_bank_values.txt` — `zz_ef_bank_tc_levels` (уровни торговых центров штата, веса посева), `zz_ef_bank_levels` (уровни банков).
- `common/on_actions/ld_bank_on_actions.txt` — `on_monthly_pulse_country` → `zz_ef_bank_monthly` → `zz_ef_bank_seed_step`.
- `common/scripted_effects/ld_bank_seed.txt` — генерат: `zz_ef_bank_seed_step` (страна-владелец рынка, один раз, флаг `zz_ef_bank_seeded`), `zz_ef_bank_seed_state` (по штату), `zz_ef_bank_seed_company` (по банковской компании E&F, `$COMPANY$`), `zz_ef_bank_seed_state_owned` (запасной вариант — 100% государству).
- `common/scripted_effects/ld_cm_bank_ownership.txt` — `zz_ef_cm_create_owned_bank` (строит/доращивает ЦБ до размера `$CB_SIZE$`, государственный, резервы 0); зовут спавнеры E&F в `09_introduction_building_lvl.txt:23410…23523`.
- `common/buildings/ef_15_bank.txt` — `building_bank` (ЦБ E&F: `buildable = no`, PMG `pmg_minting_type`, `pmg_monetary_policy`).
- `common/production_method_groups/15_ef_bank.txt`, `common/production_methods/15_ef_bank.txt` — методы ЦБ по валютным стандартам (`pm_*_standard_bank_money_currency`: `country_minting_add`, выпуск облигаций `goods_output_bond_add`), `pm_revaluation`/`pm_devaluation`.
- `common/scripted_effects/ld_nr_deposits.txt` — генерат: `zz_ef_fx_liab_trim` (обрезка чужих запасов валюты эмитента до `zz_ef_fx_start_cap` × базы), `zz_ef_nr_dep_step` (недельный шаг у эмитента: вклады, проценты, `add_investment_pool`, модификатор `zz_ef_fx_holders_demand`).
- `common/script_values/ld_nr_deposits_values.txt` — `zz_ef_fx_start_cap` (0.05), `zz_ef_nr_dep_v`, `zz_ef_v_f_nr_dep`, `zz_ef_v_w_nr_dep`, `zz_ef_nr_int_week`, `zz_ef_v_f_nr_int`, `zz_ef_fx_holders_demand_m` (до 20).
- `common/scripted_triggers/ld_nr_deposits_triggers.txt` — `zz_ef_nr_issuer` (есть `has_central_bank`, нет `zz_ef_cur_zone`).
- `common/static_modifiers/ld_fx_holders_demand.txt` — `zz_ef_fx_holders_demand` (`state_export_advantage_mult = 0.01` на единицу множителя).
- E&F, банковская часть (огромные файлы, смотреть `grep -n`):
  - `common/scripted_effects/01_financial_scripted_effects.txt`: `establish_bank_and_ef_compagnie` (:13164, ИИ раз в год получает банковские компании), `ai_privat_bank_bond_1..25` (:4130…, покупка облигаций частными банками), `private_ownership_production_stocks`, `financial_center_production_methods`.
  - `common/scripted_effects/08_list_effect.txt`: `privat_bank_variable_list` (:1748, список банковских компаний, `privat_bank_variable_list_ordered`), список `global_arbitrage_bank_variable_list_ordered` (:2209, по `gdp_var`).
  - `common/script_values/00_financial_scripted_value.txt` — значения для интерфейса/ИИ покупок облигаций; `common/script_values/00_economic_scripted_value.txt:5335-6745` — `private_bank_funds*` (`private_bank_funds` = `investment_pool`, :6246); `01_economic_company_value.txt:29` `total_privat_bank`.
  - `common/scripted_guis/00_financial_scripted_guis.txt` — только облигационные/кредитные кнопки (см. `bonds.md`); банковских кнопок нет.
  - `common/history/global/00_ef_financial_global_variable.txt` — стартовые переменные стран E&F (`speculative_share_*`, бонды); счёта частных банков не создаёт.
  - `common/scripted_effects/01_economic_scripted_effects.txt:77017…77736` — арбитражи частных банков (см. `clearing-fx.md`, реестр).

## Поток / порядок
- Месяц (`on_monthly_pulse_country`): `zz_ef_bank_seed_step` — у владельца рынка, если нет `zz_ef_bank_seeded`: уровни = (заказы на покупку `liquidity_currency` × 1.2 − заказы на продажу) / 500, распределяются по штатам стран рынка весом `zz_ef_bank_tc_levels`; в штате `zz_ef_bank_seed_state` создаёт здание (если `zz_ef_bank_n ≥ 1`), долевая собственность с компанией E&F владельца из жёсткого списка (`zz_ef_bank_seed_company`), иначе государству. Лог `EFK|`.
- Неделя (`zz_ef_money_model_step`, `ld_money_model.txt:101`, из `on_actions/ld_money_model_on_actions.txt:31`): `zz_ef_cb_hume_step` (:552) → после клиринга `zz_ef_nr_dep_step` (:554): `zz_ef_f_nr_dep` = (суммарные чужие запасы нашей валюты `zz_ef_fx_liab_all` − вклады `zz_ef_nr_dep_v`); `add_investment_pool` на эту дельту (изъятие не больше пула); проценты `zz_ef_nr_int_week` = вклады × `zz_ef_deposit_rate` / 52 причисляются к вкладам из капитала банков (`zz_ef_post` `zz_ef_bank_capital` → `zz_ef_nr_dep`); модификатор спроса держателей обновляется. Первый запуск: после старта (`zz_ef_parity_version`, нет `zz_ef_metal_rescale_due`) — `zz_ef_fx_liab_trim` с базой `zz_ef_agg_m2`, флаг `zz_ef_nr_started`. `zz_ef_fx_liab_trim` зовёт и перемасштабирование (`ld_money_model.txt:173`).
- Банковская наличность (`zz_ef_bank_cash_sum`, `ld_money_model_values.txt:2147`) вынесена из M1/M2; металл банков (вход золота/серебра) — `ld_metal_accounts.txt` (`zz_ef_bank_in_gold_goods`, `zz_ef_mt_bank_*`).
- Год (`central_bank_ef_on_yearly_pulse_country`, `00_on_action_main.txt:792`): ИИ — `establish_bank_and_ef_compagnie`; `financial_center_ef_on_yearly_pulse_country` (:1086): `ai_buy_central_bank_debt` (в т.ч. `ai_privat_bank_bond_N`).
- Проценты частных банков по чужим облигациям не начисляются (обе половины — в `_archive/ld_privbank_interest/`; вернуть одной проводкой в реестре облигаций, R5).

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `zz_ef_bank_seeded` (страна) | посев сделан | `zz_ef_bank_seed_step` | он же |
| `zz_ef_bank_l`, `zz_ef_bank_w`, `zz_ef_bank_n` | уровни, вес, уровни в штате (временные) | `ld_bank_seed.txt` | он же |
| `zz_ef_nr_dep` | вклады чужих ЦБ в наших банках, деньги | `zz_ef_nr_dep_step` | `zz_ef_nr_dep_v`, `ld_reference_currency_values.txt:142,204` |
| `zz_ef_f_nr_dep`, `zz_ef_f_nr_int` | поток недели: взнос/изъятие, проценты | `zz_ef_nr_dep_step` | `zz_ef_v_f_nr_dep`, `zz_ef_v_f_nr_int`, лог `EFR` |
| `zz_ef_t_liab_all` | временная: `zz_ef_fx_liab_all` после блока процентов, посчитанное один раз за шаг (для `zz_ef_f_nr_dep` и `zz_ef_fx_holders_demand_m`; значение имеет смысл только внутри шага) | `zz_ef_nr_dep_step` | он же, `zz_ef_fx_holders_demand_m` |
| `zz_ef_nr_started` | вклады запущены | `zz_ef_nr_dep_step` | он же |
| `zz_ef_fxt_liab/_cap/_k` | временные обрезки | `zz_ef_fx_liab_trim` | он же |
| `zz_ef_bkcash` | наличность банков | `ld_money_model.txt:108` | модель денег |
| `ai_privat_bank_bond_value_N`, `ai_privat_bank_buyer_slot_N`, `ai_privat_bank_seller_country_general_N` | облигации частных банков (E&F) | `ai_privat_bank_bond_N` | `zz_ef_bank_bonds` (`ld_money_model_values.txt:249`), `ld_bond_ledger.txt` (`zz_ef_pb_slot_N`) |
| `company_<Банк>_gold_stockpile_fix`, `_silver_stockpile_fix` (глобальные) | металл частного банка E&F | арбитраж (`private_bank_arbitrage_*`) | GUI E&F (`private_bank_gold_reserve_per_bank_gui`); модель `ld_*` их не читает |

## Вызовы и связи
- ЦБ создаётся спавнерами E&F через `zz_ef_cm_create_owned_bank` (`09_introduction_building_lvl.txt`, `history/buildings/00_ef_building.txt:16`).
- `zz_ef_bank_levels` и `building_zz_ef_bank` читают `ld_metal_accounts_values.txt:230-278`, `ld_money_model_values.txt:2144-2150`.
- Компании-владельцы: `common/company_types/00_ef_companies.txt` (`building_zz_ef_bank` в списках разрешённых зданий, 98 компаний).
- Вклады входят в позицию «за рубежом» и пул: `ld_reference_currency_values.txt:142,204`; модель денег пишет `EFW`/`EFR` строки.
- Интерфейс: `gui/ld_economy_panel.gui` — круговая диаграмма банков-держателей валюты `zz_ef_bank_holders_piechart` (:9797, список `zz_ef_bank_holders_list`, заполняет `zz_ef_holders_update` в `scripted_guis/ld_cbfx.txt`); `gui/ld_cb_rate_panel.gui` — панель ставки/ЦБ. Здание «Банк» — стандартная панель здания.

## Логи
- `EFK|` — посев банков в штате/по рынку (`ld_bank_seed.txt`).
- `EFN|trim` — обрезка чужих запасов валюты эмитента (`ld_nr_deposits.txt:118`).
- `EFB|`, `EFP|` — реестр облигаций/частные банки (см. `bonds.md`).
