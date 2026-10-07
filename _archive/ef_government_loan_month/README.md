# Долг казны ЦБ от чеканки E&F (`government_loan_month`)

**Что делало:** раз в месяц (`central_bank_ef_on_monthly_pulse_country`) `government_loan` (долг казны ЦБ, E&F)
+= `country_minting_month` (модификаторы чеканки страны × 4) — долг рос без денег и без пары.

**Почему вынесено:** R2, шаг 5 (Д.R2.5): из месячного шага ЦБ E&F снять записи в деньги, металл и запасы мимо учёта;
инфляция, курсы и `currency_strength_modifier` счетов не пишут и остались (курсы — R3). Кредит ЦБ казне — счёт реестра
и проводки (R2, шаг 8), `government_loan` — его зеркало.

**Кто вызывал:** `central_bank_ef_on_monthly_pulse_country` (`common/scripted_effects/00_on_action_main.txt`), после
`currency_strength_modifier = yes`.

## Вырезано (текст — по тем же путям)
- `common/scripted_effects/00_on_action_main.txt`: строка `government_loan_month = yes`.
- `common/scripted_effects/01_economic_scripted_effects.txt`: определение `government_loan_month`.
- `common/script_values/00_economic_scripted_value.txt`: `country_minting_month` (читал только он).

**Вернуть:** на место по описанию; по схеме — не возвращать (чеканка — металл, R2 / R13).
