# Излишек казны сверх предела резервов → пул (`ld_tr_surplus_pool`)

Вынуто 8.10.2026 (закрытие R2, решение пользователя). Решение Д4.5 / EF.38 (4.10): казна сверх предела резервов движка
(`gold_reserves_limit`; сверх него движок режет доход, излишек сгорает) каждую неделю уходила в инвестиционный пул как
вклад государства в банки (`zz_ef_bank_gov_dep`). Пул движок тратит только на частную стройку — частники строили на
деньгах казны. В игре (r1008_093105): у Цин вкладов населения ~0, со второй недели в пул ушло 7,9 млн казны, стройка на них
шла мимо учёта — −10,2 млн «прочего» за 1836 год, медиана «прочего» мира −201 тыс. / нед. Пользователь: нет денег у
частников и в банках — нет и частной стройки; государство добавляет в пул само (кнопка E&F у ключевой ставки).

## Что делало
- в `zz_ef_money_model_step` после `zz_ef_consol_step`, с второго шага страны (`has_variable = zz_ef_pop_savings`):
  `zz_ef_f_tr_pool` = `gold_reserves` − `gold_reserves_limit`, проводка `zz_ef_post_eng = { FROM = treasury TO = pool
  CLAIM = zz_ef_bank_gov_dep }` (казна → пул, требование казны к банкам).

## Удалено из живых файлов
| файл | что |
| --- | --- |
| `common/scripted_effects/ld_money_model.txt` | в `zz_ef_money_model_step` — комментарий Д4.5 и блок `if = { limit = { has_variable = zz_ef_pop_savings gold_reserves > gold_reserves_limit } … }` (текст — здесь); `set_variable = { name = zz_ef_f_tr_pool value = 0 }` оставлен — поток всегда 0 |

Остались и читают 0: значение `zz_ef_v_f_tr_pool` (`ld_money_model_values.txt`), строки `f_tr_pool` логов `EFF`
(`ld_money_log_rest.txt`), строка карточки `zz_ef_ms_x_v_f_tr_pool` (локализация, генератор
`../vic3_mods/tools/regen_ef_money_supply_loc.py`); счёт `zz_ef_bank_gov_dep` (книга банков, доля заёмного бизнес-кредита) —
под проводку кнопки E&F в R4.

## Как вернуть
Вставить блок из `common/scripted_effects/ld_money_model.txt` здесь на прежнее место (после `zz_ef_consol_step`).
