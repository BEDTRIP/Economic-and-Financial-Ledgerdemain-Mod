# Регулятор стройки не больше предложения рынка (`ld_psc_market_fill`)

Вынуто 14.10.2026 (R9, откат шага 3 — Д.R9.4). Механизм работал, но результат хуже базы — по правилу ночи откат.

**Что делал:** на стране k каждого стройтовара (`var:zz_ef_psc_k_<товар>`) = прошлое k × продажи / заказы на рынке,
0,05–1 (`zz_ef_psc_fill_update` в начале недели PSC); пропускная регулятора и очки штата × k его товара
(`zz_ef_psc_fill_v`), со смесью шага 4 — × K = Σ доля × k, действующая доля — доля × k / K.

**Почему снят:** прогоны r1014_182726 (шаг 3) и r1014_184800 (шаги 3 + 4) до 1841 против базы r1014_151458: железо
продажи / заказы 0,98–0,99 (база 0,57), `gap_psc` ~0 (база −25,7 млн) — цель достигнута, но очки мира 1840 — 509 / 595
в неделю против 1383 (−57…63 %), выпуск секторов 5,6–5,8 тыс. против 9,7, деловой кредит 108–122 млн против 289, M2 /
ВВП 1,06–1,07 против 1,49, казна 106–121 млн против 51. Очки базы наполовину не обеспечены товаром: регуляторы платили
за недостающее железо по цене нехватки, движок засчитывал очки, деньги сгорали; эта выручка держала сектора. Решение —
вопрос В.R9.10 (`история/2026-10-14 этап R9.md`, «Вопросы на утро»).

**Удалено из живых файлов:**
| файл | что |
| --- | --- |
| `common/scripted_effects/ld_psc_market_fill.txt`, `common/script_values/ld_psc_market_fill_values.txt` | файлы целиком (здесь) |
| `common/scripted_effects/PSC_scripted_effects.txt` | в `set_construction_point_demand`: вызов `zz_ef_psc_fill_update = yes` (после `if` на `urbanization`); `set_local_variable = { name = psc_fill value = zz_ef_psc_fill_v }` после `state_construction`; `multiply = local_var:psc_fill` в `psc_state_points` и в `modifier_mult` регулятора |
| `common/scripted_effects/ld_construction_market.txt` | K смеси: `zz_ef_reg_fill_add` (K += доля × `owner.var:zz_ef_psc_k_<товар>`), `var:zz_ef_reg_fill` (не меньше `zz_ef_reg_fill_min` 0,05), действующая доля = доля × k / K в `zz_ef_reg_effective` |
| `common/scripted_effects/ld_psc_log.txt` | поля `kw`, `ki` строки `EFZ` |

**Вернуть:** файлы — на место; вызовы и множители — как в таблице; в `zz_ef_psc_fill_v` первая ветка — `var:zz_ef_reg_fill`.
