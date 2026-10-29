# Проба R4а.1 (Р25): компания, созданная скриптом

**Что делало:** `ld_probe_cb.0` (только из консоли) через 30 дней выдаёт Великобритании, России, Франции и Швеции
компанию `company_ld_probe_cb` (`add_company`, здание «Банк» в типах), затем два года раз в месяц пишет
`EFZ|…|cb_probe|…`: есть ли компания, компаний и предел (`max_num_companies`), её уровни.

**Итог (прогон r1011_231834, старт 1836):**
- `add_company` работает в скрипте: компания появляется сразу, число компаний +1; предел не проверяется — у Швеции
  3 при пределе 2.
- Компания без уровней в собственности **исчезает в течение месяца** у всех четырёх (31.1.1836 есть, 2.3.1836 нет): ИИ
  её не распускал — её снимает игра. Банки E&F живут, потому что владеют уровнями «Банка» с создания
  (`zz_ef_cm_create_owned_bank`).
- Национализацию скриптом не проверить (эффекта нет).
- Область компании (`script_docs` 1.13): триггеры `company_owned_levels`, `company_employed_levels`,
  `company_prosperity`, `company_productivity`, `company_is_prosperous`, `company_has_monopoly`; цели — `executive`,
  `prosperity`, `weekly_prosperity_change`; эффекты — `add_company_monopoly`, `set_company_state_region`,
  `set_company_establishment_date`. Прибыли компании как значения нет.
- Ошибок по файлам пробы нет.

**Вырезано:** `common/company_types/ld_probe_cb_company.txt`, `common/scripted_effects/ld_probe_cb.txt`,
`events/ld_probe_cb_events.txt` (здесь), абзац пробы в `docs/код/central-bank.md`.
