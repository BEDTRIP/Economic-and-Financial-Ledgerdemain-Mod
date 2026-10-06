# Значения денежной модели без единой ссылки

**Что делали.** Формулы `script_values`, на которые не ссылался ни код, ни GUI, ни локализация (в том числе по строкам в `debug_log` и `ScriptValue('…')`).
**Кто вызывал.** Никто. **Переменные.** Читали `var:zz_ef_f_cc_issue/repay/int`, `var:zz_ef_d_cb`, `devaluation_on`, `revaluation_on` — их пишут другие живые места
(кредит потребителя, ЦБ); сами они остаются. **Интерфейс.** Нет.

**Что лежит здесь** — `common/script_values/ld_money_model_values.txt` (строки до правки, блоки подряд; в начале файла — диапазоны):
`zz_ef_pool_target`, `zz_ef_debt_cb_gold`, `zz_ef_cb_issue_month`, `zz_ef_cb_demand_others`, `zz_ef_cb_devaluation_month`,
`zz_ef_cb_revaluation_month`, `zz_ef_trade_week`, `zz_ef_v_d_cb`, `zz_ef_pop_savings_week`, `zz_ef_zero`, `zz_ef_agg_m0_gold`…`zz_ef_agg_m3_gold`,
`zz_ef_savings_gold`, `zz_ef_v_f_cc_issue/repay/int`, `zz_ef_cc_debt_to_gdp`, `zz_ef_bc_service_share`, `zz_ef_gov_rate_target_pp`;
осиротевшие после выноса: `zz_ef_credit_months`, `zz_ef_cb_demand_own`, `zz_ef_market_gdp_share`, `zz_ef_cb_demand_month`.

**Удалено из живых файлов.** Только эти определения; вызовов, GUI и локализации нет. `zz_ef_hume_metal_week` — в `ef_hume_money/`.
**Вернуть.** Вставить блоки обратно в `ld_money_model_values.txt`.
