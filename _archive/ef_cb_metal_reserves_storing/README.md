# Месячная раздача и покупка металла ЦБ (E&F storing_*, zz_ef_cb_metal_purchase_step)

**Что делало.** E&F раз в месяц клало в `gold_state_1` / `silver_state_1` столичного штата ЦБ заявки рынка на продажу металла
× 100 × 4 (`storing_gold_1`, `storing_silver_1` — металл из ничего). Д2.7а: обёртка `stockpiling_central_bank_metal_reserves_state`
опустошена, их вызов выключен; месячная покупка по модификаторам здания ЦБ (`zz_ef_cb_metal_purchase_step`, пишет
`gold_state_1`/`silver_state_1` и `zz_ef_cb_stock_acc`) заменена недельной `zz_ef_metal_week_step` (`ld_metal_accounts.txt`).

**Кто вызывал.** `stockpiling_central_bank_metal_reserves_state = yes` — месячный блок `00_on_action_main.txt` (после проверки рынка);
`storing_*` — никто; `zz_ef_cb_metal_purchase_step` — никто.
**Переменные.** `gold_state_1`, `silver_state_1` (живые, их пишет `zz_ef_metal_week_step`); `zz_ef_cb_stock_acc`/`zz_ef_cb_stock_before`
пишет и читает живая недельная цепочка (`ld_metal_accounts.txt`, `ld_money_model.txt`). **Интерфейс:** нет.

**Что лежит здесь**
- `common/scripted_effects/ld_cb_stockpile_track.txt` — файл целиком (`zz_ef_cb_metal_purchase_step`).
- `common/scripted_effects/01_economic_scripted_effects.txt` — строки 41643–41755: `stockpiling_central_bank_metal_reserves_state` (пустое тело),
  `storing_gold_1`, `storing_silver_1`.
- `common/scripted_effects/00_on_action_main.txt` — строка 417.

**Удалено из живых файлов**
- `common/scripted_effects/00_on_action_main.txt`: в месячном блоке, между `}` и `stockpiling_currency = yes`, строка `stockpiling_central_bank_metal_reserves_state = yes`.
- `common/scripted_effects/01_economic_scripted_effects.txt`: три определения подряд перед `government_loan_month` (перед ними остаётся рамка из `#`).
- Элементов GUI и локализации нет. Одноимённые `stockpiling_central_bank_metal_reserves_state_transfert(_state)` (scripted_gui, кнопка в `gui/00_ef_deported_gui_1.gui`) — другое, живое.

**Вернуть.** Вставить блок 41643–41755 обратно перед `government_loan_month`, строку вызова — в месячный блок; для покупки — положить файл и вызвать
`zz_ef_cb_metal_purchase_step = yes` в месячном шаге (но недельная цепочка уже покупает металл — будет двойная покупка).
