# Валюта формируемой страны (R3.7)

**Что делало.** При `on_country_formed` у страны с ЦБ `zz_ef_cf_find` искал закон валюты E&F, в `can_enact` которого есть
новый тег (Германия → марка); есть и не действует — событие `ld_currency_formed.1` (ввести историческую валюту /
сохранить; ИИ 3 : 1). Реформа `zz_ef_cf_reform`: паритет — середина диапазона `introduction_of_<валюта>` E&F под стандарт,
запасы старой валюты в штатах всех стран → новой по отношению паритетов, закон валюты, лог `EFM|cur_reform`.
Решение — Д.R8а.7 (пользователь 8.10): в архив — новый тег и так получает свою валюту (Д.R8а.3).

**Вырезано (по исходным путям):** `common/scripted_effects/ld_currency_formed.txt`,
`common/customizable_localization/ld_currency_formed_loc.txt`, `events/ld_currency_formed_events.txt`,
`localization/{english,russian}/ld_currency_formed_l_*.yml` (остальные девять языков — копии английской, удалены);
генератор `tools/regen_ef_currency_formed.py` — в `vic3_mods/tools/_to_delete/`.

**Удалено из живых файлов:** `common/on_actions/ld_new_country_immediate_init.txt`, `zz_ef_newcountry_on_country_formed`,
после `zz_ef_country_init = yes`:
```
		if = {
			limit = { has_modifier = has_central_bank }
			zz_ef_cf_find = yes
			if = {
				limit = { has_variable = zz_ef_cf_target }
				trigger_event = { id = ld_currency_formed.1 days = 1 }
			}
		}
```

**Вернуть:** файлы — на прежние места, блок — обратно, генератор — из `_to_delete`; `python tools/ld_loc_langs.py`.
