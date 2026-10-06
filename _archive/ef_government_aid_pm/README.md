# Военные PM `pm_government_aid_*` (5) и тип модификатора `goods_input_war_bond_add`

**Что делали:** пять PM «заказа правительства» для военных зданий (`pm_government_aid_building_arms_industry_0/_1`, `_munition_industry`, `_tank_industry`,
`_shipbuilding_industry`): вход `goods_input_war_bond_add` (товара `war_bond` нет), выход вооружения. Ни одна PMG/здание их не подключает (grep по `common`).
`goods_input_war_bond_add` читали только они — после выноса PM осиротел. **Переменные, интерфейс:** нет.

## Вырезано (текст — по тем же путям)
| файл | что |
| --- | --- |
| `common/production_methods/00_ef_market_liquidity.txt` | пять PM; две строки `pm_government_aid_building_arms_industry_1`/`_0` из `unlocking_production_methods` PM `pm_privately_owned_building_arms_industry` |
| `common/modifier_type_definitions/00_ef_building_modifier_types.txt` | `#war_bond` + `goods_input_war_bond_add={ decimals=1 color=bad game_data={ ai_value=0 } }` |
| `localization/{english,russian}/01_ef_modifier_type_localization_l_*.yml` | `goods_input_war_bond_add`, `goods_input_war_bond_add_desc` |
| `localization/{english,russian}/01_ef_production_method_localization_l_*.yml` | закомментированный раздел `## War industry PM` (5 ключей названий) |

**Не вынесено:** `pm_privately_owned_building_arms_industry` (остаётся в `00_ef_market_liquidity.txt`): ни в одной PMG, но имя совпадает с ванильным PM арсенала и содержит
`unlocking_production_methods` на ванильные ПМ — вероятно, переопределение ванили; без ванильных файлов не проверить.
