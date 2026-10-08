# Миграции старых сейвов хотфикса

**Что делали:** переносили переменные из сейвов до 1.10 (хотфикс) в новые имена или удаляли старые. В новой игре
форка этих переменных нет: движок писал «Variable 'zz_ef_m3_q1..13' / 'zz_ef_cap_ref0' / 'zz_ef_cap_index0' is used
but is never set» (error.log каждого запуска), сами блоки не срабатывали. Сейвы хотфикса форк не поддерживает.

| блок | что делал |
| --- | --- |
| `ld_money_model.txt`, `zz_ef_money_model_step` | один раз: годовое кольцо денег в обращении `zz_ef_circ_q1..13` ← старое кольцо M3 `zz_ef_m3_q1..13` (чтобы инфляция не начиналась с нуля) |
| `ld_capitalization_average.txt`, годовая отметка индекса | удаление старых баз индекса `zz_ef_cap_ref0`, `zz_ef_cap_index0` (24–25.09) |
| `ld_money_model.txt`, начало `zz_ef_money_model_step` | банкноты `zz_ef_notes` = S − D у сейва без счёта банкнот (R1б) |
| `ld_money_model.txt`, `zz_ef_money_model_step` | паритет: `zz_ef_parity_version < 6` → `money_value_target_1 = money_value_0` у ЦБ на металле; номер версии старта (9) |
| `ld_pb_overbuild_counter.txt`, начало `zz_pb_ef_overbuild_counter` | один раз (`zz_pb_ef_overbuild_v2`): снять с секторов стройки `overbuilt_economy_modifier` и `zz_pb_ef_overbuilt_brake` (v0/v1 перестройки) |
| `ld_pb_overbuild_modifiers.txt` | модификатор-наследство `zz_pb_ef_overbuilt_brake` (определён только ради снятия) |
| `ld_start_triggers.txt`, `zz_ef_game_started` | пропуск по дате (`game_date >= 1836.3.1`) для сейвов без флага `zz_ef_start_setup_done` |

**Кто вызывал:** недельный шаг модели денег и годовая отметка индекса цен (блоки внутри них). **Интерфейс:** нет.

**Удалено из живых файлов (R3б.3, В1 — мод только для новой игры):** номер версии старта `zz_ef_parity_version` (9)
заменён флагом `zz_ef_model_started` (ставит старт в `zz_ef_money_model_step`; читают `ld_currency_zone.txt`,
`ld_nr_deposits.txt`, `ld_monetary_policy.txt` — `has_variable`); из `zz_ef_game_started` — `OR` с датой (остался флаг);
локализация `zz_pb_ef_overbuilt_brake`, `zz_pb_ef_overbuilt_brake_desc` (11 языков, `ld_pb_overbuild_l_*.yml`:
«Construction Overcapacity (old)» / «Избыточные строительные мощности (старое)»); строка `zz_pb_ef_overbuild_v2` в
таблице `docs/construction.md`; комментарий «old m0/m1/m2 rings … left to rot in old saves» в `ld_money_model.txt`.
Ранее: только сами блоки (здесь, по тем же путям); комментарий о `zz_ef_cap_ref0` /
`zz_ef_cap_index0` в шапке `ld_capitalization_average.txt`; строка реестра `docs/mechanisms.md` «Очистка старых баз
индекса»; строка таблицы `docs/exchange-companies.md`.

**Вернуть:** вставить блоки на прежние места (перед `zz_ef_ring_w_push = { M = agg0 }` и в конец годовой отметки; остальные — места указаны в файлах архива).
