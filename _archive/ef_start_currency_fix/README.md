# Правки законов валют на старте (`zz_ef_currency_fix.txt`, п. 1–3)

**Что делало:** глобальная история после `99_ef_history_global_variable.txt`: Вюртембергу — `activate_law =
law_type:law_gulden_south_german_gulden_currency` (опечатка E&F в имени закона); 12 странам (LIB, COS, ECU, ELS, GUA,
HON, NIC, PRG, URU, VNZ, DAI, HAI, NZL) — `activate_law = law_type:law_no_market_liquidity` (валюты, чьи товары сняты).

**Почему вынесено:** обе правки пустые. В `99_ef_history_global_variable.txt` имя закона Вюртемберга уже верное, а
законов валют этих 12 стран нет — без закона страна и так на первом законе группы, `law_no_market_liquidity`. Валюта
страны — только из закона (`var:zz_ef_cur`, Д.R8а.2, С17); стартовые данные — история E&F.

**Вырезано:** блоки п. 1–3 (здесь, `common/history/global/zz_ef_currency_fix.txt`).

**Удалено из живых файлов:** файл `common/history/global/zz_ef_currency_fix.txt` переименован в
`ld_start_currency_standards.txt`; в нём остался только блок технологии `currency_standards` странам с подушным налогом;
шапка файла (о порядке загрузки и о правках законов) переписана.

**Вернуть:** блоки — в `GLOBAL = { every_country = { … } }` файла `ld_start_currency_standards.txt` перед блоком
технологии.
