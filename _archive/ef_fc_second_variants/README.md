# Вторые биржи страны: Манчестер, Чикаго, Гонконг (`building_financial_centre_gbr_2`, `_usa_2`, `_hkh`)

**Что делало:** варианты финцентра E&F — вторая биржа Британии (Ланкашир; Гонконг — Шаочжоу) и США (Иллинойс); появлялись
в истории поздних стартов (1861+), самосозданием E&F и по кнопкам расширения.

**Почему вынуто (R8б, шаг 4; Д.R8.7):** биржа одна на страну.

**Вырезано:** определения типов (`common/buildings/ef_16_financial_centre.txt`), типы модификаторов
`state_building_financial_centre_<x>_max_level_add`, значения `has_building_financial_centre_<x>(_custom_location)`,
эффекты `macro_facilities_fc_<x>`, скриптовые окна `financial_centre_<x>` и `_state` (здесь, по исходным путям).

**Удалено из живых файлов без копии:** записи `create_building` этих типов в `common/history/buildings/00_ef_building.txt`
(9, все — в блоках поздних дат); строки типов в `building_types` 11 типов компаний (`common/company_types/00_ef_companies.txt`:
банки США — `usa_2`, банки Британии — `gbr_2`, Гонконгский банк — `hkh`); значки в `gui/ld_cb_rate_panel.gui` (3 `icon`) и
виджеты штата в `gui/00_ef_deported_gui_1.gui` (3 `widget`); строки модификатора в
`common/static_modifiers/00_ef_dynamic_modifier_state.txt`; ключи локализации `building_financial_centre_<x>`,
`FINANCIAL_CENTRE_TITLE_<x>`, `state_building_financial_centre_<x>_max_level_add(_desc)`.
