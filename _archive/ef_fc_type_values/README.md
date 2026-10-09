# Значения «есть ли у страны финцентр вида X» (`has_building_financial_centre_<x>`, `_custom_location`)

**Что делало:** по значению на каждый тип финцентра (есть ли в стране; есть ли в штате главной биржи) — читали
`building_financial_num`, расширение `zz_ef_fc_expand` и название `stock_exchange_name`.

**Почему вынуто (R8б, шаг 4):** проверки финцентра — по группе `bg_financial_centre` и по бирже страны
(`var:zz_ef_fc_state`, `var:zz_ef_fc_variant`); `building_financial_num` — счёт штатов с национальным финцентром,
`zz_ef_fc_expand` и `stock_exchange_name` — генерат `tools/regen_ld_financial_centres.py`.

**Удалено из живых файлов:** читатели переписаны (см. выше); вызовов не осталось.
