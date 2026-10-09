# Таблица валют

Сгенерирована `../vic3_mods/tools/regen_ld_currency_data.py` из законов, истории и локализации форка — руками не
править. Переменная валюты страны — `var:zz_ef_cur` (`flag:<ключ>`), `docs/currencies.md`. Паритет — металл на
национальную единицу из истории E&F на 1.1.1836 (курс между валютами и подписи; в деньгах движка не участвует, Д.1).
Название в игре — «<прилагательное страны> <слово>» (эмитент — сама страна; `currency_name`); столбцы «название» —
названия E&F по ключу (окна E&F).
Символ в игре — «<две буквы страны> <знак>» (`currency_symbol`, `tools/regen_ld_currency_symbol.py`).

| ключ | слово в игре | название E&F | по-русски E&F | знак | ISO | страны 1836: стандарт, паритет |
| --- | --- | --- | --- | --- | --- | --- |
| `dinar` | динар / dinar | Dinar | Динар | D | — | — |
| `dinar_algerian_dinar` | динар / dinar | Algerian Dinar | Алжирский динар | D | DZD | — |
| `dinar_iraqi_dinar` | динар / dinar | Iraqi Dinar | Иракский динар | D | IQD | — |
| `dinar_libyan_dinar` | динар / dinar | Libyan Dinar | Ливийский динар | D | LYD | — |
| `dinar_moroccan_dirham` | дирхам / dirham | Moroccan Dirham | Марокканский дирхам | D | MAD | — |
| `dinar_omanian_rial` | риал / riyal | Omanian Rial | Оманский риал | R | OMR | — |
| `dinar_qiran` | киран / qiran | Qiran | Киран | Q | IRR | — |
| `dinar_saudi_riyal` | риал / riyal | Saudi Riyal | Саудовский риял | R | SAR | — |
| `dinar_serbian_dinar` | динар / dinar | Serbian Dinar | Сербский динар | D | RSD | — |
| `dinar_tunisian_dinar` | динар / dinar | Tunisian Dinar | Тунисский динар | D | TND | — |
| `dinar_yugoslav_dinar` | динар / dinar | Yugoslav Dinar | Югославский динар | D | YUD | — |
| `dollar_australian_dollar` | доллар / dollar | Australian Dollar | Австралийский доллар | $ | AUD | — |
| `dollar_canadian_dollar` | доллар / dollar | Canadian Dollar | Канадский доллар | $ | CAD | — |
| `dollar_caribbean_dollar` | доллар / dollar | Caribbean Dollar | Карибский доллар | $ | — | — |
| `dollar_confederate_states_dollar` | доллар / dollar | Confederate States Dollar | Доллар Конфедеративных Штатов | $ | — | — |
| `dollar_liberian_dollar` | доллар / dollar | Liberian Dollar | Либерийский доллар | $ | LRD | — |
| `dollar_new_zealand_dollar` | доллар / dollar | New Zealand Dollar | Новозеландский доллар | $ | NZD | — |
| `dollar_sierra_leonean_dollar` | доллар / dollar | Sierra Leonean Dollar | Доллар Сьерра-Леоне | $ | SLL | — |
| `dollar_united_states_dollar` | доллар / dollar | United States Dollar | Доллар США | $ | USD | USA: bimetallism, 5 |
| `eco_ariary` | ариари / ariary | Ariary | Ариари | Ar | MGA | — |
| `eco_central_african_eco` | эко / eco | Central African Eco | Центральноафриканский эко | E | XAF | — |
| `eco_east_african_eco` | эко / eco | East African Eco | Восточноафриканский эко | E | — | — |
| `eco_ethiopian_birr` | быр / birr | Ethiopian Birr | Эфиопский быр | Br | ETB | — |
| `eco_ghanaian_pound` | фунт / pound | Ghanaian Pound | Ганский фунт | £ | GHS | — |
| `eco_nigerian_naira` | найра / naira | Nigerian Naira | Нигерийская найра | ₦ | NGN | — |
| `eco_south_african_rand` | ранд / rand | South African Rand | Южноафриканский ранд | R | ZAR | — |
| `eco_tuareg_ouguiya` | угия / ouguiya | Tuareg Ouguiya | Туарегская угия | O | — | — |
| `eco_west_african_eco` | эко / eco | West African Eco | Западноафриканский эко | E | XOF | — |
| `franc_belgian_franc` | франк / franc | Belgian Franc | Бельгийский франк | ₣ | BEF | — |
| `franc_french_franc` | франк / franc | French Franc | Французский франк | ₣ | FRF | FRA: bimetallism, 0.75 |
| `franc_luxembourgish_franc` | франк / franc | Luxembourgish Franc | Люксембургский франк | ₣ | LUF | — |
| `franc_swiss_franc` | франк / franc | Swiss Franc | Швейцарский франк | ₣ | CHF | — |
| `gulden` | гульден / gulden | Gulden | Гульден | ƒ | — | AUS: silver, 13.32 |
| `gulden_bavarian_gulden` | гульден / gulden | Bavarian Gulden | Баварский гульден | ƒ | — | — |
| `gulden_florin` | флорин / florin | Florin | Флорин | ƒ | NLG | NET: bimetallism, 10.61 |
| `gulden_hungarian_forint` | форинт / forint | Hungarian Forint | Венгерский форинт | Ft | HUF | — |
| `gulden_indies_guilder` | гульден / guilder | Indies Guilder | Ост-индский гульден | ƒ | — | — |
| `gulden_south_german_gulden` | гульден / gulden | South German Gulden | Южногерманский гульден | ƒ | — | — |
| `krone_czech_koruna` | крона / koruna | Czech Koruna | Чешская крона | Kč | CSK | — |
| `krone_danish_krone` | крона / krone | Danish Krone | Датская крона | kr | DKK | — |
| `krone_estonian_kroon` | крона / kroon | Estonian Kroon | Эстонская крона | kr | EEK | — |
| `krone_icelandic_krona` | крона / krona | Icelandic Krona | Исландская крона | kr | ISK | — |
| `krone_norwegian_krone` | крона / krone | Norwegian Krone | Норвежская крона | kr | NOK | — |
| `krone_slovak_koruna` | крона / koruna | Slovak Koruna | Словацкая крона | Kč | SKK | — |
| `krone_swedish_krona` | крона / krona | Swedish Krona | Шведская крона | kr | SEK | — |
| `leon_leu` | лей / leu | Leu | Лей | L | ROL | — |
| `leon_lev` | лев / lev | Lev | Лев | лв | BGL | — |
| `lira` | лира / lira | Lira | Лира | ₤ | ITL | — |
| `lira_ducato` | дукат / ducat | Ducato | Дукат | D | — | — |
| `lira_ottoman_lira` | лира / lira | Ottoman Lira | Османская лира | ₺ | TRL | — |
| `lira_scudo_pontificio` | скудо / scudo | Scudo Pontificio | Папский скудо | S | — | — |
| `lira_scudo_sardo` | скудо / scudo | Scudo Sardo | Сардинский скудо | S | — | — |
| `lira_toscane_lira` | лира / lira | Toscane Lira | Тосканская лира | ₤ | — | — |
| `mark` | марка / mark | Mark | Марка | ℳ | — | — |
| `mark_finnish_markka` | марка / markka | Finnish Markka | Финская марка | mk | — | — |
| `peso` | песо / peso | Peso | Песо | $ | — | — |
| `peso_argentine_peso` | песо / peso | Argentine Peso | Аргентинское песо | $ | ARS | — |
| `peso_bolivien_peso` | песо / peso | Peso Bolivien | Боливийское песо | $ | — | — |
| `peso_chilean_peso` | песо / peso | Chilean Peso | Чилийское песо | $ | CLP | — |
| `peso_colombian_peso` | песо / peso | Colombian Peso | Колумбийское песо | $ | COP | — |
| `peso_costa_rican_colon` | колон / colon | Costa Rican Colon | Костариканский колон | ₡ | — | — |
| `peso_cuban_peso` | песо / peso | Cuban Peso | Кубинское песо | $ | — | — |
| `peso_ecuadorian_peso` | песо / peso | Ecuadorian Peso | Эквадорское песо | $ | — | — |
| `peso_el_salvador_colon` | колон / colon | El Salvador Colon | Сальвадорский колон | ₡ | — | — |
| `peso_guatemalan_quetzal` | кетсаль / quetzal | Guatemalan Quetzal | Гватемальский кетсаль | Q | GTQ | — |
| `peso_honduran_lempira` | лемпира / lempira | Honduran Lempira | Гондурасская лемпира | L | — | — |
| `peso_mexican_peso` | песо / peso | Mexican Peso | Мексиканское песо | $ | MXN | — |
| `peso_nicaraguan_cordoba` | кордоба / cordoba | Nicaraguan Cordoba | Никарагуанская кордоба | C$ | — | — |
| `peso_paraguayan_peso` | песо / peso | Paraguayan Peso | Парагвайское песо | $ | — | — |
| `peso_philippine_peso` | песо / peso | Philippine Peso | Филиппинское песо | ₱ | PHP | — |
| `peso_sol_de_oro` | соль / sol | Sol de Oro | Соль де Оро | S/ | — | — |
| `peso_uruguayan_peso` | песо / peso | Uruguayan Peso | Уругвайское песо | $ | — | — |
| `peso_venezuelan_peso` | песо / peso | Venezuelan Peso | Венесуэльское песо | $ | VEB | — |
| `pound_egyptian_pound` | фунт / pound | Egyptian Pound | Египетский фунт | £ | EGP | — |
| `pound_irish_pound` | фунт / pound | Irish Pound | Ирландский фунт | £ | — | — |
| `pound_sterling` | фунт / pound | Pound Sterling | Фунт стерлингов | £ | GBP | GBR: gold, 7.32 |
| `real` | реал / real | Real | Реал | R$ | — | — |
| `real_brazilian_real` | реал / real | Brazilian Real | Бразильский реал | R$ | BRL | — |
| `rupee_indian_rupee` | рупия / rupee | Indian Rupee | Индийская рупия | ₹ | INR | — |
| `rupee_indonesian_rupiah` | рупия / rupiah | Indonesian Rupiah | Индонезийская рупия | Rp | — | — |
| `spe_baht` | бат / baht | Baht | Бат | ฿ | THB | — |
| `spe_dong` | донг / dong | Dong | Донг | ₫ | — | — |
| `spe_drachma` | драхма / drachma | Drachma | Драхма | ₯ | — | — |
| `spe_korean_won` | вона / won | Korean Won | Корейская вона | ₩ | KRW | — |
| `spe_latvian_lats` | лат / lats | Latvian Lats | Латвийский лат | Ls | — | — |
| `spe_lithuanian_litas` | лит / litas | Lithuanian Litas | Литовский лит | Lt | LTL | — |
| `spe_peseta` | песета / peseta | Peseta | Песета | ₧ | ESP | — |
| `spe_ruble` | рубль / ruble | Ruble | Рубль | ₽ | RUB | RUS: silver, 18 |
| `spe_uni` | национальное | Uni | Уни | ¤ | — | — |
| `spe_yen` | иена / yen | Yen | Иена | ¥ | JPY | — |
| `spe_yuan` | юань / yuan | Yuan | Юань | ¥ | CNY | CHI: silver, 37.5 |
| `spe_zloti` | злотый / zloty | Zloti | Злотый | zł | PLZ | — |
| `thaler_hannoveraner_thaler` | талер / thaler | Hannoveraner Thaler | Ганноверский талер | T | — | — |
| `thaler_prussian_thaler` | талер / thaler | Prussian Thaler | Прусский талер | T | — | PRU: silver, 16.7 |
| `thaler_saxon_thaler` | талер / thaler | Saxon Thaler | Саксонский талер | T | — | — |
