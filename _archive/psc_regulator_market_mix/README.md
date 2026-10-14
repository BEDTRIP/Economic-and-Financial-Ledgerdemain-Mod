# Закупка регулятора стройки по рынку (`psc_regulator_market_mix`)

Вынуто 14.10.2026 (R9, шаг 4 — Д.R9.5, была Д.R8в.24). Механизм работал, но результат хуже — по правилу ночи откат.

**Что делал:** каждый метод регулятора брал по 10 единиц каждого из четырёх стройтоваров на очко, доли резали
модификаторы `zz_ef_reg_in_<товар>` (`goods_input_<стройтовар>_mult` — свои типы, у товаров мода их нет); доля товара
`var:zz_ef_reg_s_<товар>` штата — полшага в неделю к предложению рынка × (самая низкая местная цена / цена)²; базовая
цена смеси `var:zz_ef_reg_bp` — для модели цены PSC и веса штата; множители входа — локальные переменные штата
(`zz_ef_reg_market_step` в цикле штатов `set_construction_point_demand`, перед `state_construction_base_price`).

**Почему снят:** прогон всех шагов R9 со смесью r1014_193852 против того же кода без неё r1014_195947 (до 1841): очки
мира 1839 / 1840 / 1841 — 1023 / 1119 / 1163 против 1345 / 1423 / 1448 (−21 %), выпуск секторов (сейв 1841) 8,8 против
11,3 тыс., доля недель без трат у стран с секторами ~70 % против ~48 %; лучше — `gap_psc` −15,0 против −24,0 млн, железо
продажи / заказы 0,78 против 0,59, казна 75 против 54 млн. Очки идут по базовой цене смеси: дерево (база 130) дороже
железа (92), и переход на избыточное дерево дорожает в модели PSC. Вопрос — В.R9.11 (этапы/R9.md или история R9).

**Удалено из живых файлов:**
| файл | что |
| --- | --- |
| `common/scripted_effects/ld_construction_market.txt`, `common/script_values/ld_construction_market_values.txt`, `common/static_modifiers/ld_construction_market_modifiers.txt`, `common/modifier_type_definitions/ld_construction_market_modifier_types.txt`, `localization/*/ld_construction_market_l_*.yml` | файлы целиком (здесь — английский и русский; девять языков — копия английского) |
| `common/scripted_effects/PSC_scripted_effects.txt` | в цикле штатов после `set_construction_regulator_level = yes`: `if = { limit = { has_building = building_construction_regulator } zz_ef_reg_market_step = yes }` |
| `common/production_methods/zz_PSC_construction.txt` | в `pm_{wood,iron,steel,arc_welded}_point_conversion`: вход всех четырёх стройтоваров по 10 (осталось — свой товар) |
| `common/script_values/PSC_construction_values.txt` | в `calculate_state_construction_base_price`: первая ветка `if = { limit = { has_variable = zz_ef_reg_bp } value = var:zz_ef_reg_bp }` |

**Вернуть:** файлы — на место (локализация — `ld_loc_langs.py`), вызов, вход методов и ветку базовой цены — как в
таблице.
