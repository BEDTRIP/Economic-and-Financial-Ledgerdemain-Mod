# Арбитраж частных банков E&F (`privat_bank_*_currency`)

E&F: частные банки покупали валюту за металл при `rise_base_rate`, продавали за металл ЦБ при `down_base_rate` /
`revaluation_currency_target`, после 1873 «атаковали» серебро и биметаллизм. В форке обёртки `privat_bank_buy_currency` /
`privat_bank_sell_currency` были пустыми («В3: … off»), тела `buy_currency_privat_bank` / `sell_currency_privat_bank`
никто не вызывал. Переменные-флаги `rise_base_rate`, `down_base_rate`, `revaluation_currency_target`,
`global_monetary_reference_arbitrage`, `attack_on_currency` (одноимённые модификаторы — другое, они живые) нигде не читаются.
Интерфейса нет (список `sell_currency_privat_bank_variable_list_ordered` стоит в `datamodel` мёртвого окна
`gui/ef_dev_and_custom_windows/ef_custom_windows.gui:8767`, не тронуто — окно отладочное).

| что | откуда |
| --- | --- |
| `privat_bank_buy_currency`, `buy_currency_privat_bank`, `privat_bank_sell_currency`, `sell_currency_privat_bank` | `common/scripted_effects/01_economic_scripted_effects.txt`, 92125–92429 |
| `sell_private_bank_reserve_currency`, `private_bank_reserve_currency`, `private_bank_gold_lose`, `private_bank_silver_lose`, `private_bank_gold_gain`, `private_bank_silver_gain` (их звали только тела выше) | там же, 87982, 88336, 103334, 103529, 103724, 103919 |
| `sell_currency_privat_bank_variable_list` | `common/scripted_effects/08_list_effect.txt`, 2228–2565 |
| вызовы | `common/scripted_effects/00_on_action_main.txt` (файл в архиве — три куска) |

**Удалено из живых файлов** (`00_on_action_main.txt`, целыми `if`, вместе с `set_variable` флага):
- `central_bank_ef_on_monthly_pulse_country`: `if { has_modifier = rise_base_rate … set_variable = rise_base_rate  privat_bank_buy_currency = yes }`;
  `if { has_modifier = down_base_rate … privat_bank_sell_currency = yes }`; `if { has_modifier = revaluation_currency_target … privat_bank_sell_currency = yes }`;
  закомментированный `devaluation_currency_target` + `privat_bank_buy_currency`; три заголовка-комментария.
- `central_bank_ef_on_half_yearly_pulse_country`: `if { has_modifier = global_monetary_reference … set_variable = global_monetary_reference_arbitrage  privat_bank_buy_currency = yes }`.
- `central_bank_ef_on_yearly_pulse_country`: `if { game_date > 1873.1.1  or = { has_law = law_bimetallism_standard has_law = law_silver_standard } … set_variable = attack_on_currency  privat_bank_sell_currency = yes }` и пустой заголовок «Attack sur la currency».

Точные тексты — в `common/scripted_effects/00_on_action_main.txt` архива. **Вернуть:** вставить блоки на место (конец
соответствующих функций) и определения в исходные файлы.
