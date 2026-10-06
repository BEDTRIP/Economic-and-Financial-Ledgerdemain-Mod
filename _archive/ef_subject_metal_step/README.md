# Разовый пересчёт металла субъектов (zz_ef_subject_metal_step)

**Что делало.** M.8: один раз (на 12-й неделе, вместе с перемасштабом ЦБ) пересчитывало металл подданного / страны без ЦБ в 40% её денежной
массы по паритету и передавало подданного металл ЦБ сюзерена. Д2.13 (6.10): больше не вызывается — металл субъекта только то, что он купил.
**Кто вызывал.** Никто. **Переменные.** `zz_ef_subject_metal_done`, `zz_ef_metal_target_gold`, `zz_ef_metal_scale` (только внутри); лог `EFM|…|subject_metal|…`.
**Интерфейс.** Нет.

**Что лежит здесь**
- `common/scripted_effects/ld_subject_metal.txt` — строки 18–80: `zz_ef_subject_metal_step` (с комментарием «no longer called»).
  В живом файле остался `zz_ef_cb_state_owner_step` (В2.5), шапка сокращена до его описания.
- `common/script_values/ld_reference_currency_values.txt` — строки 53–80: `zz_ef_metal_in_gold`, `zz_ef_metal_target_in_gold` (читало только оно).

**Удалено из живых файлов.** Определение эффекта и два значения; вызовов и GUI не было. Из шапки `ld_subject_metal.txt` убран абзац «M.8».
**Вернуть.** Вставить блоки на места (значения — после `zz_ef_currency_trade_m`) и вызвать `zz_ef_subject_metal_step = yes` в недельном шаге.
