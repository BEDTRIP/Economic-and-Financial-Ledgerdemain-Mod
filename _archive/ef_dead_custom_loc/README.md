# Мёртвая customizable_localization E&F

**Что это.** 1237 определений `customizable_localization` (13,8 тыс. строк) в
`common/customizable_localization/00_ef_localization_ custom.txt`, на которые нет ни одной ссылки в моде (`ld_index.py`:
refs = 0; динамических имён `GetCustom(Concatenate(…))` в моде нет). Семейства: `currency_symbol_<cur>_mk`,
`currency_good_<cur>_mk`, `currency_<TAG>_N_<cur>_mk`, `buy/sell_<cur>_in_progress_N` и др. — остатки окон E&F, которые
форк не показывает. Решение — В3 (пользователь 8.10).

**Вырезано:** записи целиком — `common/customizable_localization/00_ef_localization_ custom.txt` (по тому же пути здесь).

**Удалено из живых файлов:** ничего — ссылок не было.

**Вернуть:** вставить записи обратно в файл (порядок неважен).
