# Рабочие остатки автора E&F

Файлы, которые лежали в папках игры, но игровым кодом не были.

| файл (исходный путь) | что это | почему мёртвый |
| --- | --- | --- |
| `common/scripted_effects/test.txt` | один блок `every_scope_state = { … }` (2667 строк, по валютам: `owner = { … }` → переменные запаса) — набросок, а не определение эффекта | движок читает его как скриптовый эффект с именем встроенного итератора `every_scope_state`; вызвать его так нельзя (имя занято встроенным), тело не выполнялось |
| `gui/ef_dev_and_custom_windows/00_ef_dev_tips.gui` | заметки автора по-французски (89 строк без `#`) | не GUI-код; парсер GUI их пропускал с ошибками |
| `localization/english/01_ef_currency_name_localization_l_english.yaml` | дубль `01_ef_currency_name_localization_l_english.yml` (601 строка) | игра `.yaml` не грузит |
| `common/history/global/update new country/nw_*.py` (4) | генераторы автора: копировали блоки `#begin_copy…#end_copy` из `history/global/*` в `common/scripted_effects/10_new_country_var.txt` (пути Windows автора) | Python, игра не читает; `10_new_country_var.txt` дальше правится руками / генераторами `vic3_mods` |

**Кто вызывал:** никто. **Переменные, интерфейс:** нет. **Удалено из живых файлов:** ничего (перенесены целиком).
**Вернуть:** положить по исходному пути (для `test.txt` — оформить как `name = { … }` и вызвать).
