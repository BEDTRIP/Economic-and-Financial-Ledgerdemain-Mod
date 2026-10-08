# Соотношение биметаллизма — группа законов E&F

**Что делало.** Группа `lawgroup_bimetalism_ratio` (законы `law_bimetallic_ratio_no/10/15/20`, иконки) и 7 поправок
закона 15:1 (`amendment_*_bimetallic_ratio*`: Франция 15,5, латинский союз 15,5, США 1834 — 16,1 и 1873, Испания 15,1,
Германия 14,5, Нидерланды 15,6) задавали законное соотношение золота к серебру (`bimetallic_rate_gold_to_silver`).
Каждый закон стандарта включал «без соотношения», биметаллизм — 15:1; позиции идеологий групп интересов по группе.
Решение — Д.R8а.11 (пользователь 8.10): соотношение — параметр биметаллического стандарта `var:zz_ef_bimet_ratio`.

**Вырезано (по исходным путям):** `common/laws/01_ef_bimetalism_ratio.txt`, `common/amendments/00_ef_amendments.txt`,
`gfx/interface/icons/law_icons/law_bimetallic_ratio_*.dds`, `localization/{english,russian}/00_ef_amandement_localization_l_*.yml`
(остальные языки — копии, удалены); куски — `common/law_groups/01_ef_laws.txt` (группа),
`common/ideologies/00_ef_ig_ideologies.txt` (7 блоков `lawgroup_bimetalism_ratio = { … }`),
`common/script_values/00_economic_scripted_value.txt` (прежнее тело `bimetallic_rate_gold_to_silver`),
`common/scripted_effects/10_new_country_var.txt` и `99_ef_history_global_variable.txt` (включение «без соотношения»
стране без закона группы), `99_ef_history_global_variable.txt` и `00_ef_divers_je.txt` (поправки),
`localization/{english,russian}/01_ef_law_localization_l_*.yml` (10 ключей закона и группы).

**Удалено / заменено в живых файлах:**
- `common/laws/01_ef_monetary_system.txt`: 6 строк `activate_law = law_type:law_bimetallic_ratio_no` в `on_activate`
  стандартов; у `law_bimetallism_standard` `activate_law = law_type:law_bimetallic_ratio_15` → `zz_ef_bimet_ratio = 15`,
  если своего нет.
- `money_value_target_pre_set` (значение `00_economic_scripted_value.txt` и эффект `01_economic_scripted_effects.txt`),
  `set_reset_monetary_system_status`: условия `has_law = law_type:law_bimetallic_ratio_*` рядом с законом стандарта.
- История: `activate_law = law_type:law_bimetallic_ratio_15` (FRA, USA, NET ×2) и `add_amendment` → `set_variable =
  { name = zz_ef_bimet_ratio value = 15.5 / 16.1 / 15.6 }`; журнал латинского союза — `15.5`.
- `bimetallic_rate_gold_to_silver`: `var:zz_ef_bimet_ratio` при биметаллизме, иначе `gold_to_silver_rate`.

**Вернуть:** файлы и куски — на прежние места; строки — по списку.
