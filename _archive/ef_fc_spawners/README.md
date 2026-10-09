# Самосоздание финцентров E&F

**Что делало:** `macro_facilities_on_action_fc` и `macro_facilities_fc_<x>` (38 вариантов + общий `macro_facilities_fc`)
создавали финцентр стране, у которой есть технология `financial_center` и нет финцентра
(`has_tech_financial_center_but_no_building_financial_center`), вторую биржу при своей области варианта
(`has_second_financial_center`) и заново после краха (`financial_crash_destroy_financial_center`); условие —
`macro_facilities_on_action_fc_limit` (ВВП).

**Почему вынуто (R8б, шаг 4; Д.R8.7, Д.R8б.1):** биржа одна на страну, новую учреждает только запись дневника
«Учреждение биржи».

**Удалено из живых файлов (вызовы):** `common/scripted_effects/ld_start_setup.txt` (`zz_ef_start_setup_year`: два вызова →
`zz_ef_fc_bind = yes`); `common/on_actions/00_ef_on_action.txt` (годовой пульс: два вызова и закомментированный);
`common/technology/technologies/ef_technology.txt` (`on_researched` технологии `financial_center`);
`common/scripted_effects/09_introduction_building_lvl.txt` (`reset_building`: вызов; `financial_crash_destroy_financial_center`:
последняя строка `macro_facilities_on_action_fc = yes`, тело — `zz_ef_fc_remove` по штатам с финцентром).
