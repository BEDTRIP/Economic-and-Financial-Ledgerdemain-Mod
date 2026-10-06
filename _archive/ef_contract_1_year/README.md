# Сбор очистки контрактов `contract_1_year`

**Что делало:** `contract_1_year` (205 строк) для 29 товаров ставило `var:<good>_contract_1_year = 1` и звало `clear_<good>_contract_1_year`; никто не вызывал
(те же 29 `clear_<good>_contract_1_year` зовёт напрямую `ef_on_yearly_pulse_reset`). Переменные `<good>_contract_1_year` живые (пишут/читают sgui запаса и `ef_on_yearly_pulse_reset`) — не тронуты.
**Интерфейс:** нет.

**Вырезано:** `common/scripted_effects/00_on_action_main.txt` — определение `contract_1_year` (после `bond_maturity_on_action`, перед `money_value_global_var`). Вызовов нет.
**Вернуть:** вставить на место и вызвать из `ef_on_yearly_pulse_reset`.
