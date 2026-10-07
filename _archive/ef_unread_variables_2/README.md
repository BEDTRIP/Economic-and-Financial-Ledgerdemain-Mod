# Переменные, которые ставятся, но никто не читает (дочистка 7.10)

**Что делали:** ничего. Движок писал «Variable '…' is set but is never used» (error.log каждого запуска). Проверено:
имени нет ни в чтениях `var:` / `has_variable` / `Var('…')` скриптов, ни в GUI и английской локализации; у тёзок
скрипт-значений (`bond_producted`, `import_value_in_currency`, `base_supply_mutual_fund_fix`, `sell_limit_var_N`,
`stockpiling_bond_var_1`) код читает значение, а не переменную. Первая чистка такого рода (2192 имени, ночь 6–7.10) —
без отдельной папки, по решению Д.1 а.

**Оставлено:** 386 имён, которые читает GUI или локализация (движок такое чтение не видит); `zz_ef_ms_what`,
`zz_ef_mt_bank_g/_s`, `zz_ef_cur_intro_norm` (поля строк логов `EFM` / `EFT` через `Var('…')`); `zz_ef_parity_hist`
(читается `var:`); `central_bank_debt_privat_bank_buyer_list_1_clear` (семейство из 25 списков, 2–25 читает GUI).

**Удалено из живых файлов** (блоки `set_*variable` / `change_*variable` — здесь, по тем же путям, с номером строки до выноса):

| файл | строк-блоков | имена |
| --- | --- | --- |
| `common/history/global/00_ef_economic_global_variable.txt` | 7 | `00_ai_buy_building_artillery_foundry_test`, `00_ai_buy_building_automotive_industry_test`, `00_ai_buy_building_naval_base_test`, `00_ai_buy_building_oil_rig_test`, `00_ai_buy_building_whaling_station_test`, `bond_producted`, `import_value_in_currency` |
| `common/history/global/00_ef_financial_global_variable.txt` | 42 | `ai_central_bank_gold_loaned_1`, `ai_central_bank_gold_loaned_10`, `ai_central_bank_gold_loaned_2`, `ai_central_bank_gold_loaned_3`, `ai_central_bank_gold_loaned_4`, `ai_central_bank_gold_loaned_5`, `ai_central_bank_gold_loaned_6`, `ai_central_bank_gold_loaned_7`, `ai_central_bank_gold_loaned_8`, `ai_central_bank_gold_loaned_9`, `ai_central_bank_interest_refund_per_year_1`, `ai_central_bank_interest_refund_per_year_10`, `ai_central_bank_interest_refund_per_year_2`, `ai_central_bank_interest_refund_per_year_3`, `ai_central_bank_interest_refund_per_year_4`, `ai_central_bank_interest_refund_per_year_5`, `ai_central_bank_interest_refund_per_year_6`, `ai_central_bank_interest_refund_per_year_7`, `ai_central_bank_interest_refund_per_year_8`, `ai_central_bank_interest_refund_per_year_9`, `ai_no_longer_exists_1`, `ai_no_longer_exists_10`, `ai_no_longer_exists_2`, `ai_no_longer_exists_3`, `ai_no_longer_exists_4`, `ai_no_longer_exists_5`, `ai_no_longer_exists_6`, `ai_no_longer_exists_7`, `ai_no_longer_exists_8`, `ai_no_longer_exists_9`, `base_supply_mutual_fund_fix`, `no_longer_exists_1`, `no_longer_exists_10`, `no_longer_exists_2`, `no_longer_exists_3`, `no_longer_exists_4`, `no_longer_exists_5`, `no_longer_exists_6`, `no_longer_exists_7`, `no_longer_exists_8`, `no_longer_exists_9`, `sell_limit_var_0` |
| `common/history/global/00_ef_stockpile_global_variable.txt` | 1 | `stockpiling_bond_var_1` |
| `common/scripted_effects/09_introduction_building_lvl.txt` | 1 | `base_supply_mutual_fund_fix` |
| `common/scripted_effects/10_new_country_var.txt` | 50 | `00_ai_buy_building_artillery_foundry_test`, `00_ai_buy_building_automotive_industry_test`, `00_ai_buy_building_naval_base_test`, `00_ai_buy_building_oil_rig_test`, `00_ai_buy_building_whaling_station_test`, `ai_central_bank_gold_loaned_1`, `ai_central_bank_gold_loaned_10`, `ai_central_bank_gold_loaned_2`, `ai_central_bank_gold_loaned_3`, `ai_central_bank_gold_loaned_4`, `ai_central_bank_gold_loaned_5`, `ai_central_bank_gold_loaned_6`, `ai_central_bank_gold_loaned_7`, `ai_central_bank_gold_loaned_8`, `ai_central_bank_gold_loaned_9`, `ai_central_bank_interest_refund_per_year_1`, `ai_central_bank_interest_refund_per_year_10`, `ai_central_bank_interest_refund_per_year_2`, `ai_central_bank_interest_refund_per_year_3`, `ai_central_bank_interest_refund_per_year_4`, `ai_central_bank_interest_refund_per_year_5`, `ai_central_bank_interest_refund_per_year_6`, `ai_central_bank_interest_refund_per_year_7`, `ai_central_bank_interest_refund_per_year_8`, `ai_central_bank_interest_refund_per_year_9`, `ai_no_longer_exists_1`, `ai_no_longer_exists_10`, `ai_no_longer_exists_2`, `ai_no_longer_exists_3`, `ai_no_longer_exists_4`, `ai_no_longer_exists_5`, `ai_no_longer_exists_6`, `ai_no_longer_exists_7`, `ai_no_longer_exists_8`, `ai_no_longer_exists_9`, `base_supply_mutual_fund_fix`, `bond_producted`, `import_value_in_currency`, `no_longer_exists_1`, `no_longer_exists_10`, `no_longer_exists_2`, `no_longer_exists_3`, `no_longer_exists_4`, `no_longer_exists_5`, `no_longer_exists_6`, `no_longer_exists_7`, `no_longer_exists_8`, `no_longer_exists_9`, `sell_limit_var_0`, `stockpiling_bond_var_1` |
| `common/scripted_effects/ld_bond_ledger.txt` | 1 | `zz_ef_f_bond_int` |
| `common/scripted_effects/ld_money_model.txt` | 1 | `zz_ef_parity_before` |

**Вернуть:** вставить блоки обратно по номерам строк.
