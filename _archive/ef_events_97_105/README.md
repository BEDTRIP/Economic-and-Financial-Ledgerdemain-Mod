# События `.97 .971 .98 .981 .982` и `.100–.105`

**Что делали:** .97–.982 — скрытые (`hidden = yes`) «FEED»-события арбитража частных банков: в `immediate` `post_notification = 00_ef_economic_event_<N>_message`
(покупка/продажа валюты банком, давление на курс). Их запускал арбитраж, ныне в `_archive/ef_privat_bank_arbitrage/`. .100–.105 — кризисные события
(валютный кризис, экономический, финансовый крах, банкротство ЦБ/страны, нестабильность), пустые `immediate`. Нигде не запускаются: ни `trigger_event`/`id =`, ни `on_action`/`events`, ни журналы/решения/GUI (grep по `common/ events/ gui/`).
**Переменные:** нет. **Интерфейс:** сообщения ленты (не показывались). Живые соседи `.95/.96` и `.106/.107` не тронуты.

## Вырезано (текст — по тем же путям)
- `events/00_ef_economic_event.txt`: 11 событий от комментария `#Passagfe FEED …` до конца .105 (с заголовком `#Crisis event`).
- `common/messages/00_ef_messages.txt`: `00_ef_economic_event_97_message`, `_971_`, `_98_`, `_981_`, `_982_message`.
- `localization/{english,russian}/01_ef_event_localization_l_*.yml`: ключи `00_ef_economic_event.{97,971,98,981,982,100..105}.{t,d,f,a}` (с комментариями) и `notification_00_ef_economic_event_{97,971,98,981,982}_message_{tooltip,name,desc}`.
- Картинки событий (`gfx/event_pictures/…_96.dds`, `_100.dds` и др.) остались в `gfx/`.
