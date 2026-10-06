# E&F: Ledgerdemain

A Victoria 3 (1.13) mod: a fork of **Economic and Financial Mod (E&F) - V4** with **Private Sector Construction**
built in. *Ledger* — the book of accounts; *legerdemain* — sleight of hand: E&F conjured metal and money out of thin
air, Ledgerdemain books every move on both sides.

**Status:** work in progress, not published yet.

## What is different from E&F

- **Money is double-entry.** Metal and money do not appear or vanish without a counterpart: the central bank's
  reserves, the banks, the treasury, businesses and pops are accounts, and every flow between them — and between
  countries — nets out.
- **One "bank settlements" good** instead of 57 currency goods; the currencies themselves stay (laws, mints,
  exchange rates). Frees goods slots, so E&F fits next to other big mods.
- **Banks** are real buildings owned by E&F's bank companies; deposits, consols, a key rate panel, monetary policy,
  currency zones for subjects, a world clearing of payments.
- **Construction runs on PSC**: sectors make construction goods, the treasury and the investment pool pay for them;
  households buy construction too.
- Dead E&F mechanics are removed rather than patched over (metal hand-outs, private-bank arbitrages, the AI forex…),
  and E&F's error spam is being cleaned out.

## Requirements

- [1.13] Community Mod Framework ([Workshop 3385002128](https://steamcommunity.com/sharedfiles/filedetails/?id=3385002128))
- [1.13] Expanded Topbar Framework ([Workshop 3508296963](https://steamcommunity.com/sharedfiles/filedetails/?id=3508296963))

Do **not** load E&F, PSC or E&F Hotfix together with it — they are inside.

## Credits

- **Economic and Financial Mod (E&F) - V4** by **EBTX** —
  [Workshop 3143591632](https://steamcommunity.com/sharedfiles/filedetails/?id=3143591632). This repository is a fork
  of the author's code (commit `48c3f70`, 13.07.2026); the author's history is kept.
- **[1.13] Private Sector Construction** —
  [Workshop 3420714166](https://steamcommunity.com/sharedfiles/filedetails/?id=3420714166), version 1.3.7, included
  whole (files `PSC_*`, its readme — `other/PSC_README.md`).
- Russian localization of E&F and PSC — BED_TRIP
  ([Workshop 3520140574](https://steamcommunity.com/sharedfiles/filedetails/?id=3520140574)).

## Layout

- E&F's and PSC's files keep their names; files added by Ledgerdemain are named `ld_*`.
- Localization: English and Russian are complete; the other nine languages are copies of English
  (`tools/ld_loc_langs.py` of the project repo).
- `other/ld_port_manifest.txt` — the files written by the one-time port of the former E&F Hotfix into E&F's own
  bodies (FK1, 6.10.2026).

---

**Кратко по-русски.** Форк E&F со встроенным PSC: деньги и металл по двойной записи, банки-здания, ставка ЦБ,
денежная политика, клиринг, стройка через PSC; мёртвые механизмы E&F удаляются. Зависимости — CMF и ETF; E&F, PSC и
E&F Hotfix вместе с ним не подключать. Авторы оригиналов — выше.
