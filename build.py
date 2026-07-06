#!/usr/bin/env python3
"""EnterpriseQuest build script — inject content into single HTML."""
import json, os, sys, re
from pathlib import Path

ROOT = Path(__file__).parent
HTML = ROOT / "EnterpriseQuest.html"
CONTENT = ROOT / "content"

def load(name):
    with open(CONTENT / f"{name}.json") as f:
        return json.load(f)

# --- Classes: 6 architect-classes with attribute spreads ---
CLASSES = [
    {
        "id":"enterprise","name":"Enterprise Architect","icon":"👁",
        "role":"Governance · Strategie · Overzicht",
        "description":"Overziet het hele landschap: houdt strategie, portfolio en principes op één lijn.",
        "hp":110,
        "attrs":{"communication":9,"leadership":10,"architecture":10,"technology":6,"innovation":8,"security":7,"businessKnowledge":9},
        "special":"Architect Vision","specialDesc":"Ziet de zwakke plek — feilloos aanval + XP bonus"
    },
    {
        "id":"solution","name":"Solution Architect","icon":"⚔",
        "role":"Oplossingen · Techniek",
        "description":"Ontwerpt concrete oplossingen; koppelt patterns aan requirements.",
        "hp":100,
        "attrs":{"communication":7,"leadership":6,"architecture":9,"technology":10,"innovation":8,"security":7,"businessKnowledge":6},
        "special":"Elegant Solution","specialDesc":"Rolt 2 D20 en kiest de beste"
    },
    {
        "id":"business","name":"Business Architect","icon":"🤝",
        "role":"Stakeholders · Processen",
        "description":"Verbindt IT met business; capability maps en value streams.",
        "hp":95,
        "attrs":{"communication":10,"leadership":9,"architecture":7,"technology":5,"innovation":7,"security":5,"businessKnowledge":10},
        "special":"Stakeholder Rally","specialDesc":"Genees +HP en val aan"
    },
    {
        "id":"security","name":"Security Architect","icon":"🛡",
        "role":"Cyber · Compliance",
        "description":"Beschermt de organisatie: Zero Trust, threat modelling, IAM.",
        "hp":115,
        "attrs":{"communication":6,"leadership":7,"architecture":8,"technology":9,"innovation":6,"security":10,"businessKnowledge":6},
        "special":"Zero Trust Shield","specialDesc":"Blokkeert de volgende 2 vijandelijke aanvallen"
    },
    {
        "id":"data","name":"Data Architect","icon":"🧠",
        "role":"Data · AI · Analytics",
        "description":"Ontwerpt de datalaag: lakehouse, mesh, MLOps, RAG.",
        "hp":100,
        "attrs":{"communication":7,"leadership":6,"architecture":8,"technology":9,"innovation":10,"security":8,"businessKnowledge":7},
        "special":"Predictive Strike","specialDesc":"Data-crit: dubbele attack bonus"
    },
    {
        "id":"devops","name":"DevOps Architect","icon":"⚙",
        "role":"Automation · CI/CD · Cloud",
        "description":"Automatiseert alles: pipelines, GitOps, Kubernetes, observability.",
        "hp":105,
        "attrs":{"communication":6,"leadership":6,"architecture":8,"technology":10,"innovation":9,"security":7,"businessKnowledge":6},
        "special":"CI/CD Barrage","specialDesc":"3 snelle hits achter elkaar"
    }
]

LEVELS = [
    {"n":1,"name":"Junior Architect"},
    {"n":2,"name":"Medior Architect"},
    {"n":3,"name":"Senior Architect"},
    {"n":4,"name":"Domain Architect"},
    {"n":5,"name":"Lead Architect"},
    {"n":6,"name":"Enterprise Architect"},
    {"n":7,"name":"Principal Architect"},
    {"n":8,"name":"Chief Architect"},
    {"n":9,"name":"Digital Strategist"},
    {"n":10,"name":"Legendary Architect"}
]

def build():
    quests = load("quests")
    chaos = load("chaos")
    artifacts = load("artifacts")
    events = load("events")
    regions = load("regions")
    board = load("board")
    monsters = load("monsters")
    achievements = load("achievements")

    # Flatten monsters
    flat_monsters = []
    for m in monsters.get("minions", []): flat_monsters.append(m)
    for m in monsters.get("midBosses", []): flat_monsters.append(m)
    fb = monsters.get("finalBoss")
    if fb:
        # Ensure top-level fields for combat engine
        if "hp" not in fb and fb.get("phases"):
            fb["hp"] = fb["phases"][0].get("hp",300)
            fb["attack"] = fb["phases"][0].get("attack",25)
            fb["defense"] = fb["phases"][0].get("defense",18)
            fb["xpReward"] = fb["phases"][0].get("xpReward",800)
            fb["budgetReward"] = fb["phases"][0].get("budgetReward",1000)
        fb["icon"] = fb.get("icon","👹")
        flat_monsters.append(fb)

    # Icons for minions if missing
    default_icons = {"m01":"🐉","m02":"👻","m03":"🗿","m04":"🐍","m05":"👤",
                     "m06":"🧟","m07":"🐙","m08":"🕷","m09":"🦇","m10":"👹",
                     "m11":"💀","m12":"⚡","m13":"🔥","m14":"❄","m15":"🤖"}
    for m in flat_monsters:
        if not m.get("icon"):
            m["icon"] = default_icons.get(m.get("id",""), "👾")

    # Board: force tile 39 to type "final" (from "boss")
    for t in board["tiles"]:
        if t["id"] == 39:
            t["type"] = "final"

    # Read HTML template
    html = HTML.read_text()

    # Replacements: each placeholder is `/*__NAME__*/DEFAULT`, we replace with JSON.
    def inject(name, data):
        nonlocal html
        pat = re.compile(r"/\*__" + name + r"__\*/[^;]*?(?=;)", re.DOTALL)
        js_val = json.dumps(data, ensure_ascii=False)
        html2, n = pat.subn(lambda m: js_val, html, count=1)
        if n != 1:
            raise SystemExit(f"Placeholder __{name}__ not found or ambiguous")
        html = html2

    inject("CLASSES", CLASSES)
    inject("LEVELS", LEVELS)
    inject("REGIONS", regions)
    inject("BOARD", board)
    inject("QUESTS", quests)
    inject("CHAOS", chaos)
    inject("ARTIFACTS", artifacts)
    inject("EVENTS", events)
    inject("MONSTERS", flat_monsters)
    inject("ACHIEVEMENTS", achievements)

    HTML.write_text(html)
    total_cards = len(quests)+len(chaos)+len(artifacts)+len(events)
    print(f"OK — injected: {len(CLASSES)} classes, {len(LEVELS)} levels, {len(regions)} regions, "
          f"{len(board['tiles'])} tiles, {len(quests)} quests, {len(chaos)} chaos, "
          f"{len(artifacts)} artifacts, {len(events)} events, {len(flat_monsters)} monsters, "
          f"{len(achievements)} achievements. Total cards: {total_cards}")
    size = HTML.stat().st_size
    print(f"HTML size: {size} bytes ({size/1024:.1f} KB)")

if __name__ == "__main__":
    build()
