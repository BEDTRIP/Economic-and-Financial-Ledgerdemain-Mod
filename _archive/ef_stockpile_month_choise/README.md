# Значения `<товар>_month_choise` склада

**Что делали:** ничего. 29 скрипт-значений `<товар>_month_choise = { value = var:<товар>_month_choise }` (раздел
«release» склада, `00_stockpile_scripted_value.txt`): переменную `<товар>_month_choise` никто не ставит, само значение
никто не читает (ни скрипт, ни GUI, ни локализация). Движок писал «Variable '<товар>_month_choise' is used but is never
set» (error.log каждого запуска, 29 строк).

Товары: aeroplanes, ammunition, artillery, automobiles, clothes, coal, dye, engines, explosives, fabric, fertilizer, grain,
groceries, hardwood, iron, lead, oil, opium, paper, radios, rubber, silk, small_arms, steel, sulfur, tanks, telephones,
tools, wood.

**Кто вызывал:** никто. **Интерфейс:** нет. **Удалено из живых файлов:** только 29 определений (здесь, по тому же пути,
с номером строки каждого до выноса). **Вернуть:** вставить блоки перед `<товар>_release_predicted`.
