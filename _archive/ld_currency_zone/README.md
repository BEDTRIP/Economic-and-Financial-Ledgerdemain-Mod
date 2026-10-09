# Валютная зона подданного (`zz_ef_cur_zone`)

**Что делало:** раз в месяц (`zz_ef_money_model_monthly_step`), на первом шаге страны и после ввода валюты E&F
(`ld_currency_intro_metal.txt`) подданный сюзерена с ЦБ на металлическом стандарте получал стандарт, закон валюты
(`zz_ef_cur_zone_currency`, цепочка по 95 законам) и паритет сюзерена, переменную `zz_ef_cur_zone` = сюзерен и
модификатор-блокиратор `monetary_systeme_transition` на 2 мес. — чтобы E&F `subject_currency` не переводил его на
внешневалютный стандарт.

**Почему вынесено:** Д.R8а.3 и В-R8а.1 (пользователь 9.10): у подданного своя валюта и свой ЦБ; привязка к сюзерену —
внешневалютный стандарт (`law_external_exchange_standard`), металл остаётся в ЦБ подданного и входит в его покрытие;
резервы в валюте якоря — требованием в реестре R8б. Зона спорила с E&F каждый месяц (Ганновер, Канады, Финляндия).

**Вырезано:** `common/scripted_effects/ld_currency_zone.txt`, `common/scripted_triggers/ld_currency_zone_triggers.txt`
(здесь целиком).

**Удалено из живых файлов:**
- `common/scripted_effects/ld_money_model.txt`: в первом шаге страны после `zz_ef_metal_start_step = yes` —
  `zz_ef_cur_zone_step = yes` (с комментарием); в начале `zz_ef_money_model_monthly_step` — `zz_ef_cur_zone_step = yes`;
- `common/scripted_effects/ld_currency_intro_metal.txt`, `zz_ef_cur_intro_after`: `if = { limit = { is_subject = yes }
  zz_ef_cur_zone_step = yes }`;
- `common/scripted_effects/01_economic_scripted_effects.txt`, `subject_currency`: обёртка `if = { limit = { NOT = {
  has_variable = zz_ef_cur_zone } } … }` (тело E&F осталось);
- генераты (`vic3_mods/tools`): `ld_clearing.txt` / `ld_clearing_values.txt` (`zz_ef_clr_head_find`, `zz_ef_clr_gpm_head`:
  `has_variable = zz_ef_cur_zone` → `has_law = law_type:law_external_exchange_standard`), `ld_nr_deposits_triggers.txt`
  (`zz_ef_nr_issuer`: то же), `ld_monetary_policy_triggers.txt` (`zz_ef_mp_can_work`: строка `NOT = { has_variable =
  zz_ef_cur_zone }`), `ld_currency_var.txt` (`zz_ef_cur_par_update`: то же → не внешневалютный).

**Вернуть:** файлы — на место, вызовы и условия — по списку выше (генераторы — по git).
