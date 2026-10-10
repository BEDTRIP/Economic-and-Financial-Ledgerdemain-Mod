# Документация мода — карта

Для агента, который правит мод: **код** — где лежит, какие переменные и вызовы. **Что это и зачем** — заметки
`понятия/` ([[_Карта понятий]]): одно понятие — одна заметка; **почему так** — `решения.md`; **что дальше** — `план.md` и `этапы/`.
Читать этот файл первым, дальше — документ нужной подсистемы; каждый документ начинается со смысла и ссылок на понятия.
Документы описывают текущее состояние: правка мода, которая меняет описанное, правит документ и заметку понятия в том же
коммите (`CLAUDE.md` форка). Игра `docs/` не читает. Ключи в файлах `ld_*` — с префиксом `zz_ef_`.

## Подсистемы
| подсистема | документ | главные файлы |
| --- | --- | --- |
| Старт игры: история, хук после лобби, первые шаги модели, разовое в пульсах E&F | `game-start.md` | `common/history/`, `common/scripted_effects/ld_start_setup.txt`, `common/scripted_effects/ld_metal_accounts.txt` |
| Точки входа: история, on_actions, порядок шагов, логи `EF*` | `entry-points.md` | `common/on_actions/`, `common/scripted_effects/00_on_action_main.txt`, `common/history/` |
| Денежная модель и счета: M0–M3, пул, касса, металл ЦБ / банков / населения | `money-model.md` | `common/scripted_effects/ld_money_model.txt`, `common/scripted_effects/ld_metal_accounts.txt` |
| Валюты, законы, стандарты, эталон, союзы; таблица валют | `currencies.md`, `currency-table.md` | `common/script_values/01_economic_currency_scripted_value.txt`, `common/scripted_effects/ld_standard_switch.txt` |
| ЦБ: ставка, денежная политика, кредит ЦБ, облигации ЦБ, премия за риск | `central-bank.md` | `common/script_values/ld_cb_rate_values.txt`, `common/scripted_effects/ld_monetary_policy.txt` |
| Банки и вклады | `banks.md` | `common/buildings/ld_bank.txt`, `common/scripted_effects/ld_bank_seed.txt`, `common/scripted_effects/ld_nr_deposits.txt` |
| Облигации и консоли | `bonds.md` | `common/scripted_effects/ld_bond_ledger.txt`, `common/scripted_effects/ld_consols.txt` |
| Реестр требований: словари держателей «должник → сумма», итоги должников, сверка | `claims.md` | `common/scripted_effects/ld_claims.txt`, `common/script_values/ld_claims_values.txt` |
| Клиринг, форекс, резервы | `clearing-fx.md` | `common/scripted_effects/ld_clearing.txt`, `common/scripted_guis/ld_cbfx.txt` |
| Биржа, компании, финансовый центр | `exchange-companies.md` | `common/company_types/00_ef_companies.txt`, `common/scripted_effects/ld_listing.txt`, `common/script_values/ld_capitalization_snapshot.txt` |
| Стройка: PSC, домохозяйства, перестройка, ИИ | `construction.md` | `common/scripted_effects/PSC_scripted_effects.txt`, `common/script_values/ld_pb_overbuild_values.txt` |
| Потребности населения и товары | `pop-needs.md` | `common/pop_needs/00_ef_pop_needs.txt`, `common/buy_packages/00_ef_buy_packages.txt`, `common/goods/ef_00_goods.txt` |
| Ядро E&F: здания и PM, модификаторы, триггеры, решения, события, журналы | `ef-core.md` | `common/scripted_effects/01_economic_scripted_effects.txt`, `common/scripted_triggers/00_ef_custom_trigger.txt` |
| Интерфейс: панели, мост GUI → скрипт, отладочные окна, локализация; список имён витрины — генерат `vitrine.md` | `interface.md`, `vitrine.md` | `gui/00_ef_deported_gui_1.gui`, `common/scripted_guis/00_economic_scripted_guis.txt`, `gui/ld_money_hook.gui` |
| Генераторы файлов `ld_*` | `generators.md` | `../vic3_mods/tools/regen_ef_*.py` |
| **Реестр механизмов** — живой / выключен / мёртвый / дубль | `mechanisms.md` | — |

## Порядок шага (кратко; подробно — `entry-points.md`)
- **Старт игры** (`game-start.md`): `common/history/buildings/` → `common/history/global/` (по имени файла) →
  `common/history/states/`; после лобби — верхняя панель E&F, проход по штатам, настройка старта E&F (`zz_ef_start_setup`),
  планировщик; PSC запускает стройку событием.
- **Новая страна:** одна точка — `zz_ef_country_init` (`common/scripted_effects/ld_country_init.txt`): переменные E&F
  (`new_country_var_ef`, через скрытое событие `zz_ef_newcountry.1`), рейтинг, валюта, реестр счетов — из хуков новой
  страны и первого захода планировщика; страна без хука — месячный хаб E&F; признак готовности — `var:zz_ef_country_vars_set`.
- **Роли и планировщик** (`money-model.md`): роль страны А / Б / В — А / Б раз в год по категории А, В и новые — раз в месяц (`on_monthly_pulse` →
  `zz_ef_roles_world_pass`); одна глобальная цепочка `zz_ef_sched_day` от дня бюджетного тика ведёт все шаги модели.
- **Месяц** (страны А / Б — из планировщика, раз в календарный месяц, в свой день, порядок фиксирован): E&F
  `ef_on_monthly_pulse_country` (ЦБ, инфляция), месячный шаг модели денег, банки, ставка ЦБ (шаг раз в 3 месяца),
  капитализация, пузырь, перестройка PSC. Страны вне планировщика (В и др.) — пульс движка, только хаб E&F.
- **Неделя:** `zz_ef_money_model_step` (металл, клиринг, облигации, консоли, кредит, M0–M3, лог `EFW`) — А каждую неделю,
  Б тоже каждую неделю (мост у Б — раз в 4 недели); мировой проход — в конце недели. Мост GUI → скрипт
  (`zz_ef_money_hook_receive`) только приносит числа, которых нет в скрипте (строки бюджета, владение за границей); шаг
  берёт последние полученные.
- **Полгода / год:** ИИ-стройка E&F, колебания курсов, выбор эталонной валюты (`EFE`).

## Соглашения
- Файлы E&F и PSC — под своими именами (`00_ef_*`, `01_*`, `ef_*`, `PSC_*`). Файлы проекта — `ld_*`; **ключи внутри
  `ld_*` сохранили имена `zz_ef_*` / `zz_pb_ef_*`** (эффекты, значения, переменные, on_action'ы).
- Переменные E&F по валюте — шаблон с `<cur>` (95 валют): `stockpiling_<cur>_state_1`, `money_value_<cur>` …; металл
  ЦБ — `gold_state_1` / `silver_state_1` штата ЦБ (`var:central_bank_location`).
- Логи — `debug_log` с префиксом `EFx|дата|страна|метка|поле значение|…` в `game.log`; таблица префиксов —
  `entry-points.md`, «Логи».
- GUI-тип регистрирует первый файл по имени; дубль типа — мёртвый (`interface.md`).
- Мёртвые механизмы — в `_archive/` (игра не читает; оглавление — `_archive/README.md`, правила — `CLAUDE.md`).

## Куда смотреть
| задача | куда |
| --- | --- |
| деньги не сходятся, невязка `EFQ` / `EFW` | `money-model.md`; что ещё пишет в счета мимо модели — `mechanisms.md`, статусы `живой` / `дубль` с пометкой о счетах |
| ставка, девальвация, кредит ЦБ | `central-bank.md` |
| валюта страны, смена стандарта, эталон | `currencies.md` |
| металл / валюта уходят за границу | `clearing-fx.md`, `banks.md` (вклады нерезидентов) |
| компании, акции, пузырь, крах | `exchange-companies.md` |
| стройка, сектора, домохозяйства | `construction.md` |
| ошибка в окне / кнопка не работает | `interface.md` |
| уборка мёртвого | `mechanisms.md` → документ подсистемы → перенос в `_archive/` |
| файл `ld_*` нельзя править руками? | `generators.md` |

## Инструменты (`../vic3_mods/tools/`)
- `ld_index.py` — индекс определений форка и числа ссылок на каждое (`refs = 0` — кандидат в мёртвые; -1 — точка
  входа движка). Вывод — `_tmp_analysis/ld_index/index.tsv`.
- `ld_docs_check.py` — каждый файл `common/` и `events/` упомянут в `docs/`, пути в `docs/` существуют. Запускать после
  правки документов или добавления / удаления файлов.
- `ld_gen.py` + `regen_ef_*.py` — генераторы (`generators.md`); `ld_loc_langs.py` — девять языков из английского;
  `ld_sync_live.py` — живая копия мода.
- `ld_smells.py` — смеллы кода по графу вызовов: где проверки закона валюты, цепочки `if / else_if`, перебор в
  переборе, семейства имён «по одной на сущность», переменные без читателя / писателя, дубли, числа, шапки генератов
  без генератора; «жара» места — неделя / месяц / год / старт / окна. `python ../vic3_mods/tools/ld_smells.py` — сводка.
