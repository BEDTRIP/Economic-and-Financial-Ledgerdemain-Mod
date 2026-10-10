# Законы валют E&F

**Что делало:** группа законов `lawgroup_currency_type` («Суверенные деньги») — 95 законов `law_<cur>_currency` и
`law_no_market_liquidity` (нет валюты). Закон и был валютой страны: его ставили история E&F (35 `activate_law`) и ввод
валюты (`introduction_of_<cur>`, 95 `activate_law`), `on_activate` писал `var:zz_ef_cur`; E&F проверял валюту законом в
2190 местах (цепочки денег `money_value_<cur>`, списки, окна, кастомная локализация). Модификаторов у законов не было
(`can_enact` — ЦБ и теги E&F, `progressiveness = 25`).

**Чем заменено:** R8в, шаг 5 — валюта — данные (`var:zz_ef_cur = flag:<cur>`, Д.R8а.2): история и ввод валюты ставят
переменную (`set_variable` + `zz_ef_cur_name_set`), новая страна без банка — снимает её, проверки E&F —
`var:zz_ef_cur ?= flag:<cur>`; союз хранит свою валюту члена (`var:zz_ef_mu_cur_own`). Список валют генераторов —
`../vic3_mods/tools/data/ld_currencies.txt`. `docs/currencies.md`.

**Удалено из живых файлов:**
- `common/laws/01_ef_currency_type.txt` — целиком (здесь);
- `common/law_groups/01_ef_laws.txt` — `lawgroup_currency_type` (здесь);
- `common/history/global/99_ef_history_global_variable.txt` — 35 `activate_law = law_type:law_<cur>_currency` →
  `set_variable = { name = zz_ef_cur value = flag:<cur> }` + `zz_ef_cur_name_set = yes`;
- `common/scripted_effects/09_introduction_building_lvl.txt` — 95 таких же `activate_law` → то же;
- `common/scripted_effects/00_on_action_main.txt` — 2 `activate_law = law_type:law_no_market_liquidity` (новая страна
  без банка) → снятие `var:zz_ef_cur` и `zz_ef_cur_set`;
- 2190 `has_law = law_type:law_<cur>_currency` в 9 файлах E&F → `var:zz_ef_cur ?= flag:<cur>`;
- `zz_ef_cur_set` (`ld_currency_var.txt`, генерат) — цепочка «закон → переменная» снята;
- локализация всех 11 языков — `lawgroup_currency_type`, `law_no_market_liquidity`, `law_<cur>_currency` (+ `_desc`)
  (английская и русская — здесь, `localization/`).
