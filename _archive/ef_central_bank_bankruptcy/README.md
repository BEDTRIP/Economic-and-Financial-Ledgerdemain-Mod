# Банкротство ЦБ E&F (`central_bank_bankruptcy`)

**Что делал.** Месячный эффект модификаторов валюты (`01_economic_scripted_effects.txt`) при `extreme_weak_currency`
(E&F: ценность денег в золоте < 0,01 или уже банкрот) у страны с ЦБ на металле звал `central_bank_bankruptcy`
(`01_financial_scripted_effects.txt`): паритет `money_value_target_1` пополам, `var:central_bank_bankruptcy = 1`,
`economic_instability`. Признак `var:central_bank_bankruptcy >= 1` сам входил в `is_extreme_weak_currency` — страна
оставалась «банкротом» навсегда (Австрия, Ганновер: `EFC|…|issuer|crisis 2`).

**Почему в архиве.** Д.R4а.6: банкротства ЦБ E&F нет, крайняя слабость валюты — по правилам модели
(`is_extreme_weak_currency`: курс к паритету < `zz_ef_cb_crisis_vtp` и покрытие < `zz_ef_cb_crisis_cover`).

**Удалено из живых файлов.**
- `common/scripted_effects/01_financial_scripted_effects.txt` — определение `central_bank_bankruptcy` (здесь).
- `common/scripted_effects/01_economic_scripted_effects.txt` — блок `if` «#central_bank_bankruptcy» с вызовом (здесь).

**Осталось.** Переменная `central_bank_bankruptcy` (0 от `10_new_country_var.txt`), её счётчики
(`central_bank_bankruptcy_count_reset*`), модификатор `central_bank_bankruptcy_country`, строка окна
(`09_ef_other.txt`), выкуп `zz_ef_rq_crisis_resell` при `var:central_bank_bankruptcy = 1` — без писателя, не срабатывают.
