---
type: code
description: "Лидер валюты E&F: списки, модификаторы, медиана: раз в год (currency_law_list у держателя эталона, старт, кнопки окна) 95 эффектов <cur>_currency_law_list (08_list_effect.txt) собирали страны с валютой <cur>, ЦБ на…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_currency_leaders/**"]
---
# Лидер валюты E&F: списки, модификаторы, медиана

**Что делало:** раз в год (`currency_law_list` у держателя эталона, старт, кнопки окна) 95 эффектов
`<cur>_currency_law_list` (`08_list_effect.txt`) собирали страны с валютой `<cur>`, ЦБ на стандарте и без привязки
банком к чужой валюте, и вешали на страну с наибольшей `national_capacity_in_gold` модификатор
`<cur>_leading_currency_type` (95 модификаторов, `00_ef_dynamic_modifier_country.txt`). По модификаторам: курс валюты E&F
`money_value_<cur>_global_var` (сумма по носителям модификатора), число лидеров `leading_currency_type`,
`money_value_in_gold_by_country` (сумма 95 курсов) и медиана `weighted_average_currency_value` = сумма / число, флаг
`is_reference_type`.

**Почему ушло:** валюта у каждого тега своя (Д.R8а.3); лидер — свойство страны, а не валюты E&F: триггер
`zz_ef_cur_leader` (Д.R8в.21, `ld_reference_currency_triggers.txt`) — ЦБ на стандарте, не привязан банком к чужой
валюте, не последователь валютного союза. Медиана — среднее `money_value_in_gold` по всем лидерам, с национальными
валютами (раньше — только 95 валют E&F); курс валюты E&F — лидер с наибольшей ёмкостью (`ordered_country`, `max = 1`).

**Вырезано:** `<cur>_currency_law_list` (95) и `currency_law_list` (`00_on_action_main.txt`), модификаторы
`<cur>_leading_currency_type` (95) и их ключи локализации (английский и русский здесь), значения
`weighted_average_currency_value`, `money_value_in_gold_by_country`, `leading_currency_type`, `is_reference_type`
(`01_economic_currency_scripted_value.txt`; новые три — в `ld_reference_currency_values.txt`); вызовы
`currency_law_list = yes` (годовой пульс, старт, мировой месяц, два окна).

Без читателей после этого остались и тоже вырезаны: `money_value_in_gold_<cur>` (95 значений), эффекты
`money_value_in_gold_<cur>_global_var` (95, `01_economic_scripted_effects.txt`), их вызовы в `money_value_global_var`
(`00_on_action_main.txt`) и нулевой старт глобальных переменных (`00_ef_economic_global_variable.txt`).
