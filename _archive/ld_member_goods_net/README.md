# Торговый счёт члена таможенного союза по товарам штатов

**Что делало:** член таможенного союза со своим ЦБ (`zz_ef_cu_member`) считал свою торговлю за неделю как производство
своих штатов сверх потребления по 53 товарам по ценам рынка (`zz_ef_member_goods_net`, 53 × штаты); владелец рынка
вычитал сумму счетов членов (`zz_ef_members_trade_sum`, перебор всех стран каждую неделю). Подданные и страны без ЦБ в
чужом рынке торговли не имели.

**Чем заменено:** доли стран в производстве и потреблении рынка раз в месяц (Д.R8в.1, `ld_market_shares.txt`), торговля
каждой страны рынка — `zz_ef_trade_net_week`.

**Удалено из живых файлов:**
- `common/script_values/ld_customs_union_values.txt` — файл целиком (здесь), генератор `regen_ef_customs_union.py` их
  больше не выдаёт (функции `goods()`, `values()`, чтение ванильных товаров);
- `common/scripted_effects/ld_money_model.txt`, `zz_ef_trade_step`: блок
  `if = { limit = { zz_ef_cu_member = yes } set_variable = { name = zz_ef_member_trade value = var:zz_ef_f_trade } } else_if = { limit = { has_variable = zz_ef_member_trade } remove_variable = zz_ef_member_trade }`;
- `common/script_values/ld_money_model_values.txt`, `zz_ef_trade_net_week`: `subtract = zz_ef_members_trade_sum` у
  владельца и ветка `else_if = { limit = { zz_ef_cu_member = yes } value = zz_ef_member_goods_net }`;
- лог `EFX` (`ld_money_model.txt`, месячный шаг): поле
  `|mtrade [THIS.GetCountry.MakeScope.ScriptValue('zz_ef_members_trade_sum')|0]`.
