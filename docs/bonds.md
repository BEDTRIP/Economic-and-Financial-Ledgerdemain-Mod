# Облигации и консоли
**Смысл.** Госдолг как доли держателей в долге движка; консоли — бессрочный долг казны населению. Сейчас — слоты E&F,
цель — словари требований (R8б) и аукцион на бирже (R5). **Понятия:** [[Облигации]], [[Консоли]], [[Казна]],
[[Словарь требований]]. **Решения:** Д.R2.7, Д.R8.9 (`решения.md`).

Государственные облигации E&F (казна покупает облигации другой страны, ИИ — слоты `ai_buy_bond_1..10`, частные банки — `ai_privat_bank_bond_1..25`,
игрок — кнопки покупки) учитываются как доли в движковом долге продавца (`principal`): «реестр облигаций» `ld`. Доли
держит реестр требований (`claims.md`): карты казны `zz_ef_rq_tr_b` и банков `zz_ef_rq_bk_b`, ключ — продавец; слоты E&F
— только вход покупки (после регистрации слот казны свободен, значение слота банков — 0). Облигации ЦБ, проданные населению,
— консоли (бессрочный долг казны населению). Выплаты процентов и погашение идут деньгами между пулами/казнами, а не «из воздуха».
Ключи в `ld_*` файлах — `zz_ef_*` (комментарии называют старые файлы `zz_ef_*.txt`).

## Файлы
- `common/scripted_effects/ld_bond_ledger.txt` — генерат (`tools/regen_ef_bond_ledger.py`): `zz_ef_bond_ledger_step` (недельный шаг: сторона продавца, вход покупок E&F, доли держателя), `zz_ef_bl_slot_1..10` (покупка казны по слоту E&F `ai_buy_bond_N_on`, `ai_seller_country_general_N`, `ai_total_bond_value_N` → `zz_ef_bl_register`, слот освобождается `zz_ef_bl_slot_free`), `zz_ef_pb_slot_1..25` (покупка банков по `ai_privat_bank_bond_value_N`, продавец — случайный из списка E&F; значение — в 0), `zz_ef_bl_hold_map` / `zz_ef_bl_hold_one` (каждая доля: урезание по `zz_ef_bl_ratio` продавца, погашение равными долями за `zz_ef_bl_term_weeks`, проценты), помощники `zz_ef_bl_pay/roll/acc_add/into_*/woff_*/icap_*`, `zz_ef_pb_no_seller`.
- `common/script_values/ld_bond_ledger_values.txt` — `zz_ef_bl_principal` (долг движка), `zz_ef_bl_held_v` (доли за рубежом — итог реестра `zz_ef_rq_out_b`), `zz_ef_bl_room`, `zz_ef_bl_int_per_part` (недельный процент на единицу, ≤ 0.01, из `zz_ef_v_g_ipay`), `zz_ef_bl_term_weeks` (390 — средний срок слотов E&F 5 и 10 лет), `zz_ef_bl_parts` / `zz_ef_bl_bank_parts` (наши доли казны / банков — итоги карт), потоки `zz_ef_v_f_bl_*`, `zz_ef_v_f_pb_*`.
- `common/script_values/ld_bond_tables_values.txt` — ключи сортировки таблиц (`zz_ef_bt_in_key`, `zz_ef_bt_out_key`), ставки строк.
- `common/scripted_guis/ld_bond_tables.txt` — `zz_ef_bonds_update`: заполняет глобальные списки `zz_ef_bt_in_list` («кто держит наши облигации») и `zz_ef_bt_out_list` («чьи облигации держим») при открытии таблицы — по картам реестра и слотам игрока E&F.
- `common/scripted_effects/ld_consols.txt` — `zz_ef_consol_step` (недельный: продажа → долг, проценты казна → сбережения населения, выкуп излишка казны).
- `common/script_values/ld_consols_values.txt` — `zz_ef_consol_output`, `zz_ef_consol_sale_week`, `zz_ef_consol_debt_v`, `zz_ef_consol_interest_week`, `zz_ef_consol_buyback_week`, `zz_ef_consol_debt_to_gdp`, потоки `zz_ef_v_f_cons_*`.
- `common/scripted_effects/ld_cb_bond_issuance.txt` — `zz_ef_cb_bond_issuance_update` (выпуск облигаций ЦБ по долг/ВВП, зов из `00_on_action_main.txt:4293`) — смежно.
- E&F, облигационная часть:
  - `common/scripted_effects/01_financial_scripted_effects.txt`: `ai_buy_bond_1..10` (:1016…, покупка ИИ у ЦБ другой страны: `add_treasury` на цену, переменные слота), `bond_maturity_1..10` (:22737, годовой счётчик срока, сброс слота), `ai_bond_maturity_1..10` (:23825), `ai_privat_bank_bond_1..25` (:4130…), `buy_bond_in_currrency_var` (:32059), `country_credit_rating` (:18), `sovereign_bond_yields` (:499), `ai_credit_at_central_bank`/`ai_refund_central_bank` (:667/:727), кризисы (`currency_crisis` :33346, `economic_crisis`, `financial_crash`, `central_bank_bankruptcy`, `country_bankruptcy`), `central_bank_debt_buyer_list_clear`.
  - `common/scripted_effects/00_on_action_main.txt`: `financial_center_ef_on_yearly_pulse_country` (:1086), `ai_buy_central_bank_debt` (:16018), `bond_maturity_on_action` (:16553…).
  - `common/scripted_guis/00_financial_scripted_guis.txt` — кнопки игрока: `buy_bond_market_panel_5Y/10Y`, `buy_bond_in_currrency_market_panel_5Y/10Y`, `increase_bond_quantity`, `reduce_bond_quantity`, `set_debt_issued`, `refund_credit_at_central_bank*`, `base_rate_increase/reduce`, `speculative_share_N_button`; окно: `gui/00_ef_deported_gui_1.gui` (:81879 и др.).
  - `common/history/global/00_ef_financial_global_variable.txt` — стартовые `speculative_share_N` и переменные слотов.

## Поток / порядок
- Неделя (`zz_ef_money_model_step`): `zz_ef_bond_ledger_step` — продавец: прокатка недельных сумм (`zz_ef_bl_roll` для `sold`, `int_out`, `redeem`, `woff`), `zz_ef_bl_ratio` = principal / доли за рубежом (итог реестра), если принципал упал ниже долей (списание — только при `in_default` и падении принципала вдвое); держатель: вход покупок E&F — слоты казны `zz_ef_bl_slot_N` и банков `zz_ef_pb_slot_N` → `zz_ef_bl_register` (доля ≤ места продавца, остаток — назад в казну / пул, доля — в карту реестра, цена → `add_investment_pool` продавца); затем каждая доля карт `zz_ef_rq_tr_b` (в казну) и `zz_ef_rq_bk_b` (в пул банков; проценты — в капитал банков): урезание при `zz_ef_bl_ratio` < 1 (выкуп из пула продавца или списание в дефолте), погашение 1 / `zz_ef_bl_term_weeks` в неделю, проценты `zz_ef_bl_int_per_part` из пула продавца. Продавец не признан (децентрализован) — доля списана. Лог `EFB|` (+`EFP|`).
- Позже в том же шаге (`ld_money_model.txt:238`): `zz_ef_consol_step`: до отчисления излишка казны в пул. Неделя продаж `sg:bond.state_goods_production` × `bond_price` → `zz_ef_consol_debt`; проценты по ставке правительства / 52 — казна → `zz_ef_pop_savings`; выкуп, когда казна выше предела (`gold_reserves_limit`). Лог `EFS|`.
- Год (`financial_center_ef_on_yearly_pulse_country`): `ai_buy_central_bank_debt` → `ai_buy_bond_N`, `ai_privat_bank_bond_N` (первичная покупка — только при непустом `central_bank_debt_variable_list_ordered_1`, иначе продавца нет); затем `bond_maturity_on_action` (`bond_maturity_N`, `ai_bond_maturity_N`); `sovereign_bond_yields`.
- Проценты частным банкам по их долям — в реестре, как казне (R8б.2; прежняя половина E&F — `_archive/ld_privbank_interest/`).
- Таблицы: кнопка в Бюджет → Финансы, `gui/ld_cb_rate_panel.gui:12404…17347` (`zz_ef_bt_in_list`/`zz_ef_bt_out_list`, `zz_ef_bt_button`).

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `zz_ef_rq_out_b` (страна-продавец) | доли нашего долга за рубежом — итог реестра (`claims.md`) | `zz_ef_rq_add` | `zz_ef_bl_held_v`, `zz_ef_bl_room` |
| `zz_ef_bl_ratio`, `zz_ef_bl_prev_principal`, `zz_ef_bl_woff_now` | коэффициент урезания, прошлый принципал, признак списания | `zz_ef_bond_ledger_step` | слоты держателей |
| карты `zz_ef_rq_tr_b`, `zz_ef_rq_bk_b` (держатель) | наши доли долга продавцов: казна, банки | `zz_ef_bl_register`, `zz_ef_bl_hold_one` | `zz_ef_bl_parts`, `zz_ef_bl_bank_parts`, `ld_bond_tables.txt` |
| `zz_ef_bl_acc_<F>` / `zz_ef_f_bl_<F>` (`sold`,`int_out`,`redeem`,`woff`) | недельные суммы продавца | `zz_ef_bl_acc_add` / `zz_ef_bl_roll` | `zz_ef_v_f_bl_*` (модель денег, лог) |
| `zz_ef_f_bl_buy/refund/int_in/back/lost/int_short`, `zz_ef_f_pb_*` | потоки держателя за неделю | слоты | модель денег (`EFM`) |
| `zz_ef_consol_debt` | долг казны населению по консолям | `zz_ef_consol_step` | `zz_ef_consol_debt_v`, `zz_ef_consol_debt_to_gdp` |
| `zz_ef_f_cons_sale/int/buy` | потоки консолей за неделю | `zz_ef_consol_step` | `zz_ef_v_f_cons_*` |
| `ai_buy_bond_N_on`, `ai_seller_country_general_N`, `ai_total_bond_value_N`, `ai_interest_per_month_calculated_N` | слот ИИ-покупки E&F | `ai_buy_bond_N`, `bond_maturity_N` | реестр, `zz_ef_treasury_bonds` (`ld_money_model_values.txt:1996`), таблицы |
| `total_bond_value_N`, `buy_bond_N_on`, `seller_country_general_N` | слот покупки игроком | кнопки `buy_bond_*_market_panel_*`, `bond_maturity_N` | таблицы |
| `zz_ef_bt_t_amt/_week/_b_amt/_b_year`, `zz_ef_bto_*` | строки таблиц (на стране) | `zz_ef_bonds_update` | GUI |

## Вызовы и связи
- `zz_ef_foreign_assets` = `zz_ef_bank_bonds` + `zz_ef_treasury_bonds` (`ld_money_model_values.txt:1999-2008`) — позиция «за рубежом» M3.
- Реестр берёт E&F-слоты как источник цены/продавца и сам перераспределяет деньги; процент за неделю берёт у движка (`zz_ef_v_g_ipay`).
- Пул продавца (`investment_pool`) платит процент и погашения (не больше, чем там есть; недостающее — `zz_ef_f_bl_int_short`/`lost`).
- Учёт (R2, шаг 7): у продавца выручка от продажи долей (в пул) и выплаты держателям (из пула) — капитал его банков
  (`zz_ef_bl_seller_capital`, `_out`); у банков-держателей доли — актив книги (`zz_ef_bank_bonds` в `zz_ef_bank_book_v`), списание
  доли и недоплата продавца — из их капитала (`zz_ef_bl_short_pool`); покупка облигации казной ИИ (`ai_buy_bond_N`, цена из казны) помечена
  как наша (`zz_ef_tr_unmark`), возврат лишнего и проценты — уже помечены. Слоты игрока (`buy_bond_*`, погашение `bond_maturity_N`) реестр
  не ведёт — открыто.
- Облигации ЦБ как товар `bond` — `pm_*_standard_bank_money_currency` (`production_methods/15_ef_bank.txt`, `goods_output_bond_add`), множитель по долгу — `ld_cb_bond_issuance.txt`.
- Смежные: `ld_capitalization_snapshot.txt` (счётчики E&F), `ld_reference_currency_values.txt:86-112` (проценты частным банкам).

## Логи
- `EFB|` — состояние реестра страны (принципал, доли, проценты) — `ld_bond_ledger.txt:91`.
- `EFP|` — частные банки: `no_seller` (покупка без продавца возвращена в пул).
- `EFS|` — консоли: долг, продажа, проценты, выкуп.
