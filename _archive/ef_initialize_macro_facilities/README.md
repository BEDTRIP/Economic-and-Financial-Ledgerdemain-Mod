# Вызов `initialize_historic_macro_facilities_ns` (история зданий)

**Что делало:** в `history/buildings` для FRA/GBR/AUS/PRU/NET/CHI/BEL/USA/RUS (и `is_valid_country_hmm`) вызывался эффект
`initialize_historic_macro_facilities_ns = { STOCKPILE_SITE = capital }` — задумка: дать технологии `stockpiling_goods`/`national_stockpile`,
построить `building_national_stockpile` в столице и поставить `has_national_stockpile`, `stockpile_location`. Определение эффекта закомментировано
(в `09_introduction_building_lvl.txt`), вызов уходил в пустоту. **Переменные, интерфейс:** нет.

## Вырезано из живых файлов (текст — по тем же путям)
| файл | что |
| --- | --- |
| `common/history/buildings/00_ef_building.txt` | блок `if = { limit = { or = { c:FRA ?= this … c:RUS ?= this  is_valid_country_hmm = yes } }  initialize_historic_macro_facilities_ns = { STOCKPILE_SITE = capital } }` (внутри `BUILDINGS = { every_country = {`, после баннера NATIONAL STOCKPILE) |
| `common/scripted_effects/09_introduction_building_lvl.txt` | закомментированное определение `# initialize_historic_macro_facilities_ns = { … }` |
| `common/history/buildings/00_a_ef_history_var_init.txt` | абзац комментария «NOT FIXED HERE … not a fix» (говорил об этом вызове) |

**Вернуть:** вставить блок `if` на место и раскомментировать определение (здание `building_national_stockpile` в `common/buildings` проверить — на момент выноса файла с таким зданием в моде нет).
