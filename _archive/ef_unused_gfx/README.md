# Графика без ссылок (E&F)

**Что это.** Картинки форка, на которые не ссылается ни один файл мода (`common/`, `events/`, `gui/`, локализация,
`.gfx` / `.asset`) ни по пути, ни через сборку пути в GUI: заготовки и старые версии автора (папки `OLD/`, `old/`,
`unuse/`, `unused/`, `Other/`), картинки событий, которых в моде нет (в т. ч. вынесенных раньше в `_archive/`: `.97`–`.105` и др.), PNG-заготовки
нейросети (`Gemini_Generated_Image_*`), архив `gfx/map/city_data.7z`. Ревизия графики R0.5 (7.10): 258 файлов,
253 МБ.

**Не вынесено, хотя ссылок по пути нет:** `gfx/loadingscreens/` (движок выбирает загрузочный экран перебором папки) и
`gfx/map/city_data/city_types/*.txt` (данные карты, читаются папкой). Совпадения имён файлов со словами в коде проверены —
случайные (ключи модификаторов, законов, локализации; пути движок берёт из определений целиком).

**Кто ссылался.** Никто: ни живой код форка, ни моды пачки в `vic3_mods` (проверено по путям 7.10).

**Вернуть.** Файл — на тот же путь без `_archive/ef_unused_gfx/` и ссылку на него в определении или GUI.

| папка | файлов | МБ |
| --- | --- | --- |
| `gfx/interface/illustrations/ef_custom_wibndows/OLD/` | 40 | 108.3 |
| `gfx/event_pictures/` | 7 | 39.3 |
| `gfx/interface/icons/production_method_icons/` | 8 | 22.3 |
| `gfx/interface/icons/law_icons/unuse/` | 16 | 8.5 |
| `gfx/interface/illustrations/institutions/` | 2 | 8.2 |
| `gfx/interface/icons/company_icons/bank/` | 19 | 7.7 |
| `gfx/interface/icons/production_method_icons/unuse/` | 60 | 7.5 |
| `gfx/interface/icons/` | 3 | 6.5 |
| `gfx/interface/icons/company_icons/` | 1 | 5.6 |
| `gfx/interface/icons/timed_modifier_icons/unuse/` | 6 | 5.1 |
| `gfx/event_pictures/unused/` | 1 | 4.7 |
| `gfx/interface/icons/goods_icons/prestige_goods/` | 2 | 4.5 |
| `gfx/interface/icons/building_icons/financial_centre/Other/` | 9 | 4.2 |
| `gfx/interface/icons/building_icons/banks/Other/` | 5 | 4.2 |
| `gfx/interface/icons/generic_icons/unuse/` | 16 | 3.9 |
| `gfx/interface/icons/alert_icons/` | 29 | 3.0 |
| `gfx/interface/illustrations/ef_custom_wibndows/currency_reserves/` | 1 | 2.3 |
| `gfx/interface/icons/timed_modifier_icons/` | 6 | 1.2 |
| `gfx/interface/icons/goods_icons/old/` | 4 | 1.1 |
| `gfx/interface/icons/invention_icons/unuse/` | 3 | 1.1 |
| `gfx/interface/icons/building_icons/other/` | 4 | 1.1 |
| `gfx/interface/icons/building_icons/` | 1 | 0.3 |
| `gfx/interface/icons/building_icons/financial_centre/` | 1 | 0.3 |
| `gfx/interface/icons/law_icons/` | 1 | 0.3 |
| `gfx/interface/icons/goods_icons/` | 1 | 0.3 |
| `gfx/interface/icons/generic_icons/` | 1 | 0.3 |
| `gfx/interface/icons/ideology_icons/` | 1 | 0.3 |
| `gfx/interface/icons/dlc_icons/` | 1 | 0.2 |
| `gfx/interface/icons/currency_icon/` | 4 | 0.2 |
| `gfx/interface/buttons/button_icons/` | 2 | 0.1 |
| `gfx/interface/icons/topbar/` | 1 | 0.1 |
| `gfx/interface/icons/notification_icons/unuse/` | 1 | 0.0 |
| `gfx/map/` | 1 | 0.0 |
