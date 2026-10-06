# Закомментированные алерты `buy_sell_<товар>_order` (29)

**Что делали:** алерты игроку «приказ покупки/продажи товара будет исполнен» (`valid`: `var:buy_<good>_1`/`var:sell_<good>_1`, `open_panel = market|msa`). Все 29 блока в файле закомментированы
(строки 92–613), локализация осталась. Живые алерты файла — `fso_alert`, `selle_bond_maturity_yers_time_*`, `store_release_<good>`.

## Вырезано (текст — по тем же путям)
- `common/alert_types/00_ef_alert_types.txt`: 29 закомментированных блоков `# buy_sell_<good>_order = { … }`.
- `localization/{english,russian}/00_ef_gui_localization_l_*.yml`: 87 ключей `alert_buy_sell_<good>_order_{name,hint,action}`.
