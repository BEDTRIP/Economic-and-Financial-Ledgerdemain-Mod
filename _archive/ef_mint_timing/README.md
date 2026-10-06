# Хронометрия чеканки ЦБ (значения zz_ef_mint_*)

**Что делало.** Значения для «чеканки в резервы»: ЦБ чеканит долю `zz_ef_mint_share` (0.5) недельной добычи золота/серебра по рыночной цене
(`zz_ef_mint_gold/silver_money`), металл по паритету (`zz_ef_mint_gold/silver_metal`), доля казны `zz_ef_mint_treasury_share` (0.01). Недельный шаг эти значения не
вызывает: `zz_ef_f_mint` и `zz_ef_f_mint_tr` в `zz_ef_money_model_step` только обнуляются (`# The mint's log keys (EFR mint / mint_tr) stay 0`), добыча золотых шахт в чеканку обнулена
INJECT `ld_gold_mine_minting_off.txt`.
**Кто вызывал.** Никто. **Интерфейс.** Нет.

**Что лежит здесь** — `common/script_values/ld_money_model_values.txt` (диапазоны в начале): `zz_ef_mint_share`, `zz_ef_mint_treasury_share` (с комментарием «Mining into the reserves»),
`zz_ef_silver_mined_week` (осиротело), `zz_ef_mint_gold_money`, `zz_ef_mint_silver_money`, `zz_ef_mint_gold_metal`, `zz_ef_mint_silver_metal`.

**Оставлено в живых файлах и почему**
- `set_variable zz_ef_f_mint = 0`, `zz_ef_f_mint_tr = 0` (`ld_money_model.txt`, недельный шаг) и значения `zz_ef_v_f_mint`, `zz_ef_v_f_mint_tr`, `zz_ef_v_f_mint_own` — их читают
  `debug_log` строк `EFR` (`ld_money_model.txt`), `EFF`/`EFO` (`ld_money_log_rest.txt`, ведётся генератором `regen_ef_money_supply_loc`), мост `gui/ld_money_hook.gui` (генератор) и ключи
  локализации `zz_ef_ms_x_v_f_mint*`, `zz_ef_ms_x_v_d_cbm_rest` (`replace/ld_money_supply_replace_l_*.yml`, генератор) — строки чеканки в карточках ЦБ всегда 0.
  Убирать их надо вместе с генератором, затем здесь.
- `zz_ef_gold_mined_week` читает `debug_log` EFR; `zz_ef_gold_price`, `zz_ef_silver_price` — лог EFT (`ld_metal_accounts.txt`).

**Удалено из живых файлов.** Только перечисленные значения; вызовов, GUI, локализации нет. **Вернуть.** Вставить блоки на место (после `zz_ef_fx_deal_size`).
