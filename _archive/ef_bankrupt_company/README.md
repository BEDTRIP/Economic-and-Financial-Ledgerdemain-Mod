---
type: code
description: "Банкротство компаний E&F `bankrupt_company`: Вызывался из последствий кризисов E&F — financial_crash_consequences и economic_crisis_consequences (01_financial_scripted_effects.txt): по жёсткому списку из ~300 типов…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_bankrupt_company/**"]
---
# Банкротство компаний E&F `bankrupt_company`

**Что делал.** Вызывался из последствий кризисов E&F — `financial_crash_consequences` и `economic_crisis_consequences`
(`01_financial_scripted_effects.txt`): по жёсткому списку из ~300 типов компаний (`company_basic_*`, исторические)
удалял компанию страны (`remove_company`), если её процветание ниже 100. Деньги, уровни, держатели не учитывались.

**Почему в архиве.** [[Д.R6.4 — Банкротство компании|Д.R6.4]] (пользователь 13.10): своё банкротство компании — R11 (вместе с кризисами и счётом компании
[[Д.R6.2 — Счёт компании|Д.R6.2]]).

**Удалено из живых файлов:**
- `common/scripted_effects/01_financial_scripted_effects.txt` — определение `bankrupt_company` (строки 20357–23526);
- там же — два вызова `#faillite des entreprise` / `bankrupt_company = yes #-> à revoir` (в `financial_crash_consequences`
  и `economic_crisis_consequences`, строки 20187–20188 и 20272–20273).
