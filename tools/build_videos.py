#!/usr/bin/env python3
"""
build_videos.py — genereer 6 demo-video's (60-70s elk) voor EnterpriseQuest:
  1. v1_digital_demo.mp4  — fantasy RPG in browser
  2. v1_analog_demo.mp4   — fantasy RPG als bordspel (PnP)
  3. v2_digital_demo.mp4  — Dragon1 in browser
  4. v2_analog_demo.mp4   — Dragon1 als bordspel (PnP)
  5. v3_digital_demo.mp4  — Train Your Dragon AI-governance in browser
  6. v3_analog_demo.mp4   — Train Your Dragon als bordspel (PnP)

Patroon: SVG-beats -> cairosvg PNG -> ffmpeg concat -> MP4 (1280x720, 30fps).
Storyboard per video: intro + 10-12 gameplay-beats + outro.
"""

import cairosvg
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent.parent
VIDEOS = ROOT / "videos"
FRAMES_ROOT = VIDEOS / "_frames"
FRAMES_ROOT.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720

# =========================================================
# GEDEELDE PRIMITIVES
# =========================================================

def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg_header(bg="#0a0e1c"):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'font-family="Helvetica, Arial, sans-serif">\n'
            f'<rect width="{W}" height="{H}" fill="{bg}"/>\n')


def header(title, sub, color="#f5c542"):
    return (f'<text x="{W/2}" y="55" text-anchor="middle" fill="{color}" '
            f'font-size="28" font-weight="800">{esc(title)}</text>\n'
            f'<text x="{W/2}" y="90" text-anchor="middle" fill="#a4acc9" '
            f'font-size="16">{esc(sub)}</text>\n')


def narrative_box(text, subtext=""):
    """Onderaan info-bar met uitleg."""
    y0 = 590
    lines = wrap(text, 92)
    s = (f'<rect x="40" y="{y0}" width="{W-80}" height="110" rx="10" '
         f'fill="#1a1f3a" stroke="#2b3572" stroke-width="1"/>\n'
         f'<text x="60" y="{y0+30}" fill="#f5c542" font-size="14" '
         f'font-weight="700">▶ Wat gebeurt hier</text>\n')
    for i, line in enumerate(lines[:2]):
        s += (f'<text x="60" y="{y0+55+i*22}" fill="#f0f3ff" font-size="15">'
              f'{esc(line)}</text>\n')
    if subtext:
        s += (f'<text x="60" y="{y0+100}" fill="#8f97ad" font-size="12" '
              f'font-style="italic">{esc(subtext)}</text>\n')
    return s


def wrap(text, max_chars):
    words = text.split()
    lines, cur = [], []
    for w in words:
        if sum(len(x) for x in cur) + len(cur) + len(w) > max_chars:
            lines.append(" ".join(cur))
            cur = [w]
        else:
            cur.append(w)
    if cur:
        lines.append(" ".join(cur))
    return lines


def outro(title, subtitle, url, bg="#0a0e1c", accent="#f5c542"):
    s = svg_header(bg)
    s += (f'<text x="{W/2}" y="{H/2-90}" text-anchor="middle" fill="{accent}" '
          f'font-size="52" font-weight="900">{esc(title)}</text>\n')
    s += (f'<text x="{W/2}" y="{H/2-30}" text-anchor="middle" fill="#f0f3ff" '
          f'font-size="22">{esc(subtitle)}</text>\n')
    s += (f'<text x="{W/2}" y="{H/2+40}" text-anchor="middle" fill="#8258e0" '
          f'font-size="20">▶ {esc(url)}</text>\n')
    s += (f'<text x="{W/2}" y="{H-60}" text-anchor="middle" fill="#8f97ad" '
          f'font-size="14">iCt Horse · AGPL-3.0 · Print &amp; Play beschikbaar</text>\n')
    s += "</svg>"
    return s


def intro(title, tagline, badge, badge_color, tagline2=""):
    s = svg_header()
    s += (f'<text x="{W/2}" y="{H/2-80}" text-anchor="middle" fill="{badge_color}" '
          f'font-size="60" font-weight="900">{esc(title)}</text>\n')
    s += (f'<text x="{W/2}" y="{H/2-30}" text-anchor="middle" fill="#f0f3ff" '
          f'font-size="22">{esc(tagline)}</text>\n')
    if tagline2:
        s += (f'<text x="{W/2}" y="{H/2+5}" text-anchor="middle" fill="#a4acc9" '
              f'font-size="18">{esc(tagline2)}</text>\n')
    s += (f'<rect x="{W/2-100}" y="{H/2+40}" width="200" height="34" rx="17" '
          f'fill="{badge_color}"/>\n'
          f'<text x="{W/2}" y="{H/2+63}" text-anchor="middle" fill="#1a1200" '
          f'font-size="16" font-weight="700">{esc(badge)}</text>\n')
    s += (f'<text x="{W/2}" y="{H-60}" text-anchor="middle" fill="#8f97ad" '
          f'font-size="14">EnterpriseQuest · iCt Horse · icthorse.nl</text>\n')
    s += "</svg>"
    return s


def render_dice(x, y, val, color="#f5c542", size=60):
    s = (f'<rect x="{x-size/2}" y="{y-size/2}" width="{size}" height="{size}" '
         f'rx="8" fill="{color}" stroke="#1a1200" stroke-width="2"/>\n')
    s += (f'<text x="{x}" y="{y+8}" text-anchor="middle" fill="#1a1200" '
          f'font-size="28" font-weight="900">{val}</text>\n')
    return s


def render_card(x, y, w, h, title, subtitle, kind="quest", bg_from="#1e1a3a",
                bg_to="#12102a", accent="#8258e0"):
    s = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" '
         f'fill="{bg_from}" stroke="{accent}" stroke-width="2"/>\n')
    # kind pill
    kind_colors = {
        "quest": "#8258e0", "chaos": "#ef476f", "artifact": "#f5c542",
        "event": "#43d5f5", "opportunity": "#06d6a0", "threat": "#ef476f",
        "governance": "#43d5f5", "mission": "#06d6a0", "challenge": "#ef476f",
    }
    pc = kind_colors.get(kind, accent)
    s += (f'<rect x="{x+10}" y="{y+10}" width="90" height="22" rx="11" '
          f'fill="{pc}"/>\n'
          f'<text x="{x+55}" y="{y+26}" text-anchor="middle" fill="#1a1200" '
          f'font-size="11" font-weight="700">{esc(kind.upper())}</text>\n')
    # title (wrap)
    tlines = wrap(title, 20)
    for i, line in enumerate(tlines[:2]):
        s += (f'<text x="{x+15}" y="{y+65+i*22}" fill="#f5c542" font-size="17" '
              f'font-weight="700">{esc(line)}</text>\n')
    # subtitle (wrap)
    slines = wrap(subtitle, 25)
    yoff = y + 65 + len(tlines[:2]) * 22 + 15
    for i, line in enumerate(slines[:3]):
        s += (f'<text x="{x+15}" y="{yoff+i*18}" fill="#a4acc9" font-size="13">'
              f'{esc(line)}</text>\n')
    return s


def role_badge(x, y, icon, name, color, active=False):
    r = 32 if active else 26
    sw = 4 if active else 2
    stroke = "#f5c542" if active else color
    s = (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#1a1f3a" stroke="{stroke}" '
         f'stroke-width="{sw}"/>\n')
    s += (f'<text x="{x}" y="{y+8}" text-anchor="middle" font-size="22">'
          f'{icon}</text>\n')
    s += (f'<text x="{x}" y="{y+55}" text-anchor="middle" fill="{color}" '
          f'font-size="11" font-weight="700">{esc(name)}</text>\n')
    return s


def hp_bar(x, y, w, h, val, max_val=100, color="#06d6a0", label=""):
    pct = max(0, min(1, val / max_val))
    s = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" '
         f'fill="#1a1f3a" stroke="#2b3572" stroke-width="1"/>\n')
    s += (f'<rect x="{x}" y="{y}" width="{w*pct}" height="{h}" rx="4" '
          f'fill="{color}"/>\n')
    if label:
        s += (f'<text x="{x}" y="{y-4}" fill="#a4acc9" font-size="11">'
              f'{esc(label)}: {val}/{max_val}</text>\n')
    return s


# =========================================================
# VIDEO 1: v1 DIGITAL - Fantasy RPG in browser
# =========================================================

def v1_digital_beats():
    beats = []

    beats.append(("intro", intro(
        "Architect's Dungeon",
        "EnterpriseQuest v1 — Fantasy RPG in de browser",
        "v0.0.1-Zachman", "#8a5cf5",
        tagline2="6 klassen · D20 combat · versla The Chaos Architect")))

    # Beat 1: rol kiezen
    s = svg_header()
    s += header("Stap 1 — Kies je architect-klasse", "6 opties met eigen special ability", "#8a5cf5")
    classes = [("🏛️", "Enterprise", "#8a5cf5"), ("🧩", "Solution", "#43d5f5"),
               ("🏢", "Business", "#06d6a0"), ("🛡️", "Security", "#ef476f"),
               ("🗄️", "Data", "#f5c542"), ("⚙️", "DevOps", "#ff8c42")]
    for i, (icon, name, color) in enumerate(classes):
        x = 130 + i * 170
        active = (i == 3)  # Security is gekozen
        s += role_badge(x, 250, icon, name, color, active)
    s += (f'<text x="{W/2}" y="380" text-anchor="middle" fill="#f5c542" '
          f'font-size="18" font-weight="700">➤ Security Architect gekozen — start-HP 45, defense 11</text>\n')
    s += narrative_box(
        "Je kiest een klasse met unieke stats en een 1x-per-spel special ability.",
        "Security krijgt 'Threat Shield': negeer 1 aanval volledig.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 2: bord + huidige positie
    s = svg_header()
    s += header("Stap 2 — Het parcours", "40 tiles over 12 regio's, van Business Village naar Digital Portal", "#8a5cf5")
    # simpele board-strip: 10 tiles
    regions = [("Business", "#06d6a0"), ("Vendor", "#f5c542"), ("Integration", "#43d5f5"),
               ("Data", "#228B22"), ("Cloud", "#87CEEB"), ("Innovation", "#f5c542"),
               ("Legacy", "#5C4033"), ("Security", "#8a5cf5"), ("Compliance", "#556B2F"),
               ("AI Temple", "#DA70D6")]
    for i, (name, color) in enumerate(regions):
        x = 80 + i * 115
        active = (i == 7)  # Security Castle
        r = 42 if active else 34
        sw = 5 if active else 2
        s += (f'<circle cx="{x}" cy="280" r="{r}" fill="#1a1f3a" stroke="{color}" '
              f'stroke-width="{sw}"/>\n')
        s += (f'<text x="{x}" y="290" text-anchor="middle" fill="#f0f3ff" '
              f'font-size="12" font-weight="700">{esc(name[:6])}</text>\n')
        s += (f'<text x="{x}" y="335" text-anchor="middle" fill="#a4acc9" '
              f'font-size="10">tile {i*4}</text>\n')
    s += (f'<text x="{80+7*115}" y="230" text-anchor="middle" fill="#f5c542" '
          f'font-size="24">▼</text>\n')
    s += (f'<text x="{80+7*115}" y="215" text-anchor="middle" fill="#f5c542" '
          f'font-size="12" font-weight="700">JIJ</text>\n')
    s += narrative_box(
        "Je pion staat in Security Castle op tile 28. Portalen bij tile 10, 20, 30 laten je teleporteren.",
        "Elke tile heeft een type: quest, chaos, event, artifact, combat, boss of rest.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 3: D20 roll
    s = svg_header()
    s += header("Stap 3 — Beweeg met D20", "steps = floor(worp/2) + 1, hogere worp = extra bonus", "#8a5cf5")
    # dice
    cx, cy = W/2, 300
    r = 90
    s += (f'<polygon points="{cx},{cy-r} {cx+r*0.87},{cy-r*0.5} {cx+r*0.87},{cy+r*0.5} '
          f'{cx},{cy+r} {cx-r*0.87},{cy+r*0.5} {cx-r*0.87},{cy-r*0.5}" '
          f'fill="#8a5cf5" stroke="#f5c542" stroke-width="4"/>\n')
    s += (f'<text x="{cx}" y="{cy+18}" text-anchor="middle" fill="#f0f3ff" '
          f'font-size="70" font-weight="900">14</text>\n')
    s += (f'<text x="{cx}" y="{cy+140}" text-anchor="middle" fill="#f5c542" '
          f'font-size="20" font-weight="700">D20 = 14 → 8 stappen vooruit</text>\n')
    s += narrative_box(
        "Je rolt 14. Steps = floor(14/2) + 1 = 8 stappen. Je pion beweegt naar tile 36.",
        "Bij natuurlijke 20 verdubbelt schade in combat. Bij natuurlijke 1 verlies je een stakeholder-token.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 4: kaart trekken
    s = svg_header()
    s += header("Stap 4 — Kaart trekken", "Elke tile heeft een deck-type", "#8a5cf5")
    s += render_card(200, 180, 350, 340,
                     "Zero Trust Fundering",
                     "Sla de fundering van het Zero Trust bastion. Nooit vertrouwen, altijd verifieren.",
                     kind="quest")
    s += (f'<text x="600" y="230" fill="#f5c542" font-size="20" font-weight="700">'
          f'EFFECT (verplicht):</text>\n')
    s += (f'<text x="600" y="270" fill="#06d6a0" font-size="18">+300 XP</text>\n')
    s += (f'<text x="600" y="300" fill="#ef476f" font-size="18">-€250 budget</text>\n')
    s += (f'<text x="600" y="330" fill="#06d6a0" font-size="18">+35 Security</text>\n')
    s += (f'<text x="600" y="360" fill="#06d6a0" font-size="18">+10 Stakeholder</text>\n')
    s += (f'<text x="600" y="410" fill="#a4acc9" font-size="15" font-style="italic">'
          f'Difficulty 4 · Regio: Security Castle</text>\n')
    s += narrative_box(
        "Je trekt een Quest-kaart uit het groene deck. Effect wordt automatisch toegepast.",
        "Bij Event-kaarten krijg je vaak een branching-choice met 2-3 opties.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 5: combat
    s = svg_header()
    s += header("Stap 5 — Combat tegen monster", "Trek monster-kaart, worp vs defense", "#8a5cf5")
    # jij vs monster
    s += (f'<text x="240" y="200" text-anchor="middle" fill="#f5c542" '
          f'font-size="22" font-weight="700">Jij (Security Arch)</text>\n')
    s += role_badge(240, 300, "🛡️", "Security", "#ef476f", active=True)
    s += hp_bar(120, 380, 240, 20, 45, 45, color="#06d6a0", label="HP")
    s += hp_bar(120, 420, 240, 20, 250, 500, color="#f5c542", label="XP")
    s += (f'<text x="{W/2}" y="320" text-anchor="middle" fill="#ef476f" '
          f'font-size="48" font-weight="900">⚔</text>\n')
    s += (f'<text x="1040" y="200" text-anchor="middle" fill="#ef476f" '
          f'font-size="22" font-weight="700">Cyber Lord (boss)</text>\n')
    s += (f'<text x="1040" y="300" text-anchor="middle" font-size="60">👹</text>\n')
    s += hp_bar(920, 380, 240, 20, 210, 250, color="#ef476f", label="Monster HP")
    s += (f'<text x="{W/2}" y="500" text-anchor="middle" fill="#f5c542" '
          f'font-size="18" font-weight="700">Jouw worp: D20=15 + attack 7 = 22. '
          f'Monster-defense: 16. HIT — schade: (22-16)+5 = 11</text>\n')
    s += narrative_box(
        "Je verslaat de mid-boss Cyber Lord. Beloning: +440 XP, +€680 budget.",
        "Bij natuurlijke 20 = crit, dubbele schade. Bij natuurlijke 1 = miss, -1 stakeholder.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 6: level up + artifact
    s = svg_header()
    s += header("Stap 6 — Level-up en artifacts", "XP-drempels verhogen je klasse", "#8a5cf5")
    # level track
    s += (f'<text x="{W/2}" y="180" text-anchor="middle" fill="#f5c542" '
          f'font-size="24" font-weight="700">Level 3 → Level 4</text>\n')
    for i in range(10):
        x = 130 + i * 105
        color = "#06d6a0" if i < 4 else ("#f5c542" if i == 4 else "#1a1f3a")
        s += (f'<rect x="{x-40}" y="220" width="80" height="30" rx="4" fill="{color}" '
              f'stroke="#2b3572" stroke-width="1"/>\n')
        s += (f'<text x="{x}" y="240" text-anchor="middle" fill="#1a1200" '
              f'font-size="14" font-weight="700">Lv {i+1}</text>\n')
    # artifact reward
    s += render_card(400, 320, 400, 220, "Zero-Trust Aegis",
                     "Legendarisch schild — verifieert elke request. +5 defense, +25 security, +15 chaos-resist.",
                     kind="artifact", accent="#f5c542")
    s += narrative_box(
        "Je bereikt level 4 en krijgt +5 HP + attack of defense keuze. Ook: legendarisch artifact uit boss-drop.",
        "Artifacts geven passive-bonussen zolang uitgerust. Max 5 slots + kroon bij level 10.")
    s += "</svg>"
    beats.append(("beat", s))

    beats.append(("outro", outro(
        "🏆 Speel zelf",
        "40 tiles · 250 kaarten · versla The Chaos Architect in 3 fases",
        "icthorse.nl/EnterpriseQuest/v1/",
        accent="#8a5cf5")))

    return beats


# =========================================================
# VIDEO 2: v1 ANALOG - Fantasy RPG als bordspel
# =========================================================

def v1_analog_beats():
    beats = []

    beats.append(("intro", intro(
        "Architect's Dungeon",
        "Analoge Print & Play — fysiek bordspel",
        "PnP · 2-6 spelers · 90-150 min", "#8a5cf5",
        tagline2="Zelfde regels als digitaal, echte kaarten op tafel")))

    # Beat 1: componenten
    s = svg_header()
    s += header("Componenten in de doos", "Alles wat je nodig hebt", "#8a5cf5")
    items = [
        ("🎲", "6× D20", "1 per speler"),
        ("🗂", "250 kaarten", "Quest/Chaos/Artifact/Event"),
        ("👹", "22 monsters", "elite + boss + finale"),
        ("📜", "6 tableaus", "klassen-vellen"),
        ("🎯", "Tokens", "HP/XP/€/stakeholder"),
        ("🗺️", "Bord", "40 tiles, 12 regio's"),
    ]
    for i, (icon, title, sub) in enumerate(items):
        col = i % 3
        row = i // 3
        x = 250 + col * 300
        y = 220 + row * 180
        s += (f'<rect x="{x-100}" y="{y-40}" width="200" height="140" rx="12" '
              f'fill="#1a1f3a" stroke="#2b3572" stroke-width="1"/>\n')
        s += (f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="46">{icon}</text>\n')
        s += (f'<text x="{x}" y="{y+50}" text-anchor="middle" fill="#f5c542" '
              f'font-size="16" font-weight="700">{esc(title)}</text>\n')
        s += (f'<text x="{x}" y="{y+72}" text-anchor="middle" fill="#a4acc9" '
              f'font-size="12">{esc(sub)}</text>\n')
    s += narrative_box(
        "Print zelf uit (€25-30 thuis) of laat drukken via The Game Crafter (€45-90 per doos).",
        "PDF met snijlijnen op icthorse.nl/EnterpriseQuest/docs/analog_v1_rpg.pdf")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 2: setup rond de tafel
    s = svg_header()
    s += header("Setup rond de tafel", "6 spelers, klasse gekozen, tokens verdeeld", "#8a5cf5")
    # tafel-view: bord in midden, 6 spelers eromheen
    s += (f'<rect x="440" y="220" width="400" height="240" rx="16" fill="#1a1f3a" '
          f'stroke="#8a5cf5" stroke-width="3"/>\n')
    s += (f'<text x="640" y="260" text-anchor="middle" fill="#f5c542" font-size="18" '
          f'font-weight="700">🗺️ BORD</text>\n')
    s += (f'<text x="640" y="290" text-anchor="middle" fill="#a4acc9" font-size="14">'
          f'40 tiles · 12 regio\'s</text>\n')
    # decks naast bord
    for i, (label, color) in enumerate([("Quest", "#06d6a0"), ("Chaos", "#ef476f"),
                                          ("Artifact", "#f5c542"), ("Event", "#43d5f5")]):
        y = 320 + i * 32
        s += (f'<rect x="470" y="{y}" width="90" height="26" rx="4" fill="{color}"/>\n')
        s += (f'<text x="515" y="{y+18}" text-anchor="middle" fill="#1a1200" '
              f'font-size="12" font-weight="700">{esc(label)}</text>\n')
    # players around
    positions = [(240, 260, "🏛️", "P1"), (240, 400, "🧩", "P2"),
                 (400, 500, "🏢", "P3"), (880, 500, "🛡️", "P4"),
                 (1040, 400, "🗄️", "P5"), (1040, 260, "⚙️", "P6")]
    for x, y, icon, name in positions:
        s += (f'<circle cx="{x}" cy="{y}" r="30" fill="#232a4a" stroke="#f5c542" '
              f'stroke-width="2"/>\n')
        s += (f'<text x="{x}" y="{y+8}" text-anchor="middle" font-size="24">{icon}</text>\n')
        s += (f'<text x="{x}" y="{y+52}" text-anchor="middle" fill="#f5c542" '
              f'font-size="12" font-weight="700">{name}</text>\n')
    s += narrative_box(
        "Elke speler kiest 1 klasse-tableau, krijgt start-HP, €1000, 3 stakeholder-tokens, 2 starter-artifacts.",
        "Facilitator schuffelt de 4 decks en zet klaar. Alle pionnen op tile 0 (Kick-off Plaza).")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 3: beurt-flow met D20
    s = svg_header()
    s += header("Voorbeeld beurt — P4 (Security Arch)", "Rol → beweeg → tile-effect", "#8a5cf5")
    s += render_dice(200, 300, 14, color="#8a5cf5", size=100)
    s += (f'<text x="200" y="420" text-anchor="middle" fill="#f5c542" font-size="16" '
          f'font-weight="700">D20 = 14</text>\n')
    s += (f'<text x="200" y="445" text-anchor="middle" fill="#a4acc9" font-size="14">'
          f'8 stappen</text>\n')
    # arrow
    s += (f'<text x="400" y="310" fill="#f5c542" font-size="40">➜</text>\n')
    # nieuwe positie
    s += (f'<rect x="500" y="220" width="600" height="180" rx="12" fill="#1a1f3a" '
          f'stroke="#8a5cf5" stroke-width="2"/>\n')
    s += (f'<text x="800" y="260" text-anchor="middle" fill="#f5c542" font-size="20" '
          f'font-weight="700">tile 36 — IAM Redesign</text>\n')
    s += (f'<text x="800" y="290" text-anchor="middle" fill="#a4acc9" font-size="16">'
          f'Security Castle · Quest-tile</text>\n')
    s += (f'<text x="800" y="335" text-anchor="middle" fill="#06d6a0" font-size="18">'
          f'→ Trek Quest-kaart</text>\n')
    s += (f'<text x="800" y="370" text-anchor="middle" fill="#a4acc9" font-size="14" '
          f'font-style="italic">"IAM Sleutelmeester: PAM-vault, +35 security"</text>\n')
    s += narrative_box(
        "P4 rolt 14, beweegt 8 stappen naar tile 36. Trekt Quest-kaart, past effect toe: +250 XP, +35 security, -€180.",
        "Bij combat-tile zou P4 in gevecht met een regio-monster raken (zie beat 5).")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 4: kaart-anatomie op tafel
    s = svg_header()
    s += header("Kaart-anatomie", "Standaard Euro-poker formaat 63×88 mm", "#8a5cf5")
    # 3 kaartjes naast elkaar
    for i, (title, sub, kind) in enumerate([
        ("Zero Trust Fundering", "+300 XP · +35 sec", "quest"),
        ("CIO Reorg", "-100 XP · -€150", "chaos"),
        ("Runbook Codex", "+8 chaos-resist", "artifact")]):
        x = 130 + i * 380
        s += render_card(x, 200, 320, 320, title, sub, kind=kind)
    s += narrative_box(
        "Elke kaart heeft: type-badge, titel, beschrijving, effect (verplicht toepassen bij Quest/Chaos).",
        "Event-kaarten hebben branching-choices (A/B/C). Artifact-kaarten geven passive-bonus zolang uitgerust.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 5: combat aan tafel
    s = svg_header()
    s += header("Combat aan tafel", "Speler-D20 tegen monster-defense", "#8a5cf5")
    # speler-kant
    s += role_badge(200, 280, "🛡️", "P4", "#ef476f", active=True)
    s += hp_bar(80, 350, 240, 20, 40, 45, color="#06d6a0", label="HP")
    s += render_dice(200, 450, 15, color="#f5c542", size=60)
    s += (f'<text x="200" y="510" text-anchor="middle" fill="#f5c542" font-size="14" '
          f'font-weight="700">worp 15 + attack 7</text>\n')
    s += (f'<text x="200" y="530" text-anchor="middle" fill="#f0f3ff" font-size="18" '
          f'font-weight="700">= 22 aanval</text>\n')
    # vs
    s += (f'<text x="{W/2}" y="330" text-anchor="middle" fill="#ef476f" '
          f'font-size="60" font-weight="900">⚔</text>\n')
    # monster
    s += (f'<text x="1000" y="220" text-anchor="middle" fill="#ef476f" '
          f'font-size="60">👹</text>\n')
    s += (f'<text x="1000" y="290" text-anchor="middle" fill="#ef476f" '
          f'font-size="20" font-weight="700">Cyber Lord</text>\n')
    s += hp_bar(880, 350, 240, 20, 210, 250, color="#ef476f", label="Monster HP")
    s += (f'<text x="1000" y="450" text-anchor="middle" fill="#a4acc9" font-size="14">'
          f'defense: 16</text>\n')
    s += (f'<text x="1000" y="480" text-anchor="middle" fill="#06d6a0" font-size="18" '
          f'font-weight="700">HIT — schade 11</text>\n')
    s += narrative_box(
        "Team-D20's: elke speler kan bijdragen aan boss-fights. Facilitator houdt monster-HP bij.",
        "Bij natuurlijke 20 crit (dubbele schade). Vluchten mag maar kost -5 HP en -1 stakeholder.")
    s += "</svg>"
    beats.append(("beat", s))

    beats.append(("outro", outro(
        "📦 Print & Play",
        "Download PDF + speel met 2-6 spelers · 90-150 min",
        "icthorse.nl/EnterpriseQuest/docs/analog_v1_rpg.pdf",
        accent="#8a5cf5")))

    return beats


# =========================================================
# VIDEO 3: v2 DIGITAL - Dragon1 workshop-simulatie
# =========================================================

def v2_digital_beats():
    beats = []

    beats.append(("intro", intro(
        "Dragon1 Architect's Journey",
        "EnterpriseQuest v2 — Dragon1 workshop-simulatie",
        "v0.2.0-Paauwe", "#20a89a",
        tagline2="8 rollen · 15 artefacten met cascade · geen combat")))

    # Beat 1: 8 rollen
    s = svg_header()
    s += header("Stap 1 — 8 rollen te kiezen", "Elke rol heeft eigen 9-attribuut-profiel", "#20a89a")
    roles = [("🏛️", "EA", "#20a89a"), ("🧩", "SA", "#43d5f5"),
             ("🏢", "BA", "#06d6a0"), ("🗄️", "IA", "#f5c542"),
             ("🛡️", "SecA", "#ef476f"), ("🎛️", "CIO", "#ff8c42"),
             ("💼", "IT-Mgr", "#8258e0"), ("🎓", "Student", "#a4acc9")]
    for i, (icon, name, color) in enumerate(roles):
        row = i // 4
        col = i % 4
        x = 200 + col * 260
        y = 220 + row * 170
        active = (i == 5)  # CIO
        s += role_badge(x, y, icon, name, color, active)
    s += (f'<text x="{W/2}" y="565" text-anchor="middle" fill="#f5c542" '
          f'font-size="18" font-weight="700">➤ CIO gekozen — Executive Mandate special ability</text>\n')
    s += narrative_box(
        "Kies uit 8 rollen. CIO krijgt +8 businessValue, +12 stakeholder, +6 governance start-bonus.",
        "Special ability: 1x per spel +20 budget-per-beurt + versnel artefact-goedkeuring.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 2: 4x4 bord
    s = svg_header()
    s += header("Stap 2 — 4×4 bord van 16 organisatie-onderdelen", "Van Directiekamer naar Governance Board", "#20a89a")
    locs = [("🏛️", "Directie"), ("🧭", "Strategie"), ("⚖️", "Governance"), ("💰", "Finance"),
            ("🏢", "Business"), ("⚙️", "Operations"), ("📈", "Sales"), ("🎧", "Service"),
            ("🖥️", "Applic"), ("🗄️", "Data"), ("🔗", "Integ"), ("☁️", "Cloud"),
            ("👥", "HR"), ("🧪", "Innov"), ("📋", "Portfolio"), ("🛡️", "SOC")]
    for i, (icon, name) in enumerate(locs):
        col = i % 4
        row = i // 4
        x = 300 + col * 170
        y = 180 + row * 100
        active = (i == 0)
        color = "#f5c542" if active else "#20a89a"
        sw = 4 if active else 1
        s += (f'<rect x="{x-70}" y="{y-40}" width="140" height="80" rx="8" fill="#1a1f3a" '
              f'stroke="{color}" stroke-width="{sw}"/>\n')
        s += (f'<text x="{x}" y="{y-8}" text-anchor="middle" font-size="24">{icon}</text>\n')
        s += (f'<text x="{x}" y="{y+22}" text-anchor="middle" fill="#f0f3ff" '
              f'font-size="12" font-weight="700">{esc(name)}</text>\n')
    s += narrative_box(
        "Jouw CIO-pion staat in Directiekamer. Elke locatie heeft eigen mission-kaarten.",
        "Beweeg max 2 tegels per beurt (orthogonaal). Elke locatie levert 1 type artefact.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 3: mission trekken
    s = svg_header()
    s += header("Stap 3 — Mission-kaart", "Modelleer een Dragon1-artefact", "#20a89a")
    s += render_card(280, 180, 420, 380,
                     "Ontwikkel Enterprise Vision voor directie",
                     "Faciliteer directie-sessie en leg de Enterprise Vision vast als eerste ankerpunt van de Dragon1 cascade.",
                     kind="mission", accent="#06d6a0")
    s += (f'<text x="770" y="230" fill="#f5c542" font-size="20" font-weight="700">'
          f'Levert artefact:</text>\n')
    s += (f'<text x="770" y="270" fill="#f0f3ff" font-size="24" font-weight="800">'
          f'A001 Vision Blueprint</text>\n')
    s += (f'<text x="770" y="320" fill="#a4acc9" font-size="16">Locatie: Directiekamer</text>\n')
    s += (f'<text x="770" y="345" fill="#a4acc9" font-size="16">Difficulty: 3</text>\n')
    s += (f'<text x="770" y="400" fill="#06d6a0" font-size="16">+250 XP · +25 BusinessValue</text>\n')
    s += (f'<text x="770" y="425" fill="#06d6a0" font-size="16">+30 StakeholderConfidence</text>\n')
    s += (f'<text x="770" y="450" fill="#06d6a0" font-size="16">+10 Governance · +15 Innovation</text>\n')
    s += (f'<text x="770" y="475" fill="#ef476f" font-size="16">-€100 budget</text>\n')
    s += narrative_box(
        "Je trekt Mission M001. Deze levert A001 Vision Blueprint — het fundament van de Dragon1-cascade.",
        "Zonder A001 kan je later A002 (Strategy Map), A003 (Capability Map) en A004 (Principles) niet ontgrendelen.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 4: cascade
    s = svg_header()
    s += header("Stap 4 — Dragon1 artefact-cascade", "Volgorde van bouwen bepaalt succes", "#20a89a")
    # cascade diagram
    def art_node(x, y, aid, name, active=False):
        color = "#f5c542" if active else "#20a89a"
        return (f'<rect x="{x-70}" y="{y-25}" width="140" height="50" rx="6" fill="#1a1f3a" '
                f'stroke="{color}" stroke-width="2"/>\n'
                f'<text x="{x}" y="{y-5}" text-anchor="middle" fill="{color}" '
                f'font-size="12" font-weight="700">{aid}</text>\n'
                f'<text x="{x}" y="{y+15}" text-anchor="middle" fill="#f0f3ff" '
                f'font-size="12">{name}</text>\n')
    s += art_node(W/2, 200, "A001", "Vision Blueprint", active=True)
    s += art_node(W/2-260, 320, "A002", "Strategy Map")
    s += art_node(W/2, 320, "A004", "Principles")
    s += art_node(W/2+260, 320, "A013", "Vision Poster")
    s += art_node(W/2-320, 440, "A003", "Capability Map")
    s += art_node(W/2-100, 440, "A010", "Roadmap")
    s += art_node(W/2+140, 440, "A009", "Governance")
    # arrows
    for xs, ys, xe, ye in [(W/2, 225, W/2-260, 295), (W/2, 225, W/2, 295), (W/2, 225, W/2+260, 295),
                            (W/2-260, 345, W/2-320, 415), (W/2-260, 345, W/2-100, 415),
                            (W/2, 345, W/2+140, 415)]:
        s += (f'<line x1="{xs}" y1="{ys}" x2="{xe}" y2="{ye}" stroke="#8258e0" '
              f'stroke-width="2"/>\n')
    s += narrative_box(
        "A001 net opgeleverd. Nu ontgrendeld: A002, A004, A013. Later opeenvolgend A003, A010, A009.",
        "Missen van kern-artefact = geen RvB-presentatie mogelijk = automatisch verlies.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 5: challenge
    s = svg_header()
    s += header("Stap 5 — Challenge met branching-keuzes", "Dilemma's met impact op metrieken", "#20a89a")
    s += render_card(80, 180, 380, 380,
                     "Legacy mainframe onmisbaar",
                     "COBOL-mainframe uit 1987 draait nog kernprocessen. Leverancier stopt met support.",
                     kind="challenge", accent="#ef476f")
    # keuzes rechts
    choices = [
        ("A", "Strangler-pattern modernisatie", "-€400, -20 debt, +20 mat, +200 XP", "#06d6a0"),
        ("B", "Externe COBOL-specialisten", "-€250, +5 debt, +100 XP", "#f5c542"),
        ("C", "Big-bang vervanging", "-€700, -30 debt, -15 stake", "#ef476f"),
        ("D", "Documenteer en freeze", "+10 debt, +10 gov, +75 XP", "#8258e0"),
    ]
    for i, (letter, label, effect, color) in enumerate(choices):
        y = 200 + i * 85
        s += (f'<rect x="500" y="{y}" width="720" height="70" rx="8" fill="#1a1f3a" '
              f'stroke="{color}" stroke-width="2"/>\n')
        s += (f'<text x="530" y="{y+30}" fill="{color}" font-size="20" font-weight="800">'
              f'{letter}</text>\n')
        s += (f'<text x="580" y="{y+28}" fill="#f0f3ff" font-size="16" font-weight="700">'
              f'{esc(label)}</text>\n')
        s += (f'<text x="580" y="{y+52}" fill="#a4acc9" font-size="13">{esc(effect)}</text>\n')
    s += narrative_box(
        "Als CIO kies je A (Strangler-pattern) — vereist wel dat je Transformation Roadmap-artefact hebt.",
        "Sommige keuzes vereisen specifiek artefact. Zonder cascade = suboptimale keuze.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 6: dashboard
    s = svg_header()
    s += header("Stap 6 — Team-dashboard", "12 metrieken samen bijhouden", "#20a89a")
    metrics = [
        ("Business Value", 65, "#06d6a0"),
        ("Stakeholder", 72, "#06d6a0"),
        ("Governance", 58, "#f5c542"),
        ("Digital Maturity", 45, "#f5c542"),
        ("Innovation", 40, "#f5c542"),
        ("Security", 35, "#ef476f"),
        ("Technical Debt", 25, "#06d6a0"),
    ]
    for i, (name, val, color) in enumerate(metrics):
        row = i % 4
        col = i // 4
        x = 100 + col * 610
        y = 200 + row * 90
        s += (f'<text x="{x}" y="{y-5}" fill="#f0f3ff" font-size="15" font-weight="700">'
              f'{esc(name)}</text>\n')
        s += (f'<text x="{x+560}" y="{y-5}" text-anchor="end" fill="{color}" '
              f'font-size="15" font-weight="700">{val}/100</text>\n')
        s += hp_bar(x, y+5, 560, 18, val, 100, color=color)
    s += narrative_box(
        "Elke actie beweegt metrieken. Team-dashboard is single-source-of-truth voor jullie voortgang.",
        "Eindscore bepaalt of RvB-presentatie slaagt: 8-aspect gewogen berekening (max 100).")
    s += "</svg>"
    beats.append(("beat", s))

    beats.append(("outro", outro(
        "🏛️ Speel zelf",
        "Dragon1-methodiek · geen combat · presenteer aan de RvB",
        "icthorse.nl/EnterpriseQuest/v2/",
        accent="#20a89a")))

    return beats


# =========================================================
# VIDEO 4: v2 ANALOG - Dragon1 als bordspel
# =========================================================

def v2_analog_beats():
    beats = []

    beats.append(("intro", intro(
        "Dragon1 Architect's Journey",
        "Analoge Print & Play — workshop-editie",
        "PnP · 2-8 spelers · 90-120 min", "#20a89a",
        tagline2="Dragon1-methodiek · fysieke artefact-cascade op tafel")))

    # Beat 1: componenten
    s = svg_header()
    s += header("Componenten in de doos", "Speciaal voor workshop-context", "#20a89a")
    items = [
        ("🎲", "1× D6", "voor events"),
        ("🗂", "125 kaarten", "M+C+E+A+Ach"),
        ("📜", "8 tableaus", "rollen A4"),
        ("🎯", "Cascade-veld", "artefact-stapels"),
        ("📊", "A3 dashboard", "team-gedeeld"),
        ("🗺️", "4×4 bord", "16 locaties"),
    ]
    for i, (icon, title, sub) in enumerate(items):
        col = i % 3
        row = i // 3
        x = 250 + col * 300
        y = 220 + row * 180
        s += (f'<rect x="{x-100}" y="{y-40}" width="200" height="140" rx="12" '
              f'fill="#1a1f3a" stroke="#20a89a" stroke-width="1"/>\n')
        s += (f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="46">{icon}</text>\n')
        s += (f'<text x="{x}" y="{y+50}" text-anchor="middle" fill="#f5c542" '
              f'font-size="16" font-weight="700">{esc(title)}</text>\n')
        s += (f'<text x="{x}" y="{y+72}" text-anchor="middle" fill="#a4acc9" '
              f'font-size="12">{esc(sub)}</text>\n')
    s += narrative_box(
        "PnP-kosten: €35 thuis, €90 copyshop, €65-80 via The Game Crafter.",
        "Ideaal voor consultancy-firma's, EA-cursussen (HAN, Nyenrode), Dragon1-community-events.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 2: setup dashboard + cascade
    s = svg_header()
    s += header("Setup — dashboard + cascade-veld", "Team-single-source-of-truth op tafel", "#20a89a")
    # dashboard links
    s += (f'<rect x="80" y="180" width="500" height="400" rx="12" fill="#1a1f3a" '
          f'stroke="#20a89a" stroke-width="2"/>\n')
    s += (f'<text x="330" y="215" text-anchor="middle" fill="#f5c542" font-size="18" '
          f'font-weight="700">📊 Dashboard-vel A3</text>\n')
    for i, name in enumerate(["Business Value", "Stakeholder", "Governance", "Digital Mat.",
                                "Innovation", "Security", "Tech Debt"]):
        y = 250 + i * 42
        s += (f'<text x="110" y="{y+15}" fill="#f0f3ff" font-size="14">{esc(name)}</text>\n')
        s += hp_bar(280, y, 280, 15, 40+i*7, 100, color="#20a89a")
    # cascade-veld rechts
    s += (f'<rect x="640" y="180" width="560" height="400" rx="12" fill="#1a1f3a" '
          f'stroke="#f5c542" stroke-width="2"/>\n')
    s += (f'<text x="920" y="215" text-anchor="middle" fill="#f5c542" font-size="18" '
          f'font-weight="700">🎯 Cascade-veld</text>\n')
    # 5 lege slots
    for i, label in enumerate(["Vision", "Principles", "Business", "Applicatie", "Technology"]):
        x = 680 + (i % 3) * 165
        y = 250 + (i // 3) * 140
        s += (f'<rect x="{x}" y="{y}" width="140" height="110" rx="8" '
              f'fill="#232a4a" stroke="#8258e0" stroke-width="2" '
              f'stroke-dasharray="6,3"/>\n')
        s += (f'<text x="{x+70}" y="{y+35}" text-anchor="middle" fill="#8258e0" '
              f'font-size="16" font-weight="700">{esc(label)}</text>\n')
        s += (f'<text x="{x+70}" y="{y+70}" text-anchor="middle" fill="#8f97ad" '
              f'font-size="12">nog leeg</text>\n')
    s += narrative_box(
        "Dashboard en cascade-veld liggen naast bord. Elke ronde updaten jullie samen.",
        "Bij artefact-opleveren: leg fysieke kaart op cascade-slot met required-tab.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 3: mission uitvoeren
    s = svg_header()
    s += header("Beurt 3 — CIO speelt Mission M001", "Vision Blueprint opleveren", "#20a89a")
    # mission-kaart links
    s += render_card(60, 180, 380, 380,
                     "Ontwikkel Enterprise Vision",
                     "Faciliteer directie-sessie. Levert A001 Vision Blueprint.",
                     kind="mission", accent="#06d6a0")
    # arrow
    s += (f'<text x="480" y="380" fill="#f5c542" font-size="40">➜</text>\n')
    # cascade nu met A001
    s += (f'<rect x="560" y="200" width="640" height="360" rx="12" fill="#1a1f3a" '
          f'stroke="#f5c542" stroke-width="2"/>\n')
    s += (f'<text x="880" y="235" text-anchor="middle" fill="#f5c542" font-size="18" '
          f'font-weight="700">Cascade-veld</text>\n')
    # A001 nu op tafel
    s += (f'<rect x="600" y="260" width="180" height="120" rx="8" fill="#f5c542" '
          f'stroke="#f5c542" stroke-width="3"/>\n')
    s += (f'<text x="690" y="295" text-anchor="middle" fill="#1a1200" '
          f'font-size="14" font-weight="700">A001</text>\n')
    s += (f'<text x="690" y="325" text-anchor="middle" fill="#1a1200" '
          f'font-size="16" font-weight="900">Vision</text>\n')
    s += (f'<text x="690" y="350" text-anchor="middle" fill="#1a1200" '
          f'font-size="16" font-weight="900">Blueprint</text>\n')
    # rest nog leeg
    for i, label in enumerate(["Principles", "Strategy", "Cap Map", "Roadmap"]):
        x = 810 + (i % 2) * 190
        y = 260 + (i // 2) * 140
        s += (f'<rect x="{x}" y="{y}" width="170" height="120" rx="8" '
              f'fill="#232a4a" stroke="#8258e0" stroke-width="2" '
              f'stroke-dasharray="6,3"/>\n')
        s += (f'<text x="{x+85}" y="{y+65}" text-anchor="middle" fill="#8258e0" '
              f'font-size="16" font-weight="700">{esc(label)}</text>\n')
    s += narrative_box(
        "CIO speelt Mission M001 en legt A001 Vision-kaart fysiek op cascade-veld.",
        "Dashboard-metrieken +25 businessValue, +30 stakeholder, +10 governance, -€100 budget.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 4: challenge en team-overleg
    s = svg_header()
    s += header("Beurt 5 — Challenge om tafel bespreken", "Team stemt over aanpak", "#20a89a")
    s += render_card(60, 180, 380, 380,
                     "Legacy mainframe onmisbaar",
                     "COBOL-mainframe stopt met support. Kies aanpak (A/B/C/D).",
                     kind="challenge", accent="#ef476f")
    # rondom kaart 4 rollen die overleggen
    for i, (icon, name, y_off) in enumerate([("🏛️", "EA", 220), ("🎛️", "CIO", 340),
                                                ("🛡️", "SecA", 460), ("💼", "IT-Mgr", 350)]):
        x = 720 if i < 2 else 1050
        y = 220 if i in (0, 2) else 380
        s += role_badge(x, y, icon, name, "#20a89a", active=(i == 1))
        # bubble
        if i == 1:
            s += (f'<rect x="{x-100}" y="{y+70}" width="200" height="30" rx="15" fill="#f5c542"/>\n')
            s += (f'<text x="{x}" y="{y+90}" text-anchor="middle" fill="#1a1200" '
                  f'font-size="12" font-weight="700">"Strangler-pattern"</text>\n')
    s += narrative_box(
        "Team bespreekt: A (Strangler) vereist Roadmap-artefact. CIO stelt A voor, EA + SecA akkoord.",
        "Bij consensus: leg oplossing op tafel, apply effect. Dashboard: -€400, -20 debt, +20 maturity.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 5: RvB-eindpresentatie
    s = svg_header()
    s += header("Beurt 20 — RvB-eindpresentatie", "8-aspect gewogen score", "#20a89a")
    # score
    s += (f'<text x="{W/2}" y="200" text-anchor="middle" fill="#f5c542" font-size="80" '
          f'font-weight="900">78/100</text>\n')
    s += (f'<text x="{W/2}" y="240" text-anchor="middle" fill="#06d6a0" font-size="24" '
          f'font-weight="700">"Goed — RvB tekent voor volgende fase"</text>\n')
    # 8 aspecten
    aspects = [
        ("Strategie", 82, "#06d6a0"), ("Business-fit", 75, "#06d6a0"),
        ("Info-integriteit", 68, "#f5c542"), ("Applicatie", 72, "#06d6a0"),
        ("Technologie", 74, "#06d6a0"), ("Security", 58, "#f5c542"),
        ("Innovatie", 65, "#f5c542"), ("Governance", 88, "#06d6a0"),
    ]
    for i, (name, val, color) in enumerate(aspects):
        col = i % 2
        row = i // 2
        x = 200 + col * 500
        y = 300 + row * 60
        s += (f'<text x="{x}" y="{y+15}" fill="#f0f3ff" font-size="14">{esc(name)}</text>\n')
        s += (f'<text x="{x+380}" y="{y+15}" text-anchor="end" fill="{color}" '
              f'font-size="14" font-weight="700">{val}</text>\n')
        s += hp_bar(x, y+25, 380, 12, val, 100, color=color)
    s += narrative_box(
        "Facilitator berekent gewogen score. Boven 75 = RvB-akkoord voor volgende fase.",
        "Verbeterpunten op zwakste aspecten (info-integriteit, security, innovatie) worden huiswerk.")
    s += "</svg>"
    beats.append(("beat", s))

    beats.append(("outro", outro(
        "📦 Workshop-tool",
        "Cascade-artefact fysiek op tafel · team-consensus zichtbaar",
        "icthorse.nl/EnterpriseQuest/docs/analog_v2_dragon1.pdf",
        accent="#20a89a")))

    return beats


# =========================================================
# VIDEO 5: v3 DIGITAL - Train Your Dragon AI-governance
# =========================================================

def v3_digital_beats():
    beats = []

    beats.append(("intro", intro(
        "🐉 Train Your Dragon",
        "EnterpriseQuest v3 — Agentic AI Governance",
        "v0.3.0-Turing", "#ff8c42",
        tagline2="Draak = AI drift + rogue agents · Gouverneur-mechaniek")))

    # Beat 1: 8 rollen v3
    s = svg_header()
    s += header("Stap 1 — 8 AI-Governance rollen", "Van AIGO tot Prompt Engineer", "#ff8c42")
    roles = [("🏛️", "AIGO", "#ff8c42"), ("🧠", "ML Eng", "#43d5f5"),
             ("🗄️", "Data", "#06d6a0"), ("🛡️", "SecA", "#ef476f"),
             ("⚖️", "Ethics", "#f5c542"), ("⚙️", "MLOps", "#8258e0"),
             ("🎛️", "CTO", "#20a89a"), ("📝", "PE", "#DA70D6")]
    for i, (icon, name, color) in enumerate(roles):
        row = i // 4
        col = i % 4
        x = 200 + col * 260
        y = 220 + row * 170
        active = (i == 0)  # AIGO
        s += role_badge(x, y, icon, name, color, active)
    s += (f'<text x="{W/2}" y="565" text-anchor="middle" fill="#f5c542" '
          f'font-size="18" font-weight="700">➤ AI Governance Officer gekozen</text>\n')
    s += narrative_box(
        "AIGO krijgt +15 Compliance, +5 Determinisme, +5 Trust. Special ability: Policy Sweep.",
        "Elke rol heeft unieke stats. AIGO is de bewaker van AI-policy en dwingt reflectie af.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 2: bord 5x3
    s = svg_header()
    s += header("Stap 2 — 5×3 AI-landscape", "Van Data Warehouse naar Drift Dragon", "#ff8c42")
    locs = [("📊", "DataWH"), ("🗂", "Registry"), ("🤖", "Runtime"),
            ("🏛️", "GovBoard"), ("⚖️", "Ethics"), ("📡", "Monitor"),
            ("🌐", "Vendor"), ("🧪", "Sandbox"), ("📝", "Prompts"),
            ("🔁", "Feedback"), ("📞", "Escalate"), ("📋", "Compl"),
            ("👤", "HITL"), ("📜", "Audit"), ("🐉", "DRAGON")]
    for i, (icon, name) in enumerate(locs):
        col = i % 5
        row = i // 5
        x = 200 + col * 200
        y = 200 + row * 120
        is_dragon = (i == 14)
        color = "#ef476f" if is_dragon else "#ff8c42"
        active = (i == 0)  # start
        sw = 4 if (active or is_dragon) else 1
        stroke = "#f5c542" if active else color
        bg = "#4a1c1c" if is_dragon else "#1a1f3a"
        s += (f'<rect x="{x-80}" y="{y-45}" width="160" height="90" rx="8" fill="{bg}" '
              f'stroke="{stroke}" stroke-width="{sw}"/>\n')
        s += (f'<text x="{x}" y="{y-8}" text-anchor="middle" font-size="24">{icon}</text>\n')
        s += (f'<text x="{x}" y="{y+25}" text-anchor="middle" fill="#f0f3ff" '
              f'font-size="12" font-weight="700">{esc(name)}</text>\n')
    s += narrative_box(
        "15 locaties = het AI-landschap. Draak op tile 14 groeit door 3 fases: Hallucination → Tool-Abuse → Autonomous.",
        "D6 movement. Bij drift ≥ 30 wakker; ≥ 60 Tool-Abuse; = 100 game-over.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 3: opportunity kaart
    s = svg_header()
    s += header("Stap 3 — Opportunity kaart", "AI-use-case: kies deterministisch/stochastisch/hybride", "#ff8c42")
    s += render_card(60, 180, 380, 380,
                     "Nieuwe RAG voor helpdesk",
                     "Business vraagt AI-chatbot met interne kennis. Snel of grondig?",
                     kind="opportunity", accent="#06d6a0")
    choices = [
        ("A", "Deploy zonder guardrails (LLM-native)", "+15 inn, +8 drift, -5 trust", "#ef476f"),
        ("B", "Deploy met guardrails + evaluatie ⚖", "+10 inn, +5 det, +5 trust, -€50", "#06d6a0"),
        ("C", "Pilot in sandbox, geen prod-data", "+5 inn, +3 trust, -€20", "#f5c542"),
    ]
    for i, (letter, label, effect, color) in enumerate(choices):
        y = 200 + i * 110
        s += (f'<rect x="500" y="{y}" width="720" height="95" rx="8" fill="#1a1f3a" '
              f'stroke="{color}" stroke-width="2"/>\n')
        s += (f'<text x="540" y="{y+40}" fill="{color}" font-size="24" font-weight="900">'
              f'{letter}</text>\n')
        s += (f'<text x="590" y="{y+35}" fill="#f0f3ff" font-size="16" font-weight="700">'
              f'{esc(label)}</text>\n')
        s += (f'<text x="590" y="{y+60}" fill="#a4acc9" font-size="13">{esc(effect)}</text>\n')
    s += (f'<text x="590" y="215" fill="#f5c542" font-size="12" font-weight="700">'
          f'⚖ Gouverneur-check vereist bij B</text>\n')
    s += narrative_box(
        "AIGO kiest B (guardrails). Kaart heeft ⚖-icoon: Gouverneur-check verplicht.",
        "Als je skipt: +5 drift-schade + 1 in rogue-teller. 3 skips in 5 beurten = rogue agent spawn.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 4: Gouverneur-modal
    s = svg_header()
    s += header("Stap 4 — ⚖ Vraag de Gouverneur", "4 policy-vragen aan tafel bespreken", "#ff8c42")
    # gouverneur symbol
    s += (f'<circle cx="{W/2}" cy="180" r="55" fill="#f5c542" stroke="#f5c542" '
          f'stroke-width="4"/>\n')
    s += (f'<text x="{W/2}" y="200" text-anchor="middle" fill="#1a1200" font-size="60">'
          f'⚖</text>\n')
    s += (f'<text x="{W/2}" y="270" text-anchor="middle" fill="#f5c542" font-size="18" '
          f'font-weight="700">Verzoeker → Gouverneur → Data</text>\n')
    questions = [
        ("Q1", "Geldige zakelijke reden?", True),
        ("Q2", "Data-scope juist voor rol?", True),
        ("Q3", "Retentie- en logging-plan?", True),
        ("Q4", "AVG/AI Act/DORA + intern?", False),
    ]
    for i, (qid, q, checked) in enumerate(questions):
        y = 320 + i * 55
        cbg = "#06d6a0" if checked else "#232a4a"
        s += (f'<rect x="200" y="{y}" width="880" height="45" rx="6" fill="#1a1f3a" '
              f'stroke="#8258e0" stroke-width="1"/>\n')
        s += (f'<rect x="220" y="{y+10}" width="26" height="26" rx="4" fill="{cbg}" '
              f'stroke="#f5c542" stroke-width="2"/>\n')
        if checked:
            s += (f'<text x="233" y="{y+29}" text-anchor="middle" fill="#1a1200" '
                  f'font-size="18" font-weight="900">✓</text>\n')
        s += (f'<text x="260" y="{y+28}" fill="#f5c542" font-size="16" font-weight="700">'
              f'{qid}</text>\n')
        s += (f'<text x="300" y="{y+28}" fill="#f0f3ff" font-size="15">{esc(q)}</text>\n')
    s += (f'<text x="{W/2}" y="570" text-anchor="middle" fill="#ef476f" font-size="18" '
          f'font-weight="700">3/4 bevestigd — Q4 open → toegang GEWEIGERD</text>\n')
    s += narrative_box(
        "Team bespreekt: Q4 (AVG-check) is nog niet duidelijk. Als AIGO kies je: skip niet, doe eerst DPIA.",
        "4/4 = toegang + Compliance/Data +3. <4 = heroverweeg. Skip = +5 drift.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 5: threat + drift
    s = svg_header()
    s += header("Stap 5 — 🐉 Threat: Model drift gedetecteerd", "Drift-metriek stijgt richting fase 2", "#ff8c42")
    s += render_card(60, 180, 380, 380,
                     "🐉 Model drift +12%",
                     "AI hallucineert meer. Klanten klagen over verkeerde adviezen.",
                     kind="threat", accent="#ef476f")
    # metrieken rechts met drift
    metrics = [
        ("Trust", 45, "#f5c542"),
        ("Compliance", 62, "#06d6a0"),
        ("Determinisme", 55, "#f5c542"),
        ("Data", 60, "#06d6a0"),
        ("Innovation", 70, "#06d6a0"),
        ("Drift-schade", 45, "#ef476f"),
    ]
    for i, (name, val, color) in enumerate(metrics):
        y = 210 + i * 55
        s += (f'<text x="500" y="{y+15}" fill="#f0f3ff" font-size="15" font-weight="700">'
              f'{esc(name)}</text>\n')
        s += (f'<text x="1180" y="{y+15}" text-anchor="end" fill="{color}" font-size="15" '
              f'font-weight="700">{val}/100</text>\n')
        s += hp_bar(500, y+22, 680, 15, val, 100, color=color)
    s += (f'<text x="840" y="565" text-anchor="middle" fill="#ef476f" font-size="16" '
          f'font-weight="700">⚠ Drift ≥ 30 → Hallucination Wraith actief · -2 Trust/beurt</text>\n')
    s += narrative_box(
        "Drift-metriek stijgt van 33 naar 45. De draak is nu Hallucination Wraith en veroorzaakt schade per beurt.",
        "Antwoord: rollback naar vorig model (-8 drift, -€30 budget) of add guardrails (⚖ Gouverneur).")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 6: draak-encounter
    s = svg_header()
    s += header("Stap 6 — Draak-encounter tile 14", "Readiness-check tegen draak-fase", "#ff8c42")
    s += (f'<text x="200" y="200" text-anchor="middle" fill="#ef476f" font-size="80">🐉</text>\n')
    s += (f'<text x="200" y="270" text-anchor="middle" fill="#ef476f" font-size="22" '
          f'font-weight="700">Hallucination</text>\n')
    s += (f'<text x="200" y="295" text-anchor="middle" fill="#ef476f" font-size="22" '
          f'font-weight="700">Wraith</text>\n')
    s += (f'<text x="200" y="335" text-anchor="middle" fill="#a4acc9" font-size="14">'
          f'HP 100 · -2 Trust/beurt</text>\n')
    # vs
    s += (f'<text x="{W/2}" y="230" text-anchor="middle" fill="#f5c542" font-size="60" '
          f'font-weight="900">⚔</text>\n')
    # readiness box
    s += (f'<rect x="640" y="180" width="580" height="360" rx="12" fill="#1a1f3a" '
          f'stroke="#f5c542" stroke-width="2"/>\n')
    s += (f'<text x="930" y="220" text-anchor="middle" fill="#f5c542" font-size="18" '
          f'font-weight="700">Team readiness</text>\n')
    stats = [("Trust", 45, 200), ("Compliance", 62, 200), ("Determinisme", 55, 200),
             ("Data Sov", 60, 200)]
    for i, (name, val, req) in enumerate(stats):
        y = 260 + i * 45
        s += (f'<text x="670" y="{y}" fill="#f0f3ff" font-size="14">{esc(name)}</text>\n')
        s += hp_bar(830, y-15, 300, 15, val, 100, color="#20a89a")
    total = 45+62+55+60
    s += (f'<text x="930" y="465" text-anchor="middle" fill="#f5c542" font-size="20" '
          f'font-weight="800">Som = 222 / 200 vereist ✓</text>\n')
    s += (f'<text x="930" y="500" text-anchor="middle" fill="#a4acc9" font-size="14">'
          f'+ 3 artefacten (nodig: 1) ✓</text>\n')
    s += narrative_box(
        "Team heeft genoeg governance-fundering (som 222/200 + 3 artefacten). Wraith fase-1 verslagen!",
        "Trust +8, Drift -15. Ga naar tile 0. Volgende fase: Tool-Abuse Serpent bij drift ≥ 60.")
    s += "</svg>"
    beats.append(("beat", s))

    beats.append(("outro", outro(
        "🐉 Speel zelf",
        "Regie op determinisme + Gouverneur-check · verslaat de draak",
        "icthorse.nl/EnterpriseQuest/v3/",
        accent="#ff8c42")))

    return beats


# =========================================================
# VIDEO 6: v3 ANALOG - Train Your Dragon als bordspel
# =========================================================

def v3_analog_beats():
    beats = []

    beats.append(("intro", intro(
        "🐉 Train Your Dragon",
        "Analoge Print & Play — AI Governance workshop",
        "PnP · 3-8 spelers · 90-120 min", "#ff8c42",
        tagline2="Fysieke Gouverneur-plaat · draak-suppressie op tafel")))

    # Beat 1: componenten met Gouverneur-plaat
    s = svg_header()
    s += header("Componenten — met Gouverneur-plaat", "Kern-mechaniek fysiek zichtbaar", "#ff8c42")
    items = [
        ("⚖", "Gouverneur-plaat", "4 draaischijven"),
        ("🎲", "1× D6 + D8", "movement + events"),
        ("🗂", "110 kaarten", "Opp+Threat+Gov+Event+Ach"),
        ("📜", "8 tableaus", "AI-rollen"),
        ("📊", "A3 dashboard", "6 metrieken + drift"),
        ("🗺️", "5×3 bord", "15 AI-locaties"),
    ]
    for i, (icon, title, sub) in enumerate(items):
        col = i % 3
        row = i // 3
        x = 250 + col * 300
        y = 220 + row * 180
        # highlight Gouverneur
        stroke = "#f5c542" if i == 0 else "#ff8c42"
        sw = 3 if i == 0 else 1
        s += (f'<rect x="{x-100}" y="{y-40}" width="200" height="140" rx="12" '
              f'fill="#1a1f3a" stroke="{stroke}" stroke-width="{sw}"/>\n')
        s += (f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="46">{icon}</text>\n')
        s += (f'<text x="{x}" y="{y+50}" text-anchor="middle" fill="#f5c542" '
              f'font-size="16" font-weight="700">{esc(title)}</text>\n')
        s += (f'<text x="{x}" y="{y+72}" text-anchor="middle" fill="#a4acc9" '
              f'font-size="12">{esc(sub)}</text>\n')
    s += narrative_box(
        "Gouverneur-plaat is HET kern-artefact (A4-karton met 4 draaischijven). Ligt centraal op tafel.",
        "PnP-kosten: €40 thuis, €100 copyshop, €70-90 via The Game Crafter.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 2: setup rond tafel met plaat centraal
    s = svg_header()
    s += header("Setup — Gouverneur-plaat in het midden", "Rondom: bord + dashboard + rollen", "#ff8c42")
    # centrum: Gouverneur-plaat
    s += (f'<rect x="{W/2-200}" y="240" width="400" height="240" rx="16" fill="#1a1f3a" '
          f'stroke="#f5c542" stroke-width="4"/>\n')
    s += (f'<text x="{W/2}" y="280" text-anchor="middle" fill="#f5c542" font-size="60">'
          f'⚖</text>\n')
    s += (f'<text x="{W/2}" y="335" text-anchor="middle" fill="#f5c542" font-size="20" '
          f'font-weight="800">GOUVERNEUR-PLAAT</text>\n')
    s += (f'<text x="{W/2}" y="365" text-anchor="middle" fill="#a4acc9" font-size="14">'
          f'Verzoeker → Gouverneur → Data</text>\n')
    # 4 vraagblokjes
    for i in range(4):
        x = W/2 - 175 + i * 100
        s += (f'<circle cx="{x}" cy="425" r="18" fill="#232a4a" stroke="#f5c542" '
              f'stroke-width="2"/>\n')
        s += (f'<text x="{x}" y="431" text-anchor="middle" fill="#f5c542" '
              f'font-size="12" font-weight="700">Q{i+1}</text>\n')
    # bord links
    s += (f'<rect x="80" y="240" width="240" height="240" rx="12" fill="#1a1f3a" '
          f'stroke="#ff8c42" stroke-width="2"/>\n')
    s += (f'<text x="200" y="280" text-anchor="middle" fill="#ff8c42" font-size="14" '
          f'font-weight="700">🗺️ BORD 5×3</text>\n')
    s += (f'<text x="200" y="365" text-anchor="middle" fill="#ef476f" font-size="30">🐉</text>\n')
    # dashboard rechts
    s += (f'<rect x="960" y="240" width="240" height="240" rx="12" fill="#1a1f3a" '
          f'stroke="#8258e0" stroke-width="2"/>\n')
    s += (f'<text x="1080" y="280" text-anchor="middle" fill="#8258e0" font-size="14" '
          f'font-weight="700">📊 A3 dashboard</text>\n')
    for i, name in enumerate(["Trust", "Compliance", "Determinisme", "Drift"]):
        y = 320 + i * 32
        color = "#ef476f" if name == "Drift" else "#20a89a"
        s += (f'<text x="985" y="{y}" fill="#f0f3ff" font-size="11">{esc(name)}</text>\n')
        s += hp_bar(985, y+5, 200, 8, 30+i*15, 100, color=color)
    s += narrative_box(
        "Gouverneur-plaat is HET kern-object. Bij elke ⚖-kaart moet team samen 4 draaischijven zetten.",
        "3-8 spelers rond de tafel, elke rol eigen tableau. Beurt-teller telt af van 1 tot 15.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 3: opportunity + kaart trekken
    s = svg_header()
    s += header("Beurt 4 — AIGO trekt Opportunity", "RAG-helpdesk met ⚖-icoon", "#ff8c42")
    s += render_card(60, 180, 380, 380,
                     "RAG voor helpdesk",
                     "Business vraagt AI-chatbot met interne kennis. Kies A/B/C ⚖",
                     kind="opportunity", accent="#06d6a0")
    # arrow
    s += (f'<text x="480" y="380" fill="#f5c542" font-size="40">➜</text>\n')
    # team overlegt
    s += (f'<rect x="560" y="200" width="640" height="360" rx="12" fill="#1a1f3a" '
          f'stroke="#8258e0" stroke-width="2"/>\n')
    s += (f'<text x="880" y="235" text-anchor="middle" fill="#f5c542" font-size="18" '
          f'font-weight="700">Team-overleg</text>\n')
    # 4 rollen bespreken
    positions = [("🏛️", "AIGO", 660, 300), ("🧠", "ML", 800, 300),
                 ("⚖️", "Eth", 940, 300), ("🛡️", "SecA", 1080, 300)]
    for icon, name, x, y in positions:
        s += role_badge(x, y, icon, name, "#ff8c42", active=(name == "AIGO"))
    s += (f'<text x="880" y="430" text-anchor="middle" fill="#f5c542" font-size="16" '
          f'font-weight="700">"We kiezen B — met guardrails.</text>\n')
    s += (f'<text x="880" y="455" text-anchor="middle" fill="#f5c542" font-size="16" '
          f'font-weight="700">Maar dan wel Gouverneur-check."</text>\n')
    s += (f'<text x="880" y="510" text-anchor="middle" fill="#a4acc9" font-size="14" '
          f'font-style="italic">Ethics-Rep: "Q4 hebben we niet, doe DPIA eerst."</text>\n')
    s += narrative_box(
        "Team beslist samen: B is de aanpak. Maar eerst Gouverneur-check aan tafel.",
        "Facilitator leest 4 Q's voor. Team draait fysiek de schijven op de plaat.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 4: Gouverneur-check aan tafel
    s = svg_header()
    s += header("⚖ Gouverneur-check aan tafel", "Draaischijven fysiek zetten", "#ff8c42")
    # grote Gouverneur-plaat centraal
    s += (f'<rect x="200" y="180" width="880" height="360" rx="16" fill="#1a1f3a" '
          f'stroke="#f5c542" stroke-width="4"/>\n')
    s += (f'<text x="{W/2}" y="220" text-anchor="middle" fill="#f5c542" font-size="20" '
          f'font-weight="800">⚖ GOUVERNEUR-PLAAT</text>\n')
    # 4 vraag-blokjes met draaischijf
    questions = [
        ("Q1", "Zakelijke reden?", True),
        ("Q2", "Data-scope OK?", True),
        ("Q3", "Retentie/logging?", True),
        ("Q4", "AVG/AI Act OK?", False),
    ]
    for i, (qid, q, checked) in enumerate(questions):
        x = 260 + i * 210
        y = 320
        # draaischijf
        bg = "#06d6a0" if checked else "#ef476f"
        s += (f'<circle cx="{x}" cy="{y}" r="55" fill="{bg}" stroke="#f5c542" '
              f'stroke-width="3"/>\n')
        s += (f'<text x="{x}" y="{y+8}" text-anchor="middle" fill="#1a1200" '
              f'font-size="30" font-weight="900">{"✓" if checked else "?"}</text>\n')
        s += (f'<text x="{x}" y="{y+90}" text-anchor="middle" fill="#f5c542" '
              f'font-size="14" font-weight="700">{qid}</text>\n')
        s += (f'<text x="{x}" y="{y+110}" text-anchor="middle" fill="#a4acc9" '
              f'font-size="11">{esc(q)}</text>\n')
    s += narrative_box(
        "Team draait Q1-Q3 op ✓. Q4 op ? (twijfel over AVG). Uitspraak: 3/4 = toegang GEWEIGERD.",
        "AIGO stelt voor: eerst DPIA doen. Team akkoord. Actie wordt opnieuw ingezet in volgende beurt.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 5: rogue agent-token op tafel
    s = svg_header()
    s += header("Beurt 8 — Rogue Agent spawnt", "3 Gouverneur-skips in 5 beurten", "#ff8c42")
    # rogue tracker
    s += (f'<rect x="80" y="180" width="480" height="360" rx="12" fill="#1a1f3a" '
          f'stroke="#ef476f" stroke-width="2"/>\n')
    s += (f'<text x="320" y="220" text-anchor="middle" fill="#ef476f" font-size="20" '
          f'font-weight="700">⚠ Rogue Tracker</text>\n')
    # 5 turn-slots met skip-status
    for i, skipped in enumerate([True, False, True, False, True]):
        x = 130 + i * 90
        y = 260
        color = "#ef476f" if skipped else "#20a89a"
        s += (f'<rect x="{x-30}" y="{y}" width="60" height="60" rx="6" fill="{color}"/>\n')
        s += (f'<text x="{x}" y="{y+40}" text-anchor="middle" fill="#1a1200" '
              f'font-size="30" font-weight="900">{"✗" if skipped else "✓"}</text>\n')
        s += (f'<text x="{x}" y="{y+80}" text-anchor="middle" fill="#a4acc9" '
              f'font-size="12">B{i+3}</text>\n')
    s += (f'<text x="320" y="400" text-anchor="middle" fill="#ef476f" font-size="18" '
          f'font-weight="700">3 skips in 5 beurten</text>\n')
    s += (f'<text x="320" y="430" text-anchor="middle" fill="#ef476f" font-size="24" '
          f'font-weight="900">→ ROGUE SPAWN!</text>\n')
    # rogue token
    s += (f'<circle cx="900" cy="330" r="70" fill="#000" stroke="#ef476f" '
          f'stroke-width="4"/>\n')
    s += (f'<text x="900" y="345" text-anchor="middle" fill="#ef476f" font-size="60">🤖</text>\n')
    s += (f'<text x="900" y="440" text-anchor="middle" fill="#ef476f" font-size="16" '
          f'font-weight="700">Rogue Agent #1</text>\n')
    s += (f'<text x="900" y="465" text-anchor="middle" fill="#a4acc9" font-size="13">'
          f'-3 Compliance / -3 Trust per beurt</text>\n')
    s += narrative_box(
        "Team heeft 3 keer Gouverneur geskipt binnen 5 beurten. Rogue Agent-token op willekeurige locatie.",
        "Verwijderen: 1 beurt op zelfde locatie + Governance-kaart spelen. Anders elke beurt schade.")
    s += "</svg>"
    beats.append(("beat", s))

    # Beat 6: eindpresentatie
    s = svg_header()
    s += header("Beurt 15 — RvB-eindpresentatie", "Uitkomst en verhaal", "#ff8c42")
    s += (f'<text x="{W/2}" y="220" text-anchor="middle" fill="#f5c542" font-size="60" '
          f'font-weight="900">🏆 68/100</text>\n')
    s += (f'<text x="{W/2}" y="270" text-anchor="middle" fill="#20a89a" font-size="22" '
          f'font-weight="700">"Sterke governance-basis"</text>\n')
    s += (f'<text x="{W/2}" y="300" text-anchor="middle" fill="#a4acc9" font-size="16" '
          f'font-style="italic">Draak fase 1 verslagen, fase 2 nog actief</text>\n')
    # aspecten
    aspects = [
        ("Trust", 65), ("Compliance", 75),
        ("Determinisme", 62), ("Data Sovereignty", 70),
        ("Innovation", 55), ("Draak-suppressie", 58),
        ("Governance-artefacten", 60), ("(bouwde er 3/5)", None),
    ]
    for i, (name, val) in enumerate(aspects):
        col = i % 2
        row = i // 2
        x = 250 + col * 500
        y = 355 + row * 45
        if val is not None:
            color = "#06d6a0" if val >= 65 else ("#f5c542" if val >= 50 else "#ef476f")
            s += (f'<text x="{x}" y="{y+15}" fill="#f0f3ff" font-size="14">{esc(name)}</text>\n')
            s += (f'<text x="{x+400}" y="{y+15}" text-anchor="end" fill="{color}" '
                  f'font-size="14" font-weight="700">{val}</text>\n')
        else:
            s += (f'<text x="{x+80}" y="{y+15}" fill="#a4acc9" font-size="13" '
                  f'font-style="italic">{esc(name)}</text>\n')
    s += narrative_box(
        "Score 68 = draak fase 1 verslagen, maar governance-basis nog niet compleet.",
        "Verbeterpunten worden huiswerk voor de organisatie. Debrief-vragen sluiten sessie af.")
    s += "</svg>"
    beats.append(("beat", s))

    beats.append(("outro", outro(
        "🐉 Workshop-tool",
        "Fysieke Gouverneur-plaat · team-consensus op AI-governance",
        "icthorse.nl/EnterpriseQuest/docs/analog_v3_ai.pdf",
        accent="#ff8c42")))

    return beats


# =========================================================
# RENDERER
# =========================================================

def render_video(name, beats, target_seconds=60):
    print(f"\n=== Rendering: {name} ({len(beats)} beats) ===")
    frame_dir = FRAMES_ROOT / name
    frame_dir.mkdir(exist_ok=True)
    # cleanup old
    for f in frame_dir.glob("*.png"):
        f.unlink()

    for i, (kind, svg) in enumerate(beats):
        png_path = frame_dir / f"beat_{i:02d}.png"
        cairosvg.svg2png(bytestring=svg.encode("utf-8"),
                         output_width=W, output_height=H,
                         write_to=str(png_path))
        print(f"  beat {i:02d} — {kind}")

    duration = target_seconds / len(beats)
    concat_path = frame_dir / "concat.txt"
    frame_files = sorted(frame_dir.glob("beat_*.png"))
    with open(concat_path, "w") as f:
        for p in frame_files:
            f.write(f"file '{p.name}'\n")
            f.write(f"duration {duration}\n")
        f.write(f"file '{frame_files[-1].name}'\n")

    out = VIDEOS / f"{name}_demo.mp4"
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_path),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        "-vf", f"scale={W}:{H}",
        str(out),
    ]
    subprocess.run(cmd, check=True, cwd=frame_dir,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    size_kb = out.stat().st_size / 1024
    print(f"  ✓ {out.name} ({size_kb:.0f} KB, ~{target_seconds}s)")


def main():
    videos = [
        ("v1_digital", v1_digital_beats(), 60),
        ("v1_analog",  v1_analog_beats(),  60),
        ("v2_digital", v2_digital_beats(), 60),
        ("v2_analog",  v2_analog_beats(),  60),
        ("v3_digital", v3_digital_beats(), 60),
        ("v3_analog",  v3_analog_beats(),  60),
    ]
    for name, beats, secs in videos:
        render_video(name, beats, secs)

    print("\n=== Klaar ===")
    for name, _, _ in videos:
        p = VIDEOS / f"{name}_demo.mp4"
        if p.exists():
            print(f"  {p.name}: {p.stat().st_size/1024:.0f} KB")


if __name__ == "__main__":
    main()
