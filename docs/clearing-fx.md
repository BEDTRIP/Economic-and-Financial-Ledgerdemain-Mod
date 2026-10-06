# Клиринг, форекс, резервы, торговля валютой
Мировой клиринг платежей с заграницей (каждую неделю чистый внешний поток страны проходит через «клиринговую палату»: плательщик платит
золотом/металлом по доверию к валюте и своей валютой, получатель забирает долю содержимого палаты). Форекс E&F (ИИ раз в год, игрок кнопками) меняет
валюту на металл и обратно в запасах ЦБ. Валютные запасы ЦБ показываются таблицей и диаграммой держателей. Сила валюты двигает торговлю.
E&F `trade_balance` отключён. Ключи `ld_*` — с префиксом `zz_ef_`.

## Файлы
- `common/scripted_effects/ld_clearing.txt` — генерат (`tools/regen_ef_clearing.py`): `zz_ef_clr_window_roll` (окно 7 дней, глобалки `zz_ef_clr_window`, `zz_ef_clr_in_acc`, `zz_ef_clr_out_acc`), `zz_ef_clr_step` (страна, недельный), `zz_ef_clr_head_find` (кто платит за нас: хозяин валютной зоны `zz_ef_cur_zone` / владелец рынка), `zz_ef_clr_pay`, `zz_ef_clr_receive`, `zz_ef_clr_put_own` (своя валюта в палату), `zz_ef_clr_take_all` (по 95 валютам, 1617 строк), `zz_ef_cbfx_week_step` (недельная дельта запасов каждой валюты `zz_ef_cbfx_d_<cur>`).
- `common/script_values/ld_clearing_values.txt` — доля металла плательщика `zz_ef_clr_metal_share` (0.75…1.25 → 100%…30%), золото за единицу денег `zz_ef_clr_gold_per_money` (+`_gpm_head`, `_gpm_own`), `zz_ef_clr_pot_value` (всё в палате в золоте, по валютам), `zz_ef_clr_pay_ratio_v`, `zz_ef_clr_ratio_v`, потоки `zz_ef_v_f_clr_*`, `zz_ef_bank_holds_<Bank>` (валюта страны у частных банков E&F, из `stockpiling_<cur>_company_<Bank>_fixe`), `zz_ef_cbfx_<cur>` (запас валюты ЦБ).
- `common/scripted_guis/ld_cbfx.txt` — `zz_ef_cbfx_update_sorted` (таблица валют ЦБ, список `zz_ef_cbfx_list`), `zz_ef_holders_update` (кто держит нашу валюту: `zz_ef_holds_pc`, `zz_ef_holders_list`, `zz_ef_bank_holders_list`).
- `common/script_values/ld_fx_reserves_values.txt` — `zz_ef_fx_reserves_metal` (чужая валюта в резервах ЦБ в золоте: `stockpiling_<cur>_state_1` × стоимость валюты).
- `common/scripted_effects/ld_stockpile_state_var_seed.txt` — смежный учётный файл.
- `common/script_values/ld_reserve_trade_values.txt` (генерат) — `zz_ef_rc_currency_value` (стоимость валюты, живое — читает клиринг), `zz_ef_fx_liab` (чужие запасы нашей валюты у держателей, живое), `zz_ef_v_rc_*` (поля лога `EFX`, всегда 0).
- `common/scripted_effects/ld_reference_strength.txt` — `zz_ef_currency_trade_step` (месяц: накладывает `zz_ef_currency_trade` по силе валюты), `zz_ef_reference_strength_step`.
- `common/static_modifiers/ld_currency_trade.txt` — `zz_ef_currency_trade` (импорт/экспорт ±10% при силе 1.25/0.75), плюс E&F `strong_currency`/`weak_currency` без торговых полей.
- `common/static_modifiers/ld_fx_holders_demand.txt` — экспортное преимущество от валюты за рубежом (см. `banks.md`).
- `common/modifier_type_definitions/ld_liquidity_currency_sell_orders.txt` — объявляет `state_sell_orders_liquidity_currency_add` (модификатора с ним больше нет).
- `common/production_methods/00_ef_market_liquidity.txt` — `pm_no_market_liquidity`, `pm_market_liquidity_currency` (вход `goods_input_liquidity_currency_add = 28` — бизнесы покупают услугу расчётов у банков), далее методы военных заказов (`pm_government_aid_*`).
- E&F, форекс и арбитраж:
  - `common/scripted_effects/00_on_action_main.txt`: `ai_buy_sell_currency` (:5687; по каждой валюте с `money_value_<cur> > 0`: `buy_<cur>_currency` если валюта не слабая, `sell_<cur>_currency` если запас > 1 000 000 и `purchase_cycle = 0`), вызов из `central_bank_ef_on_yearly_pulse_country` (:954), `monetary_systeme_transition`; арбитражи — см. поток.
  - `common/scripted_effects/01_economic_scripted_effects.txt`: `buy_<cur>_currency`/`sell_<cur>_currency` (:42720…, по эффекту на валюту; запись `gold_state_1`/`silver_state_1` и `stockpiling_<cur>_state_1` столицы ЦБ), `private_bank_arbitrage_gold_drain` (:91721), `private_bank_arbitrage_silver_drain` (:91979), `private_bank_gold_lose` (:106832), `trade_balance` (:41765).
  - `common/scripted_guis/00_economic_scripted_guis.txt`: `<cur>_buy_in_gold`/`<cur>_sell_in_gold` — кнопки игрока (окно в `gui/00_ef_deported_gui_1.gui`); `09_ef_other.txt:2190` `trade_balance_actualized`, `:5283` `trade_balance_0`.
  - `common/script_values/00_economic_scripted_value.txt:5924-6176` — `trade_balance_*` значения; `01_economic_currency_scripted_value.txt:287334…` — `trade_balance_in_gold*`.

## Поток / порядок
- Неделя (`zz_ef_money_model_step`, `ld_money_model.txt:101`): `zz_ef_fx_metal_update` (:114) → `zz_ef_cbfx_week_step` (:116) → … → `zz_ef_cb_hume_step` (:552) → `zz_ef_clr_step` (:705): взнос членов зоны глава-стране (`zz_ef_clr_sub_g`), у страны с ЦБ — окно, `zz_ef_clr_pay` при `zz_ef_f_clr_net < 0` (долг в золоте × `zz_ef_clr_pay_ratio_v`; металл ≤ металла ЦБ, остальное своей валютой `zz_ef_f_clr_cur_out`), `zz_ef_clr_receive` при `> 0` (доля палаты: металл + валюты, своя валюта погашается, чужая → запас ЦБ `zz_ef_f_clr_fx_in`); страна без ЦБ платит только валютой. Результаты в `zz_ef_f_hume`, `zz_ef_f_clr_*`. Затем `zz_ef_nr_dep_step` (:554).
- Месяц (`zz_ef_money_model_monthly_step`, `ld_money_model.txt:1027`): `zz_ef_currency_trade_step` (:1036).
- Год (`central_bank_ef_on_yearly_pulse_country`, `00_on_action_main.txt:919`, `on_actions/00_ef_on_action.txt:189`): для ИИ-владельца рынка с ЦБ `SS/BS/GS/NISO` — `ai_buy_sell_currency` (:954) и `monetary_systeme_transition`; сделка = `zz_ef_fx_deal_size` (2% M2 эмитента, `ld_money_model_values.txt:987`). Арбитраж биметаллизма (:1050-1170, до 1873, закон `law_bimetallism_standard`, перекос ≥ 0.05): металл ЦБ меняет золото на серебро (`gold_state_1`/`silver_state_1`), доля у случайного частного банка (`private_bank_arbitrage_*_drain` → `company_*_gold_stockpile_fix`), событие `00_ef_economic_event.95` игроку.
- Метал-сверка: `zz_ef_metal_reconcile` (`ld_metal_accounts.txt:149`) относит движение металла ЦБ, не покрытое нашими парами (форекс E&F, арбитраж, смена стандарта), в «oth» (лог `EFQ`).

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
| `gold_state_1`, `silver_state_1` (штат столицы ЦБ) | металл ЦБ | клиринг, форекс E&F, арбитраж, `ld_metal_accounts.txt` | вся модель металла |
| `stockpiling_<cur>_state_1` (штат ЦБ) | запас валюты `<cur>` в ЦБ, единицы | клиринг, `buy/sell_<cur>_currency`, кнопки игрока | `zz_ef_cbfx_<cur>`, `zz_ef_fx_reserves_metal` |
| `zz_ef_cbfx_d_<cur>`, `zz_ef_cbfx_p_<cur>` | дельта и прошлое значение запаса | `zz_ef_cbfx_week_step` | таблица ЦБ |
| `zz_ef_holds_pc`, список `zz_ef_holders_list` | сколько нашей валюты у держателя | `zz_ef_holders_update` | GUI |
| `trade_balance_in_gold_fixe` | счётчик торгового баланса E&F (держится 0) | `trade_balance`, кнопка `trade_balance_actualized` | `central_bank_reserves_*` E&F |
| `purchase_cycle` | признак покупки за цикл ИИ | `buy_<cur>_currency` | `ai_buy_sell_currency` |

## Вызовы и связи
- `zz_ef_clr_gold_per_money` и `zz_ef_rc_currency_value` читают клиринг, таблицы облигаций (`ld_bond_tables.txt`), модель денег.
- `zz_ef_fx_liab`/`zz_ef_fx_liab_all` — вклады (`banks.md`).
- Интерфейс: `gui/ld_economy_panel.gui` (кнопки `zz_ef_cbfx_update_sorted`, `zz_ef_holders_update` :3011-3012, диаграммы :9832, :9874; кнопка `trade_balance_actualized` :2802, :3016); `gui/00_ef_deported_gui_1.gui` — окно покупки/продажи валют и облигаций E&F.
- Модификатор `zz_ef_currency_trade` — на стране (импорт/экспорт).

## Логи
- `EFX|` — месячная строка по валютам/стандарту (`ld_money_model.txt:1058`).
- `EFR|` — недельное состояние внешних счетов страны (клиринг, вклады: `ld_money_model.txt:565`).
- `EFQ` — «oth» сверки металла ЦБ (`ld_metal_accounts.txt`).
- Файлы `ld_clearing.txt`, `ld_cbfx.txt` своих `debug_log` не имеют.
