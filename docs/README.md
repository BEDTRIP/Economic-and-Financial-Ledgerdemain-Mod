# Документация мода — карта

Для агента, который правит мод. Читать этот файл первым, дальше — документ нужной подсистемы. Документы описывают
текущее состояние: правка мода, которая меняет описанное, правит документ в том же коммите (`CLAUDE.md` форка).
Игра `docs/` не читает.

## Подсистемы
| подсистема | документ | главные файлы |
| --- | --- | --- |
| Точки входа: история, on_actions, порядок шагов, логи `EF*` | `entry-points.md` | `common/on_actions/`, `common/scripted_effects/00_on_action_main.txt`, `common/history/` |
| Денежная модель и счета: M0–M3, пул, касса, металл ЦБ / банков / населения | `money-model.md` | `common/scripted_effects/ld_money_model.txt`, `common/scripted_effects/ld_metal_accounts.txt` |
| Валюты, законы, стандарты, эталон, валютные зоны и союзы | `currencies.md` | `common/laws/01_ef_currency_type.txt`, `common/script_values/01_economic_currency_scripted_value.txt`, `common/scripted_effects/ld_standard_switch.txt` |
| ЦБ: ставка, денежная политика, кредит ЦБ, облигации ЦБ, премия за риск | `central-bank.md` | `common/script_values/ld_cb_rate_values.txt`, `common/scripted_effects/ld_monetary_policy.txt` |
| Банки и вклады | `banks.md` | `common/buildings/ld_bank.txt`, `common/scripted_effects/ld_bank_seed.txt`, `common/scripted_effects/ld_nr_deposits.txt` |
| Облигации и консоли | `bonds.md` | `common/scripted_effects/ld_bond_ledger.txt`, `common/scripted_effects/ld_consols.txt` |
| Клиринг, форекс, резервы | `clearing-fx.md` | `common/scripted_effects/ld_clearing.txt`, `common/scripted_guis/ld_cbfx.txt` |
| Биржа, компании, финансовый центр | `exchange-companies.md` | `common/company_types/00_ef_companies.txt`, `common/scripted_effects/ld_listing.txt`, `common/script_values/ld_capitalization_snapshot.txt` |
| Стройка: PSC, домохозяйства, перестройка, ИИ | `construction.md` | `common/scripted_effects/PSC_scripted_effects.txt`, `common/script_values/ld_pb_overbuild_values.txt` |
| Потребности населения и товары | `pop-needs.md` | `common/pop_needs/00_ef_pop_needs.txt`, `common/buy_packages/00_ef_buy_packages.txt`, `common/goods/ef_00_goods.txt` |
| Ядро E&F: здания и PM, модификаторы, триггеры, решения, события, журналы | `ef-core.md` | `common/scripted_effects/01_economic_scripted_effects.txt`, `common/scripted_triggers/00_ef_custom_trigger.txt` |
| Интерфейс: панели, мост GUI → скрипт, отладочные окна, локализация | `interface.md` | `gui/00_ef_deported_gui_1.gui`, `common/scripted_guis/00_economic_scripted_guis.txt`, `gui/ld_money_hook.gui` |
| Генераторы файлов `ld_*` | `generators.md` | `../vic3_mods/tools/regen_ef_*.py` |
| **Реестр механизмов** — живой / выключен / мёртвый / дубль | `mechanisms.md` | — |

## Порядок шага (кратко; подробно — `entry-points.md`)
- **Старт игры:** `common/history/buildings/` → `common/history/global/` (по имени файла) → `common/history/states/`; после
  лобби — верхняя панель E&F и проход по штатам для старых сейвов; PSC запускает стройку событием.
- **Новая страна:** `new_country_var_ef` (`common/scripted_effects/10_new_country_var.txt`) — из `common/on_actions/ld_new_country_immediate_init.txt`
  и страховкой из месячного пульса; признак готовности — `var:zz_ef_country_vars_set`.
- **Месяц** (`on_monthly_pulse_country`, страны размазаны по дням): E&F `ef_on_monthly_pulse_country` (ЦБ, инфляция)
  и on_action'ы `ld_*` — банки, пузырь, капитализация, ставка ЦБ (шаг раз в 3 месяца), месячный шаг модели
  денег, перестройка PSC. Порядок между файлами on_actions движок не гарантирует.
- **Неделя:** цепочка модели денег `zz_ef_money_week_start` → зонд бюджетного тика → `zz_ef_money_model_step` (металл,
  клиринг, облигации, консоли, кредит, M0–M3, лог `EFW`) → перезапуск через 7 дней. Мост GUI → скрипт
  (`zz_ef_money_hook_receive`) приносит данные, которых нет в скрипте (утечка, сбережения, вклады).
- **Полгода / год:** ИИ-стройка E&F, колебания курсов, ИИ-форекс, арбитраж частных банков, выбор эталонной валюты (`EFE`).

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
