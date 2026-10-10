# Латинский и Скандинавский союзы E&F

**Что делало:** записи дневника `latin_monetary_union_je_1` (Франция с 1860 года, игрок в Европе) и
`scandinavian_monetary_union_je_1` (лидер скандинавских стран по списку `scandinavian_leader_list_1`) вели «переговоры»
событиями `00_ef_economic_event.8–12` и `.19–24`: кнопки записей (`latin_/scandinavian_monetary_union_1/2_button`)
ставили переменные `*_on_discution`, полосы `*_progress_bar` считали страны в переговорах
(`*_monetary_union_country_in_debat`), последнее событие создавало договор со статьёй `latin_monetary_union_treaty` /
`scandinavian_monetary_union_treaty` (`common/treaty_articles/16_…`, `17_…`). Статьи денежных эффектов не имели — только
лоббийное умиротворение; общей валюты не было.

**Чем заменено:** R8в, шаг 4 (Д.R8в.13, Д.R8в.16) — статья «Монетарная интеграция»
(`common/treaty_articles/ld_monetary_integration.txt`) и записи `ld_latin_union_je` / `ld_scandinavian_union_je`
(`common/journal_entries/ld_monetary_union_je.txt`); `docs/currencies.md`, «Валютные союзы».

**Удалено из живых файлов** (вырезанное — здесь по исходным путям):
- `common/treaty_articles/16_latin_monetary_union_treaty.txt`, `17_scandinavian_monetary_union_treaty.txt` — целиком;
- `common/journal_entries/00_ef_divers_je.txt` — `latin_monetary_union_je_1`, `scandinavian_monetary_union_je_1`
  (закомментированные ссылки на них в `silver_crisis_je_1` остались комментариями);
- `common/scripted_buttons/00_ef_buttons.txt` — 4 кнопки с комментариями-заголовками;
- `common/scripted_progress_bars/00_ef_progressbar.txt` — `latin_/scandinavian_monetary_union_progress_bar`;
- `common/script_values/00_economic_scripted_value.txt` — `latin_/scandinavian_monetary_union_country_in_debat`;
- `events/00_ef_economic_event.txt` — события `.8`, `.9`, `.10`, `.11`, `.12`, `.19`–`.24`;
- `common/scripted_effects/10_new_country_var.txt` — 5 `set_variable` (`scandinavian_monetary_union_initiator`,
  `_on_discution`, `_time`, `latin_monetary_union_on_discution`, `_time`);
- `common/scripted_effects/08_list_effect.txt` — `scandinavian_leader_list_1_list`; его вызов в
  `central_bank_ef_on_five_year_pulse_country` (`00_on_action_main.txt`:
  `every_country = { limit = { global_country_ranking = 1 } scandinavian_leader_list_1_list = yes }`);
- `common/script_values/00_economic_scripted_value.txt` — `rate_by_law_metal_type_FRA`, `rate_by_law_metal_type_2_FRA`
  (читала только локализация статьи Латинского союза); `common/scripted_effects/01_economic_scripted_effects.txt` —
  `reset_debt_in_currency_for_monetary_systeme_transition` (звали только архивные события);
- локализация всех 11 языков — ключи `latin_monetary_union*`, `scandinavian_monetary_union*`, `status_*` этих записей,
  `00_ef_economic_event.{8–12,19–24}.*`, `treaty_name_union_latine`, `treaty_name_scandinavian_monetary_union`,
  `has_treaty_*_monetary_union_treaty_with_trigger` (английская и русская — здесь, `localization/`).
