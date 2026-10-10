# Клиринг, форекс, резервы, торговля валютой
**Смысл.** Расчёты страны с заграницей за неделю: позиция страны (сальдо в золоте) → в конце недели позиции сводятся
внутри групп металла, остаток — между группами; каждый плательщик платит каждому получателю набором: долей своей валютой
(требование получателя на плательщика), остальное — по стандарту получателя (металл, его валюта из резервов плательщика,
долг недели). Палаты и главы клиринга нет. **Понятия:** [[Клиринг]], [[Зачёт по группам металла]],
[[Торговля с заграницей]], [[Сила валюты]], [[Вклады нерезидентов]], [[Биржа]], [[Денежная власть]]. **Решения:**
Д.R0.8.4, Д.R3.4, Д.R8в.1, Д.R8в.2, Д.R8в.4, Д.R8в.11 (`решения.md`).

Форекс E&F (ИИ-сделки и окно обмена игрока) — в `_archive/` (`ef_ai_forex/`, `ef_forex_windows/`); заявки игрока —
биржей (R8б). Валютные запасы ЦБ показываются таблицей и диаграммой держателей. Сила валюты двигает торговлю. E&F
`trade_balance` отключён. Ключи `ld_*` — с префиксом `zz_ef_`. Прежняя палата клиринга (общая касса, глава, окно с
множителями) — `_archive/ld_clearing_house/`.

## Файлы
- `common/scripted_effects/ld_clearing.txt` (рукописный): `zz_ef_clr_step` (страна, недельный: позиция
  `var:zz_ef_clr_pos` в золоте = поток × `zz_ef_clr_gpm_own`, доля своей валютой `var:zz_ef_clr_n`, группа
  `zz_ef_clr_group_set`, в список `global_list:zz_ef_clr_list`; без своих денег — мировая строка
  `global_var:zz_ef_clr_wl`), `zz_ef_clr_settle` (мир, конец недели: группы — первая страна группы держит её суммы
  `var:zz_ef_clr_gp` / `_gm` и список получателей `zz_ef_clr_grl`; доли зачёта `zz_ef_clr_kp` / `_kr`; остатки мира
  `global_var:zz_ef_clr_rp` / `_rm`, доли `_xp` / `_xr`; пары внутри группы, затем между группами за вычетом комиссии
  биржи плательщика `zz_ef_xch_fee_v`), `zz_ef_clr_pair` (платёж-набор), `zz_ef_clr_give_claim` (требование получателя
  на плательщика: `zz_ef_rq_add`, держатель cb / bk), `zz_ef_clr_give_metal` / `zz_ef_clr_metal_move` (металл ЦБ — в
  столичном штате ЦБ, металл своего стандарта; без ЦБ — металл банков `var:zz_ef_bankm_gold` / `_silver`),
  `zz_ef_clr_give_back` (валюта получателя из резервов плательщика возвращается эмитенту), `zz_ef_clr_need_add` (долг
  недели в валюте получателя — карта `zz_ef_clr_need`), `zz_ef_clr_post_needs` (на шаге биржи плательщика — заявка на
  покупку этой валюты по верхнему шагу, `zz_ef_xch_order_put`), `zz_ef_clr_take_acc` / `zz_ef_clr_take_hume` (итоги
  расчёта — в недельные `zz_ef_f_clr_*`, металл ЦБ — до сверки металла), `zz_ef_cbfx_week_step` (недельное изменение
  чужих денег ЦБ по эмитентам — карты `zz_ef_cbfx_d`, `zz_ef_cbfx_p`).
- `common/script_values/ld_clearing_values.txt` (рукописный) — доля металла `zz_ef_clr_metal_share` (сила 0,75…1,25 →
  100 %…30 %, эталон — 15 %), доля своей валютой `zz_ef_clr_own_share` = 1 − она, золото за единицу денег
  `zz_ef_clr_gold_per_money` (своё, без своих денег — среднее мира) и `zz_ef_clr_gpm_own`, металл к оплате
  `zz_ef_clr_metal_av_g`, итоги недели `zz_ef_v_f_clr_*` (карточка заграницы), мировые суммы `zz_ef_clr_w_*_v` (лог
  `EFC`), `zz_ef_cbfx_g_v` (порядок строк таблицы).
- `common/scripted_triggers/ld_clearing_triggers.txt` — `zz_ef_clr_cb_ok` (денежная власть — ЦБ: ЦБ и столичный штат ЦБ;
  иначе — банки), `zz_ef_clr_wants_metal` (металлический стандарт, не обменный).
- `common/scripted_guis/ld_cbfx.txt` — `zz_ef_cbfx_update_sorted` (таблица чужих денег ЦБ по эмитентам: список
  `zz_ef_cbfx_list`, строка — переменные эмитента `zz_ef_cbfx_u/_g/_mn/_dd`), `zz_ef_holders_update` (какие ЦБ держат
  наши деньги: `zz_ef_holds_pc`, `zz_ef_holders_list`).
- `common/script_values/ld_fx_reserves_values.txt` — `zz_ef_fx_reserves_metal` (чужие деньги в резервах ЦБ, которые идут
  в покрытие, в золоте: `var:zz_ef_fx_res_gold`, `zz_ef_fx_metal_update`).
- `common/scripted_effects/ld_stockpile_state_var_seed.txt` — смежный учётный файл.
- `common/scripted_effects/ld_reference_strength.txt` — `zz_ef_currency_trade_step` (месяц: накладывает
  `zz_ef_currency_trade` по силе валюты), `zz_ef_reference_strength_step`.
- `common/static_modifiers/ld_currency_trade.txt` — `zz_ef_currency_trade` (импорт / экспорт от реального перекоса курса
  к эталону, ±50 % потолок, R3.4), плюс E&F `strong_currency`/`weak_currency` без торговых полей.
- `common/static_modifiers/ld_fx_holders_demand.txt` — экспортное преимущество от валюты за рубежом (см. `banks.md`).
- `common/modifier_type_definitions/ld_liquidity_currency_sell_orders.txt` — объявляет
  `state_sell_orders_liquidity_currency_add` (модификатора с ним больше нет).
- `common/production_methods/00_ef_market_liquidity.txt` — `pm_no_market_liquidity` (по закону «без денежной системы»,
  Д.R8а.2), `pm_market_liquidity_currency` (вход `goods_input_liquidity_currency_add = 28` — бизнесы покупают услугу
  расчётов у банков), далее методы военных заказов (`pm_government_aid_*`).
- E&F, форекс:
  - ИИ-форекс E&F (`ai_buy_sell_currency` → `buy_/sell_<cur>_currency`) — в `_archive/ef_ai_forex/` (R2, Д.R2.2; форекс
    ЦБ сделками — R8); в `central_bank_ef_on_yearly_pulse_country` остался `monetary_systeme_transition`; арбитражи —
    см. поток.
  - `common/scripted_effects/01_economic_scripted_effects.txt`: `trade_balance` (:11204).
  - Окно обмена валют игрока (вкладка рынка «global», кнопки `<cur>_buy_in_gold` / `<cur>_sell_in_gold`, проводка
    `zz_ef_fxb_*`) — в `_archive/ef_forex_windows/` (Д.R8а, п. 8).
  - `common/scripted_guis/09_ef_other.txt`: `trade_balance_actualized`.
  - `common/script_values/00_economic_scripted_value.txt:5661-5913` — `trade_balance_*` значения;
    `01_economic_currency_scripted_value.txt:285996…` — `trade_balance_in_gold*`.

## Поток / порядок
- Неделя страны (`zz_ef_money_model_step`): `zz_ef_clr_take_hume` перед `zz_ef_metal_week_step` (металл ЦБ, сдвинутый
  расчётом, — `var:zz_ef_f_hume`, его сверка видит), затем `zz_ef_cb_hume_step` → `zz_ef_clr_step`: итоги прошлого
  расчёта (`zz_ef_clr_take_acc`) и позиция недели. В шаге биржи (`zz_ef_xch_step`) — `zz_ef_clr_post_needs`.
- Конец недели планировщика (`zz_ef_world_week_close`, `ld_scheduler.txt`): `zz_ef_clr_settle` — все позиции недели.
  Сначала позиции переводятся на масштабы мировых пулов этой же недели (Ч4): торговля и комиссии рынков (`zz_ef_wtr_kr`
  / `_kp`) и дивиденды (`zz_ef_wdv_r`) — шаги стран брали прошлое окно (`global_var:zz_ef_wtr_kr_used` и т. п.),
  поправка — части позиции `var:zz_ef_clr_ce` (экспорт + комиссии), `_ci` (импорт), `_ca` (владение за рубежом) ×
  разница масштабов. Что пул отнимает у экспортёров (экспорт + комиссии − импорт мира, «рынок-посредник») — строка `mid`
  лога `EFC` (`global_var:zz_ef_wld_mid`). Внутри группы металла (золото 1, серебро 2, фиат 4, биметалл — 100 + 10 ×
  законное соотношение; обменный — группа своего металла, внешневалютный — якоря) сводится min(получить, заплатить):
  плательщик i платит получателю j группы
  |pos_i| × kp × pos_j / gp. Остатки групп — между группами, насколько остатки мира совпадают: d_i × xp × res_j / rp,
  минус комиссия биржи плательщика (не доходит до получателя, `f_clr_fee`). Не совпавшее миром — не сведено
  (`f_clr_unm`: + не получено, − не заплачено).
- Платёж-набор (Д.R8в.11): доля `zz_ef_clr_n` — требованием получателя на плательщика (его деньги во вкладах в банках
  плательщика, `vklady` — `banks.md`); остаток металлическому стандарту — металлом из резервов плательщика (по мировой
  цене в металл получателя); затем валютой получателя из резервов плательщика (требование гасится у эмитента — «своя
  вернулась»); остаток — долг недели: тоже требование на плательщика, и плательщик на следующем шаге выставляет заявку
  на покупку валюты получателя (по верхнему шагу стакана своей биржи). Ненужные требования получатель продаёт на бирже
  (R8б).
- Месяц (`zz_ef_money_model_monthly_step`, `ld_money_model.txt:1002`): `zz_ef_currency_trade_step` (:1011).
- Год (`central_bank_ef_on_yearly_pulse_country`, `on_actions/00_ef_on_action.txt:155`): для ИИ-владельца рынка с ЦБ
  `SS/BS/GS/NISO` — `monetary_systeme_transition`. Арбитраж биметаллизма (до 1873; перекос `misalignment_rate_*_drain` =
  0, не срабатывал) — в `_archive/ef_bimetallic_arbitrage/` (R2, шаг 3).
- Метал-сверка: `zz_ef_metal_reconcile` (`ld_metal_accounts.txt:149`) относит движение металла ЦБ, не покрытое нашими
  парами (смена стандарта), в «oth» (лог `EFQ`).

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `zz_ef_f_ext_net` | чистый внешний поток недели, деньги | `zz_ef_cb_hume_step` | `zz_ef_clr_step` |
| `zz_ef_f_clr_net` | поток недели к расчёту, деньги | `zz_ef_clr_step` | позиция |
| `zz_ef_clr_pos`, `zz_ef_clr_gpm`, `zz_ef_clr_n`, `zz_ef_clr_gc` (страна) | позиция недели в золоте (+ получить / − заплатить), золото за единицу денег, доля своей валютой, группа металла | `zz_ef_clr_step` | `zz_ef_clr_settle` (позиция снимается после расчёта) |
| `zz_ef_clr_rep`, `zz_ef_clr_gp`, `_gm`, `_gn`, `_kp`, `_kr`, список `zz_ef_clr_grl` | группа страны и суммы группы (на первой стране группы) | `zz_ef_clr_settle` | он же |
| глобальные `zz_ef_clr_list`, `zz_ef_clr_reps`, `zz_ef_clr_rr`, `zz_ef_clr_rp`, `_rm`, `_xm`, `_xp`, `_xr` | участники недели, группы, получатели остатков, остатки мира и доли их сведения | `zz_ef_clr_step`, `zz_ef_clr_settle` | `zz_ef_clr_settle` |
| `zz_ef_clr_a_<n>` → `zz_ef_f_clr_<n>` (n: `cur_out`, `fx_in`, `own_back`, `fx_out`, `metal_g`, `paid`, `got`, `debt`, `unm`, `fee`) | итоги расчёта с прошлого шага: наша валюта за границу (ед.), чужая получена (золото), своя вернулась (ед.), чужая отдана (золото), металл (золото, ±), заплачено, получено, долг недели, не сведено миром (±), комиссия (золото) | `zz_ef_clr_settle` → `zz_ef_clr_take_acc` | `zz_ef_v_f_clr_*`, карточка заграницы, лог `EFX` |
| `zz_ef_clr_a_hume` → `zz_ef_f_hume` | металл ЦБ, сдвинутый расчётом (свой металл стандарта, + вход / − выход) | `zz_ef_clr_metal_move` → `zz_ef_clr_take_hume` | `zz_ef_metal_reconcile` |
| карта `zz_ef_clr_need` (плательщик) | долг недели в валюте получателя, ед. | `zz_ef_clr_need_add` | `zz_ef_clr_post_needs` (заявка на бирже, карта очищается) |
| `global_var:zz_ef_clr_wl` | мировая строка: поток стран без своих денег за неделю, золото | `zz_ef_clr_step` | лог `EFC` (обнуляется в расчёте) |
| `gold_state_1`, `silver_state_1` (штат столицы ЦБ) | металл ЦБ | клиринг, `ld_metal_accounts.txt` | вся модель металла |
| карты `zz_ef_rq_cb_m`, `zz_ef_rq_bk_m` (страна) | чужие деньги ЦБ / банков по эмитентам, в их деньгах (`claims.md`) | `zz_ef_clr_give_claim`, `zz_ef_clr_give_back`, `zz_ef_rq_interest_step`, `zz_ef_rq_crisis_resell`, биржа | таблица ЦБ, `zz_ef_fx_metal_update` |
| `stockpiling_<cur>_state_1` (штат ЦБ) | E&F: собственный запас валюты ЦБ (невыпущенные деньги); чужих денег здесь больше нет | история и ввод валют E&F | значения E&F |
| карты `zz_ef_cbfx_d`, `zz_ef_cbfx_p` (игрок) | изменение за неделю и прошлое значение по эмитентам | `zz_ef_cbfx_week_step` | таблица ЦБ |
| `zz_ef_holds_pc`, список `zz_ef_holders_list` | сколько нашей валюты у держателя | `zz_ef_holders_update` | GUI |
| `trade_balance_in_gold_fixe` | счётчик торгового баланса E&F (держится 0) | `trade_balance`, кнопка `trade_balance_actualized` | `central_bank_reserves_*` E&F |

## Вызовы и связи
- `zz_ef_clr_gold_per_money` (золото на единицу денег: своя — `zz_ef_clr_gpm_own` = `zz_ef_value_to_parity`, Д.R8а.4;
  без денежной системы — среднее мира по ВВП `global_var:zz_ef_wld_gpm_avg`) читают клиринг, таблицы облигаций
  (`ld_bond_tables.txt`), модель денег.
- `zz_ef_fx_liab_all` = `zz_ef_nr_dep_v` — наши деньги за границей (`banks.md`).
- Интерфейс: `gui/ld_economy_panel.gui` (кнопки `zz_ef_cbfx_update_sorted`, `zz_ef_holders_update` :2971-3012, диаграммы
  :9754, :9796; кнопка `trade_balance_actualized` :2768, :2976); `gui/00_ef_deported_gui_1.gui` — окно покупки/продажи
  валют и облигаций E&F.
- Модификатор `zz_ef_currency_trade` — на стране (преимущество экспорта / импорта её штатов): у всякой страны со своими
  деньгами (`zz_ef_has_currency_value`), кроме эталона, — и у члена чужого рынка.

## Логи
- `EFX|` — месячная строка по валютам/стандарту (`ld_money_model.txt:1033`).
- `EFR|` — недельное состояние внешних счетов страны (клиринг, вклады: `ld_money_model.txt:540`).
- `EFQ` — «oth» сверки металла ЦБ (`ld_metal_accounts.txt`).
- `EFC|дата|WORLD|n|groups|grp|x|fee|unpaid|unrec|metal|debt|wl|rp|rm` — расчёт недели (`zz_ef_clr_settle`): участников,
  групп; сведено внутри групп и между группами, комиссия, не заплачено и не получено (мир не совпал), металлом, долгом
  недели; мировая строка; остатки групп к получению / к оплате (золото).
