# Интерфейс (панели, окна, мост GUI → скрипт, локализация)
**Смысл.** Всё, что игрок видит и нажимает; окна читают витрину и ничего не считают. **Понятия:** [[Витрина]],
[[Мост GUI]]. **Решения:** Д.R3б.3, Д.R0.8.10 (`решения.md`).

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
- `gui/ld_cb_rate_panel.gui` (руками) — `budget_panel_financial_panel_content` (:10): ключевая ставка,
  ЦБ, облигации, таблицы держателей (`zz_ef_bt_in_list`/`zz_ef_bt_out_list`), биржа игрока — две таблицы
  (`zz_ef_xwin_own`, `zz_ef_xwin_book`, `ld_exchange_window.txt`), `mp_row` политики.
- `gui/ld_currency_symbol_fix.gui` — единственное определение `currency_symbol_country_panel` (один текстбокс
  `GetCustom('currency_symbol')`). Используется 5 раз в `00_ef_deported_gui_1.gui:87912…`.
- `gui/ld_national_capacity_chart.gui` — единственное определение `ef_bp_national_capacity_piechart` (используется
  `ld_economy_panel.gui:8273`); ряд в металле стандарта, доли — в золотом эквиваленте.
- `gui/ld_money_hook.gui` — мост «бюджет → скрипт» (см. ниже); регистрация `gui/scripted_widgets/ld_money_hook.txt`.
- `gui/ld_logs_hook.gui` — в режиме отладки включает логи `EF*` (`zz_ef_logs_debug_sg`; `docs/entry-points.md`, «Логи»); регистрация
  `gui/scripted_widgets/ld_logs_hook.txt`.
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
  `*_list_gerenation_ordered` (2 шт.), `gold_gui_N`/`silver_gui_N`, `gdp_sort_by_country_gdp`.
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
| `zz_ef_xwin_own` — наши активы, `zz_ef_xwin_book` — предложения на нашей бирже: прошедшие через её стакан на прошлой неделе (ключи `zz_ef_xr_<вид>_c` биржи) и короткий список (хозяин рынка, лидер блока, эталон, `zz_ef_xdeep`) (глобальные списки); на строке-стране `zz_ef_xwin_fair/_last/_hold/_gold/_bid/_ask` (`zz_ef_xwin_row_set`; облигации — без bid / ask фонда); на игроке `zz_ef_xpl_kind`, `zz_ef_xpl_sum` (заголовок — значения `zz_ef_xwin_fee_v/_bid_v/_ask_v`), карты заявок `zz_ef_xpl_buy_m/_b`, `zz_ef_xpl_sell_m/_b` | окно биржи игрока (минимальное, Д.R8б.13) | `common/scripted_guis/ld_exchange_window.txt` (`zz_ef_xwin_fill` — `ld_exchange_trade.txt`) | `gui/ld_cb_rate_panel.gui`; заявки — `zz_ef_xch_post_player` (шаг игрока) |
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

## Витрина

Окна читают значения модели только через витрину ([[Витрина]]): всё, что они берут функциями данных (`ScriptValue` /
`Var` / `GetVariable` с `zz_ef_*`). Список имён с классом и местом чтения — генерат `vitrine.md`
(`../vic3_mods/tools/ld_vitrine.py --write`, `--check` — сверка); читать при правке окна, которое берёт число модели.
