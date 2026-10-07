# Денежная реформа E&F (`reset_law_event_currency`, кнопка `currency_introduction`)

**Что делало:** при сверхслабой валюте (`extreme_weak_currency`, курс в золоте < 0,01) — новая валюта:
- ИИ: `extreme_weak_currency_solution` (годовой пульс ЦБ, `00_on_action_main.txt`) считает годы слабости; на третий (без
  банкротства ЦБ и валютного кризиса) — `reset_balance`, `reset_debt_currency_reserve_and_export_value`,
  `reset_law_event_currency`, `law_no_monetary_system_with_tech_currency_standards`, `introduction_new_currency`, флаг
  `new_currency_recreat`, `new_currency_count` + 1, `money_value_global_var`, снова `reset_balance`;
- игрок: секция «currency_introduction» экономического окна (`gui/scripted_widgets/00_ef_custom_widgets.gui`,
  видна при `extreme_weak_currency_visible`) с кнопкой `currency_introduction` (scripted_gui): все чужие ЦБ продают
  валюту (`all_currency_resold`), `reset_law_event_currency`, `reset_debt_currency_reserve_and_export_value`, закон
  `law_no_market_liquidity`, `introduction_new_currency`, серебряный стандарт.

`reset_law_event_currency` по закону валюты (95 веток): `circulating_<cur>_c_var_1` = 0, `government_loan` = 0,
`add_investment_pool = { subtract = private_bank_funds }`, запас `stockpiling_<cur>_state_1` столицы = 0 — пул, долг
казны ЦБ и запасы мимо учёта. `reset_balance` — пересчёт списков и балансов валют; `reset_debt_currency_reserve_and_export_value`
— обнуление долгов в валюте, резервов и экспорта (~10 тыс. строк).

**Почему вынесено:** решение пользователя 8.10 (Д.R2.6) — выключить до R3. Вернуть в R3 проводками: пересчёт вкладов по
курсу реформы, списание долга казны ЦБ в капитал ЦБ.

## Вырезано (текст — по тем же путям)
- `common/scripted_effects/01_economic_scripted_effects.txt`: определение `reset_law_event_currency` (строки 10694–12884
  до выреза); в `extreme_weak_currency_solution` — комментарий `#reset currency` и блок `if` целиком (после
  `change_variable extreme_weak_currency_solution_count`; счётчик остался); определения `reset_balance`,
  `reset_debt_currency_reserve_and_export_value` (после выреза вызовов — без ссылок).
- `common/scripted_guis/00_economic_scripted_guis.txt`: `currency_introduction`, `extreme_weak_currency_visible`.
- `gui/scripted_widgets/00_ef_custom_widgets.gui`: комментарий `#currency_introduction - temporaire new currency`,
  `section_header_button` (заголовок секции, `onclick` переключает `currency_introduction` и зовёт
  `world_currency_list_gerenation_ordered`) и `flowcontainer` секции (счётчик лет слабости, закон стандарта, курс, новая
  валюта, кнопка `currency_introduction`) — между `divider_decorative` предыдущей секции и концом окна.
- `common/script_values/00_economic_scripted_value.txt`: `extreme_weak_currency_solution_count_sc` (читала только кнопка).

**Осталось:** `extreme_weak_currency_solution[_player]` (счётчики), `introduction_new_currency` (введение валюты — его
зовут история и смена закона), `all_currency_resold` (зовут другие места), локализация секции.

**Вернуть:** определения и блоки — на место по описанию; по схеме — проводками (R3).
