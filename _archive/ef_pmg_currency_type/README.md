# Группа PM `pmg_currency_type` («Выпускаемая валюта»)

Скрытая группа метода производства ЦБ: `pm_no_currency_type` / `pm_currency_liquidity_currency` (выход
`goods_output_liquidity_currency_add` по занятости). В `building_bank` строка `#pmg_currency_type` была закомментирована,
больше ни одно здание группу не подключало; PM — только в этой группе. Интерфейса нет (в дублях `gui/ef_dev_and_custom_windows/maj/Essential/*`
имя встречается лишь в строковых сравнениях `EqualTo_string`, они безвредны).

**Удалено из живых файлов:**
- `common/production_method_groups/15_ef_bank.txt`: `pmg_currency_type = { production_methods = { pm_no_currency_type pm_currency_liquidity_currency } }`;
- `common/production_methods/15_ef_bank.txt`: баннер и определения `pm_no_currency_type`, `pm_currency_liquidity_currency` (237–276);
- `common/buildings/ef_15_bank.txt`: закомментированная строка `#pmg_currency_type ### Д2.5: no currency good from the central bank`;
- локализация (`localization/english`, `russian`, остальные — копии английской): `pmg_currency_type`, `pm_no_currency_type`, `pm_currency_liquidity_currency` из `01_ef_production_method_localization_l_<язык>.yml`.

**Вернуть:** вернуть блоки и ключи; чтобы заработало — добавить `pmg_currency_type` в `production_method_groups` здания.
