# Историческое создание финцентра `initialize_historic_macro_facilities_fc` и запасы финцентра США

**Что делали:** эффект `initialize_historic_macro_facilities_fc` (`09_introduction_building_lvl.txt`) — технологии
`financial_center`, `stock_exchange`, здание финцентра в `$FIN_CENT_SITE$`, модификатор `has_financial_center`,
переменная страны `financial_center_location`. **Никто не вызывал** (финцентры в истории ставит
`history/buildings/00_ef_building.txt` напрямую). Блок США в `99_ef_history_global_variable.txt` клал стартовые
запасы финпродуктов (`stockpiling_*_var_state_1`) в `var:financial_center_location` — переменная не ставилась
(«Variable 'financial_center_location' is used but is never set», error.log), блок не срабатывал. Те же запасы всем
странам с финцентром ставит общий блок выше (по `var:central_bank_location`).

**Интерфейс:** нет. **Удалено из живых файлов:** определение эффекта; блок `if = { limit = { c:USA ?= this } … }`
(здесь, по тем же путям). **Вернуть:** вставить обратно; эффект заработает только с вызовом в истории.
