# Тестовые окна E&F и дубли `maj/`

**Что делало.** `gui/ef_dev_and_custom_windows/ef_custom_windows.gui` (56 тыс. строк) — 83 `default_popup`. Живое окно одно —
`gold_reserve_window` (оно осталось в файле, строки 1–2835; открывается из `ld_economy_panel.gui` через
`gui.createwidget gui/ef_dev_and_custom_windows/ef_custom_windows.gui gold_reserve_window`). Вынесены: `currency_reserve_window`
(кнопка открытия закомментирована), хаб `ef_custom_windows` (кнопки открытия тестовых окон) и 80 тестовых окон `panel_1`…`panel_20`,
`panel_L`, `panel_1_1`…`panel_1_20`, `panel_2_1`…`panel_2_20`, `panel_3_1`…`panel_3_20` (переменные-образцы `variable_test_var_2`, строки
`-----`; в них нет ни одного вызова, который писал бы данные для живого кода).
Хаб открывала кнопка «1» вкладки «Экономика» (`ld_economy_panel.gui`, условие показа закомментировано — видна всем игрокам).
Дубли `maj/`: те же типы объявлены в корневых файлах мода с тем же именем, корень выигрывает у подкаталога.

**Кто вызывал.** Только кнопка «1» (хаб) и закомментированная кнопка `currency_reserve_window`; панели `panel_*` открывал хаб.
**Переменные.** GUI-флаги `GetVariableSystem`: `my_ef_custom_windows`, `currency_reserve_window`, `panel_*`. Скрипт их не видел.

**Удалено из живых файлов**
- `gui/ef_dev_and_custom_windows/ef_custom_windows.gui` — строки 2837–56149 (всё после `gold_reserve_window`).
- `gui/ld_economy_panel.gui` — строки 41–76: блок `#E&F debug` (`flowcontainer` с `button_icon_round` `name = "Panel_1"`, текст «1»,
  `onclick` → `gui.createwidget … ef_custom_windows` + `Toggle('my_ef_custom_windows')`; закомментированный `visible = GetScriptedGui('EF_debug_mode_visibility')…`);
  строки 7085–7112 (в окне резервов: закомментированные `divider_decorative` и `button_icon_square` «currency_reserve_window»).
  Файл ведёт генератор `regen_ef_economy_panel_gui.py` — правка внесена и в живой файл; генератору нужна та же правка (оркестратор).
- файлы целиком: `gui/ef_dev_and_custom_windows/maj/Essential/{budget_panel,market_panel,states_panel}.gui`,
  `gui/ef_dev_and_custom_windows/maj/NonEssential/companies_panel.gui` (дубли корневых `gui/{budget,market,states,companies}_panel.gui` с тем же именем файла).
- локализация (en + ru): `currency_reserve_window`, `show_currency_reserve_window` (`00_ef_gui_localization`);
  `TOOLTIP_FOREIGN_COLLATERAL`, `TOOLTIP_FOREIGN_COLLATERAL_player` (`01_ef_tooltips_localization`; использовались только в `panel_1_14`).

**Осталось, потому что живое:** `gold_reserve_window`; `maj/Essential/building_details_panel.gui` (у него нет одноимённого в корне —
подменяет ванильный `building_details_panel.gui`; `00_MPM_building_details_panel.gui` объявляет только 3 типа из 50); остальные файлы `maj/`.

**Вернуть:** положить файлы по исходным путям; вставить блоки в `ef_custom_windows.gui`/`ld_economy_panel.gui` по строкам из заголовков; ключи локализации — в исходные файлы.
