# Стартовые запасы чужих валют у ЦБ и их срез (`ef_start_fx_reserves`)

Вынуто 8.10.2026 (Хвост R1, решение пользователя). История E&F раздавала каждому ЦБ по 2,5–10 млн единиц каждой
чужой валюты (26 валют) — в масштабе E&F (оборот фунта 750 млн – 1 млрд), из ничего. Модель повторяла эти запасы
вкладами чужих ЦБ в банках эмитента: на старте срезала их до 5 % денег эмитента (`zz_ef_fx_liab_trim`) и записывала
вклады из капитала банков — капитал Британии на старте −3,0 млн, Франции −2,5, России −3,3. Теперь у ЦБ на старте чужой
валюты нет; вклад чужого ЦБ появляется только встречной проводкой (клиринг — `zz_ef_nr_dep_step`, `docs/banks.md`).

## Что делало
- `99_ef_history_global_variable.txt`, блок «CURRENCY RESERVES» (`#ok`): странам GBR, FRA, USA, RUS, AUS, PRU, NET,
  SPA, TUR, BIC и `is_valid_country_hmm` — в столичный штат `stockpiling_<cur>_state_1` += случайное `{ 2500002 10000009 }`
  по каждой из 26 валют, кроме своей (по закону валюты);
- `zz_ef_fx_liab_trim = { BASE = … }` (страна-эмитент): чужие запасы её валюты (`zz_ef_fx_liab`) не больше
  `zz_ef_fx_start_cap` (0,05) × базы, у каждого держателя в той же доле; лог `EFN|trim`. Вызовы: первый шаг модели
  (`BASE = zz_ef_start_money`) и запуск вкладов (`BASE = zz_ef_agg_m2`);
- `zz_ef_start_money` — ожидаемые деньги старта (норма сбережений + 0,33 ВВП), база первого среза;
- при запуске вкладов — `zz_ef_post = { FROM = zz_ef_bank_capital TO = zz_ef_nr_dep V = zz_ef_fx_liab_all }`.

## Удалено из живых файлов
| файл | что |
| --- | --- |
| `common/history/global/99_ef_history_global_variable.txt` | строки 2034–2418 (блок — `common/history/global/` здесь), на месте — комментарий-ссылка |
| `common/scripted_effects/ld_nr_deposits.txt` (генерат `tools/regen_ef_nr_deposits.py` в `vic3_mods`) | определение `zz_ef_fx_liab_trim`; в `zz_ef_nr_dep_step`, блок запуска — `zz_ef_fx_liab_trim = { BASE = zz_ef_agg_m2 }`, `set_variable = { name = zz_ef_t_liab_all value = zz_ef_fx_liab_all }`, `zz_ef_post = { FROM = zz_ef_bank_capital TO = zz_ef_nr_dep V = var:zz_ef_t_liab_all }` |
| `common/script_values/ld_nr_deposits_values.txt` | `zz_ef_fx_start_cap = 0.05` |
| `common/script_values/ld_money_model_values.txt` | `zz_ef_start_money` |
| `common/scripted_effects/ld_money_model.txt` | в `zz_ef_money_model_step`, блок старта (`zz_ef_parity_version` = 9) — `zz_ef_fx_liab_trim = { BASE = zz_ef_start_money }` |

## Как вернуть
Не возвращать как было: запасы без денег за ними. Если нужны исторические держатели (фунт у нескольких ЦБ), выдавать
их проводкой: металл держателя → металл ЦБ эмитента, вклад в пуле эмитента (`zz_ef_nr_dep`), а запас — зеркалом.
