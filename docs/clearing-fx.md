# Клиринг, форекс, резервы, торговля валютой
Мировой клиринг платежей с заграницей (каждую неделю чистый внешний поток страны проходит через «клиринговую палату»: плательщик платит
золотом/металлом по доверию к валюте и своей валютой, получатель забирает долю содержимого палаты). Форекс E&F (ИИ-сделки и окно обмена игрока) — в
`_archive/` (`ef_ai_forex/`, `ef_forex_windows/`); заявки игрока — биржей (R8б). Валютные запасы ЦБ показываются таблицей и диаграммой держателей. Сила валюты двигает торговлю.
E&F `trade_balance` отключён. Ключи `ld_*` — с префиксом `zz_ef_`.

## Файлы
- `common/scripted_effects/ld_clearing.txt` — генерат (`tools/regen_ef_clearing.py`): `zz_ef_clr_window_roll` (окно 7 дней, глобалки `zz_ef_clr_window`, `zz_ef_clr_in_acc`, `zz_ef_clr_out_acc`), `zz_ef_clr_step` (страна, недельный), `zz_ef_clr_head_find` (кто платит за нас: хозяин валютной зоны `zz_ef_cur_zone` / владелец рынка), `zz_ef_clr_pay`, `zz_ef_clr_receive`, `zz_ef_clr_put_own` (своя валюта в палату), `zz_ef_clr_take_all` (по 95 валютам, 1617 строк), `zz_ef_cbfx_week_step` (недельная дельта запасов каждой валюты `zz_ef_cbfx_d_<cur>`).
- `common/script_values/ld_clearing_values.txt` — доля металла плательщика `zz_ef_clr_metal_share` (0.75…1.25 → 100%…30%), золото за единицу денег `zz_ef_clr_gold_per_money` (+`_gpm_head`, `_gpm_own`), `zz_ef_clr_pot_value` (всё в палате в золоте, по валютам), `zz_ef_clr_pay_ratio_v`, `zz_ef_clr_ratio_v`, потоки `zz_ef_v_f_clr_*`, `zz_ef_bank_holds_<Bank>` (валюта страны у частных банков E&F, из `stockpiling_<cur>_company_<Bank>_fixe`), `zz_ef_cbfx_<cur>` (запас валюты ЦБ).
- `common/scripted_guis/ld_cbfx.txt` — `zz_ef_cbfx_update_sorted` (таблица валют ЦБ, список `zz_ef_cbfx_list`), `zz_ef_holders_update` (какие ЦБ держат нашу валюту: `zz_ef_holds_pc`, `zz_ef_holders_list`).
- `common/script_values/ld_fx_reserves_values.txt` — `zz_ef_fx_reserves_metal` (чужая валюта в резервах ЦБ в золоте: `stockpiling_<cur>_state_1` × стоимость валюты).
- `common/scripted_effects/ld_stockpile_state_var_seed.txt` — смежный учётный файл.
- `common/script_values/ld_reserve_trade_values.txt` (генерат) — `zz_ef_fx_liab` (чужие запасы нашей валюты у держателей, живое).
- `common/scripted_effects/ld_reference_strength.txt` — `zz_ef_currency_trade_step` (месяц: накладывает `zz_ef_currency_trade` по силе валюты), `zz_ef_reference_strength_step`.
- `common/static_modifiers/ld_currency_trade.txt` — `zz_ef_currency_trade` (импорт / экспорт от реального перекоса курса к эталону, ±50 % потолок, R3.4), плюс E&F `strong_currency`/`weak_currency` без торговых полей.
- `common/static_modifiers/ld_fx_holders_demand.txt` — экспортное преимущество от валюты за рубежом (см. `banks.md`).
- `common/modifier_type_definitions/ld_liquidity_currency_sell_orders.txt` — объявляет `state_sell_orders_liquidity_currency_add` (модификатора с ним больше нет).
- `common/production_methods/00_ef_market_liquidity.txt` — `pm_no_market_liquidity` (по закону «без денежной системы», Д.R8а.2), `pm_market_liquidity_currency` (вход `goods_input_liquidity_currency_add = 28` — бизнесы покупают услугу расчётов у банков), далее методы военных заказов (`pm_government_aid_*`).
- E&F, форекс:
  - ИИ-форекс E&F (`ai_buy_sell_currency` → `buy_/sell_<cur>_currency`) — в `_archive/ef_ai_forex/` (R2, Д.R2.2; форекс ЦБ сделками — R8); в `central_bank_ef_on_yearly_pulse_country` остался `monetary_systeme_transition`; арбитражи — см. поток.
  - `common/scripted_effects/01_economic_scripted_effects.txt`: `sell_<cur>_currency_crisis` (кризисная продажа, из `all_currency_resold`), `trade_balance` (:11204).
  - Окно обмена валют игрока (вкладка рынка «global», кнопки `<cur>_buy_in_gold` / `<cur>_sell_in_gold`, проводка `zz_ef_fxb_*`) — в `_archive/ef_forex_windows/` (Д.R8а, п. 8).
  - `common/scripted_guis/09_ef_other.txt`: `trade_balance_actualized`.
  - `common/script_values/00_economic_scripted_value.txt:5661-5913` — `trade_balance_*` значения; `01_economic_currency_scripted_value.txt:285996…` — `trade_balance_in_gold*`.

## Поток / порядок
- Неделя (`zz_ef_money_model_step`, `ld_money_model.txt:101`): `zz_ef_fx_metal_update` (:114) → `zz_ef_cbfx_week_step` (только у игроков) → … → `zz_ef_cb_hume_step` (:527) → `zz_ef_clr_step` (:680): взнос членов зоны глава-стране (`zz_ef_clr_sub_g`), у страны с ЦБ — окно, `zz_ef_clr_pay` при `zz_ef_f_clr_net < 0` (долг в золоте × `zz_ef_clr_pay_ratio_v`; металл ≤ металла ЦБ, остальное своей валютой `zz_ef_f_clr_cur_out`), `zz_ef_clr_receive` при `> 0` (доля палаты: металл + валюты, своя валюта погашается, чужая → запас ЦБ `zz_ef_f_clr_fx_in`); страна без ЦБ платит только валютой. Результаты в `zz_ef_f_hume`, `zz_ef_f_clr_*`. Затем `zz_ef_nr_dep_step` (:529).
- Месяц (`zz_ef_money_model_monthly_step`, `ld_money_model.txt:1002`): `zz_ef_currency_trade_step` (:1011).
- Год (`central_bank_ef_on_yearly_pulse_country`, `on_actions/00_ef_on_action.txt:155`): для ИИ-владельца рынка с ЦБ `SS/BS/GS/NISO` — `monetary_systeme_transition`. Арбитраж биметаллизма (до 1873; перекос `misalignment_rate_*_drain` = 0, не срабатывал) — в `_archive/ef_bimetallic_arbitrage/` (R2, шаг 3).
- Метал-сверка: `zz_ef_metal_reconcile` (`ld_metal_accounts.txt:149`) относит движение металла ЦБ, не покрытое нашими парами (смена стандарта), в «oth» (лог `EFQ`).

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `zz_ef_f_ext_net` | чистый внешний поток недели, деньги | `zz_ef_cb_hume_step` | `zz_ef_clr_step` |
| `zz_ef_f_clr_net`, `zz_ef_f_clr_sent`, `zz_ef_f_clr_sub` | сумма к расчёту, отправлено главе, принято от членов | `zz_ef_clr_step` | значения `zz_ef_v_f_clr_*` |
| `zz_ef_clr_head` | глава расчётов (overlord / владелец рынка) | `zz_ef_clr_head_find` | `zz_ef_clr_step` |
| `zz_ef_t_gpm` | временная: `zz_ef_clr_gold_per_money`, посчитанное один раз за `zz_ef_clr_step` (и за `zz_ef_world_acc` после блока окна); значение имеет смысл только внутри вызова | `zz_ef_clr_step`, `zz_ef_world_acc` | `zz_ef_clr_step`, `_pay`, `_receive`, `zz_ef_world_acc` |
| `zz_ef_clr_sub_g` | золото членов к расчёту | члены | `zz_ef_clr_step` главы |
| `zz_ef_f_hume` | металл ЦБ за неделю (native, +вход/−выход) | `zz_ef_clr_pay/receive` | `zz_ef_metal_reconcile` |
| `zz_ef_f_clr_cur_out`, `_fx_in`, `_own_back` | потоки валюты | `zz_ef_clr_*` | карточка платёжного баланса, лог |
| глобалки `zz_ef_clr_window`, `zz_ef_clr_in_acc`, `zz_ef_clr_out_acc` | окно палаты, требования и платежи (золото) | `zz_ef_clr_window_roll`, `_pay`, `_receive` | `zz_ef_clr_pay_ratio_v` |
| `gold_state_1`, `silver_state_1` (штат столицы ЦБ) | металл ЦБ | клиринг, кнопки форекса E&F, `ld_metal_accounts.txt` | вся модель металла |
| `stockpiling_<cur>_state_1` (штат ЦБ) | запас валюты `<cur>` в ЦБ, единицы | клиринг, кнопки игрока, `sell_<cur>_currency_crisis` | `zz_ef_cbfx_<cur>`, `zz_ef_fx_reserves_metal` |
| `zz_ef_cbfx_d_<cur>`, `zz_ef_cbfx_p_<cur>` | дельта и прошлое значение запаса | `zz_ef_cbfx_week_step` | таблица ЦБ |
| `zz_ef_holds_pc`, список `zz_ef_holders_list` | сколько нашей валюты у держателя | `zz_ef_holders_update` | GUI |
| `trade_balance_in_gold_fixe` | счётчик торгового баланса E&F (держится 0) | `trade_balance`, кнопка `trade_balance_actualized` | `central_bank_reserves_*` E&F |

## Вызовы и связи
- `zz_ef_clr_gold_per_money` (золото на единицу денег: своя — `zz_ef_clr_gpm_own` = `zz_ef_value_to_parity`, Д.R8а.4; без денежной системы — хозяина рынка) читают клиринг, таблицы облигаций (`ld_bond_tables.txt`), модель денег.
- `zz_ef_fx_liab`/`zz_ef_fx_liab_all` — вклады (`banks.md`).
- Интерфейс: `gui/ld_economy_panel.gui` (кнопки `zz_ef_cbfx_update_sorted`, `zz_ef_holders_update` :2971-3012, диаграммы :9754, :9796; кнопка `trade_balance_actualized` :2768, :2976); `gui/00_ef_deported_gui_1.gui` — окно покупки/продажи валют и облигаций E&F.
- Модификатор `zz_ef_currency_trade` — на стране (импорт/экспорт).

## Логи
- `EFX|` — месячная строка по валютам/стандарту (`ld_money_model.txt:1033`).
- `EFR|` — недельное состояние внешних счетов страны (клиринг, вклады: `ld_money_model.txt:540`).
- `EFQ` — «oth» сверки металла ЦБ (`ld_metal_accounts.txt`).
- Файлы `ld_clearing.txt`, `ld_cbfx.txt` своих `debug_log` не имеют.
