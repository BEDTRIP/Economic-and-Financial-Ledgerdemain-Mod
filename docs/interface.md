# Интерфейс (панели, окна, мост GUI → скрипт, локализация)
Всё, что игрок видит и нажимает: ванильные панели, переписанные E&F (бюджет, рынок, страна, штат, топбар, компании),
вкладки валют/запасов/ЦБ, журнальные виджеты, окно резервов. Кнопки зовут скрипт через scripted_gui; данные идут
в GUI через `GetCustom`/`ScriptValue`/`GetGlobalList`. Игра читает GUI один раз при загрузке — активной логики нет,
считает скрипт (другие подсистемы).

## Файлы
GUI-тип регистрирует первый файл по имени (ASCII, по всем модам; при равных — ближе к корню `gui/`); дубль типа мёртв.
Мод-файл с путём ванильного заменяет его целиком. Подкаталог мода проигрывает корню мода, но выигрывает у ванили
с тем же именем (так «потерянные» типы в `maj/*` ломали ваниль).

### Заменяют ванильный файл по пути (копия ванили + вставки E&F)
- `gui/budget_panel.gui` — `budget_panel` (2186 строк); вкладки вставляют типы `budget_panel_economy_panel_content` (:1497),
  `budget_panel_financial_panel_content` (:1522); `@money!` вместо символа валюты.
- `gui/market_panel.gui` — `market_panel`; вкладка «global» (`'msa'`) с `market_global_panel_content` (:949), кнопки
  `market_gui_market_currency_list` / `market_gui_market_financial_product_list` (:52, :1212-1403).
- `gui/states_panel.gui` — `states_panel`; `state_panel_currency_panel_content` (:1459).
- `gui/country_panel.gui` — `country_panel`; `country_panel_currency_panel_content` (:968).
- `gui/topbar.gui` — `topbar`; `currency_symbol_top_bar` (:540), прогрессбары `white_/gold_progressbar_horizontal_law` (:576, :591).
- `gui/companies_panel.gui` — ванильная + `ef_company_type_row` / `ef_established_company_row`, флаг `ef_companies_compact`
  (сжатый список непостроенных компаний).
- `gui/construction_panel.gui` — заглушка (3 строки, комментарий): не даёт загрузиться ванильному; типы стройки — в PSC-файле.
- `gui/texticons.gui` (309 текстиконок) — копия ванильного; 30 имён иконок повторены в `gui/00_ef_texticons.gui` (249).

### Файлы E&F
- `gui/00_ef_deported_gui_1.gui` (16 тыс. строк) — 3 типа: `market_global_panel_content` (:37, сравнение страны игрока и
  владельца рынка; покупка облигаций владельца рынка), `country_panel_currency_panel_content` (:6988),
  `state_panel_currency_panel_content` (:7111). Две пустые `types market_states_panel`-обёртки. Обмен валют по 95 валютам —
  в `_archive/ef_forex_windows/`.
- `gui/00_ef_deported_gui_2.gui` (11906 строк) — 205 типов: 191 `ef_bp_*_piechart` (круговые диаграммы запасов/денег по
  валютам; данные из `GetGlobalList('..._variable_list_ordered_N')`), `currency_symbol_top_bar` (один текстбокс `currency_symbol`
  символов), `ef_economy_N_formwork`/`ef_financial_N_formwork` (:9289-10680), `vo_plotline_minting` (:10984).
- `gui/00_ef_texticons.gui` — иконки текста E&F. `gui/00_MPM_building_details_panel.gui` — MPM: `condensed_building_information*`.
- `gui/scripted_widgets/00_ef_custom_widgets.gui` — виджеты журнала: `widget_je_ef_efcc_situation` (используется
  `common/journal_entries/00_ef_divers_je.txt`), кнопки `speculative_share_N_button`.
- `gui/scripted_widgets/PSC_scripted_widgets.txt` — `gui/PSC_construction_expense_widget.gui`.
- `gui/ef_dev_and_custom_windows/ef_custom_windows.gui` (2835 строк) — одно окно `default_popup` `gold_reserve_window` (резервы металла);
  открывается `ExecuteConsoleCommand('gui.createwidget …')` + `GetVariableSystem.Toggle('gold_reserve_window')`.
- `gui/ef_dev_and_custom_windows/maj/Essential/*.gui` (5) — `building_browser_panel`, `building_details_panel` (в корне мода одноимённого
  нет: подменяет ванильный, `00_MPM_building_details_panel.gui` объявляет только 3 типа из 50), `goods_panel`, `goods_state_panel`,
  `production_methods` — подмены ванильных по имени.
- `gui/ef_dev_and_custom_windows/maj/NonEssential/*.gui` (13) — копии ванильных (`map_list_panel`, `outliner_pinnable_types`,
  `graph_tooltips`, …); устаревшие копии без правок E&F (`map_markers`, `custom_tooltip`, `military_formation_panel`, `popups`,
  `right_click_menu`, `frontend/shared/lists.gui`) — в `_archive/ef_outdated_vanilla_gui/`, грузятся ванильные 1.13.

### Файлы проекта (`ld_*`, переопределяют типы E&F; грузятся раньше или вместо оригинала)
- `gui/ld_economy_panel.gui` (генерат. `regen_ef_economy_panel_gui.py`) — `budget_panel_economy_panel_content` (:10,
  оригинал из `00_ef_deported_gui_1.gui` удалён), торговый баланс в модели денег,
  `zz_ef_holders_piechart`, `vo_plotline_minting` (вызов :4143).
- `gui/ld_cb_rate_panel.gui` (генерат. `regen_ef_cb_rate_gui.py`) — `budget_panel_financial_panel_content` (:10): ключевая ставка,
  ЦБ, облигации, таблицы держателей (`zz_ef_bt_in_list`/`zz_ef_bt_out_list`), `mp_row` политики.
- `gui/ld_currency_symbol_fix.gui` — единственное определение `currency_symbol_country_panel` (один текстбокс
  `GetCustom('currency_symbol')`). Используется 5 раз в `00_ef_deported_gui_1.gui:87912…`.
- `gui/ld_national_capacity_chart.gui` — единственное определение `ef_bp_national_capacity_piechart` (используется
  `ld_economy_panel.gui:8273`); ряд в металле стандарта, доли — в золотом эквиваленте.
- `gui/ld_money_hook.gui` — мост «бюджет → скрипт» (см. ниже); регистрация `gui/scripted_widgets/ld_money_hook.txt`.
- `gui/scripted_widgets/ld_pb_fso_widgets.gui` — журнальные виджеты `zz_pb_ef_fso_bubble_widget`, `zz_pb_ef_fso_overcap_widget`,
  `zz_pb_ef_fso_hide_bars_widget` (подключены `common/journal_entries/00_ef_financial_center_je.txt:187-202`).

### PSC
- `gui/PSC_construction_panel.gui` (`construction_panel*`, `ship_construction_*`), `gui/PSC_states_panel_buildings.gui`
  (`buildings_list*`), `gui/shared/PSC_construction_spending_options.gui` (`construction_frame_coin`, `set_level_bar_construction*`),
  `gui/PSC_construction_expense_widget.gui` (скрытый виджет: `psc_test_show` → `psc_save_real_construction_cost`),
  `gui/PSC_goods_texticons.gui` (4 иконки строительных товаров).

### Скриптовые GUI / кнопки / прогресс-бары / понятия
- `common/scripted_guis/00_economic_scripted_guis.txt` — девальвация/ревальвация
  (`devaluation_*`, `revaluation_*`, `set_*_rate`), `is_ai`/`not_is_ai`, законы стандартов.
- `common/scripted_guis/00_financial_scripted_guis.txt` — облигации, кредит ЦБ, `speculative_share_N_button` (sgui),
  `transfert_currency_to_investement_pool_*`, `global_player_help_*`.
- `common/scripted_guis/09_ef_other.txt` — `EF_room_gui_N`/`EF_current_room_gui_N` (100+100; панель `gold_reserve_window`),
  `*_list_gerenation_ordered` (2 шт.), `gold_gui_N`/`silver_gui_N`, `gdp_sort_by_country_gdp`, `si_sort_by_country_indice`.
- `common/scripted_guis/PSC_construction_sguis.txt` (9) — `psc_button_*_sgui`, `psc_save_real_construction_cost`, `psc_test_show`.
- `common/scripted_guis/ld_*.txt` — `ld_money_hook` (приёмник моста), `ld_cb_rate_buttons` (кнопки ставки), `ld_monetary_policy_buttons`
  (девальвация/ревальвация как инструмент ЦБ), `ld_bond_tables` (заполнение таблиц держателей), `ld_cbfx` (`zz_ef_cbfx_update_sorted`,
  `zz_ef_holders_update`: списки для таблицы валют и круга держателей), `ld_pb_fso_sguis` (показ строк журнала).
- `common/scripted_buttons/00_ef_buttons.txt` (16) — кнопки журналов: `speculative_share_1..8_button`, `latin_/scandinavian_monetary_union_1/2_button`.
  `ld_pb_css_private_ban_buttons.txt` — `zz_pb_ef_css_private_ban_button` / `_allow_button` (кнопки ИИ).
- `common/scripted_progress_bars/00_ef_progressbar.txt` (10) — полосы журналов (`currency_standards_`, `central_banking_`, `stock_exchange_`,
  `financial_center_`, `speculative_share_`, `overbuilt_economy_`, `*_monetary_union_`, `silver_crisis_`, `je_efcc_progress_bar`).
- `common/game_concepts/00_ef_game_concepts.txt` (75 `concept_*`), `ld_cb_rate_concepts.txt` (2: `concept_zz_ef_policy_rule_rate`,
  `concept_zz_ef_discretionary_adjustment`), `PSC_game_concepts.txt` (`concept_construction_spending`).

### Локализация (`localization/<язык>/`, 11 языков)
- Полные: `english/` (38 `.yml`) и `russian/`
  (+`zz_ef_rus_gui_fix_l_russian.yml`, 22 строки ключей, которых нет в моде). Остальные девять — копии английской
  (`python ../vic3_mods/tools/ld_loc_langs.py`).
- Группы: `00_ef_gui_localization_*` (12 351 строка: подписи панелей), `01_ef_*` (здания, компании, понятия, валюты, события,
  товары, законы, модификаторы, технологии, подсказки), `PSC_*`, `ld_*` (`ld_missing_keys` — литеральные ключи из `.gui`/`custom_description`, не определённые в других файлах; `ld_cb_rate_panel`, `ld_economy_panel`, `ld_cbfx`,
  `ld_bond_tables`, `ld_monetary_policy`, `ld_currency_trade`, …), `replace/ld_*` (REPLACE-ключи: `ld_money_supply_replace`,
  `ld_cb_loan_replace`, `ld_pb_psc`, `ld_tgr_private_ownership_stock`, `ld_psc_modifiers`; только русская — `ld_vanilla_fix`: ключ
  `INSTITUTION_NEW_EFFECT` с `[INSTITUTION.GetName]` вместо ошибочного ванильного `[INSTITUTION_TYPE.GetName]`).

## Поток / порядок
- Регистрация GUI-типов — при загрузке; победитель по правилу выше. Типы `ld_*` и `ld_currency_symbol_fix` не имеют
  оригиналов в `00_ef_deported_gui_*` (оригиналы удалены), конфликтов нет.
- Виджет моста `zz_ef_money_hook` (HUD) постоянно живёт; для каждой страны из глобального списка `zz_ef_hook_countries`
  (её ставит недельный шаг денег, `common/scripted_effects/ld_money_model.txt`) состояние `trigger_when = [Scope.IsSet]`
  вызывает `zz_ef_money_hook_probe_sg`, `zz_ef_player_sg` (корень `GetPlayer` — роль А игроку) и `zz_ef_money_hook_sg` с областями `ext`, `abr` и ~20 `g_*` (данные, которые скрипт не
  видит: тренды дохода/расхода, торговый баланс, самодолг). Приёмник `zz_ef_money_hook_receive` (`ld_money_model.txt`)
  забирает `var:zz_ef_hook_pending`, снимает страну со списка и только пишет числа в переменные (`zz_ef_hk_*`, `zz_ef_g_*`);
  расчёт по ним — `zz_ef_bridge_apply` в недельном шаге (`money-model.md`). Мост работает только при открытом/созданном HUD.
- Клик по кнопке: `onclick = [GetScriptedGui('<имя>').Execute(GuiScope.SetRoot(GetPlayer.MakeScope).End)]`; видимость/доступность:
  `.IsShown(...)` / `.IsValid(...)`; параметры — `.AddScope('имя', MakeScopeValue(...))`. Корень — игрок, рынок (`Market.MakeScope`) или страна.
- Списки панелей: `GetGlobalList('<имя>')` в `datamodel` (список заполняет эффект/sgui при открытии секции; `*_list_gerenation_ordered` определён только `world_currency_…`).
- Открытие секций/окон: `GetVariableSystem.Toggle('<флаг>')` (чисто GUI, скрипт не видит). Окно резервов: ещё
  `ExecuteConsoleCommand('gui.createwidget gui/ef_dev_and_custom_windows/ef_custom_windows.gui gold_reserve_window')`.
- Журналы: `scripted_button`/`scripted_progress_bar`/`widget = { gui = …; name = …; container = … }` в `common/journal_entries/*`.

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `zz_ef_hook_countries` (глобальный список), `zz_ef_hook_pending` | очередь моста | `ld_money_model.txt` | `gui/ld_money_hook.gui`, `zz_ef_money_hook_receive` |
| `zz_ef_hook_probe_calls` (глобальная) | счётчик запусков моста | `zz_ef_money_hook_probe_sg` | `common/script_values/ld_money_model_values.txt` |
| `zz_ef_cbfx_list`, `zz_ef_holders_list` | таблицы валют ЦБ и держателей | `ld_cbfx.txt` | `gui/ld_economy_panel.gui` |
| `zz_ef_bt_in_list`, `zz_ef_bt_out_list` | таблицы облигаций | `ld_bond_tables.txt` | `gui/ld_cb_rate_panel.gui` |
| `national_capacity_variable_list_ordered_1` | порядок кругов резервов | `common/scripted_effects/08_list_effect.txt` | `gui/ld_national_capacity_chart.gui` |
| `EF_gui_room_brut` | число открытых «комнат» окна резервов | `common/script_values/00_economic_scripted_value.txt` | `EF_room_gui_N` |
| GUI-флаги (`GetVariableSystem`) | `currency_reserves`, `seller_country`, `ai_seller`, `national_debt`, `small_monetary_policy`, `ef_companies_compact`, `hide_current_companies`, `zz_pb_ef_fso_overcap_closed`, `zz_pb_ef_fso_bubble_closed`, `gold_reserve_window` | GUI | GUI |

## Вызовы и связи
- Панели, зависящие от других подсистем (описаны там): деньги — `ld_money_model.txt`; ставка/ЦБ — `ld_cb_rate_*`; валютный клиринг — `ld_cbfx`;
  облигации — `ld_bond_tables`; стройка — `PSC_*`.
- GUI ссылается на 2757 имён `GetScriptedGui('…')`; не определены в `common/scripted_guis`: 10 живых вызовов `*_list_gerenation_ordered`
  (кнопки секций в `ld_cb_rate_panel.gui`; файл ведёт генератор `regen_ef_cb_rate_gui`; определён только `world_currency_…` в `09_ef_other.txt`),
  9 вызовов `gdpg_sort_by_country_gdp` (там же; sgui — `gdp_sort_by_country_gdp`), `je_meiji_restoration_get_faction_sgui` (`states_panel.gui`, ванильное имя). Клик не выполняет эффекта (ожидается ошибка поиска sgui в `error.log`; в игре не проверено).
- `topbar.gui` → `currency_symbol_top_bar` (один `GetCustom('currency_symbol')` — «<две буквы страны> <знак слова>», `currencies.md`).
- Комментарий в `common/game_concepts/ld_cb_rate_concepts.txt` называет `zz_ef_cb_rate_panel_l_*.yml`; файлы локализации — `ld_cb_rate_panel_l_*.yml`.

## Логи
- GUI-логов с префиксом нет. Для проверки: `gui.log` (дубли типов «already registered at …», пропавшие `name=`/`type=`),
  `error.log` (отсутствующие sgui). Счётчик моста — `zz_ef_hook_probe_calls`.

## Витрина (R1а.9)
Окна читают значения модели только через витрину: всё, что они берут функциями данных (`ScriptValue` / `Var` /
`GetVariable` с `zz_ef_*`), перечислено ниже; список строит `../vic3_mods/tools/ld_vitrine.py --write` (`--check` — сверка).
Классы: `var` — переменная страны; `vit` — значение, которое только читает переменную (дёшево); `calc` — значение,
считаемое при каждой перерисовке окна (переносится за переменную шага в R10; каждый этап держит витрину живой:
новые числа для окон — переменная шага + `zz_ef_v_*`). Торговля недели в «Бюджет → Экономика» читает
`zz_ef_v_f_imp` / `zz_ef_v_f_exp` (шаг, R1а.7), а не суммы по 53 товарам. Значение `zz_ef_bank_capital` окон — остаток
пула (пул + кредиты + облигации − вклады − кредит ЦБ − вклады чужих ЦБ), т. е. капитал банков учёта
(`var:zz_ef_bank_capital`, `money-model.md`) + «прочее».
<!-- vitrine -->
Сгенерировано `../vic3_mods/tools/ld_vitrine.py --write`. Имён 586: переменных 11, значений-витрины 159, вычисляемых при перерисовке 416; файлов 13.

| имя | класс | где читается |
| --- | --- | --- |
| `zz_ef_abroad_net` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg0_pct_5y` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg0_pct_month` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg0_pct_year` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg1_pct_5y` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg1_pct_month` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg1_pct_year` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg2_pct_5y` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg2_pct_month` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg2_pct_year` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg3_pct_5y` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg3_pct_month` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg3_pct_year` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg_m0` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg_m0_to_gdp` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg_m1` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg_m1_to_gdp` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg_m2` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg_m2_to_gdp` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg_m3` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bank_assets` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bank_bonds` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bank_capital` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bank_cash` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bank_cb_debt` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bank_liabilities` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bank_loans` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bankm_money` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bc_debt` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bc_debt_to_gdp` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_div_in` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_div_out` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_exp` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_fin_in` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_fin_out` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_in_total` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_int_in` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_int_out` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_oth_in` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_oth_out` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_out_total` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_sec_in` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_sec_out` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bt_b_amt` | var | `gui/ld_cb_rate_panel.gui`, `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bt_b_year` | var | `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bt_t_amt` | var | `gui/ld_cb_rate_panel.gui`, `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bt_t_rate` | calc | `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bt_t_week` | var | `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bto_b_amt` | var | `gui/ld_cb_rate_panel.gui`, `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bto_b_year` | var | `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bto_t_amt` | var | `gui/ld_cb_rate_panel.gui`, `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bto_t_rate` | calc | `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bto_t_week` | var | `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bubble_step_eff` | calc | `localization/english/ld_pb_overbuild_l_english.yml` |
| `zz_ef_cb_cover` | calc | `localization/english/01_ef_tooltips_localization_l_english.yml`, `localization/english/ld_cb_rate_panel_l_english.yml`, `localization/english/ld_economy_panel_l_english.yml` и ещё 2 |
| `zz_ef_cb_credit_target` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_cb_loan_after_to_gdp` | calc | `localization/english/replace/ld_cb_loan_replace_l_english.yml` |
| `zz_ef_cb_loan_now_to_gdp` | calc | `localization/english/replace/ld_cb_loan_replace_l_english.yml` |
| `zz_ef_cb_money` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_cb_rate_bias_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rate_months_to_step` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rate_next_step_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rate_note_value` | vit | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rate_rating_target` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rate_target` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rule_cover_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rule_gap_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rule_inflation_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rule_money_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rule_neutral_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rule_risk_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_valuation` | calc | `localization/english/01_ef_tooltips_localization_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_cbfx_dinar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_algerian_dinar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_algerian_dinar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_algerian_dinar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_algerian_dinar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_iraqi_dinar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_iraqi_dinar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_iraqi_dinar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_iraqi_dinar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_libyan_dinar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_libyan_dinar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_libyan_dinar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_libyan_dinar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_moroccan_dirham` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_moroccan_dirham_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_moroccan_dirham_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_moroccan_dirham_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_omanian_rial` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_omanian_rial_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_omanian_rial_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_omanian_rial_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_qiran` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_qiran_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_qiran_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_qiran_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_saudi_riyal` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_saudi_riyal_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_saudi_riyal_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_saudi_riyal_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_serbian_dinar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_serbian_dinar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_serbian_dinar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_serbian_dinar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_tunisian_dinar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_tunisian_dinar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_tunisian_dinar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_tunisian_dinar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_yugoslav_dinar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_yugoslav_dinar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_yugoslav_dinar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dinar_yugoslav_dinar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_australian_dollar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_australian_dollar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_australian_dollar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_australian_dollar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_canadian_dollar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_canadian_dollar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_canadian_dollar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_canadian_dollar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_caribbean_dollar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_caribbean_dollar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_caribbean_dollar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_caribbean_dollar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_confederate_states_dollar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_confederate_states_dollar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_confederate_states_dollar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_confederate_states_dollar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_liberian_dollar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_liberian_dollar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_liberian_dollar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_liberian_dollar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_new_zealand_dollar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_new_zealand_dollar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_new_zealand_dollar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_new_zealand_dollar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_sierra_leonean_dollar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_sierra_leonean_dollar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_sierra_leonean_dollar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_sierra_leonean_dollar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_united_states_dollar` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_united_states_dollar_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_united_states_dollar_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_dollar_united_states_dollar_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_ariary` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_ariary_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_ariary_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_ariary_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_central_african_eco` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_central_african_eco_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_central_african_eco_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_central_african_eco_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_east_african_eco` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_east_african_eco_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_east_african_eco_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_east_african_eco_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_ethiopian_birr` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_ethiopian_birr_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_ethiopian_birr_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_ethiopian_birr_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_ghanaian_pound` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_ghanaian_pound_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_ghanaian_pound_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_ghanaian_pound_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_nigerian_naira` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_nigerian_naira_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_nigerian_naira_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_nigerian_naira_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_south_african_rand` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_south_african_rand_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_south_african_rand_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_south_african_rand_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_tuareg_ouguiya` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_tuareg_ouguiya_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_tuareg_ouguiya_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_tuareg_ouguiya_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_west_african_eco` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_west_african_eco_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_west_african_eco_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_eco_west_african_eco_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_belgian_franc` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_belgian_franc_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_belgian_franc_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_belgian_franc_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_french_franc` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_french_franc_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_french_franc_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_french_franc_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_luxembourgish_franc` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_luxembourgish_franc_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_luxembourgish_franc_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_luxembourgish_franc_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_swiss_franc` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_swiss_franc_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_swiss_franc_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_franc_swiss_franc_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_bavarian_gulden` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_bavarian_gulden_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_bavarian_gulden_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_bavarian_gulden_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_florin` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_florin_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_florin_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_florin_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_hungarian_forint` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_hungarian_forint_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_hungarian_forint_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_hungarian_forint_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_indies_guilder` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_indies_guilder_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_indies_guilder_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_indies_guilder_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_south_german_gulden` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_south_german_gulden_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_south_german_gulden_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_gulden_south_german_gulden_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_czech_koruna` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_czech_koruna_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_czech_koruna_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_czech_koruna_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_danish_krone` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_danish_krone_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_danish_krone_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_danish_krone_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_estonian_kroon` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_estonian_kroon_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_estonian_kroon_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_estonian_kroon_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_icelandic_krona` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_icelandic_krona_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_icelandic_krona_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_icelandic_krona_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_norwegian_krone` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_norwegian_krone_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_norwegian_krone_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_norwegian_krone_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_slovak_koruna` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_slovak_koruna_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_slovak_koruna_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_slovak_koruna_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_swedish_krona` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_swedish_krona_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_swedish_krona_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_krone_swedish_krona_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_leon_leu` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_leon_leu_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_leon_leu_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_leon_leu_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_leon_lev` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_leon_lev_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_leon_lev_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_leon_lev_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_ducato` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_ducato_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_ducato_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_ducato_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_ottoman_lira` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_ottoman_lira_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_ottoman_lira_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_ottoman_lira_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_scudo_pontificio` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_scudo_pontificio_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_scudo_pontificio_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_scudo_pontificio_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_scudo_sardo` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_scudo_sardo_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_scudo_sardo_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_scudo_sardo_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_toscane_lira` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_toscane_lira_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_toscane_lira_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_lira_toscane_lira_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_mark` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_mark_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_mark_finnish_markka` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_mark_finnish_markka_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_mark_finnish_markka_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_mark_finnish_markka_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_mark_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_mark_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_argentine_peso` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_argentine_peso_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_argentine_peso_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_argentine_peso_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_bolivien_peso` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_bolivien_peso_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_bolivien_peso_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_bolivien_peso_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_chilean_peso` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_chilean_peso_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_chilean_peso_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_chilean_peso_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_colombian_peso` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_colombian_peso_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_colombian_peso_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_colombian_peso_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_costa_rican_colon` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_costa_rican_colon_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_costa_rican_colon_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_costa_rican_colon_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_cuban_peso` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_cuban_peso_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_cuban_peso_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_cuban_peso_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_ecuadorian_peso` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_ecuadorian_peso_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_ecuadorian_peso_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_ecuadorian_peso_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_el_salvador_colon` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_el_salvador_colon_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_el_salvador_colon_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_el_salvador_colon_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_guatemalan_quetzal` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_guatemalan_quetzal_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_guatemalan_quetzal_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_guatemalan_quetzal_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_honduran_lempira` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_honduran_lempira_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_honduran_lempira_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_honduran_lempira_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_mexican_peso` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_mexican_peso_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_mexican_peso_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_mexican_peso_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_nicaraguan_cordoba` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_nicaraguan_cordoba_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_nicaraguan_cordoba_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_nicaraguan_cordoba_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_paraguayan_peso` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_paraguayan_peso_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_paraguayan_peso_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_paraguayan_peso_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_philippine_peso` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_philippine_peso_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_philippine_peso_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_philippine_peso_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_sol_de_oro` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_sol_de_oro_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_sol_de_oro_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_sol_de_oro_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_uruguayan_peso` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_uruguayan_peso_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_uruguayan_peso_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_uruguayan_peso_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_venezuelan_peso` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_venezuelan_peso_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_venezuelan_peso_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_peso_venezuelan_peso_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_pound_egyptian_pound` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_pound_egyptian_pound_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_pound_egyptian_pound_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_pound_egyptian_pound_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_pound_irish_pound` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_pound_irish_pound_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_pound_irish_pound_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_pound_irish_pound_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_pound_sterling` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_pound_sterling_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_pound_sterling_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_pound_sterling_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_real` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_real_brazilian_real` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_real_brazilian_real_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_real_brazilian_real_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_real_brazilian_real_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_real_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_real_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_real_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_rupee_indian_rupee` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_rupee_indian_rupee_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_rupee_indian_rupee_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_rupee_indian_rupee_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_rupee_indonesian_rupiah` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_rupee_indonesian_rupiah_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_rupee_indonesian_rupiah_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_rupee_indonesian_rupiah_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_baht` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_baht_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_baht_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_baht_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_dong` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_dong_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_dong_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_dong_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_drachma` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_drachma_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_drachma_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_drachma_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_korean_won` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_korean_won_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_korean_won_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_korean_won_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_latvian_lats` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_latvian_lats_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_latvian_lats_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_latvian_lats_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_lithuanian_litas` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_lithuanian_litas_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_lithuanian_litas_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_lithuanian_litas_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_peseta` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_peseta_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_peseta_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_peseta_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_ruble` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_ruble_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_ruble_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_ruble_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_uni` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_uni_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_uni_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_uni_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_yen` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_yen_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_yen_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_yen_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_yuan` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_yuan_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_yuan_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_yuan_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_zloti` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_zloti_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_zloti_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_spe_zloti_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_thaler_hannoveraner_thaler` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_thaler_hannoveraner_thaler_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_thaler_hannoveraner_thaler_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_thaler_hannoveraner_thaler_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_thaler_prussian_thaler` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_thaler_prussian_thaler_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_thaler_prussian_thaler_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_thaler_prussian_thaler_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_thaler_saxon_thaler` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_thaler_saxon_thaler_d` | vit | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_thaler_saxon_thaler_gold` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cbfx_thaler_saxon_thaler_money` | calc | `localization/english/ld_cbfx_l_english.yml` |
| `zz_ef_cc_debt` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_cc_rate` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_circ_business_cash` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_circ_growth_year` | calc | `localization/english/01_ef_tooltips_localization_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_clr_metal_share` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_clr_pay_ratio_v` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_clr_pot_value` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_clr_ratio_v` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_credit_limit` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_credit_now` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_credit_to_gdp` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_credit_total` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_currency_strength` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_debt_principal` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_deposit_margin` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_deposit_rate` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_foreign_assets` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_fx_liab_all` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_fx_money` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_gdp_growth_year` | calc | `localization/english/01_ef_tooltips_localization_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_gdp_week` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_gov_rate_corr_pct` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_gov_rate_premium_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_gov_rate_target` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_holds_pc` | var | `gui/ld_economy_panel.gui` |
| `zz_ef_hook_calls` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_hook_ok` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_hook_probe_calls` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_inflation` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_literate_rich_share` | var | `localization/english/ld_cm_goods_l_english.yml` |
| `zz_ef_mp_cum_v` | vit | `localization/english/ld_monetary_policy_l_english.yml` |
| `zz_ef_mp_dyn_pp` | calc | `localization/english/ld_monetary_policy_l_english.yml` |
| `zz_ef_mp_flow_v` | vit | `localization/english/ld_monetary_policy_l_english.yml` |
| `zz_ef_mp_months_left` | calc | `localization/english/ld_monetary_policy_l_english.yml` |
| `zz_ef_mp_pace_v` | calc | `localization/english/ld_monetary_policy_l_english.yml` |
| `zz_ef_mp_progress` | calc | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_mp_start_v` | vit | `localization/english/ld_monetary_policy_l_english.yml` |
| `zz_ef_mp_target_v` | vit | `localization/english/ld_monetary_policy_l_english.yml` |
| `zz_ef_nr_dep_v` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_other_treasury_rest` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_pool` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_pool_months` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_pool_transfer_week` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_pop_cash` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_pop_cash_held` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_pop_deposits` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_pop_savings` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_popm_gold` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_popm_money` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_popm_silver` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_price_index` | calc | `localization/english/01_ef_tooltips_localization_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_fixed_expenses` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_fixed_income` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_gdp` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_military` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_minting_week` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_pool_gross` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_pool_net` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_total_expenses` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_total_income` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_reserve_norm` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_risk_debt_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_risk_fx_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_sav_norm` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_savings_to_gdp` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_total_expenses_week` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_total_income_week` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_tr_to_cb` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_treasury` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_treasury_bonds` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_cbl_int` | calc | `gui/ld_money_hook.gui`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_abroad` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_agg0` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_agg1` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_agg2` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_agg3` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_bonds` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_buildings` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_cbm` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_deposits` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_deposits_neg` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_pool` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_savings` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_tbonds` | vit | `gui/ld_money_hook.gui`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_tc` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_treasury` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_bc_int` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_bc_new` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_bc_paid` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_bl_int_in` | vit | `gui/ld_money_hook.gui`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_bl_int_out` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_bl_redeem` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_bl_sold` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_buyback_m` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_borrow` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_hume_m` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_interest` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_repay` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_rescale` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_reval` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_stock` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_clr_fx_money` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_clr_metal_money` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_clr_reserves_money` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_clr_unsettled` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cons_buy` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cons_int` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_contrib` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_exp` | vit | `gui/ld_economy_panel.gui` |
| `zz_ef_v_f_ext` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_ext_net` | vit | `gui/ld_economy_panel.gui`, `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_imp` | vit | `gui/ld_economy_panel.gui`, `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_inflow` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_leak` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_mint` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_mint_own` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_mint_tr` | vit | `gui/ld_money_hook.gui`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_pool_other` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_tr_pool` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_trade` | vit | `gui/ld_economy_panel.gui` |
| `zz_ef_v_f_transfer` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_fx_metal` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_cc_int` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_cc_issue` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_cc_repay` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_clr_cur_out` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_clr_fx_in_money` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_clr_own_back` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_dep_int` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_hume_money` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_inflow` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_nr_dep` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_value_in_silver` | calc | `localization/english/01_ef_tooltips_localization_l_english.yml` |
<!-- /vitrine -->
