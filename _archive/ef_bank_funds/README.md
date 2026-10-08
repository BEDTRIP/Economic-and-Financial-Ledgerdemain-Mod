# Фонды частных банков E&F

**Что делали.** «Фонд» банка E&F — не деньги банка, а подпись: сколько чужих облигаций из 25 слотов страны
(`ai_privat_bank_bond_value_N`) числится за банком и сколько чужих валют он держит. Облигации покупает пул страны
(`add_investment_pool`), банк-«покупатель» выбирается случайно из списка банков страны; модель `ld_*` считает облигации
банков одной суммой (`zz_ef_bank_bonds`) и от фондов не зависит. Валюты банков (`stockpiling_<cur>_company_<bank>_fixe`,
16 банков × 95 валют) история ставила в 0, и никто их больше не писал. Снаружи группу читали только окна и сортировка
списка банков. Решение — В2 (пользователь 8.10): в архив; банк как компания со своими счетами (портфель облигаций и
валюты) — заново в R4.

**Вырезано (по исходным путям):**

| файл | что |
| --- | --- |
| `common/script_values/01_economic_company_value.txt` | `company_<bank>_fund` (97), `saint_petersburg_international_commercial_bank_fund`, `russo_chinese_bank_fund`, `funds_from_foreign_debt(_total)`, `ai_privat_bank_{bond_quantity,bond_value,interest_calculated}_<1..25>_from_list`, `private_bank_foreign_reserves_per_bank(_gui)`, `company_<bank>_total_in_gold` (16), `stockpiling_<cur>_private_bank` (95), `stockpiling_<cur>_company_<bank>_fixe_in_gold` (1520), `private_bank_funds_per_private_bank_add_foreign_debt` (ключ сортировки), `private_bank_silver_reserve_per_bank_gui_in_gold` |
| `common/script_values/01_economic_currency_scripted_value.txt` | `stockpiling_<cur>_private_bank_gui` (95), `currency_global_stokpile`, `currency_own_by_private_bank` |
| `common/scripted_effects/08_list_effect.txt` | `global_arbitrage_bank_<cur>_variable_list` (95) |
| `common/scripted_guis/00_economic_scripted_guis.txt` | `update_company_<bank>_currency_stored_liste` (16) |
| `common/scripted_guis/09_ef_other.txt` | `company_<bank>_privat_bank_foreign_reserves_visible` (16) |
| `common/script_values/ld_clearing_values.txt` | `zz_ef_bank_holds_<bank>` (16; генератор `regen_ef_clearing` их больше не пишет) |
| `common/history/global/00_ef_economic_global_variable.txt` | 3040 глобальных: `company_<bank>_currency_stored_<cur>_02` + список `company_<bank>_privat_bank_stored_currency`, `stockpiling_<cur>_company_<bank>_fixe = 0` |
| `gui/00_ef_deported_gui_2.gui` | типы `ef_bp_<cur>_c_private_bank_stokpile_piechart` (95) |
| `gui/ld_economy_panel.gui`, `gui/ld_cb_rate_panel.gui` | элементы окон (ниже) |
| `localization/english`, `russian` `00_ef_gui_localization_l_*.yml`, `ld_economy_panel_l_*.yml` | строки окон (ниже); остальные девять языков — копии английской |

**Удалено из живых файлов (вызовы и окна):**

- `common/script_values/01_economic_company_value.txt`, `total_bank_funds`: слагаемые `add = funds_from_foreign_debt_total`,
  `add = private_bank_foreign_reserves_per_bank`.
- `common/scripted_effects/08_list_effect.txt`, `privat_bank_variable_list_ordered`: `ordered_in_list = { … order_by =
  private_bank_funds_per_private_bank_add_foreign_debt max = 100 check_range_bounds = no … }` → `every_in_list` (Д.R3б.1:
  без сортировки).
- `common/scripted_guis/09_ef_other.txt`, `list_generation_when_player_open_tab`: 95 строк
  `global_arbitrage_bank_<cur>_variable_list = yes` (под комментарием `#graph currency private bank`).
- `common/scripted_guis/ld_cbfx.txt`, `zz_ef_holders_update` (генератор `regen_ef_clearing`): часть «Е.2» — список
  `zz_ef_bank_holders_list` банков-держателей (`zz_ef_bh_<bank>`, `zz_ef_bank_holds_pc`).
- `gui/ld_economy_panel.gui`: вкладка «Экономика» — коробки «total_currency_product» (`currency_global_stokpile`) и
  «currency_own_by_private_bank»; у каждой валюты — `ef_bp_<cur>_c_private_bank_stokpile_piechart = {}` рядом с
  `ef_bp_<cur>_c_global_stokpile_piechart`; торговый баланс — `zz_ef_bank_holders_piechart = {}` и тип
  `zz_ef_bank_holders_piechart`.
- `gui/ld_cb_rate_panel.gui`, вкладка «Финансы»: сводка частных банков — коробки «private_bank_bond_holdings»
  (`funds_from_foreign_debt_total`) и «private_bank_foreign_reserves» (`private_bank_foreign_reserves_per_bank`); строка
  таблицы банков — текст `funds_from_foreign_debt` (`@bond!`) и `private_bank_foreign_reserves_per_bank_gui`
  (`@spe_uni_c!`), столбец `private_bank_funds_per_private_bank_add_foreign_debt` → доля пула
  `Company.GetCountry … private_bank_funds_per_private_bank` (Д.R3б.2); 16 секций «company_<bank>_privat_bank_foreign_reserves»
  (заголовок, список `company_<bank>_privat_bank_stored_currency`, внешний контейнер); облигации — секция
  «see_buyer_private_bank» (банки-покупатели слотов 1..25 с `ai_privat_bank_*_N_from_list`).
- Локализация (11 языков): ключи, читающие вырезанное (`company_<bank>_<cur>_02_accumulated_in_gold`), ключи строк
  снятых секций (`company_<bank>_<cur>_02_{accumulated,money_value_in_gold,name_currency}`,
  `company_<bank>_privat_bank_foreign_reserves`), подписи снятых коробок (`currency_own_by_private_bank`,
  `total_currency_product`, `private_bank_bond_holdings`, `private_bank_foreign_reserves`, `see_buyer_private_bank`,
  `EF_BP_CHART_RESERVE_PRIVATE_BANK_HEADING`), `zz_ef_ep_bank_holders_title`.

**Остаются (до R5):** покупки `ai_privat_bank_bond_N` (пул страны покупает, банк-покупатель — случайный из
`privat_bank_variable_list_ordered`), слоты реестра `zz_ef_pb_slot_N`.

**Вернуть:** вырезанное — на прежние места; вызовы и элементы окон — по списку выше (вырезанные куски окон — в
`gui/…` архива с подписью места); генератор `regen_ef_clearing` — вернуть `BANKS`, `zz_ef_bank_holds_<bank>` и часть
«Е.2» `zz_ef_holders_update` (git: коммит R3б.6).
