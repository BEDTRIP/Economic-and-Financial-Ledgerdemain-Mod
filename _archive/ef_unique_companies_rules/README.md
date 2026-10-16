# Правила игры E&F «уникальные компании» (`unique_companies_banks`, `unique_companies_newspapers`)

**Что делало:** `TRY_REPLACE:` двух правил игры — по умолчанию `banks_disabled` / `newspapers_disabled` с флагами того
же имени. Видимо, рассчитано на мод «Unique Companies», которого в наборе нет.

**Почему вынесено (R12 Л.8, 17.10):** `TRY_REPLACE` записи, которой нет ни в ванили, ни в модах набора (`v3 def
unique_companies_banks` — одно определение, это), ничего не создаёт; флаги `banks_disabled` / `newspapers_disabled`
никто не читает (`v3 refs` — только сам файл). В игре правило не появлялось.

**Удалено из живых файлов:** файл `common/game_rules/00_EF_unique_companies_game_rules.txt` целиком (здесь); строки в
`docs/exchange-companies.md`, `docs/ef-core.md`, `docs/mechanisms.md`. **Вернуть:** вернуть файл, если в набор войдёт
мод с этими правилами.
