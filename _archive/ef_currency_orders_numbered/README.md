# `buy_sell_currency_order` (приказы валюты по уровням `buy_<cur>_N` / `sell_<cur>_N`)

**Что делало:** эффект `buy_sell_currency_order` (6938 строк, 950 блоков `if { limit = { has_modifier = has_central_bank var:<buy|sell>_<cur>_<1..5> = 1 } <buy|sell>_<cur>_<N> = yes }` по 95 валютам). Эффектов `buy_<cur>_<N>` / `sell_<cur>_<N>` в моде и ваниле нет
(есть только `buy_<cur>_currency` / `sell_<cur>_currency`), поэтому каждый вызов был «Unknown effect», эффект ничего не делал.
**Кто вызывал:** `central_bank_ef_on_half_yearly_pulse_country` (`00_on_action_main.txt`), в блоке `has_central_bank_SS_BS_GS_GES_NISO`.
**Переменные:** читал `var:buy_<cur>_N`, `var:sell_<cur>_N` (ставятся историей и `10_new_country_var.txt`; их читает и кастомная локализация); не писал.

## Вырезано (текст — по тем же путям)
- `common/scripted_effects/00_on_action_main.txt`: определение `buy_sell_currency_order` целиком (строки 5773-12710 до выреза);
- там же, в `central_bank_ef_on_half_yearly_pulse_country` (после `fluctuations_money_value_1_year = yes`, перед `leading_producer_of_oil = yes`): `buy_sell_currency_order = yes`.

**Вернуть:** определение — на место, вызов — по описанию; чтобы заработало — завести эффекты `buy_<cur>_<N>` / `sell_<cur>_<N>`.
