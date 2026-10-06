# Деньги за металл по Юму (zz_ef_f_hume_money, ветка в zz_ef_cb_hume_step)

**Что делало.** M.3: металл, пришедший по клирингу в ЦБ (`var:zz_ef_f_hume`), чеканился в деньги по паритету — `add_investment_pool` на сумму (на выходе — не больше пула).
П.5 (4.10): выключено константой `zz_ef_hume_money_on = 0` (деньги экспортёру двигатель платит сам, эмиссия ЦБ считала их дважды: пул Британии 4M → 163M за 8 лет).
**Кто вызывал.** Ветка внутри `zz_ef_cb_hume_step` (страна с ЦБ на золотом/серебряном/биметаллическом стандарте). **Интерфейс.** Строки «Юм» в карточках банков/ЦБ — всегда 0.

**Что лежит здесь**
- `common/scripted_effects/ld_money_model.txt` — блок `if` стандарта металла (строки 700–742): `has_modifier = has_central_bank` + стандарт → `if zz_ef_hume_money_on > 0` →
  `zz_ef_f_hume_money`, `add_investment_pool = var:zz_ef_f_hume_money`.
- `common/script_values/ld_money_model_values.txt` — `zz_ef_hume_metal_week` (без ссылок), `zz_ef_hume_money_on = 0`.

**Оставлено в живых файлах и почему**
- `set_variable zz_ef_f_hume_money = 0` в начале `zz_ef_cb_hume_step`, `zz_ef_money_window_roll = { F = hume_money }` (`zz_ef_w_hume_money` = 0) и значения `zz_ef_v_f_hume_money`,
  `zz_ef_v_w_hume_money`: `zz_ef_v_w_hume_money` вычитается в `zz_ef_v_d_pool_rest` и ещё одном значении (`ld_money_model_values.txt`), его же и `zz_ef_v_f_hume_money` читают
  логи `EFO`/`EFF` (`ld_money_log_rest.txt`, генератор `regen_ef_money_supply_loc`) и ключи локализации `zz_ef_ms_banks_25/26`, `zz_ef_ms_x_v_w_hume_money(_neg)` (генератор) — нули в карточке банков.
- Металл Юма (`zz_ef_f_hume`, `zz_ef_f_cb_hume_m`, `zz_ef_wld_hume*`) — живой.

**Удалено из живых файлов.** Блок `if` стандарта металла из `zz_ef_cb_hume_step` (за `zz_ef_clr_step = yes`, перед `zz_ef_world_acc = yes`), два определения/комментария значений.
**Вернуть.** Блок — на место; значения — перед `zz_ef_v_f_abr` и после `zz_ef_v_f_ext_net`; включить `zz_ef_hume_money_on = 1` (внимание: двойной счёт).
