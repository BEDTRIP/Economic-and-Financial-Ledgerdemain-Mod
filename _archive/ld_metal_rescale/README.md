# Перемасштаб металла ЦБ на старте (`ld_metal_rescale`)

Вынуто 8.10.2026 (R1б.1, решения пользователя Д.1, Д.2; аудит R1б.0 — А3, А22). Хотфикс (версии паритета 7–8, Д2.13,
Д2.23): на первом недельном шаге паритет каждого металлического стандарта с ЦБ ставился ~1 (исторический — в
`zz_ef_parity_hist` для подписей), а металл ЦБ перемасштабировался к 40 % денег дважды — на 1-м шаге против ожидаемых
денег (`zz_ef_rescale_money`: норма накоплений + 0,33 ВВП) и на 12-й неделе против самих денег
(`zz_ef_metal_rescale_due`), по оценке покрытия `zz_ef_cb_cover_ref` (ёмкость E&F / деньги / паритет). В игре фунт падал
с 7,31 до 1 золота; первые 13 недель держали обходки (ИИ-политика, премия, зона, клиринг металлом).

Стало: паритет — исторический E&F (курс и подписи), металл в деньгах движка — по постоянной `zz_ef_metal_per_money`;
металл ЦБ = 40 % M2 один раз (`zz_ef_cb_metal_start_step`, `docs/money-model.md`).

## Удалено из живых файлов
| файл | что |
| --- | --- |
| `common/scripted_effects/ld_money_model.txt` | `zz_ef_metal_rescale_step` (весь); в `zz_ef_money_model_step` — блок версий паритета 7–8 (`zz_ef_parity_version` = 8, `zz_ef_metal_rescale_due` = 11, перемасштаб на 12-й неделе) — заменён стартом версии 9 |
| `common/script_values/ld_money_model_values.txt` | `zz_ef_rescale_money` (заменено `zz_ef_start_money` без условия), `zz_ef_cb_cover_ref` |
| `common/scripted_effects/ld_metal_accounts.txt` | в `zz_ef_metal_start_step` — паритет ~1 (`money_value_target_1` = 1 / `gold_to_silver_rate`, `zz_ef_parity_hist`), вызов `zz_ef_metal_rescale_step`, обнуление металла E&F у стран без ЦБ (теперь — населению); текст — в git (`R1б, шаг 5`) |
| `common/scripted_effects/ld_monetary_policy.txt`, `ld_risk_premium.txt`, `ld_currency_zone.txt`, `script_values/ld_metal_accounts_values.txt`, `scripted_effects/ld_nr_deposits.txt` | условия `zz_ef_weeks_run >= 13` и `zz_ef_metal_rescale_due` (правила металла ЦБ и ИИ-политика ждут `zz_ef_cb_start_due`; вклады чужих ЦБ — с первого шага) |

Тексты `zz_ef_metal_rescale_step`, блока версий и значений — здесь, по исходным путям.

## Как вернуть
Не возвращать: старт в балансе — решение пользователя 7.10 («не хотфикс, а свой мод»). Старый сейв (версия 8) с
`zz_ef_metal_rescale_due` доводит старт через `zz_ef_cb_start_due`.
