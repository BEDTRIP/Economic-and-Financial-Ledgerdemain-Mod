# Читатели переменных, которые нигде не задаются (`ld_dead_readers`)

Вынуто 8.10.2026 (R3а, разбор логов r1008_122252: «Variable '…' is used but is never set»). Каждое место читало
переменную, которую ни один живой файл не пишет, — ветка никогда не срабатывала или значение всегда 0.

## Удалено из живых файлов
| файл | что | почему мёртвое |
| --- | --- | --- |
| `common/scripted_effects/ld_money_model.txt` | эффект `zz_ef_money_week_retire` (снимал `zz_ef_week_alive`, `zz_ef_week_probe`, `zz_ef_week_probe_value`) | чистка сейвов до R1а.4 (7.10), прежней недельной цепочки нет |
| `common/on_actions/ld_money_model_on_actions.txt` | заглушки `zz_ef_money_week_probe`, `zz_ef_money_model_weekly` (звали `zz_ef_money_week_retire`) | то же |
| `common/scripted_effects/ld_money_model.txt` | в `zz_ef_money_model_step` ветка `else_if = { limit = { has_variable = zz_ef_metal_rescale_due } … set zz_ef_cb_start_due }` | сейвы до версии старта 9 |
| `common/scripted_effects/ld_money_model.txt` | в логе `EFX` поля `rcin`, `rcback`, `rcmetal` | их переменные `zz_ef_rc_fx_in`, `zz_ef_rc_back`, `zz_ef_rc_metal_out` писал шаг `zz_ef_rc_step`, он в `_archive/ef_reserve_trade_step/` |
| `common/script_values/ld_reserve_trade_values.txt` (и `../vic3_mods/tools/regen_ef_reserve_trade.py`, `VALUES`) | `zz_ef_v_rc_fx_in`, `zz_ef_v_rc_back`, `zz_ef_v_rc_metal_out` | то же |
| `common/script_values/PSC_construction_values.txt` | тело `construction_demand_ratio` (чтение `nominal_construction_demand` × очки / `national_production`); теперь `value = 0` | `nominal_construction_demand` PSC не задаёт; читатель — алерт `PSC_alert_types.txt` (не срабатывал) |
| `common/script_values/00_economic_scripted_value.txt` | в `silver_lost` — `if exists = scope:arbitrage_privat_bank` (потолок по резерву частного банка) | цель задавал арбитраж частных банков, он в `_archive/ef_privat_bank_arbitrage/` |
| `common/scripted_effects/09_introduction_building_lvl.txt` | 190 блоков `#Currency recreat` (`if has_variable = new_currency_recreat` → снять, `capital_state`, `target_country`) в эффектах ввода валют | `new_currency_recreat` E&F нигде не задаёт |

Текст — в файлах по исходным путям здесь.

## Как вернуть
Вставить вырезанное на прежние места; для `zz_ef_v_rc_*` — вернуть `VALUES` в генератор и поля в строку `EFX`.
Имеет смысл, только если вернётся писатель переменной.
