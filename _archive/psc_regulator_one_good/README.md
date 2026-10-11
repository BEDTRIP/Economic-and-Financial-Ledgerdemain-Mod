# Регулятор PSC на одном стройтоваре

**Что делал.** Регулятор стройки (`building_construction_regulator`) в каждом штате брал один стройтовар — тот, что
выпускает сектор стройки штата (без сектора — по технологии: сварные / стальные / чугунные / древесные). Для этого были
четыре метода `pm_{wood,iron,steel,arc_welded}_point_conversion` и переключатели: `set_new_point_conversion_method`
(сектор сменил метод или построен), `set_new_regulator_point_conversion_method` + `production_method_building_switch`
(создание регулятора с нужным методом), `set_point_conversion_method_from_tech` (технология). Базовая цена штата для
модели цены PSC была по методу регулятора (`calculate_state_construction_base_price`).

**Почему вынуто.** Д.R8в.24: регулятор покупает все четыре стройтовара по местной цене, делёж — по рынку
(`common/scripted_effects/ld_construction_market.txt`, `docs/construction.md`); базовая цена — смеси регулятора.

**Переменные:** `production_method_chosen` (штат) — номер метода для создания регулятора; в старых сейвах остаётся,
никто не читает.

**Удалено из живых файлов** (вырезанное — здесь по исходным путям):
- `common/production_methods/zz_PSC_construction.txt` — `pm_iron_point_conversion`, `pm_steel_point_conversion`,
  `pm_arc_welded_point_conversion`.
- `common/production_method_groups/PSC_construction.txt` — три строки этих методов в `pmg_construction_regulator`.
- `common/scripted_effects/PSC_scripted_effects.txt` — три эффекта выше; в `set_construction_regulator_level` вызов
  `set_new_regulator_point_conversion_method = yes`,
  `set_local_variable = { name = production_method_chosen value = var:production_method_chosen }` и
  `production_method_building_switch = { level = local_var:regulator_level production_methods = local_var:production_method_chosen }`
  заменены на `create_building` с `pm_wood_point_conversion`.
- `common/scripted_effects/PSC_production_method_building_switch.txt` — файл целиком.
- `common/on_actions/PSC_on_actions.txt` — `on_production_method_changed`, `on_acquired_technology`, `on_building_built`
  (подписки) и `on_construction_sector_method_changed`, `on_acquired_construction_tech`, `on_construction_sector_built`.
- `common/history/buildings/PSC_buildings.txt` —
  `b:building_construction_sector = { set_new_point_conversion_method = yes }` (в `if` по сектору) и
  `set_point_conversion_method_from_tech = yes`.
- `common/script_values/PSC_construction_values.txt` — старое тело `calculate_state_construction_base_price` (ключ жив с
  новым телом).
- Локализация `PSC_production_methods_l_{russian,english}.yml` — три строки методов («Базовый надзор»);
  `pm_wood_point_conversion` переименован в «Рыночная закупка стройматериалов».
