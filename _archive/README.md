# Архив мёртвых механизмов

Механизмы E&F / PSC / `ld_*`, которые ни на что не влияли (не вызывались или были заглушены), — вынуты из мода, чтобы
игра их не читала, и сохранены здесь на случай, если пригодятся. Игра эту папку не грузит; в живую копию и мастерскую
она не попадает. Не нужен — папку механизма можно удалить.

Правила — `CLAUDE.md` форка, раздел «Мёртвое — `_archive/`». Устройство папки механизма:

```
_archive/<механизм>/
  README.md                 что делал; кто вызывал; переменные; интерфейс; удалённые вызовы и элементы GUI (файл, ключ, текст)
  common/.../<файл>.txt     вырезанные определения, по исходному пути (в начале — откуда, строки)
  gui/..., localization/... то же для GUI и локализации
```

## Механизмы

| механизм | папка | что удалено из живых файлов |
| --- | --- | --- |
| Архивы `.zip`/`.rar` E&F (старый ИИ-форекс, ИИ-стратегии, PM, события) | `ef_zip_archives/` | ничего — файлы целиком |
| Резервные копии `.backup` GUI и локализации | `ef_backups/` | ничего — файлы целиком |
| Рабочие остатки автора: `test.txt`, `00_ef_dev_tips.gui`, дубль `.yaml`, генераторы `nw_*.py` | `ef_dev_leftovers/` | ничего — файлы целиком |
| Месячная раздача/покупка металла ЦБ: `storing_gold_1`/`storing_silver_1`, пустая обёртка `stockpiling_central_bank_metal_reserves_state`, `zz_ef_cb_metal_purchase_step` | `ef_cb_metal_reserves_storing/` | вызов обёртки в `00_on_action_main.txt`; три определения из `01_economic_scripted_effects.txt`; файл `ld_cb_stockpile_track.txt` |
| Разовый пересчёт металла субъектов `zz_ef_subject_metal_step` (+ `zz_ef_metal_in_gold`, `zz_ef_metal_target_in_gold`) | `ef_subject_metal_step/` | определение из `ld_subject_metal.txt`, два значения из `ld_reference_currency_values.txt` |
| Значения денежной модели без ссылок (25 штук) | `ef_unused_money_values/` | определения из `ld_money_model_values.txt` |
| Заказы запаса за золото (`*_order_in_gold`) и `buy_<g>_budget_panel` | `ef_stockpile_gold_orders/` | 58 блоков `if` в `01_stockpile_scripted_effects.txt`; 29 scripted_gui в `00_stockpile_scripted_guis.txt` |
| Перемасштаб валютных запасов `zz_ef_fx_stock_rescale` | `ef_fx_stock_rescale/` | файл `ld_fx_stock_rescale.txt`; закомментированный вызов в `ld_money_model.txt` |
| Хронометрия чеканки ЦБ (`zz_ef_mint_*`) | `ef_mint_timing/` | 7 значений из `ld_money_model_values.txt` (обнуления `zz_ef_f_mint*` остались — их читают логи) |
| Деньги за металл по Юму (`zz_ef_hume_money_on`) | `ef_hume_money/` | ветка `if` в `zz_ef_cb_hume_step`; два значения |
| Зонды EFJ / EFD | `ef_probes_efj_efd/` | два вызова и два эффекта в `ld_money_model.txt`; 4 значения |
| Пустой модификатор `zz_ef_business_cash` | `ef_business_cash_modifier/` | файл `ld_business_cash.txt`; снятие в `zz_ef_money_week_start` |
| Проверочные значения валют (`money_supply_verification_<cur>`, `sell_<cur>_market_panel_verification`, `buy_<cur>_order`, `*_spe_to_add_*`, `buy_/sell_<cur>_market_panel` и др.) | `ef_currency_verification_values/` | 765 определений из `01_economic_currency_scripted_value.txt` (252 626 строк) |
| Значения и триггер валют без ссылок (`zz_ef_reserves_money`, `*_neg`, `zz_ef_cb_rule_*_pp`, `is_valid_country_for_currency_accumulation`) | `ef_unused_currency_values/` | 6 значений из `ld_reference_currency_values.txt` / `ld_cb_rate_values.txt`, триггер из `00_ef_custom_trigger.txt` |
| Остатки выдачи местной валюты (`zz_ef_local_currency_*`, `zz_ef_lc_curve_*`) | `ef_local_currency_issuance/` | четыре файла `ld_local_currency_*` целиком (в т.ч. on_action очистки модификатора) |
| Контроллер ставки E&F `base_rate_change` | `ef_base_rate_change/` | пустое определение из `01_economic_scripted_effects.txt`; вызов (`if is_ai`) в `00_on_action_main.txt` |
