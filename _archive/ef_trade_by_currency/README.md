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
