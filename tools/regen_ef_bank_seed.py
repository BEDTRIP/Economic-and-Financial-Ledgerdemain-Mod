#!/usr/bin/env python3
"""
Д2.4 (5.10.2026) -- the banks' seed: scripted_effects/ld_bank_seed.txt of the fork «E&F: Ledgerdemain» (via ld_gen:
written by entry keys).

Banks (building_zz_ef_bank) make the bank settlements (the former E&F currency good) that used to come from the
central bank from day one. The user (5.10): enough banks to cover the initial demand; spread over the states with
trade centres, not only the capital; owned by the population and by companies.

How (once per market, by its owner, in the owner's first monthly pulse):
  * levels wanted L = (the market's buy orders of liquidity_currency x 1.2 - its sell orders) / 500 (Д2.8, 5.10: the
    counting house's 500 a level -- a new bank starts with the money changer, 300, and the AI moves it to a counting
    house where there is paper; until 5.10 the divisor was 300 and the seed overshot; the sell orders are what trade
    centres already make -- they produce settlements too);
  * spread over the market's states (every country on the market) by their trade centre levels; a market with no
    trade centre -- the owner's capital;
  * in each state one create_building, the largest ladder size not above its share (calling create_building
    again on a standing building adds no levels -- run r1005_192418);
  * owners: 40% an E&F bank company of the state's owner if it has one, the rest the state -- sold by the AI to
    private owners (ai_nationalization_desire -5 on the building; run r1005_194935: in a year and a half 339 of
    1097 state levels went to financial districts and companies). A company type cannot be a variable, so the
    company is a macro argument: one ladder per bank company (the 94 of zz_ef_cm_companies.txt).
    The financial district cannot be the seed's owner: it needs a literal region -- `region = scope:...` is
    refused ("Failed to read key reference", run r1005_201105), and the state's region would take a dispatcher of
    ~700 regions x 98 companies x the ladder.
Reads the fork: the bank companies are the ones of common/company_types/00_ef_companies.txt that list
building_zz_ef_bank (the 94).
Logged per state: EFK|date|country|state|want N|tc T|built B.

Usage:
    py tools/regen_ef_bank_seed.py            # write
    py tools/regen_ef_bank_seed.py --check    # exit 1 if the fork file differs
"""

from __future__ import annotations

import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))  # tools/ of the fork; two levels under Projects/vic3, like vic3_mods/tools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ld_gen  # noqa: E402

OUT = "common/scripted_effects/zz_ef_bank_seed.txt"      # путь хотфикса; ld_gen пишет в форк ld_bank_seed.txt
COMPANIES = os.path.join(ld_gen.FORK, "common", "company_types", "00_ef_companies.txt")

BANKS = [
    "company_BancoNacionArgentina",
    "company_BancoProvincia",
    "company_OesterreichischeNationalbank",
    "company_BayerischeHypothekenUndWechselBank",
    "company_BanqueNationaleDeBelgique",
    "company_ImperialBankofIndia",
    "company_BancoNacionalDeBolivia",
    "company_BancoDoBrasil",
    "company_CanadianImperialBankOfCommerce",
    "company_DaQingBank",
    "company_BankHSBC",
    "company_BancoEstado",
    "company_BancoDeValparaiso",
    "company_BancoRepublicaColombia",
    "company_BancoCentralDeCostaRica",
    "company_BancoEspanolDeLaHabana",
    "company_LandmandsBanken",
    "company_BanqueEgyptienne",
    "company_BanqueDeFrance",
    "company_BankofEngland",
    "company_Reichsbank",
    "company_PreussischeSeehandlung",
    "company_bankofgreec",
    "company_BancoCentralDeGuatemala",
    "company_BancoCentralDeHonduras",
    "company_BancaDItalia",
    "company_BankOfJapan",
    "company_Mitsubishiexchangehousebank",
    "company_BancoDeMexico",
    "company_DeNederlandscheBank",
    "company_ChristianiaBank",
    "company_ColonialBankOfAustralia",
    "company_RoyalBankofCanada",
    "company_BancoNacionalDePanama",
    "company_BankMelliIran",
    "company_ImperialBankofPersia",
    "company_BancoDePortugal",
    "company_BancoNacionalDelParaguay",
    "company_BankOfMontreal",
    "company_StateBankRussianEmpire",
    "company_BankSBoBSA",
    "company_CassaDiRisparmioDiTorino",
    "company_BankofSpain",
    "company_HandelsBanken",
    "company_Bankenverein",
    "company_OttomanBank",
    "company_BancoCentralDelUruguay",
    "company_BancoCentralDeVenezuela",
    "company_BankJPMorgan",
    "company_BankGoldmanSachs",
    "company_ChaseBank",
    "company_BankWellsFargo",
    "company_BankAmericanExpress",
    "company_amsterdamschebank",
    "company_RotterdamscheBankvereeniging",
    "company_SocieteGeneraledeBelgique",
    "company_BanqueDeBruxelles",
    "company_BancoDeBilbao",
    "company_BancoHispanoColonial",
    "company_BancoCommercialPortugues",
    "company_Bank_Ultramarino",
    "company_BancaCommercialeItaliana",
    "company_LloydsBank",
    "company_barclaysBank",
    "company_NationalWestminsterBank",
    "company_RoyalBankOfScotland",
    "company_Rothschild_Bank_gbr",
    "company_BankCreditLyonnais",
    "company_SocieteGenerale",
    "company_BanqueDeParisEtDesPaysBas",
    "saint_petersburg_international_commercial_bank",
    "russo_chinese_bank",
    "company_DeutscheBank",
    "company_OesterreichischeCreditAnstalt",
    "company_WienerBankverein",
    "company_TurkishZiraatBankasi",
    "company_BanqueImperialeOttomane",
    "company_BankTejaratPersia",
    "company_BankAngloPersian",
    "company_ChohungBank",
    "company_BankIBC",
    "company_BankBOCOM",
    "company_SumitomoBank",
    "company_BankOfIndiaCompany",
    "company_BankOfBombay",
    "company_BankDesjardins",
    "company_NationalBankOfAustralia",
    "company_SouthAustralianBank",
    "company_bancodelondresmexico",
    "company_BancoMercantilMexicano",
    "company_BancoMercantil",
    "company_BancoCommercialDoBrasil",
    "company_BancoHipotecarioNacional",
    "company_BancoDeChile",
]

# Д.R9б.6, Д.R4а.10: the central banks among the bank companies -- the country's CB company is the first of these it
# has; a country with none of them -- its first bank company in BANKS' order (принято ночью, проверить)
CB_COMPANIES = [
    "company_BankofEngland", "company_BanqueDeFrance", "company_OesterreichischeNationalbank",
    "company_DeNederlandscheBank", "company_BankofSpain", "company_BancoDePortugal", "company_StateBankRussianEmpire",
    "company_Reichsbank", "company_PreussischeSeehandlung", "company_BancaDItalia", "company_BankOfJapan",
    "company_BanqueNationaleDeBelgique", "company_BancoDeMexico", "company_BancoCentralDelUruguay",
    "company_BancoCentralDeCostaRica", "company_BancoCentralDeGuatemala", "company_BancoCentralDeHonduras",
    "company_BancoCentralDeVenezuela", "company_BancoDoBrasil", "company_BancoNacionArgentina",
    "company_BancoNacionalDeBolivia", "company_BancoRepublicaColombia", "company_BancoNacionalDePanama",
    "company_BancoNacionalDelParaguay", "company_BankMelliIran", "company_DaQingBank", "company_ImperialBankofIndia",
    "company_bankofgreec", "company_BanqueEgyptienne", "company_BanqueImperialeOttomane", "company_BancoEstado",
]
# a bank company's own "Bank" at the start (Д.R9б.6): levels, in a state where no other "Bank" stands
COMPANY_LEVELS = 5
# a bank company's presence abroad at the start (Д.R9а.5): its "Bank" levels in another country's state -- the company,
# its country, the states (country, state region); in the capital of a country with its own CB company both own the
# one "Bank" (create_building on a standing building adds no levels)
PRESENCE = [
    ("company_Rothschild_Bank_gbr", "GBR", [("FRA", "STATE_ILE_DE_FRANCE"), ("AUS", "STATE_AUSTRIA"),
                                            ("FRM", "STATE_HESSE"), ("SIC", "STATE_CAMPANIA")]),
]

SIZES = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 22, 26, 30, 35, 40, 50, 60, 70, 80, 100, 120, 150, 200]
COMPANY_SHARE = 0.4

HEADER = """\
# GENERATED by tools/regen_ef_bank_seed.py -- do not edit by hand.
#############################################
# the banks' seed, once per market, by its owner (on_actions/zz_ef_bank_on_actions.txt):
# bank settlements (the former currency good) used to come from the central bank from day one. Levels = (the
# market's buy orders x 1.2 - sell orders, trade centres make some) / 500, spread over the market's states by trade centre levels; owners 40% the owner's
# E&F bank company, the rest the state (the AI sells it to private owners). Why so: the generator's docstring.
#############################################

"""


def banks() -> list[str]:
    """BANKS (the order is the seed's: the first company the owner has gets the bank), checked against the fork's
    00_ef_companies.txt: exactly its companies that list building_zz_ef_bank."""
    s = open(COMPANIES, encoding="utf-8-sig").read()
    found = set()
    for m in re.finditer(r"(?m)^(\w+)\s*=\s*\{", s):
        nxt = re.search(r"(?m)^\S", s[m.end():])
        body = s[m.end(): m.end() + nxt.start()] if nxt else s[m.end():]
        if re.search(r"(?m)^\s*building_zz_ef_bank\b", body):
            found.add(m.group(1))
    assert found == set(BANKS) and len(BANKS) == 94, (found ^ set(BANKS))
    return BANKS


def split(size: int, with_company: bool) -> tuple[int, int]:
    """(company, state) levels."""
    if not with_company:
        return 0, size
    c = int(size * COMPANY_SHARE)
    return c, size - c


def ladder(owner_block) -> str:
    """Flat if/else_if over SIZES (largest first) on scope:zz_ef_bank_s.var:zz_ef_bank_n -- state scope."""
    out = []
    for i, size in enumerate(sorted(SIZES, reverse=True)):
        kw = "if" if i == 0 else "else_if"
        out.append(f"\t{kw} = {{\n\t\tlimit = {{ var:zz_ef_bank_n >= {size} }}\n"
                   f"\t\tcreate_building = {{\n\t\t\tbuilding = building_zz_ef_bank\n\t\t\treserves = 0\n"
                   f"\t\t\tadd_ownership = {{\n{owner_block(size)}\t\t\t}}\n\t\t}}\n\t}}\n")
    return "".join(out)


def company(levels: int) -> str:
    return ("\t\t\t\tcompany = {\n\t\t\t\t\ttype = $COMPANY$\n\t\t\t\t\tcountry = scope:zz_ef_bank_o\n"
            f"\t\t\t\t\tlevels = {levels}\n\t\t\t\t}}\n")


def country(levels: int) -> str:
    return f"\t\t\t\tcountry = {{\n\t\t\t\t\tcountry = scope:zz_ef_bank_o\n\t\t\t\t\tlevels = {levels}\n\t\t\t\t}}\n"


def with_company_block(size: int) -> str:
    c, f = split(size, True)
    return (company(c) if c else "") + country(f)


def build() -> str:
    keys = banks()
    o = [HEADER]

    # market owner: the market's levels and trade centre weight, then every state of the market
    o.append("""\
### COUNTRY scope (the market owner), monthly; once.
zz_ef_bank_seed_step = {
	if = {
		limit = {
			NOT = { has_variable = zz_ef_bank_seeded }
			exists = market
			market.owner = this
		}
		set_variable = zz_ef_bank_seeded
		save_scope_as = zz_ef_bank_m
		set_variable = {
			name = zz_ef_bank_l
			value = {
				value = market.mg:liquidity_currency.market_goods_buy_orders
				multiply = 1.2
				subtract = market.mg:liquidity_currency.market_goods_sell_orders
				min = 0
				divide = 500
			}
		}
		set_variable = { name = zz_ef_bank_w value = 0 }
		# the states where a bank company's own "Bank" stands are left out: create_building on a standing building adds
		# no levels (Д.R9б.6)
		every_country = {
			limit = { exists = market market.owner = scope:zz_ef_bank_m }
			every_scope_state = {
				limit = { NOT = { has_building = building_zz_ef_bank } }
				scope:zz_ef_bank_m = { change_variable = { name = zz_ef_bank_w add = prev.zz_ef_bank_tc_levels } }
			}
		}
		if = { limit = { zz_ef_logs_on = yes } debug_log = "EFK|[TimeKeeper.GetCurrentDate.GetString]|[THIS.GetCountry.GetNameNoFormatting]|market|levels [THIS.GetCountry.MakeScope.Var('zz_ef_bank_l').GetValue|1]|tc [THIS.GetCountry.MakeScope.Var('zz_ef_bank_w').GetValue|0]" }
		if = {
			limit = { var:zz_ef_bank_w > 0 }
			every_country = {
				limit = { exists = market market.owner = scope:zz_ef_bank_m }
				every_scope_state = {
					limit = {
						zz_ef_bank_tc_levels > 0
						NOT = { has_building = building_zz_ef_bank }
					}
					set_variable = {
						name = zz_ef_bank_n
						value = {
							value = scope:zz_ef_bank_m.var:zz_ef_bank_l
							multiply = zz_ef_bank_tc_levels
							divide = scope:zz_ef_bank_m.var:zz_ef_bank_w
						}
					}
					zz_ef_bank_seed_state = yes
				}
			}
		}
		else_if = {
			limit = { capital = { NOT = { has_building = building_zz_ef_bank } } }
			capital = {
				set_variable = { name = zz_ef_bank_n value = scope:zz_ef_bank_m.var:zz_ef_bank_l }
				zz_ef_bank_seed_state = yes
			}
		}
		else_if = {
			limit = { any_scope_state = { NOT = { has_building = building_zz_ef_bank } } }
			random_scope_state = {
				limit = { NOT = { has_building = building_zz_ef_bank } }
				set_variable = { name = zz_ef_bank_n value = scope:zz_ef_bank_m.var:zz_ef_bank_l }
				zz_ef_bank_seed_state = yes
			}
		}
	}
}

### STATE scope, var:zz_ef_bank_n = the levels wanted here.
zz_ef_bank_seed_state = {
	if = {
		limit = { var:zz_ef_bank_n >= 1 }
		save_scope_as = zz_ef_bank_s
		owner = { save_scope_as = zz_ef_bank_o }
		owner = { set_variable = zz_ef_bank_nocomp }
""")
    for k in keys:
        o.append(f"""\
		if = {{
			limit = {{ owner = {{ has_variable = zz_ef_bank_nocomp has_company = company_type:{k} }} }}
			owner = {{ remove_variable = zz_ef_bank_nocomp }}
			zz_ef_bank_seed_company = {{ COMPANY = {k} }}
		}}
""")
    o.append("""\
		if = {
			limit = { owner = { has_variable = zz_ef_bank_nocomp } }
			owner = { remove_variable = zz_ef_bank_nocomp }
			zz_ef_bank_seed_state_owned = yes
		}
		if = {
			limit = { NOT = { has_building = building_zz_ef_bank } }
			zz_ef_bank_seed_state_owned = yes
		}
		if = { limit = { zz_ef_logs_on = yes } debug_log = "EFK|[TimeKeeper.GetCurrentDate.GetString]|[THIS.GetState.GetOwner.GetNameNoFormatting]|[THIS.GetState.GetNameNoFormatting]|want [THIS.GetState.MakeScope.Var('zz_ef_bank_n').GetValue|1]|tc [THIS.GetState.MakeScope.ScriptValue('zz_ef_bank_tc_levels')|0]|built [THIS.GetState.MakeScope.ScriptValue('zz_ef_bank_levels')|0]" }
	}
	remove_variable = zz_ef_bank_n
}

""")
    o.append("### STATE scope; $COMPANY$ = an E&F bank company of the owner.\nzz_ef_bank_seed_company = {\n")
    o.append(ladder(with_company_block))
    o.append("}\n\n### STATE scope; no bank company (and the fallback): state-owned, sold by the AI.\nzz_ef_bank_seed_state_owned = {\n")
    o.append(ladder(lambda s: country(s)))
    o.append("}\n\n")
    o.append(company_seed(keys))
    return "".join(o)


def company_seed(keys: list[str]) -> str:
    """Д.R9б.6 (Д.R4а.10): at the start (history, after the companies are added) every bank company of the country
    gets its own "Bank" -- COMPANY_LEVELS levels in a state where no other "Bank" stands: the CB company
    (var:zz_ef_cb_co) in the capital, the others in a random incorporated state. A company lives only while it owns
    levels; E&F gave each one level in a random state, and a second company there got none (create_building on a
    standing building adds no levels), so most of them were gone at the start."""
    cbs = [k for k in CB_COMPANIES if k in keys]
    o = ["""### COUNTRY scope, history (history/buildings/00_ef_building.txt, after the companies): the bank companies' own
### "Banks" (Д.R9б.6) and the CB company var:zz_ef_cb_co (Д.R4а.10), its "Bank"'s state var:zz_ef_cb_bank_state.
zz_ef_bank_company_seed = {
	save_scope_as = zz_ef_bkc_o
"""]
    chain = cbs + [k for k in keys if k not in cbs]
    for i, k in enumerate(chain):
        kw = "if" if i == 0 else "else_if"
        o.append(f"""	{kw} = {{
		limit = {{ has_company = company_type:{k} }}
		set_variable = {{ name = zz_ef_cb_co value = company:{k} }}
		set_variable = zz_ef_bkc_cb_{k}
		capital = {{
			zz_ef_bank_company_build = {{ COMPANY = {k} }}
			owner = {{ set_variable = {{ name = zz_ef_cb_bank_state value = prev }} }}
		}}
	}}
""")
    for k in keys:
        o.append(f"""	if = {{
		limit = {{ has_company = company_type:{k} }}
		if = {{
			limit = {{ has_variable = zz_ef_bkc_cb_{k} }}
			remove_variable = zz_ef_bkc_cb_{k}
		}}
		else = {{
			zz_ef_bank_company_state = {{ COMPANY = {k} }}
		}}
	}}
""")
    for co, tag, states in PRESENCE:
        for t, st in states:
            o.append(f"""\t# presence (Д.R9а.5): {co} of {tag} in {st}, if no "Bank" of the country took it already
\tif = {{
\t\tlimit = {{
\t\t\tthis = c:{t}
\t\t\texists = c:{tag}
\t\t\tc:{tag} = {{ has_company = company_type:{co} }}
\t\t\texists = s:{st}.region_state:{t}
\t\t\ts:{st}.region_state:{t} = {{ NOT = {{ has_building = building_zz_ef_bank }} }}
\t\t}}
\t\ts:{st}.region_state:{t} = {{
\t\t\tcreate_building = {{
\t\t\t\tbuilding = building_zz_ef_bank
\t\t\t\treserves = 0
\t\t\t\tadd_ownership = {{
\t\t\t\t\tcompany = {{
\t\t\t\t\t\ttype = {co}
\t\t\t\t\t\tcountry = c:{tag}
\t\t\t\t\t\tlevels = {COMPANY_LEVELS}
\t\t\t\t\t}}
\t\t\t\t}}
\t\t\t}}
\t\t}}
\t}}
""")
    o.append("""}

### COUNTRY scope; $COMPANY$ -- a bank company of the country: its "Bank" in a state without one (incorporated first).
zz_ef_bank_company_state = {
	if = {
		limit = { any_scope_state = { is_incorporated = yes NOT = { has_building = building_zz_ef_bank } } }
		random_scope_state = {
			limit = { is_incorporated = yes NOT = { has_building = building_zz_ef_bank } }
			zz_ef_bank_company_build = { COMPANY = $COMPANY$ }
		}
	}
	else_if = {
		limit = { any_scope_state = { NOT = { has_building = building_zz_ef_bank } } }
		random_scope_state = {
			limit = { NOT = { has_building = building_zz_ef_bank } }
			zz_ef_bank_company_build = { COMPANY = $COMPANY$ }
		}
	}
}

### STATE scope; scope:zz_ef_bkc_o -- the country. In a state of a foreign company's presence (PRESENCE) -- one "Bank" of both.
zz_ef_bank_company_build = {
""")
    first = True
    for co, tag, states in PRESENCE:
        for t, st in states:
            o.append(f"""\t{'if' if first else 'else_if'} = {{
\t\tlimit = {{
\t\t\tstate_region = s:{st}
\t\t\tscope:zz_ef_bkc_o = c:{t}
\t\t\texists = c:{tag}
\t\t\tc:{tag} = {{ has_company = company_type:{co} }}
\t\t}}
\t\tcreate_building = {{
\t\t\tbuilding = building_zz_ef_bank
\t\t\treserves = 0
\t\t\tadd_ownership = {{
\t\t\t\tcompany = {{
\t\t\t\t\ttype = $COMPANY$
\t\t\t\t\tcountry = scope:zz_ef_bkc_o
\t\t\t\t\tlevels = {COMPANY_LEVELS}
\t\t\t\t}}
\t\t\t\tcompany = {{
\t\t\t\t\ttype = {co}
\t\t\t\t\tcountry = c:{tag}
\t\t\t\t\tlevels = {COMPANY_LEVELS}
\t\t\t\t}}
\t\t\t}}
\t\t}}
\t}}
""")
            first = False
    o.append(("\telse = {\n" if not first else "\t{\n") + """\t\tcreate_building = {
\t\t\tbuilding = building_zz_ef_bank
\t\t\treserves = 0
\t\t\tadd_ownership = {
\t\t\t\tcompany = {
\t\t\t\t\ttype = $COMPANY$
\t\t\t\t\tcountry = scope:zz_ef_bkc_o
\t\t\t\t\tlevels = """ + str(COMPANY_LEVELS) + """
\t\t\t\t}
\t\t\t}
\t\t}
\t}
}
""")
    return "".join(o)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.parse_args()
    text = build()
    assert text.count("{") == text.count("}")
    ld_gen.emit(OUT, text)
    ld_gen.report("regen_ef_bank_seed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
