# Месячный учёт спроса на финпродукты `stockpiling_<вид>_1`

`stockpiling_bond_1`, `_manufacture_stock_1`, `_agricultural_stock_1`, `_mining_stock_1`, `_railroad_stock_1` (считали
`stockpiling_<вид>_var_2` из заказов рынка, при `var_1 < 1000000`) и их вторые части `stockpiling_<вид>_2_state`
(добавляли `var_2` в `stockpiling_<вид>_var_state_1` столицы-финцентра). Вызовов нет (refs=0; `_2_state` звали только
`_1`). Переменные `var_1/var_2/var_state_1` остались (инициализация, чтение значениями и GUI), ничего их больше не
накапливает — как и раньше, до выноса. **Удалено из живых файлов:** определения и баннер раздела
`01_financial_scripted_effects.txt`, 787–997. **Вернуть:** вставить на место.
