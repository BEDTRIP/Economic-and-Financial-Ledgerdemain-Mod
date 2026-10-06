# Осиротевшее после выноса мёртвых GUI (script_values, эффекты, sgui)

**Что это.** Определения, на которые ссылались только вынесенные блоки (`ef_unused_scripted_guis`, окна `ef_dev_custom_windows`, отладка `ef_debug_mode`, `ef_gui_dead_leftovers`);
после выноса у них `refs=0` (несколько кругов пересчёта `ld_index`, пока осиротевшее не кончилось). Динамических ссылок нет.

**Вынесено** (тот же путь в архиве):
- `common/script_values/00_economic_scripted_value.txt` — 88 определений; `00_financial_scripted_value.txt` — 22; `00_stockpile_scripted_value.txt` — 3; `01_economic_currency_scripted_value.txt` — 2.
- `common/scripted_effects/08_list_effect.txt` — 24 эффекта `test_*_c_global_stokpile_variable_list` (`test_XXX_…`, `test_1_…`…`test_23_…`; вызывались только из вынесенных sgui).
- `common/scripted_guis/09_ef_other.txt` — 35 (`gold_N_silver_M`, `PCS_growing_visibility`); `00_economic_scripted_guis.txt` — 2 (`test_execute`, `PL_actualize`).
**Кто вызывал:** только вынесенное. **Не тронуто:** `economic_sentiment_index_*` (EF.31).

**Вернуть:** вернуть вместе с механизмом, который их вызывал (`ef_unused_scripted_guis/`).
