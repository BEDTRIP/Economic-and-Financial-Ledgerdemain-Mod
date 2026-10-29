---
type: code
description: "Методы бирж «акций» финцентра и деление комиссии по владельцам (Д.R4б.5, Д.R4б.7): четыре группы методов финцентра (pmg_{manufacture,agricultural,mining,railroad}_stock_exchange, pm_no_* / pm_*_stock_exchange: вход goods_input_<вид>_stock_add 1 на…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_fc_stock_exchange_pm/**"]
---
# Методы бирж «акций» финцентра и деление комиссии по владельцам (Д.R4б.5, Д.R4б.7)

**Что делало:** четыре группы методов финцентра (`pmg_{manufacture,agricultural,mining,railroad}_stock_exchange`,
`pm_no_*` / `pm_*_stock_exchange`: вход `goods_input_<вид>_stock_add` 1 на рабочую силу) — финцентр покупал товары-«акции»;
переключал их `financial_center_production_methods` (в `_archive/ef_stock_goods_output/`). [[Комиссия биржи]] делилась по
владельцам финцентра: доля государства в здании (по четвертям, `zz_ef_xch_fc_state_share_v`, `_here_v`) — в казну,
частная — во вклады населения.

**Почему в архив:** [[Д.R4б.5 — Биржа — государственная инфраструктура|Д.R4б.5]] — биржа государственная, комиссия в казну; [[Д.R4б.7 — Финцентр|Д.R4б.7]] — финцентр «акций» не покупает, у него
работники и вход «услуг» (`pmg_zz_ef_fc_exchange`).

**Вырезано из живых файлов:** определения — здесь по исходным путям; генератор `regen_ld_financial_centres.py`
(`../vic3_mods/tools/`) больше не пишет группы «акций» в типы финцентра и `zz_ef_fc_activate_pm` (был в
`common/scripted_effects/ld_fc_types.txt`: метод во всех финцентрах штата); `zz_ef_xch_fee_pay`
(`ld_exchange_trade.txt`) — без деления по владельцам.
