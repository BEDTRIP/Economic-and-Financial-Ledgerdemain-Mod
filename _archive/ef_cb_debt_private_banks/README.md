---
type: code
description: "Долг ЦБ перед частными банками (E&F): частные банки ссужали золото ЦБ страны; держатели — 25 списков central_bank_debt_privat_bank_buyer_list_N, суммы — значения…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_cb_debt_private_banks/**"]
---
# Долг ЦБ перед частными банками (E&F)

**Что делал (замысел E&F):** частные банки ссужали золото ЦБ страны; держатели — 25 списков
`central_bank_debt_privat_bank_buyer_list_N`, суммы — значения `ai_central_bank_debt_privat_bank_gold_loaned_N` (золото в
займе, по `owner.var:ai_privat_bank_bond_value_N`) и `ai_entral_bank_debt_privat_bank_interest_refund_per_year_N`
(проценты в год), N = 1–10.

**Почему мёртв:** списки никто не заполнял — их только очищали (`central_bank_debt_privat_bank_buyer_list_N_clear`,
кнопка очистки списков ЦБ); значения складывались в суммы E&F и всегда давали 0 (покупки облигаций частными банками E&F —
в `_archive/ef_ai_treasury_bonds/`, Д.R6.6). Найдено аудитом 16.10, снято в R9б.19.

**Вырезано** (по исходным путям этой папки):
- `common/script_values/00_financial_scripted_value.txt` — 20 значений `ai_central_bank_debt_privat_bank_gold_loaned_1..10`,
  `ai_entral_bank_debt_privat_bank_interest_refund_per_year_1..10`;
- `common/scripted_effects/08_list_effect.txt` — 25 эффектов `central_bank_debt_privat_bank_buyer_list_1..25_clear`;
- `common/scripted_effects/01_financial_scripted_effects.txt` — обёртка `central_bank_debt_privat_bank_buyer_list_clear`.

**Удалено из живых файлов:**
- `common/script_values/00_financial_scripted_value.txt`: строки `add = ai_central_bank_debt_privat_bank_gold_loaned_1..10`
  в `gold_loaned_to_central_bank` и `gold_loaned_to_central_bank_no_interest`, `add =
  ai_entral_bank_debt_privat_bank_interest_refund_per_year_1..10` в `central_bank_interest_refund_per_year` (30 строк);
- `common/scripted_guis/09_ef_other.txt`, scripted_gui `central_bank_debt_buyer_list_clear`, `effect`: строка
  `central_bank_debt_privat_bank_buyer_list_clear = yes` (кнопка осталась — очищает списки ЦБ; окно E&F — R10).

Закомментированный вызов `central_bank_debt_privat_bank_buyer_list_1_clear` в тестовом блоке
`00_on_action_main.txt` — остался комментарием E&F.

**Вернуть:** записи — на прежние места; строки `add` — в три суммы; строку эффекта — в кнопку.
