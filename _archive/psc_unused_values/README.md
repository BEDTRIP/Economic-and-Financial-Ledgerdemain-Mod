# Значения PSC без ссылок

**Что делали:** скрипт-значения PSC, которые ни один файл форка не читает (проверено grep по `common/ events/ gui/ localization/`, `define:`
и GUI не используют).

| значение | файл |
| --- | --- |
| `command_economy_spending_mult` (1,5), `oversupply_limit` (1,5), `state_oversupply_limit` (1,05), `construction_price_weeks` (12) | `common/script_values/PSC_set_values.txt` |
| `construction_sector_efficiency_multiplier` (корень из максимального уровня сектора, `#Scope: Country`) | `common/script_values/PSC_construction_values.txt` |

**Кто вызывал:** никто. **Переменные, интерфейс:** нет. **Удалено из живых файлов:** только сами определения (вызовов не было).
Помощник `calculate_construction_sector_max_level` остался: его читает живое значение в том же файле.
**Вернуть:** вставить блоки из архивных файлов обратно.
