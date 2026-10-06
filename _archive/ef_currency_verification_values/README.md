# Проверочные значения валют (E&F)

Всё в `common/script_values/01_economic_currency_scripted_value.txt` (вырезано по блокам, исходные строки — в заголовках блоков архивного файла).

| что | сколько | что делало |
| --- | --- | --- |
| `money_supply_verification_<cur>` | 95 блоков, ~98 тыс. строк | сверка денег в обороте по законам валют (по ~1050 строк на валюту) |
| `sell_<cur>_market_panel_verification` и `_current` | 190 блоков | сверка панели продажи валюты |
| `buy_<cur>_order`, `buy_<cur>_order_valid` | 190 блоков | чистый заказ / остаток слотов `var:buy_<cur>_1..5`, `var:sell_<cur>_1..5` |
| `sell_limit_currency_var_current`, `currency_total_stokpile`, `currency_total_stokpile_ordered`, `money_value_target_in_gold_by_country`, `metal_state_in_gold` | по 1 | отладочные суммы |
| `<cur>_spe_to_add_to_specific_currency` | 95 блоков | читали только `money_supply_verification_<cur>` |
| `buy_<cur>_market_panel`, `sell_<cur>_market_panel` | 190 блоков | читали только проверочные значения и `*_spe_to_add_*`; GUI биржи валют читает `buy_sell_currency_in_metal_market_panel` и `*_in_gold_market_panel` (они остались) |

**Кто вызывал:** никто (в `common/ events/ gui/ localization/` имён нет, в том числе в `customizable_localization`; значения верхнего уровня читали друг друга только внутри вырезанного). **Переменные:** читали `var:buy_<cur>_N`, `var:sell_<cur>_N`, `player.var:<cur>_spe_to_subtract_to_money_suply_N` (их пишут живые эффекты, не вырезались). **Интерфейс:** нет.
**Удалено из живых файлов:** только эти определения (всего 765 блоков, 252 626 строк); вызовов и GUI не было.
**Вернуть:** вставить блоки обратно в `01_economic_currency_scripted_value.txt` (порядок в файле значения не имеет).
