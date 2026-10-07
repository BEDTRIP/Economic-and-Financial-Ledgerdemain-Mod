# Потребности населения и товары
Население покупает товары-«деньги» (`liquidity_currency` / `local_currency`), финансовые продукты (облигации, акции четырёх видов, паевые фонды, золото и серебро), металлы-накопления и строительные товары PSC. Потребности вешаются на ванильные пакеты покупок `wealth_1..wealth_99` через `INJECT`; цены и объёмы задают числа в `buy_packages`, а набор товаров — потребность (`pop_needs`).

## Файлы
- `common/pop_needs/00_ef_pop_needs.txt` — E&F: потребности `popneed_currency` (по умолчанию `liquidity_currency`; `local_currency` с весом 0,25, `liquidity_currency` — 1) и `popneed_financial_products` (по умолчанию `bond`; `bond`, `manufacture_stock`, `agricultural_stock`, `mining_stock`, `railroad_stock`, `mutual_funds` — вес 1; `gold`, `silver` — 0,5, `max_supply_share` 0,5).
- `common/pop_needs/ld_household_construction.txt` — `popneed_household_construction` (домохозяйства и городские центры берут `wood_construction`, `iron_construction`, `steel_construction`, `arc_welded_construction`, вес 1; генератор `tools/regen_ef_household_construction.py`, руками не править). Описана в PSC/ld-подсистемах.
- `common/pop_needs/ld_metal_hoard.txt` — `popneed_metal_hoard` (серебро по умолчанию; `silver` и `gold` с весами 0,5; генератор `tools/regen_ef_metal_hoard.py`). Описана в подсистеме модели денег.
- `common/buy_packages/00_ef_buy_packages.txt` — 99 строк `INJECT:wealth_N={goods={...}}`, N = 1..99 (уровень достатка), по одной строке на уровень.
- `common/goods/ef_00_goods.txt` — товары E&F: `INJECT:gold` (торгуемый, `fixed_price = no`, `traded_quantity = 5`), `silver`, `bond`, `manufacture_stock`, `agricultural_stock`, `mining_stock`, `railroad_stock`, `mutual_funds` (не торгуется, фикс. цена 250), `local_currency` (`tradeable = no`, `local = no`), `liquidity_currency` (торгуемый).
- `common/goods/PSC_goods.txt` — PSC: `wood_construction`, `iron_construction`, `steel_construction`, `arc_welded_construction`.
- `common/named_colors/00_ef_goods_colors.txt` — цвета товаров для GUI: `silver`, `bond`, `manufacture_stock`, `agricultural_stock`, `mining_stock`.
- `common/prestige_goods/00_ef_prestige_goods.txt`, `00_ef_prestige_goods_2.txt` — 13 престижных вариантов товаров (`prestige_good_mexican_silver`, `prestige_good_russian_gold`, `prestige_good_usa_oil`, `manufacture_stock_{construction,gbr,gbr_2}` (`manufacture_stock_usa` выключен: предел движка — три на товар), `agricultural_stock_rus`, `mining_stock_{usa,aus}`, `railroad_stock_{usa,fra,ger,rus}`); подключаются в `common/company_types/00_ef_companies.txt` (`possible_prestige_goods`).

## Поток / порядок
Расчёта по on_action нет: движок каждую неделю считает покупки попов по пакету их уровня достатка. Строка `wealth_N` содержит записи:
- `popneed_currency = X` — потребность в деньгах (банковские расчёты `liquidity_currency`): 0,07 от значения E&F (от 1 на уровне 1 до 432 на уровне 99; спрос населения ~2% ВВП, решение Д2.2). Ключ в строке один: повторы одного ключа в `goods` движок складывает.
- `popneed_household_construction = Y` — строительные товары, во всех 99 уровнях (7 → 38438).
- `popneed_metal_hoard = Z` — металлы-накопления, уровни 5–14 (2 → 10), и в строках 1–4 и 15–99 отсутствует.
- `popneed_financial_products = F` — финпродукты, начиная с уровня 15 (40 → 360556 на 99).
Цепочка: `liquidity_currency` производят банки (`production_methods/ld_bank_pm.txt`, `ld_trade_center_settlements.txt`) и покупают здания (`pm_market_liquidity_currency`, вход 28) и попы; `bond`/акции производят ПМ владения (`goods_output_<stock>_add` в `production_methods/01..03/11_ef_*`) и покупают фин. центры (`16_ef_financial_centre.txt`, вход `goods_input_*_stock_add`); `mutual_funds` — выход `pm_bond_exchange`, не торгуется.

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `wealth_1..99` (ванильный ключ пакета) | пакет покупок попов уровня достатка | `INJECT` в `00_ef_buy_packages.txt` (+ PSC/ld-вставки в других файлах) | движок |
Своих переменных у подсистемы нет.

## Вызовы и связи
- Товары `bond`/акции/`mutual_funds`/`liquidity_currency` участвуют в модели `ld_*` (клиринг, листинг, капитализация, массовое владение акциями `script_values/ld_mass_shareholding_values.txt`, грамотность `ld_stock_issue_literacy_values.txt`).
- Для каждого товара в `modifier_type_definitions/00_ef_building_modifier_types.txt` заведены `goods_input_<good>_add/_mult`, `goods_output_<good>_add/_mult` (134 имени: 38 — на 10 живых товаров, 96 — на несуществующие товары (национальные валюты `<cur>_c`, `war_bond`), их читают значения `base_demande_<валюта>` (`modifier:goods_input_<cur>_c_add` в `00_economic_scripted_value.txt`) и PM `pm_government_aid_*`).
- Закон/валюта: `laws/01_ef_currency_type.txt:1888` помечает `spe_uni_c` как «внутренний по умолчанию `popneed_currency`».
- Локализация: `01_ef_goods_localization_l_*.yml`.
- GUI: рынок и панели товаров E&F берут цвета из `00_ef_goods_colors.txt`.

## Логи
Нет.
