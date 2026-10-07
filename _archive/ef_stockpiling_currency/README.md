# Месячный пересчёт запасов валют E&F (`stockpiling_currency` → `stockpiling_currency_type_1`)

**Что делало:** раз в месяц у страны-владельца рынка с ЦБ (`central_bank_ef_on_monthly_pulse_country`) по каждой
валюте с `money_value_<cur> > 0` (95 веток `stockpiling_currency_type_1 = { currency = <cur> }`):
- своя валюта (закон `law_<cur>_currency`): запас ЦБ своей валюты `stockpiling_<cur>_state_1` столицы ЦБ += 4 × (продажи −
  покупки товара `liquidity_currency` на рынке) (при девальвации / ревальвации — плюс / минус `money_supply_to_add/
  subtract_per_month`), не ниже 0; счётчик населения `circulating_<cur>_c_var_1` += 4 × покупки того же товара;
- чужая валюта на своём рынке: резерв `stockpiling_<cur>_reserve_currency_state_1` += `export_in_<cur>`, долг
  `debt_in_national_currency_<cur>` += `import_in_<cur>` — оба счётчика торговли `trade_balance` держит в 0 (В2.1), так
  что эта ветка ничего не добавляла;
- `all_<cur>_stored` (столица ЦБ) = запас валюты.

**Почему вынесено:** решение пользователя 8.10 (Д.R2.4) — в архив, если от счётчиков не зависит курс. Не зависит: курс
на металле — `zz_ef_metal_value` (паритет × полоса покрытия ld: металл ЦБ и чужая валюта по `zz_ef_fx_reserves_metal`, M2
модели), на золотом обменном — запас эталонной (чужой) валюты, а эта ветка чужую не писала. Своя валюта ЦБ и
`circulating_<cur>_c_var_1` читаются только E&F: `money_supply_state` (прогнозы девальвации, панель ставки — показ,
кнопка `transfert_currency_to_investement_pool_button`), `pop_savings` (потери населения в экономическом кризисе E&F),
`<cur>_c_total_stokpile` (окно валют, порядок списка). Запас своей валюты из истории остаётся как был.

**Кто вызывал:** `central_bank_ef_on_monthly_pulse_country` (`common/scripted_effects/00_on_action_main.txt`), блок `if`
с `market_owner_is_root = yes`, перед `trade_balance = yes`.

## Вырезано (текст — по тем же путям)
- `common/scripted_effects/00_on_action_main.txt`: строка `stockpiling_currency = yes` (по описанию выше).
- `common/scripted_effects/01_economic_scripted_effects.txt`: `stockpiling_currency`, `stockpiling_currency_type_1`.

**Вернуть:** строку и определения — на место. По схеме — не возвращать: запас валюты ЦБ — зеркало регистра вкладов
(`zz_ef_nr_dep`), меняется проводками (R2, п. 1; клиринг — R8).
