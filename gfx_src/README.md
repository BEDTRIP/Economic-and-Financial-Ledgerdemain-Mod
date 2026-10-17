# gfx_src — исходники графики мода

Одна картинка мода — карточка `<вид>/<имя>.toml` и выбранный исходник `<вид>/<имя>.png` в полном размере (Д.R10.16).
Варианты, из которых выбирали, — `<имя>.variants/`, вне git. Источник стиля — ваниль (Д.R10.13); значки — по одному
вместе с пользователем (Д.R10.15).

```
v3 gfx new  gfx_src/goods/<имя>.toml --kind goods --target gfx/interface/icons/goods_icons/<имя>.dds --prompt "..."
v3 gfx gen  gfx_src/goods/<имя>.toml --repeat 4    # варианты Q1…Q4 (Qwen 2.1), K1…K4 (FLUX.2 klein) + лист
v3 gfx pick gfx_src/goods/<имя>.toml Q3            # выбранный → <имя>.png (с прозрачностью, если вид требует)
v3 gfx build --mod .                               # все карточки → DDS в gfx/ (как у ванили: BGRA8 с мипами)
v3 gfx check gfx/interface/icons/goods_icons/<имя>.dds
```

Виды, их размеры и доводка — `vic3_tools/vic3tools/gfx/cards.py`; разбор ванили — `этапы/R10.md`, «Виды графики».
