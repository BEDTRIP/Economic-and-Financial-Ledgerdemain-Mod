---
type: code
description: "Перевод казны в металл ЦБ (`transfer_gold_to_central_bank_metal_reserves`): Раздел «Перевод казны в металлические резервы ЦБ» в Бюджет → Экономика (при металлическом стандарте и технологии денежной политики): кнопки ± меняли сумму…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ef_treasury_metal_transfer/**"]
---
# Перевод казны в металл ЦБ (`transfer_gold_to_central_bank_metal_reserves`)

**Что делал.** Раздел «Перевод казны в металлические резервы ЦБ» в Бюджет → Экономика (при металлическом стандарте и
технологии денежной политики): кнопки ± меняли сумму `var:transfer_gold_to_central_bank_metal_reserves` (шаг 10 млн, старт
10 млн), «Перевод» списывал её с казны и добавлял металл в штат ЦБ (`silver_state_1` / `gold_state_1` столичного
ЦБ-штата, `transfer_gold_to_central_bank_metal_reserves_sc` = сумма × `money_value`) — металл из ничего, сверка металла
его не знала.

**Почему в архиве.** [[Д.R4а.13 — Кубышка — металлический счёт казны|Д.R4а.13]]: у казны своя кубышка металла — купить и продать на рынке через «Банки», сдать денежной
власти по паритету, выкупить у неё (`scripted_effects/ld_treasury_metal.txt`, блок «Кубышка казны» в той же панели).

**Удалено из живых файлов.**
- `gui/ld_economy_panel.gui` — раздел `#transfer_government_treasury_to_central_bank_metal_reserves` (кнопка раздела,
  тексты, кнопки ±, «Перевод»), здесь по тому же пути.
- `common/scripted_guis/00_economic_scripted_guis.txt` — `transfer_gold_to_central_bank_metal_reserves_increase`,
  `_reduce`, `transfer_gold_to_central_bank_metal_reserves`, `_visible`.
- `common/script_values/00_economic_scripted_value.txt` — `transfer_gold_to_central_bank_metal_reserves_sc`.
- `common/scripted_effects/10_new_country_var.txt` — начальное `set_variable` `transfer_gold_to_central_bank_metal_reserves`.

Локализация раздела (`transfer_government_treasury_to_central_bank_metal_reserves*`, `Transfert`) осталась — без
читателей.
