# Здание-пустышка E&F `building_ef_private_construction` и всё, что с ним связано

**Что делало:** E&F-овское здание «частный строительный сектор» (`ef_14_private_construction.txt`, группа `bg_ef_private_construction`, 4 PM
`pm_*_buildings_private`). В форке оно не строилось (`buildable = no`, `potential = always no`, `production_method_groups = {}`; PMG
`pmg_base_building_private_construction_sector` ниоткуда не подключена; все 28 ссылок истории переименованы на `building_construction_sector`).
Настоящую стройку ведёт PSC. Вокруг осталась обвязка, которая искала это здание.

**Кто вызывал:** `building_ef_private_construction_modifier` (месячный пульс ЦБ) — перебирал здания типа `building_ef_private_construction`
(no-op) и снимал/ставил `overbuilt_economy_modifier`; кнопки `speculative_share_9..12_button` (ветка ИИ, `visible = { always = no }`) и
`speculative_share_13_button` (сносила здание; из журнала снята). **Переменные:** нет (`speculative_share_2` ведёт `ld_pb_overbuild_counter.txt`).
**Интерфейс:** кнопка 13 в мёртвом виджете `widget_je_ef_pcs_fso_situation` (его не подключает ни один журнал; живой интерфейс — `ld_pb_fso_widgets.gui`).

## Вынесено целиком (`git mv`)
- `common/buildings/ef_14_private_construction.txt`
- `common/production_methods/14_ef_private_construction.txt` (`pm_wooden_/iron_frame_/steel_frame_/arc_welded_buildings_private`)
- `common/production_method_groups/14_ef_private_construction.txt` (`pmg_base_building_private_construction_sector`)

## Вырезано из живых файлов (текст — по тем же путям)
| файл | что |
| --- | --- |
| `common/scripted_effects/09_introduction_building_lvl.txt` | эффект `building_ef_private_construction_modifier` (строки 22923–22952) |
| `common/scripted_effects/00_on_action_main.txt` | вызов `building_ef_private_construction_modifier = yes` в `central_bank_ef_on_monthly_pulse_country` (строка 291, после `government_loan_month = yes`) |
| `common/scripted_buttons/00_ef_buttons.txt` | `speculative_share_9..12_button` (ветка ИИ) и `speculative_share_13_button` (строки 2331–2652) |
| `common/journal_entries/00_ef_financial_center_je.txt` | 4 строки `scripted_button = speculative_share_9_button` … `_12_button` (в `financial_center_je_2`, перед комментарием EF.18 v2) |
| `common/scripted_guis/00_financial_scripted_guis.txt` | sgui `speculative_share_13_button` (строки 6113–6142) |
| `common/scripted_guis/09_ef_other.txt` | sgui `no_PCS_growing_visibility` (его вызывал только блок виджета ниже) |
| `gui/scripted_widgets/00_ef_custom_widgets.gui` | обёртка `#No PCS growing` с кнопкой `#_13` в `widget_je_ef_pcs_fso_situation` (строки 627–677) |
| `common/static_modifiers/00_ef_dynamic_modifier_state.txt` | `building_ef_private_construction_max_level` |
| `common/static_modifiers/00_ef_dynamic_modifier_country.txt` | `speculative_share_modifier_7` (кулдаун кнопки 13) |
| `common/modifier_type_definitions/00_ef_state_modifier_types.txt` | `state_building_ef_private_construction_max_level_add` |
| `gui/00_ef_texticons.gui` | texticon `building_ef_private_construction` |
| `gfx/map/city_data/city_types/{african,arabic,asian,default,latin,southasian}_city.txt` | строка `building_ef_private_construction = {"generic_manufactory_03_mesh"}` |
| `localization/english/`, `russian/` | `01_ef_building_localization`: `building_ef_private_construction`; `01_ef_production_method_localization`: `pmg_base_building_private_construction_sector`, 4 ключа PM; `01_ef_je_localization`: `speculative_share_13_button`, `_desc`, `_tt_1`, `_tt`, `_tt_effect_1_1`, `speculative_share_modifier_7` |

## Изменено в живых файлах (не вынесено)
- Локализация `01_ef_je_localization` (`financial_center_je_2_reason_2`, `speculative_share_9..12_button_tt_2`) и `00_ef_gui_localization` (`alert_fso_alert_hint`):
  `GetBuildingType('building_ef_private_construction')` заменено на `GetBuildingType('building_construction_sector')` (так же уже сделано в `speculative_share_13_button_tt_1`).
  В игре в этих текстах вместо названия «Private Construction Sector» теперь название PSC-здания.
- Остались: скрипт-значения `building_ef_private_construction_lvl*` (их имя — историческое, считают `building_construction_sector`), группа
  `bg_ef_private_construction` и `bg_ef_private_construction_score` в `INJECT:building_financial_district` (правка ванильного здания), sgui `speculative_share_9..12_button`
  (кнопки игрока), текстура `gfx/interface/icons/building_icons/ef_private_construction.dds`, `gfx/interface/icons/timed_modifier_icons/ef_private_construction.dds`.

**Вернуть:** положить три файла на место, вставить блоки обратно, вернуть вызов; остальные языки — `python ../vic3_mods/tools/ld_loc_langs.py`.
Сохранения, где здание стоит, при загрузке дадут «unknown building» (в новой игре зданий нет).
