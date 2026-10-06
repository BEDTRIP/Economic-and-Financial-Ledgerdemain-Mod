# `central_bank_production_methods`, `_3`, `_4` (ПМ «потребления металла» банка)

**Что делало:** переключало ПМ `building_bank` по закону денежной системы / валюте подданного: `pm_silver_consuption`, `pm_gold_consuption`, `pm_bimetallism_consuption`,
`pm_no_metal_consuption`, `pm_no_subject_currency_type`, `pm_no_gold_consuption`, `pm_subject_currency_<cur>_currency`. Этих ПМ нет (группы ПМ `pmg_monetary_system`/`pmg_subject_currency_type`
скрыты, комментарий «suppression suite à trop de bug»): каждое условие `is_production_method_active` было ложным, каждый `activate_production_method` — ошибкой; тела ничего не делали.
`_3` (2379 строк) нигде не вызывался, `_4` вызывается из `central_bank_ef_on_yearly_pulse_country`.

## Вырезано (текст — по тем же путям)
- `common/scripted_effects/01_economic_scripted_effects.txt`: тела трёх эффектов; в живом файле остались **пустые определения** `central_bank_production_methods`, `_3`, `_4`
  (их зовут: `central_bank_production_methods` — `00_on_action_main.txt`, `01_economic_scripted_effects.txt`, `01_financial_scripted_effects.txt`, `09_introduction_building_lvl.txt`,
  `99_ef_history_global_variable.txt`, `events/00_ef_economic_event.txt`, `scripted_guis/00_economic_scripted_guis.txt`; `_3` — `00_on_action_main.txt`, `09_introduction_building_lvl.txt`; `_4` — `01_economic_scripted_effects.txt`).
- `common/scripted_triggers/00_ef_custom_trigger.txt` (не вынос, правка): `market_owner_is_root_univ_with_buiding` — убран `not = { is_production_method_active pm_no_subject_currency_type }`;
  `bank_central_buiding_no_external_currency_consuption` — тело заменено на `always = no`.

**Вернуть:** тела — на место; для работы нужны ПМ и их группы в `building_bank`.
