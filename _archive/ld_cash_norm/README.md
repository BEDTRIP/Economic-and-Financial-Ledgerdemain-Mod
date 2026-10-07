# Норма наличных населения и наличные ↔ вклады по ней (`ld_cash_norm`)

Вынуто 8.10.2026 (R1б, решение пользователя В3, аудит R1б.0 — А5). Заглушка хотфикса: наличные населения держались у
нормы от ВВП (6–20 % ВВП по ставке вкладов), сверх неё население несло 10 % разрыва в неделю во вклады, ниже — снимало.
Деньги в пул входили и выходили (`add_investment_pool`) против наличных, которые были ничьим обязательством (S − D) —
деньги движка из ничего и в никуда. Теперь наличные — банкноты, долг ЦБ (`zz_ef_notes`, `docs/money-model.md`), их
двигают только проводки; поведение населения (ставка, недоверие) — R7.

## Что делало
- `zz_ef_cash_norm_gdp` (доля ВВП по ставке вкладов: 20 % при 0 %, 12 % при 3 %, не ниже 6 %), `zz_ef_pop_cash_norm`
  (= ВВП × доля), `zz_ef_cash_speed` (0,1);
- `zz_ef_dep_in` — 10 % наличных сверх нормы во вклады; `zz_ef_dep_out` — 10 % недостачи из вкладов (не больше вкладов и
  пула); в `zz_ef_pop_savings_step` — `add_investment_pool` ± и вклады ±;
- окна `zz_ef_w_dep_in / _out` (`zz_ef_money_window_roll`), значения `zz_ef_v_f_dep_in/_out`, `zz_ef_v_w_dep_in/_out`;
  строки в потоковых остатках `zz_ef_pool_other_week`, `zz_ef_leak_week`;
- норма задавала и старт: сбережения не ниже нормы наличных, вклады = сбережения − норма.

## Удалено из живых файлов
| файл | что |
| --- | --- |
| `common/script_values/ld_money_model_values.txt` | блок «pops' cash at hand and deposits» (`zz_ef_cash_norm_gdp`, `zz_ef_cash_speed`, `zz_ef_pop_cash_norm`), `zz_ef_dep_in`, `zz_ef_dep_out`, `zz_ef_v_f_dep_in/_out`, `zz_ef_v_w_dep_in/_out`; две строки в `zz_ef_pool_other_week` и `zz_ef_leak_week`; в `zz_ef_pop_start_savings` — `min = zz_ef_pop_cash_norm`, в `zz_ef_pop_start_deposits` — `subtract` / `min` (вклады = сбережения) |
| `common/scripted_effects/ld_money_model.txt` | в `zz_ef_pop_savings_step` — 8 строк dep_in / dep_out; в `zz_ef_money_model_step` — два `zz_ef_money_window_roll` (`dep_in`, `dep_out`); в логах — `EFW … normsh`, `EFR … dep_in, dep_out, norm` |
| `localization/<язык>/replace/ld_money_supply_replace_l_<язык>.yml` (11 языков) | карточка населения — «2 Вклады в банках» с двумя строками и текст «норма наличных … сверх неё несёт во вклады, ниже — снимает»; карточка банков — «вклады населения из накоплений», «снятие вкладов»; карточка вкладов — «внесено из наличных», «снято в наличные»; ключи `zz_ef_ms_x_v_w_dep_in(_2)`, `_dep_out(_2)`, `zz_ef_ms_x_pop_cash_norm` (прежний текст — `localization/` здесь); ключи карточек перенумерованы генератором, лишние в конце удалены |
| `../vic3_mods/tools/regen_ef_money_supply_loc.py` | те же строки карточек |

## Как вернуть
Вставить значения и блок на прежние места (тексты — здесь), строки генератора — назад, запустить
`python ../vic3_mods/tools/regen_ef_money_supply_loc.py` и `ld_loc_langs.py`. Но наличные теперь — банкноты: обмен
наличные ↔ вклады — проводка `zz_ef_notes` ↔ `zz_ef_pop_deposits` с выпуском / погашением банкнот ЦБ (пул ±), а не
норма от ВВП.
