# Стройка (PSC + E&F private construction + лимит секторов)
**Смысл.** Стройка — PSC внутри форка: частный сектор и казна платят за строительные товары, частная стройка — кредит
банков из пула, рычаг — ставка. **Понятия:** [[Строительство|Стройка]], [[Инвестиционный пул|Пул]], [[Ставка ЦБ]],
[[Рычаги на движок]]. **Решения:** Д.R3.7, Д.R2.13, Д.Г.6, Д.Г.7, Д.R9.5 (аудит PSC; правила — Д.R8в.27), Д.R9.11
(`решения.md`); отменённые Д.R8в.24, Д.R8в.26 — `история/2026-10-14 этап R9.md`, «Перенесено».

Частный сектор строит через здание `building_construction_sector` (PSC), казна платит остаток через регулятор очков
`building_construction_regulator`; делёж долей (частные/государственные очки стройки) пересчитывается раз в неделю.
Кол-во секторов ограничено уровнями городских центров и ключевой ставкой; сверх лимита копится «перестройка»
(`speculative_share_2`, штраф к пропускной способности), ИИ сносит лишнее. Домохозяйства и ЖКХ покупают стройтовары.
Настоящее здание стройки — `building_construction_sector` (PSC); E&F-овского `building_ef_private_construction` в форке
нет, его имя остаётся только в названиях скрипт-значений `building_ef_private_construction_lvl*`.

## Файлы
**PSC (ядро)**
- `common/buildings/zz_PSC_construction.txt` — `building_construction_sector` (REPLACE: ai_value, `can_build_private` по
  лимиту, PMG `pmg_base_building_construction_sector` + `pmg_market_liquidity`), `building_construction_regulator`
  (невидимое государственное здание, 1 на штат).
- `common/building_groups/zz_PSC_building_groups.txt` — `bg_construction` (частная, parent `bg_private_infrastructure`),
  `bg_construction_regulator`.
- `common/production_methods/zz_PSC_construction.txt` — PM сектора
  `pm_wooden/iron_frame/steel_frame/arc_welded_buildings` (вход: материалы; выход: `*_construction`; выпуск
  «акций» E&F `manufacture_stock` снят — Д.R4б.8; выход стройтоваров больше на его выручку по базовым ценам: 24 / 64 /
  136 / 204 — Д.R4б.14), PM регулятора `pm_{wood,iron,steel,arc_welded}_point_conversion` (`country_construction_add`;
  вход — по 10 каждого из четырёх стройтоваров на очко, доли режут модификаторы `zz_ef_reg_in_<товар>`, Д.R9.5; метод
  регулятора называет товар сектора штата — по его базовой цене очки, Д.R9.11).
- `common/production_method_groups/PSC_construction.txt` — `pmg_construction_regulator`.
- `common/goods/PSC_goods.txt` — `wood_/iron_/steel_/arc_welded_construction`.
- `common/defines/PSC_defines.txt` — `CONSTRUCTION_CAMP_BUILDING = building_construction_regulator`.
- `common/history/global/PSC_global.txt` (запуск цикла), `common/history/buildings/PSC_buildings.txt` (регуляторы по
  штатам).
- `common/modifier_type_definitions/PSC_building_modifier_types.txt`, `common/static_modifiers/PSC_modifiers.txt` —
  `construction_throughput_mult`, `country_private_construction_allocation_add`,
  `state_construction_efficiency_increase`.
- `common/alert_types/PSC_alert_types.txt` — `insufficient_construction_for_investment`.
- `common/on_actions/PSC_on_actions.txt` — недельный цикл + реакции на смену PM/постройку/технологию.
- `common/scripted_effects/PSC_scripted_effects.txt` — `set_construction_point_demand` (главный),
  `set_construction_regulator_level`, `set_state_construction_efficiency`, `set_government_construction_spending`,
  `set_new_point_conversion_method`, `set_new_regulator_point_conversion_method`,
  `set_point_conversion_method_from_tech`, `check_construction_spending_level`.
- `common/scripted_effects/PSC_delay_event_switch.txt`, `PSC_my_trigger_event.txt`,
  `PSC_production_method_building_switch.txt` — разнос запуска по дням недели; создание регулятора с нужным PM.
- `common/script_values/PSC_construction_values.txt` — расчёт трат/долей/эффективности (корень
  `calculate_total_construction_spending`, `privatisation_spending_percent`, `state_construction_spending_allocation`,
  `state_construction_allocation`, `construction_ordering`, `ai_construction_demand`, `goods_efficiency_per_level` —
  эффективность стройки штата на уровень сектора, около ×10 ванильной по методу: 0,02 / 0,035 / 0,07 / 0,1;
  sqrt-рекурсия). `PSC_set_values.txt` — константы;
  `PSC_event_values.txt` — календарь недели.
- `common/scripted_guis/PSC_construction_sguis.txt` — кнопки уровня трат (`psc_button_*_sgui`),
  `psc_save_real_construction_cost`, `psc_test_show`.
- `gui/PSC_construction_panel.gui` (панель стройки), `gui/shared/PSC_construction_spending_options.gui` (ползунок/кнопки
  трат), `gui/PSC_construction_expense_widget.gui` (триггер сохранения фактических трат),
  `gui/PSC_states_panel_buildings.gui`, `gui/PSC_goods_texticons.gui`. `common/game_concepts/PSC_game_concepts.txt` —
  понятие `concept_construction_spending`; `gui/scripted_widgets/PSC_scripted_widgets.txt` — регистрация виджета трат
  (`gui/PSC_construction_expense_widget.gui`); оба файла — одна строка без перевода строки.

**Ledgerdemain (`ld_*`) над PSC**
- `common/scripted_effects/ld_construction_market.txt`, `common/script_values/ld_construction_market_values.txt`,
  `common/static_modifiers/ld_construction_market_modifiers.txt` (`zz_ef_reg_in_<товар>`: `goods_input_<товар>_mult`),
  `common/modifier_type_definitions/ld_construction_market_modifier_types.txt` (типы `goods_input_<стройтовар>_mult` —
  у товаров мода их нет), `localization/*/ld_construction_market_l_*.yml` — закупка регулятора по рынку (Д.R9.5,
  Д.R9.11): `zz_ef_reg_market_step` в штате с регулятором каждую неделю PSC — доля товара `var:zz_ef_reg_s_<товар>` —
  полшага (`zz_ef_reg_step`) к предложению рынка × (самая низкая местная цена / местная цена)² (местная цена — база × (1
  + `state_goods_pricier`)); множители входа — локальные переменные штата (блок регулятора читает только их). Очки и
  вес штата — по базовой цене товара метода регулятора (`calculate_state_construction_base_price`, как без смеси):
  закупка дешёвого дерева в модели цены PSC не дорожает (Д.R9.11).
- Снят в R9 и лежит в архиве: регулятор не больше предложения рынка (Д.R9.4 — очки −60 %, `_archive/ld_psc_market_fill/`);
  вернуть — R9б, вместе с выпуском секторов (Д.R9.10).
- `common/script_values/ld_psc_private_allocation.txt` — REPLACE `private_construction_increase` (цель
  `zz_ef_psc_private_target`: доход + простаивающий пул + ставка, × рычаг кредита `zz_ef_psc_credit_f` — от 0,5 без
  свободного лимита банков до 1, когда свободный лимит страны `var:zz_ef_bk_free_cr` ≥ 13 недель нового делового
  кредита (Д.R9.2, принято ночью; `docs/banks.md`).
- `common/script_values/ld_pb_overbuild_values.txt` — лимит и перестройка: `zz_pb_ef_css_levels`,
  `zz_pb_ef_urban_center_levels`, `zz_pb_ef_css_rate_factor`, `zz_pb_ef_overcap_target/gap`, `zz_pb_ef_overbuild_step`,
  цена выкупа `zz_pb_ef_state_css_buyout`, порядок сноса `zz_pb_ef_state_css_downsize_order`.
- `common/script_values/ld_pb_remap_pcs_values.txt` — `pcs_construction_sector_headroom_by_base_rate`;
  `ld_pb_ai_construction_values.txt` — бонус ИИ от дороговизны стройтоваров.
- `common/on_actions/ld_pb_overbuild_counter.txt` — месячный счётчик перестройки (`zz_pb_ef_overbuild_counter`).
- `common/on_actions/ld_pb_ai_sector_downsize.txt` + `common/scripted_effects/ld_pb_ai_sector_downsize_effects.txt` — ИИ
  сносит по уровню (`zz_pb_ef_css_downsize_one`); выкуп частных уровней — проводка казна → пул, получатель — вклады
  населения (`zz_ef_post_eng`, `CLAIM = zz_ef_pop_deposits`).
- `common/static_modifiers/ld_pb_overbuild_modifiers.txt` — `zz_pb_ef_overbuilt_economy`
  (`building_construction_sector_throughput_add`); `common/messages/ld_pb_overbuild_messages.txt` —
  `zz_pb_ef_overbuild_rising`.
- `common/scripted_buttons/ld_pb_css_private_ban_buttons.txt` — AI-кнопки запрета/разрешения частных секторов;
  `common/scripted_guis/ld_pb_fso_sguis.txt` — видимость секций журнала и те же ban/allow для игрока.
- `gui/scripted_widgets/ld_pb_fso_widgets.gui` — пересобранный журнал «Financial Stability Office»
  (`financial_center_je_2`): секции пузыря и перепроизводства; `gui/ld_national_capacity_chart.gui` — копия диаграммы
  E&F (не стройка, лишь в списке подсистемы).
- `common/static_modifiers/ld_rate_private_construction.txt` (+ `zz_ef_rate_construction_mult` в
  `ld_money_model_values.txt`, запись в `ld_money_model.txt:1058`) — вклад ставки ЦБ в долю частной стройки.

**Домохозяйства**
- `common/pop_needs/ld_household_construction.txt` — `popneed_household_construction` (4 стройтовара); подключён в
  `common/buy_packages/00_ef_buy_packages.txt` (`wealth_1..9`).
- `common/production_methods/ld_household_construction_pms.txt` — 10 `INJECT:` в натуральные PM
  (`pm_home_workshops_*_subsistence_*`: +0.06 `wood_construction`, рисовые — 0.12; Д.Г.7) и 4 `REPLACE:` ванильных PM
  городского центра (`pm_market_stalls/squares/covered_markets/arcades`: вход — стройтовар). Ключи — ванильные имена,
  поэтому refs=0 в индексе.

**E&F**
- `common/building_groups/00_ef_building_groups.txt:123` — группа `bg_ef_private_construction` (зданий в ней нет; на неё
  ссылается запись `bg_ef_private_construction_score` в `INJECT:building_financial_district`,
  `common/buildings/ef_11_private_infrastructure.txt:39`).
- `common/buildings/ef_11_private_infrastructure.txt` — не здание: `INJECT` PMG `pmg_market_liquidity` в порт/железную дорогу/торговый центр и `investment_scores` в `building_financial_district`
  (`bg_construction_score` живой, `bg_ef_private_construction_score` — в группу без зданий).
- `common/script_values/00_financial_scripted_value.txt:123-190` — переопределены:
  `building_urban_center_lvl_by_base_rate` (лимит), `building_ef_private_construction_lvl` (= сумма уровней
  `building_construction_sector`), `..._lvl_to_build`, `..._lvl_state`.
- `common/scripted_effects/09_introduction_building_lvl.txt` — ~50 тыс. строк: валюты/центробанк/ФЦ, не стройка.
- `common/history/buildings/00_ef_building.txt` — стартовые `create_building building_construction_sector` (213
  `create_building`, ~28 — сектор; рудники — не выше того, что держит ресурс штата) с владельцами-банками/компаниями;
  `00_a_ef_history_var_init.txt` — предзапись переменных (стройки не касается).
- `common/defines/zz_ef_reinvestment_defines.txt` — `REINVESTMENT_SUBSISTENCE_FRACTION_REDUCTION = 0`,
  `OWNER_COMPANY_PRIVATIZATION_CHANCE_MULTIPLIER = 0.4`; `zzzz_ef_credit_def.txt` (кредитный лимит) и
  `00_ef_defines.txt` (приватизация закомментирована) со стройкой не связаны.
- `common/scripted_guis/00_financial_scripted_guis.txt:3997-4152` — кнопки стимула `speculative_share_9..12_button`
  (ставят `var:zz_pb_ef_stimulus_mult` на 1080 дней, +10..+40 к `speculative_share_2`).

## Поток / порядок
1. `history/global/PSC_global.txt` -> `set_construction_start`: запуск `set_construction_weekly_on_action` и
   `set_construction_country` для всех стран.
2. `on_monthly_pulse` -> `set_construction_weekly_on_action`: для каждой страны глобальная `added_days` -> цикл по дням
   месяца, `delay_event_switch` ставит `set_construction_country` и `set_spending_value` с задержкой (шаг 1+6 = раз в 7
   дней).
3. `set_construction_country` (раз в игровую дату) -> `set_construction_point_demand` (страна, недельный, при изученной
   `urbanization`):
   - снимает старый модификатор `country_private_construction_allocation_add`;
   - `privatisation_percent_estimate` (сглаживание по `privatisation_percent_weeks`), обнуляет
     `national_production`/`weighted_total`, по штатам суммирует производство `*_construction`
     (`sum_construction_types_production`);
   - `corrected_private_allocation` -> `max_government_construction_spending` -> `check_construction_spending_level`
     (игрок 0.25 по умолчанию; ИИ = `ai_construction_demand` / макс) -> `limited_government_construction_spending`;
   - `private_construction_increase` (в форке = `zz_ef_psc_private_target - corrected_private_allocation`) кладётся
     модификатором `country_private_construction_allocation_add`;
   - `total_construction_spending` и по штатам в порядке `construction_ordering` (`ordered_scope_state`: `min = 0`,
     `max = 1000`, `check_range_bounds = no` — все штаты): `set_construction_regulator_level` (регулятор растёт до
     уровня сектора, не сносится — Д.R8в.27), `state_construction_spending_allocation` (доля штата — по стоимости его
     выпуска: выпуск × базовая цена / `weighted_total`; от 0 до остатка трат страны
     `var:psc_remaining_construction_spending` — переменная страны, уменьшается после каждого штата и снимается после
     цикла), `set_state_construction_efficiency` (модификатор на сектор), `state_construction_allocation` ->
     `construction_throughput_mult` на регуляторе; перед этим — `zz_ef_reg_market_step` (доли закупки, Д.R9.5);
   - `prev_estimated_investment_pool = investment_pool + investment_pool_net_income`.
4. `set_spending_value` (только игрок) -> `set_government_construction_spending`.
5. `on_production_method_changed`, `on_building_built` (сектор) -> `set_new_point_conversion_method` (PM регулятора = PM
   сектора; в штате без регулятора — ничего); `on_acquired_technology` -> `set_point_conversion_method_from_tech`.
6. `on_monthly_pulse_country`: `zz_pb_ef_overbuild_counter` (месяц: `speculative_share_2` += шаг к цели
   `zz_pb_ef_overcap_target`, модификатор `zz_pb_ef_overbuilt_economy` x значение, уведомление, бар
   `financial_center_je_2`) и `zz_pb_ef_ai_sector_downsize` (ИИ; раз в 3 месяца: если `speculative_share_2 >= 10` и
   сектора выше лимита — `zz_pb_ef_css_downsize_one` в штате по `zz_pb_ef_state_css_downsize_order`).
7. Строительство вне цикла: `can_build_private` сектора (`owner` без `zz_pb_ef_css_private_ban`, уровни <=
   `building_urban_center_lvl_by_base_rate` или `building_urban_center_lvl`), `ai_value` (0 при превышении лимита).

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `zz_ef_reg_s_<товар>` (штат) | доля товара в закупке регулятора (Д.R9.5) | `zz_ef_reg_market_step` | он же |
| `last_construction_run` (страна) | дата последнего пересчёта | `set_construction_country`, `psc_save_real_construction_cost` | `psc_test_show`, `on_acquired_construction_tech` |
| `construction_spending_level` (страна) | доля макс. госрасходов на стройку | `check_construction_spending_level`, `psc_button_*_sgui` | `max_government_construction_at_spending_level` |
| `max_government_construction_spending`, `max_government_construction_at_spending_level`, `limited_government_construction_spending`, `total_construction_spending` | расходы | `set_construction_point_demand`, sgui | значения PSC, GUI |
| `real_construction_spending` | фактические траты (из GUI) | `psc_save_real_construction_cost` | `calculate_government_construction_spending` |
| `privatisation_percent_estimate`, `prev_estimated_investment_pool` | доля пула, прошлая оценка | `set_construction_point_demand` | `privatisation_spending_percent*`, `zz_ef_psc_private_income` |
| `corrected_private_allocation`, `prev_construction_allocation`, `weekly_income_multiplier` | поправка долей | `set_construction_point_demand` | `private_construction_increase`, `calculate_max_government_construction_spending` |
| `national_production`, `weighted_total`, `state_construction_production` | производство стройтоваров (страна/штат); `weighted_total` — сумма выпуск × базовая цена по штатам | `set_construction_point_demand` | аллокации |
| `speculative_share_2` | штраф перестройки 0..100 (общая с E&F-кнопками/журналом) | `zz_pb_ef_overbuild_counter`, кнопки 9..12 | downsize, ban-кнопки, `speculative_share_2_penality`, JE-бар |
| `zz_pb_ef_ob_old` | прошлое значение | counter | counter |
| `zz_pb_ef_stimulus_mult` (таймер 1080 дн.) | множитель ставки в лимите вместо 5 | `speculative_share_9..12_button` | `zz_pb_ef_css_rate_mult` |
| `zz_pb_ef_css_private_ban`, `..._cooldown` | запрет частных секторов (6 мес. перерыв) | ban/allow-кнопки и sgui | `can_build_private`, `ai_nationalization_desire` (10 при запрете) |
| `zz_pb_ef_ai_downsize_timer` | период сноса ИИ | downsize | downsize |
| `base_rate_percentage` (E&F) | ставка (доля) | E&F/ld_money_model | лимит, counter, downsize |
| `zz_ef_rate_constr_applied` | вклад ставки в долю, % | `ld_money_model.txt:1058` | `zz_ef_psc_rate_share` |

## Вызовы и связи
- Лимит секторов: `building_urban_center_lvl_by_base_rate` = (уровни `building_urban_center` x
  `zz_pb_ef_css_rate_factor` + x0.25), min 1. Тот же ключ читают E&F-кнопки/GUI
  (`building_ef_private_construction_lvl > ...`) и `zz_pb_ef_overbuild_pct`.
- С моделью денег `ld_*`: читаются `investment_pool*` и `zz_ef_pool_need` (`ld_money_model_values.txt:183`); ставка ЦБ
  входит через `zz_ef_rate_constr_applied`. Пишут деньги: только `zz_pb_ef_css_downsize_one` (выкуп сектора:
  `add_treasury -X` и `add_investment_pool +X`, X = доля частных x уровень x 15000, перенос казна -> пул без
  сторон-контрагентов).
- Сектор «акций» не выпускает (Д.R4б.8) и содержит
  `pmg_market_liquidity` (`pm_market_liquidity_currency`, сохраняется при сносе уровня).
- Покупатели `*_construction`: регулятор (очки), домохозяйства (`popneed_household_construction`), ЖКХ (4 PM городских
  центров).
- GUI: панель стройки (`construction_panel`), журнал FSO (`financial_center_je_2`: `zz_pb_ef_fso_bubble_widget`,
  `zz_pb_ef_fso_overcap_widget`, sgui `zz_pb_ef_fso_*`, `zz_pb_ef_css_private_{ban,allow}_sgui`); алерт
  `insufficient_construction_for_investment` выключен (`valid = { always = no }`: пул при стройке PSC не «простаивает»;
  снятое — `_archive/psc_audit_r9/`).
- ИИ-цены: `ai_construction_sector_price_pressure_bonus` в `ai_value` сектора.

## Логи
`EFZ` (при логах, раз в неделю PSC на страну, `zz_ef_psc_log` в `common/scripted_effects/ld_psc_log.txt`): `total` —
траты на стройку, `alloc` — роздано штатам, `pts` — очки, купленные на них, `rest` — не роздано,
`prod` — выпуск стройтоваров страны, `gov` — государственная часть трат, `wtot` — сумма выпуск × базовая цена по
штатам, `csec_profit`, `csec_lv` — прибыль и уровни стройсекторов, `cf` — рычаг кредита частной доли (Д.R9.2). Сводка
по годам —
`../vic3_mods/tools/ld_psc_sum.py`. Уведомление
игроку: `zz_pb_ef_overbuild_rising` (рост полосы `speculative_share_2` на 10).

## Прочие файлы
- `common/script_values/PSC_set_values.txt` — константы PSC (`privatisation_percent_weeks`, цены строительных товаров,
  `construction_goods_per_point` …).
- `common/script_values/PSC_event_values.txt` — `calculate_added_days` (дни до начала недели для событий PSC).
- `my_trigger_event` (обёртка `trigger_event` по on_action) — из CMF (его файл com_trigger_event.txt), тело то же, что
  было у PSC.
- `common/scripted_effects/PSC_production_method_building_switch.txt` — `production_method_building_switch`.
- `common/script_values/ld_pb_ai_construction_values.txt` — помощники ИИ по цене строительных товаров рынка.
