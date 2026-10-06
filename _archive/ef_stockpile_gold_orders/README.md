# Заказы запаса за золото и покупка запаса из казны (E&F)

**Что делало.** (1) В `buy_<g>_order` / `sell_<g>_order` (29 товаров) ветка «флаг `var:<buy|sell>_<g>_in_gold_1 = 1` → `<buy|sell>_<g>_order_in_gold = yes»; сами эффекты
`*_order_in_gold` нигде не определены, вызов ничего не делал. (2) 29 scripted_gui `buy_<g>_budget_panel` (`add_treasury` на сумму панели + прибавка запаса в `stockpiling_<g>_state_1`);
GUI вызывает только `*_budget_panel_visible` и `trade_<g>_budget_panel`.
**Кто вызывал.** (1) цепочка заказов запаса E&F (`buy_/sell_<g>_order` → `*_order_in_currency`, вызов из `RMSA_MMSA_order_trigger`); (2) никто. **Переменные.** Флаги `buy_/sell_<g>_in_gold_1` (инициализируются в
`common/history/global/00_ef_stockpile_global_variable.txt`, показываются GUI) — остались в живых файлах, сброс и показ работают как прежде.

**Что лежит здесь**
- `common/scripted_effects/01_stockpile_scripted_effects.txt` — 58 блоков `if = { limit = { var:… _in_gold_1 = 1 } … _order_in_gold = yes }` (в начале — диапазоны строк).
- `common/scripted_guis/00_stockpile_scripted_guis.txt` — строки 1410–2047: 29 `buy_<g>_budget_panel` с метками `#<товар>`.

**Удалено из живых файлов.** В каждом `buy_<g>_order` и `sell_<g>_order` первый блок `if` (остался только блок `_order_in_currency`); 29 определений scripted_gui подряд.
**Вернуть.** Блок `if` — первым в каждый `*_order`; scripted_gui — на место перед баннером «EFF/…» (после `*_budget_panel_visible`). Для работы потребуются эффекты `*_order_in_gold` (в E&F их нет).
