# Денежная модель и счета
**Смысл.** Учёт денег страны двойной записью: реестр счетов, проводки, сверка по запасам, агрегаты M0–M3, кредит, роли и
планировщик, металл ЦБ / банков / населения. **Понятия:** [[Проводка]], [[Сверка по запасам]], [[Денежная масса]],
[[Инвестиционный пул|Пул]], [[Группа населения|Население]], [[Металл]], [[Роли стран]], [[Планировщик]]. **Решения:**
Д.R0.8.1–11, Д.R1а.1–6, Д.R1б.1–2, В.R1б.3–4, Д.R2.1–14 (`решения.md`).

Недельная двойная запись в деньгах движка: счета страны (казна, пул банков, наличные бизнеса, сбережения и вклады
населения, касса ЦБ), агрегаты M0–M3, кредит ЦБ банкам, потребительский и бизнес-кредит, ставка правительства. Рядом —
счета металла (золото/серебро у ЦБ, банков, населения) и запасы валют E&F («stockpile»). Нацзапас товаров E&F вынесен в
`_archive/ef_national_stockpile/`. Игрок видит результат в карточках денежной массы и ЦБ (разметка в
`gui/ld_economy_panel.gui`, переменные читает она).

## Файлы
- `common/on_actions/ld_money_model_on_actions.txt` — месячный шаг `zz_ef_money_model_monthly` (зовёт планировщик).
- `common/scripted_effects/ld_scheduler.txt`, `common/on_actions/ld_scheduler_on_actions.txt`,
  `common/script_values/ld_scheduler_values.txt` — планировщик (ниже).
- `common/scripted_effects/ld_start_setup.txt`, `events/ld_start_setup_events.txt` — `zz_ef_start_setup` (события
  `ld_start_setup.1` / `.2` каждой стране, root — страна): настройка старта E&F с первого дня (из годового пульса —
  ступени ВВП, ЦБ и финцентры по ВВП, рейтинг, списки эталона; месячный хаб целиком), один раз на первом бюджетном тике
  после первой недели (не раньше 8.1), до шагов модели.
- `common/scripted_effects/ld_money_model.txt` — недельный шаг, приёмник GUI-моста, ежемесячный шаг, сбережения/вклады,
  кредиты, кольца истории, ставка правительства, стартовый металл ЦБ (`ld_metal_accounts.txt`), выкуп валюты в кризис,
  зонды.
- `common/script_values/ld_money_model_values.txt` — все формулы: счета, M0–M3, кредитные лимиты, ставки, платёжный
  баланс, кольца роста (почти все ключи `zz_ef_*`).
- `common/scripted_effects/ld_metal_accounts.txt` — старт металла, недельные покупки/продажи ЦБ/банков/населения, выкуп
  у населения, сверка металла ЦБ, мировая линия металла.
- `common/scripted_triggers/ld_metal_triggers.txt` — `zz_ef_cb_metal_standard` (ЦБ на стандарте с металлом);
  `zz_ef_metal_gold/_silver/_bimet` — металл стандарта по закону (у внешневалютного — по закону якоря
  `var:zz_ef_anchor`), `zz_ef_exchange_std` (Д.R8а.6).
- `common/scripted_effects/ld_anchor.txt` — `zz_ef_anchor_update` (якорь внешневалютного), `zz_ef_anchor_metal_step`
  (запасы ЦБ — в металл якоря).
- `common/script_values/ld_metal_accounts_values.txt` — единицы металла, нормы резерва, покупки через модификаторы
  зданий, продажа ЦБ, выкуп, мировые суммы.
- `common/scripted_effects/ld_money_log_rest.txt` — сгенерированный `debug_log` «прочее» карточек (`EFO`); не править
  (генератор `tools/regen_ef_money_supply_loc.py`).
- `common/scripted_guis/ld_money_hook.txt` + `gui/ld_money_hook.gui` — мост GUI→скрипт: строки бюджета, доступные только
  GUI, передаются в `zz_ef_money_hook_receive`.
- `common/scripted_effects/ld_currency_intro_metal.txt` — обёртка вокруг введения валюты E&F
  (`introduction_new_currency`): металл столицы возвращается как был.
- `common/scripted_effects/ld_subject_metal.txt` — `zz_ef_cb_state_owner_step` (металл ушедшего ЦБ-региона возвращается
  прежнему владельцу).
- `common/scripted_effects/ld_stockpile_state_var_seed.txt`, `common/on_actions/ld_stockpile_state_var_init.txt`,
  `common/history/global/zz_ef_init_stockpiling_state_vars.txt` — засев 5 переменных `stockpiling_*_var_state_1` и двух
  вспомогательных на регионах (`financial_center_site_var`, `looted_state`); GLOBAL-блок истории (новая кампания),
  `on_game_started_after_lobby` и месячная страховка (раз за игру по глобальной `zz_ef_stockpile_state_vars_seeded`).
- `common/pop_needs/ld_metal_hoard.txt` — потребность населения: серебро/золото как накопление (по 0.5).
- `common/production_methods/ld_gold_mine_minting_off.txt` — INJECT в методы золотых шахт: обнуляет
  `country_minting_add`.
- `common/static_modifiers/ld_metal_trade.txt` — модификаторы зданий: покупка металла банками/ЦБ, продажа ЦБ
  (`zz_ef_bank_gold_buy`, `zz_ef_bank_silver_buy`, `zz_ef_cb_metal_buy`, `zz_ef_cb_gold_sell`, `zz_ef_cb_silver_sell`).
- `common/static_modifiers/ld_consumer_credit.txt` — `zz_ef_consumer_credit` (`state_dependent_wage_add`).
- `common/static_modifiers/ld_debt_service.txt` — `zz_ef_debt_service` (+1% взноса в пул у слоёв).
- E&F вне списка, но пишут те же счета: `common/scripted_effects/ld_claims.txt` (`zz_ef_rq_crisis_resell`, кризисная
  продажа валют); месячный пересчёт запасов `stockpiling_currency_type_1` — в `_archive/ef_stockpiling_currency/` (R2).

## Реестр счетов, проводка, сверка (R1а.5)
Файлы: `common/scripted_effects/ld_ledger.txt`, `common/script_values/ld_ledger_values.txt`.
| счёт | переменная (страна) | чей | движет |
| --- | --- | --- | --- |
| казна | движок: `gold_reserves` (`zz_ef_treasury`), в сверке — за вычетом долга `principal` | государство | бюджет движка; наши проводки `zz_ef_post_eng*` (`ENG = treasury`) и прочие наши `add_treasury` — все с пометкой `zz_ef_tr_posted` |
| касса бизнеса (M1) | движок: `cash_reserves` зданий (`zz_ef_bcash`); касса торговых центров — её часть | бизнес | движок |
| пул (касса банков) | движок: `investment_pool` | банки — по счетам ниже | движок (взносы, стройка, выкуп), наши проводки (`ENG = pool`) |
| вклады населения | `zz_ef_pop_deposits` | население | вклады / изъятия, проценты |
| банкноты в обращении = наличные населения (M0) | `zz_ef_notes` | долг ЦБ (без ЦБ — банков) населению; вне книги банков | консоли (казна → банкноты), выкуп металла ЦБ (новые банкноты); старт 0 |
| вклад инвестиционного фонда | `zz_ef_fd_dep` (страна биржи) | фонд биржи | `ld_investment_fund.txt`: паи — вклады населения и капитал банков → вклад (покупатель за границей — из своего пула в пул страны фонда), стартовый вклад — доля капитала банков, проценты по ставке вкладов — из капитала банков; входит в M2 (`exchange-companies.md`) |
| вклады чужих ЦБ | `zz_ef_nr_dep` | заграница | `ld_nr_deposits.txt`: клиринг; проценты — из капитала банков (`zz_ef_post`); вклады чужих банков и населения — счетов пока нет (писателей нет: R7, R8) |
| кредит ЦБ банкам | `zz_ef_bank_cb_debt` | ЦБ | недельный шаг; только при ЦБ (`has_central_bank`: без ЦБ цель `zz_ef_cb_credit_target` = 0, долг гасится из пула) |
| деньги казны в банках | `zz_ef_bank_gov_dep` | казна | не пишется: перевод излишка казны в пул — в архиве (`_archive/ld_tr_surplus_pool/`), вклад государства — кнопкой E&F проводкой (R4); поток `zz_ef_f_tr_pool` = 0 |
| кредит ЦБ казне | `credit_at_central_bank` (E&F, деньги движка; `government_loan` — зеркало в валюте E&F) | ЦБ (актив), долг казны | заём / возврат — кнопки `set_debt_issued`, `refund_credit_at_central_bank(_all)`, ИИ `ai_credit_at_central_bank` / `ai_refund_central_bank`: казна ↔ счёт (`zz_ef_eng_add/sub_treasury`); прощение без денег (ИИ) — списание ЦБ `zz_ef_cb_writeoff` |
| капитал банков | `zz_ef_bank_capital` | банки (агрегат) | первая сверка (пул − остальные счета), проценты ЦБ (`zz_ef_post_eng_paid`), проценты вкладам населения и чужих ЦБ (`zz_ef_post`); облигации (R2): у продавца — выручка от продажи долей и выплаты держателям из пула (`zz_ef_bl_seller_capital(_out)`), у банков-держателей — списания долей |
| потреб- / бизнес-кредит | `zz_ef_cc_debt`, `zz_ef_bc_debt` | банки (актив) | `zz_ef_consumer_credit_step`, `zz_ef_business_credit_step` |
| доли банков в чужих облигациях | `zz_ef_bank_bonds` (= Σ `ai_privat_bank_bond_value_N` E&F) | банки (актив) | покупка E&F `ai_privat_bank_bond_N` (пул → доля), реестр облигаций (`ld_bond_ledger.txt`: возврат лишнего — пул, выкуп — пул, списание и недоплата продавца — из капитала банков) |
| требования населения | `zz_ef_pop_claims_stocks`, `_bonds`, `_private` | население | по нулям (R6, R7) |
| позиция клиринга недели | `zz_ef_clr_pos` (золото) | страна | `zz_ef_clr_step`, снимается расчётом `zz_ef_clr_settle` (`clearing-fx.md`) |
| металл ЦБ / банков / населения | `gold_state_1` / `silver_state_1` штата ЦБ, `zz_ef_bankm_*`, `zz_ef_popm_*` | — | `ld_metal_accounts.txt`; у ЦБ биметаллизма — арбитраж через биржу (`zz_ef_f_mt_arb_g/_s`, `exchange-companies.md`) |
Счета, которых нет, заводит `zz_ef_registry_init` из `zz_ef_country_init` — первый заход планировщика (раз за игру,
признак `zz_ef_registry`).

**Проводка** — пара счетов, одна сумма: `zz_ef_post = { FROM TO V }` (наш → наш), `zz_ef_post_from_eng = { ENG TO V }`,
`zz_ef_post_to_eng = { FROM ENG V }`, `zz_ef_post_eng = { FROM TO CLAIM V }` (казна ↔ пул и требование на CLAIM),
`zz_ef_post_eng_paid = { FROM TO PAYER V }` (то же, платит PAYER); `ENG` — `treasury` / `pool`, `V` — один токен.

**Сверка по запасам** (`zz_ef_reconcile`, конец недельного шага): «прочее» `zz_ef_other` = часть пула + часть казны.
Пул: `zz_ef_other_pool` = пул − книга банков `zz_ef_bank_book_v` (вклады населения, фонда и чужих ЦБ + кредит ЦБ +
деньги казны + капитал − потреб- и бизнес-кредит − доли в чужих облигациях `zz_ef_bank_bonds`). Казна (В5):
`zz_ef_other_tr` копится по шагам — изменение казны за вычетом долга (`zz_ef_treasury_net_v` = `gold_reserves` −
`principal`; снимок `zz_ef_tr_prev`) − бюджет движка недель шага (`zz_ef_budget_steps_v` = `zz_ef_budget_week` × недели
шага) − наши проводки на казну `zz_ef_tr_posted` (каждый наш `add_treasury` помечен `zz_ef_tr_mark` / `zz_ef_tr_unmark`:
проводки `zz_ef_post_eng*`, консоли, денежная политика, реестр облигаций `zz_ef_bl_into_treasury`, выкуп сектора PSC —
казна → пул, вклады населения; сверка обнуляет), изменение за шаг — `zz_ef_f_other_tr`; первая сверка берёт только
снимок. **Выкуп уровней движком** (приватизация: 250 × очки стройки уровня, без хука) — отдельная статья, не «прочее»:
изменение части пула за шаг, целое отрицательное кратное `zz_ef_lvl_unit` (25 000; `zz_ef_lvl_is_buy_v`), копится в
`zz_ef_lvl_buy_pool` и вычитается из `zz_ef_other_pool`; положительное кратное казны — в `zz_ef_lvl_buy_tr`
(государство-продавец); за шаг — `zz_ef_f_lvl_buy_pool/_tr`. Смешанное в одном шаге с другими деньгами остаётся
«прочим»; проводка — R6. Касса бизнеса — счёт движка, читается как есть. Изменение «прочего» за шаг — `zz_ef_f_other`;
первая сверка ставит капитал так, что часть пула 0. «Прочее» никому не зачисляется; в нём — записи E&F в казну и пул
мимо модели (покупки облигаций `ai_buy_bond_N`, кнопки E&F) и то, что движок делает сверх бюджета. Лог `EFJ` (страна:
прочее, изменение, часть пула, часть казны, выкуп уровней пула и казны, изменение части казны, казна за вычетом долга,
бюджет, пул, книга, капитал, вклады, недель в шаге, роль) и `EFJ|WORLD` в мировом проходе (сумма изменений, из них
казна, сумма модулей, число стран за неделю). Потоковые остатки карточек (`tr_other`, `pool_other`, утечка) — только
разбивка (R10). Значения для окон: `zz_ef_v_other`, `zz_ef_v_f_other`.

## Население: наличные и вклады (R1а.6)
Решение Д.R1а.6 (пользователь 7.10): пул — деньги в банке, взнос попа в пул — его вклад. Счета населения: сбережения S
`zz_ef_pop_savings` = наличные (M0) + вклады D `zz_ef_pop_deposits`; позже — металл, акции.
- **Вклады = взносы движка** (`zz_ef_pop_deposits_step`, недельный шаг после бизнес-кредита): D и S += взносы пула
  (`investment_pool_gross_income` × недели шага) − часть, что гасит бизнес-кредит (`zz_ef_f_bc_paid`) —
  `zz_ef_f_dep_contrib`; своих денег в пул за них не кладём (проба 7.10: наш `add_investment_pool` во взносы движка не
  входит). Частная стройка пула (перевод в казну) сверх нового бизнес-кредита оплачена из вкладов: D → требования
  «частный сектор» `zz_ef_pop_claims_private` (`zz_ef_f_dep_build`; правило не проверено прогоном, R6). Плановая
  экономика (`law_command_economy`) — пула нет, вкладов нет.
- **Бизнес-кредит** (`zz_ef_business_credit_step`): новый — частная стройка пула × доля заёмных денег банков в пуле
  `zz_ef_bc_borrowed_share` (кредит ЦБ + вклады населения + вклад казны `zz_ef_bank_gov_dep`), не выше запаса кредита
  `zz_ef_credit_room`; долг `zz_ef_bc_debt` гасится из взносов зданий в пул.
- **Наличные** (M0) — банкноты, долг ЦБ населению (В3): счёт `zz_ef_notes`, `zz_ef_pop_cash` читает его; S = банкноты +
  D. Двигают только проводки: консоли (`zz_ef_post_from_eng` казна → `zz_ef_notes`), выкуп металла ЦБ (новые банкноты).
  Старт — 0; старый сейв без счёта — банкноты = S − D (в начале недельного шага). Норма наличных от ВВП и наличные ↔
  вклады по ней — в `_archive/ld_cash_norm/` (поведение — R7). Остаток сверки недели («утечка» `zz_ef_f_leak`) и
  необъяснённая убыль пула — «прочее», в сбережения не идут. Догадки хотфикса (выкуп уровней и события казны →
  сбережения, излишек → «в богатство») вынуты в `_archive/ld_pop_savings_guesses/`.
- **Проценты** по вкладам — капитал банков → D (`zz_ef_post`), по бизнес- и потребкредиту — в капитал банков.
- Стартовые сбережения — только вклады (`zz_ef_pop_start_deposits` = `zz_ef_pop_start_savings` = норма накоплений
  `zz_ef_sav_norm`, но не больше `zz_ef_dep_start_pool_share` = 90 % пула — остальное капитал банков), при первом
  `zz_ef_pop_savings_step`; принято ночью, проверить.
- `zz_ef_f_inflow` — что вошло в сбережения за шаг (взносы − стройка), карточка наличных (`zz_ef_v_w_inflow`).

## Торговля — одна проводка (R1а.7)
Мера — торговля рынка по базовым ценам (`zz_ef_trade_net_week`). Страна одна в своём рынке — торговля рынка целиком; в
рынке двух стран и больше ([[Один рынок]], Д.R8в.1) — её доли: p × (X + T) − c × (M + T), где p / c — доли страны в
производстве / потреблении рынка (`var:zz_ef_msh_p` / `_c`, раз в месяц, `ld_market_shares.txt`), X / M — продажи и
покупки рынка за границу (`var:zz_ef_mk_xr` / `_mr` у владельца), T — оборот внутри рынка (производство рынка
`zz_ef_trade_production_week` − экспорт, `var:zz_ef_mk_t`); член читает последние числа владельца. Сумма по членам —
торговля рынка (`var:zz_ef_f_exp_my` / `_imp_my` — доли продаж и покупок за границу, `_tin` — оборот внутри). Масштабы
мирового пула (`zz_ef_wtr_kr` / `_kp`) — прошлого окна; клиринг сводит неделю её собственными (`zz_ef_clr_settle`, Ч4).
Считается раз за шаг в `zz_ef_trade_step` (`ld_money_model.txt`, в начале недельного шага): экспорт и импорт (по 53
товара) — в `zz_ef_f_exp` / `zz_ef_f_imp`, чистая — в `zz_ef_f_trade` (× недели шага у Б); клиринг
(`zz_ef_ext_net_week`), платёжный баланс и мировой пул торговли читают эти переменные. Касса торговых центров
(`zz_ef_tc_cash`, счёт `tc`) — часть кассы бизнеса (M1), за границу не вычитается.

## Дивиденды через границу (R8в, шаг 3)
[[Дивиденды через границу]], Д.R8в.6. `zz_ef_div_net_week` (`ld_money_model_values.txt`) — строка потока с заграницей
(`zz_ef_f_div`): приток = ВВП наших владельцев за рубежом (`var:zz_ef_g_aown`, мост) × `global_var:zz_ef_wdv_r` (мир:
заплачено за неделю / ВВП во владении за рубежом, окно — `zz_ef_world_window_open`); отток `zz_ef_div_pay_week` = ВВП во
владении иностранцев (`var:zz_ef_g_fown`) × `var:zz_ef_div_y` / 52 (прибыль зданий за год / ВВП, месячный шаг, предел
`zz_ef_div_yield_max` 0,5). Мировая сумма оттока — `global_var:zz_ef_wld_wdpay` (`zz_ef_world_acc`).

## Роли стран (R1а.3, R8б.3)
`var:zz_ef_role`: 1 — **А** (полный шаг каждую неделю), 2 — **Б** (тот же недельный шаг, мост раз в 4 недели; агрегаты
субъектов — R4 / R6), 3 — **В** (`is_country_type = decentralized`: ни месячного шага модели, ни недельной цепочки, ни
моста; счетов нет). `every_country` децентрализованные не перебирает (прогон r1007_180243: 284 = 442 − 158), так что
переменной роли у них нет — вне планировщика, только хаб E&F через `zz_ef_monthly_unscheduled`. Проход по миру — раз в
месяц: `on_monthly_pulse` → `zz_ef_roles_world_pass` (`common/scripted_effects/ld_roles.txt`, on_action —
`common/on_actions/ld_roles_on_actions.txt`). Раз в 12 месяцев (`global_var:zz_ef_role_year_next` против номера месяца
`zz_ef_month_n`; первый — на старте) — решение года: мировые суммы ВВП и торговли (`zz_ef_role_w_gdp`,
`zz_ef_role_w_trade` — экспорт + импорт недели стран модели), затем каждой стране — А, если категория А
(`zz_ef_role_significant`, `ld_roles_triggers.txt`: игрок, великая или крупная держава, доля мирового ВВП ≥
`zz_ef_role_a_gdp_share` или торговли ≥ `zz_ef_role_a_trade_share`, `ld_roles_values.txt`; Д.R8.1, Д.R8.4), иначе Б; ЦБ
роли не даёт (Б с ЦБ, Д.R8.2). В остальные месяцы — только страна без роли, игрок (сразу А) и переход в В / из В. Смена
роли — `zz_ef_role_change` (место проводки переноса остатков; у А и Б одни и те же счета страны — переносить нечего).
Триггеры `zz_ef_role_is_a/b/v` — `common/scripted_triggers/ld_roles_triggers.txt` (нет роли — ни одна, шаг как прежде);
числа для лога `EFY` — `common/script_values/ld_roles_values.txt` (строка `EFY|…|<страна>|a|gdp_sh|trade_sh|rank` —
каждая страна А в месяц решения). Роль В снимает месячный шаг (`trigger` у `zz_ef_money_model_monthly`) и недельный
(планировщик шагает только А и Б).

## Поток / порядок
0. **Планировщик** (R1а.4): одна глобальная цепочка на «якорной» стране (крупнейшая по ВВП на момент старта; у движка
   нет глобального отложенного on_action). Старт — `on_game_started_after_lobby` (`zz_ef_sched_start`; на первом
   бюджетном тике после первой недели (не раньше 8.1) — настройка старта E&F один раз, `zz_ef_start_setup`,
   `ld_start_setup.txt`, шаги — со следующего дня: ЦБ и финцентры по ВВП, валюта подданных, металл ЦБ — первый шаг
   модели видит страну настроенной) и месячный `on_monthly_pulse` (`zz_ef_sched_ensure`, если цепочка потеряна: нет
   `global_var:zz_ef_sched_alive`, 3 дня): зонд якоря `zz_ef_sched_probe` ждёт смены казны (бюджетный тик, один день
   недели у всех стран — проверка Р10), ≤8 дней; дальше `zz_ef_sched_day` раз в день. День: `zz_ef_dom` + 1 (день
   месяца, 0 на `on_monthly_pulse`), у каждой страны роли А / Б — `zz_ef_sched_country_day`; в конце дня 6 — мировой
   проход `zz_ef_world_week_close` (окно мировой строки `zz_ef_world_window_open` и расчёт клиринга `zz_ef_clr_settle`;
   глобалка окна живёт 9 дней — запасной путь, если планировщик потерян); `zz_ef_sched_d` 0..6, `zz_ef_sched_week` + 1.
   Страна: при первом заходе `zz_ef_sched_slot_assign` — `zz_ef_week_slot` (счётчик `zz_ef_week_slot_n` по модулю 7),
   `zz_ef_week_phase` (/7 по модулю 4), `zz_ef_m_offset` = слот + 7 × фаза; **месячные шаги** — раз в календарный месяц
   (`zz_ef_m_done` против `zz_ef_month_n`), когда `zz_ef_dom` > смещения: `zz_ef_sched_monthly` по порядку — хаб E&F
   `ef_on_monthly_pulse_country`, `zz_ef_money_model_monthly`, `zz_ef_bank_monthly`, `zz_ef_cb_rate_monthly`,
   `zz_ef_capitalization_monthly`, `zz_ef_bubble_monthly`, `zz_pb_ef_overbuild_counter`, `zz_pb_ef_ai_sector_downsize`,
   `zz_ef_init_stockpile_state_vars_monthly_backstop` (с `on_monthly_pulse_country` они сняты); **недельный шаг** — в
   свой день, своим on_action `zz_ef_sched_step` (чтобы `root` был страной, а не якорем): А и Б — каждую неделю (В6);
   `zz_ef_step_weeks` — недель с прошлого шага (`zz_ef_last_step_week`, 1..8; > 1 только после разрыва — смена роли,
   перезапуск цепочки), `zz_ef_sw` умножает на него потоки, измеренные за одну неделю (взносы и перевод пула, проценты
   ЦБ / вкладов / потребкредита / бизнес-кредита / консолей / облигаций держателя, строки моста `ext`, `abr`, `aint`,
   торговля, сборы, дивиденды, вход металла зданий и потребление штатов), счётчики `zz_ef_weeks_run` и колец — на
   столько же. Страны вне планировщика (В, без роли, цепочка не запущена) получают месячный пульс движка через
   `zz_ef_monthly_unscheduled` (вместо `ef_on_monthly_pulse_country` в `00_ef_on_action.txt`): В и без роли — только хаб
   E&F; А / Б при потерянной цепочке — все месячные шаги.
1. **Месяц** (`zz_ef_sched_monthly`): `zz_ef_money_model_monthly` → `zz_ef_money_model_monthly_step` (якорь
   внешневалютного, курс серебра, сила валюты, торговый модификатор, `zz_ef_dependents`,
   `zz_ef_money_ledger_delta ACC=cb`, цена политики ставки, ставка правительства `zz_ef_gov_rate_step`, `zz_ef_mp_step`,
   модификатор частного строительства).
3. **Неделя** `zz_ef_money_model_step` (из планировщика): суммы наличных зданий и банков → обновление валютных резервов
   (`zz_ef_fx_metal_update`, `zz_ef_cbfx_week_step`) → `zz_ef_cb_state_owner_step` → `zz_ef_bond_ledger_step` → паи и
   вклад инвестиционного фонда (`zz_ef_fund_shares_step`, `zz_ef_fund_week_step`) → биржа: расчёт прошлой недели и
   заявки (`zz_ef_xch_step`, `exchange-companies.md`) → счётчик недель → старт в балансе (один раз, версия 9: металл
   населения и стран без ЦБ `zz_ef_metal_start_step` (у страны с ЦБ металл E&F остаётся в ЦБ и при старте ЦБ
   масштабируется до 40 % M2 — курс по паритету, золото и серебро одним множителем; если металлического стандарта нет 26
   недель — остаётся как есть) — туда же у стран без металлического стандарта металл E&F вне мест ЦБ, который история
   пишет в `central_bank_location` до ЦБ (Бавария), штаты — в ноль (на металле его масштабирует старт ЦБ); чужой валюты
   у ЦБ на старте нет; металл ЦБ = 40 % M2 — `zz_ef_cb_metal_start_step`, сразу после стартовых вкладов (в
   `zz_ef_bridge_apply` того же шага, и запасным вызовом в следующих шагах), где M2 / ВВП > 0,1 и у страны есть штат ЦБ
   — настройка старта E&F на первом тике строит ЦБ и пишет туда металл, старт его масштабирует) → снимок бюджета →
   кредит ЦБ банкам (`zz_ef_cb_borrow/repay/interest` в пул и `zz_ef_bank_cb_debt`, проценты в казну) →
   `zz_ef_consol_step` → `zz_ef_business_credit_step` → **`zz_ef_metal_week_step`** (счета металла, модификаторы зданий
   на следующую неделю) → кольца истории M0–M3 (w1..4, q1..13, r1..20) → поток ЦБ (переоценка, Юм, запас) →
   `zz_ef_money_ledger_delta` по каждому счёту → строка `EFW` → окна `zz_ef_money_window_roll` → постановка страны в
   глобальный список `zz_ef_hook_countries` (у Б — раз в 4 недели, когда номер недели по модулю 4 = фаза
   `zz_ef_week_phase`, и до первых чисел моста).
4. **Мост GUI — только транспорт** (R1а.8): приёмник `zz_ef_money_hook_receive` (числа `g_*` сначала 0, виджет
   переписывает их своими; из `gui/ld_money_hook.gui` по `trigger_when`, раз на шаг страны — `zz_ef_hook_pending`)
   только пишет числа: `zz_ef_hk_ext`, `zz_ef_hk_abr`, `zz_ef_hk_aint`, `zz_ef_hk_tfees`, `zz_ef_g_*`, неделю получения
   `zz_ef_hk_date_week`. Всё, что он считал раньше, — `zz_ef_bridge_apply` в конце недельного шага на последних
   полученных числах (0 до первого; неделя без моста берёт прежние): утечка, коэффициент ставки правительства,
   `zz_ef_pop_savings_step` → `zz_ef_cb_hume_step` (клиринг `zz_ef_clr_step`, мировые суммы `zz_ef_world_acc`) →
   `zz_ef_nr_dep_step` → `zz_ef_consumer_credit_step` → `zz_ef_pop_extra_income_step` → логи `EFA` / `EFR` / `EFO`.
   Числа моста приходят после шага и описывают бюджет прошлого тика — шаг их берёт на следующей неделе (у Б — те же
   числа 4 недели подряд). Тот же виджет зовёт `zz_ef_player_sg` с корнем `GetPlayer`
   (`common/scripted_guis/ld_money_hook.txt`) — страна игрока получает роль А сразу (`zz_ef_role_player_now`,
   `ld_roles.txt`); месячный проход ролей ловит `is_player` тоже. Б получает тот же набор чисел раз в 4 недели
   (сокращение до 3 чисел не даёт выигрыша: собственное время приёмника 0,004 с, профиль R0.7). **Мультиплеер (Р9, не
   проверено):** виджет есть у каждого клиента, и каждый шлёт `Execute` с корнем чужой страны; защита —
   `zz_ef_hook_pending` (первый вызов снимает его, остальные ничего не делают). Проверить: игра по сети на двух
   клиентах, `global_var:zz_ef_hook_calls` против числа шагов (`EFR` по странам) — пропускает ли движок `Execute` с
   корнем чужой страны; не пропускает — модель идёт на числах скрипта, строки моста = 0.
5. **Год**: `central_bank_ef_on_yearly_pulse_country` (E&F). Проценты частных банков по чужим облигациям
   (`investement_pool_borrowing` держателю, январская выплата эмитента) — в `_archive/ld_privbank_interest/` (В7;
   вернуть проводкой реестра облигаций, R5).

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| глобальные `zz_ef_sched_alive`, `zz_ef_sched_probing`, `zz_ef_sched_d`, `zz_ef_sched_week`, `zz_ef_dom`, `zz_ef_month_n`, `zz_ef_week_slot_n`; у якоря `zz_ef_sched_probe(_value)` | планировщик: жив (3 дня), зонд, день недели, номер недели, день и номер месяца, счётчик слотов | `ld_scheduler.txt`, `ld_roles_on_actions.txt` (месяц) | `ld_scheduler.txt` |
| `zz_ef_week_slot`, `zz_ef_week_phase`, `zz_ef_m_offset`, `zz_ef_m_done`, `zz_ef_last_step_week`, `zz_ef_step_weeks` | день недели и фаза 4 недель страны, день месяца её месячных шагов, месяц последнего, неделя последнего шага, недель в шаге | `zz_ef_sched_slot_assign`, `zz_ef_sched_country_day` | планировщик, `zz_ef_sw`, `zz_ef_step_weeks_v` |
| `zz_ef_weeks_run` | недель модели (до 100) | `zz_ef_money_model_step` | кольцо цен (с 9-й недели — статистика) |
| `zz_ef_pop_savings`, `zz_ef_pop_deposits`, `zz_ef_notes` | сбережения населения (S), вклады в банках (D), банкноты (M0); S = банкноты + D | `zz_ef_pop_deposits_step` (взносы, стройка), `zz_ef_pop_savings_step`, `zz_ef_metal_week_step` (выкуп), `ld_consols.txt` | `zz_ef_pop_cash`, M0–M3, карточки, книга банков |
| `zz_ef_bank_cb_debt` | долг банков перед ЦБ | `zz_ef_money_model_step` | `zz_ef_cb_credit_target`, кредитные лимиты |
| `zz_ef_cc_debt`, `zz_ef_bc_debt`, `zz_ef_bc_svc` | потребительский / бизнес-долг, обслуживание | `zz_ef_consumer_credit_step`, `zz_ef_business_credit_step` | значения `zz_ef_cc_*`, `zz_ef_bc_*`, модификатор `zz_ef_debt_service` |
| `zz_ef_f_<F>` (`budget`, `contrib`, `transfer`, `cb_borrow`, `cb_repay`, `cb_interest`, `tr_pool`, `ext`, `abr`, `leak`, `inflow`, `dep_int`, `trade`, `div`, …) | поток недели по статье | недельный шаг и приёмник | `zz_ef_v_f_<F>` (значения для GUI), окна `zz_ef_w_<F>` (`zz_ef_money_window_roll`) |
| `zz_ef_prev_<ACC>`, `zz_ef_<ACC>_w1..4/q1..13/r1..20` | прошлая неделя и кольца истории счета (`pool`, `buildings`, `tc`, `treasury`, `bonds`, `tbonds`, `m2`, `cbm`, `abroad`, `agg0..3`, `circ`, `gdp`, `price`, `govlv`, `savings`, `deposits`, `cb`) | `zz_ef_money_ledger_delta`, `zz_ef_ring_*_push` | `zz_ef_v_d_<ACC>`, `zz_ef_agg<N>_pct_*`, `zz_ef_circ_growth_year`, `zz_ef_price_index` |
| `zz_ef_t_led` | временная: значение счёта, посчитанное один раз в `zz_ef_money_ledger_delta` (снимается там же) | `zz_ef_money_ledger_delta` | оно же |
| `zz_ef_bcash`, `zz_ef_bkcash` | наличные бизнеса и банков за неделю | `zz_ef_money_model_step` | `zz_ef_building_cash`, `zz_ef_agg_m0..m3` |
| `zz_ef_model_started`, `zz_ef_cb_start_due`, `zz_ef_metal_started` | первый шаг страны сделан (читают вклады нерезидентов, ИИ-политика курса), ЦБ ждёт стартового металла (40 % M2, когда M2 / ВВП > 0,1 и страна — ЦБ на металле: подданный входит в зону сюзерена после первого шага; не на металле полгода — ожидание снимается), флаг первого шага металла | `zz_ef_money_model_step`, `zz_ef_metal_start_step`, `zz_ef_cb_metal_start_step` | правила металла ЦБ (`zz_ef_cb_buy_mult`, `zz_ef_cb_sell_units`, `zz_ef_cb_buyback_units`), ИИ-политика курса (`ld_monetary_policy.txt`), `zz_ef_cur_intro_after` |
| `gold_state_1`, `silver_state_1` (регион ЦБ с `central_bank_historic_place`) | металл ЦБ (переменные E&F) | `zz_ef_metal_week_step`, `zz_ef_cb_metal_start_step`, `zz_ef_metal_start_step`, `zz_ef_cb_state_owner_step`, `zz_ef_cur_intro_after`; E&F: `introduction_*` | `gold_state_native_for_stockpile`, `central_bank_reserves`, `zz_ef_cbm_gold/silver`, `zz_ef_cb_cover` |
| `zz_ef_popm_gold/silver`, `zz_ef_bankm_gold/silver` | металл населения и банков (единицы резерва) | `zz_ef_metal_start_step`, `zz_ef_metal_start_banks`, `zz_ef_metal_week_step` | `zz_ef_popm_money`, `zz_ef_bankm_money`, `zz_ef_wm_sum_*` |
| `zz_ef_f_mt_<cb_in/cb_out/bank_in/pop_in>_<g/s>`, `zz_ef_f_mt_buyback(_money)`, `zz_ef_f_mt_oth_<g/s>`, `zz_ef_mt_prev_<g/s>`, `zz_ef_mt_start_adj_<g/s>`, `zz_ef_cb_stock_acc` | покупки/продажи недели, выкуп, невязка сверки, снимок, поправка старта, изменение резервов ЦБ | `zz_ef_metal_week_step`, `zz_ef_metal_reconcile`, `zz_ef_metal_start_cb_after` | сверка следующей недели, карточка ЦБ (`zz_ef_v_f_cb_stock`) |
| `zz_ef_t_cb_in_<g/s>`, `zz_ef_t_bank_in_<g/s>` | временные: вход зданий ЦБ и банков (товары), посчитанный один раз за шаг; из них `zz_ef_f_mt_cb_in/bank_in` и часть населения (потребление штатов − они, не ниже 0; та же формула, что `zz_ef_pop_<gold/silver>_goods`) | `zz_ef_metal_week_step` | он же |
| `zz_ef_mt_bank_mult_g/s`, `zz_ef_mt_cb_mult`, `zz_ef_mt_cb_sell` | множители модификаторов `ld_metal_trade` на следующую неделю | `zz_ef_metal_week_step` | `add_modifier` на зданиях `building_zz_ef_bank` (только при `zz_ef_mt_bank_levels > 0`) / `building_bank` |
| глобальные `zz_ef_wm_<start/buy/sell/oth>_<gold/silver>` | мировая линия металла (накопительно; только при `zz_ef_logs_on`) | `zz_ef_wm_add` | `zz_ef_wm_v_*`, `zz_ef_wm_rest_*`, лог `EFV` |
| глобальные `zz_ef_hook_countries` (список), `zz_ef_hook_calls`, `zz_ef_hook_probe_calls` | очередь моста, счётчики вызовов (счётчики — только при `zz_ef_logs_on`) | `zz_ef_money_model_step`, `zz_ef_money_hook_receive`, `zz_ef_money_hook_probe_sg` | `gui/ld_money_hook.gui`, `zz_ef_hook_ok` |
| `stockpiling_<cur>_state_1`, `stockpiling_<cur>_reserve_currency_state_1` (регион, E&F) | собственный запас валюты ЦБ (E&F); чужие деньги ЦБ — карта `zz_ef_rq_cb_m` (`claims.md`) | история и ввод валют E&F | `money_supply_state` |
| `<cur>_c_no_own` (значение, 95 валют) | запас валюты минус `money_supply` | — (значения) | `currency_no_own` → `gui/ld_economy_panel.gui` (текст «currency_no_own») |

## Вызовы и связи
- Из модели вызываются другие подсистемы: `zz_ef_silver_rate_update` (мировая цена серебра к золоту раз в месяц:
  рыночная × (1 + `zz_ef_silver_demand_elasticity` × (доля серебра в деньгах металлических стандартов по M2 − её первый
  месяц)), `zz_ef_silver_to_gold_world`, R8б.9), `zz_ef_reference_strength_step`, `zz_ef_currency_trade_step`,
  `zz_ef_rate_policy_costs`, `zz_ef_mp_step`, `zz_ef_clr_step`, `zz_ef_nr_dep_step`, `zz_ef_consol_step`,
  `zz_ef_bond_ledger_step`, `zz_ef_cbfx_week_step` (клиринг, облигации, зона валюты, денежная политика).
- Модель вызывается: `zz_ef_cur_intro_before/after` из
  `common/scripted_effects/09_introduction_building_lvl.txt:34323/34463` (обёртка `introduction_new_currency`).
- Значения модели читают GUI и локализация: `gui/ld_economy_panel.gui`,
  `localization/<язык>/replace/ld_money_supply_replace_l_<язык>.yml`, `ld_cb_rate_panel_*`, `ld_monetary_policy_*`;
  `gui/ld_money_hook.gui` — единственный GUI-узел модели (виджет `zz_ef_money_hook`, скрытый, на
  `GetGlobalList('zz_ef_hook_countries')`).
- Металл ЦБ меняется только покупкой зданием ЦБ (`zz_ef_cb_metal_buy`): раздачи металла E&F из рынка в `gold_state_1`
  нет.
- Ручные операции E&F, меняющие счета мимо недельной записи (попадают в «прочее»/невязку `EFQ`):
  `global_monetary_reference_reset`, `transfer_gold_to_central_bank_metal_reserves`.

## Логи
- `EFW` — недельная строка страны: M0..M3, счета (игрок и страны с ВВП > 20 млн).
- `EFR` — расчёт по числам моста (`zz_ef_bridge_apply`): внешний поток, утечка, прочее; `EFO` — «прочее» карточек
  (`zz_ef_money_log_rest`).
- `EFG|…|WORLD` — мировая линия потоков (клиринг); `EFV|…|WORLD` — мировая линия металла.
- `EFT` — недельные покупки металла ЦБ/банков/населения (`zz_ef_metal_week_step`); `EFQ` — невязка металла ЦБ > 1000
  золота / 10000 серебра.
- `EFM` — события: `metal_start`, `cb_state_lost`, `cur_intro`; `EFA` — доп. доходы/расходы > 1000; `EFX` — валюта раз в
  месяц; `EFC` — выкуп валюты в кризис.
