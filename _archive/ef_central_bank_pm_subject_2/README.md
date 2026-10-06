# `central_bank_production_methods_2` и `_2_act` (ПМ ЦБ для подданных)

**Что делало:** `central_bank_production_methods_2` (2670 строк, «Désactiver suite à trop de bug») переключало PM здания `building_bank` у подданных по валюте
(`pm_subject_currency_<cur>_currency`: `activate_production_method`, `is_production_method_active`). Все вызовы закомментированы; `_2_act` —
обёртка `every_country { if { limit = { not = { market.owner = this } } #central_bank_production_methods_2 = yes } }` (пустое тело). Живое — `central_bank_production_methods` и `_3`/`_4`.
**Переменные:** не писало (пустое). **Интерфейс:** нет.

## Вырезано из живых файлов (текст — по тем же путям)
| файл | что |
| --- | --- |
| `common/scripted_effects/01_economic_scripted_effects.txt` | определения `central_bank_production_methods_2` и `central_bank_production_methods_2_act`; закомментированная строка `#central_bank_production_methods_2 = yes` (после `if` с `law_gold_exchange_standard`, перед `money_value_target_modification`) |
| `common/scripted_effects/00_on_action_main.txt` | в `central_bank_ef_on_yearly_pulse_country` после `central_bank_production_methods = yes`: `if = { limit = { market_owner_is_root = no  market_owner_is_root_univ_with_buiding = no } #central_bank_production_methods_2 = yes }` (эффект пуст) |
| `common/scripted_effects/09_introduction_building_lvl.txt`, `common/history/global/99_ef_history_global_variable.txt` | закомментированные строки `#central_bank_production_methods_2 = yes` |
| `common/on_actions/00_ef_on_action.txt` | закомментированный `# if = { limit = { has_modifier = has_central_bank  has_law = law_type:law_external_exchange_standard } central_bank_production_methods_2 = yes }` в `ef_on_production_method_changed` |
| `common/scripted_guis/09_ef_other.txt` | `central_bank_production_methods_2_act = yes` в двух sgui: в списке `effect` первого (после `reference_currency_in_gold_fixe = yes`, с заголовком `#subject pm`) и в `world_currency_list_gerenation_ordered` (после `dependent_economies_list = yes`) |

**Вернуть:** определения — на место в `01_economic_scripted_effects.txt`, вызовы — по таблице; `_2` писал в PM здания, проверять в игре.
