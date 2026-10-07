# Сироты переносов R2 (8.10)

**Что это:** определения, которые читали только вынесенные этой ночью механизмы (`_archive/ef_ai_forex/`,
`ef_stockpiling_currency/`, `ef_currency_reform/`, `ef_bimetallic_arbitrage/`, `ef_government_loan_month/`) и после
переноса остались без ссылок (`ld_index.py`: ссылок 0, до ночи — были). Ничего не делали.

## Вырезано (текст — по тем же путям)
- `common/scripted_triggers/00_ef_custom_trigger.txt`: 95 `law_<cur>_monetary_system_SS_BS_trigger` (читал ИИ-форекс
  `buy/sell_<cur>_currency`), `has_central_bank_FS_NISO` (кнопка `currency_introduction`).
- `common/script_values/01_economic_currency_scripted_value.txt`: 95 `<cur>_c_market_goods_delta`, 95
  `<cur>_c_market_goods_buy_orders`, 95 `<cur>_c_market_goods_sell_orders` (читал `stockpiling_currency_type_1`; все читали
  товар `liquidity_currency` рынка).
- `common/script_values/00_economic_scripted_value.txt`: `money_supply_to_add_per_month`, `money_supply_to_subtract_per_month`
  (`stockpiling_currency_type_1`), `money_value_prevision_new_currency(_in_gold)` (реформа), `money_value_target_real_below_25`,
  `_above_25` (триггеры ИИ-форекса `buy/sell_currency_1`), `silver_gained`, `gold_lost` (арбитраж).

**Осталось без отправителя (не вынесено):** сообщения `your_currency_are_buy/sell_message` и их локализация;
`monetary_system_icon` (своя локализация E&F) — на случай, если их читает текст.

**Вернуть:** вместе с механизмом, который их читал.
