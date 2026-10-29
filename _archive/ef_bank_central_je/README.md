---
type: code
description: "Журнал «Центральный банк» (`bank_je_central_1`): Журнал игрока без ЦБ: каждый месяц показывал два прогресс-бара по ВВП (currency_standards_progress_bar, central_banking_progress_bar) и выдавал технологии banking +…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_bank_central_je/**"]
---
# Журнал «Центральный банк» (`bank_je_central_1`)

**Что делал.** Журнал игрока без ЦБ: каждый месяц показывал два прогресс-бара по ВВП (`currency_standards_progress_bar`,
`central_banking_progress_bar`) и выдавал технологии `banking` + `currency_standards` при ВВП ≥ 2,5 млн,
`central_banking` — при ≥ 5 млн; завершался, когда у страны появлялось здание ЦБ E&F (`building_bank`). Остальные
журналы файла (`bank_je_central_2`, валютные) были закомментированы.

**Почему в архиве.** [[Д.R4а.3 — ЦБ появляется законом группы «Центральный банк»|Д.R4а.3]]: ЦБ основывается законом (`law_ld_cb_state` / `law_ld_cb_private`), технология
`central_banking` открывает закон; путь «технология → здание» и бесплатные технологии по ВВП больше не нужны.

**Кто вызывал.** Игра — сам журнал (`journal_entries`); других ссылок нет.

**Удалено из живых файлов.** `common/journal_entries/00_ef_bank_central_je.txt` — целиком (здесь, по тому же пути);
`common/scripted_progress_bars/00_ef_progressbar.txt` — `currency_standards_progress_bar`, `central_banking_progress_bar`
(здесь). Локализация журнала и баров (`bank_je_central_1*`, `status_central_bank_1..3`, `*_progress_bar*`) осталась в
`localization/` — без читателей, безвредна.
