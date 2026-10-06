# ИИ-стройка E&F `ai_building_strategy` (закомментированная часть)

**Что делал:** эффект `ai_building_strategy` (`common/scripted_effects/00_on_action_main.txt`, ~3380 строк) — ИИ-стратегии покупки и
постройки зданий E&F (частные шахты, фабрики, порты, нефть и т. д.). Сами стратегии E&F вынес в `99_ai_strategies.zip`, игра
zip не читает, а вызовы в теле закомментированы: стройкой ИИ управляет PSC.

**Кто вызывал:** `ef_on_half_yearly_pulse_recurence` (`00_on_action_main.txt`) — `ai_building_strategy = yes`. Вызов и эффект остались
в моде. **Переменные, интерфейс:** нет.

**В файле остались (живое, на месте, байт в байт):** `if` по `has_technology_researched = railways` — ИИ строит частные железные дороги
(`start_privately_funded_building_construction = building_railway` в штатах с `state_market_access < 0.80`); пустые оболочки `if`
по технологиям (их содержимое было закомментировано).

**Вынесено** (`common/scripted_effects/00_on_action_main.txt`, 3304 строки): все закомментированные строки (`#`) тела эффекта и пустые
строки между ними; блок
```
if  = {
	limit = {
		has_technology_researched = shaft_mining
		bg_gold_mining_potential_lvl_to_build > 0
	}
	ai_build_privat_building_gold_mining = yes
}
```
— вызов `ai_build_privat_building_gold_mining`, эффекта с таким именем нигде нет.
Скрипт-значение `bg_gold_mining_potential_lvl_to_build` осталось (его читает отладочное окно `ef_custom_windows.gui`).

**Вернуть:** вставить строки из архивного файла обратно в тело эффекта (порядок — как в файле; эффект `ai_build_privat_building_gold_mining`
пришлось бы написать заново).
