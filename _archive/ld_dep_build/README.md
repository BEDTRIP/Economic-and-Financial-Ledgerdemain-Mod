# Частная стройка пула из вкладов населения (`ld_dep_build`)

Вынуто 14.10.2026 (R6.3, Д.R6.13; аудит А14, А15). Частная стройка пула (перевод пула в казну) сверх нового делового
кредита оплачивалась из вкладов населения: вклады → требования «частный сектор» `zz_ef_pop_claims_private` (уровни,
оплаченные деньгами населения); сбережения убывали на ту же сумму. Правило прогоном не проверялось; вклады населения
убывали от стройки (В.R7.3: M1 ≈ M2). Теперь вся стройка сверх нового кредита — деловой кредит банков
(`zz_ef_bc_debt`), он делится по компаниям по уровням (Д.R6.9, `docs/код/exchange-companies.md`).

## Что делало
- `zz_ef_f_dep_build` = перевод пула (`zz_ef_v_f_transfer`) − новый деловой кредит (`zz_ef_v_f_bc_new`), не больше
  вкладов; проводка `zz_ef_post = { FROM = zz_ef_pop_deposits TO = zz_ef_pop_claims_private }`; сбережения − та же
  сумма; приход в сбережения шага `zz_ef_f_inflow` = взносы − стройка;
- остаток стройки сверх вкладов (`zz_ef_f_bc_short`) — деловой кредит (остался, теперь — вся стройка сверх кредита);
- `zz_ef_pop_claims_private` — нулевой счёт реестра на старте (`zz_ef_registry_init`), никто не читал.

## Удалено из живых файлов
| файл | что |
| --- | --- |
| `common/scripted_effects/ld_money_model.txt`, `zz_ef_pop_deposits_step` | `set_variable zz_ef_f_dep_build = 0`; блок `set_variable zz_ef_f_dep_build = { … }`, проводка в `zz_ef_pop_claims_private`, `change_variable zz_ef_pop_savings subtract`; `subtract = var:zz_ef_f_dep_build` в `zz_ef_f_bc_short`; `change_variable zz_ef_f_inflow subtract = var:zz_ef_f_dep_build` — текст ниже |
| `common/scripted_effects/ld_ledger.txt`, `zz_ef_registry_init` | `if = { limit = { NOT = { has_variable = zz_ef_pop_claims_private } } set_variable = { name = zz_ef_pop_claims_private value = 0 } }` |
