# Переменные без читателя и читатели без писателя (E&F)

**Что это.** По `ld_smells.py vars` (В3, пользователь 8.10): переменные, которые пишутся, но нигде не читаются (ни
скрипт, ни окна, ни английская локализация), и строки, читающие то, что никто не пишет.

**Вырезано (записи переменных, по исходным путям):**
- `<cur>_quantity` (95) — `10_new_country_var.txt` (`new_country_var_ef_economy`; история зовёт его же);
- `ai_buyer_country_1..10` (`01_financial_scripted_effects.txt`), `buyer_country_1..10` (`00_financial_scripted_guis.txt`);
- `central_bank_debt_privat_bank_buyer_list_1..25_clear` (`08_list_effect.txt`; окно, которое их читало, — в
  `_archive/ef_bank_funds/`);
- `central_bank_interest_refund_per_year`, `central_bank_metal_reserves_state`, `gold_loaned_to_central_bank`,
  `purchase_cycle`, `extreme_weak_currency_solution_count_player`, `money_supply_predicted_add_{de,re}valuation_1_month_valided`
  (`10_new_country_var.txt`, `00_economic_scripted_guis.txt`, `01_economic_scripted_effects.txt`);
- `global_arbitrage_bank_variable_list_ordered` (`08_list_effect.txt`), `gui_market_currency_list` (`09_ef_other.txt`);
- список `import_export_value_in_currency` (история, `00_economic_scripted_guis.txt`) и с ним scripted GUI
  `update_import_export_value_in_currency_liste` целиком (после снятия записей — 95 пустых `if`) и глобальная
  `currency_import_export_value_gold_03` (история).
- сообщения `your_currency_are_buy_message`, `your_currency_are_sell_message` (`common/messages/00_ef_messages.txt`;
  не постятся нигде; их текст читал `stockpiling_*_quantity_var`, которого никто не пишет).

**Удалено из живых файлов:**
- `gui/ld_economy_panel.gui`, секция «import_export_value_in_currency_panel», `blockoverride "onclick"`: строка
  `onclick = "[GetScriptedGui('update_import_export_value_in_currency_liste').Execute( GuiScope.SetRoot(GetPlayer.MakeScope).End)]"`.
- Локализация (11 языков): `<good>_flag_red_arow_bellow` (29, `00_ef_gui_localization_l_*.yml`, читали
  `release_<good>_var_1` нацзапаса — его нет) и строка-комментарий с тем же; ключи сообщений
  `notification_your_currency_are_{buy,sell}_message*` (`01_ef_notification_localization_l_*.yml`).

**Оставлены:** `zz_ef_cb_kind` (прочтёт R4); `com_topbar_second_line`, `com_topbar_items` (общая верхняя панель
сообщества — читает чужой GUI); `national_production` (PSC); `japan_emperor_restored`, `japan_restoration_complete`
(переменные ванильного журнала Японии); `XXXX` — только в закомментированном GUI.

**Вернуть:** записи — на прежние места (в файлах архива — по порядку файлов); строки GUI и локализации — по списку.
