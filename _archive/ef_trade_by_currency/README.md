---
type: code
description: "Торговля в разрезе 95 валют E&F: записи кнопки и подписи без читателя: кнопка игрока trade_balance_actualized (common/scripted_guis/09_ef_other.txt, кнопки в gui/ld_economy_panel.gui) кроме счётчиков торгового баланса записывала по каждой…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_trade_by_currency/**"]
---
# Торговля в разрезе 95 валют E&F: записи кнопки и подписи без читателя

**Что делало:** кнопка игрока `trade_balance_actualized` (`common/scripted_guis/09_ef_other.txt`, кнопки в
`gui/ld_economy_panel.gui`) кроме счётчиков торгового баланса записывала по каждой валюте импорт и экспорт в золоте —
`import_in_<cur>_in_gold_fix` и `export_in_<cur>_in_gold_fix` (95 + 95 блоков `if`). Их читали только ключи локализации
`<cur>_03_import_in`, `<cur>_03_import_in_gold`, `<cur>_03_export_in`, `<cur>_03_export_in_gold`, а эти ключи не
показывало ни одно окно.

**Почему вынесено:** очередь R8а, п. 8 (переменные «по одной на валюту» E&F — вместе с читателями); в прогоне
r1009_044350 — 190 «Variable … is set but is never used».

**Вырезано (текст — по тем же путям):**
- `common/scripted_guis/09_ef_other.txt`, `trade_balance_actualized`, эффект: 190 блоков `if = { limit = { money_value_<cur> > 0
  import_from_<cur> > 0 } set_variable = { name = import_in_<cur>_in_gold_fix … } }` (и `export_in_…`) с комментарием `#<cur>`
  над каждым; счётчики `trade_balance_in_gold_fixe`, `trade_balance_in_gold_delta_fix` и прочее в кнопке остались;
- `localization/<11 языков>/00_ef_gui_localization_l_<язык>.yml`: 384 ключа `<cur>_03_import_in`, `_import_in_gold`,
  `_export_in`, `_export_in_gold` (здесь — английский и русский).

Значения `import_in_<cur>` / `export_in_<cur>` остались: их читают `import_value_in_currency_week` и соседние суммы E&F.

**Вернуть:** блоки — в эффект `trade_balance_actualized`, ключи — в те же файлы локализации.

## R8в, шаг 6: торговля по валютам целиком

**Что делало:** значения `export_to_<cur>`, `export_in_<cur>`, `import_from_<cur>`, `import_in_<cur>` (по 95) читали
переменные `*_<cur>_fix`, а суммы `export_to_currency_sum`, `import_from_currency_sum`, `import_value_in_currency_week`,
`excess_foreign_state_currency_in_gold_week` складывали их в экспорт и импорт недели в золоте. Переменные `*_<cur>_fix`
только обнулялись (`trade_balance`, `new_country_var_ef_economy`) — никто их не писал, все значения были нулями; торговлю
считает модель (`zz_ef_trade_step`, Д.R1а.7).

**Вырезано:** 380 значений и 4 суммы (`common/script_values/01_economic_currency_scripted_value.txt`), 380 обнулений в
`trade_balance` (`01_economic_scripted_effects.txt`) и 380 в `10_new_country_var.txt`, ключи `<cur>_03_export_to`,
`<cur>_03_import_from` (190, их не показывало ни одно окно). Читатели сумм получили их значения: `export_to_gold`,
`import_from_gold` — без вычета нуля, `export_value_in_gold_week` — `export_in_gold`, `import_value_in_gold_week` —
`money_value_target_real` + `import_in_gold` (сумма недели была 1 + нули).
