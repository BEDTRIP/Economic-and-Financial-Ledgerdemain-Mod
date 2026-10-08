# Генераторы

Часть файлов `ld_*` строится скриптами Python проекта (`../vic3_mods/tools/regen_ef_*.py`), а не пишется руками.
Такой файл (или его записи) **руками не править**: правка теряется при следующем запуске генератора. Правится
генератор, потом он запускается.

## Как работают
- Общий модуль — `tools/ld_gen.py`: `emit(путь, текст)` вписывает вывод в файл форка **по ключам записей**
  (запись есть — заменяется на месте, нет — пропускается и попадает в отчёт `absent`; записи файла, которых генератор
  не выдал, не трогаются — рукописные). Локализация — по ключам строк, пишутся только `english` и `russian`.
- Ключи записей внутри файлов `ld_*` сохранили имена `zz_ef_*` / `zz_pb_ef_*`; путь генератора `zz_ef_X` → `ld_X`,
  `zz_pb_ef_X` → `ld_pb_X`, `00_00_ef_X` → `ld_X` (`ld_gen.fork_rel`).
- Запуск из `vic3_mods`: `python tools/<генератор>.py` — запись; `--check` — только сверка, код выхода 1 при
  расхождении. После генератора, который менял английскую локализацию, — `python tools/ld_loc_langs.py`.
- Часть генераторов читает ваниль из `vic3_mods_out/.vanillaVIC3` — запускаются только на ПК.

## Список
| генератор | файлы форка | читает |
| --- | --- | --- |
| `regen_ef_bank_seed` | `common/scripted_effects/ld_bank_seed.txt` | `common/company_types/00_ef_companies.txt` |
| `regen_ef_bond_ledger` | `common/scripted_effects/ld_bond_ledger.txt`, `common/script_values/ld_bond_ledger_values.txt` | — |
| `regen_ef_bond_tables` | `common/scripted_guis/ld_bond_tables.txt`, `common/script_values/ld_bond_tables_values.txt`, `localization/<lang>/ld_bond_tables_l_<lang>.yml` | — |
| `regen_ef_cb_loan` | `common/script_values/ld_cb_loan_values.txt`, `localization/<lang>/replace/ld_cb_loan_replace_l_<lang>.yml` | — |
| `regen_ef_cb_rate_gui` | `gui/ld_cb_rate_panel.gui` | `gui/ld_cb_rate_panel.gui` / E&F-оригинал (ПК) |
| `regen_ld_currency_data` | `common/scripted_effects/ld_currency_var.txt`, `on_activate` законов `common/laws/01_ef_currency_type.txt`, `currency_name` / `currency_symbol` / `currency_symbol_generic` / `currency_symbol_<cur>` в `common/customizable_localization/00_ef_localization_ custom.txt`, `common/script_values/ld_currency_values.txt`, оценка валют в `zz_ef_fx_reserves_metal` (`ld_fx_reserves_values.txt`), `docs/currency-table.md` | законы, история и локализация валют форка |
| `regen_ld_currency_national` | `common/scripted_triggers/ld_currency_national_triggers.txt`, `common/scripted_effects/ld_currency_national.txt`, `localization/english/ld_currency_national_l_english.yml`, `localization/russian/ld_currency_national_l_russian.yml` — национальные валюты по региону столицы (данные игры — `tools/data/vic3_strategic_regions.json`) |
| `regen_ef_cb_rate_loc` | `localization/<lang>/ld_cb_rate_panel_l_<lang>.yml` | — |
| `regen_ef_clearing` | `common/scripted_effects/ld_clearing.txt`, `common/script_values/ld_clearing_values.txt`, `common/scripted_guis/ld_cbfx.txt`, `localization/<lang>/ld_cbfx_l_<lang>.yml` | список валют (`ld_reserve_trade_values.txt`) |
| `regen_ef_customs_union` | `common/script_values/ld_customs_union_values.txt`, `common/scripted_triggers/ld_customs_union_triggers.txt` | ванильные товары (ПК) |
| `regen_ef_household_construction` | `common/pop_needs/ld_household_construction.txt`, `common/production_methods/ld_household_construction_pms.txt`, локализация | ванильные PM городского центра (ПК) |
| `regen_ef_listing` | `common/scripted_effects/ld_listing_switch.txt` | компании ванили (ПК) и `00_ef_companies.txt` |
| `regen_ef_metal_hoard` | `common/pop_needs/ld_metal_hoard.txt`, `localization/<lang>/ld_metal_hoard_l_<lang>.yml` | — |
| `regen_ef_monetary_policy` | `common/scripted_effects/ld_monetary_policy.txt`, `common/script_values/ld_monetary_policy_values.txt`, `common/scripted_triggers/ld_monetary_policy_triggers.txt`, `common/scripted_guis/ld_monetary_policy_buttons.txt`, `localization/<lang>/ld_monetary_policy_l_<lang>.yml` | — |
| `regen_ef_money_supply_loc` | `localization/<lang>/replace/ld_money_supply_replace_l_<lang>.yml`, `gui/ld_money_hook.gui`, `common/scripted_effects/ld_money_log_rest.txt` | — |
| `regen_ef_nr_deposits` | `common/scripted_effects/ld_nr_deposits.txt`, `common/script_values/ld_nr_deposits_values.txt`, `common/scripted_triggers/ld_nr_deposits_triggers.txt`, `common/static_modifiers/ld_fx_holders_demand.txt` | список валют (`ld_reserve_trade_values.txt`) |
| `regen_ef_pm_stock_hook` | `common/scripted_effects/ld_pm_stock_hook.txt` | `common/scripted_effects/01_financial_scripted_effects.txt` (`private_ownership_production_stocks` — правила) |
| `regen_ef_currency_formed` | `common/scripted_effects/ld_currency_formed.txt` (кроме `zz_ef_cf_reform`), `common/customizable_localization/ld_currency_formed_loc.txt` | `common/laws/01_ef_currency_type.txt` (теги `can_enact`), `common/scripted_effects/09_introduction_building_lvl.txt` (паритеты `introduction_of_<валюта>`) |
| `regen_ef_reserve_trade` | `common/script_values/ld_reserve_trade_values.txt` | `common/scripted_effects/01_economic_scripted_effects.txt` (валюты) |

Генератор ведёт только записи, которые есть в его файлах; в файле могут быть и рукописные записи. Законы денежной
политики, кнопки кредита ЦБ, панель экономики, сделки форекса и прочие места в файлах E&F правятся руками.

Не относятся к форку: `regen_ef_cmf_gui` (компач E&F × CMF), `regen_ef_tr_copies` (компач с T&R).
