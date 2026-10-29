---
type: code
description: "Ввод валюты E&F по культуре: при технологии currency_standards или постройке ЦБ (introduction_new_currency) 95 эффектов introduction_of_<cur> выбирали валюту E&F по культуре страны…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_currency_introduction/**"]
---
# Ввод валюты E&F по культуре

**Что делало:** при технологии `currency_standards` или постройке ЦБ (`introduction_new_currency`) 95 эффектов
`introduction_of_<cur>` выбирали валюту E&F по культуре страны (`currency_identifiers_<cur>`, script values по основным
культурам), и стране на фиате давали серебряный стандарт до 1873 года и золотой после, случайный паритет 15–30
(серебро) или 1–2 (золото), деньги в счёт E&F (`circulating_<cur>_c_var_1` + 50–100 млн), запас ЦБ и металл столицы
«из ничего» ((деньги + запас + сбережения) × паритет), сообщение игрокам о новом ЦБ.

**Почему ушло:** валюта у каждого тега своя, название — по стране ([[Д.R8а.3 — Валюта у каждого тега своя, кроме валютных союзов|Д.R8а.3]], [[Д.R8а.7 — Формирование валют E&F|Д.R8а.7]]); ввод не трогает страну с
паритетом, паритет новой валюты — от денег её рынка ([[Д.R8в.7 — Ввод валюты E&F не трогает страну, у которой уже есть валюта и паритет|Д.R8в.7]]); металл «из ничего» модель уже возвращала обёрткой.
Замена — один эффект `zz_ef_cur_intro` (`common/scripted_effects/ld_currency_intro.txt`): стандарт по дате, паритет
хозяина рынка или средний паритет E&F, без металла и денег E&F; сообщение игрокам осталось.

**Вырезано:** `introduction_of_<cur>` (95, `09_introduction_building_lvl.txt`), `currency_identifiers_<cur>` (95,
`01_economic_currency_scripted_value.txt`), `zz_ef_cur_intro_first_v` (`ld_money_model_values.txt`, строка лога металла
ввода). Проверки `currency_identifiers_<cur> = 1` в пользовательской локализации и спросе на валюту сюзерена
(`central_bank_overlord_currency_purchases`) — `var:zz_ef_cur ?= flag:<cur>`; `zz_ef_has_currency_identifier` —
`has_variable = zz_ef_cur`.
