# Таблица валют

Сгенерирована `../vic3_mods/tools/regen_ld_currency_data.py` из законов, истории и локализации форка — руками не
править. Переменная валюты страны — `var:zz_ef_cur` (`flag:<ключ>`), `docs/currencies.md`. Паритет — металл на
национальную единицу из истории E&F на 1.1.1836 (курс между валютами и подписи; в деньгах движка не участвует, Д.1).
Название в игре — «<прилагательное страны> <слово>» (эмитент — сама страна; `currency_name`); столбцы «название» —
названия E&F по ключу (окна E&F).

| ключ | слово в игре | название E&F | по-русски E&F | символ | ISO | страны 1836: стандарт, паритет |
| --- | --- | --- | --- | --- | --- | --- |
| `dinar` | динар / dinar | Dinar | Динар | `dinar_texture` | — | — |
| `dinar_algerian_dinar` | динар / dinar | Algerian Dinar | Алжирский динар | `dinar_algerian_dinar_texture` | DZD | — |
| `dinar_iraqi_dinar` | динар / dinar | Iraqi Dinar | Иракский динар | `dinar_iraqi_dinar_texture` | IQD | — |
| `dinar_libyan_dinar` | динар / dinar | Libyan Dinar | Ливийский динар | `dinar_libyan_dinar_texture` | LYD | — |
| `dinar_moroccan_dirham` | дирхам / dirham | Moroccan Dirham | Марокканский дирхам | `dinar_moroccan_dirham_texture` | MAD | — |
| `dinar_omanian_rial` | риал / riyal | Omanian Rial | Оманский риал | `dinar_omanian_rial_texture` | OMR | — |
| `dinar_qiran` | киран / qiran | Qiran | Киран | `dinar_qiran_texture` | IRR | — |
| `dinar_saudi_riyal` | риал / riyal | Saudi Riyal | Саудовский риял | `dinar_saudi_riyal_texture` | SAR | — |
| `dinar_serbian_dinar` | динар / dinar | Serbian Dinar | Сербский динар | `dinar_serbian_dinar_texture` | RSD | — |
| `dinar_tunisian_dinar` | динар / dinar | Tunisian Dinar | Тунисский динар | `dinar_tunisian_dinar_texture` | TND | — |
| `dinar_yugoslav_dinar` | динар / dinar | Yugoslav Dinar | Югославский динар | `dinar_yugoslav_dinar_texture` | YUD | — |
| `dollar_australian_dollar` | доллар / dollar | Australian Dollar | Австралийский доллар | `dollar_australian_dollar_texture` | AUD | — |
| `dollar_canadian_dollar` | доллар / dollar | Canadian Dollar | Канадский доллар | `dollar_canadian_dollar_texture` | CAD | — |
| `dollar_caribbean_dollar` | доллар / dollar | Caribbean Dollar | Карибский доллар | `dollar_caribbean_dollar_texture` | — | — |
| `dollar_confederate_states_dollar` | доллар / dollar | Confederate States Dollar | Доллар Конфедеративных Штатов | `dollar_confederate_states_dollar_texture` | — | — |
| `dollar_liberian_dollar` | доллар / dollar | Liberian Dollar | Либерийский доллар | `dollar_liberian_dollar_texture` | LRD | — |
| `dollar_new_zealand_dollar` | доллар / dollar | New Zealand Dollar | Новозеландский доллар | `dollar_new_zealand_dollar_texture` | NZD | — |
| `dollar_sierra_leonean_dollar` | доллар / dollar | Sierra Leonean Dollar | Доллар Сьерра-Леоне | `dollar_sierra_leonean_dollar_texture` | SLL | — |
| `dollar_united_states_dollar` | доллар / dollar | United States Dollar | Доллар США | `dollar_united_states_dollar_texture` | USD | USA: bimetallism, 5 |
| `eco_ariary` | ариари / ariary | Ariary | Ариари | `eco_ariary_texture` | MGA | — |
| `eco_central_african_eco` | эко / eco | Central African Eco | Центральноафриканский эко | `eco_central_african_eco_texture` | XAF | — |
| `eco_east_african_eco` | эко / eco | East African Eco | Восточноафриканский эко | `eco_east_african_eco_texture` | — | — |
| `eco_ethiopian_birr` | быр / birr | Ethiopian Birr | Эфиопский быр | `eco_ethiopian_birr_texture` | ETB | — |
| `eco_ghanaian_pound` | фунт / pound | Ghanaian Pound | Ганский фунт | `eco_ghanaian_pound_texture` | GHS | — |
| `eco_nigerian_naira` | найра / naira | Nigerian Naira | Нигерийская найра | `eco_nigerian_naira_texture` | NGN | — |
| `eco_south_african_rand` | ранд / rand | South African Rand | Южноафриканский ранд | `eco_south_african_rand_texture` | ZAR | — |
| `eco_tuareg_ouguiya` | угия / ouguiya | Tuareg Ouguiya | Туарегская угия | `eco_tuareg_ouguiya_texture` | — | — |
| `eco_west_african_eco` | эко / eco | West African Eco | Западноафриканский эко | `eco_west_african_eco_texture` | XOF | — |
| `franc_belgian_franc` | франк / franc | Belgian Franc | Бельгийский франк | `franc_belgian_franc_texture` | BEF | — |
| `franc_french_franc` | франк / franc | French Franc | Французский франк | `franc_french_franc_texture` | FRF | FRA: bimetallism, 0.75 |
| `franc_luxembourgish_franc` | франк / franc | Luxembourgish Franc | Люксембургский франк | `franc_luxembourgish_franc_texture` | LUF | — |
| `franc_swiss_franc` | франк / franc | Swiss Franc | Швейцарский франк | `franc_swiss_franc_texture` | CHF | — |
| `gulden` | гульден / gulden | Gulden | Гульден | `gulden_texture` | — | AUS: silver, 13.32 |
| `gulden_bavarian_gulden` | гульден / gulden | Bavarian Gulden | Баварский гульден | `gulden_bavarian_gulden_texture` | — | — |
| `gulden_florin` | флорин / florin | Florin | Флорин | `gulden_florin_texture` | NLG | NET: bimetallism, 10.61 |
| `gulden_hungarian_forint` | форинт / forint | Hungarian Forint | Венгерский форинт | `gulden_hungarian_forint_texture` | HUF | — |
| `gulden_indies_guilder` | гульден / guilder | Indies Guilder | Ост-индский гульден | `gulden_indies_guilder_texture` | — | — |
| `gulden_south_german_gulden` | гульден / gulden | South German Gulden | Южногерманский гульден | `gulden_south_german_gulden_texture` | — | — |
| `krone_czech_koruna` | крона / koruna | Czech Koruna | Чешская крона | `krone_czech_koruna_texture` | CSK | — |
| `krone_danish_krone` | крона / krone | Danish Krone | Датская крона | `krone_danish_krone_texture` | DKK | — |
| `krone_estonian_kroon` | крона / kroon | Estonian Kroon | Эстонская крона | `krone_estonian_kroon_texture` | EEK | — |
| `krone_icelandic_krona` | крона / krona | Icelandic Krona | Исландская крона | `krone_icelandic_krona_texture` | ISK | — |
| `krone_norwegian_krone` | крона / krone | Norwegian Krone | Норвежская крона | `krone_norwegian_krone_texture` | NOK | — |
| `krone_slovak_koruna` | крона / koruna | Slovak Koruna | Словацкая крона | `krone_slovak_koruna_texture` | SKK | — |
| `krone_swedish_krona` | крона / krona | Swedish Krona | Шведская крона | `krone_swedish_krona_texture` | SEK | — |
| `leon_leu` | лей / leu | Leu | Лей | `leon_leu_texture` | ROL | — |
| `leon_lev` | лев / lev | Lev | Лев | `leon_lev_texture` | BGL | — |
| `lira` | лира / lira | Lira | Лира | `lira_texture` | ITL | — |
| `lira_ducato` | дукат / ducat | Ducato | Дукат | `lira_ducato_texture` | — | — |
| `lira_ottoman_lira` | лира / lira | Ottoman Lira | Османская лира | `lira_ottoman_lira_texture` | TRL | — |
| `lira_scudo_pontificio` | скудо / scudo | Scudo Pontificio | Папский скудо | `lira_scudo_pontificio_texture` | — | — |
| `lira_scudo_sardo` | скудо / scudo | Scudo Sardo | Сардинский скудо | `lira_scudo_sardo_texture` | — | — |
| `lira_toscane_lira` | лира / lira | Toscane Lira | Тосканская лира | `lira_toscane_lira_texture` | — | — |
| `mark` | марка / mark | Mark | Марка | `mark_texture` | — | — |
| `mark_finnish_markka` | марка / markka | Finnish Markka | Финская марка | `mark_finnish_markka_texture` | — | — |
| `peso` | песо / peso | Peso | Песо | `peso_texture` | — | — |
| `peso_argentine_peso` | песо / peso | Argentine Peso | Аргентинское песо | `peso_argentine_peso_texture` | ARS | — |
| `peso_bolivien_peso` | песо / peso | Peso Bolivien | Боливийское песо | `peso_bolivien_peso_texture` | — | — |
| `peso_chilean_peso` | песо / peso | Chilean Peso | Чилийское песо | `peso_chilean_peso_texture` | CLP | — |
| `peso_colombian_peso` | песо / peso | Colombian Peso | Колумбийское песо | `peso_colombian_peso_texture` | COP | — |
| `peso_costa_rican_colon` | колон / colon | Costa Rican Colon | Костариканский колон | `peso_costa_rican_colon_texture` | — | — |
| `peso_cuban_peso` | песо / peso | Cuban Peso | Кубинское песо | `peso_cuban_peso_texture` | — | — |
| `peso_ecuadorian_peso` | песо / peso | Ecuadorian Peso | Эквадорское песо | `peso_ecuadorian_peso_texture` | — | — |
| `peso_el_salvador_colon` | колон / colon | El Salvador Colon | Сальвадорский колон | `peso_el_salvador_colon_texture` | — | — |
| `peso_guatemalan_quetzal` | кетсаль / quetzal | Guatemalan Quetzal | Гватемальский кетсаль | `peso_guatemalan_quetzal_texture` | GTQ | — |
| `peso_honduran_lempira` | лемпира / lempira | Honduran Lempira | Гондурасская лемпира | `peso_honduran_lempira_texture` | — | — |
| `peso_mexican_peso` | песо / peso | Mexican Peso | Мексиканское песо | `peso_mexican_peso_texture` | MXN | — |
| `peso_nicaraguan_cordoba` | кордоба / cordoba | Nicaraguan Cordoba | Никарагуанская кордоба | `peso_nicaraguan_cordoba_texture` | — | — |
| `peso_paraguayan_peso` | песо / peso | Paraguayan Peso | Парагвайское песо | `peso_paraguayan_peso_texture` | — | — |
| `peso_philippine_peso` | песо / peso | Philippine Peso | Филиппинское песо | `peso_philippine_peso_texture` | PHP | — |
| `peso_sol_de_oro` | соль / sol | Sol de Oro | Соль де Оро | `peso_sol_de_oro_texture` | — | — |
| `peso_uruguayan_peso` | песо / peso | Uruguayan Peso | Уругвайское песо | `peso_uruguayan_peso_texture` | — | — |
| `peso_venezuelan_peso` | песо / peso | Venezuelan Peso | Венесуэльское песо | `peso_venezuelan_peso_texture` | VEB | — |
| `pound_egyptian_pound` | фунт / pound | Egyptian Pound | Египетский фунт | `pound_egyptian_pound_texture` | EGP | — |
| `pound_irish_pound` | фунт / pound | Irish Pound | Ирландский фунт | `pound_irish_pound_texture` | — | — |
| `pound_sterling` | фунт / pound | Pound Sterling | Фунт стерлингов | `pound_sterling_texture` | GBP | GBR: gold, 7.32 |
| `real` | реал / real | Real | Реал | `real_texture` | — | — |
| `real_brazilian_real` | реал / real | Brazilian Real | Бразильский реал | `real_brazilian_real_texture` | BRL | — |
| `rupee_indian_rupee` | рупия / rupee | Indian Rupee | Индийская рупия | `rupee_indian_rupee_texture` | INR | — |
| `rupee_indonesian_rupiah` | рупия / rupiah | Indonesian Rupiah | Индонезийская рупия | `rupee_indonesian_rupiah_texture` | — | — |
| `spe_baht` | бат / baht | Baht | Бат | `spe_baht_texture` | THB | — |
| `spe_dong` | донг / dong | Dong | Донг | `spe_dong_texture` | — | — |
| `spe_drachma` | драхма / drachma | Drachma | Драхма | `spe_drachma_texture` | — | — |
| `spe_korean_won` | вона / won | Korean Won | Корейская вона | `spe_korean_won_texture` | KRW | — |
| `spe_latvian_lats` | лат / lats | Latvian Lats | Латвийский лат | `spe_latvian_lats_texture` | — | — |
| `spe_lithuanian_litas` | лит / litas | Lithuanian Litas | Литовский лит | `spe_lithuanian_litas_texture` | LTL | — |
| `spe_peseta` | песета / peseta | Peseta | Песета | `spe_peseta_texture` | ESP | — |
| `spe_ruble` | рубль / ruble | Ruble | Рубль | `spe_ruble_texture` | RUB | RUS: silver, 18 |
| `spe_uni` | национальное | Uni | Уни | `spe_uni_texture` | — | — |
| `spe_yen` | иена / yen | Yen | Иена | `spe_yen_texture` | JPY | — |
| `spe_yuan` | юань / yuan | Yuan | Юань | `spe_yuan_texture` | CNY | CHI: silver, 37.5 |
| `spe_zloti` | злотый / zloty | Zloti | Злотый | `spe_zloti_texture` | PLZ | — |
| `thaler_hannoveraner_thaler` | талер / thaler | Hannoveraner Thaler | Ганноверский талер | `thaler_hannoveraner_thaler_texture` | — | — |
| `thaler_prussian_thaler` | талер / thaler | Prussian Thaler | Прусский талер | `thaler_prussian_thaler_texture` | — | PRU: silver, 16.7 |
| `thaler_saxon_thaler` | талер / thaler | Saxon Thaler | Саксонский талер | `thaler_saxon_thaler_texture` | — | — |
