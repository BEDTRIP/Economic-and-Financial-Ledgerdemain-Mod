# Месячный торговый резерв `zz_ef_rc_step` (выключен)

**Что делал:** раз в месяц для каждой пары владельцев рынков с ЦБ искал недельный экспорт в обе стороны (двоичный поиск по
`market_exports`), и импортёр платил долю `zz_ef_rc_share` (25%) чистого экспорта своей валютой вместо металла: сначала
возвращал валюту экспортёра, которую держал, остальное ЦБ экспортёра брал валютой импортёра
(`stockpiling_<cur>_state_1` столичных штатов ЦБ).

**Почему выключен:** недельный клиринг (`zz_ef_clr_step`, `ld_clearing.txt`) платит отток металлом и валютой плательщика —
месячная пара поверх него посчитала бы дважды. Вызов был закомментирован.

**Переменные:** писал `zz_ef_rc_q_in/_q_out/_price/_units/_held/_back_now/_try`, `zz_ef_rc_fx_in`, `zz_ef_rc_back`,
`zz_ef_rc_metal_out` (их читают поля лога `EFX` через `zz_ef_v_rc_*` — значения оставлены в моде, всегда 0).

**Файлы здесь:** `common/scripted_effects/ld_reserve_trade.txt` целиком (`zz_ef_rc_step`, `_pair`, `_search`,
`_read_held`, `_take_held`, `_add_units`); `common/script_values/ld_reserve_trade_values.txt` — вырезанные
`zz_ef_rc_share`, `_share_month`, `_unit_price`, `_export_value`, `_export_units`, `_pair_net`.

**Удалено из живых файлов:**
- `common/scripted_effects/ld_money_model.txt` (`zz_ef_money_model_monthly_step`): комментарий из 4 строк и `# zz_ef_rc_step = yes`.
- генератор `vic3_mods/tools/regen_ef_reserve_trade.py`: эффекты (`effects`, `search_effect`, `STEP`) и значения выше; генератор
  пишет теперь только `zz_ef_rc_currency_value`, `zz_ef_fx_liab`, `zz_ef_v_rc_*`.

**Вернуть:** код генератора — в истории `vic3_mods` (до 6.10.2026); файл эффектов — обратно в `common/scripted_effects/`,
значения — в `ld_reserve_trade_values.txt`, вызов `zz_ef_rc_step = yes` — в месячный шаг.
