---
type: code
description: "Мёртвое и снятое по аудиту PSC (`psc_audit_r9`): Вынуто 14.10.2026, R9.1 (аудит PSC, Д.R9.5, Д.R8в.27)."
project: vic3
tags: [форк, архив]
paths: ["_archive/psc_audit_r9/**"]
---
# Мёртвое и снятое по аудиту PSC (`psc_audit_r9`)

Вынуто 14.10.2026, R9.1 (аудит PSC, Д.R9.5, Д.R8в.27).

| что | где было | почему снято |
| --- | --- | --- |
| счётчик `num_runs` (страна) | начало `set_construction_point_demand`, `common/scripted_effects/PSC_scripted_effects.txt` | пишется каждую неделю, никто не читает |
| снос регулятора выше уровня сектора (`week_count`, `remove_building`) | начало `set_construction_regulator_level`, там же | снесённый регулятор следующим блоком строился заново пустым и нанимал бюрократов с нуля; лишние уровни только понижают пропускную (`construction_throughput_mult`) — Д.R8в.27: регулятор только растёт |
| `construction_demand_ratio` (= 0) | `common/script_values/PSC_construction_values.txt` | `nominal_construction_demand` PSC не задаёт (тело — в `_archive/ld_dead_readers/`); единственный читатель — алерт ниже |
| условие алерта `insufficient_construction_for_investment` | `common/alert_types/PSC_alert_types.txt` | с `construction_demand_ratio` = 0 никогда не срабатывало; REPLACE остался с `valid = { always = no }` — ванильный алерт («пул не тратится») при стройке PSC выключен |

Переменные в старых сейвах (`num_runs`, `week_count` у штатов) остаются и ничего не делают.

**Вернуть:** вставить блоки из файлов здесь на прежние места (снос регулятора — перед ростом в
`set_construction_regulator_level`; условие алерта — вместо `always = no`).
