# Кризисная продажа валюты E&F по 95 валютам (`all_currency_resold`, `sell_<cur>_currency_crisis`)

**Что делало:** при кризисе валюты страны (E&F `global_monetary_reference_reset` — банкротство ЦБ эталона;
`economic_instability` — валютный кризис) каждая страна с ЦБ звала `all_currency_resold` (`00_on_action_main.txt`) —
лестница по 95 валютам → `sell_<cur>_currency_crisis` (`01_economic_scripted_effects.txt`): весь запас валюты кризиса
в ЦБ-штате продавца (`stockpiling_<cur>_state_1`) — эмитенту за металл по паритету (`zz_ef_crisis_redeem`), запас — в 0,
`reset_debt_in_national_currency` у эмитента.

**Почему вынуто (R8б, шаг 2):** чужие деньги ЦБ — реестр требований (карта `zz_ef_rq_cb_m`, `docs/claims.md`), а не
запасы E&F в ЦБ-штатах; продажа держателей — `zz_ef_rq_crisis_resell` (`common/scripted_effects/ld_claims.txt`).
`reset_debt_in_national_currency` из тела `sell_<cur>_currency_crisis` новым кодом не зовётся (долг E&F в нацвалюте
модель не ведёт).

**Удалено из живых файлов:**
- `common/scripted_effects/00_on_action_main.txt` — `all_currency_resold` (здесь);
- `common/scripted_effects/01_economic_scripted_effects.txt` — 95 `sell_<cur>_currency_crisis` (здесь);
- `common/scripted_effects/01_economic_scripted_effects.txt`, `global_monetary_reference_reset` и
  `common/scripted_effects/01_financial_scripted_effects.txt`, `economic_instability` — блок
  `every_country = { if = { limit = { has_modifier = has_central_bank not = { this = root } } save_scope_as = seller all_currency_resold = yes } }`
  заменён на `zz_ef_rq_crisis_resell = yes`.
