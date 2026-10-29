# Здание ЦБ E&F (`building_bank`)

Вынуто R9б.4 по Д.R9б.1 (исполняет Д.R4а.9, Д.R5.11): центральный банк — модификатор страны `has_central_bank`, не
здание; что здание делало своими методами — чеканка, база закупки металла, выпуск товара «облигации» — теперь от размера
ЦБ (`common/script_values/ld_cb_size_values.txt`, `common/scripted_effects/ld_cb_size.txt`; `docs/код/central-bank.md`).

**Что делало здание.** Государственное здание в столице (`ownership_type = no_ownership`, группа `bg_bank` —
`is_government_funded`, зарплаты из бюджета, прибыль — казне), 75 рабочих мест на уровень (25 бюрократов, 50 клерков).
Уровни — размер ЦБ: история — 5 или 20, каждый год `macro_facilities_bc` достраивала до 5 × `var:gdp_view` (5 уровней на 5
млн ВВП; переключатель на 1000 веток), экономический кризис сносил и ставил 5. Методы `pmg_minting_type` по закону
стандарта: `country_minting_add` на единицу рабочей силы (фиат 250, металлические и внешний — 1000, золотодевизный —
2500), вход бумаги 1–2, металла (золото 1, серебро 10, биметалл 1 + 5 — вход выключен модификатором `zz_ef_cb_metal_buy`
−100 %, металл покупают «Банки», Д.R4а.9; вход читался как база закупки денежной власти), выход «облигаций» 10;
`pmg_monetary_policy` — `country_minting_mult` ±25 % при `law_revaluation` / `law_devaluation`. Модификаторы здания:
`zz_ef_cb_bond_issuance_low/_high` (выпуск облигаций по долгу / ВВП), `currency_demande` (выход валюты — у методов его
нет, без действия), `modifier_desactive_bank` (оккупация столицы — пропускная −100 % на 12 месяцев: облигаций нет; на
чеканку не влиял).

**Чем заменено:**
| было | стало |
| --- | --- |
| здание есть (`has_building`, `any_scope_state`) | `has_modifier = has_central_bank` |
| уровни здания | `var:zz_ef_cb_size` (`zz_ef_cb_size_update`: не меньше 5 × `gdp_view`, не убывает; история — 5 / 20; кризис — 5) |
| чеканка методом | `zz_ef_cb_minting` × `zz_ef_cb_mint_v` (величина метода стандарта × размер; здания стояли полностью укомплектованными — сейв 1838: `staffing` = уровни) |
| ±25 % методом политики | `zz_ef_cb_mint_reval` / `_deval` при законе и ЦБ |
| база закупки металла — вход метода | `zz_ef_cb_bldg_base_*_goods` = величина стандарта × размер |
| выпуск «облигаций» зданием | метод `pm_zz_ef_bank_bonds` «Банков» (открыт законами ЦБ), выпуск страны — 10 × размер × множитель долга, `goods_output_bond_mult` на каждом «Банке» |
| рабочие места ЦБ | не перенесены (Д.R9б.1) |
| оккупация столицы гасит облигации | нет |
| `market_owner_is_root_univ_with_buiding` — метод внешнего стандарта у здания | ЦБ и закон `law_external_exchange_standard` |
| `base_demande_currency / _silver / _gold / _<валюта>` — модификаторы здания через `scope:central_bank_scope` (его выход валюты, вход металла и валют) | 0, база закупки металла по стандарту × размер, 0 (`central_bank_metal_purchases` — чеканка от закупки металла — как была) |
| `[GetBuildingType('building_bank').GetName]` в локализации (44 места, 11 языков) | название ЦБ языка текстом |

Сейвы со зданием: тип здания снят, загрузку сейва до R9б.4 не проверяли (новые игры) — принято ночью, проверить.

**Удалено из живых файлов** (вырезанное — здесь по исходным путям):
| файл | что |
| --- | --- |
| `common/buildings/ef_15_bank.txt`, `common/production_methods/15_ef_bank.txt`, `common/production_method_groups/15_ef_bank.txt`, `common/scripted_effects/ld_cm_bank_ownership.txt` | файлы целиком (здание, 9 методов, 2 группы, `zz_ef_cm_create_owned_bank`) |
| `gfx/interface/icons/production_method_icons/{fiat,silver,bimetallism,gold,gold_exchange,external_exchange}_standard.dds`, `no_monetary_policy.dds` | иконки методов (`central_bank.dds`, `revaluation.dds`, `devaluation.dds` нужны живым файлам — остались) |
| `common/building_groups/00_ef_building_groups.txt` | `bg_bank` |
| `common/static_modifiers/00_ef_dynamic_modifier_building.txt` | `modifier_desactive_bank`, `currency_demande` |
| `common/static_modifiers/ld_metal_trade.txt` | `zz_ef_cb_metal_buy` |
| `common/script_values/ld_metal_accounts_values.txt` | `zz_ef_cb_bldg_base_*_goods` по входу здания, `zz_ef_cb_bldg_buy_off` |
| `common/scripted_effects/ld_metal_accounts.txt` | условие базы по зданию; выключатель входа здания |
| `common/script_values/ld_cb_bond_issuance_values.txt` | `zz_ef_cb_bond_output_low/_high` |
| `common/scripted_effects/ld_cb_bond_issuance.txt` | тело `zz_ef_cb_bond_issuance_update` по зданию (переписано на «Банки») |
| `common/scripted_effects/09_introduction_building_lvl.txt` | в `central_bank_modifier` — условие по зданию и блок здания (`central_bank_modifier_fixed_var`, `currency_demande`); фондовая биржа-лидер — `has_building`; ветка ЦБ в `remove_country_building_modifier` и `destroy_building_not_allowed`; `reset_building`; `initialize_historic_macro_facilities_bc` — создание здания; `macro_facilities_on_action_bc` / `macro_facilities_bc` — переключатель на 1000 веток; `central_bank_respawn_after_crisis`; `economic_crisis_destroy_central_bank` — снос и 5 уровней; `has_currency_law_but_no_building_central_bank`, `introduction_new_currency` — условие и создание здания |
| `common/scripted_effects/00_on_action_main.txt` | новая страна — условия и снос здания; `update_modifiers_bc_fc_ns` — условие по зданию |
| `common/scripted_effects/ld_cb_law.txt` | `zz_ef_cb_found` — создание, `zz_ef_cb_close` — снос |
| `common/scripted_effects/01_economic_scripted_effects.txt` | `monetary_policy_inflation_reset_law` — метки девальвации на здании; оккупация столицы — `modifier_desactive_bank` |
| `common/scripted_triggers/00_ef_custom_trigger.txt` | `market_owner_is_root_univ_with_buiding` — метод здания |
| `common/script_values/00_economic_scripted_value.txt`, `01_economic_currency_scripted_value.txt` | `scope:central_bank_scope.modifier:…` в `base_demande_*` (98 значений) — заменены на месте, не вырезаны |
| `common/history/buildings/00_ef_building.txt` | параметр `BANK_BLDG_TYPE` двух вызовов `initialize_historic_macro_facilities_bc` |
| `localization/*/01_ef_building_localization_l_*.yml`, `01_ef_production_method_localization_l_*.yml` | ключи здания, групп и методов |

**Вернуть:** файлы и иконки — на место; вырезанные куски — по их файлам; новые `ld_cb_size*` и метод облигаций
«Банков» (`pmg_zz_ef_bank_bonds`) — снять; `[GetBuildingType('building_bank').GetName]` — в локализацию.
