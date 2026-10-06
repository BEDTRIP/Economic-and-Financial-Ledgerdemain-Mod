# Контроллер ставки E&F `base_rate_change`

| что | откуда |
| --- | --- |
| пустое определение `base_rate_change = { # EF.30: the rate is set by zz_ef_cb_rate_step. }` | `common/scripted_effects/01_economic_scripted_effects.txt`, строки 99047-99049 |
| вызов (ИИ, полугодовой пульс) | `common/scripted_effects/00_on_action_main.txt`, строки 603-608, `central_bank_ef_on_half_yearly_pulse_country`: |

```
	if = {
		limit = {
			is_ai = yes
		}
		base_rate_change = yes
	}
```

Тело E&F (полугодовой ИИ-контроллер ставки) было заменено пустым ещё раньше: ставку ведёт `zz_ef_cb_rate_step` (`ld_central_bank_rate.txt`). Переменных и интерфейса нет.
**Удалено из живых файлов:** определение и этот `if` (на месте — между блоком `global_country_ranking = 1` и `crisis_general_reset_count = yes`). Также убраны два комментария и строка «MAINTENANCE» в шапке `ld_central_bank_rate.txt`.
**Вернуть:** вставить определение и вызов обратно; вернуть тело E&F — из оригинала 4.1.7.
