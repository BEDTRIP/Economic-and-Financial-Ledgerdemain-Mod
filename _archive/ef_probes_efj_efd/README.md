# Зонды EFJ и EFD (zz_ef_probe_newyear_cash, zz_ef_probe_pop_income)

**Что делали.** Диагностика (3.10, этап 0): `zz_ef_probe_newyear_cash` — в декабре и в первую январскую неделю логировал `EFJ` по каждому зданию с наличными > 10 000 (откуда
скачок наличных 1 января); `zz_ef_probe_pop_income` — до 1838 для игрока и Франции логировал `EFD` по каждому попу (доход от двигателя). Включались значениями
`zz_ef_probe_on` / `zz_ef_probe_pop_on`, оба 0. Журнал на ПК: `parse_eflog.py` знает ключи EFJ/EFD — строк нет.
**Кто вызывал.** Недельный шаг (`zz_ef_money_model_step`, после `zz_ef_bkcash`) и приёмник моста (`zz_ef_money_hook_receive`, после `zz_ef_money_log_rest`). **Переменные.** `zz_ef_probe_jan` (флаг на 60 дней). **Интерфейс.** Нет.

**Что лежит здесь**
- `common/scripted_effects/ld_money_model.txt` — два вызова с комментариями, оба эффекта с комментариями.
- `common/script_values/ld_money_model_values.txt` — `zz_ef_probe_on`, `zz_ef_probe_pop_on`, `zz_ef_probe_cash_now`, `zz_ef_probe_level` (последние два читал только EFJ).

**Удалено из живых файлов.** `ld_money_model.txt`: `zz_ef_probe_newyear_cash = yes` (+ комментарий «В1.3 probe …») в недельном шаге; `zz_ef_probe_pop_income = yes` (+ «UI.7б probe …») в приёмнике моста.
**Вернуть.** Вызовы — на те же места; эффекты — в конец `ld_money_model.txt`; значения — в `ld_money_model_values.txt`; включить флаги = 1.
