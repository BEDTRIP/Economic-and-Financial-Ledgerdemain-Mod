---
type: code
description: "Возврат металла ушедшего ЦБ-штата (`zz_ef_cb_state_owner_step`): Металл ЦБ лежал на штате ЦБ (gold_state_1 / silver_state_1 с central_bank_historic_place); штат, перешедший к другой стране (восстание, война), уносил его. Каждую неделю…"
project: vic3
tags: [форк, архив]
paths: ["_archive/ld_cb_state_owner/**"]
---
# Возврат металла ушедшего ЦБ-штата (`zz_ef_cb_state_owner_step`)

**Что делал.** [[Металл]] ЦБ лежал на штате ЦБ (`gold_state_1` / `silver_state_1` с `central_bank_historic_place`); штат,
перешедший к другой стране (восстание, война), уносил его. Каждую неделю шаг страны искал свои ЦБ-штаты с чужим
владельцем (`var:zz_ef_cb_owner`), переносил их металл в столицу прежнего владельца (делая её ЦБ-штатом) и обнулял, лог
`EFM|…|cb_state_lost`.

**Почему в архиве.** [[Д.R4а.2 — Счета денежной власти|Д.R4а.2]]: металл денежной власти — счета страны `zz_ef_am_gold` / `zz_ef_am_silver`; штат его больше
не держит, уносить нечего.

**Кто вызывал.** `zz_ef_money_model_step` (`common/scripted_effects/ld_money_model.txt`) — строка
`zz_ef_cb_state_owner_step = yes` (на её месте теперь `zz_ef_am_sweep = yes`).

**Переменные.** `zz_ef_cb_owner` (штат) — осталась без писателя и читателя; scope `zz_ef_lost_cb_state`.

**Удалено из живых файлов.** `common/scripted_effects/ld_subject_metal.txt` — шапка файла и определение
`zz_ef_cb_state_owner_step` (`common/scripted_effects/ld_subject_metal.txt` здесь); вызов в `ld_money_model.txt` (см.
выше). Интерфейса не было.
