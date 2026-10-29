---
type: code
description: "Запас своей валюты ЦБ E&F в штате (`stockpiling_<валюта>_state_1`): E&F держит в штате ЦБ (var:central_bank_location) собственный запас валюты страны — stockpiling_<валюта>_state_1 и …_reserve_currency_state_1 (невыпущенные деньги ЦБ);…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_currency_stockpiles/**"]
---
# Запас своей валюты ЦБ E&F в штате (`stockpiling_<валюта>_state_1`)

**Что делал.** E&F держит в штате ЦБ (`var:central_bank_location`) собственный запас валюты страны —
`stockpiling_<валюта>_state_1` и `…_reserve_currency_state_1` (невыпущенные деньги ЦБ); их сумма — `money_supply_state`
(`01_economic_currency_scripted_value.txt`). Модель денег форка этот запас не ведёт: его читают только счёт `cb` сверки
(`ld_money_model.txt`, `zz_ef_money_ledger_delta = { ACC = cb VALUE = money_supply_state }`), карточка ЦБ, панели и
значения E&F (разведка — `docs/история/2026-10-17 этап R9б.md`, R9б.5а). Снимается кусками (R9б.5); здесь — снятое.

## Кусок 1 — старт (история)

`common/history/global/99_ef_history_global_variable.txt` у 35 исторических стран клал в штат ЦБ 10 % обращения:

```
var:central_bank_location ?= {
	change_variable = {
		name = stockpiling_<валюта>_state_1
		add = { value = owner.var:circulating_<валюта>_c_var_1 multiply = 0.1 }
	}
	...
```

Вырезанные блоки — `common/history/global/99_ef_history_global_variable.txt` здесь (с номерами строк старого файла).
Стартовый металл ЦБ в той же истории (`gold_state_1` / `silver_state_1`) читал запас слагаемым
`add = var:stockpiling_<валюта>_state_1` — 41 место (строки старого файла 108, 168, 179, 220, 231, 289, 305, 314, 356, 366, 406, 416, 456, 502, 556, 605, 654, 703, 752, 801, 850, 899, 948, 997, 1046, 1095, 1144, 1193, 1242, 1291, 1340, 1389, 1438, 1487, 1536, 1585, 1634, 1683, 1732, 1781, 1830); теперь там та же доля прямо:
`add = { value = owner.var:circulating_<валюта>_c_var_1 multiply = 0.1 }`, металл на старте тот же.

**Удалено из живых файлов** (`99_ef_history_global_variable.txt`, строки старого файла):

| строки | переменная |
| --- | --- |
| 98-103 | `stockpiling_pound_sterling_state_1` |
| 157-163 | `stockpiling_franc_french_franc_state_1` |
| 209-215 | `stockpiling_dollar_united_states_dollar_state_1` |
| 278-284 | `stockpiling_gulden_florin_state_1` |
| 345-351 | `stockpiling_gulden_state_1` |
| 395-401 | `stockpiling_spe_ruble_state_1` |
| 445-451 | `stockpiling_thaler_prussian_thaler_state_1` |
| 491-497 | `stockpiling_spe_yuan_state_1` |
| 545-551 | `stockpiling_dollar_canadian_dollar_state_1` |
| 594-600 | `stockpiling_dollar_canadian_dollar_state_1` |
| 643-649 | `stockpiling_dollar_australian_dollar_state_1` |
| 692-698 | `stockpiling_rupee_indian_rupee_state_1` |
| 741-747 | `stockpiling_mark_finnish_markka_state_1` |
| 790-796 | `stockpiling_rupee_indonesian_rupiah_state_1` |
| 839-845 | `stockpiling_gulden_south_german_gulden_state_1` |
| 888-894 | `stockpiling_thaler_hannoveraner_thaler_state_1` |
| 937-943 | `stockpiling_thaler_saxon_thaler_state_1` |
| 986-992 | `stockpiling_gulden_bavarian_gulden_state_1` |
| 1035-1041 | `stockpiling_franc_swiss_franc_state_1` |
| 1084-1090 | `stockpiling_franc_belgian_franc_state_1` |
| 1133-1139 | `stockpiling_krone_danish_krone_state_1` |
| 1182-1188 | `stockpiling_spe_drachma_state_1` |
| 1231-1237 | `stockpiling_dinar_qiran_state_1` |
| 1280-1286 | `stockpiling_real_state_1` |
| 1329-1335 | `stockpiling_lira_toscane_lira_state_1` |
| 1378-1384 | `stockpiling_lira_scudo_pontificio_state_1` |
| 1427-1433 | `stockpiling_lira_scudo_sardo_state_1` |
| 1476-1482 | `stockpiling_lira_ducato_state_1` |
| 1525-1531 | `stockpiling_krone_swedish_krona_state_1` |
| 1574-1580 | `stockpiling_peso_bolivien_peso_state_1` |
| 1623-1629 | `stockpiling_peso_bolivien_peso_state_1` |
| 1672-1678 | `stockpiling_real_brazilian_real_state_1` |
| 1721-1727 | `stockpiling_peso_mexican_peso_state_1` |
| 1770-1776 | `stockpiling_spe_peseta_state_1` |
| 1819-1825 | `stockpiling_lira_ottoman_lira_state_1` |

**Вернуть:** вставить блоки обратно под `var:central_bank_location ?= {` своей страны (перед блоком `gold_state_1` /
`silver_state_1`) и в 41 месте заменить долю на `add = var:stockpiling_<валюта>_state_1`.

Не снято (живое): заведение переменных нулём у новых стран (`10_new_country_var.txt`), перенос запаса при переезде
финцентра и кризисы (`01_economic_scripted_effects.txt`), `money_supply_state` и счёт `cb`, кнопки
`00_financial_scripted_guis.txt`.

## Кусок 2 — перенос при переезде столицы и оккупации

`common/scripted_effects/01_economic_scripted_effects.txt`: из `stockpiling_capital_state_transfert` (переезд столицы /
места ЦБ), `stockpiling_capital_state_transfert_financial_center_place` и `enemy_capital_is_occuped` (оккупация
столицы) вырезаны 475 блоков `change_variable` / `set_variable` запасов **валют** (`stockpiling_<валюта>_state_1`,
`…_reserve_currency_state_1`; 95 валют — у которых есть `_reserve_currency`) — сюда, тем же путём. Запасы товаров
нацзапаса (`stockpiling_<товар>_state_1`, R13), металл (счёт страны), `all_<валюта>_stored`, грабёж — на месте. После
куска 1 запасы валют всегда 0 — перенос ничего не двигал. Вернуть — блоки на прежние места в этих эффектах (порядок
в файле архива — порядок в эффекте).

## Запас валюты-эталона (Д.R9б.15)

### Вырезано

- `common/script_values/01_economic_currency_scripted_value.txt` — `reference_currency_owned_by_the_country` (668 строк:
  запас валюты-эталона страны по 95 валютам). Его читал только `reference_currency_in_gold_fixe`
  (`01_economic_scripted_effects.txt`) — для перехода ИИ на золотодевизный стандарт
  (`is_monetary_systeme_transition_valid_country_to_gold_exchange_standard`). Заменено (Д.R9б.15): требования ЦБ
  страны к эмитенту-эталону (карта `zz_ef_rq_cb_m`, деньги эмитента).

### Удалено из живых файлов

- `reference_currency_in_gold_fixe`: `set_variable = { name = reference_currency_owned_by_the_country_fixe value =
  reference_currency_owned_by_the_country }` → чтение `zz_ef_rq_cb_m` по стране с `global_monetary_reference`.

### Вернуть

Значение — на место (`01_economic_currency_scripted_value.txt`, после `currency_no_own`); в
`reference_currency_in_gold_fixe` — прежний `set_variable`.
