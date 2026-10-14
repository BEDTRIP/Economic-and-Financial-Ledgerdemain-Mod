# Покупки облигаций ИИ E&F: казна (`ai_buy_bond_N`) и частные банки (`ai_privat_bank_bond_N`)

Вынуто 14.10.2026 (R6.9, кусок 1; Д.R6.6, Д.R5.6). Раз в год (`financial_center_ef_on_yearly_pulse_country` →
`ai_buy_central_bank_debt`) казна страны ИИ покупала облигации чужого ЦБ слотами `ai_buy_bond_1..10`, частные банки —
слотами `ai_privat_bank_bond_1..25` (и `_renforcement`); погашение казны — `ai_bond_maturity_N` в
`bond_maturity_on_action`. Реестр облигаций (`ld_bond_ledger.txt`) брал слоты как вход покупок
(`zz_ef_bl_slot_N`, `zz_ef_pb_slot_N` → `zz_ef_bl_register`). Теперь покупки — заявками на бирже (Д.R6.6): банки и
население покупают доли в стакане (`ld_exchange_trade.txt`), банки продают за рубеж долю внутреннего долга
(`zz_ef_xch_post_sells_ob`).

## Удалено из живых файлов
| файл | что |
| --- | --- |
| `common/scripted_effects/01_financial_scripted_effects.txt` | `ai_buy_bond_1..10`, `ai_bond_maturity_1..10`, `ai_privat_bank_bond_1..25`, `ai_privat_bank_bond_1..25_renforcement` (здесь) |
| `common/scripted_effects/00_on_action_main.txt` | `ai_buy_central_bank_debt` (здесь); вызов `ai_buy_central_bank_debt = yes` в `financial_center_ef_on_yearly_pulse_country`; ИИ-часть `bond_maturity_on_action` (10 `if` с `ai_bond_maturity_N`, здесь) |
| `common/messages/00_ef_messages.txt` | `ai_selle_bond_maturity_1..10_message`, сообщения частных банков `ai_privat_bank_(renforcement_)?(buy\|selle)_bond_maturity_N_message` (здесь) |
| `common/script_values/00_financial_scripted_value.txt` | `ai_no_longer_exists_1..10`, `bond_quantity_scripted`, `bond_quantity_scripted_privat_bank` (здесь) |
| `common/script_values/00_economic_scripted_value.txt` | `gold_reserves_10`, `gold_reserves_var_10`, `private_bank_funds_25` — читали только архивные (здесь) |
| `common/scripted_effects/10_new_country_var.txt` | 20 стартовых `set_variable` слотов ИИ (`ai_buy_bond_N_on`, `ai_selle_bond_maturity_yers_N`; здесь) |
| `common/scripted_effects/ld_bond_ledger.txt` (генерат `regen_ef_bond_ledger.py`) | `zz_ef_bl_slot_1..10`, `zz_ef_bl_slot_free`, `zz_ef_pb_slot_1..25`, `zz_ef_pb_no_seller`, `zz_ef_bl_register` и их вызовы в `zz_ef_bond_ledger_step` (здесь) |
| `docs/entry-points.md` | строка лога `EFP` (покупка банков без продавца) |

Осталось (кусок 2 — R6.9): слоты игрока E&F (`buy_bond_N`, `bond_maturity_N`, кнопки `00_financial_scripted_guis.txt`),
окно E&F и наша панель с таблицами слотов ИИ (`ai_seller_country_general_N`, `ai_total_bond_value_N`,
`ai_interest_calculated_N` — пишутся только стартом, читают `gui/00_ef_deported_gui_1.gui`, `gui/ld_cb_rate_panel.gui`,
`00_financial_scripted_value.txt`), ключи локализации сообщений и модификаторов `ai_buy_bond_N` (11 языков), покупка за
иностранную валюту и запасы `stockpiling_<валюта>_state_1`.
