# Витрина — список имён, которые читают окна

Окна читают значения модели только через витрину ([[Витрина]]; Д.R0.8.10, Д.R3б.3): всё, что они берут функциями
данных (`ScriptValue` / `Var` / `GetVariable` с `zz_ef_*`), перечислено ниже. Классы: `var` — переменная страны; `vit` —
значение, которое только читает переменную (дёшево); `calc` — значение, считаемое при каждой перерисовке окна
(переносится за переменную шага в R10; новые числа для окон — переменная шага + `zz_ef_v_*`). Торговля недели в «Бюджет
→ Экономика» читает `zz_ef_v_f_imp` / `zz_ef_v_f_exp` (шаг), а не суммы по 53 товарам. Значение `zz_ef_bank_capital`
окон — остаток пула (пул + кредиты + облигации − вклады − кредит ЦБ − вклады чужих ЦБ), т. е. капитал банков учёта
(`var:zz_ef_bank_capital`, `money-model.md`) + «прочее». Окна и файлы — `interface.md`.

<!-- vitrine -->
Сгенерировано `tools/ld_vitrine.py --write`. Имён 288: переменных 31, значений-витрины 95, вычисляемых при перерисовке 162; файлов 18.

| имя | класс | где читается |
| --- | --- | --- |
| `zz_ef_abr_fx_all_v` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_abroad_net` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg0_pct_5y` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg0_pct_month` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg0_pct_year` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg1_pct_5y` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg1_pct_month` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg1_pct_year` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg2_pct_5y` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg2_pct_month` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg2_pct_year` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg3_pct_5y` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg3_pct_month` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg3_pct_year` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg_m0` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg_m0_to_gdp` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg_m1` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg_m1_to_gdp` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg_m2` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg_m2_to_gdp` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_agg_m3` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bank_assets` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bank_bonds` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bank_capital` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bank_cash` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bank_cb_debt` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bank_liabilities` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bank_loans` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bankm_money` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bc_debt` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bc_debt_to_gdp` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bimet_ratio` | var | `localization/english/ld_bimet_ratio_l_english.yml` |
| `zz_ef_bk_cap` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_bk_co` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_bk_deposits_v` | calc | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_bk_inc_v` | vit | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_bk_kind` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_bk_loans_v` | calc | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_bk_lv` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_bk_mg` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_bk_ms` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_bk_rate` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_bk_sh` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_bop_div_in` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_div_out` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_exp` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_fin_in` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_fin_out` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_in_total` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_int_in` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_int_out` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_oth_in` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_oth_out` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_out_total` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_sec_in` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bop_sec_out` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_bt_b_amt` | var | `gui/ld_cb_rate_panel.gui`, `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bt_b_year` | var | `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bt_t_amt` | var | `gui/ld_cb_rate_panel.gui`, `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bt_t_rate` | calc | `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bt_t_week` | var | `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bto_b_amt` | var | `gui/ld_cb_rate_panel.gui`, `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bto_b_year` | var | `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bto_t_amt` | var | `gui/ld_cb_rate_panel.gui`, `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bto_t_rate` | calc | `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bto_t_week` | var | `localization/english/ld_bond_tables_l_english.yml` |
| `zz_ef_bubble_step_eff` | calc | `localization/english/ld_pb_overbuild_l_english.yml` |
| `zz_ef_cb_cover` | calc | `localization/english/01_ef_tooltips_localization_l_english.yml`, `localization/english/ld_cb_rate_panel_l_english.yml`, `localization/english/ld_economy_panel_l_english.yml` и ещё 3 |
| `zz_ef_cb_credit_target` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_cb_loan_after_to_gdp` | calc | `localization/english/replace/ld_cb_loan_replace_l_english.yml` |
| `zz_ef_cb_loan_cap` | calc | `localization/english/replace/ld_cb_loan_replace_l_english.yml` |
| `zz_ef_cb_loan_now_to_gdp` | calc | `localization/english/replace/ld_cb_loan_replace_l_english.yml` |
| `zz_ef_cb_money` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_cb_rate_bias_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rate_months_to_step` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rate_next_step_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rate_note_value` | vit | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rate_rating_target` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rate_target` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rule_cover_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rule_gap_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rule_inflation_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rule_money_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rule_neutral_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_rule_risk_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_cb_valuation` | calc | `localization/english/01_ef_tooltips_localization_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_cbfx_dd` | var | `gui/ld_economy_panel.gui` |
| `zz_ef_cbfx_g` | var | `gui/ld_economy_panel.gui` |
| `zz_ef_cbfx_mn` | var | `gui/ld_economy_panel.gui` |
| `zz_ef_cbfx_u` | var | `gui/ld_economy_panel.gui` |
| `zz_ef_cc_debt` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_cc_rate` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_circ_business_cash` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_circ_growth_year` | calc | `localization/english/01_ef_tooltips_localization_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_clr_own_share` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_co_acc_sum_v` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_co_rest_v` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_co_share_v` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_comp_dep_v` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_consol_debt_v` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_credit_limit` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_credit_now` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_credit_to_gdp` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_credit_total` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_currency_strength` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_debt_principal` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_deposit_margin` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_deposit_rate` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_fc_bank_levels_min` | calc | `localization/english/01_ef_je_localization_l_english.yml` |
| `zz_ef_fd_dep_v` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_foreign_assets` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_fx_liab_all` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_fx_money` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_gdp_growth_year` | calc | `localization/english/01_ef_tooltips_localization_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_gdp_week` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_gov_rate_corr_pct` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_gov_rate_premium_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_gov_rate_target` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_holds_pc` | var | `gui/ld_economy_panel.gui` |
| `zz_ef_hook_calls` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_hook_ok` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_hook_probe_calls` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_inflation` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_m3_fd_bonds` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_m3_pp_bonds` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_mp_cum_v` | vit | `localization/english/ld_monetary_policy_l_english.yml` |
| `zz_ef_mp_dyn_pp` | calc | `localization/english/ld_monetary_policy_l_english.yml` |
| `zz_ef_mp_flow_v` | vit | `localization/english/ld_monetary_policy_l_english.yml` |
| `zz_ef_mp_months_left` | calc | `localization/english/ld_monetary_policy_l_english.yml` |
| `zz_ef_mp_pace_v` | calc | `localization/english/ld_monetary_policy_l_english.yml` |
| `zz_ef_mp_progress` | calc | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_mp_start_v` | vit | `localization/english/ld_monetary_policy_l_english.yml` |
| `zz_ef_mp_target_v` | vit | `localization/english/ld_monetary_policy_l_english.yml` |
| `zz_ef_mu_bloc_all_v` | calc | `localization/english/ld_monetary_union_l_english.yml` |
| `zz_ef_mu_bloc_half_v` | calc | `localization/english/ld_monetary_union_l_english.yml` |
| `zz_ef_mu_bloc_in_v` | calc | `localization/english/ld_monetary_union_l_english.yml` |
| `zz_ef_mu_latin_all_v` | calc | `localization/english/ld_monetary_union_l_english.yml` |
| `zz_ef_mu_latin_half_v` | calc | `localization/english/ld_monetary_union_l_english.yml` |
| `zz_ef_mu_latin_in_v` | calc | `localization/english/ld_monetary_union_l_english.yml` |
| `zz_ef_mu_scand_all_v` | calc | `localization/english/ld_monetary_union_l_english.yml` |
| `zz_ef_mu_scand_half_v` | calc | `localization/english/ld_monetary_union_l_english.yml` |
| `zz_ef_mu_scand_in_v` | calc | `localization/english/ld_monetary_union_l_english.yml` |
| `zz_ef_mv_ok_10_v` | calc | `gui/ld_economy_panel.gui` |
| `zz_ef_mv_ok_1_v` | calc | `gui/ld_economy_panel.gui` |
| `zz_ef_mv_ok_5_v` | calc | `gui/ld_economy_panel.gui` |
| `zz_ef_nr_dep_v` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_other_treasury_rest` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_pool` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_pool_months` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_pool_transfer_week` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_pop_cash` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_pop_cash_held` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_pop_deposits` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_pop_savings` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_popm_gold` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_popm_money` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_popm_silver` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_price_index` | calc | `localization/english/01_ef_tooltips_localization_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_fixed_income` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_gdp` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_military` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_minting_week` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_pool_gross` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_pool_net` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_total_expenses` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_raw_total_income` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_reserve_norm` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_risk_debt_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_risk_fx_pp` | calc | `localization/english/ld_cb_rate_panel_l_english.yml` |
| `zz_ef_sav_norm` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_savings_to_gdp` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_total_expenses_week` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_total_income_week` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_tr_to_cb` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_treasury` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_trm_buy_g_v` | vit | `localization/english/ld_treasury_metal_l_english.yml` |
| `zz_ef_trm_buy_s_v` | vit | `localization/english/ld_treasury_metal_l_english.yml` |
| `zz_ef_trm_fee` | calc | `localization/english/ld_treasury_metal_l_english.yml` |
| `zz_ef_trm_gold_goods_v` | calc | `localization/english/ld_treasury_metal_l_english.yml` |
| `zz_ef_trm_money_v` | calc | `localization/english/ld_treasury_metal_l_english.yml` |
| `zz_ef_trm_sell_g_v` | vit | `localization/english/ld_treasury_metal_l_english.yml` |
| `zz_ef_trm_sell_s_v` | vit | `localization/english/ld_treasury_metal_l_english.yml` |
| `zz_ef_trm_silver_goods_v` | calc | `localization/english/ld_treasury_metal_l_english.yml` |
| `zz_ef_trm_step_goods` | calc | `localization/english/ld_treasury_metal_l_english.yml` |
| `zz_ef_trust_v` | calc | `localization/english/ld_panic_l_english.yml` |
| `zz_ef_v_cbl_int` | calc | `gui/ld_money_hook.gui`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_abroad` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_agg0` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_agg1` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_agg2` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_agg3` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_bonds` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_buildings` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_cbm` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_deposits` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_deposits_neg` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_pool` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_savings` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_tbonds` | vit | `gui/ld_money_hook.gui`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_tc` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_d_treasury` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_bc_int` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_bc_new` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_bc_paid` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_bl_int_in` | vit | `gui/ld_money_hook.gui`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_bl_int_out` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_bl_redeem` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_bl_sold` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_buyback_m` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_borrow` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_hume_m` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_int_dep` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_interest` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_repay` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_rescale` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_reval` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cb_stock` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_clr_fx_money` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_clr_got` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_clr_metal_money` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_clr_paid` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_clr_reserves_money` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_clr_unsettled` | calc | `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_co_contrib` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cons_buy` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_cons_int` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_contrib` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_exp` | vit | `gui/ld_economy_panel.gui` |
| `zz_ef_v_f_ext` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_ext_net` | vit | `gui/ld_economy_panel.gui`, `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_fd_in` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_fd_out` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_fd_pp` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_gl_pool` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_imp` | vit | `gui/ld_economy_panel.gui`, `localization/english/ld_economy_panel_l_english.yml`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_inflow` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_leak` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_mint` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_mint_own` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_mint_tr` | vit | `gui/ld_money_hook.gui`, `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_pool_other` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_popm_bank` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_popm_cb` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_tr_pool` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_trade` | vit | `gui/ld_economy_panel.gui` |
| `zz_ef_v_f_transfer` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_xch_pool` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_f_xch_pp` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_fx_metal` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_bk_div_pop` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_bk_div_tr` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_cash_dep` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_cc_int` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_cc_issue` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_cc_repay` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_clr_cur_out` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_clr_fx_in_money` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_clr_fx_out_money` | calc | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_clr_own_back` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_co_div` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_dep_int` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_fxint_abr` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_hume_money` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_inflow` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_leak_back` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_leak_back_pop` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_lvl_post` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_nr_dep` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_nr_xch` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_v_w_xch_abr` | vit | `localization/english/replace/ld_money_supply_replace_l_english.yml` |
| `zz_ef_value_in_silver` | calc | `localization/english/01_ef_tooltips_localization_l_english.yml` |
| `zz_ef_xch` | var | `localization/english/ld_exchange_window_l_english.yml` |
| `zz_ef_xch_my_heat_v` | calc | `gui/00_ef_deported_gui_1.gui`, `gui/ld_cb_rate_panel.gui` |
| `zz_ef_xch_my_to_v` | calc | `gui/00_ef_deported_gui_1.gui`, `gui/ld_cb_rate_panel.gui` |
| `zz_ef_xlm_cap_v` | vit | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_xlm_heat_v` | calc | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_xlm_rank_v` | calc | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_xwin_ask` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_xwin_bid` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_xwin_fair` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_xwin_fee_v` | calc | `localization/english/ld_exchange_window_l_english.yml` |
| `zz_ef_xwin_gold` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_xwin_holdc` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_xwin_kind_v` | vit | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_xwin_last` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_xwin_ob` | var | `localization/english/ld_exchange_window_l_english.yml` |
| `zz_ef_xwin_os` | var | `gui/ld_cb_rate_panel.gui` |
| `zz_ef_xwin_sum_v` | calc | `localization/english/ld_exchange_window_l_english.yml` |
<!-- /vitrine -->
