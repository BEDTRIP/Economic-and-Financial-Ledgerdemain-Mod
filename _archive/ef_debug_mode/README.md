# Отладочный режим E&F (`EF_debug_mode`)

**Что делал.** Виджет `01_ef_debug_widget` зеркалил `[InDebugMode]` (консольный режим отладки игры) в глобальную переменную `EF_debug_mode`
через sgui `EF_sg_set_debug_flag` / `EF_sg_unset_debug_flag`. Флаг читали только отладочные решения (`has_global_variable = EF_debug_mode`):
`Open_Test_Decision`/`Close_Test_Decison` (ставят/снимают `openTestDecision_variable`), `Test_event_1..5` (перебор штатов, `remove_suject_currency`,
`central_bank_production_methods_4`, событие `test_2.4`, обнуление глобальных `silver_to_gold_*`), `law_encouranging_childbirth_Decision_0/1/5/10`
(`need_workforce_modifier`). Регистрация виджета указывала на несуществующий `gui/01_ef_debug_widget.gui` (файл назывался `00_…`), поэтому флаг не ставился,
решения не показывались; `EF_debug_mode_visibility` (`is_shown = { always = no }`) был нужен только закомментированному условию кнопки «1».
**Переменные:** `EF_debug_mode` (глобальная), `openTestDecision_variable` (страна). Локализации у решений нет.

**Удалено из живых файлов**
- файлы целиком: `gui/00_ef_debug_widget.gui`, `gui/scripted_widgets/EF_scripted_widgets.txt` (одна строка `gui/01_ef_debug_widget.gui = 01_ef_debug_widget`),
  `common/decisions/00_ef_debug_decisions.txt` (277 строк, 11 решений).
- `common/scripted_guis/09_ef_other.txt` — три sgui: `EF_sg_set_debug_flag`, `EF_sg_unset_debug_flag`, `EF_debug_mode_visibility`.

**Вернуть:** положить файлы и sgui по исходным путям; исправить регистрацию на `gui/00_ef_debug_widget.gui = 01_ef_debug_widget`.
