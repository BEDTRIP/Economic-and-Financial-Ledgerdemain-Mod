# Пустой модификатор zz_ef_business_cash

**Что делал.** EF.48, прогон 13: ежемесячный модификатор снижал потолок кассы зданий на 85%; потом потолок перенесён в `base_values` (INJECT в E&F/TGR/VC), а модификатор оставлен
пустым только затем, чтобы сохранения, где он есть, грузились; `zz_ef_money_week_start` снимал его каждый месяц.
**Кто вызывал.** Снятие в `zz_ef_money_week_start`. **Переменные.** Нет. **Интерфейс.** Только название/описание в локализации (модификатор нигде не показывается, пока пуст).

**Что лежит здесь**
- `common/static_modifiers/ld_business_cash.txt` — файл целиком.
- `common/scripted_effects/ld_money_model.txt` — блок снятия (6 строк).

**Удалено из живых файлов.** `ld_money_model.txt`, начало `zz_ef_money_week_start`: комментарий «Business cash at ~0.3 GDP …» и
`if = { limit = { has_modifier = zz_ef_business_cash } remove_modifier = zz_ef_business_cash }`. В `common/defines/zzzz_ef_credit_def.txt` в комментарии ссылка на файл заменена на «the cash cap in base_values».
**Оставлено.** Ключи `zz_ef_business_cash` и `zz_ef_business_cash_desc` в `localization/<язык>/ld_cb_rate_panel_l_<язык>.yml` — файл ведёт генератор `regen_ef_cb_rate_loc`; ключи убирать в генераторе.
**Вернуть.** Файл — на место, блок — в начало `zz_ef_money_week_start`. Сохранения, где модификатор ещё висит на стране, после выноса файла могут дать ошибку «static modifier не найден» в логе (при старте новой игры не бывает).

Ключи локализации `zz_ef_business_cash`, `zz_ef_business_cash_desc` вынуты из `localization/<lang>/ld_cb_rate_panel_l_<lang>.yml` (en, ru — в архиве; девять языков — копия en) и из генератора `regen_ef_cb_rate_loc` (`vic3_mods/tools`). Вернуть — вернуть ключи в генератор.
