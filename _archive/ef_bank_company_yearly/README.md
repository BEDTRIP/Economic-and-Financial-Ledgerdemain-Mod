# Ежегодная раздача ИИ банковских компаний E&F (Д.R4б.3, аудит Ч10)

**Что делало:** в годовом пульсе страны (`central_bank_ef_on_yearly_pulse_country`, `common/scripted_effects/
00_on_action_main.txt`) ИИ-стране — `establish_bank_and_ef_compagnie`: исторические компании E&F по датам (банки,
Ротшильды, а также Krupp, Thonet, Ricordi, GWR и др.) — `add_company` сверх предела компаний и в подарок 10 уровней
стройсектора (или торговый центр, рудник) в собственность компании.

**Почему в архив:** Д.R4б.3 — банки — стартовые и основанные обычным путём игры; подарки уровней к тому же делают
`company_owned_levels` банковской компании непригодным для уровней «Банка» (В.R4б.8).

**Вырезано из живых файлов:** `common/scripted_effects/00_on_action_main.txt`, `central_bank_ef_on_yearly_pulse_country`:
```
	if  = {
		limit = {
			is_ai = yes
			#maximum_number_companies_exceeded_monthly_pulse >= 1
		}
		establish_bank_and_ef_compagnie = yes
	}
```
Сама `establish_bank_and_ef_compagnie` (`01_financial_scripted_effects.txt`) жива — её зовёт история старта
(`common/history/buildings/00_ef_building.txt`, начало и конец `BUILDINGS`): стартовые компании (вопрос В.R4б.10).
