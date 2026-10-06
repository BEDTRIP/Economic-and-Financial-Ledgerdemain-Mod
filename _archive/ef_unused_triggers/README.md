# Триггеры без ссылок в `00_ef_custom_trigger.txt` (114)

**Что делали:** 95 `law_<валюта>_monetary_system_FS_trigger` (в customizable_localization есть только варианты `_SS/_BS/_GS/_GES*`) и 19 прочих триггеров, на которые нет ссылок
(проверено счётчиком слов по `common/ events/ gui/ localization/` без комментариев — GUI-строки с `#T` в тексте учтены; динамических имён/`$param$`-шаблонов нет).
**Переменные, интерфейс:** нет.

**Прочие:** ``owner_is_player`, `has_central_bank_FS_NS_NISO`, `subject_overlord_has_central_bank`, `market_owner_is_root_with_buiding_subject_building_modifier`, `market_owner_power_bloc_leader`, `is_in_devaluation`, `is_in_revaluation`, `is_valid_country_PEU`, `is_valid_country_BOL`, `macro_facilities_on_action_ns_limit`, `country_is_in_annexable_territory_NGF`, `ai_purchase_territory_valid_NGF`, `union_latine`, `subjetc_no_modifier_on_bc`, `not_the_same_monetary_system_as_overlord`, `any_neighbouring_state_root`, `overlord_has_central_bank`, `no_indepeendeent_market_test`, `state_is_in_annexable_territory_NGF``.

**Вырезано:** определения из `common/scripted_triggers/00_ef_custom_trigger.txt` (текст — тем же путём). **Вернуть:** вставить на место.
