# Товары национальных валют `<cur>_c`, их цвета и модификаторы; `bond_usa`

**Что делали:** E&F задумывал товар на каждую национальную валюту (95 штук: `dinar_c`, `dollar_united_states_dollar_c`, …) — в
`common/goods/ef_00_goods.txt` все блоки `INJECT_OR_CREATE:<cur>_c` закомментированы, товаров нет (страны без товара
валюты переводит на `law_no_market_liquidity` `history/global/zz_ef_currency_fix.txt`). Вокруг остались цвета и модификаторы.

**Вынесено:**
- `common/goods/ef_00_goods.txt` — строки 138–1089: закомментированные блоки 95 валют-товаров (`# #begin_tag_1 … # #end_tag_1`).
- `common/named_colors/00_ef_goods_colors.txt` — 95 цветов `<cur>_c` (`hsv360 { 45 100 95 }`); остались `silver`, `bond`, `manufacture_stock`,
  `agricultural_stock`, `mining_stock`.
- `common/modifier_type_definitions/00_ef_building_modifier_types.txt` — 300 типов `goods_input/output_<товар>_add/_mult` для несуществующих
  товаров (95 валют, `commodity_crates`, `paper_gold`, `construction_loans`, `war_bond`) — те, на которые нет ни одной живой ссылки.
  **Остались 96 имён** — их читает живой код: `modifier:goods_input_<cur>_c_add` в `base_demande_<валюта>` (`00_economic_scripted_value.txt`; читает
  `central_bank_modifier_fixed_var`) и `goods_input_war_bond_add` в PM `pm_government_aid_*` (`00_ef_market_liquidity.txt`).
- Локализация (`localization/english/`, `russian/`, `01_ef_modifier_type_localization_*.yml`): ключи вынесенных модификаторов (с `_desc`).
- `common/prestige_goods/00_ef_prestige_goods.txt` — `bond_usa` (база `bond`, ни одна компания не ссылается) и ключ `bond_usa`
  в `01_ef_prestige_goods_localization_*.yml`. В `other/ld_port_manifest.txt` строка об `bond_usa.dds` осталась (текстура на месте).

**Кто вызывал:** никто (кроме 96 оставшихся модификаторов, см. выше). **Переменные, интерфейс:** нет.
**Не тронуто:** ключи локализации `<cur>_c` (`dinar_c` и др.) и тексты-иконки `icon = <cur>_c` в `gui/00_ef_texticons.gui` — это не товары, а имена для
`[Localize('dinar_c')]` / `@dinar_c!` в локализации валют; запись `local_currency` в `popneed_currency` (товар определён, запись даёт попам вариант покупки).
**Вернуть:** вставить блоки в те же файлы (остальные языки — `python ../vic3_mods/tools/ld_loc_langs.py`).
