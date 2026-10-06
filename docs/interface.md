# Интерфейс (панели, окна, мост GUI → скрипт, локализация)
Всё, что игрок видит и нажимает: ванильные панели, переписанные E&F (бюджет, рынок, страна, штат, топбар, компании),
вкладки валют/запасов/ЦБ, журнальные виджеты, отладочные окна. Кнопки зовут скрипт через scripted_gui; данные идут
в GUI через `GetCustom`/`ScriptValue`/`GetGlobalList`. Игра читает GUI один раз при загрузке — активной логики нет,
считает скрипт (другие подсистемы).

## Файлы
GUI-тип регистрирует первый файл по имени (ASCII, по всем модам; при равных — ближе к корню `gui/`); дубль типа мёртв.
Мод-файл с путём ванильного заменяет его целиком. Подкаталог мода проигрывает корню мода, но выигрывает у ванили
с тем же именем (так «потерянные» типы в `maj/*` ломали ваниль).

### Заменяют ванильный файл по пути (копия ванили + вставки E&F)
- `gui/budget_panel.gui` — `budget_panel` (2186 строк); вкладки вставляют типы `budget_panel_economy_panel_content` (:1518),
  `budget_panel_financial_panel_content` (:1522), `budget_panel_stockpile_panel_content` (:1526); `@money!` вместо символа валюты.
- `gui/market_panel.gui` — `market_panel`; блок «E&F» с `market_global_panel_content` (:949), кнопки
  `market_gui_market_currency_list` / `market_gui_market_financial_product_list` (:52, :1212-1403).
- `gui/states_panel.gui` — `states_panel`; `state_panel_currency_panel_content` (:1459).
- `gui/country_panel.gui` — `country_panel`; `country_panel_currency_panel_content` (:968).
- `gui/topbar.gui` — `topbar`; `currency_symbol_top_bar` (:540), прогрессбары `white_/gold_progressbar_horizontal_law` (:576, :591).
- `gui/companies_panel.gui` — ванильная + `ef_company_type_row` / `ef_established_company_row`, флаг `ef_companies_compact`
  (сжатый список непостроенных компаний).
- `gui/construction_panel.gui` — заглушка (3 строки, комментарий): не даёт загрузиться ванильному; типы стройки — в PSC-файле.
- `gui/frontend/shared/lists.gui` — копия ванильного (`dropdown_menu_standard`, `scrollbox`); E&F-вставок нет.
- `gui/texticons.gui` (309 текстиконок) — копия ванильного; 30 имён иконок повторены в `gui/00_ef_texticons.gui` (249).

### Файлы E&F
- `gui/00_ef_deported_gui_1.gui` (197 тыс. строк) — 4 типа: `market_global_panel_content` (:37, рынок валют: купить/продать
  по каждой валюте), `budget_panel_stockpile_panel_content` (:131694, запасы/резервы), `country_panel_currency_panel_content`
  (:180607), `state_panel_currency_panel_content` (:180730). Шесть пустых `types market_states_panel`-обёрток. Повтор блока по валютам.
- `gui/00_ef_deported_gui_2.gui` (11906 строк) — 205 типов: 191 `ef_bp_*_piechart` (круговые диаграммы запасов/денег по
  валютам; данные из `GetGlobalList('..._variable_list_ordered_N')`), `currency_symbol_top_bar` (:8567, 96 текстбоксов
  символов), `ef_economy_N_formwork`/`ef_financial_N_formwork` (:9289-10680), `vo_plotline_*` (:10983-11867).
- `gui/00_ef_texticons.gui` — иконки текста E&F. `gui/00_MPM_building_details_panel.gui` — MPM: `condensed_building_information*`.
- `gui/00_ef_debug_widget.gui` — виджет `01_ef_debug_widget`: зеркалит `[InDebugMode]` в глобальный флаг `EF_debug_mode`
  через sgui `EF_sg_set_debug_flag` / `EF_sg_unset_debug_flag`.
- `gui/scripted_widgets/00_ef_custom_widgets.gui` — виджеты журнала: `widget_je_ef_efcc_situation` (используется
  `common/journal_entries/00_ef_divers_je.txt:1662`), `widget_je_ef_fc_fso_situation`, `widget_je_ef_pcs_fso_situation`
  (журналы на них больше не ссылаются), кнопки `speculative_share_N_button`.
- `gui/scripted_widgets/EF_scripted_widgets.txt` — регистрация gui/01_ef_debug_widget.gui = 01_ef_debug_widget;
  `PSC_scripted_widgets.txt` — `gui/PSC_construction_expense_widget.gui`.
- `gui/ef_dev_and_custom_windows/ef_custom_windows.gui` (56 тыс. строк) — 83 `default_popup`: `gold_reserve_window`,
  `currency_reserve_window`, `ef_custom_windows` (хаб кнопок) и 80 тестовых `panel_*`; все открываются
  `ExecuteConsoleCommand('gui.createwidget …')` + `GetVariableSystem.Toggle('<имя>')`.
- `gui/ef_dev_and_custom_windows/maj/Essential/*.gui` (8) — `budget_panel`, `market_panel`, `states_panel` (дубли корневых,
  отличаются подстановкой `[..GetCustom('currency_symbol')]` вместо `@money!`), `building_browser_panel`,
  `building_details_panel`, `goods_panel`, `goods_state_panel`, `production_methods` — подмены ванильных по имени.
- `gui/ef_dev_and_custom_windows/maj/NonEssential/*.gui` (19) — копии ванильных (`custom_tooltip`, `right_click_menu`,
  `map_list_panel`, `map_markers`, `military_formation_panel`, `popups`, `outliner_pinnable_types`, `graph_tooltips`, …);
  `companies_panel.gui` там — 63 строки, проигрывает корневому.

### Файлы проекта (`ld_*`, переопределяют типы E&F; грузятся раньше или вместо оригинала)
- `gui/ld_economy_panel.gui` (генерат. `regen_ef_economy_panel_gui.py`) — `budget_panel_economy_panel_content` (:10,
  оригинал из `00_ef_deported_gui_1.gui` удалён), торговый баланс в модели денег, кнопка отладки `Panel_1` (:54),
  `zz_ef_holders_piechart` (:9833), `zz_ef_bank_holders_piechart` (:9875), `vo_plotline_minting`.
- `gui/ld_cb_rate_panel.gui` (генерат. `regen_ef_cb_rate_gui.py`) — `budget_panel_financial_panel_content` (:10): ключевая ставка,
  ЦБ, облигации, таблицы держателей (`zz_ef_bt_in_list`/`zz_ef_bt_out_list`), `mp_row` политики.
- `gui/ld_currency_symbol_fix.gui` — единственное определение `currency_symbol_country_panel` (один текстбокс
  `GetCustom('currency_symbol')`). Используется 5 раз в `00_ef_deported_gui_1.gui:180618…`.
- `gui/ld_national_capacity_chart.gui` — единственное определение `ef_bp_national_capacity_piechart` (используется
  `ld_economy_panel.gui:8335`); ряд в металле стандарта, доли — в золотом эквиваленте.
- `gui/ld_money_hook.gui` — мост «бюджет → скрипт» (см. ниже); регистрация `gui/scripted_widgets/ld_money_hook.txt`.
- `gui/scripted_widgets/ld_pb_fso_widgets.gui` — журнальные виджеты `zz_pb_ef_fso_bubble_widget`, `zz_pb_ef_fso_overcap_widget`,
  `zz_pb_ef_fso_hide_bars_widget` (подключены `common/journal_entries/00_ef_financial_center_je.txt:184-199`).

### PSC
- `gui/PSC_construction_panel.gui` (`construction_panel*`, `ship_construction_*`), `gui/PSC_states_panel_buildings.gui`
  (`buildings_list*`), `gui/shared/PSC_construction_spending_options.gui` (`construction_frame_coin`, `set_level_bar_construction*`),
  `gui/PSC_construction_expense_widget.gui` (скрытый виджет: `psc_test_show` → `psc_save_real_construction_cost`),
  `gui/PSC_goods_texticons.gui` (4 иконки строительных товаров).

### Скриптовые GUI / кнопки / прогресс-бары / понятия
- `common/scripted_guis/00_economic_scripted_guis.txt` (959 определений) — выбор валюты `choose_currency_type_<cur>`
  (+`_visible`, `_on`, `_off`), `money_value_<cur>_visible`, `<cur>_buy_in_gold`/`_sell_in_gold`, девальвация/ревальвация
  (`devaluation_*`, `revaluation_*`, `set_*_rate`), `currency_quantity_increase/_reduce`, `is_ai`/`not_is_ai`, законы стандартов.
- `common/scripted_guis/00_stockpile_scripted_guis.txt` (1602) — запасы по валютам, `set_store_<товар>_enabled`, `buy_<товар>_budget_panel_visible`, `trade_<товар>_budget_panel*`.
- `common/scripted_guis/00_financial_scripted_guis.txt` (45) — облигации, кредит ЦБ, `speculative_share_N_button` (sgui),
  `transfert_currency_to_investement_pool_*`, `global_player_help_*`.
- `common/scripted_guis/09_ef_other.txt` (1155) — отладочный флаг (`EF_sg_set_debug_flag`, `EF_sg_unset_debug_flag`,
  `EF_debug_mode_visibility` = `always = no`), `EF_room_gui_N`/`EF_current_room_gui_N` (100+100; панель `gold_reserve_window`),
  `stockpiling_<cur>_visibility`/`_state_visibility`, `law_<cur>_*`, `*_list_gerenation_ordered` (2 шт.), `gold_gui_N`/`silver_gui_N`.
- `common/scripted_guis/PSC_construction_sguis.txt` (9) — `psc_button_*_sgui`, `psc_save_real_construction_cost`, `psc_test_show`.
- `common/scripted_guis/com_local_goods_sgui.txt` — `com_add_local_good` (добавляет в список `com_local_goods`; вызова нет).
- `common/scripted_guis/ld_*.txt` — `ld_money_hook` (приёмник моста), `ld_cb_rate_buttons` (кнопки ставки), `ld_monetary_policy_buttons`
  (девальвация/ревальвация как инструмент ЦБ), `ld_bond_tables` (заполнение таблиц держателей), `ld_cbfx` (`zz_ef_cbfx_update_sorted`,
  `zz_ef_holders_update`: списки для таблицы валют и круга держателей), `ld_pb_fso_sguis` (показ строк журнала).
- `common/scripted_buttons/00_ef_buttons.txt` (21) — кнопки журналов: `speculative_share_1..13_button`, `latin_/scandinavian_monetary_union_1/2_button`,
  `bank_central_currency_JE_1..4_button` (пустые). `ld_pb_css_private_ban_buttons.txt` — `zz_pb_ef_css_private_ban_button` / `_allow_button` (кнопки ИИ).
- `common/scripted_progress_bars/00_ef_progressbar.txt` (12) — полосы журналов (`currency_standards_`, `central_banking_`, `stock_exchange_`,
  `financial_center_`, `speculative_share_`, `overbuilt_economy_`, `*_monetary_union_`, `silver_crisis_`, `je_efcc_progress_bar`).
- `common/game_concepts/00_ef_game_concepts.txt` (77 `concept_*`), `ld_cb_rate_concepts.txt` (2: `concept_zz_ef_policy_rule_rate`,
  `concept_zz_ef_discretionary_adjustment`), `PSC_game_concepts.txt` (`concept_construction_spending`).
- Отладка: `common/decisions/00_ef_debug_decisions.txt` (11 решений, показ — `has_global_variable = EF_debug_mode`).

### Локализация (`localization/<язык>/`, 11 языков)
- Полные: `english/` (37 `.yml`) и `russian/`
  (+`zz_ef_rus_gui_fix_l_russian.yml`, 22 строки ключей, которых нет в моде). Остальные девять — копии английской
  (`python ../vic3_mods/tools/ld_loc_langs.py`).
- Группы: `00_ef_gui_localization_*` (12 351 строка: подписи панелей), `01_ef_*` (здания, компании, понятия, валюты, события,
  товары, законы, модификаторы, технологии, подсказки), `PSC_*`, `ld_*` (`ld_cb_rate_panel`, `ld_economy_panel`, `ld_cbfx`,
  `ld_bond_tables`, `ld_monetary_policy`, `ld_currency_trade`, …), `replace/ld_*` (REPLACE-ключи: `ld_money_supply_replace`,
  `ld_cb_loan_replace`, `ld_pb_psc`, `ld_tgr_private_ownership_stock`, `ld_psc_modifiers`).

## Поток / порядок
- Регистрация GUI-типов — при загрузке; победитель по правилу выше. Типы `ld_*` и `ld_currency_symbol_fix` не имеют
  оригиналов в `00_ef_deported_gui_*` (оригиналы удалены), конфликтов нет.
- Виджет моста `zz_ef_money_hook` (HUD) постоянно живёт; для каждой страны из глобального списка `zz_ef_hook_countries`
  (её ставит недельный шаг денег, `common/scripted_effects/ld_money_model.txt`) состояние `trigger_when = [Scope.IsSet]`
  вызывает `zz_ef_money_hook_probe_sg` и `zz_ef_money_hook_sg` с областями `ext`, `abr` и ~20 `g_*` (данные, которые скрипт не
  видит: тренды дохода/расхода, торговый баланс, самодолг). Приёмник `zz_ef_money_hook_receive` (`ld_money_model.txt:465`)
  забирает `var:zz_ef_hook_pending` и снимает страну со списка. Мост работает только при открытом/созданном HUD.
- Клик по кнопке: `onclick = [GetScriptedGui('<имя>').Execute(GuiScope.SetRoot(GetPlayer.MakeScope).End)]`; видимость/доступность:
  `.IsShown(...)` / `.IsValid(...)`; параметры — `.AddScope('имя', MakeScopeValue(...))`. Корень — игрок, рынок (`Market.MakeScope`) или страна.
- Списки панелей: `GetGlobalList('<имя>')` в `datamodel` (список заполняет эффект/sgui при открытии секции — `*_list_gerenation_ordered`).
- Открытие секций/окон: `GetVariableSystem.Toggle('<флаг>')` (чисто GUI, скрипт не видит). Отладочные окна: ещё
  `ExecuteConsoleCommand('gui.createwidget gui/ef_dev_and_custom_windows/ef_custom_windows.gui <окно>')`.
- Журналы: `scripted_button`/`scripted_progress_bar`/`widget = { gui = …; name = …; container = … }` в `common/journal_entries/*`.
- Выбор валюты в панели рынка: sgui `choose_currency_type_<cur>` обнуляет переменные `choose_currency_type_*` страны и ставит
  свою в 1; `choose_currency_type_<cur>_visible` показывает блок.

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `EF_debug_mode` (глобальная) | режим отладки E&F | `EF_sg_set_debug_flag` / `_unset_` (`gui/00_ef_debug_widget.gui`) | `common/decisions/00_ef_debug_decisions.txt:9,25` |
| `choose_currency_type_<cur>` (страна) | выбранная в панели валюта | sgui `choose_currency_type_<cur>` | `choose_currency_type_<cur>_visible` |
| `zz_ef_hook_countries` (глобальный список), `zz_ef_hook_pending` | очередь моста | `ld_money_model.txt` | `gui/ld_money_hook.gui`, `zz_ef_money_hook_receive` |
| `zz_ef_hook_probe_calls` (глобальная) | счётчик запусков моста | `zz_ef_money_hook_probe_sg` | `common/script_values/ld_money_model_values.txt` |
| `zz_ef_cbfx_list`, `zz_ef_holders_list`, `zz_ef_bank_holders_list` | таблицы валют ЦБ и держателей | `ld_cbfx.txt` | `gui/ld_economy_panel.gui` |
| `zz_ef_bt_in_list`, `zz_ef_bt_out_list` | таблицы облигаций | `ld_bond_tables.txt` | `gui/ld_cb_rate_panel.gui` |
| `national_capacity_variable_list_ordered_1` | порядок кругов резервов | `common/scripted_effects/08_list_effect.txt` | `gui/ld_national_capacity_chart.gui` |
| `EF_gui_room_brut` | число открытых «комнат» окна резервов | `common/script_values/00_economic_scripted_value.txt` | `EF_room_gui_N` |
| GUI-флаги (`GetVariableSystem`) | `stockpile_panel`, `currency_reserves`, `seller_country`, `ai_seller`, `national_debt`, `small_monetary_policy`, `ef_companies_compact`, `hide_current_companies`, `zz_pb_ef_fso_overcap_closed`, `zz_pb_ef_fso_bubble_closed`, `my_ef_custom_windows`, `<окно>` | GUI | GUI |

## Вызовы и связи
- Панели, зависящие от других подсистем (описаны там): деньги — `ld_money_model.txt`; ставка/ЦБ — `ld_cb_rate_*`; валютный клиринг — `ld_cbfx`;
  облигации — `ld_bond_tables`; стройка — `PSC_*`.
- GUI ссылается на 2757 имён `GetScriptedGui('…')`; не определены в `common/scripted_guis`: 25 живых вызовов `*_list_gerenation_ordered`
  (кнопки секций в `00_ef_deported_gui_1.gui`, `ld_economy_panel.gui`, `ld_cb_rate_panel.gui`, `00_ef_custom_widgets.gui`;
  определены только `financial_product_panel_…` и `world_currency_…` в `09_ef_other.txt:1946,1971`), `gdpg_sort_by_country_gdp`
  (13 вызовов), `je_meiji_restoration_get_faction_sgui` (`states_panel.gui`). Клик не выполняет эффекта (ожидается ошибка поиска sgui в `error.log`; в игре не проверено).
- `topbar.gui` → `currency_symbol_top_bar` (96 `GetCustom('currency_symbol_<cur>')`, считаются каждый кадр).
- Отладочная кнопка `Panel_1` (`gui/ld_economy_panel.gui:54`) открывает окно-хаб `ef_custom_windows`; условие показа
  `EF_debug_mode_visibility` в `:43` закомментировано — кнопка видна всем на вкладке «Экономика».
- `gui/scripted_widgets/EF_scripted_widgets.txt` указывает на gui/01_ef_debug_widget.gui (такого файла нет); файл называется `gui/00_ef_debug_widget.gui`
  (виджет внутри — `01_ef_debug_widget`): регистрация не находит файл, флаг `EF_debug_mode` может не ставиться.
- Подкаталог мода выигрывает у ванили: в `maj/NonEssential/{map_markers,custom_tooltip,military_formation_panel,popups,right_click_menu}.gui`
  и `frontend/shared/lists.gui` отсутствуют имена, которых нет в копиях E&F, но есть в ванили 1.13 (`enemy_naval_mission_marker`,
  `coastal_building_marker`, `naval_mission_marker_tooltip_fleet`, `military_formation_cancel_invasion_button`,
  `decommission_supply_ships_window`, `enemy_fleets_on_mission_in_sea_region`, `dropdown_menu_round`) — проверить `gui.log`/`error.log`.
- Комментарий в `common/game_concepts/ld_cb_rate_concepts.txt` называет `zz_ef_cb_rate_panel_l_*.yml`; файлы локализации — `ld_cb_rate_panel_l_*.yml`.

## Логи
- GUI-логов с префиксом нет. Для проверки: `gui.log` (дубли типов «already registered at …», пропавшие `name=`/`type=`),
  `error.log` (отсутствующие sgui). Счётчик моста — `zz_ef_hook_probe_calls`.
