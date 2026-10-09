# Проба R8а.7: тег страны и `Localize(Concatenate(...))` в строке

**Что делало:** событие `ld_probe_tag.1` (только из консоли) писало в `debug.log` строку `EFZ|<GetTagName>|<имя>|<Concatenate('a', 'b')>|<Localize(Concatenate('zz_ef_iso2_', тег))>|`
у GBR, RUS, SWI, USA; ключи `zz_ef_iso2_<тег>` — `localization/*/ld_probe_tag_l_*.yml`.

**Итог (прогон r1009_032419):** `EFZ|GBR|Великобритания|ab|GB|`, `RUS … RU`, `SWI … CH`, `USA … US` — `Country.GetTagName`
отдаёт тег, строка собирает ключ локализации. На этом стоит символ валюты (`regen_ld_currency_symbol.py`), ключи
`zz_ef_iso2_<тег>` теперь пишет он.

**Вырезано:** `events/ld_probe_tag_events.txt`, `localization/<11 языков>/ld_probe_tag_l_<язык>.yml` (здесь — английский);
строка `EFZ` из таблицы логов `docs/entry-points.md`.
