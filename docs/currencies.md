# Валюты, законы, стандарты, эталон, валютные зоны, союзы
Каждая страна с ЦБ имеет закон валюты (`lawgroup_currency_type`, 95 законов E&F) и закон денежной системы (серебро / биметаллизм / золото /
золотодевизный / фиат / внешний). Курс валюты — «паритет» `var:money_value_target_1` (металл на единицу). Одна страна-эталон
(`global_monetary_reference`) — база для «силы» остальных валют; сила двигает торговлю. Подданный входит в валютную зону сюзерена.
Таможенный союз даёт члену свою валюту на чужом рынке. Деньги-как-товар (`<cur>_c`, 57 валют) — в других подсистемах; здесь только определения E&F.

## Файлы
- `common/law_groups/01_ef_laws.txt` — группы законов: `lawgroup_monetary_policy`, `lawgroup_monetary_system`, `lawgroup_currency_type`, `lawgroup_bimetalism_ratio` (группа ратио биметаллизма; видимость по биметаллизму не задана).
- `common/laws/01_ef_currency_type.txt` — 95 законов `law_<cur>_currency` + `law_no_market_liquidity` (нет валюты). Одинаковая форма: `can_enact` = `has_modifier = has_central_bank` + список тегов, которым E&F выдаёт валюту в истории; 39 законов с `always = no` (товар закомментирован / вырезан под лимит 128 товаров); `unlocking_technologies = currency_standards`.
- `common/laws/01_ef_monetary_system.txt` — `law_no_monetary_system`, `law_fiat_standard`, `law_silver_standard`, `law_bimetallism_standard`, `law_gold_standard`, `law_gold_exchange_standard`, `law_external_exchange_standard`; `on_activate` зовёт `on_activate_monetary_system_law` (01_economic_scripted_effects.txt:27957, тело E&F + `zz_ef_std_switch_before/_after`).
- `common/laws/01_ef_bimetalism_ratio.txt` — `law_bimetallic_ratio_no/10/15/20` (соотношение золото:серебро).
- `common/laws/01_ef_monetary_policy.txt` — `law_no_monetary_policy`, `law_revaluation`, `law_devaluation`, `law_large_monetary_policy` (на уровне ЦБ: `central-bank.md`).
- `common/script_values/01_economic_currency_scripted_value.txt` (294 тыс. строк, 93 повтора на валюту; индекс ниже).
- `common/script_values/ld_reference_currency_values.txt` — сила валюты к эталону, торговый множитель, металл в золоте, учётные значения для карточек банка (`zz_ef_bank_capital`, `zz_ef_v_d_*`, `zz_ef_fx_money`, `zz_ef_bank_assets/liabilities`), торговля неделя.
- `common/scripted_triggers/ld_reference_currency_triggers.txt` — `zz_ef_reference_candidate`.
- `common/scripted_effects/ld_reference_strength.txt` — `zz_ef_reference_strength_step`, `zz_ef_currency_trade_step`.
- `common/scripted_effects/ld_standard_switch.txt` — `zz_ef_std_switch_before/_after`: смена стандарта сохраняет стоимость денег в золоте.
- `common/scripted_effects/ld_currency_zone.txt` (генерируется `tools/regen_ef_currency_zone.py`) — `zz_ef_cur_zone_step`, `zz_ef_cur_zone_currency` (667 строк: цепочка `else_if` по 95 законам).
- `common/scripted_triggers/ld_currency_zone_triggers.txt` — `zz_ef_cur_zone_has_currency` (OR по 95 законам).
- `common/script_values/ld_customs_union_values.txt`, `common/scripted_triggers/ld_customs_union_triggers.txt` (генерируются `tools/regen_ef_customs_union.py`) — `zz_ef_cu_member`, `zz_ef_currency_own`, `zz_ef_member_goods_net` (по товарам, 324 строки), `zz_ef_members_trade_sum`.
- `common/history/global/zz_ef_currency_fix.txt` — старт: опечатка WUR (`law_gulden_south_german_gulden_currency`), 13 стран без валюты → `law_no_market_liquidity`; страны с подушным налогом без технологии `currency_standards` (E&F перенёс её в эру 2) получают её (метка `zz_ef_start_currency_standards` — `on_researched` E&F не переводит их в фиат). Грузится после `99_ef_history_global_variable.txt`.
- `common/treaty_articles/16_latin_monetary_union_treaty.txt`, `common/treaty_articles/17_scandinavian_monetary_union_treaty.txt` — статьи договоров (флаги, `can_ratify`, `on_entry_into_force` только лоббийное умиротворение). Денежных эффектов нет.
- `common/scripted_triggers/00_ef_custom_trigger.txt` — `is_reference_currency` (:582), `is_reference_currency_no` (:587), `is_strong/balanced/weak_currency` (:592-:637, тело E&F, сравнение с `zz_ef_currency_strength` вместо медианы), `is_extreme_weak_currency` (:623), `law_currency_enacted` (:1134), `market_goods_is_currency` (:1423).
- `common/scripted_effects/08_list_effect.txt` :202 `national_capacity_variable_list` — раз в год (`ef_on_yearly_pulse_country`, `on_actions/00_ef_on_action.txt:139`) выбор эталона: кандидаты `zz_ef_reference_candidate`, по `national_capacity_in_gold`, позиция 0 → модификатор `global_monetary_reference`; лог `EFE|`.
- Прочее E&F: `common/scripted_effects/09_introduction_building_lvl.txt:34328` `introduction_new_currency` (выдача валюты/паритета при исследовании; зовёт `zz_ef_cur_zone_step` через `ld_currency_intro_metal.txt:75`).

### Индекс `01_economic_currency_scripted_value.txt` (на каждую валюту `<cur>`)
- :228-:294 общие `base_demande_currency*`, `target_demand_currency*`, `enough_foreign_currrency`.
- :1926 `leading_currency_type`; :2800.. `currency_of_player_is_<cur>` = `global_var:currency_of_player_is_<cur>` (это script_value, не триггер; глобальные переменные обнуляются в `common/history/global/00_ef_economic_global_variable.txt:31568..`); :2966 `currency_of_player` (сумма).
- :3306.. `money_value_<cur>` = `global_var:money_value_<cur>_global_var`; `money_value_<cur>_target`, `money_value_in_gold_<cur>`, `money_value_<cur>_related_to_country_law` (:4854, пересчёт под стандарт).
- :7788 `is_reference_type`; :8476 `money_supply_state` (+`_monthly`) — цепочка `if has_law <cur>_currency add stockpiling_<cur>_state`.
- :8871 `pop_savings`, :9066 `pop_savings_monthly`; :15013.. `<cur>_c_market_goods_*`, `stockpiling_<cur>_state/_private_bank`, `<cur>_c_total/global_stokpile`; `buy_/sell_<cur>_in_gold_market_panel`.
- :24090 `buy_sell_currency_in_metal_market_panel` (его читает GUI биржи валют).
- :277203.. торговля в золоте: `export_/import_to/from/in_<cur>`, `*_value_in_gold(_week)`, `trade_balance_*`, `debt_in_national_currency_*`, `excess_foreign_state_currency_*`, `currency_identifiers_<cur>`, `valid_<cur>_metal_reserve_type`.

## Поток / порядок
- Старт: `99_ef_history_global_variable.txt` выдаёт законы валют → `zz_ef_currency_fix.txt` правит WUR и 13 стран.
- Раз в месяц (`zz_ef_money_model_monthly_step`, `ld_money_model.txt:1005..`): `zz_ef_cur_zone_step`; `zz_ef_reference_strength_step`; `zz_ef_currency_trade_step` (после шага эталона; только страны с ЦБ, не эталон).
- Раз в год (`ef_on_yearly_pulse_country`, `on_actions/00_ef_on_action.txt:139`, зовёт страна-эталон): `national_capacity_variable_list` → пересев эталона. Кандидат: великая держава, ЦБ, рейтинг ≥ 6 (BBB), металлический/золотодевизный стандарт, нет дефолта ЦБ, покрытие ≥ 25%.
- Смена закона стандарта: `on_activate_monetary_system_law` → `zz_ef_std_switch_before` (запомнить стандарт и паритет) → тело E&F → `zz_ef_std_switch_after` (пересчёт паритета по `silver_to_gold_rate`/`gold_to_silver_rate`, перевод запасов `silver_state_1`↔`gold_state_1` в столичных штатах с `central_bank_historic_place`).
- Зона: подданный (≥13 недель `zz_ef_weeks_run`), сюзерен с ЦБ, металл. стандарт и валюта → подданный получает стандарт, валюту и паритет сюзерена, `monetary_systeme_transition` на 2 мес. Иначе `zz_ef_cur_zone` снимается.

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `var:money_value_target_1` | паритет (металл на единицу) | история E&F, `zz_ef_std_switch_after`, `zz_ef_cur_zone_step`, `zz_ef_mp_complete` | `zz_ef_value_to_parity`, `zz_ef_metal_target_in_gold`, `zz_ef_cur_zone_step`, `zz_ef_mp_can_work` |
| `global_var:money_value_<cur>_global_var` | курс валюты `<cur>` | E&F | `money_value_<cur>` |
| `global_var:money_value_median` | медиана E&F | E&F | `zz_ef_value_to_parity` (запасной путь), `is_reference_currency` |
| `global_var:zz_ef_ref_vtp` | value_to_parity эталона | `zz_ef_reference_strength_step` | `zz_ef_currency_strength` |
| `zz_ef_std_old`, `zz_ef_std_parity_old/_new` | старый стандарт (1 серебро, 2 би, 3 золото) и паритет при смене | `zz_ef_std_switch_*` | они же |
| `zz_ef_cur_zone` | сюзерен, чью зону держит страна | `zz_ef_cur_zone_step` | `zz_ef_mp_can_work` |
| `zz_ef_member_trade` | торговый счёт члена ТС за неделю | приёмник денег (`ld_money_model.txt`) | `zz_ef_members_trade_sum` |
| `global_monetary_reference` | модификатор эталона | `08_list_effect.txt:300-306` | `zz_ef_currency_trade_step`, `is_*_currency` |
| `zz_ef_currency_trade` | модификатор торговли от силы (`static_modifiers/ld_currency_trade.txt`), множитель `zz_ef_currency_trade_m` = (1 − сила)×40, в −10..10 | `zz_ef_currency_trade_step` | движок |

## Вызовы и связи
- Сила: `zz_ef_currency_strength` = `zz_ef_value_to_parity` / `global_var:zz_ef_ref_vtp`; пороги 1.25 / 0.75 (`is_strong/weak_currency`). Подмена E&F: `difference_with_average_gold_exchange_rate_currencies`, `money_value_median_and_money_value_in_gold_ratio` (`00_economic_scripted_value.txt:4707, 8279`).
- `zz_ef_cb_cover`, `zz_ef_value_floor_cover` (0.25) — `ld_money_model_values.txt`; `zz_ef_reference_candidate` и риск-премия читают их.
- Членство в ТС: `zz_ef_cu_member` читают `ld_money_model.txt`, `ld_clearing_values.txt`, `00_economic_scripted_value.txt` (`money_value`/`money_value_in_gold` для члена).
- `zz_ef_privbank_interest_due` — `ld_money_model.txt`.
- Договоры: `latin_monetary_union_treaty` создаётся событием `events/00_ef_economic_event.txt:499`, ЖЗ `latin_monetary_union_je_1` (`journal_entries/00_ef_divers_je.txt:1`) проверяет статью.
- GUI: биржа валют (`buy_sell_currency_in_metal_market_panel`, `buy_/sell_<cur>_in_gold_market_panel`), карточки банка (значения `zz_ef_v_*`), панель ставки (`gui/ld_cb_rate_panel.gui`, другой документ).

## Логи
- `EFM|…|std_switch|old …` — смена стандарта (`ld_standard_switch.txt:130`).
- `EFE|…|note…|cover…|std…|cb…|ref…`, `EFE|…|cand`, `EFE|…|pick` — кандидаты и выбор эталона (`08_list_effect.txt:210`).
