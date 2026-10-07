# Биметаллический арбитраж частных банков E&F (`private_bank_arbitrage_gold_drain` / `_silver_drain`)

**Что делало:** раз в год (`central_bank_ef_on_yearly_pulse_country`) у страны на биметаллизме до 1873: при перекосе
рыночного соотношения золота и серебра к законному (`misalignment_rate_gold_drain` / `_silver_drain` ≥ 0,05) случайный
частный банк из `global_arbitrage_bank_variable_list_ordered` менял у ЦБ дешёвый металл на дорогой: ЦБ терял
`gold_lost` золота и получал `silver_gained` серебра (или наоборот), банк — встречно (глобалки
`company_<Банк>_gold/silver_stockpile_fix`, `gold_state_1_fix` / `silver_state_1_fix` страны); событие игроку
`00_ef_economic_event.95` / `.96`.

**Почему вынесено:** не срабатывало — `misalignment_rate_gold_drain` и `misalignment_rate_silver_drain`
(`common/script_values/00_economic_scripted_value.txt`) равны 0, условие ≥ 0,05 недостижимо (статус «выключен», реестр
считал его живым). Решение пользователя 8.10 (Д.R2.3) — арбитраж проводкой (металл ЦБ ↔ металл банков страны
банка-арбитражёра, счёт `zz_ef_bankm_gold/silver`, глобалки E&F не писать); пока перекос не считается, проводка была бы
мёртвым кодом. Принято ночью 8.10, проверить: вернуть вместе с перекосом (R3, стандарты), сразу проводкой.

**Кто вызывал:** `central_bank_ef_on_yearly_pulse_country` (`common/scripted_effects/00_on_action_main.txt`), после
`economic_crisis_count_reset_condition = yes`.

## Вырезано (текст — по тем же путям)
- `common/scripted_effects/00_on_action_main.txt`: блок `#Arbitrage: bimetalism arbi pre 1873` (рамка из `#` и `if`
  целиком) в `central_bank_ef_on_yearly_pulse_country`.
- `common/scripted_effects/01_economic_scripted_effects.txt`: `private_bank_arbitrage_gold_drain`,
  `private_bank_arbitrage_silver_drain`.

**Осталось без вызова:** события `00_ef_economic_event.95` / `.96` и их сообщения; значения `misalignment_rate_*`,
`gold_lost`, `silver_gained`, `silver_lost`, `gold_gained` (их читают локализация и подсказки); список
`global_arbitrage_bank_variable_list_ordered` (строится в `08_list_effect.txt`).

**Вернуть:** блок и эффекты — на место; по схеме — с перекосом и проводкой (выше).
