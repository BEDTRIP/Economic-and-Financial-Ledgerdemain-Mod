# ИИ-форекс E&F (`ai_buy_sell_currency` → `buy_<cur>_currency` / `sell_<cur>_currency`)

**Что делало:** раз в год ИИ-владелец рынка с ЦБ на серебре / биметалле / золоте (`has_central_bank_SS_BS_GS_NISO`)
по каждой из 95 валют: если валюта не слабая — `buy_<cur>_currency` (покупка недооценённой валюты у ЦБ-эмитента из
`<cur>_currency_law_list_ordered_1`, условие `buy_currency_1`), если запас валюты > 1 млн и `purchase_cycle = 0` —
`sell_<cur>_currency` (продажа переоценённой, `sell_currency_1`). Сделка — `zz_ef_fx_deal_size` (2 % M2 эмитента; 0 у ИИ
с покрытием ниже нормы) по паритету `money_value_target_real`: металл ЦБ-покупателя (`gold_state_1` / `silver_state_1`
столицы ЦБ) → металл ЦБ-эмитента, запас `stockpiling_<cur>_state_1` эмитента → покупателю; продажа — наоборот. Сообщения
игроку-эмитенту `your_currency_are_buy_message` / `your_currency_are_sell_message`.

**Почему вынесено:** пишет металл ЦБ и запасы валют мимо учёта (в сверке металла — «прочее», `EFQ`); запас чужой валюты
по правилу модели — вклад в банках эмитента, появляется только проводкой (регистр `zz_ef_nr_dep`). Решение пользователя
8.10 (Д.R2.2): ИИ-форекс — в архив; форекс ЦБ сделками через проводку — этап R8. Кнопки игрока
`<cur>_buy_in_gold` / `<cur>_sell_in_gold` остаются (через проводку — R2, п. 1–2).

**Кто вызывал:** `central_bank_ef_on_yearly_pulse_country` (`common/scripted_effects/00_on_action_main.txt`), блок
`if = { limit = { is_ai = yes market_owner_is_root = yes has_central_bank_SS_BS_GS_NISO = yes } … }`.

**Переменные:** писало `purchase_cycle` (страна), `<cur>_quantity_var`, `stockpiling_undervalued_quantity_var`,
`stockpiling_undervalued_currency_state_1_buyer_in_metal` (страна-покупатель; их читает локализация сообщений), `gold_state_1`,
`silver_state_1`, `stockpiling_<cur>_state_1` (штаты ЦБ). Читало списки `<cur>_currency_law_list_ordered_1` (их строит живой
`currency_law_list`, он же ставит модификатор `<cur>_leading_currency_type` — остался).

## Вырезано (текст — по тем же путям)
- `common/scripted_effects/00_on_action_main.txt`: определение `ai_buy_sell_currency` целиком (строки 2118–4306 до
  выреза); в `central_bank_ef_on_yearly_pulse_country`, в блоке `is_ai = yes market_owner_is_root = yes
  has_central_bank_SS_BS_GS_NISO = yes` — строка `ai_buy_sell_currency = yes` (перед `monetary_systeme_transition = yes`,
  он остался).
- `common/scripted_effects/01_economic_scripted_effects.txt`: 190 определений `buy_<cur>_currency` и `sell_<cur>_currency`
  (95 валют, строки 25209–73217 до выреза; комментарии-разделители `#<cur>` между ними остались).
  `sell_<cur>_currency_crisis` остались (их зовёт живой `all_currency_resold`).
- `common/scripted_triggers/00_ef_custom_trigger.txt`: `buy_currency_1`, `sell_currency_1`.
- `common/script_values/ld_money_model_values.txt`: `zz_ef_fx_deal_size` (с комментарием).

**Осталось в живых файлах без отправителя:** сообщения `your_currency_are_buy_message` / `your_currency_are_sell_message`
(`common/messages/00_ef_messages.txt`, sell зовут и кризисные продажи) и их локализация; установка `purchase_cycle = 0`
(`history/global/00_ef_economic_global_variable.txt`, `10_new_country_var.txt`).

**Генератор:** `tools/regen_ef_reserve_trade.py` (`vic3_mods`) брал список валют из `buy_<cur>_currency` — теперь из
`sell_<cur>_currency_crisis` (тот же список из 95).

**Вернуть:** определения — на место, вызов — по описанию, значение и триггеры — на место. По схеме — не возвращать, а
сделать форекс ЦБ проводкой (R8).
