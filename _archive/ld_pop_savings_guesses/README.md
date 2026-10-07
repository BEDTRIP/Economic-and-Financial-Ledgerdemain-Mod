# Догадки хотфикса о сбережениях населения (`ld_pop_savings_guesses`)

Вынуто 8.10.2026 (R1а, решение пользователя: «вклады идут в пул, кредиты — из пула в наличные; что за излишек»).
Три механизма хотфикса, которые зачисляли или списывали деньги населения без второй стороны. Они были нужны, пока
сбережения пополнялись утечкой M2 (до R1а.6); после R1а.6 вклады = взносы попов в пул по движку, наличные двигаются
только проводками, необъяснённое — «прочее» (`docs/money-model.md`).

## Что делали
1. **Выкуп уровней → сбережения** (В1.2, 3.10). Необъяснённая убыль пула за неделю (`zz_ef_v_f_pool_other` < 0) считалась
   выкупом уровней зданий компаниями у населения по цене приватизации и зачислялась в сбережения `zz_ef_pop_savings`
   (`zz_ef_f_buyout_got`, значение `zz_ef_v_f_buyout`). Любая потеря пула мимо проводок создавала столько же наличных.
2. **События казны → сбережения** (В1.6 / ИВ.1, решение 5.10 «а»). Дополнительные расходы казны (экспедиции, события)
   зачислялись населению как «заказ внутри страны», доходы — списывались (`zz_ef_f_event_sav`, `zz_ef_v_f_event_sav`).
3. **Излишек сбережений → «в богатство»** (Д2.20, Д2.22 в, 6.10). 10 % в неделю того, что выше нормы 0,3–0,6 ВВП
   (`zz_ef_sav_norm`), списывалось из сбережений без пары (`zz_ef_sav_to_wealth`, `zz_ef_sav_speed`, `zz_ef_f_sav_wealth`);
   резали наличные, их норму потом восстанавливало изъятие вкладов из пула.
Все три — только с 3-й недели (`zz_ef_weeks_run >= 3`). Вызывал `zz_ef_pop_savings_step` (`zz_ef_bridge_apply` шага).

## Удалено из живых файлов
| файл | что |
| --- | --- |
| `common/scripted_effects/ld_money_model.txt` | в `zz_ef_pop_savings_step` — три блока (от «В1.2 (3.10): levels sold to companies» до `set_variable = { name = zz_ef_f_dep_in …`); в `zz_ef_money_model_step` — `zz_ef_money_window_roll = { F = buyout_got }` и `{ F = sav_wealth }`; в строке лога `EFR` — поля `event_sav …` и `sav_wealth …` (текст — `common/scripted_effects/ld_money_model.txt` здесь) |
| `common/script_values/ld_metal_accounts_values.txt` | `zz_ef_sav_to_wealth`, `zz_ef_sav_speed`, `zz_ef_v_w_sav_wealth` |
| `common/script_values/ld_money_model_values.txt` | `zz_ef_v_f_buyout`, `zz_ef_v_f_event_sav` |
| `common/script_values/ld_reference_currency_values.txt` | `zz_ef_v_w_buyout` |
| `localization/<язык>/replace/ld_money_supply_replace_l_<язык>.yml` (11 языков) | `zz_ef_ms_x_v_w_buyout`, `zz_ef_ms_x_v_w_sav_wealth`; карточка населения (`zz_ef_ms_pops_NN`) — строки «← выручка продавцов уровней зданий» и «→ сверх нормы накоплений — в богатство», ключи перенумерованы генератором, `zz_ef_ms_pops_27..29` удалены; в карточке пула строка «компании выкупают уровни … — деньги продавцам» стала «необъяснённая убыль пула (прочее)», строка «в накопления: выручка продавцов уровней» удалена (прежний текст карточки — `localization/` здесь) |
| `../vic3_mods/tools/regen_ef_money_supply_loc.py` | те же строки карточек (генератор) |

`zz_ef_sav_norm` остаётся: по нему стартовые сбережения (`zz_ef_pop_start_savings`) и подсказка карточки.

## Как вернуть
Вставить блоки и значения на прежние места, строки генератора — назад, запустить
`python ../vic3_mods/tools/regen_ef_money_supply_loc.py` и `ld_loc_langs.py`. Пара для излишка, если понадобится, —
`add_pop_wealth` (уровни богатства попам), для потерь — R7.
