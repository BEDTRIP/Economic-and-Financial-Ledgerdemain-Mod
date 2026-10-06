# Мёртвое в GUI и журналах E&F

| что | откуда (файл) | почему мёртвое |
| --- | --- | --- |
| типы `vo_plotline_income_formwork`, `vo_plotline_income`, `vo_plotline_expenses_formwork`, `vo_plotline_expenses`, `vo_plotline_gdp_formwork`, `vo_plotline_gdp` (884 строки) | `gui/00_ef_deported_gui_2.gui:10984–11867` | `income`/`expenses` вызывались только из `*_formwork`, `formwork` и `gdp` — нигде (две закомментированные вставки `#vo_plotline_expenses = {` в том же файле остались). `vo_plotline_minting` живой |
| журнальные виджеты `widget_je_ef_fc_fso_situation`, `widget_je_ef_pcs_fso_situation` (618 строк) | `gui/scripted_widgets/00_ef_custom_widgets.gui:17–634` | в `common/journal_entries` не подключены (заменены `zz_pb_ef_fso_*_widget`); внутри — кнопки на несуществующие sgui `*_list_gerenation_ordered` |
| кнопки `bank_central_currency_JE_1..4_button` (пустые тела, 48 строк) | `common/scripted_buttons/00_ef_buttons.txt:2419–2466` | подключение в журнале закомментировано (`00_ef_bank_central_je.txt`) |
| прогресс-бары `bank_je_central_progress_bar`, `bank_central_currency_JE_dollar_united_states_dollar_progress_bar` | `common/scripted_progress_bars/00_ef_progressbar.txt` | вызовы закомментированы; локализации ключей нет |
| игровые понятия `concept_automatic_money_value`, `concept_financial_product` | `common/game_concepts/00_ef_game_concepts.txt` | `refs=0`, локализации нет |

**Переменные:** виджеты читали GUI-флаги `fc_fso_situation`/`pcs_fso_situation` (`GetVariableSystem`). **Удалено из живых файлов:** только перечисленные блоки; вызовов вне их нет.
**Вернуть:** вставить блоки по строкам из заголовков архивных файлов; журналы подключить `scripted_button =` / `scripted_progress_bar =` / `widget = { … }`.
