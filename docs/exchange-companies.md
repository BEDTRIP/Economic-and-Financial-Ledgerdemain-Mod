# Биржа, компании, финансовый центр
**Смысл.** Биржа страны (финцентр) и компании: листинг, капитализация, показатели биржи (Д.R4б.11), крах, пузырь. Биржа
требований — одна на страну: стакан на каждый актив с недельным сведением, остаток — фонду (Д.R8б.19–22); R6 — компании.
**Понятия:** [[Биржа]], [[Финцентр]], [[Инвестиционный фонд]], [[Компания|Компании]], [[Межрыночный субъект]],
[[Комиссия биржи]]. **Решения:** Д.R8.5–8.7, Д.R8б.19–22 (`решения.md`).

Биржа — одна на страну (Д.R8.7): здание финцентра (группа `bg_financial_centre`, общий тип и 38 вариантов — оформление)
в штате `var:zz_ef_fc_state` страны; биржи из истории остаются (Д.R8б.14), новую учреждает запись дневника «Учреждение
биржи» (Д.R8б.1). Финцентр — здание государства (Д.R4б.5, Д.R4б.7): группа `bg_financial_centre` финансируется бюджетом
(`is_government_funded`), строит только государство, метод `pmg_zz_ef_fc_exchange`
(`common/production_methods/ld_fc_pm.txt`: клерки 40 и бюрократы 10 на уровень, вход «услуг» 10 и бумаги 5 — принято
ночью); уровни банков в финцентрах истории — государству (`history/buildings/00_ef_building.txt`); методы «акций» E&F —
в `_archive/ef_fc_stock_exchange_pm/`. Комиссия биржи — в казну (`zz_ef_xch_fee_pay`). Финцентр даёт стране модификатор
`has_financial_center` и слоты компаний. Раз в месяц по стране: считается доля публичных штаб-квартир (ШК) компаний,
капитализация рынка акций, скользящие средние, проверка краха, «пузырь», массовое владение акциями. Компании E&F — в
основном банки (105 типов), связаны со зданиями `building_company_<ключ>` и биржевыми зданиями.

## Файлы
Все ключи `ld_*` файлов начинаются с `zz_ef_` (имя файла `ld_`, ключ `zz_ef_`); комментарии внутри ссылаются на старые
имена файлов `zz_ef_*.txt`.
- `common/company_types/00_ef_companies.txt` — 105 типов компаний E&F (банки по странам +
  `company_PennsylvaniaRailroad`, `company_standard_oil`, `company_private_construction`,
  `company_basic_gold_and_silver_mining_2`, `company_basic_gold_mining_rus`, `company_basic_silver_mining_mex`);
  `replaces_company` — подмена старых ключей; `building_types` — `building_zz_ef_bank` (98 раз,
  `common/buildings/ld_bank.txt`) или `building_financial_centre_<код>`.
- `common/game_rules/00_EF_unique_companies_game_rules.txt` — правила
  `unique_companies_banks`/`unique_companies_newspapers` (по умолчанию `*_disabled`, флаги).
- `common/script_values/01_economic_company_value.txt` — НЕ биржа, а частные банки: `total_bank_funds`,
  `private_bank_*_reserve*` (фонды банков E&F — в `_archive/ef_bank_funds/`). Подсистема банков; здесь — только связь.
- `common/scripted_effects/ld_listing.txt` — `zz_ef_listing_update` (месячный перевод ШК в «публичные/частные»),
  `zz_ef_listing_log` (лог `EFL|`).
- `common/scripted_effects/ld_listing_switch.txt` — ГЕНЕРИРУЕТСЯ (`tools/regen_ef_listing.py` в vic3_mods):
  `zz_ef_listing_go_public`, `zz_ef_listing_go_private` — диспетчер по 271 типу ШК (`building_company_*` ванили и E&F;
  `activate_production_method` берёт тип литералом).
- `common/script_values/ld_listing_values.txt` — `zz_ef_hq_levels/_count/_div_week`, `zz_ef_listed_hq_levels`,
  `zz_ef_listed_share`, `zz_ef_listed_div_year`, `zz_ef_equity_premium` (0.04), `zz_ef_cap_discount`,
  `zz_ef_cap_listed_snapshot`, `zz_ef_cap_to_gdp`.
- `common/scripted_triggers/ld_listing_triggers.txt` — `zz_ef_listing_allowed` (биржа ур.≥1 + технология
  `joint_stock_companies` + не традиционализм/командная/кооперативная экономика).
- `common/company_types/ld_companies.txt` — компании форка: `company_baring_brothers` (Baring Brothers, Лондон; особая
  компания-фонд, Д.R9а.1; банковская — свой «Банк» с начала игры, история `00_ef_building.txt`, засев
  `ld_bank_seed.txt`).
- `common/production_methods/ld_company_hq_publicly_traded.txt` +
  `common/production_method_groups/ld_company_hq_publicly_traded.txt` — `pm_company_headquarter_publicly_traded`,
  добавлен INJECT в `pmg_ownership_building_company_headquarter`. Ванильные методы владения штабов —
  `common/production_methods/11_ef_private_infrastructure.txt`: полное тело ванили (категории компаний, законы,
  принципы) с наймом и долями E&F (Д.R9б.7): частный — только у капиталистических компаний, государственный — при
  командной экономике, кооперативный — при кооперативной собственности. Компания-ЦБ при законе гос-ЦБ —
  `pm_company_headquarter_ld_cb_state` (`common/production_methods/ld_company_hq_cb_state.txt`, в группу владения штаба
  — `common/production_method_groups/ld_company_hq_cb_state.txt`, дивиденды казне 100 % — принято ночью): ставит и
  снимает `zz_ef_cb_hq_step` (`ld_listing.txt`, раз в месяц перед листингом; диспетчеры `zz_ef_listing_go_cb_state`,
  `zz_ef_listing_cb_check` — генерат `regen_ef_listing.py`); листинг штаб компании-ЦБ не трогает (R9б.14, Д.R9б.12).
- `common/scripted_effects/ld_capitalization_average.txt` — `zz_ef_cap_monthly_update`: 4 скользящих средних,
  `zz_ef_cap_half` (пункты индекса E&F — в `_archive/ef_stock_market_points/`, Д.R4б.11).
- `common/scripted_effects/ld_capitalization_crash.txt` — `zz_ef_cap_monthly_crash_check`: 12 месячных отметок,
  `country_indice_value_dif_01`, вызов `financial_crash`.
- `common/script_values/ld_capitalization_snapshot.txt` — веса средних, `zz_ef_crash_floor`(5 млн),
  `zz_ef_equity_capitalization` (сумма четырёх средних E&F); капитализация по выпуску товаров-«акций» — в
  `_archive/ld_stock_goods_capitalization/` (Д.R6.12).
- `common/on_actions/ld_capitalization_on_actions.txt` — `zz_ef_capitalization_monthly` (в `on_monthly_pulse_country`),
  задаёт порядок шагов.
- `common/on_actions/ld_bubble_on_actions.txt` + `common/script_values/ld_bubble_values.txt` +
  `common/messages/ld_bubble_messages.txt` — «пузырь» `speculative_share_1`: `zz_ef_bubble_monthly`,
  `zz_ef_bubble_step(_eff)`, `zz_ef_bb_band_*`, сообщение `zz_ef_bubble_rising`.
- `common/script_values/ld_mass_shareholding_values.txt` + `common/static_modifiers/ld_mass_shareholding.txt` —
  `zz_ef_mass_shareholding_points/_max`, модификатор `zz_ef_mass_shareholding`
  (`building_company_worker_dividends_add`).
- `common/scripted_effects/ld_rich_literacy.txt` — `zz_ef_rich_literacy_update`: грамотность богатых — доля ШК, которые
  выходят на биржу; срез выпуска товаров-«акций» по ней — в `_archive/ld_stock_goods_capitalization/`.
- `common/script_values/ld_company_slots.txt` — `zz_ef_slots_rating/_cb/_cap`, `zz_ef_cap_total`; читаются в
  `value_for_has_financial_center` (`common/script_values/00_economic_scripted_value.txt:4354`).
- `common/buildings/ef_16_financial_centre.txt` — генерат (`tools/regen_ld_financial_centres.py`, таблица «вариант →
  тег, область, иконка»): `building_financial_centre` (общий, технология `financial_center`) + 38 вариантов
  `building_financial_centre_<код>` (область — `potential`); у всех `possible` — `zz_ef_fc_possible` (расширяется только
  биржа своей страны). Манчестер, Чикаго, Гонконг — `_archive/ef_fc_second_variants/`.
- `common/scripted_effects/ld_fc_types.txt` — генерат того же генератора, всё, что требует перечня типов:
  `zz_ef_fc_remove` (снести финцентр штата), `zz_ef_fc_expand = { N }` (государственная стройка N уровней биржи),
  `zz_ef_fc_variant_set` (вариант биржи — `var:zz_ef_fc_variant` страны, флаг), `zz_ef_fc_found` (учредить: вариант в
  своей области или общий в столице). Там же генерат — `stock_exchange_name`
  (`common/customizable_localization/00_ef_localization_ custom.txt`, по варианту).
- `common/scripted_effects/ld_fc.txt` — `zz_ef_fc_bind` (на старте: финцентр истории — биржа страны, вариант прежде
  общего; лог `EFH`). `common/scripted_triggers/ld_fc_triggers.txt` — `zz_ef_fc_possible`, `zz_ef_has_exchange` (штат
  биржи свой и в нём финцентр), `zz_ef_fc_can_found` (условия записи дневника). `common/script_values/ld_fc_values.txt`
  — `zz_ef_fc_bank_levels_min` (уровни «Банка» для учреждения, 5 — Д.R8б.24).
- `common/scripted_effects/ld_exchange.txt` — маршрут (Д.R8в.22): `zz_ef_xch_route` (страна, месяц, из
  `zz_ef_money_model_monthly_step`; и в неделю, когда страна биржи исчезла — `var:zz_ef_xch` пуст, недельный шаг модели)
  — `var:zz_ef_xch` (страна, на чьей бирже торгуем) и `var:zz_ef_xch_how`; порядок — 1 своя, 3 лидера своего блока, 4
  сильнейшего блока, 2 хозяина рынка, 5 мировая; сильнейший блок — `zz_ef_xch_strong_bloc_find` (`ordered_power_bloc` по
  `zz_ef_xch_bloc_adv` = `leverage_advantage` на страну среди блоков, чей лидер с биржей и у которых есть влияние —
  `zz_ef_xch_bloc_has_influence`: блоку без влияния движок даёт преимущество 0, а не минус; у самого влиятельного
  преимущество наибольшее, даже отрицательное) и `zz_ef_xch_strong_bloc` (блок найден); лог `EFH|…|route` (с `blev` —
  преимущество выбранного блока) у стран логов; `zz_ef_xch_world_set` (мир, месяц, из `zz_ef_world_month_ef`) —
  `global_var:zz_ef_xch_world`: страна эталонной валюты с биржей, иначе крупнейшая экономика с биржей;
  `zz_ef_xch_fees_set` — комиссии биржи по видам `var:zz_ef_xch_fee_m/_b/_f` = `zz_ef_xch_fee_v` (база 0,5 % × метод
  здания биржи и закон — ниже, «Здание биржи»; без здания — минус 15 % базы за каждую финансовую технологию страны биржи
  — фондовая биржа, акционерные общества, инвестиционные банки, паевые фонды, международные стандарты обмена,
  современные финансовые инструменты; не ниже 10 % базы; Д.R8.5). Надбавка за чужие требования `zz_ef_xch_surcharge_v`
  (покупатель, должник — `scope:zz_ef_xch_d`): нет для своих, сюзерена и подданного, одного рынка и договора о правах на
  зарубежные инвестиции (`zz_ef_xch_free_with`), иначе по закону торговой политики покупателя — свободная торговля 0,5
  %, меркантилизм 1 %, протекционизм 2 %, кантонская система 3 %; изоляционизм покупателя или должника — сделки нет
  (`zz_ef_xch_banned`; Д.R8б.18). Читатели — торги (`ld_exchange_trade.txt`).
  `common/script_values/ld_exchange_values.txt` — числа, лога.
- **Здание биржи** (R9в; Д.R9в.1–3): `common/buildings/ld_exchange.txt` (`building_ld_exchange`, `buildable = no`,
  `downsizeable = no`), группа `common/building_groups/ld_exchange_group.txt` (`bg_ld_exchange` — дочерняя
  `bg_government`: вкладка «Развитие», содержит государство), методы `pmg_ld_exchange_trading`
  (`common/production_method_groups/ld_exchange_pmg.txt`, `common/production_methods/ld_exchange_pm.txt`: голосовые
  торги — без технологии, банкирские дома — `investment_banks`, тикер и клиринг — `international_exchange_standards`;
  клерки и бюрократы на уровень, принято ночью). Месяц (`zz_ef_xb_month_step`,
  `common/scripted_effects/ld_exchange_building.txt`, из `ld_world_month.txt` после `zz_ef_xch_month_roll`, страны с
  `zz_ef_has_exchange`): здания нет — ставится в `var:zz_ef_fc_state` (и в старых сейвах); уровень — на 1 в месяц к цели
  `zz_ef_xb_target_v` (1 + удвоения капитализации `var:zz_ef_xlm_cap` сверх `zz_ef_xb_cap_base` 100 тыс. золота, до 15;
  принято ночью; `add_building_level`); метод — лучший открытый, только где он не активен. Комиссия `zz_ef_xch_fee_v`
  (`ld_exchange_values.txt`) — множитель активного метода `zz_ef_xch_fee_pm_*` × закон экономической системы
  `zz_ef_xch_fee_law_*`; у страны без здания — по технологиям, как прежде. Снос, когда биржи нет, — R11. Триггер
  `zz_ef_xb_has` (`ld_fc_triggers.txt`). Лог `EFD|…|xch_building` (уровень, цель, капитализация в базах, комиссия).
  Комиссия — проводкой в казну, в меню здания — подсказкой (R10).
- Инвестиционный фонд (R8б, шаг 6; Д.R8б.2, Д.R8б.4, Д.R8б.5, Д.R8б.16): здание `building_ld_investment_fund`
  (`common/buildings/ld_investment_fund.txt`; группа `bg_zz_ef_banking`, технология `financial_center`, `possible` —
  штат биржи своей страны, частная стройка) производит паи `mutual_funds` методом `pm_bond_exchange`
  (`pmg_bond_exchange` ушла из финцентра к фонду). Учреждается с биржей (`zz_ef_fund_found`,
  `common/scripted_effects/ld_investment_fund.txt`: из `zz_ef_fc_found` и `zz_ef_fc_bind`). Товар паёв покупает
  население (потребность `popneed_financial_products`; банки — на бирже, `zz_ef_rq_bk_f`, Д.R9б.13); неделя —
  `zz_ef_fund_shares_step`: купленное страной (`zz_ef_fund_bought_week` = потребление `mutual_funds` штатов × цена 250,
  не больше вкладов населения) → требования населения на фонд своей биржи (карта `zz_ef_rq_pp_f`, вид f). Деньги за паи
  движок уже перевёл в кассу здания фонда; модель проводит покупку (Д.R8б.21): вклады населения и капитал банков → вклад
  фонда `var:zz_ef_fd_dep` страны биржи (обязательство её банков — в книге банков и в M2); фонд за границей — покупатель
  платит из пула (`zz_ef_f_fd_out`), страна фонда на своём шаге берёт его в пул и во вклад (`var:zz_ef_fd_in_for` →
  `zz_ef_f_fd_in`); оба — поток с заграницей в клиринг (`zz_ef_ext_net_week`). `zz_ef_fund_week_step` (страна биржи,
  после паёв): приток из-за границы, стартовый вклад банков — доля их капитала `zz_ef_fd_start_share_of_capital` (0,1;
  один раз, флаг `zz_ef_fd_start_due` ставит `zz_ef_fund_found`; банки получают паи); тогда же особые компании-фонды
  страны (Ротшильды, Бэринги — `zz_ef_co_special_fund`, `ld_bank_subjects_triggers.txt`) покупают паи на
  `zz_ef_fd_special_share` (0,1) капитала фонда каждая со своего счёта (`zz_ef_fd_special_start`, Д.R9а.10: вклады
  компаний → вклад фонда, требование `zz_ef_rq_co_f`, доля компании — `var:zz_ef_co_fd_f`; лог `EFK|fund_special`),
  проценты по вкладу фонда по ставке вкладов из капитала банков (`zz_ef_fd_dep_interest`), капитал фонда
  `var:zz_ef_fd_capital` = вклад + книга фонда (карты `zz_ef_rq_fd_m`, `zz_ef_rq_fd_b`) по оценке в золоте
  (`zz_ef_fd_capital_update`; книга переоценивается раз в 4 недели — `zz_ef_xch_phase_week`). Лог `EFU` — раз в месяц по
  фонду (`zz_ef_fund_log`). Дилер: ёмкость `zz_ef_fd_capacity` (уровни × `zz_ef_fd_capacity_per_level`), спред
  `zz_ef_fd_spread` (ключевая ставка × 0,5), справедливая цена денег должника `zz_ef_q_fair_m`
  (`common/script_values/ld_investment_fund_values.txt`). Торги фонда — остаток стакана (Д.R8б.19; ниже — «Торги»).
- **Торги — стакан** (R8б, шаги 7, 13–17; Д.R8б.17, Д.R8б.19–22, Д.R8б.26, Д.R8б.32–37):
  `common/scripted_effects/ld_exchange_trade.txt` (логика), `common/scripted_effects/ld_exchange_book.txt` (генерат
  `tools/regen_ld_exchange_book.py`: карты стакана по шагам цены, читатели, сведение актива),
  `common/scripted_triggers/ld_exchange_trade_triggers.txt` (кто что покупает, сброс ЦБ, свои облигации),
  `common/script_values/ld_exchange_trade_values.txt` (числа). Актив — вид требования (деньги m, облигации b) × должник;
  стакан — на каждой бирже: карты на стране биржи `zz_ef_xs_<вид>_<шаг>` (продажа) и `zz_ef_xb_<вид>_<шаг>` (покупка),
  ключ — должник; шаг цены i = 1..9, цена = справедливая × (1 + (i − 5) × 0,5 %). **Справедливая цена** (на должнике,
  Д.R8б.33): базовая × множитель актива (`var:zz_ef_xmul_m` / `_b`, один на должника в мире; `zz_ef_xch_mul_move` после
  фонда: сдвиг = (остаток покупок − остаток продаж) / глубина рынка — деньги за рубежом `zz_ef_rq_out_m`, не меньше 1 %
  M2 должника (`zz_ef_xmul_depth_m2`), облигации — тело долга, не больше 1 % за сведение, 0,5–2; у разменной валюты —
  между валютными точками ± комиссия своей биржи, `zz_ef_xch_point_v`). Деньги — курс к паритету
  (`zz_ef_value_to_parity` × множитель денег — он внутри курса: курс зависит от покрытия и от биржи; `zz_ef_rq_gpm`
  обновляется сразу), облигации — 1 + (купон − доходность долга) × средний оставшийся срок 3,75 года (`zz_ef_xq_fair_b`,
  0,3–2, × множитель). **Неделя держателя** (`zz_ef_xch_step` из недельного шага, после фонда): (1) расчёт заявок
  прошлой недели (`zz_ef_xch_settle`: итоги сведения своей биржи той же недели — `global_var:zz_ef_xr_week`); (2) заявки
  в стакан биржи маршрута (`zz_ef_xch_post_sells`, `zz_ef_xch_post_buys`; страна А — каждую неделю, Б — раз в 4 недели,
  `zz_ef_xch_posts_this_week`): выгода держания `g` = доходность (деньги — ставка вкладов эмитента, облигации — ставка
  правительства) − ставка дома (население и банки — ставка вкладов своей страны, Д.R8б.40; казна и ЦБ — ключевая; у ЦБ
  обменного стандарта для валюты с разменом — 0, Д.R8б.26) − премия за риск должника − стоимость выхода
  (`zz_ef_xch_exit_v`). **Продают все** (Д.R8б.32): каждый держатель выставляет каждую позицию — меньше 1 % портфеля —
  шаг 1 (уходит первой), ЦБ с покрытием ниже 25 %, продающий валюту вне покрытия, — шаг 1, остальное — справедливая × (1
  + max(g, 0)) (выше шага 9 — нет заявки); если `g` больше издержек покупки — не продаёт, а покупает (скидка покупателя
  = издержки − выгода, Д.R8б.30). Покупка — лучший из короткого списка (хозяин рынка, лидер блока, эталон, три самых
  глубоких рынка — `global_list:zz_ef_xdeep`) по `g` − издержки > 0, на бюджет недели (ЦБ — 1 % металла в деньгах, банки
  — 1 % капитала на деньги, облигации и акции каждые, население — 0,5 % вкладов; банки и население — не больше 10 %
  пула, банки — и не больше трети свободных денег пула `zz_ef_pool_free` на каждый вид, Д.R9.9, `banks.md`); казна
  выкупает свои облигации ниже номинала на 1 % казны в неделю (`zz_ef_xch_buyback`, Д.R8б.37). Издержки покупки
  (`zz_ef_xch_fee_buy_v`) — комиссия биржи + надбавка торговой политики + комиссия нерезидента (`zz_ef_xch_nonres_v`:
  ещё раз комиссия биржи × (1 − ½ доли торговли со страной биржи), Д.R8б.35). Заявки держателя — карты
  `zz_ef_xa_<держатель>_<вид>` (объём) и `zz_ef_xp_…` (шаг; покупка — 10 + шаг); ИИ ставит их заново каждую свою неделю.
  **Сведение** — мировой проход в конце недели (`zz_ef_xch_week_close` из `zz_ef_world_week_close`): глубина рынков,
  эталон (`zz_ef_xref`), три самых глубоких; каждая биржа (`zz_ef_xch_clear_exchange`): котировки фонда в шагах
  (`zz_ef_xr_ib` / `zz_ef_xr_ia`), место фонда (`zz_ef_xr_room`); по каждому активу (`zz_ef_xch_clear_asset_<вид>`) —
  шаг с наибольшим сведённым объёмом, доли крайнего шага; остаток — (1) фонду биржи (`zz_ef_xch_fund_rest`: продажи не
  выше bid — за его место, покупки не ниже ask — из запаса); (2) ЦБ-эмитенту в валютных точках (`zz_ef_xch_points_set`,
  `zz_ef_xch_issuer_rest`, Д.R8б.34: продажи не выше нижней точки — за его металл, покупки не выше верхней — все, он
  выпускает свои деньги; у фиата и облигаций точек нет); множитель актива — после фонда; остатки по справедливой цене
  (`zz_ef_xch_left_set`); итоги — карты `zz_ef_xr_<вид>_c/ps/pb/fs/fb/is/ib/ls/lb/lc`. После всех бирж
  (`zz_ef_xch_cross`, Д.R8б.36; биржи недели — глобальный список `zz_ef_xr_list`): остатки продаж по справедливой и ниже
  одной биржи сводятся с остатками покупок по справедливой и выше другой — доли `_xs` / `_xb` по справедливой цене,
  покупатель платит ещё раз комиссию биржи — во вклад её фонда; дешёвый остаток (по bid фонда и ниже, деньги) выкупает
  фонд с наибольшим местом — доля `_xf`, этот фонд — `var:zz_ef_xcf_m` должника. **Расчёт сделки** (`zz_ef_xch_deal`;
  другая сторона `zz_ef_xd_f`: 0 аукцион, 1 фонд биржи, 2 ЦБ-эмитент, 3 фонды между биржами, 4 фонд другой биржи):
  требование меняет владельца (`zz_ef_rq_add`; свои облигации казны не держатся — гасятся `clear_scaled_debt` на
  купленное / лимит кредита; погашенное тело долга помечено для сверки `zz_ef_tr_mark`), цена в золоте платится в
  деньгах каждой стороны со счёта (Д.R8б.21): население — вклады, банки — капитал, казна — казна, ЦБ — выпуск / изъятие,
  фонд — его вклад; деньги банков и населения — из пула / в пул; цену рассчитывает страна биржи (0, 1), эмитент (2),
  страна фонда (4) — держатель за их пределами — поток с заграницей обеих (`zz_ef_f_xch_net`, у той стороны —
  `zz_ef_xch_ext_acc` до её шага, `zz_ef_xch_ext_in`); между биржами (3) потоки покупателей и продавцов сходятся в
  клиринге; комиссии — стране биржи. Доход от комиссий — владельцам финцентра (`zz_ef_xch_fee_pay`: доля государства — в
  казну, частная — во вклады населения и пул). **Арбитраж биметаллизма** (R8б, шаг 9; Д.R8.10; `zz_ef_xch_bimet_arb`):
  ЦБ своего биметаллического стандарта; за неделю уходит доля недооценённого металла ЦБ = (|разрыв| − 2 комиссии) × 0,5,
  не больше 1 % и места фонда; прибыль — во вклад фонда; металл ЦБ — `var:zz_ef_f_mt_arb_g/_s`. Проценты по чужим
  деньгам — всем держателям (`zz_ef_rq_interest_step`). **Окно игрока** (R8б, шаги 8, 12–14, 17; Д.R8б.13, Д.R8б.35):
  Бюджет → Финансы, раздел «Биржа» (`gui/ld_cb_rate_panel.gui`, `common/scripted_guis/ld_exchange_window.txt`,
  локализация `ld_exchange_window_l_*.yml`): вид (деньги — заявки ЦБ, облигации — казны), сумма заявки; таблицы
  (`zz_ef_xwin_fill`, глобальные списки): «Наши заявки» (`zz_ef_xwin_ord`, «Отменить» — `zz_ef_xwin_cancel`), «Наши
  активы» (`zz_ef_xwin_own`, «Продать» — всё), «Предложения на бирже» (`zz_ef_xwin_book`: прошедшие через её стакан и
  короткий список; облигации — и свои, выкуп), цены денег — в нашей валюте за единицу валюты должника
  (`zz_ef_cur_unit_v` = E&F `money_value_in_gold`), облигаций — % номинала; заполняются кнопкой «Обновить» и раз в
  неделю после сведения. Заявки игрока (`zz_ef_xpl_buy_<вид>` — оставшаяся сумма, `zz_ef_xpl_sell_<вид>`) ставятся в
  стакан каждую его неделю раньше автоматических, пока не исполнятся (`zz_ef_xpl_paid`) или не будут отменены. Логи:
  `EFD` (страна биржи — заголовок недели; должник — `asset|kind` по активу с множителями; `player|side|kind|amount`; ЦБ
  — `arb`; `WORLD` — месяц: заявки, активы, сделки, стоимость в золоте — аукцион, фонды, ЦБ-эмитенты (`cb_buy_g` /
  `cb_sell_g`), между биржами (`cross_g`), арбитраж, пирамида резервов и взаимные остатки обменных ЦБ).
- **Показатели биржи** (Д.R4б.11; [[Биржа]]): пунктов нет — биржи сравнивают по обороту. Сделка (`zz_ef_xch_deal` →
  `zz_ef_xch_month_add`, `ld_exchange_trade.txt`) добавляет бирже `scope:zz_ef_xch_e` модуль стоимости в золоте
  (`var:zz_ef_xd_g`; аукцион `zd_f = 0` — половину) в `zz_ef_xmo_to`, `zz_ef_xmo_to_<K>`, сделку в `zz_ef_xmo_n`,
  держатель не страна биржи — в `zz_ef_xmo_fo`; `zz_ef_xch_fee_pay` — комиссию в золоте `zz_ef_xmo_fee`;
  `zz_ef_xch_clear_exchange` — наибольшее за месяц число активов стакана `zz_ef_xmo_as`. Раз в месяц
  `zz_ef_xch_month_roll` (из `zz_ef_world_month_ef`, без условия логов; следом — потери держателей
  `zz_ef_hl_world_month`, `money-model.md`): каждая страна с `var:zz_ef_xch` оценивает свои карты требований
  (`zz_ef_xmo_cap_map`: 11 карт `zz_ef_rq_<H>_<K>`; на должнике `zz_ef_xk_gold_<K>_v` — рынок, `zz_ef_xk_base_<K>_v` —
  без множителей `zz_ef_xmul_m/_b`; пай — оценка × золото единицы) и добавляет бирже в `zz_ef_xmo_cap` / `_capb`,
  `zz_ef_xmo_mem` + 1; затем у каждой биржи суммы → `var:zz_ef_xlm_*` (доля из-за границы `fo` = `fo` / `to`, перегрев
  `heat` = `cap` / `capb`), оборот за 12 месяцев `zz_ef_xlm_to_y`, строка `EFD|<биржа>|xch_month`, суммы обнуляются.
  Меню: `zz_ef_xch_my_to_v`, `zz_ef_xch_my_heat_v` (биржа страны по маршруту); таблица «Биржи мира»
  (`country_index_variable_in_pts_list`, `08_list_effect.txt`): страны с `zz_ef_has_exchange`, порядок —
  `zz_ef_xlm_rank_v` (оборот за год, в первый год — месяц × 12), колонки — оборот за год, капитализация, перегрев.
- `common/scripted_triggers/ld_power_bloc_triggers.txt` — `REPLACE_OR_CREATE:country_can_form_power_bloc` (ваниль + своя
  биржа, Д.R8.7).
- `common/production_methods/16_ef_financial_centre.txt` + `common/production_method_groups/16_ef_financial_centre.txt`
  — `pmg_bond_exchange` (`pm_bond_exchange`, здание фонда); метод финцентра —
  `common/production_method_groups/ld_fc_pmg.txt` / `common/production_methods/ld_fc_pm.txt` (`pmg_zz_ef_fc_exchange`).
- `common/journal_entries/00_ef_financial_center_je.txt` — `financial_center_je_1` «Учреждение биржи» (у всех стран без
  биржи; биржа есть — `invalid`, запись снимается; выполнено — `zz_ef_fc_can_found`: технология `financial_center`,
  категория А, своя денежная система, банки ≥ `zz_ef_fc_bank_levels_min`; итог — `zz_ef_fc_found`,
  `financial_center_modifier`, запись `financial_center_je_2`), `financial_center_je_2` («Управление финансовой
  стабильностью»: шкала пузыря, кнопки `speculative_share_N_button` (расширение финцентра 5 / 10 / 15 / 20 уровней —
  кнопки 5..8 в `scripted_buttons/00_ef_buttons.txt` и `scripted_guis/00_financial_scripted_guis.txt` зовут
  `zz_ef_fc_expand = { N }`, `common/scripted_effects/ld_fc_types.txt`; любой финцентр — триггер
  `building_financial_centre_any`, национальный — `building_financial_centre_spe`, `00_ef_custom_trigger.txt` — по
  группе `bg_financial_centre`), виджеты `gui/scripted_widgets/ld_pb_fso_widgets.gui`; `on_monthly_pulse` пустой —
  пузырь двигает on_action).
- `common/production_methods/ld_trade_center_settlements.txt` — INJECT в `pm_trade_center` и
  `pm_trade_center_principle_external_trade_2`: `goods_output_liquidity_currency_add = 60` (расчёты-ликвидность).
- Биржевая часть E&F вне перечисленного: `common/script_values/00_financial_scripted_value.txt` (`country_indice`,
  `<вид>_stock_price/_index`, `stockpiling_<вид>_var_state` — переписаны на скользящие средние),
  `common/scripted_effects/01_financial_scripted_effects.txt` (`financial_crash` 33541, `financial_crash_consequences`
  34007), `common/scripted_effects/09_introduction_building_lvl.txt:22135` (`financial_center_modifier`, вешает
  `has_financial_center` с множителем), `common/scripted_effects/00_on_action_main.txt:499`
  (`financial_center_ef_on_half_yearly_pulse_country`, сейчас без биржевой логики).

## Поток / порядок
`on_monthly_pulse_country` → `zz_ef_capitalization_monthly` (`ld_capitalization_on_actions.txt`), страна, по порядку:
1. `zz_ef_rich_literacy_update` — один проход по попам: `zz_ef_literate_rich_share`, `zz_ef_rich_literacy`; доля
   маргиналов `zz_ef_marg` (Д.R7.7, читает цель наличных — `money-model.md`).
2. `zz_ef_listing_update` — если `zz_ef_listing_allowed`: ШК (`bg_company_headquarter`) по возрастанию уровня
   переводятся в `pm_company_headquarter_publicly_traded`, пока накопленные уровни < всех уровней ШК ×
   `zz_ef_rich_literacy`; остальные — `pm_company_headquarter_privately_owned`; компания ШК метится `zz_ef_listing_mark`
   (листинг, IPO — «Акции»). Без разрешения — все ШК в частные, метки сняты.
3. `zz_ef_cap_monthly_update` — снимок = `zz_ef_cap_listed_snapshot` (акции публичных компаний по рыночной цене,
   `zz_ef_co_cap_mkt_v`; Д.R6.12) делится на 4 «акции» E&F поровну, обновляются `zz_ef_cap_avg_{ms,as,mn,rr}` (вес
   0.0833), `zz_ef_cap_half` (вес 0.1667).
4. `zz_ef_listing_log` — строка `EFL|`.
5. `zz_ef_cap_monthly_crash_check` — отметки `zz_ef_cap_m1..m12`, `country_indice_value_dif_01 = half/m12 − 1`; крах
   (`financial_crash`), если < −50%, нет `zz_ef_cap_crash_cooldown` (15 мес), есть `has_financial_center`, капитализация
   > `zz_ef_crash_floor`, дата ≥ 1838.1.1.
6. Массовое владение: `remove_modifier`/`add_modifier zz_ef_mass_shareholding` с множителем `zz_ef_msh_points` (=
   капитализация/ВВП, max 1 × `literacy_rate` × 25). Отдельный on_action `zz_ef_bubble_monthly`
   (`ld_bubble_on_actions.txt`, `on_monthly_pulse_country`; условие: есть `financial_center_je_2` и
   `speculative_share_1`): сдвиг пузыря −3..+3 по `fiancial_center_week_balance_in_ratio`, прогресс-бар, сообщение при
   входе в новую десятку, модификаторы `speculative_bubble_modifier` и `speculative_bubble_character_modifier` (на
   исполнителей). Слоты компаний: `has_financial_center` с множителем `value_for_has_financial_center` =
   `zz_ef_slots_rating` (0..5, из `country_credit_note_fixe`/2) + `zz_ef_slots_cb` (0..5, от ставки ЦБ
   `zz_ef_money_rate`) + `zz_ef_slots_cap` (0..10, +1 за каждые 10% ВВП). Прочее: E&F больше не создаёт финцентры сам
   (по технологии, по ВВП, после краха — `_archive/ef_fc_spawners/`); крах → `economic_instability`; при втором кризисе
   в `01_financial_scripted_effects.txt:33766` — `financial_crash_consequences` (разрушает биржи, `government_loan`,
   `add_investment_pool`; `bankrupt_company` — в архиве, Д.R6.4).

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `zz_ef_literate_rich_share` | доля грамотных богатых (wealth ≥15) среди всех попов | `zz_ef_rich_literacy_update` | лог |
| `zz_ef_rich_literacy` | грамотность самих богатых, 0..1 | `zz_ef_rich_literacy_update` | `zz_ef_listing_update`, лог |
| `zz_ef_cap_avg_ms/_as/_mn/_rr` | годовая средняя капитализации (производство/сельхоз/добыча/ж.д. акции) | `zz_ef_cap_monthly_update` | `stockpiling_<вид>_var_state`, `zz_ef_cap_total` |
| `zz_ef_cap_half` | средняя за полгода по всем акциям | `zz_ef_cap_monthly_update` | краш-проверка |
| `zz_ef_cap_m1..m12` | месячные отметки `zz_ef_cap_half` | `zz_ef_cap_monthly_crash_check` | она же |
| `zz_ef_cap_crash_cooldown` | таймер 15 мес после краха | краш-проверка | она же |
| `country_indice_value_dif_01` | изменение капитализации за год (E&F читает в `financial_crash`) | краш-проверка | меню E&F, `financial_crash` |
| `zz_ef_xmo_*` (`to`, `to_m`, `to_b`, `n`, `fo`, `fee`, `cap`, `capb`, `mem`, `as`; `ya`, `mc` — год) | суммы месяца биржи (страна биржи), в золоте | `zz_ef_xch_month_add` (сделка), `zz_ef_xch_fee_pay` (комиссия), `zz_ef_xch_clear_exchange` (активы), `zz_ef_xch_month_roll` (капитализация, участники) | `zz_ef_xch_month_roll` |
| `zz_ef_xlm_*` (те же и `fo` — доля, `heat`, `to_y`) | показатели прошлого месяца биржи; `to_y` — оборот 12 месяцев | `zz_ef_xch_month_roll` | значения `zz_ef_xlm_*_v`, `zz_ef_xch_my_*_v`, таблица «Биржи мира», лог `EFD|xch_month` |
| `zz_ef_msh_points` | пункты `building_company_worker_dividends_add` | `zz_ef_capitalization_monthly` | модификатор |
| `speculative_share_1` | пузырь 0..100 | `zz_ef_bubble_monthly`, кнопки `speculative_share_N_button` (E&F) | JE, `ld_pb_fso_sguis.txt`, `zz_ef_bubble_step_eff` |
| `zz_ef_bb_old` | пузырь до шага (для уведомления) | `zz_ef_bubble_monthly` | `zz_ef_bb_band_old` |
| локальные `zz_lst_*`, `zz_s_*`, `zz_lr_*` | счётчики внутри эффектов | listing/average/issue | они же |

## Вызовы и связи
- Читает чужое: `zz_ef_gov_rate_target`, `zz_ef_money_rate` (подсистема ставки ЦБ), `country_credit_note_fixe`
  (рейтинг), `gdp`, `literacy_rate`, `weekly_profit` ШК (доход ШК = дивиденды), `<вид>_stock_price` (E&F),
  `fiancial_center_week_balance_in_ratio` (E&F).
- Пишет в чужое: `has_financial_center` (слоты), `financial_crash`/`economic_instability` (E&F),
  `building_company_worker_dividends_add` и выпуск акций на всю страну.
- `stockpiling_<вид>_var_state` (`00_financial_scripted_value.txt:2904`…) переведены с накопления на `zz_ef_cap_avg_*` /
  цену — их читают `country_indice`, меню E&F, рейтинг финансовой мощи.
- GUI: `gui/ld_cb_rate_panel.gui` (оборот биржи `zz_ef_xch_my_to_v` / `zz_ef_xch_my_heat_v`, таблица «Биржи мира» —
  `country_index_variable_in_pts_list` по `zz_ef_xlm_rank_v`; `country_indice`, `value_for_has_financial_center`),
  `gui/ef_dev_and_custom_windows/ef_custom_windows.gui`, `gui/scripted_widgets/ld_pb_fso_widgets.gui` (пузырь),
  `common/scripted_guis/ld_pb_fso_sguis.txt`; панель компаний `gui/companies_panel.gui` (интерфейс-агент).

## Логи
- `EFL|дата|страна|hq|listed|lshare|nhq|hqdiv|lit|div|snap|cap|cap_gdp|disc` — `zz_ef_listing_log` (игрок или ВВП > 20
  млн).
- `ZZEF crash: equity fell by more than half in a year` + `debug_log_scopes` — краш в `zz_ef_cap_monthly_crash_check`.

## Известные несоответствия
- `financial_crash_consequences` перечисляет не все национальные биржи (нет `_dei`, `_han`, `_sax`, `_usa_2`, `_gbr_2`;
  `_TUS` в другом регистре).
- `08_list_effect.txt` ссылается на ключи компаний, которых нет в диспетчере `ld_listing_switch.txt` (диспетчер знает
  только 271 тип); ссылки на ключи, которых нет ни в ванили, ни в CMF/ETF, ни в форке, удалены.

**Счёт компании** (Д.R6.7; [[Компания]]): `common/scripted_effects/ld_company_accounts.txt`,
`common/script_values/ld_company_accounts_values.txt`. Счёт — вклад компании в банках страны, `var:zz_ef_co_acc` на
компании (в деньгах страны); вклады компаний страны `var:zz_ef_comp_dep` (книга банков, M2) = счета существующих
компаний + собиратель — частный сектор вне компаний, `zz_ef_co_rest_v` (остаток; счёт исчезнувшей компании становится
его частью сам, переменные компании уходят с ней). Раз в месяц (`zz_ef_co_month_step`, из
`zz_ef_money_model_monthly_step`): уровни компании `var:zz_ef_co_lv` = `company_owned_levels`, сумма
`var:zz_ef_co_lv_sum`, доля в частных уровнях `var:zz_ef_co_share` (`zz_ef_priv_levels`, не больше 1), приход прошлого
месяца `var:zz_ef_co_in_last`. Приход: `zz_ef_co_credit_lv = { V }` — по уровням на счета и в `zz_ef_comp_dep`: доля
взносов в пул (`zz_ef_f_co_contrib`, `zz_ef_pop_deposits_step`), доля возврата сгоревшего (`zz_ef_co_leak_back`; остаток
— собирателю); снятие `zz_ef_co_take = { V }` — со всех счетов и собирателя одной долей. Лог `EFJ|…|comp` — `acc`, `in`;
`comp_sum` — `comp_dep`, `acc_sum`, `rest`, `share`, `bc_debt`, `co_debt`. Карточка вкладов — строкой (генератор
`regen_ef_money_supply_loc.py`). **Кредит компаний** (Д.R6.9, Д.R6.13): деловой кредит страны `zz_ef_bc_debt`
(`zz_ef_business_credit_step`, `ld_money_model.txt`; вся частная стройка пула сверх нового кредита — тоже он) — компаний
по доле уровней: `zz_ef_co_debt_v` (компания) = долг × `zz_ef_co_lv_part_v` (её уровни / уровни компаний ×
`zz_ef_co_share`), остальное — собирателя; сумма по компаниям `zz_ef_co_debt_sum_v`. Обслуживание недели
(`zz_ef_f_bc_paid`, из взносов в пул) — доля компаний `zz_ef_f_co_paid` со счетов по уровням (`zz_ef_co_pay_lv`; взносы
им приходят той же долей раньше в том же шаге), остальное — из доли населения во взносах. Счёт меньше процентов месяца
(`zz_ef_co_int_month_v`, ставка `zz_ef_cc_rate`) — `var:zz_ef_co_distress` на компании (банкротство — R11). Лог `comp`:
`out` (расход месяца), `debt`, `distress`. **Дивиденды** (Д.R6.8): раз в месяц (`zz_ef_co_month_step`) счёт сверх нормы
— `zz_ef_co_reserve_months` (3, принято ночью) месяцев расхода (обслуживание кредита) — владельцам из населения: вклады
и сбережения населения (один агрегат — категория компании игры пока не делит), `zz_ef_comp_dep` убывает;
`var:zz_ef_f_co_div` (окно `zz_ef_w_co_div` — строка карточки вкладов), на компании `var:zz_ef_co_div_last` (лог `comp`:
`div`). Держатели акций — шаг 6.

**Акции** (R6.6; Д.R6.3, Д.R6.8, Д.R6.10, Д.R6.11, Д.R6.14; [[Компания]], [[Биржа]], [[Требование]]):
`common/scripted_effects/ld_company_shares.txt`, `common/script_values/ld_company_shares_values.txt`; вид требования `s`
в реестре (`docs/claims.md`) и в стакане (`ld_exchange_book.txt` — генератор `regen_ld_exchange_book.py`, вид `s`,
заявки `pp_s`, `bk_s`, `co_s`). Должник — компания. **Листинг:** месячный проход ШК (`zz_ef_listing_update`) метит
компанию диспетчером `zz_ef_listing_mark = { S = public | private }` (генерат `regen_ef_listing.py`: тип ШК → компания
страны — `zz_ef_co_go_public` / `_private`, `var:zz_ef_co_listed`). **IPO** (`zz_ef_co_ipo`; компания в листинге, у её
счёта — `zz_ef_co_ipo_months` (6) месяцев `var:zz_ef_co_months`, прибыль года > 0 — принято ночью): акций
`var:zz_ef_co_shares` = капитализация по справедливой цене (одна акция — единица денег страны по ней, не меньше
`zz_ef_co_ipo_min_shares` = 1000); доля `zz_ef_co_ipo_share` (0,25, принято ночью) — в непроданные (`zz_ef_rq_co_s`
страны), остальное — населению страны (`zz_ef_rq_pp_s`), бесплатно; лог `EFJ|…|ipo`. **Цена** (Д.R6.11): капитализация
по справедливой `zz_ef_co_cap_fair_v` = чистая прибыль года `zz_ef_co_np_y` (приход − расход счёта × 12, скользящая
средняя `zz_ef_co_np_months` = 6 мес., `zz_ef_co_np_update`) / (ставка правительства + `zz_ef_equity_premium`), не
меньше счёта и 1; акция — `zz_ef_co_px_v` = она / акции; в золоте с множителем стакана — `zz_ef_xq_gold_s`
(`var:zz_ef_xmul_s`, глубина — все акции компании); доходность по рыночной цене `zz_ef_co_yield_v`. **Торги:** акции
компании идут на бирже, где торгует её страна (`zz_ef_co_trades_on`: листинг, акции, `owner.var:zz_ef_xch`); список
компаний биржи `zz_ef_xls` — раз в месяц (`zz_ef_co_world_month`). В неделю держателя (`zz_ef_xch_step`): непроданные
IPO — заявка по справедливой (`zz_ef_xch_post_sells_co`); население и банки продают свои (`zz_ef_xch_post_sells_s`:
мелкая позиция — нижний шаг, иначе по выгоде держания, сохраняют, если выгода выше издержек покупки) и покупают лучшую
из списка (`zz_ef_xch_post_buys_s`, бюджет — как на деньги); выгода и издержки — `zz_ef_xch_eval_s` (премия за риск,
стоимость выхода и комиссии — по стране компании). Расчёт — общий (`zz_ef_xch_deal`; комиссия — `zz_ef_xch_deal_fee_s`):
население — вклады и пул, банки — актив `zz_ef_bank_inv` (переоценка по цене акций — `zz_ef_bank_inv_revalue`),
компания-продавец — на счёт (`zz_ef_xch_pay_co_s`, `var:zz_ef_co_ipo_got`, в доход для прибыли не идёт) и пул. Фонда,
валютных точек и сведения между биржами у акций нет. **Дивиденды держателям** (Д.R6.8): у компании с акциями дивиденд
месяца (`zz_ef_co_div_holders`) — держателям по доле (списки держателей компании), доля непроданных остаётся на счёте;
население своей страны — вклады и сбережения, банки — капитал; держатель за рубежом — через клиринг: пул и поток с
заграницей обеих стран (`zz_ef_xch_pool_acc`, `zz_ef_xch_ext_acc` — шаг `zz_ef_xch_step`). Итог держателя по акциям —
`zz_ef_co_holders_month` (перебором: акции исчезнувшей компании пропадают). Сверка реестра (`EFI`) — `n_s`, `out_s`,
`bad_s`; лог стакана `EFD|…|asset_s` (на компании), оборот месяца `to_s_g`, `s_co_g`.

**Компания в скрипте** (проба R6.1, `_archive/ld_probe_co/`): переменные и карты на компании; карта на стране с
ключом-компанией и список компаний работают, как с ключом-страной; исчезнувшая компания уносит свои переменные, ключ
остаётся (`is_key_in_variable_map` — да, `variable_map_size` считает), но перебор его пропускает — суммы по картам
держателей только перебором. Прибыль компании (`Company.GetProfit`, неделя) и касса ШК — только в окне (мост окно →
скрипт, как `gui/ld_bank_hook.gui`); здания компании скрипт не видит. Категория компании — по перечню типов.
