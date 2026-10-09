# Ядро экономики E&F и прочее
Содержимое E&F вокруг денег: здания и методы производства (добыча серебра/золота, акции/облигации «частного владения», рыночная ликвидность, фин. центры, ЦБ), законы-пакеты (денежные системы 95 валют), модификаторы, технологии, журнальные записи, события, решения. Ядро расчётов — гигантские `scripted_effects`/`script_values`/`scripted_triggers`, из которых модель `ld_*` отключила часть веток (пустые тела) и переиспользует счета `gold_state_1`/`silver_state_1`.

## Файлы
### Здания и методы производства
- `common/buildings/ef_01_industry.txt`, `ef_02_agro.txt`, `ef_03_mines.txt` (кроме `building_silver_mine`), `ef_04_plantations.txt`, `ef_06_urban_center.txt`, `ef_09_misc_resource.txt`, `ef_11_private_infrastructure.txt` (порт, железная дорога, торговый центр) — `INJECT:building_<vanilla>` с добавлением `pmg_market_liquidity` и `pmg_private_ownership_{manufacture,agricultural,mining,railroad}_stock` в ванильные здания; `ef_11` также `INJECT:building_financial_district` (оценки инвестиций `bg_ef_private_construction_score`, `bg_financial_centre_score`, `bg_construction_score`).
- `common/buildings/ef_03_mines.txt:53` — новое `building_silver_mine` (группа `bg_silver_mining`, доступно только при `silver_mine_max_level`, 4 PMG).
- Частная стройка — PSC `common/buildings/zz_PSC_construction.txt` (`building_construction_sector`); здания E&F `building_ef_private_construction` в форке нет.
- `common/buildings/ef_15_bank.txt` — `building_bank` (центральный банк, `ownership_type = no_ownership`, PMG `pmg_minting_type`, `pmg_monetary_policy`). Частный банк — `buildings/ld_bank.txt`.
- `common/buildings/ef_16_financial_centre.txt` — `building_financial_centre` (общий, только в столице, нет, если уже есть национальный вариант) и 40 страновых вариантов `building_financial_centre_<tag>` (`arg aus bav bel bic brz chi chl den dei egy fra frm gbr gbr_2 gre hkh han ita jap mex net nsw ont peu por pru que rus saf sar sic spa swe swi tus tur uru usa usa_2 sax`), по ~44 строки каждый, одинаковые PMG (биржи 4 видов + `pmg_bond_exchange`).
- `common/production_method_groups/01_ef_industry.txt`, `02_ef_agro.txt`, `03_ef_mine.txt`, `11_ef_private_infrastructure.txt`, `15_ef_bank.txt`, `16_ef_financial_centre.txt` — PMG: `pmg_market_liquidity`, `pmg_private_ownership_{manufacture,agricultural,mining,railroad}_stock`, 4 PMG серебряной шахты, `pmg_minting_type`, `pmg_monetary_policy`, `pmg_currency_type`, `pmg_bond_exchange`, 4 биржи.
- `common/production_methods/00_ef_market_liquidity.txt` — `pm_no_market_liquidity` (по закону «без денежной системы»), `pm_market_liquidity_currency` (вход `goods_input_liquidity_currency_add = 28`).
- `common/production_methods/01_ef_industry.txt`, `02_ef_agro.txt`, `03_ef_mines.txt`, `11_ef_private_infrastructure.txt` — PM «частного владения» (`pm_no_private_ownership_*` / `pm_private_ownership_majority_*`: выход акций 12,5 на рабочую силу), PM серебряной шахты (кирка, насосы, взрывчатка, паровой осёл), `REPLACE:pm_company_headquarter_*` (16 ванильных PM штаб-квартиры с ослабленными акциями капиталистов).
- `common/production_methods/15_ef_bank.txt` — 6 PM стандарта (`pm_<fiat|silver|bimetallism|gold|gold_exchange|external_exchange>_standard_bank_money_currency`: выход `goods_output_bond_add` и `country_minting_add`), `pm_no_monetary_policy`/`pm_revaluation`/`pm_devaluation`.
- `common/production_methods/16_ef_financial_centre.txt` — `pm_bond_exchange` (выход `mutual_funds`, вход `bond`), 4 пары `pm_[no_]<kind>_stock_exchange` (вход акций).
- `common/building_groups/00_ef_building_groups.txt` — `bg_bank`, `bg_financial_centre`, `bg_ef_private_construction`, `bg_silver_mining`.
### Модификаторы
- `common/modifier_type_definitions/00_ef_building_modifier_types.txt` — 1,4 тыс. строк: `goods_input_<good>_add/_mult`, `goods_output_<good>_add/_mult` для 10 живых товаров (38 имён) и 95 имён несуществующих товаров (национальные валюты `<cur>_c`), которые читают значения `base_demande_<валюта>`; + `building_silver_mine_throughput`, `building_group_bg_financial_centre_throughput`.
- `.../00_ef_state_modifier_types.txt` — `state_sell_orders_local_currency_add`, `state_building_financial_centre[_<tag>]_max_level_add`, `state_building_silver_mine_max_level_add`.
- `.../00_ef_country_modifier_types.txt` — `country_credit_note_add/_mult`, `country_institution_economic_central_bank_max_investment_add`, `country_financial_product_by_trade_route_mult` (только строка в подсказке технологий; само действие — значение `financial_product_by_trade_route` по изученным технологиям), `country_change_gold_silver_ratio_bool`.
- `common/static_modifiers/00_ef_dynamic_modifier_country.txt` — страновые: `has_central_bank`, `has_financial_center`, `global_monetary_reference`, `foreign_exchange_controls`, `monetary_systeme_transition`, кризисы (`economic_instability`, `central_bank_bankruptcy_country`, `currency_crisis_country`, `economic_crisis_country`, `financial_crash_country`), `speculative_share_modifier_1..7`, `speculative_bubble_modifier`, `rise_base_rate`/`down_base_rate`, `devaluation_currency_*`/`revaluation_currency_*`, `country_credit_rating_AAA..D`, `strong/balanced/weak/extreme_weak_currency`, `no_money_production`, `inflation_country`/`deflation_country`, `economic_sentiment_index_modifier_1..3`.
- `.../00_ef_dynamic_modifier_state.txt` — штатные: `central_bank_place`/`_historic_place`, `financial_center_place*`, `looted_state`, `silver_mine_max_level`, `offshore_port`.
- `.../00_ef_dynamic_modifier_building.txt` — зданий: `financial_crash`, `economic_crisis`, `*_deemande` (спрос), `overbuilt_economy_modifier`, `modifier_desactive_bank/_building`.
- `.../00_ef_static_modifier.txt` — движковые `base_values`, `country_gdp`.
### Скрипты
- `common/scripted_effects/01_economic_scripted_effects.txt` — 100 тыс. строк, 36 эффектов (оглавление ниже).
- `common/scripted_effects/08_list_effect.txt` — 373 эффекта-построителя списков: `*_variable_list` рейтингов/ВВП/долгов (для GUI таблиц), `central_bank_debt_buyer_list_N_clear`, `central_bank_debt_privat_bank_buyer_list_N_clear` (25), `<cur>_currency_law_list` и `<cur>_c_global_variable_list` (по 95 валютам), `com_topbar_save_game_compatibility_EF`.
- `common/script_values/00_economic_scripted_value.txt` — 486 значений: `money_value`, `bimetallic_rate_gold_to_silver`, `central_bank_overlord_currency_purchases` (1333 строки), инфляция, цели девальвации/ревальвации.
- `common/scripted_triggers/00_ef_custom_trigger.txt` — 665 триггеров: `has_central_bank_*`, `is_valid_country_*`, `law_<cur>_monetary_system_{SS,BS,GS,GES,...}_trigger` (по 95 валютам), `market_owner_is_root*`, `is_subject_custom_trigger`.
### Прочее
- `common/decisions/00_ef_ai_loooting.txt` (ИИ-грабёж центробанка столицы).
- `common/ideologies/00_ef_ig_ideologies.txt` — 4 новые идеологии (`ideology_monetary_{moderate,conservative,left}`, `ideology_monetary_policy`) + `INJECT` оценок законов в 9 ванильных (`laissez_faire … socialist`).
- `common/institutions/00_ef_institutions.txt` — `institution_economic_central_bank`.
- `common/technology/technologies/ef_technology.txt` — 10 `REPLACE:` ванильных финтехнологий (`banking`, `currency_standards`, `central_banking`, `mutual_funds`, `corporate_charters`, `investment_banks`, `international_exchange_standards`, `joint_stock_companies`, `postal_savings`, `modern_financial_instruments`) и 7 своих (`debt_currency_exchange_regime`, `gold_exchange_standard`, `metalique_standard`, `financial_center`, `monetary_policy_tools`, `private_liquidity_provision`, `advanced_interbank_refinancing`).
- `common/messages/00_ef_messages.txt` (+ `ld_bubble_messages.txt`, `ld_pb_overbuild_messages.txt`) — 10 сообщений событий, `maturity_arrives_message`, `ai_selle_bond_maturity_1..10_message`, 4×8 `ai_privat_bank_*_bond_maturity_N_message`.
- `common/alert_types/00_ef_alert_types.txt` — 3 алерта: `fso_alert`, `selle_bond_maturity_yers_time_5_Y/_10_Y`; `PSC_alert_types.txt` — PSC.
- `common/journal_entries/00_ef_bank_central_je.txt` (`bank_je_central_1`), `00_ef_divers_je.txt` (`latin_monetary_union_je_1`, `scandinavian_monetary_union_je_1`, `silver_crisis_je_1`, `je_ef_efcc_situation`), `00_ef_financial_center_je.txt` (`financial_center_je_1`, `financial_center_je_2`); `common/journal_entry_groups/00_ef_journal_entries.txt` — `je_group_ef`.
- `events/00_ef_economic_event.txt` — 39 событий `00_ef_economic_event.<N>` (историческое объединение валют, ограбление, уведомления, идеологии).
- `common/defines/00_ef_defines.txt` (`NEconomy`: `PRICE_RANGE=0.99`, `GOODS_SHORTAGE_PENALTY_MAX=0.9`, `GOODS_SHORTAGE_PENALTY_MISSING_INPUTS=0.9` (движок требует ≥ MAX), `GOLD_RESERVE_RETURNS_FACTOR=0.0001`), `zz_ef_reinvestment_defines.txt` (`REINVESTMENT_SUBSISTENCE_FRACTION_REDUCTION=0`, `OWNER_COMPANY_PRIVATIZATION_CHANCE_MULTIPLIER=0.4`), `zzzz_ef_credit_def.txt` (`COUNTRY_MIN_CREDIT_SCALED=1.7`), `PSC_defines.txt`.
- `common/game_rules/00_EF_unique_companies_game_rules.txt` — `TRY_REPLACE` ванильных правил `unique_companies_banks`/`_newspapers`: по умолчанию `*_disabled`.

## Поток / порядок
Расчёт — по пульсам (см. `entry-points`): `ef_on_*_pulse_country` зовёт эффекты из `00_on_action_main.txt`, а те — эффекты `01_economic_scripted_effects.txt`. Оглавление `01_economic_scripted_effects.txt` (строка; эффект; кто живой):
| строки | группа | живое? |
|---|---|---|
| 18–470 | `global_monetary_reference_global_var_fixe`, `reference_currency_in_gold_fixe`, `median_currency_value`, `choose_currency_type_reset_all`, `global_gold_silver_production` | да (пульсы) |
| 480–1336 | `currency_of_player` (857) | `currency_of_player` — GUI; `currency_of_player_reset` — `_archive/ef_dead_effects_8_10/` |
| 1380–5967 | 3×95 эффектов `money_value[_target|_in_gold]_<cur>_global_var` | да, через `money_value_global_var` и др. |
| 5967–7574 | `global_monetary_reference_1/_2/_gui/_reset`, список эталонной валюты | да (годовой) |
| 7574–9776 | `fluctuations_*`, `cumulative_inflation_*`, 5 групп `inflation_on_<type>_market_value_fluctuations` + `_rolling_inflation_6_months_effect` + `reset_*` | да (месячный/годовой) |
| 9639–9776 | `monetary_policy_inflation[_reset|_reset_law|_base_rate]` | да (игрок) |
| 9776–11049 | `currency_strength_modifier`, `inflation_modifier`, `money_value_target_modification`, `devaluation/revaluation_money_value_target*` | да |
| 14226–16990 | `extreme_weak_currency_solution[_player]` (счётчик; ветка денежной реформы, `reset_balance`, `reset_law_event_currency`, `reset_debt_currency_reserve_and_export_value` — в `_archive/ef_currency_reform/`, R2), `reset_debt_in_currency` | да — из scripted_guis (кнопки смены закона) |
| 41132–41987 | `devaluation_on`, `revaluation_on`, `set_reset_monetary_system_status`, `on_activate_*_law` | — |
| 41385 | `trade_balance` (388) | да (месячный) |
| — | `stockpiling_currency`, `stockpiling_currency_type_1` — в `_archive/ef_stockpiling_currency/` (R2) | — |
| 42340–90729 | 95 `sell_<cur>_currency_crisis` (`buy_/sell_<cur>_currency` ИИ-форекса — в `_archive/ef_ai_forex/`) | да, из `all_currency_resold`; пишут `gold_state_1`/`silver_state_1` |
| 92195, 104223 | `reset_debt_in_national_currency[_player]` (2×2 тыс. строк) | да (GUI/смена закона) |
| 94312–98727 | `stockpiling_capital_state_transfert`, `..._financial_center_place`, `enemy_capital_is_occuped` (1,8 тыс.), `enemy_stats_is_occuped` | да (месячный, решение ИИ, бой) |
| 98819–104131 | `central_bank_production_methods`, `_3`, `_4` — пустые определения (тела в `_archive/ef_central_bank_pm_consuption/`) | пусто |
| 106333–107230 | `remove_suject_currency`, `subject_currency` | живые (подданные; неподданный на чужом рынке — со своей системой, Д.R8а.3) |
Внутри E&F-тел встроены вызовы модели: `zz_ef_cb_rate_step`, `zz_ef_std_switch_*`, `zz_ef_mp_init/_clear`, `zz_ef_crisis_redeem` (95), `zz_ef_cb_cover`, `zz_ef_cover_normal` (по 95 валютам в `sell_<cur>_currency_crisis`).

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `gold_state_1`, `silver_state_1` (штат) | запас металла штата (ЦБ-штат — резерв ЦБ; в модели `ld_*` — резерв ЦБ) | history, `sell_<cur>_currency_crisis`, кнопки форекса, `enemy_capital_is_occuped`, `zz_ef_*` | `gold_state_native_for_stockpile`, `zz_ef_cbm_gold/silver` |
| `money_value_<cur>` / `money_value_target_<cur>` / `money_value_in_gold_<cur>` (глобальные) | курс валюты, цель и в золоте по каждой из 95 валют | `money_value[_target|_in_gold]_<cur>_global_var` | инфляция, GUI |
| `base_rate_percentage`, `rise_base_rate`, `down_base_rate` | ставка ЦБ; модификаторы направления | `zz_ef_cb_rate_step` | `central_bank_ef_on_monthly_pulse_country`, PSC |
| `speculative_share_1` / `_2` | пузырь / индекс перестройки | `ld_bubble`, `ld_pb_overbuild_counter` | JE `financial_center_je_2` |
| `looting_1_year` | флаг грабежа | `enemy_capital_is_occuped`, годовой пульс | `ef_on_yearly_pulse_reset` |
| `global_var:money_value_median` | медиана курсов | `median_currency_value` (`zz_ef_world_month_ef`, `ld_world_month.txt`) | `is_reference_currency` |

## Вызовы и связи
- Законы: 95 `law_<cur>_currency` (`laws/01_ef_currency_type.txt`), `law_*_standard`, `lawgroup_monetary_policy`, соотношение биметаллизма `zz_ef_bimet_ratio` — триггеры `law_<cur>_monetary_system_*_trigger` (customizable_localization `00_ef_localization_ custom.txt`, GUI).
- Здания ↔ PM ↔ товары: `pmg_market_liquidity` вставлена в ванильные здания (`goods_input_liquidity_currency_add = 28`); PM «частного владения» производят акции; фин. центр потребляет акции/облигации и производит `mutual_funds`; банк `ld_bank` производит `liquidity_currency`.
- Решения: `00_ef_ai_loooting_decisions_1` (ИИ при `enemy_capital_is_occuped >= 1`) → `enemy_capital_is_occuped` + событие `00_ef_economic_event.35`.
- События `00_ef_economic_event.1..35, 56..65, 95, 96, 106, 107` — из `ef_on_yearly_pulse_event_at_date`, `enemy_capital_is_occuped`, решений (`.95/.96` звал арбитраж — в `_archive/ef_bimetallic_arbitrage/`, сейчас без вызова); сообщения `00_ef_economic_event_<N>_message`.
- Алерты (`alert_types`) движок обходит сам: регистрация по папке, `valid` определяет показ; в `trigger`/GUI на них ссылок нет, это норма.
- Идеологии: `ideology_monetary_*` раздаются ИГ в `99_ef_history_global_variable.txt:~8000` (`add_ideology`), оценки законов читает движок.

## Логи
В файлах этой подсистемы единственная группа логов — `EFE` (`scripted_effects/08_list_effect.txt:210,267,288`, `national_capacity_variable_list`, годовой). Остальные — в `entry-points`.

## Прочие файлы E&F
- Здания и PM добычи и сельского хозяйства: `common/buildings/ef_02_agro.txt`, `common/buildings/ef_04_plantations.txt`, `common/buildings/ef_09_misc_resource.txt`
  `common/buildings/ef_06_urban_center.txt` (`INJECT` групп PM ликвидности и акций в ванильные
  здания); PM и группы — `common/production_methods/02_ef_agro.txt`, `common/production_methods/03_ef_mines.txt`,
  `common/production_methods/11_ef_private_infrastructure.txt`, `common/production_method_groups/02_ef_agro.txt`,
  `common/production_method_groups/03_ef_mine.txt`, `common/production_method_groups/11_ef_private_infrastructure.txt`.
- Типы модификаторов: `common/modifier_type_definitions/00_ef_country_modifier_types.txt`,
  `common/modifier_type_definitions/00_ef_state_modifier_types.txt`; модификаторы:
  `common/static_modifiers/00_ef_static_modifier.txt` (`INJECT:base_values`: чеканка, наличность зданий),
  `common/static_modifiers/00_ef_dynamic_modifier_building.txt`, `common/static_modifiers/00_ef_dynamic_modifier_state.txt`.
- `common/defines/zzzz_ef_credit_def.txt` — `NEconomy.COUNTRY_MIN_CREDIT_SCALED`.
- `common/decisions/00_ef_ai_loooting.txt` — решения ИИ с ЦБ (грабёж резервов).
- `common/prestige_goods/00_ef_prestige_goods_2.txt` — пусто: `manufacture_stock_usa` выключен (у `manufacture_stock` уже три престижных товара — предел движка).
- `common/customizable_localization/00_ef_localization_ custom.txt` — имя валюты страны (`currency_name` — по `var:zz_ef_cur_noun`, «<прилагательное страны> <слово>»; `currency_symbol*` — по `var:zz_ef_cur`, генератор `regen_ld_currency_data`; пробел в
  имени файла — авторский).
