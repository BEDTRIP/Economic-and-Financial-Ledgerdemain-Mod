# Строка расходов эмитента `zz_ef_foreign_bond_interest` (мёртвый)

**Что делал:** статический модификатор страны (`country_expenses_add = 1`, множитель — `zz_ef_bond_interest_due_week`: годовой
процент держателей по облигациям страны / 48) — эмитент платил проценты по своим облигациям у чужих казначейств. Заменён
книгой облигаций (`ld_bond_ledger.txt`, проценты держателю платит книга); модификатор больше не накладывался, шаг книги
только снимал его со старых сохранений.

**Файлы здесь:** `common/static_modifiers/ld_bond_interest.txt` (целиком); `localization/<lang>/ld_bond_interest_l_<lang>.yml`
(11 языков, целиком); `common/script_values/ld_reference_currency_values.txt` — вырезанное значение
`zz_ef_bond_interest_due_week`.

**Удалено из живых файлов:**
- `common/scripted_effects/ld_bond_ledger.txt` (`zz_ef_bond_ledger_step`):
  `if = { limit = { has_modifier = zz_ef_foreign_bond_interest } remove_modifier = zz_ef_foreign_bond_interest }`;
  то же — в генераторе `vic3_mods/tools/regen_ef_bond_ledger.py`.

**Проверить в игре:** сохранение с этим модификатором на стране даст строку об отсутствующем модификаторе.
**Вернуть:** файлы — по исходным путям, строку снятия — в генератор.
