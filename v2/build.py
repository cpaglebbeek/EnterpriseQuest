#!/usr/bin/env python3
"""EnterpriseQuest v2 build — Dragon1 edition."""
import json, os, sys, re
from pathlib import Path

ROOT = Path(__file__).parent
HTML = ROOT / "EnterpriseQuest.html"
CONTENT = ROOT / "content"

# --- Levels (10 architect-levels) ---
LEVELS = [
    {"n":1,"name":"Junior Architect"},
    {"n":2,"name":"Medior Architect"},
    {"n":3,"name":"Senior Architect"},
    {"n":4,"name":"Lead Architect"},
    {"n":5,"name":"Domain Architect"},
    {"n":6,"name":"Enterprise Architect"},
    {"n":7,"name":"Principal Architect"},
    {"n":8,"name":"Chief Architect"},
    {"n":9,"name":"Digital Strategist"},
    {"n":10,"name":"Dragon1 Master Architect"}
]

# --- Achievements (47) — id-matched met code predicates da01..da47 ---
ACHIEVEMENTS = [
    {"id":"da01","title":"Eerste artefact","description":"Lever je eerste Dragon1-artefact op.","icon":"📜","xpReward":50},
    {"id":"da02","title":"Portfolio-bouwer","description":"Lever 6 artefacten op.","icon":"📚","xpReward":150},
    {"id":"da03","title":"Architect met bagage","description":"Lever 12 artefacten op.","icon":"🎖","xpReward":300},
    {"id":"da04","title":"Dragon1 Grand Slam","description":"Lever alle 15 Dragon1-artefacten op.","icon":"🐉","xpReward":600},
    {"id":"da05","title":"Eerste missie","description":"Rond je eerste missie succesvol af.","icon":"✅","xpReward":40},
    {"id":"da06","title":"Missiedecoratie","description":"Rond 10 missies af.","icon":"🎯","xpReward":150},
    {"id":"da07","title":"Missie-machine","description":"Rond 25 missies af.","icon":"⚡","xpReward":400},
    {"id":"da08","title":"Eerste bluspoging","description":"Los 1 uitdaging op.","icon":"🧯","xpReward":40},
    {"id":"da09","title":"Firefighter","description":"Los 10 uitdagingen op.","icon":"🚒","xpReward":180},
    {"id":"da10","title":"Crisis-manager","description":"Los 25 uitdagingen op.","icon":"🛠","xpReward":400},
    {"id":"da11","title":"Groei","description":"Bereik level 3 (Senior Architect).","icon":"📈","xpReward":100},
    {"id":"da12","title":"Enterprise-scope","description":"Bereik level 6 (Enterprise Architect).","icon":"🏛","xpReward":250},
    {"id":"da13","title":"Dragon1 Master","description":"Bereik level 10 (Dragon1 Master Architect).","icon":"🐲","xpReward":800},
    {"id":"da14","title":"Business Value Champion","description":"Business Value ≥ 80.","icon":"💼","xpReward":150},
    {"id":"da15","title":"Stakeholder Whisperer","description":"Stakeholder Confidence ≥ 90.","icon":"🤝","xpReward":200},
    {"id":"da16","title":"Governance Guardian","description":"Governance ≥ 80.","icon":"⚖","xpReward":150},
    {"id":"da17","title":"Innovation Guru","description":"Innovation ≥ 80.","icon":"💡","xpReward":150},
    {"id":"da18","title":"Zero Trust Adept","description":"Security ≥ 80.","icon":"🛡","xpReward":150},
    {"id":"da19","title":"Digitaal Volwassen","description":"Digital Maturity ≥ 80.","icon":"☁","xpReward":150},
    {"id":"da20","title":"Debt Slayer","description":"Technical Debt ≤ 15.","icon":"💀","xpReward":250},
    {"id":"da21","title":"Budget-koning","description":"Budget ≥ €5000.","icon":"💰","xpReward":100},
    {"id":"da22","title":"Wereldreiziger","description":"Bezoek 8 organisatie-onderdelen.","icon":"🗺","xpReward":100},
    {"id":"da23","title":"Kartograaf","description":"Bezoek alle 16 organisatie-onderdelen.","icon":"🧭","xpReward":250},
    {"id":"da24","title":"Visie geland","description":"Vision Blueprint opgeleverd.","icon":"👁","xpReward":80},
    {"id":"da25","title":"Strategie in kaart","description":"Strategy Map opgeleverd.","icon":"🎯","xpReward":80},
    {"id":"da26","title":"Capability Master","description":"Capability Map opgeleverd.","icon":"🧩","xpReward":80},
    {"id":"da27","title":"Principes vast","description":"Architecture Principles opgeleverd.","icon":"📖","xpReward":80},
    {"id":"da28","title":"App-landschap in beeld","description":"Application Landscape opgeleverd.","icon":"🏙","xpReward":80},
    {"id":"da29","title":"Tech Blueprint","description":"Technology Blueprint opgeleverd.","icon":"🖥","xpReward":80},
    {"id":"da30","title":"Governance-frame","description":"Governance Framework opgeleverd.","icon":"⚖","xpReward":80},
    {"id":"da31","title":"Transformatie-roadmap","description":"Transformation Roadmap opgeleverd.","icon":"🛣","xpReward":80},
    {"id":"da32","title":"Portfolio-inzicht","description":"Portfolio Dashboard opgeleverd.","icon":"📊","xpReward":80},
    {"id":"da33","title":"Repository operationeel","description":"Architecture Repository opgeleverd.","icon":"🗄","xpReward":80},
    {"id":"da34","title":"Event-manager","description":"Handel 10 events af.","icon":"📜","xpReward":100},
    {"id":"da35","title":"Beslisser","description":"Maak 20 keuzes bij uitdagingen/events.","icon":"⚡","xpReward":120},
    {"id":"da36","title":"Voldoende","description":"Presenteer met eindscore ≥ 80.","icon":"🎓","xpReward":300},
    {"id":"da37","title":"Uitstekend","description":"Presenteer met eindscore ≥ 90.","icon":"🏅","xpReward":500},
    {"id":"da38","title":"Legendarisch","description":"Presenteer met eindscore ≥ 95.","icon":"👑","xpReward":800},
    {"id":"da39","title":"Debt-arm","description":"Presenteer met Technical Debt ≤ 20.","icon":"🧹","xpReward":250},
    {"id":"da40","title":"Compleet portfolio","description":"Presenteer met alle 15 Dragon1-artefacten.","icon":"📜","xpReward":600},
    {"id":"da41","title":"Special!","description":"Gebruik je special ability.","icon":"✦","xpReward":50},
    {"id":"da42","title":"Speedrunner","description":"Presenteer binnen 40 beurten.","icon":"⚡","xpReward":300},
    {"id":"da43","title":"Krap budget","description":"Overleef tot Budget ≤ €100.","icon":"🪙","xpReward":150},
    {"id":"da44","title":"Draagvlak weg","description":"Overleef level 4+ met Stakeholder Confidence ≤ 20.","icon":"🚧","xpReward":180},
    {"id":"da45","title":"Governance + Security","description":"Presenteer met Governance≥90 én Security≥90.","icon":"🏛","xpReward":400},
    {"id":"da46","title":"Innovation + Digital","description":"Presenteer met Innovation≥90 én Digital Maturity≥90.","icon":"🚀","xpReward":400},
    {"id":"da47","title":"Meta Master","description":"Ontgrendel alle andere achievements.","icon":"🐉","xpReward":1000}
]

# --- Location-name mapping (agent E gebruikte generieke org-namen) ---
LOC_MAP = {
    # keys are what agent E used, values must match locations.json name-field
    "Directie":"Directiekamer",
    "Directie/RvB":"Directiekamer",
    "Business":"Business Domein",
    "Business Domein":"Business Domein",
    "Marketing":"Sales",
    "Sales":"Sales",
    "HR":"HR",
    "Finance":"Finance",
    "Legal":"Governance Board",
    "Compliance":"Governance Board",
    "R&D":"Innovatielab",
    "R&amp;D":"Innovatielab",
    "IT-Operations":"Applicatielandschap",
    "IT Operations":"Applicatielandschap",
    "IT-Security":"Security Operations Center",
    "SOC":"Security Operations Center",
    "Data":"Dataplatform",
    "Cloud":"Cloudplatform",
    "Integratie":"Integratielaag",
    "Klantenservice":"Klantenservice",
    "Operations":"Operations",
    "Projectenkantoor":"Project Portfolio",
    "Portfolio":"Project Portfolio",
    "PMO":"Project Portfolio",
    "Governance":"Governance Board",
    "Strategie":"Strategiecentrum",
    "Innovatie":"Innovatielab",
    "Innovatielab":"Innovatielab",
    "Applicatielandschap":"Applicatielandschap",
    "Dataplatform":"Dataplatform",
    "Integratielaag":"Integratielaag",
    "Cloudplatform":"Cloudplatform",
    "Security Operations Center":"Security Operations Center",
    "Project Portfolio":"Project Portfolio",
    "Governance Board":"Governance Board",
    "Strategiecentrum":"Strategiecentrum",
    "Directiekamer":"Directiekamer",
}

def norm_location(v):
    if not v: return None
    return LOC_MAP.get(v, v)

def build():
    def load(n):
        with open(CONTENT/f"{n}.json") as f: return json.load(f)

    roles = load("roles")
    locations = load("locations")
    missions = load("missions")
    challenges_raw = load("challenges")
    events_raw = load("events")
    artefacts = load("artefacts")

    # Flatten challenges/events dicts
    challenges = challenges_raw["challenges"] if isinstance(challenges_raw, dict) else challenges_raw
    events = events_raw["events"] if isinstance(events_raw, dict) else events_raw

    # Normalize locations
    for m in missions:
        m["location"] = norm_location(m.get("location"))
    for c in challenges:
        c["location"] = norm_location(c.get("location"))
    for e in events:
        e["location"] = norm_location(e.get("location"))

    # Save achievements to content folder for consistency
    (CONTENT/"achievements.json").write_text(json.dumps(ACHIEVEMENTS, ensure_ascii=False, indent=2))

    html = HTML.read_text()
    def inject(name, data):
        nonlocal html
        pat = re.compile(r"/\*__" + name + r"__\*/[^;]*?(?=;)", re.DOTALL)
        js_val = json.dumps(data, ensure_ascii=False)
        html2, n = pat.subn(lambda m: js_val, html, count=1)
        if n != 1:
            raise SystemExit(f"Placeholder __{name}__ not found or ambiguous")
        html = html2

    inject("ROLES", roles)
    inject("LEVELS", LEVELS)
    inject("LOCATIONS", locations)
    inject("MISSIONS", missions)
    inject("CHALLENGES", challenges)
    inject("EVENTS", events)
    inject("ARTEFACTS", artefacts)
    inject("ACHIEVEMENTS", ACHIEVEMENTS)

    HTML.write_text(html)
    size = HTML.stat().st_size
    total_cards = len(missions)+len(challenges)+len(events)
    print(f"OK — v2 injected: {len(roles)} roles, {len(LEVELS)} levels, {len(locations)} locations, "
          f"{len(missions)} missions, {len(challenges)} challenges, {len(events)} events, "
          f"{len(artefacts)} artefacts, {len(ACHIEVEMENTS)} achievements. Total cards: {total_cards}")
    print(f"HTML size: {size} bytes ({size/1024:.1f} KB)")

if __name__ == "__main__":
    build()
