# Облигации и консоли
**Смысл.** Госдолг как доли держателей в долге движка; консоли — бессрочный долг казны населению. Сейчас — слоты E&F,
цель — словари требований (R8б) и аукцион на бирже (R5). **Понятия:** [[Облигации]], [[Консоли]], [[Казна]],
[[Словарь требований]]. **Решения:** Д.R2.7, Д.R4а.13 (`решения.md`).

Облигации — доли в движковом долге продавца (`principal`): «реестр облигаций» `ld`. Доли держит реестр требований
(`claims.md`): карты казны `zz_ef_rq_tr_b` и банков `zz_ef_rq_bk_b`, ключ — продавец. Доли покупаются на бирже (стакан,
`exchange-companies.md`; банки продают за рубеж долю внутреннего долга — Д.R6.6); покупки ИИ E&F (казна —
`ai_buy_bond_1..10`, частные банки — `ai_privat_bank_bond_1..25`) — в `_archive/ef_ai_treasury_bonds/` (R6.9, Д.R6.6);
кнопки покупки игрока E&F (`buy_bond_N`, `bond_maturity_N`) — пока живые (остаток архива — R6.9). Облигации ЦБ,
проданные населению, — консоли (бессрочный долг казны населению). Выплаты процентов и погашение идут деньгами между
пулами/казнами, а не «из воздуха». Ключи в `ld_*` файлах — `zz_ef_*` (комментарии называют старые файлы `zz_ef_*.txt`).

## Файлы
- `common/scripted_effects/ld_bond_ledger.txt` — генерат (`tools/regen_ef_bond_ledger.py`): `zz_ef_bond_ledger_step`
  (недельный шаг: сторона продавца, доли держателя), `zz_ef_bl_hold_map` / `zz_ef_bl_hold_one` (каждая доля: урезание по
  `zz_ef_bl_ratio` продавца, погашение равными долями за `zz_ef_bl_term_weeks`, проценты), помощники
  `zz_ef_bl_pay/roll/acc_add/into_*/woff_*/icap_*`. Слоты покупок E&F (`zz_ef_bl_slot_N`, `zz_ef_pb_slot_N`,
  `zz_ef_bl_register`, `zz_ef_bl_slot_free`, `zz_ef_pb_no_seller`) — в `_archive/ef_ai_treasury_bonds/`.
- `common/script_values/ld_bond_ledger_values.txt` — `zz_ef_bl_principal` (долг движка), `zz_ef_bl_held_v` (доли за
  рубежом — итог реестра `zz_ef_rq_out_b`), `zz_ef_bl_room`, `zz_ef_bl_int_per_part` (недельный процент на единицу, ≤
  0.01, из `zz_ef_v_g_ipay`), `zz_ef_bl_term_weeks` (390 — средний срок слотов E&F 5 и 10 лет), `zz_ef_bl_parts` /
  `zz_ef_bl_bank_parts` (наши доли казны / банков — итоги карт), потоки `zz_ef_v_f_bl_*`, `zz_ef_v_f_pb_*`.
- `common/script_values/ld_bond_tables_values.txt` — ключи сортировки таблиц (`zz_ef_bt_in_key`, `zz_ef_bt_out_key`),
  ставки строк.
- `common/scripted_guis/ld_bond_tables.txt` — `zz_ef_bonds_update`: заполняет глобальные списки `zz_ef_bt_in_list` («кто
  держит наши облигации») и `zz_ef_bt_out_list` («чьи облигации держим») при открытии таблицы — по картам реестра и
  слотам игрока E&F.
- `common/scripted_effects/ld_gov_loan.txt` — `zz_ef_gov_loan_step` (недельный, сразу после реестра; Д.R5.2, Д.R5.9):
  долг игры внутри страны (`zz_ef_gov_loan_home_v` = `principal` − `zz_ef_bl_held_v`) — актив банков
  `zz_ef_bank_gov_loan` (книга `zz_ef_bank_book_v` его вычитает; первый шаг — актив и капитал); изменение долей за
  рубежом — актив и капитал; рост `principal` — займ из пула (`zz_ef_f_gl_pool` < 0; недостаток пула `zz_ef_f_gl_short`
  — кредит ЦБ банкам, без ЦБ — капитал; в `zz_ef_heir_debt_steps` — долг наследника: актив и капитал,
  `zz_ef_f_gl_heir`); падение — погашение в пул, в дефолте — списание (актив и капитал); проценты на долю банков
  (`zz_ef_v_g_ipay` × доля × недели шага) — в пул и капитал. Пул-поток — строка карточки пула и вне
  `zz_ef_pool_other_week`; `zz_ef_f_gl_short` — вне статьи утечки. Лог `EFB|…|gov_loan`. Значения —
  `common/script_values/ld_gov_loan_values.txt`. Свои облигации банков на бирже (Д.R6.6): `zz_ef_xch_post_sells_ob`
  (`ld_exchange_trade.txt`, неделя держателя) — заявка держателя `ob` на `zz_ef_xch_ob_share` (1 %) от
  `zz_ef_bank_gov_loan` по справедливой × (1 + выгода банков), не выше верхнего шага стакана (`zz_ef_xq_top`); сделка не
  трогает реестр продавца (`zz_ef_xch_is_own_b`), цена — в пул и капитал (`zz_ef_xch_pay_ob_b`), доля покупателя — его
  карта, итог `zz_ef_rq_out_b` растёт — на следующем шаге здесь актив и капитал вниз на долю.
- `common/scripted_effects/ld_consols.txt` — `zz_ef_consol_step` (недельный: продажа → долг, проценты казна → сбережения
  населения, выкуп излишка казны). При частном ЦБ с компанией-ЦБ (`zz_ef_consol_private`,
  `common/scripted_triggers/ld_consols_triggers.txt`; Д.R9б.12) консоли — долг компании: проценты и выкуп (счёт сверх
  годовых процентов, за год — принято ночью, `zz_ef_consol_co_buyback_week`) — со счёта компании-ЦБ `zz_ef_co_acc` во
  вклады населения (`zz_ef_post` вклады компаний → вклады населения, поток `zz_ef_f_co_div` — карточка вкладов; за
  неделю — `zz_ef_f_cons_co`, лог `EFS|…|co`); казна не платит.
- `common/script_values/ld_consols_values.txt` — `zz_ef_consol_output`, `zz_ef_consol_sale_week`, `zz_ef_consol_debt_v`,
  `zz_ef_consol_interest_week`, `zz_ef_consol_buyback_week`, `zz_ef_consol_debt_to_gdp`, потоки `zz_ef_v_f_cons_*`.
- `common/scripted_effects/ld_cb_bond_issuance.txt` — `zz_ef_cb_bond_issuance_update` (товар «облигации» выпускают «Банки»
  страны с ЦБ — по размеру ЦБ и долгу / ВВП, Д.R9б.1; зов из `update_modifiers_bc_fc_ns`) — смежно, `central-bank.md`.
- E&F, облигационная часть:
  - `common/scripted_effects/01_financial_scripted_effects.txt`: `bond_maturity_1..10` (годовой счётчик срока слота
    игрока, сброс слота), `buy_bond_in_currrency_var` (:32059), `country_credit_rating` (:18), `sovereign_bond_yields`
    (:499), кризисы (`currency_crisis` :33346, `economic_crisis`, `financial_crash`, `central_bank_bankruptcy`,
    `country_bankruptcy`), `central_bank_debt_buyer_list_clear`.
  - `common/scripted_effects/00_on_action_main.txt`: `financial_center_ef_on_yearly_pulse_country`,
    `bond_maturity_on_action` (слоты игрока; ИИ-часть — в архиве).
  - `common/scripted_guis/00_financial_scripted_guis.txt` — кнопки игрока: `buy_bond_market_panel_5Y/10Y`,
    `buy_bond_in_currrency_market_panel_5Y/10Y`, `increase_bond_quantity`, `reduce_bond_quantity`, `set_debt_issued`,
    `refund_credit_at_central_bank*`, `base_rate_increase/reduce`, `speculative_share_N_button`; окно:
    `gui/00_ef_deported_gui_1.gui` (:81879 и др.).
  - `common/history/global/00_ef_financial_global_variable.txt` — стартовые `speculative_share_N` и переменные слотов.

## Поток / порядок
- Неделя (`zz_ef_money_model_step`): `zz_ef_bond_ledger_step` — продавец: прокатка недельных сумм (`zz_ef_bl_roll` для
  `sold`, `int_out`, `redeem`, `woff`), `zz_ef_bl_ratio` = principal / доли за рубежом (итог реестра), если принципал
  упал ниже долей (списание — только при `in_default` и падении принципала вдвое); держатель: каждая доля карт
  `zz_ef_rq_tr_b` (в казну) и `zz_ef_rq_bk_b` (в пул банков; проценты — в капитал банков): урезание при `zz_ef_bl_ratio`
  < 1 (выкуп из пула продавца или списание в дефолте), погашение 1 / `zz_ef_bl_term_weeks` в неделю, проценты
  `zz_ef_bl_int_per_part` из пула продавца. Продавец не признан (децентрализован) — доля списана. Лог `EFB|`. Доли
  входят в карты только сделками биржи (`zz_ef_xch_deal`).
- Позже в том же шаге (`ld_money_model.txt:238`): `zz_ef_consol_step`: до отчисления излишка казны в пул. Неделя продаж
  `sg:bond.state_goods_production` × `bond_price` → `zz_ef_consol_debt`; проценты по ставке правительства / 52 — казна →
  `zz_ef_pop_savings`; выкуп, когда казна выше предела (`gold_reserves_limit`). Лог `EFS|`.
- Год (`financial_center_ef_on_yearly_pulse_country`): `sovereign_bond_yields`, `bond_maturity_on_action`
  (`bond_maturity_N` — слоты игрока); покупки ИИ E&F — в архиве.
- Проценты частным банкам по их долям — в реестре, как казне (R8б.2; прежняя половина E&F —
  `_archive/ld_privbank_interest/`).
- Таблицы: кнопка в Бюджет → Финансы, `gui/ld_cb_rate_panel.gui:12404…17347` (`zz_ef_bt_in_list`/`zz_ef_bt_out_list`,
  `zz_ef_bt_button`).

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `zz_ef_rq_out_b` (страна-продавец) | доли нашего долга за рубежом — итог реестра (`claims.md`) | `zz_ef_rq_add` | `zz_ef_bl_held_v`, `zz_ef_bl_room` |
| `zz_ef_bl_ratio`, `zz_ef_bl_prev_principal`, `zz_ef_bl_woff_now` | коэффициент урезания, прошлый принципал, признак списания | `zz_ef_bond_ledger_step` | слоты держателей |
| карты `zz_ef_rq_tr_b`, `zz_ef_rq_bk_b` (держатель) | наши доли долга продавцов: казна, банки | биржа (`zz_ef_xch_deal`), `zz_ef_bl_hold_one` | `zz_ef_bl_parts`, `zz_ef_bl_bank_parts`, `ld_bond_tables.txt` |
| `zz_ef_bl_acc_<F>` / `zz_ef_f_bl_<F>` (`sold`,`int_out`,`redeem`,`woff`) | недельные суммы продавца | `zz_ef_bl_acc_add` / `zz_ef_bl_roll` | `zz_ef_v_f_bl_*` (модель денег, лог) |
| `zz_ef_f_bl_buy/refund/int_in/back/lost/int_short`, `zz_ef_f_pb_*` | потоки держателя за неделю (`buy`/`refund` — 0: покупок E&F нет) | `zz_ef_bl_hold_one` | модель денег (`EFM`) |
| `zz_ef_consol_debt` | долг казны населению по консолям | `zz_ef_consol_step` | `zz_ef_consol_debt_v`, `zz_ef_consol_debt_to_gdp` |
| `zz_ef_f_cons_sale/int/buy` | потоки консолей за неделю | `zz_ef_consol_step` | `zz_ef_v_f_cons_*` |
| `ai_seller_country_general_N`, `ai_total_bond_value_N`, `ai_interest_per_month_calculated_N` | слот ИИ-покупки E&F — больше не пишутся (покупки — в архиве), читает окно E&F (остаток архива — R6.9) | стартовые значения `10_new_country_var.txt` | окно E&F, `ld_cb_rate_panel.gui` |
| `total_bond_value_N`, `buy_bond_N_on`, `seller_country_general_N` | слот покупки игроком | кнопки `buy_bond_*_market_panel_*`, `bond_maturity_N` | таблицы |
| `zz_ef_bt_t_amt/_week/_b_amt/_b_year`, `zz_ef_bto_*` | строки таблиц (на стране) | `zz_ef_bonds_update` | GUI |

## Вызовы и связи
- `zz_ef_foreign_assets` = `zz_ef_bank_bonds` + `zz_ef_treasury_bonds` (`ld_money_model_values.txt`) — облигации в
  счёте «заграница»; в M3 — облигации населения и фонда биржи и консоли (Д.R9б.11), не эти.
- Процент за неделю реестр берёт у движка (`zz_ef_v_g_ipay`).
- Пул продавца (`investment_pool`) платит процент и погашения (не больше, чем там есть; недостающее —
  `zz_ef_f_bl_int_short`/`lost`).
- Учёт (R2, шаг 7): у продавца выручка от продажи долей (в пул) и выплаты держателям (из пула) — капитал его банков
  (`zz_ef_bl_seller_capital`, `_out`); у банков-держателей доли — актив книги (`zz_ef_bank_bonds` в
  `zz_ef_bank_book_v`), списание доли и недоплата продавца — из их капитала (`zz_ef_bl_short_pool`). Слоты игрока
  (`buy_bond_*`, погашение `bond_maturity_N`) реестр не ведёт — остаток архива (R6.9).
- Облигации ЦБ как товар `bond` — `pm_*_standard_bank_money_currency` (`production_methods/15_ef_bank.txt`,
  `goods_output_bond_add`), множитель по долгу — `ld_cb_bond_issuance.txt`.
- Смежные: `ld_capitalization_snapshot.txt` (средние капитализации), `ld_reference_currency_values.txt:86-112` (проценты
  частным банкам).

## Логи
- `EFB|` — состояние реестра страны (принципал, доли, проценты) — `ld_bond_ledger.txt:91`.
- `EFP|` — частные банки: `no_seller` (покупка без продавца возвращена в пул).
- `EFS|` — консоли: долг, продажа, проценты, выкуп.
