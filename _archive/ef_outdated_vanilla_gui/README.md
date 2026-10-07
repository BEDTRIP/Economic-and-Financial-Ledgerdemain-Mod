# Устаревшие копии ванильных GUI (до 1.13)

**Что это:** E&F держал копии ванильных файлов (`gui/ef_dev_and_custom_windows/maj/NonEssential/{map_markers,
custom_tooltip,military_formation_panel,popups,right_click_menu}.gui`, `gui/frontend/shared/lists.gui`), которые
подменяли ванильные по имени файла / пути. Копии сняты с версии до 1.13: в них нет имён, которые ждёт ваниль 1.13
(`enemy_naval_mission_marker`, `dropdown_menu_round` …), — ошибки в `error.log` / `gui.log`.

**Почему вынесено:** сравнение с ванилью 1.13 (`tools/ld_vanilla_diff.py`, 7.10): строк с признаками E&F
(`GetScriptedGui`, `GetCustom`, `ScriptValue`, валюты, `ef`) — 0; отличия — старая раскладка ванили (у ванили 1.13 на
68–419 строк больше) и мелочи: `using = tooltip_above` в маркерах, закомментированный `tooltip` без ключа,
`visible` у статей договора `acquire_monopoly_for_company`, `minimumsize` выпадающего списка. Без файла грузится
ванильный 1.13.

**Удалено из живых файлов:** файлы целиком. **Вернуть:** взять ванильный файл 1.13 и внести нужную правку.
