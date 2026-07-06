# EnterpriseQuest v1 — Analoge Print & Play uitwerking

**Basis:** digitale versie `v1/EnterpriseQuest.html` (v0.0.1-Zachman)
**Vorm:** fysiek bordspel + kaartspel + dobbelstenen + tokens
**Doelgroep:** 2-6 spelers, 90-150 minuten, 16+ (business/tech basiskennis handig)
**Setting:** één architect moet de organisatie redden van de Chaos Architect — fantasy-RPG-flavour over EA/TOGAF/cloud/security/data/AI-content.

---

## 1. Ontwerpprincipes bij vertaling digitaal → analoog

| Digitaal element | Analoge oplossing | Reden |
|---|---|---|
| D20 movement (steps = ⌊d/2⌋+1 boven 15) | 1× D20 per speler | Direct 1:1 overneembaar |
| D20 combat (crit 20 / miss 1) | Zelfde D20 hergebruiken | Bekende RPG-conventie |
| LocalStorage autosave | Speler-dashboard-vel met potlood | Save = beurten opschrijven op vel |
| Web Audio API tones | Optioneel: klein muziek-cue-kaartje voorleest facilitator | Sfeer, niet essentieel |
| Auto-shuffle 250-kaartendeck | Fysiek shuffelen per deck-type | Gebruikelijk in bordspel |
| Level-up modal | Level-track op speler-vel + level-up-kaartje | Papieren XP-balk |
| Night-cycle elke 5 beurten | Beurten-teller-kraaltje aan bord + kaart "Nacht valt" | Bekend uit Betrayal/Mansions |
| 10 klassen-passives | Kartonnen klassen-tableau met blijvende regel-tekst | Vergelijkbaar met Root/Scythe |

**Grondregel bij twijfel:** kies de eenvoudigste analoge oplossing en gebruik "de facilitator/spelleider beslist" als ontsnappingsclausule voor edge-cases.

---

## 2. Componentenlijst

### 2.1 Bord (1×)

- **Formaat:** 60 × 60 cm gevouwen (2 helften), gedrukt op linnen-karton of stevig papier bij PnP
- **Layout:** 40 tegels in een spiraal-parcours van tile 0 (Kick-off Plaza) naar tile 39 (Throne of Chaos)
- **12 regio's** met eigen achtergrondkleur (zie tabel §3.1)
- **3 portaal-tegels** (10, 20, 30) verbonden met portaal-lijnen tussen elkaar
- **Startpunt** links onderin (tile 0), **eindboss** rechts bovenin (tile 39)

### 2.2 Kaartdecks (4× decks, 250 kaarten totaal)

| Deck | Aantal | Kaart-achterkant | Trekt bij tile-type |
|---|---|---|---|
| **Quest**    | 100 | groen  | tile-type `quest` |
| **Chaos**    |  50 | zwart  | tile-type `chaos` |
| **Artifact** |  50 | goud   | tile-type `artifact` |
| **Event**    |  50 | blauw  | tile-type `event` |

Kaartformaat: standaard Euro-poker (63 × 88 mm).

### 2.3 Monster-kaarten (22×, apart deck met rood achterkant)

- 15 minions/elites (tile-type `combat` in regio)
- 6 mid-bosses (tile-type `boss`, één per grote regio)
- 1 final boss (Chaos Architect) op 3 kaartjes — fase 1 / 2 / 3

### 2.4 Speler-tokens

- **6 klassen-pionnen** (unieke kleur + icoon):
  - 🏛️ Enterprise Architect
  - 🧩 Solution Architect
  - 🏢 Business Architect
  - 🛡️ Security Architect
  - 🗄️ Data Architect
  - ⚙️ DevOps Architect
- **6 klassen-tableaus** (A5 kartonnen vellen) met special ability + starting stats + level-track (1-10)

### 2.5 Dobbelstenen

- **1× D20 per speler** (kleur bij pion)
- **1× D6** voor Chaos Architect (fase-toewijzing bij random events in eindboss)

### 2.6 Tokens & markers

| Token | Aantal | Kleur | Gebruik |
|---|---|---|---|
| HP-marker              | 6 (1/speler) | rood      | Verplaats over HP-track op tableau |
| XP-marker              | 6            | groen     | XP-track (0-1000+) |
| Budget-cash (€)        | 200 fiches (waarden 50/100/500) | goud     | Startbudget, quest-kosten, boss-drops |
| Stakeholder-token      | 60           | wit       | Sociaal kapitaal — 3 startkapitaal per speler |
| Security-token         | 40           | blauw     | Security-status voor speler-vel |
| Chaos-token            | 40           | zwart     | Wereld-chaos-tracker (gedeeld) |
| Night-cycle marker     | 1            | maan      | Elke 5 beurten omgedraaid |
| Achievement-kaarten    | 51           | zilver    | Deck met behaalde achievements |
| Artefact-slots         | 5 per speler | —         | Icoontjes op klassen-tableau: scroll / compass / crystal / armor / weapon (+crown voor Chief Architect) |

### 2.7 Facilitator-map

- Regelboek (30 pag)
- Combat-referentiekaart (2× A5, dubbelzijdig)
- Referentiekaarten Chaos Architect (3 fases)
- Achievement-checklist (A4)

---

## 3. Setup

### 3.1 Bord neerleggen

Regio-volgorde (kleur):

| # | Regio | Kleur (hex) | Difficulty | Tiles |
|---|---|---|---|---|
| 1 | Business Village   | #8FBC8F | 1 | 0-4 |
| 2 | Vendor Market      | #FF8C00 | 2 | 5-9 |
| 3 | Integration Bridge | #20B2AA | 3 | 10-13 |
| 4 | Data Forest        | #228B22 | 3 | 14-19 |
| 5 | Cloud Mountains    | #87CEEB | 3 | 20-23 |
| 6 | Innovation Tower   | #FFD700 | 2 | 24-26 |
| 7 | Legacy Dungeon     | #5C4033 | 4 | 27-29 |
| 8 | Security Castle    | #4B0082 | 4 | 30-33 |
| 9 | Compliance Swamp   | #556B2F | 4 | 34-36 |
| 10 | AI Temple         | #DA70D6 | 5 | 37 |
| 11 | Executive Palace  | #B22222 | 4 | 38 |
| 12 | Digital Portal    | #000000 | 5 | 39 |

Elke tile toont:
- **Type-icoon** (quest/chaos/event/artifact/combat/boss/rest/portal/start)
- **Label** (bv "Zero Trust Fundering", "GDPR-lek", "Vendor Hydra")
- **Regio-kleur** rondom rand

### 3.2 Deck-shuffling

Shuffle elk deck apart en leg met achterkant boven op de bijbehorende slots naast het bord (4 quest/chaos/artifact/event + 1 monster-deck opzij + 3 gestapelde Chaos Architect-fasekaarten in aparte enveloppe).

### 3.3 Klasse-keuze

Elke speler kiest een klasse-tableau:

| Klasse | Special Ability | Start-HP | Start-attack | Start-defense |
|---|---|---|---|---|
| Enterprise Architect | *Big Picture* — 1× per spel: bekijk top 5 van elk deck | 40 | 8  | 8  |
| Solution Architect  | *Blueprint Sprint* — 1× per spel: solo een quest tekenen (skip roll) | 40 | 9  | 7  |
| Business Architect  | *Stakeholder Rally* — +2 stakeholder-tokens bij elke succesvolle quest | 45 | 6  | 9  |
| Security Architect  | *Threat Shield* — 1× per gevecht: negeer 1 aanval volledig | 45 | 7  | 11 |
| Data Architect      | *Data Lineage* — 1× per spel: onthul komende 3 tegels | 40 | 8  | 8  |
| DevOps Architect    | *Automated Pipeline* — +1 XP-multiplier voor build-quests | 42 | 9  | 8  |

Startloadout per speler:
- **HP-track:** vol (40-45 afhankelijk van klasse)
- **XP:** 0
- **Budget:** €1000
- **Stakeholder:** 3 tokens
- **Security:** 0
- **Level:** 1 (Junior Architect)
- Trek **2 starter Artifact-kaarten** (common-rariteit); mag er 1 uitrusten in vrije slot

### 3.4 Bord-startpositie

Alle pionnen op tile 0 (Kick-off Plaza).

---

## 4. Speelverloop

### 4.1 Beurten in tafel-volgorde

Per beurt van een speler:

1. **Start-fase**
   - Ontvang budget-per-beurt uit uitgeruste artifacten (bv Cloud Crystal +€20/beurt)
   - Herstel 0 HP tenzij op rest-tile
   - Check "Night-cycle": elke 5e beurt (na alle spelers) → nachtkaart lezen (extra chaos-effect)

2. **Move-fase**
   - Rol de D20
   - **Steps** = ⌊worp/2⌋ + 1 als worp ≤ 15, anders steps = worp − 15 + 8 (bonus voor hoge worp; snelle vooruitgang)
   - Voorbeeld: worp 10 → 6 stappen; worp 18 → 11 stappen
   - Verplaats pion langs het parcours (zonder over-shoot: stop bij de tile die je bereikt)
   - **Portaal-tile** (10/20/30) bereikt? → mag optioneel teleporteren naar een andere portaal-tile (kies)

3. **Tile-fase** (voer effect uit)

| Tile-type | Actie |
|---|---|
| `start`    | (alleen begin) Ontvang €1000 + 3 stakeholder-tokens |
| `quest`    | Trek Quest-kaart, lees effect, apply |
| `chaos`    | Trek Chaos-kaart, apply (meestal negatief) |
| `event`    | Trek Event-kaart, apply (kan branching-choice hebben) |
| `artifact` | Trek Artifact-kaart, mag uitrusten in vrije slot of ruilen |
| `combat`   | Trek monster-kaart die bij regio hoort → combat-flow (§5) |
| `boss`     | Trek regio-boss-kaart → combat-flow (mid-boss = boven-tafel) |
| `rest`     | Herstel HP (5 of 8 afhankelijk van tile) |
| `portal`   | Kies teleporteren naar andere portal (al gedaan in move-fase) |

4. **Level-up-check**
   - XP-drempels: 100 / 250 / 500 / 900 / 1500 / 2200 / 3000 / 4000 / 5500 XP
   - Bij overschrijden: +1 level, +5 max HP, +1 attack óf +1 defense (keuze)

5. **Actie-fase (optioneel)**
   - Ruil artefacten met andere spelers (facilitator kan onderhandelen faciliteren)
   - Verkoop 1 artefact voor 50% waarde → budget
   - Verplaats stakeholder-tokens naar quest-drempels op tableau

6. **Einde beurt** — volgende speler.

### 4.2 Vals-alarm-check "Chaos oploopt"

Aan het einde van élke ronde (alle spelers gehad):
- Als het gezamenlijke Chaos-token-aantal boven 20 komt: trek 1 extra Chaos-kaart en apply op de speler met de meeste XP.
- Boven 30: Chaos Architect (fase 1) verschijnt bij tile 39 en beweegt langzaam richting spelers.

### 4.3 Kaart-anatomie

**Voorbeeld Quest-kaart:**

```
┌─────────────────────────────────┐
│ Q004 · Zero Trust Fundering  ⚔️ │
│─────────────────────────────────│
│ Sla de fundering van het        │
│ Zero Trust bastion; nooit       │
│ vertrouwen, altijd verifiëren.  │
│─────────────────────────────────│
│ Regio: Security Castle · DL 4   │
│─────────────────────────────────│
│ EFFECT (moet accepteren):       │
│ +300 XP · −€250                 │
│ +35 Security · +10 Stakeholder  │
│ HP: 0                           │
└─────────────────────────────────┘
```

**Voorbeeld Chaos-kaart:**

```
┌─────────────────────────────────┐
│ C012 · CIO Reorg                │
│─────────────────────────────────│
│ Nieuwe CIO wijzigt het          │
│ IT-portfolio: alle roadmaps     │
│ terug naar de tekentafel.       │
│─────────────────────────────────│
│ EFFECT:                         │
│ −100 XP · −€150 · −5 Stakeholder│
│ Trek daarnaast een Event-kaart. │
└─────────────────────────────────┘
```

**Voorbeeld Artifact-kaart (uitrust-slot):**

```
┌─────────────────────────────────┐
│ A004 · Security Shield  🛡️      │
│ Rarity: common · Slot: armor    │
│─────────────────────────────────│
│ Beukelaar met OWASP-runen.      │
│─────────────────────────────────│
│ PASSIVE (permanent zolang       │
│ uitgerust):                     │
│  +3 defense                     │
│  +10 security-per-beurt         │
└─────────────────────────────────┘
```

**Voorbeeld Event-kaart (branching):**

```
┌─────────────────────────────────┐
│ E017 · Auditor komt langs       │
│─────────────────────────────────│
│ De externe auditor stelt vragen │
│ over je change-proces.          │
│─────────────────────────────────│
│ KIES ÉÉN:                       │
│ A) Toon Runbook Codex           │
│    → +50 XP · +2 Stakeholder    │
│    (vereist: dit artifact)      │
│ B) Improviseer met CAB          │
│    → +25 XP · 50% kans −€100    │
│ C) Vraag uitstel                │
│    → −5 Stakeholder             │
└─────────────────────────────────┘
```

---

## 5. Combat (D20-mechanica)

### 5.1 Initiatief

Speler rolt D20; monster heeft vaste initiative-waarde op kaart. Hoogste eerst. Bij gelijk: speler eerst.

### 5.2 Aanval-worp

```
Aanvals-totaal = D20 + attack-stat + eventuele artifact-bonus
Defense-drempel = monster-defense
Hit als: aanvals-totaal ≥ defense-drempel
```

**Crit / Miss:**
- Natuurlijke 20 → automatisch hit, **dubbele schade**
- Natuurlijke 1 → automatisch miss, verlies 1 stakeholder-token (embarrassment)

### 5.3 Schade berekening

```
Schade = (aanvals-totaal − defense-drempel) + 5
```

(Minimum 5 schade bij hit, geen negatieve schade)

Monster verliest HP op referentiekaart; bij 0 HP: overwinning → XP + budget beloningen.

### 5.4 Speciale monster-abilities

Elke monster-kaart heeft één abilities-regel. Voorbeelden:

| Monster | Ability |
|---|---|
| Legacy Dragon        | *Breath of Technical Debt*: +2 chaos-token per beurt |
| Shadow IT Goblins    | *Swarm*: verschijnt altijd in groep van 3 (drie kaartjes tegelijk) |
| Data Kraken          | *Tentacle Grip*: bij hit → speler skipt volgende beurt |
| Compliance Ghost     | *Phase*: 50% kans (D6 ≥ 4) om schade te ontwijken |
| Prompt Injection Djinn | *Override*: negeert eenmalig defense-bonus |

### 5.5 Vluchten

Speler mag vluchten aan begin van elke combat-ronde:
- Rol D20. Bij ≥ 14 gelukt: keer terug naar vorige tile, verlies 5 HP + 1 stakeholder.
- Bij < 14 gefaald: monster krijgt gratis aanval.

### 5.6 Final Boss (Chaos Architect, 3 fases)

Kaart-drieluik:

| Fase | Naam | HP | Attack | Defense | Speciaal |
|---|---|---|---|---|---|
| 1 | The Whiteboard Phase   | 200 | 25 | 18 | *Scope Explosion* — trek elke 3 rondes 1 extra minion-kaart |
| 2 | The Implementation Phase | 350 | 30 | 22 | *Cascading Failure* — bij <50% HP: 3 aanvallen per beurt |
| 3 | The Chaos Ascendant    | 500 | 38 | 28 | *Reality Rewrite* — negeert 1× alle uitgeruste artefacten + roept 2 minions op |

Fases worden opeenvolgend gespeeld: fase 2 kaart verschijnt zodra fase 1 verslagen is, etc. Spelers herstellen niets tussen fases (verhoogt spanning).

**Winst voor coop-partij:** Chaos Architect fase 3 verslagen.
**Winst voor solo-partij:** Chaos Architect fase 3 verslagen én HP > 0.

---

## 6. Progressie en tellingen op speler-vel

Elk klassen-tableau bevat vier tracks:

```
HP     [1][2][3]...[45]    ← markeer met rood token
XP     [0][100][250]...[5500+]  ← groen token schuift
LEVEL  [1][2][3][4][5][6][7][8][9][10]
BUDGET (schrijf op met potlood, of fiches op vak "€")
STAKEHOLDER (max 20 tokens in stakeholder-vak)
SECURITY  0-100 track
```

En vijf artifact-slots:

```
[scroll] [compass] [crystal] [armor] [weapon]  (+[crown] bij level 10)
```

---

## 7. Achievements

51 achievements analoog geïmplementeerd:

- **Achievement-deck** ligt open naast bord. Voorbeeld-kaartjes: "Legendary Slayer — versla 3 mid-bosses", "Cloud Master — voltooi 5 Cloud Mountains quests", "Zero Trust Champion — heb Zero-Trust Aegis uitgerust bij final boss".
- Zodra voorwaarde vervuld: pak kaart, leg op eigen tableau. Sommige achievements geven **eenmalige bonus** (bv +100 XP, +1 artifact-slot).
- Voor lange campagnes: houd achievements bij op vervolg-campagne-vel.

---

## 8. Winstconditie en scoring

### 8.1 Solo (1 speler)

Winst: verslaat Chaos Architect fase 3.
Verlies: HP = 0 óf 40 beurten voorbij zonder tile 39 bereikt.

### 8.2 Coop (2-6 spelers)

Winst: gezamenlijk final boss verslaan. Iedereen mag rollen tijdens boss-fight.
Score-ranking:

```
Score = XP × level + (behaalde achievements × 100)
       + budget-bonus (−100 per rondes over 25)
       − chaos-token-penalty (×5)
```

Hoogste score = "Grand Chief Architect" van de sessie.

### 8.3 Competitief (2-4 spelers)

Alternatieve modus: elke speler probeert éérst Chaos Architect te verslaan (los van elkaar). PvP-tegels 22 en 33 laten spelers duel-worp doen om HP van elkaar af te bijten.

---

## 9. Print & Play checklist

- [ ] Bord op A2/A1 geprint of gestikt uit 4× A4-tegels
- [ ] 250 kaart-tekst-vellen laminated (of gesleeved in Ultra Pro)
- [ ] 22 monster-referentie-kaartjes (A6)
- [ ] 6 klassen-tableau's (A5)
- [ ] 1 D20 per speler + 1 D6 voor facilitator
- [ ] Tokens: HP, XP, budget, stakeholder, security, chaos, night, achievement
- [ ] Facilitator-map: regelboek (dit document), combat-referentie, achievement-checklist
- [ ] Optioneel: 3D-print pionnen in de 6 klasse-iconen
- [ ] Optioneel: MP3-track met Web-Audio-jingles voor sfeer

Kosten PnP-productie (indicatief 2026):
- Zelf-print A4 kleur: **€25** (thuis) — €80 (copyshop met stevige karton)
- Print-on-demand (The Game Crafter, MakePlayingCards): **€45-60** per doos
- Kleinschalige oplage (100 stuks) via BoardGameLab / MPC: **€25-32** per doos

---

## 10. Verschillen digitaal ↔ analoog

| Aspect | Digitaal (HTML5) | Analoog (bordspel) |
|---|---|---|
| Speeltijd | 45-90 min | 90-150 min (langer door fysieke handelingen) |
| Speleraantal | 1 (single-player) | 1-6 (uitbreiding coop/competitief) |
| Random events | JavaScript RNG | D20 + gemarkeerde tables |
| Save/resume | LocalStorage autosave | Foto van speler-vel met telefoon |
| Achievements | Auto-detection op predicates | Manueel bijhouden via checklist |
| Chaos-oploop | Berekend per beurt | Gedeelde Chaos-tokens (max 40) |
| Night cycle | Elke 5 beurten | Elke 5 rondes; night-kaart wordt hardop voorgelezen |
| Tutorial | Interactieve modal | 5-minuten intro door facilitator (script bijgevoegd) |

---

## 11. Facilitator-tips

- **Sessie-tijd:** Reserveer 3 uur voor volledige sessie inclusief 15 min intro + 30 min debrief.
- **Debrief-vragen** (voor workshop-context):
  1. Welke architectuur-beslissingen in het spel herken je uit je eigen praktijk?
  2. Welke artifact zou je in real-life willen hebben — en waarom?
  3. Welke monster (Vendor Hydra, Legacy Dragon, etc.) worstel je momenteel mee?
  4. Zou je Chaos Architect fase 1, 2 of 3 karakteriseren als jouw huidige uitdaging?
- **Variant "Consultant-modus":** Spelers zijn extern architect-team; ze delen budget-pool.
- **Variant "Junior-focus":** Alleen tiles 0-19; verslaat mid-boss Chaos CIO om te winnen.

---

## 12. Verantwoording ontwerp-keuzes

| Keuze | Alternatief overwogen | Argumentatie |
|---|---|---|
| 40 tiles (parcours) | 6×6 grid (36 tiles) | Digitale versie heeft 40 tiles; behoud 1:1 lengte |
| D20 hergebruiken | D6 + kaartjes | D20 is bekend uit D&D-tradition; drukt EA-nerd-flavour uit |
| 5 artifact-slots | 3 slots | Kaartcollectie stimuleert engagement; digitale versie kent slot-icoons |
| Gedeelde Chaos-tokens | Individuele chaos | Coop-ervaring vereist gedeelde druk; sluit aan bij "organisatie in crisis"-narratief |
| Fysiek klassen-tableau | Alleen kaartjes | Vergelijkbaar met Root/Scythe; nodig voor level/HP/XP-tracks |
| Vluchten bij ≥ 14 | Automatisch vluchten | Risk/reward — matcht digitale keuzes |

---

## 13. Openstaande vragen bij playtest

- **Balancing:** Loopt de beurt-teller-druk (25 rondes plafond) niet uit de hand bij 6 spelers?
- **Kaart-lengte:** Zijn 250 kaarten te veel voor 2-3 uur sessie? Overweeg subsets per regio.
- **Nacht-cyclus:** Werkt "elke 5e ronde" ook bij hoge speler-aantallen (5 rondes = 30 beurten)?
- **Solo-modus:** Is 40 rondes zonder tile 39 een realistisch verlies-criterium?
- **Kaarttekst-lengte:** Passen alle event-effecten op poker-formaat (63×88 mm)?

---

## Bijlagen (kaartuitgifte-overzichten)

- **Quest 100** — zie `content/quests.json` (100 kaarten, verspreid over regio's)
- **Chaos 50** — zie `content/chaos.json`
- **Artifact 50** — zie `content/artifacts.json` (5 rariteits-tiers: common/rare/epic/legendary)
- **Event 50** — zie `content/events.json` (19 met branching-choices)
- **Monsters 22** — zie `content/monsters.json`
- **Achievements 51** — zie `content/achievements.json`

---

**Versie doc:** analog_v1_rpg v0.1
**Gebaseerd op digitale versie:** v0.0.1-Zachman (commit `aae8e69`)
**Auteur:** Claude Opus 4.7 (1M context) namens Christian Glebbeek
**Licentie:** AGPL-3.0 (matches repo)
