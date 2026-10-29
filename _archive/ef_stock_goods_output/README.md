---
type: code
description: "Выпуск товаров-«акций» E&F (Д.R4б.8): методы «частного владения» (pmg_private_ownership_{manufacture,agricultural,mining,railroad}_stock, pm_private_ownership_majority_*_stock: выход «акций» 12,5 на рабочую…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_stock_goods_output/**"]
---
# Выпуск товаров-«акций» E&F (Д.R4б.8)

**Что делало:** методы «частного владения» (`pmg_private_ownership_{manufacture,agricultural,mining,railroad}_stock`,
`pm_private_ownership_majority_*_stock`: выход «акций» 12,5 на рабочую силу, ферма 5, частная ж/д 25) у ванильных
зданий (INJECT в `common/buildings/ef_*.txt`) — переключались по доле частного владения (> 0,5) хуком смены метода
(`zz_ef_pm_stock_building`, генератор `regen_ef_pm_stock_hook`) и годовым перебором `private_ownership_production_stocks`;
стройсектор PSC выпускал `manufacture_stock` (20 / 50 / 100 / 150 по методам). [[Финцентр]] покупал «акции» методами
`pm_*_stock_exchange`, их включал `financial_center_production_methods` (`zz_ef_fc_pm_switch`). Население покупало
«акции» потребностью «финансовые продукты».

**Почему в архив:** [[Д.R4б.8 — Товары-«акции» E&F|Д.R4б.8]] (пользователь 12.10) — выпуск «акций» убрать вместе со входом финцентра; что такое акции —
R6. Товары `manufacture_stock` и др. остаются (их читают капитализация, листинг, престижные товары, окна E&F — R6).

**Вырезано из живых файлов** (кроме файлов и определений, лежащих здесь по исходным путям):
```
common/buildings/ef_01_industry.txt:7: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:14: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:21: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:28: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:35: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:42: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:50: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:57: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:64: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:71: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:78: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:86: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:94: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:101: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:109: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:116: pmg_private_ownership_manufacture_stock
common/buildings/ef_01_industry.txt:123: pmg_private_ownership_manufacture_stock
common/buildings/ef_02_agro.txt:6: pmg_private_ownership_agricultural_stock
common/buildings/ef_02_agro.txt:13: pmg_private_ownership_agricultural_stock
common/buildings/ef_02_agro.txt:20: pmg_private_ownership_agricultural_stock
common/buildings/ef_02_agro.txt:27: pmg_private_ownership_agricultural_stock
common/buildings/ef_02_agro.txt:34: pmg_private_ownership_agricultural_stock
common/buildings/ef_02_agro.txt:41: pmg_private_ownership_agricultural_stock
common/buildings/ef_02_agro.txt:48: pmg_private_ownership_agricultural_stock
common/buildings/ef_03_mines.txt:7: pmg_private_ownership_mining_stock
common/buildings/ef_03_mines.txt:15: pmg_private_ownership_mining_stock
common/buildings/ef_03_mines.txt:23: pmg_private_ownership_mining_stock
common/buildings/ef_03_mines.txt:32: pmg_private_ownership_mining_stock
common/buildings/ef_03_mines.txt:39: pmg_private_ownership_mining_stock
common/buildings/ef_03_mines.txt:47: pmg_private_ownership_mining_stock
common/buildings/ef_03_mines.txt:83: pmg_private_ownership_mining_stock
common/buildings/ef_04_plantations.txt:7: pmg_private_ownership_agricultural_stock
common/buildings/ef_04_plantations.txt:14: pmg_private_ownership_agricultural_stock
common/buildings/ef_04_plantations.txt:21: pmg_private_ownership_agricultural_stock
common/buildings/ef_04_plantations.txt:28: pmg_private_ownership_agricultural_stock
common/buildings/ef_04_plantations.txt:35: pmg_private_ownership_agricultural_stock
common/buildings/ef_04_plantations.txt:42: pmg_private_ownership_agricultural_stock
common/buildings/ef_04_plantations.txt:49: pmg_private_ownership_agricultural_stock
common/buildings/ef_04_plantations.txt:56: pmg_private_ownership_agricultural_stock
common/buildings/ef_04_plantations.txt:63: pmg_private_ownership_agricultural_stock
common/buildings/ef_06_urban_center.txt:4: pmg_private_ownership_manufacture_stock
common/buildings/ef_09_misc_resource.txt:8: pmg_private_ownership_agricultural_stock
common/buildings/ef_09_misc_resource.txt:16: pmg_private_ownership_agricultural_stock
common/buildings/ef_09_misc_resource.txt:24: pmg_private_ownership_agricultural_stock
common/buildings/ef_09_misc_resource.txt:32: pmg_private_ownership_agricultural_stock
common/buildings/ef_09_misc_resource.txt:40: pmg_private_ownership_mining_stock
common/buildings/ef_11_private_infrastructure.txt:8: pmg_private_ownership_manufacture_stock
common/buildings/ef_11_private_infrastructure.txt:16: pmg_private_ownership_railroad_stock
common/buildings/ef_11_private_infrastructure.txt:24: pmg_private_ownership_manufacture_stock
common/production_methods/zz_PSC_construction.txt:15: # output goods (E&F)
common/production_methods/zz_PSC_construction.txt:16: goods_output_manufacture_stock_add = 20 #50
common/production_methods/zz_PSC_construction.txt:48: # output goods (E&F)
common/production_methods/zz_PSC_construction.txt:49: goods_output_manufacture_stock_add = 50 #100
common/production_methods/zz_PSC_construction.txt:82: # output goods (E&F)
common/production_methods/zz_PSC_construction.txt:83: goods_output_manufacture_stock_add = 100 #150
common/production_methods/zz_PSC_construction.txt:117: # output goods (E&F)
common/production_methods/zz_PSC_construction.txt:118: goods_output_manufacture_stock_add = 150 #200
common/scripted_effects/00_on_action_main.txt:767: private_ownership_production_stocks = yes
common/scripted_effects/00_on_action_main.txt:768: financial_center_production_methods = yes
common/scripted_effects/09_introduction_building_lvl.txt:22320: financial_center_production_methods = yes
common/scripted_effects/ld_start_setup.txt: if = { limit = { has_modifier = has_financial_center } private_ownership_production_stocks = yes financial_center_production_methods = yes }
common/pop_needs/00_ef_pop_needs.txt: popneed_financial_products entry goods = manufacture_stock
common/pop_needs/00_ef_pop_needs.txt: popneed_financial_products entry goods = agricultural_stock
common/pop_needs/00_ef_pop_needs.txt: popneed_financial_products entry goods = mining_stock
common/pop_needs/00_ef_pop_needs.txt: popneed_financial_products entry goods = railroad_stock
common/on_actions/00_ef_on_action.txt: on_production_method_changed = { on_actions = { ef_on_production_method_changed } }, ef_on_production_method_changed
common/scripted_effects/01_financial_scripted_effects.txt: financial_center_production_methods, zz_ef_fc_pm_switch, private_ownership_production_stocks
```
Генератор `regen_ef_pm_stock_hook.py` (был в `../vic3_mods/tools/`) — здесь, `tools/`.
