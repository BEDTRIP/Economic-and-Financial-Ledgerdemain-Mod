# Пустой учёт финпродуктов `stockpile_finacial_product`

Пустое определение `stockpile_finacial_product = { }` и его месячный вызов. Раньше копило биржевые счётчики «пул акций»
(`stockpiling_<вид>_var_state_1` и др.); эти переменные остались (инициализация в `history/global`, `10_new_country_var.txt`,
`ld_stockpile_state_var_seed.txt`), их читают значения `00_financial_scripted_value.txt` и GUI.

**Удалено из живых файлов:**
- `common/scripted_effects/01_financial_scripted_effects.txt`: `stockpile_finacial_product = { }`;
- `common/scripted_effects/00_on_action_main.txt`, `financial_center_ef_on_monthly_pulse_country`:
  `if = { limit = { market_owner_is_root = yes } stockpile_finacial_product = yes }`.

**Вернуть:** вставить определение и `if` в конец месячного пульса финцентра.
