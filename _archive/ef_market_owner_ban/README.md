# Запрет стандартов на чужом рынке (`is_not_market_owner`)

**Что делал.** Триггер E&F `is_not_market_owner` (страна на существующем чужом рынке) стоял в `can_enact` законов
`law_silver_standard`, `law_bimetallism_standard`, `law_gold_standard` (`common/laws/01_ef_monetary_system.txt`) и в
`is_valid` трёх кнопок смены стандарта (`common/scripted_guis/00_economic_scripted_guis.txt`). Движок на загрузке
срезал стандарт истории у стран на чужом рынке (Бавария, Саксония, Вюртемберг, Финляндия, Ганновер: «not permitted to
retain law»), Бавария и Саксония весь прогон были без денежной системы при ЦБ с металлом. Решение — Д.R8а.3 / R8а.5:
страна на чужом рынке — со своей денежной системой.

**Вырезано:** определение триггера — `common/scripted_triggers/00_ef_custom_trigger.txt` (здесь).

**Удалено из живых файлов:** строка `is_not_market_owner = yes` внутри `NOT = { … }` — в `can_enact` трёх законов
стандартов и в `is_valid` трёх scripted GUI (`00_economic_scripted_guis.txt`: кнопки перехода на фиат и металл), строка
закомментированного `can_enact` закона `law_no_monetary_system`. Вместе с этим `subject_currency` (внешневалютный
стандарт ЦБ на чужом рынке) — только у подданных (`ef_on_monthly_pulse_recurence`, `zz_ef_start_setup_year`), снятие —
и у неподданного (`remove_suject_currency`).

**Вернуть:** определение — обратно; строки — в `NOT = { … }` тех же блоков.
