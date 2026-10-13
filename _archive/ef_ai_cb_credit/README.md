# ИИ-кредит ЦБ казне E&F

**Что делал.** Раз в месяц (хаб E&F `00_on_action_main.txt`, ветка `is_ai` и `has_central_bank_SS_BS_GS_GES_NISO`) ИИ
занимал у своего ЦБ, когда казна ниже 10 % предела золотого резерва (в мир — до доли `zz_ef_cbl_target_share` предела,
в войну — до 15 % без предела), и гасил долг из казны, когда долг ЦБ выше разрешённого (`ai_refund_central_bank`);
часть сверх 25 % ЦБ прощал (`zz_ef_cb_writeoff`). Деньги — проводки казна ↔ счёт `credit_at_central_bank`.

**Почему в архиве.** Д.R5.10 (пользователь 13.10): казна занимает только долгом игры у банков страны (Д.R5.2,
`ld_gov_loan.txt`), ЦБ финансирует её покупкой облигаций (Д.R5.4). Прогон r1013_235244: Франция 18.12.1843 гасила долг
ЦБ на 0,99 млн сверх бюджета — скачок «прочего» казны.

**Удалено из живых файлов:**
- `common/scripted_effects/01_financial_scripted_effects.txt` — определения `ai_credit_at_central_bank`,
  `ai_refund_central_bank` (строки 650–782);
- `common/scripted_effects/00_on_action_main.txt`, строка 326 — блок `if = { limit = { is_ai = yes
  has_central_bank_SS_BS_GS_GES_NISO = yes } ai_credit_at_central_bank = yes ai_refund_central_bank = yes }`;
- `common/script_values/ld_money_model_values.txt` — `zz_ef_cbl_target_share`, `zz_ef_cbl_take_v`;
- `common/script_values/00_economic_scripted_value.txt` — `gold_reserve_compared_gold_reserves_limit`,
  `bond_producted_war`.

Кнопки игрока (`set_debt_issued`, `refund_credit_at_central_bank(_all)`) остались.
