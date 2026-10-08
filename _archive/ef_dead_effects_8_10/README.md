# Эффекты E&F без вызовов (ночь 8.10, запас)

**Что это:** два scripted effect, которые никто не вызывал (`ld_index.py` — 0 ссылок).
- `currency_of_player_reset` (`common/scripted_effects/01_economic_scripted_effects.txt`, строки 1337–1718 до выреза) —
  обнуление глобальных `currency_of_player_is_<cur>` (95 валют). Единственный вызов — закомментированный
  `#currency_of_player_reset = yes` в `common/scripted_guis/09_ef_other.txt` (остался комментарием).
- `financial_center_respawn_after_crisis` (`common/scripted_effects/09_introduction_building_lvl.txt`, строки
  33381–33389 до выреза; параметры `FIN_CENT_SITE`, `FIN_BLDG_TYPE`, `FC_SIZE`) — восстановление финцентра после
  кризиса. Вызовы — только закомментированные блоки в том же файле (остались комментариями).

Игра их не исполняла — поведение не меняется. Удалённых вызовов и элементов GUI нет.

**Вернуть:** определение — в тот же файл (текст — по тем же путям в этой папке).
