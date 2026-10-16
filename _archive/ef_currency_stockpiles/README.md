# Запасы валют E&F в штатах (R9б.5)

Товар-валюта E&F копился запасом в штатах: `stockpiling_<валюта>_state_1` (обращение) и
`…_reserve_currency_state_1` (резерв) в штате ЦБ; сумма по стране — `stockpiling_<валюта>_state`, своей валюты —
`money_supply_state`. Модель форка их не читает (курс — паритет и M2; Д.R9б.15). Снимается кусками (R9б.5б),
вырезанное — сюда по исходным путям.

## Вырезано

- `common/script_values/01_economic_currency_scripted_value.txt` — `reference_currency_owned_by_the_country` (668 строк:
  запас валюты-эталона страны по 95 валютам). Его читал только `reference_currency_in_gold_fixe`
  (`01_economic_scripted_effects.txt`) — для перехода ИИ на золотодевизный стандарт
  (`is_monetary_systeme_transition_valid_country_to_gold_exchange_standard`). Заменено (Д.R9б.15): требования ЦБ
  страны к эмитенту-эталону (карта `zz_ef_rq_cb_m`, деньги эмитента).

## Удалено из живых файлов

- `reference_currency_in_gold_fixe`: `set_variable = { name = reference_currency_owned_by_the_country_fixe value =
  reference_currency_owned_by_the_country }` → чтение `zz_ef_rq_cb_m` по стране с `global_monetary_reference`.

## Вернуть

Значение — на место (`01_economic_currency_scripted_value.txt`, после `currency_no_own`); в
`reference_currency_in_gold_fixe` — прежний `set_variable`.
