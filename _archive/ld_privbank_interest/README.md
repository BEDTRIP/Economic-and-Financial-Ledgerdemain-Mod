# Проценты частных банков по чужим облигациям (`ld_privbank_interest`)

Вынуто 8.10.2026 (R1б, решение пользователя В7, аудит R1б.0 — А8). Две несвязанные половины одной выплаты: держатель
получал проценты в пул из ничего, эмитент платил из казны никому — разные переменные E&F, разные даты. Вернуть одной
проводкой эмитент → держатель в реестре облигаций (слоты `zz_ef_pb_*`), этап R5.

## Что делали
1. **Держатель** — `investement_pool_borrowing` (E&F, тело заменено хотфиксом): раз в год, у владельца рынка,
   `add_investment_pool = ai_privat_bank_total_interest` (сумма `ai_privat_bank_interest_calculated_1..25` — проценты по
   облигациям чужих ЦБ, купленным частными банками E&F). Вызов — `central_bank_ef_on_yearly_pulse_country`
   (`00_on_action_main.txt`).
2. **Эмитент** — `zz_ef_privbank_interest_pay` (Ф.2, 4.10): в январе месячного шага казна платит
   `zz_ef_privbank_interest_due` (сумма `ai_entral_bank_debt_privat_bank_interest_refund_per_year_1..25`) — `add_treasury`
   минус, получателя нет; лог `EFM|…|privbank_interest|paid`, переменная `zz_ef_f_pbi_paid`.

## Удалено из живых файлов
| файл | что |
| --- | --- |
| `common/scripted_effects/01_economic_scripted_effects.txt` | определение `investement_pool_borrowing` с комментарием Ф.2 (на его месте — строка-ссылка сюда) |
| `common/scripted_effects/00_on_action_main.txt` | в `central_bank_ef_on_yearly_pulse_country` — `if = { limit = { market_owner_is_root = yes } investement_pool_borrowing = yes }` |
| `common/script_values/00_financial_scripted_value.txt` | `ai_privat_bank_total_interest` (больше никто не читал) |
| `common/scripted_effects/ld_money_model.txt` | определение `zz_ef_privbank_interest_pay`; в `zz_ef_money_model_monthly_step` — `if = { limit = { month = 0 } zz_ef_privbank_interest_pay = yes }`; абзац шапки о замене `investement_pool_borrowing` |
| `common/script_values/ld_reference_currency_values.txt` | `zz_ef_privbank_interest_due` |

Значения E&F `ai_entral_bank_debt_privat_bank_interest_refund_per_year_1..25` остались — их читает E&F
(`00_financial_scripted_value.txt`, сумма «золото в займах»).

## Как вернуть
Вставить определения на прежние места (тексты — здесь, по исходным путям) и оба вызова. Лучше — не возвращать половины,
а сделать проводку `zz_ef_post_eng` эмитент (казна) → держатель (пул) в реестре облигаций (R5).
