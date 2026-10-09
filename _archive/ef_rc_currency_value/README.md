# Стоимость валюты по закону для клиринга (`zz_ef_rc_currency_value`)

**Что делало.** Значение `zz_ef_rc_currency_value` (`common/script_values/ld_reserve_trade_values.txt`, генератор
`regen_ef_reserve_trade`) — стоимость E&F валюты закона страны (`money_value_<cur>`, цепочка по 95 законам). Клиринг
делил на него долг в золоте, переводя его в «единицы своей валюты», а держатели оценивали эти единицы по курсу
эмитента (~1): у Саксонии (стоимость E&F 11,9) палата получала ~8 % долга. Его же читал триггер «есть валюта».

**Сейчас (R8а.2, Д.R8а.4):** золото на единицу своих денег — `zz_ef_clr_gpm_own` = `zz_ef_value_to_parity` (металл — 1),
перевод в единицы — по нему; «есть своя валюта» (`zz_ef_has_currency_value`) — есть денежный стандарт (Д.R8а.2).

**Вырезано:** определение — здесь (`common/script_values/ld_reserve_trade_values.txt`).

**Удалено из живых файлов:** `common/script_values/ld_clearing_values.txt`, `zz_ef_clr_gpm_own`: `value =
zz_ef_rc_currency_value` (+ 1 у металлических); `common/scripted_effects/ld_clearing.txt`, `zz_ef_clr_pay`: `divide =
zz_ef_rc_currency_value`; `common/scripted_triggers/ld_reference_currency_triggers.txt`, `zz_ef_has_currency_value`:
`zz_ef_rc_currency_value > 0.0002`. Генераторы `regen_ef_clearing`, `regen_ef_reserve_trade` — в `vic3_mods`.

**Вернуть:** определение и строки — обратно (генераторы — по git, коммит R8а.2).
