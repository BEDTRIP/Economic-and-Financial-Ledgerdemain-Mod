# Банки и вклады
**Смысл.** Банковский сектор страны: здания «Банк» производят банковские расчёты и покупают металл резерва; книга
банков (вклады, кредит ЦБ, капитал, кредиты) — агрегат на страну; вклады чужих ЦБ — регистр эмитента. Поштучные банки —
R4. **Понятия:** [[Банки]], [[Пул]], [[Вклады нерезидентов]], [[Металл]], [[Свободные банки]]. **Решения:** Д2.15, Д2.16,
Д2.25, Д2.26, Д.R0.8.Б1–Б5, В.R3б.2 (`решения.md`). **От E&F, не решалось:** `establish_bank_and_ef_compagnie` (ИИ
получает банковские компании) — R4.

Частный «Банк» (`building_zz_ef_bank`) — здание-услуга: производит «расчёты» (товар `liquidity_currency`), покупает услуги, бумагу, немного
золота/серебра. Стартовые банки сеются один раз по рынку страны (40% — банковская компания E&F владельца, остальное — государство).
Центральный банк (`building_bank`) — государственное здание E&F без продажи валюты как товара. Вклады чужих ЦБ в наших банках — `nr_dep`.
Фонды частных банков E&F — в `_archive/` (В.R3б.2); банковские компании E&F — владельцы зданий «Банк».
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
- `common/scripted_effects/ld_nr_deposits.txt` — генерат: `zz_ef_nr_dep_step` (недельный шаг у эмитента: вклады, проценты, проводка клиринга `add_investment_pool`, модификатор `zz_ef_fx_holders_demand`).
- `common/script_values/ld_nr_deposits_values.txt` — `zz_ef_nr_dep_v`, `zz_ef_v_f_nr_dep`, `zz_ef_v_w_nr_dep`, `zz_ef_v_f_nr_oth`, `zz_ef_nr_int_week`, `zz_ef_v_f_nr_int`, `zz_ef_fx_holders_demand_m` (до 20).
- `common/scripted_triggers/ld_nr_deposits_triggers.txt` — `zz_ef_nr_issuer` (есть `has_central_bank`, не внешневалютный стандарт).
- `common/static_modifiers/ld_fx_holders_demand.txt` — `zz_ef_fx_holders_demand` (`state_export_advantage_mult = 0.01` на единицу множителя).
- E&F, банковская часть (огромные файлы, смотреть `grep -n`):
  - `common/scripted_effects/01_financial_scripted_effects.txt`: `establish_bank_and_ef_compagnie` (:13164, ИИ раз в год получает банковские компании), `ai_privat_bank_bond_1..25` (:4130…, покупка облигаций частными банками), `private_ownership_production_stocks`, `financial_center_production_methods`.
  - `common/scripted_effects/08_list_effect.txt`: `privat_bank_variable_list` (список банковских компаний; `privat_bank_variable_list_ordered` — те же банки без сортировки, из него `ai_privat_bank_bond_N` берёт случайного покупателя облигаций), список `global_arbitrage_bank_variable_list_ordered` (:2209, по `gdp_var`; читатель — арбитраж — в `_archive/ef_bimetallic_arbitrage/`).
  - `common/script_values/00_financial_scripted_value.txt` — значения для интерфейса/ИИ покупок облигаций; `common/script_values/00_economic_scripted_value.txt:5335-6745` — `private_bank_funds*` (`private_bank_funds` = `investment_pool`, :6246); `01_economic_company_value.txt:29` `total_privat_bank`.
  - `common/scripted_guis/00_financial_scripted_guis.txt` — только облигационные/кредитные кнопки (см. `bonds.md`); банковских кнопок нет.
  - `common/history/global/00_ef_financial_global_variable.txt` — стартовые переменные стран E&F (`speculative_share_*`, бонды); счёта частных банков не создаёт.

## Поток / порядок
- Месяц (`on_monthly_pulse_country`): `zz_ef_bank_seed_step` — у владельца рынка, если нет `zz_ef_bank_seeded`: уровни = (заказы на покупку `liquidity_currency` × 1.2 − заказы на продажу) / 500, распределяются по штатам стран рынка весом `zz_ef_bank_tc_levels`; в штате `zz_ef_bank_seed_state` создаёт здание (если `zz_ef_bank_n ≥ 1`), долевая собственность с компанией E&F владельца из жёсткого списка (`zz_ef_bank_seed_company`), иначе государству. Лог `EFK|`.
- Неделя (`zz_ef_money_model_step`, `ld_money_model.txt:101`, из `on_actions/ld_money_model_on_actions.txt:31`): `zz_ef_cb_hume_step` (:552) → после клиринга `zz_ef_nr_dep_step` (:554): вклад чужого ЦБ — только встречной проводкой, регистр `zz_ef_nr_dep` — источник, запасы держателей `stockpiling_<cur>_state_1` — его зеркало. Проводка клиринга: `zz_ef_f_nr_dep` = своя валюта, отданная в клиринг за неделю (`zz_ef_f_clr_cur_out`), − выкупленная назад (`zz_ef_f_clr_own_back`) — деньги, которые движок уже взял за импорт; `add_investment_pool` на неё (изъятие не больше пула). Остальное изменение запасов (`zz_ef_fx_liab_all` − регистр: месячные запасы E&F, форекс E&F, сброс валюты) — без денег: регистр догоняет запасы, `zz_ef_f_nr_oth`, сверка показывает его в «прочем» (пул − книга) до проводок R2 (Ф9). Проценты `zz_ef_nr_int_week` = вклады × `zz_ef_deposit_rate` / 52 причисляются к вкладам из капитала банков (`zz_ef_post` `zz_ef_bank_capital` → `zz_ef_nr_dep`); модификатор спроса держателей обновляется. Старт: чужой валюты у ЦБ нет (раздача истории E&F — в `_archive/ef_start_fx_reserves/`); первый запуск — как страна стала эмитентом (`zz_ef_model_started`): вклады 0, флаг `zz_ef_nr_started`.
- Банковская наличность (`zz_ef_bank_cash_sum`, `ld_money_model_values.txt:2147`) вынесена из M1/M2; металл банков (вход золота/серебра) — `ld_metal_accounts.txt` (`zz_ef_bank_in_gold_goods`, `zz_ef_mt_bank_*`).
- Год (`central_bank_ef_on_yearly_pulse_country`, `00_on_action_main.txt:792`): ИИ — `establish_bank_and_ef_compagnie`; `financial_center_ef_on_yearly_pulse_country` (:1086): `ai_buy_central_bank_debt` (в т.ч. `ai_privat_bank_bond_N`).
- Проценты частных банков по чужим облигациям не начисляются (обе половины — в `_archive/ld_privbank_interest/`; вернуть одной проводкой в реестре облигаций, R5).

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `zz_ef_bank_seeded` (страна) | посев сделан | `zz_ef_bank_seed_step` | он же |
| `zz_ef_bank_l`, `zz_ef_bank_w`, `zz_ef_bank_n` | уровни, вес, уровни в штате (временные) | `ld_bank_seed.txt` | он же |
| `zz_ef_nr_dep` | вклады чужих ЦБ в наших банках, деньги | `zz_ef_nr_dep_step` | `zz_ef_nr_dep_v`, `ld_reference_currency_values.txt:142,204` |
| `zz_ef_f_nr_dep`, `zz_ef_f_nr_int`, `zz_ef_f_nr_oth` | поток недели: проводка клиринга (взнос/изъятие), проценты, изменение запасов без проводки («прочее») | `zz_ef_nr_dep_step` | `zz_ef_v_f_nr_dep`, `zz_ef_v_f_nr_int`, `zz_ef_v_f_nr_oth`, лог `EFR` |
| `zz_ef_t_liab_all` | временная: `zz_ef_fx_liab_all` после блока процентов, посчитанное один раз за шаг (для `zz_ef_f_nr_oth` и `zz_ef_fx_holders_demand_m`; значение имеет смысл только внутри шага) | `zz_ef_nr_dep_step` | он же, `zz_ef_fx_holders_demand_m` |
| `zz_ef_nr_started` | вклады запущены | `zz_ef_nr_dep_step` | он же |
| `zz_ef_bkcash` | наличность банков | `ld_money_model.txt:108` | модель денег |
| `ai_privat_bank_bond_value_N`, `ai_privat_bank_buyer_slot_N`, `ai_privat_bank_seller_country_general_N` | облигации частных банков (E&F) | `ai_privat_bank_bond_N` | `zz_ef_bank_bonds` (`ld_money_model_values.txt:249`), `ld_bond_ledger.txt` (`zz_ef_pb_slot_N`) |
| `company_<Банк>_gold_stockpile_fix`, `_silver_stockpile_fix` (глобальные) | металл частного банка E&F | история (арбитраж `private_bank_arbitrage_*` — в `_archive/ef_bimetallic_arbitrage/`) | GUI E&F (`private_bank_gold_reserve_per_bank_gui`); модель `ld_*` их не читает |

## Вызовы и связи
- ЦБ создаётся спавнерами E&F через `zz_ef_cm_create_owned_bank` (`09_introduction_building_lvl.txt`, `history/buildings/00_ef_building.txt:16`).
- `zz_ef_bank_levels` и `building_zz_ef_bank` читают `ld_metal_accounts_values.txt:230-278`, `ld_money_model_values.txt:2144-2150`.
- Компании-владельцы: `common/company_types/00_ef_companies.txt` (`building_zz_ef_bank` в списках разрешённых зданий, 98 компаний).
- Вклады входят в позицию «за рубежом» и пул: `ld_reference_currency_values.txt:142,204`; модель денег пишет `EFW`/`EFR` строки.
- Интерфейс: `gui/ld_cb_rate_panel.gui` — панель ставки/ЦБ; таблица частных банков вкладки «Финансы» — банк, тип, доля пула страны на банк (`private_bank_funds_per_private_bank`), металл банка; сводка — `total_bank_funds` (пул + металл банков). Фонды банков E&F (чужие облигации и валюты по банкам) — в `_archive/ef_bank_funds/`, заново — R4. Здание «Банк» — стандартная панель здания.

## Логи
- `EFK|` — посев банков в штате/по рынку (`ld_bank_seed.txt`).
- `EFB|`, `EFP|` — реестр облигаций/частные банки (см. `bonds.md`).
