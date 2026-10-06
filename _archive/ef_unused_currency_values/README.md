# Значения и триггер валют без ссылок

| файл (исходный путь) | ключ | что было |
| --- | --- | --- |
| `common/script_values/ld_reference_currency_values.txt` | `zz_ef_reserves_money` | `zz_ef_cb_money` + `zz_ef_fx_money` (сумма резервов; GUI её не читал) |
| то же | `zz_ef_tr_abr_overlap_neg`, `zz_ef_v_d_bonds_neg`, `zz_ef_v_d_tbonds_neg` | `zz_ef_tr_abr_overlap`, `zz_ef_v_d_bonds`, `zz_ef_v_d_tbonds` × −1 (знакопеременные копии для тултипа карточки банка; сами тултипы их не берут) |
| `common/script_values/ld_cb_rate_values.txt` | `zz_ef_cb_rule_rating_pp`, `zz_ef_cb_rule_stability_pp` | `zz_ef_cb_rule_rating` / `_stability` × 100 (проценты для подсказки) |
| `common/scripted_triggers/00_ef_custom_trigger.txt` | `is_valid_country_for_currency_accumulation` | не банкрот ЦБ, не в валютном кризисе, не владелец рынка с `market_owner_is_root_univ_with_buiding`, не подданный |

**Кто вызывал:** никто (refs=0 в индексе; grep по `common/ events/ gui/ localization/` пусто). **Переменные, интерфейс:** нет. **Удалено из живых файлов:** только эти определения.
**Вернуть:** вставить блоки обратно в исходные файлы.
