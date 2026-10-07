# Очистка списков покупателей / продавцов, в которые никто не пишет

**Что делали:** ничего. В шагах погашения облигаций (`bond_maturity_N`, `01_financial_scripted_effects.txt`) после
раздачи списки сбрасываются `clear_variable_list`; 15 из них никто никогда не заполняет (наполнявшие их кнопки
`seller_/buyer_country_general_XY_oclick` — в `ef_unused_scripted_guis/`). Движок писал «Variable '<список>' is used but
is never set» (error.log каждого запуска).

**Удалено из живых файлов** — `common/scripted_effects/01_financial_scripted_effects.txt`, строки до выноса:

| строка | текст |
| --- | --- |
| 18206 | `clear_variable_list = seller_country_1` |
| 18401 | `clear_variable_list = seller_country_3` |
| 18405 | `clear_variable_list = buyer_country_general_3` |
| 18597 | `clear_variable_list = seller_country_5` |
| 18698 | `clear_variable_list = buyer_country_general_6` |
| 18893 | `clear_variable_list = buyer_country_general_8` |
| 18991 | `clear_variable_list = buyer_country_general_9` |
| 19086 | `clear_variable_list = seller_country_10` |
| 19090 | `clear_variable_list = buyer_country_general_10` |
| 19446 | `clear_variable_list = ai_buyer_country_general_4` |
| 19529 | `clear_variable_list = ai_seller_country_5` |
| 19532 | `clear_variable_list = ai_buyer_country_general_5` |
| 19615 | `clear_variable_list = ai_seller_country_6` |
| 19702 | `clear_variable_list = ai_buyer_country_general_7` |
| 19869 | `clear_variable_list = ai_seller_country_9` |

Остальные списки тех же шагов (заполняются) не тронуты. **Вернуть:** строки на прежние места.
