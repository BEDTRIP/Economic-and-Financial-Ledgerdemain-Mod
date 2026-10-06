# Годовой снимок индекса E&F

`fluctuations_country_indice_value_year` (разница индекса за год → `country_indice_value_dif_01`, при падении ниже −0,5
`financial_crash`) и `fluctuations_country_indice_value_year_clear` (обнуление `country_indice_value_dif_01`,
`base_index_value_dif`). Вызовов нет: `financial_center_ef_on_half_yearly_pulse_country` их больше не зовёт, краш считает
`ld_capitalization_crash.txt`. Переменные (`index_value_count`, `country_indice_value_1/2`, `*_dif_01`) остались —
инициализация в `history/global` и `10_new_country_var.txt`. **Удалено из живых файлов:** только определения
(`01_financial_scripted_effects.txt`, 32055–32142). **Вернуть:** вставить на место и вызвать из полугодового пульса.
