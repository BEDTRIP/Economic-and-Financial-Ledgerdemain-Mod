# Выдача местной валюты малым странам (остатки)

Файлы целиком, по исходным путям:

| файл | что |
| --- | --- |
| `common/script_values/ld_local_currency_values.txt` | `zz_ef_local_currency_rate`, `zz_ef_lc_curve_a..e`, `zz_ef_local_currency_wealth_curve`, `_state_count`, `_demand`, `_per_state` — размер выдачи `liquidity_currency` на штат по населению и уровню жизни |
| `common/scripted_triggers/ld_local_currency_triggers.txt` | `zz_ef_local_currency_needs_throttle` (`has_modifier = no_money_production`) |
| `common/on_actions/ld_local_currency_on_actions.txt` | `zz_ef_local_currency_monthly` в `on_monthly_pulse_country`: только `remove_modifier = zz_ef_local_currency_fix` со страны и всех штатов (очистка старых сейвов; выдача убрана ранее) |
| `common/static_modifiers/ld_local_currency_fix.txt` | модификатор `zz_ef_local_currency_fix` (`state_sell_orders_liquidity_currency_add = 1`) |

**Кто вызывал:** on_action `zz_ef_local_currency_monthly` каждый месяц; значения и триггер никто не читал (модификатор не ставился нигде). **Переменные:** нет. **Интерфейс:** нет.
**Удалено из живых файлов:** четыре файла целиком (вызов — сам on_action в `on_monthly_pulse_country`, `on_actions = { zz_ef_local_currency_monthly }`). Объявление типа `state_sell_orders_liquidity_currency_add` (`common/modifier_type_definitions/ld_liquidity_currency_sell_orders.txt`) и его локализация остались: объявление теперь без пользователей.
**Вернуть:** положить файлы по исходным путям; для нового выпуска модификатор надо снова ставить `add_modifier` с множителем `zz_ef_local_currency_per_state`. Старый сейв с модификатором после выноса останется с неизвестным модификатором (в новой игре не бывает).
