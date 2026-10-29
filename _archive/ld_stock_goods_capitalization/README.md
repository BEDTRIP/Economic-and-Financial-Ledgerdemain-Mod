---
type: code
description: "Капитализация по выпуску товаров-«акций» и срез выпуска по грамотности богатых: Вынуто 14.10.2026 (R6.7, Д.R6.12). Товары-«акции» E&F (manufacture_stock, agricultural_stock, mining_stock, railroad_stock) больше не производятся (Д.R4б.8);…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ld_stock_goods_capitalization/**"]
---
# Капитализация по выпуску товаров-«акций» и срез выпуска по грамотности богатых

Вынуто 14.10.2026 (R6.7, [[Д.R6.12 — Капитализация и товары-«акции»|Д.R6.12]]). Товары-«акции» E&F (`manufacture_stock`, `agricultural_stock`, `mining_stock`,
`railroad_stock`) больше не производятся ([[Д.R4б.8 — Товары-«акции» E&F|Д.R4б.8]]); капитализация биржи — акции компаний по рыночной цене
(`zz_ef_cap_listed_snapshot`, `ld_listing_values.txt`; акции — `ld_company_shares.txt`).

## Что делало
- `zz_ef_cap_state_output_<акция>` (штат: недельный выпуск), `zz_ef_cap_qty_<акция>` (выпуск страны × `zz_ef_cap_weeks`
  = 520), `zz_ef_cap_snap_<акция>` (× цена E&F) — делили месячный снимок капитализации на четыре «акции» по долям
  выпуска (`zz_ef_cap_monthly_update`) и давали E&F-количество `stockpiling_<акция>_var_state` до первой средней;
- `zz_ef_stock_issue_update` (EF.28): доля грамотных богатых (`zz_ef_literate_rich_share`) → срез выпуска «акций»
  модификатором страны `zz_ef_stock_issue_literacy` (`goods_output_<акция>_mult`, `zz_ef_stock_issue_cut_points`,
  эталон `zz_ef_stock_issue_reference_share` = 12 %); грамотность самих богатых (`zz_ef_rich_literacy`) — доля ШК на
  бирже — осталась (`zz_ef_rich_literacy_update`, `common/scripted_effects/ld_rich_literacy.txt`).

## Удалено из живых файлов
| файл | что |
| --- | --- |
| `common/script_values/ld_capitalization_snapshot.txt` | шапка о выпуске × 520, `zz_ef_cap_weeks`, 12 значений `zz_ef_cap_state_output_*`, `zz_ef_cap_qty_*`, `zz_ef_cap_snap_*` (здесь) |
| `common/scripted_effects/ld_capitalization_average.txt` | разбивка снимка по выпуску (4 `zz_ef_cap_snap_*`, `zz_s_total`) — теперь поровну |
| `common/script_values/00_financial_scripted_value.txt` | `else = { value = zz_ef_cap_qty_<акция>_stock }` в четырёх `stockpiling_<акция>_var_state` — теперь 0 |
| `common/static_modifiers/ld_stock_issue_literacy.txt`, `common/script_values/ld_stock_issue_literacy_values.txt` | целиком (здесь) |
| `common/scripted_effects/ld_stock_issue_literacy.txt` | → `ld_rich_literacy.txt` (`zz_ef_rich_literacy_update`); снято: модификатор и `zz_ef_stock_issue_cut` (файл целиком — здесь) |
| `common/on_actions/ld_capitalization_on_actions.txt` | `zz_ef_stock_issue_update = yes` → `zz_ef_rich_literacy_update = yes` |
| `localization/<язык>/ld_cm_goods_l_<язык>.yml` | `zz_ef_stock_issue_literacy`, `zz_ef_stock_issue_literacy_desc` (11 языков; английский и русский — `localization/`) |

## Кусок 2 (14.10.2026, R6.7): счётчики «акций» E&F в штатах
`stockpiling_<акция>_stock_var_state_1` (четыре «акции») E&F копил в штате финцентра и переносил при переезде
(`stockpiling_capital_state_transfert*`, `01_economic_scripted_effects.txt`); скрипт их больше не читает (капитализация
— акции компаний). Удалено: 20 записей и чтений в `01_economic_scripted_effects.txt` (условие переноса, перенос в
новый штат финцентра, сброс старого — здесь). Остались, пока их показывает окно штата E&F
(`gui/00_ef_deported_gui_1.gui`, строки «акций» — R10): стартовые значения (`common/history/global/zz_ef_init_stockpiling_state_vars.txt`,
`99_ef_history_global_variable.txt`, `10_new_country_var.txt`) и посев `ld_stockpile_state_var_seed.txt`.
