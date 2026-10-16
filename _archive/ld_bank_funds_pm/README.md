# Метод «Банка» «Паи фондов» (R8б.6, Д.R8б.16, Д.R8б.24)

**Что делал:** группа методов `pmg_zz_ef_bank_funds` здания «Банк» (`building_zz_ef_bank`): `pm_zz_ef_bank_funds` — вход
паёв `mutual_funds` 0,04 на единицу рабочей силы; `pm_zz_ef_bank_no_funds` — по умолчанию. Раз в месяц
`zz_ef_fund_bank_pm_step` (`ld_investment_fund.txt`, вызов в месячном шаге `ld_money_model.txt`) включал метод паёв
всем «Банкам» страны, где рынок продаёт паи (`var:zz_ef_bank_funds_on`), и выключал, где нет. Недельный
`zz_ef_fund_shares_step` делил купленное страной: банкам — `zz_ef_fund_bank_week` (уровни «Банков» × 1000 работников ×
0,04 × цена пая), остальное — населению; банковская часть — вложение банков (`zz_ef_bank_inv_add`), требование `bk` на
фонд, вклад фонда.

**Почему снят (Д.R9б.13, пользователь 16.10):** паи производят здания фонда; банку товар паёв не нужен — паи как вложение
банки покупают на бирже (`zz_ef_rq_bk_f`). Метод к тому же копился у «Банков» (`activate_production_method` на всей
стране без проверки здания — копии в сейве, R9б.17).

**Вырезано** (по исходным путям): `production_methods/ld_bank_pm.txt` — два метода; `production_method_groups/ld_bank_pmg.txt`
— группа; `scripted_effects/ld_investment_fund.txt` — `zz_ef_fund_bank_pm_step`; `script_values/ld_investment_fund_values.txt`
— `zz_ef_fund_bank_week`, `zz_ef_bank_fund_shares_per_unit`, `zz_ef_bank_workforce_per_level`; `localization/{english,russian}` —
ключи `pmg_zz_ef_bank_funds`, `pm_zz_ef_bank_no_funds`, `pm_zz_ef_bank_funds`, `pm_zz_ef_bank_funds_desc`.

**Удалено из живых файлов:**
- `common/buildings/ld_bank.txt`: строка `pmg_zz_ef_bank_funds` в `production_method_groups`;
- `common/scripted_effects/ld_money_model.txt`: вызов `zz_ef_fund_bank_pm_step = yes` (с комментарием) в месячном шаге;
  поля `fd_bk` в строках лога `EFJ|bank_cap` (`Var('zz_ef_f_fd_bk')`) и `EFR` (`ScriptValue('zz_ef_v_f_fd_bk')`);
- `common/script_values/ld_investment_fund_values.txt`: значение `zz_ef_v_f_fd_bk`;
- `common/scripted_effects/ld_investment_fund.txt`, `zz_ef_fund_shares_step`: банковская часть — `zz_ef_f_fd_bk`
  (начальный 0, `= zz_ef_fund_bank_week`, вычет из части населения, место в пуле для фонда за границей, `zz_ef_bank_inv_add`,
  `zz_ef_rq_add = { H = bk K = f … }`, `zz_ef_fd_dep_add` банковской части);
- локализация 11 языков (`ld_cm_goods_l_*.yml`): четыре ключа выше.

Сейвы: группы у здания больше нет — движок её отбрасывает при загрузке.

**Вернуть:** записи — на прежние места; строки — по списку; банковскую часть шага — по git (`zz_ef_fund_shares_step`
до R9б.13).
