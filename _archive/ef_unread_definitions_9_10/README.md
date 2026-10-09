# Определения E&F без ссылок (ночь 9.10)

**Что это.** По `ld_index.py` (определения без ссылок) и проверке по всем живым файлам, включая GUI и локализацию:
определения, на которые нет ни одной ссылки (только комментарии). Взяты только определения E&F; `inflation_on_*` не
трогались (их переопределяет компач E&F + Morgenröte мегапака, `tools/regen_ef_tr_copies.py`), учётные `zz_ef_v_f_*` —
тоже.

**Вырезано (текст — по тем же путям):**
- `common/script_values/00_economic_scripted_value.txt` — `import_export_disable`;
- `common/script_values/00_financial_scripted_value.txt` — `prosperity_target`, `prosperity_increase`,
  `building_ef_private_construction_lvl_state`, `economic_sentiment_index_malus_factor`, `country_in_crisis`;
- `common/scripted_guis/00_economic_scripted_guis.txt` — `purchase_of_bond_debt_visibility` (в GUI — только
  комментарий `#purchase_of_bond_debt_visibility`);
- `common/scripted_guis/09_ef_other.txt` — `trade_balance_0` (933 строки), `si_sort_by_country_indice`;
- `common/scripted_triggers/00_ef_custom_trigger.txt` — `law_currency_enacted`.

Ссылок в живых файлах не было (остались только закомментированные строки в `00_ef_buttons.txt`,
`00_ef_bank_central_je.txt`, `00_ef_financial_center_je.txt`, `00_financial_scripted_value.txt`, `09_ef_other.txt`).
Строки документов: `clearing-fx.md`, `currencies.md`, `interface.md`, `mechanisms.md`.

**Вернуть:** записи — в те же файлы.
