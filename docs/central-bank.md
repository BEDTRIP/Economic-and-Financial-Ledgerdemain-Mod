# ЦБ: ставка, денежная политика, кредит ЦБ, облигации ЦБ, премия за риск
Ставка ЦБ (`var:base_rate_percentage`, доли: 0.05 = 5%) каждые 3 месяца шагает к цели: правило (нейтральная + инфляция + рост денег + покрытие металлом)
плюс политика игрока `var:zz_ef_rate_bias` (±2 пп, кнопки). Девальвация/ревальвация — инструмент ЦБ с целью по покрытию; ИИ двигает паритет
по правилу. Премия за риск правительства (рейтинг + стабильность + валюта + долг + дефицит) входит в ставку государственных займов.
Выпуск облигаций зданием ЦБ масштабируется по долгу/ВВП.

## Файлы
- Ставка: `common/script_values/ld_cb_rate_values.txt` (правило, цель, шаг, значения в пп для GUI), `common/on_actions/ld_cb_rate_on_actions.txt` (`zz_ef_cb_rate_monthly`), `common/scripted_effects/ld_central_bank_rate.txt` (`zz_ef_cb_rate_step`).
- Кнопки/подсказки: `common/scripted_guis/ld_cb_rate_buttons.txt` (`zz_ef_cb_rule_above_rate/_below_rate/_at_rate` — цвет блока правила), `common/game_concepts/ld_cb_rate_concepts.txt` (`concept_zz_ef_policy_rule_rate`, `concept_zz_ef_discretionary_adjustment`). Сами кнопки — `base_rate_increase` / `base_rate_reduce` в `common/scripted_guis/00_financial_scripted_guis.txt:3683, 3729` (тело E&F переписано под `zz_ef_rate_bias`). Панель — `gui/ld_cb_rate_panel.gui` (описана отдельно).
- Цена политики ставки: `common/scripted_effects/ld_rate_policy.txt` (`zz_ef_rate_policy_costs`), `common/static_modifiers/ld_rate_policy.txt` (`zz_ef_rate_policy_authority`, `_hard_money`, `_soft_money`).
- Ставка госзаймов: `common/static_modifiers/ld_gov_rate.txt` (`zz_ef_gov_rate_mult`, `zz_ef_gov_rate_add`; ставит `ld_money_model.txt:1393`).
- Ставка → частная стройка: `common/static_modifiers/ld_rate_private_construction.txt` (множитель `zz_ef_rate_construction_mult`, `ld_money_model_values.txt:283`; ставит `ld_money_model.txt:1059`).
- Девальвация/ревальвация (генерируются `tools/regen_ef_monetary_policy.py`): `common/scripted_effects/ld_monetary_policy.txt` (`zz_ef_mp_init/_clear/_complete/_step`), `common/script_values/ld_monetary_policy_values.txt` (константы `zz_ef_mp_*`, выпуск/изъятие), `common/scripted_guis/ld_monetary_policy_buttons.txt` (`zz_ef_mp_visible`, `zz_ef_mp_target_m5/m1/p1/p5`, `zz_ef_mp_pace_minus/plus`), `common/scripted_triggers/ld_monetary_policy_triggers.txt` (`zz_ef_mp_can_work`, `zz_ef_mp_law_on`); законы `common/laws/01_ef_monetary_policy.txt`.
- Соотношение биметаллизма (Д.R8а.11, руками): `common/scripted_triggers/ld_bimet_ratio_triggers.txt` — `zz_ef_can_bimet_ratio` (кто двигает рычаг: биметаллизм, ЦБ, `var:zz_ef_bimet_ratio`; условие — только здесь), `common/scripted_guis/ld_bimet_ratio_buttons.txt` — `zz_ef_bimet_ratio_minus/_plus` (±0,5, от 10 до 25), строка «Золото : серебро» в `gui/ld_cb_rate_panel.gui` после строки девальвации/ревальвации; читает `bimetallic_rate_gold_to_silver` (`00_economic_scripted_value.txt`). ИИ соотношение не двигает.
- Кредит ЦБ: `common/script_values/ld_cb_loan_values.txt` (`zz_ef_cb_loan_after_to_gdp`, `_now_to_gdp`); кнопка `set_debt_issued` — `00_financial_scripted_guis.txt:2294` (лимит 50% ВВП), `debt_issued_relative_GDP_reduce` (:2270).
- Облигации ЦБ: `common/script_values/ld_cb_bond_issuance_values.txt`, `common/scripted_effects/ld_cb_bond_issuance.txt` (`zz_ef_cb_bond_issuance_update`), `common/static_modifiers/ld_cb_bond_issuance.txt` (`zz_ef_cb_bond_issuance_low/_high`, `goods_output_bond_mult` ±0.01 за единицу).
- Премия за риск: `common/script_values/ld_risk_premium_values.txt`, `common/scripted_effects/ld_risk_premium.txt`.
- Закон «Центральный банк» (R3.2): группа `common/law_groups/ld_central_bank.txt` (`lawgroup_ld_central_bank`), законы `common/laws/ld_central_bank_laws.txt` (`law_ld_cb_state` / `_private` / `_none`, флаг `var:zz_ef_cb_kind` = `flag:state/private/none`; не принимаются — `can_enact = { always = no }`; государственный и частный — с технологией `central_banking`), `common/scripted_effects/ld_cb_law.txt` (`zz_ef_cb_law_sync`: есть `has_central_bank` → государственный, нет → «без ЦБ»; частный не трогает), зовут `common/history/global/ld_central_bank_law.txt` (старт) и хаб E&F `ef_on_monthly_pulse_country` (`on_actions/00_ef_on_action.txt`, месяц); локализация `ld_cb_law_l_*.yml`. Поведение видов ЦБ — R4.
- ЖЗ: `common/journal_entries/00_ef_bank_central_je.txt` — `bank_je_central_1`: игроку без ЦБ; ежемесячно ставит индикаторы и выдаёт технологии `banking` + `currency_standards` при ВВП ≥ 2.5 млн, `central_banking` при ≥ 5 млн; по завершении `bank_je_central_2`.
- Связанные файлы E&F с правкой в теле: `scripted_effects/01_economic_scripted_effects.txt` (`on_activate_law_revaluation/devaluation/no_monetary_policy` :35349-:42350 зовут `zz_ef_mp_init/_clear`; идеология «большая денежная политика» в `monetary_policy_ideology_dynamic` (:34557-:41604) учитывает `zz_ef_rate_policy_steps`), `scripted_effects/00_on_action_main.txt` (:17170 `update_modifiers_bc_fc_ns` → `zz_ef_cb_bond_issuance_update`).

## Поток / порядок
1. Месяц, `on_monthly_pulse_country` → `zz_ef_cb_rate_monthly`: `zz_ef_risk_monthly`; задаёт `zz_ef_rate_bias = 0`, если нет; счётчик `zz_ef_cb_rate_month` 1,2,3; на 3 — сброс и `zz_ef_cb_rate_step`.
2. `zz_ef_cb_rate_step`: `base_rate_percentage += zz_ef_cb_rate_next_step`; ставит `rise_base_rate`/`down_base_rate` на 3 мес. (E&F читает их для арбитража, `00_on_action_main.txt:336`).
3. Цель: `zz_ef_cb_rate_rating_target` = нейтраль (3% металл / 2.5% фиат) + инфляция (фиат) + рост денег − ВВП (±) + покрытие (металл); коридор 2..12% металл, 0.5..25% фиат, у зависимых (золотой обменный, внешневалютный) — от ставки эталона `global_var:zz_ef_ref_rate` до неё + 4 пп в пределах 2..12% (`zz_ef_cb_rate_is_dependent`, R3.3) (`zz_ef_cb_rate_floor/ceiling`). `zz_ef_cb_rate_target` = правило + `var:zz_ef_rate_bias`. Шаг 0.5 пп (1 пп при разрыве > 5 пп). Страны без ЦБ — 6.5%.
4. Месячный шаг денежной модели (`ld_money_model.txt`): `zz_ef_rate_policy_costs` (:1043), `zz_ef_mp_step` (:1050), стройка (:1059), ставка госзаймов (:1393).
5. Девальвация/ревальвация: закон → `zz_ef_mp_init` (старт = цель = покрытие). Игрок двигает `zz_ef_mp_target` кнопками (взвод `zz_ef_mp_armed`); `zz_ef_mp_step` ежемесячно: девальвация печатает `add_treasury` (`zz_ef_mp_issue`), ревальвация изымает (`zz_ef_mp_withdraw`); цель достигнута → `zz_ef_mp_complete` (паритет × покрытие / стартовое, пауза 730 дней, `zz_ef_risk_parity_changed`, закон → `law_no_monetary_policy`). ИИ без закона: покрытие < 25% или > 80% 24 месяца → паритет × `zz_ef_mp_ai_parity_step` (±25%), пауза 5 лет.
6. Премия: `zz_ef_cb_rule_risk` = `zz_ef_cb_rule_rating` (0.6 пп за балл ниже 10 из `country_credit_note_fixe`) + `zz_ef_cb_rule_stability` (дефолт, радикалы, легитимность, война, грамотность + `zz_ef_risk_fx` + `zz_ef_risk_debt` + `zz_ef_risk_deficit`), 0..8 пп; не входит в ставку ЦБ.
7. Облигации: `update_modifiers_bc_fc_ns` (страны со зданием банка) → `zz_ef_cb_bond_issuance_update`: на каждое `building_bank` — `zz_ef_cb_bond_issuance_low/_high` с множителем из `var:zz_ef_cb_bond_low/_high`; выход = E&F × (долг% / `zz_ef_cb_bond_reference_debt_pct` = 50), 0..3×.

## Переменные
| имя | смысл | пишет | читает |
|---|---|---|---|
| `base_rate_percentage` | ставка ЦБ (доли) | история E&F, `zz_ef_cb_rate_step` | `zz_ef_cb_rate_gap`, `zz_ef_cb_rule_gap` |
| `base_rate_percentage_old` | ставка до шага | `zz_ef_cb_rate_step` | он же |
| `zz_ef_rate_bias` | политика игрока, ±0.02, шаг 0.005 | `base_rate_increase/reduce`, `zz_ef_cb_rate_monthly` (init 0) | `zz_ef_cb_rate_target`, `zz_ef_rate_policy_steps` |
| `zz_ef_cb_rate_month` | счётчик 0..2 до шага | `zz_ef_cb_rate_monthly` | `zz_ef_cb_rate_months_to_step` |
| `rise_base_rate`, `down_base_rate` | модификаторы направления шага (3 мес.) | `zz_ef_cb_rate_step` | E&F (`00_on_action_main.txt:336`, :8886) |
| `zz_ef_mp_start/target/prev/dyn/flow/cum/pace/armed/cooldown` | состояние девальвации/ревальвации | `zz_ef_mp_*`, кнопки | `zz_ef_mp_*_v`, панель |
| `zz_ef_mp_parity_before` | паритет до изменения | `zz_ef_mp_complete`, ИИ-блок `zz_ef_mp_step` | `zz_ef_risk_fx_parity_pen` |
| `zz_ef_mp_low_months`, `zz_ef_mp_high_months` | счётчики ИИ-правила | `zz_ef_mp_step` | он же |
| `zz_ef_bimet_ratio` | законное соотношение золото : серебро биметаллизма | история (FRA 15,5, USA 16,1, NET 15,6), `on_activate` биметаллизма (15, если нет), `zz_ef_bimet_ratio_minus/_plus` | `bimetallic_rate_gold_to_silver`, строка окна ставки ЦБ |
| `zz_ef_risk_fx_pen`, `zz_ef_risk_fx_step`, `zz_ef_risk_susp` | штраф за манипуляцию паритетом / приостановку обмена, затухание 60 мес. | `zz_ef_risk_fx_add`, `zz_ef_risk_monthly` | `zz_ef_risk_fx` |
| `zz_ef_risk_bal_avg` | скользящее (12 мес.) сальдо бюджета / ВВП | `zz_ef_risk_monthly` | `zz_ef_risk_balance_avg` |
| `zz_ef_cb_bond_low`, `zz_ef_cb_bond_high` | множители выпуска облигаций | `zz_ef_cb_bond_issuance_update` | то же (`owner.var:`) |
| `credit_at_central_bank`, `government_loan`, `debt_issued_relative_GDP(_percentage)`, `zz_ef_cb_writeoff` | долг казны перед ЦБ — счёт реестра (деньги движка; `government_loan` — то же в валюте E&F), размер займа, списанное ЦБ без денег | `set_debt_issued`, `refund_credit_at_central_bank(_all)`, ИИ `ai_credit_at_central_bank` / `ai_refund_central_bank` — проводками (деньги казны помечены `zz_ef_tr_mark`) | `zz_ef_cb_loan_*`, `zz_ef_cb_bond_debt_pct`, `ld_money_model_values.txt:301` |
| `country_credit_note_fixe` | рейтинг E&F 0..12.5 | E&F | `zz_ef_cb_rule_rating`, `zz_ef_reference_candidate` |

## Вызовы и связи
- Кто зовёт: `ld_money_model.txt` — `zz_ef_rate_policy_costs`, `zz_ef_mp_step`, `zz_ef_gov_rate_*`, стройка; `base_rate_increase/reduce` — `zz_ef_rate_policy_costs`; E&F-законы — `zz_ef_mp_init/_clear`.
- Что читает ЦБ из денежной модели: `zz_ef_cb_cover`, `zz_ef_cover_normal`, `zz_ef_inflation`, `zz_ef_circ_growth_year`, `zz_ef_gdp_growth_year`, `zz_ef_budget_week`, `zz_ef_cb_start_due` (ИИ-политика курса — после стартового металла ЦБ), `zz_ef_value_floor_cover`.
- `zz_ef_mp_can_work` требует металл. стандарт, паритет и `NOT zz_ef_cur_zone` (подданные зоны не девальвируют).
- Закон `law_revaluation/devaluation` блокирует кнопки ставки (повышение/снижение, E&F-условия сохранены).
- GUI: `gui/ld_cb_rate_panel.gui` — блоки ставки, правила, политики; строка девальвации скрыта по `zz_ef_mp_visible` (:9446); значения `zz_ef_cb_*_pp`, `zz_ef_mp_*_v`, `zz_ef_risk_*_pp` — для подсказок.

## Логи
- `EFM|…|done|…`, `EFM|…|step|…`, `EFM|…|ai_parity|…` — `ld_monetary_policy.txt` (завершение, месячный шаг, ИИ-паритет).
- Для ставки, облигаций и премии `debug_log` нет.
