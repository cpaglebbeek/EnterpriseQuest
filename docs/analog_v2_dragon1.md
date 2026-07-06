# EnterpriseQuest v2 — Analoge Print & Play uitwerking (Dragon1)

**Basis:** digitale versie `v2/EnterpriseQuest.html` (v0.2.0-Paauwe)
**Vorm:** fysiek bordspel + kaartspel + tokens + dashboard-vellen
**Doelgroep:** 2-8 spelers (1 rol per speler), 90-120 minuten, 18+ (workshop-context / EA-training)
**Setting:** de architect(en) moeten een organisatie **toekomstbestendig** maken volgens de **Dragon1-methodiek** en dat aan de RvB presenteren. Geen combat, geen HP, wel budget/stakeholder-druk en verplichte artefact-cascade.

---

## 1. Ontwerpprincipes bij vertaling digitaal → analoog

| Digitaal element | Analoge oplossing | Reden |
|---|---|---|
| 4×4 organisatie-grid | Bord met 16 locatie-tegels in 4×4-raster | Direct 1:1 overneembaar |
| 8 rollen met 9-attributen | Rollen-tableau's (A4) met 9 attribuut-tracks | Vergelijkbaar met Pandemic-rollenkaart |
| 15 artefacten met required-cascade | Kaarten met vereist-icoon; leg fysiek op elkaar | Zichtbare dependency-graph op tafel |
| 40 missies + 40 uitdagingen + 30 events | 3 aparte decks (M/U/E) van totaal 110 kaarten | Digitale versie kent zelfde split |
| 12 dashboard-metrieken | Dashboard-vel (A3) met 12 tracks + tokens | Team-dashboard = single source of truth |
| Cascade `required: ["A001"]` | Kartonnen tab-icoon aan onderkant nieuwe kaart | Fysiek zichtbaar: welke voorloper vereist |
| 8-aspect eindscore | Score-vel met 8 gaskaartjes (0-10 draaischijven) | Puur cijfermatig — geen speech acteren |
| RvB-presentatie eindgame | Facilitator schrijft "RvB-verhaal" op basis van score | Geeft workshop-context serieuze afsluiter |
| LocalStorage autosave | Foto van dashboard-vel per ronde | Traceerbaar herstart-punt |

**Grondregel:** deze versie is een **serieuze management-simulatie** — geen fantasy-flavour, geen dobbelsteen-luck. Uitkomsten hangen af van keuzes en volgorde. D6 wordt alleen gebruikt voor event-randomizers.

---

## 2. Componentenlijst

### 2.1 Bord (1×)

- **Formaat:** 60 × 60 cm, 4×4-raster van 16 locatie-tegels
- Elke tegel toont:
  - Icoon + naam
  - Primary Dragon1-concept (bv "Business Function", "Value Stream")
  - Locatie-kleur (donkerblauw voor bestuur, groen voor business, geel voor finance, etc.)
- **Centraal Dragon1-cascade-veld** (5 vakken onder bord): Vision → Principles → Business → Applicatie → Technology
- **Metric-dashboard-strip** rechts van bord (12 metrieken)

### 2.2 Locatie-tegels (16×, één per organisatie-onderdeel)

| # | Locatie | Primary Concept | Kleur (hex) |
|---|---|---|---|
|  1 | Directiekamer | Strategie | #1B2A49 |
|  2 | Strategiecentrum | Strategy Map | #2E4A7B |
|  3 | Business Domein | Business Function | #4B3F72 |
|  4 | HR | Actor & Role Model | #7A5C3E |
|  5 | Finance | Business Value & Cost Model | #C9A227 |
|  6 | Operations | Business Process | #37535E |
|  7 | Sales | Value Stream | #8C1C40 |
|  8 | Klantenservice | Customer Journey | #B76E39 |
|  9 | Applicatielandschap | Applicatie-portfolio | #274060 |
| 10 | Dataplatform | Information Architecture | #3E6680 |
| 11 | Integratielaag | Integration Architecture | #5B7B7A |
| 12 | Cloudplatform | Technology Platform | #4A6FA5 |
| 13 | Security Operations Center | Security Architecture | #2C2C54 |
| 14 | Innovatielab | Innovation Portfolio | #6A0DAD |
| 15 | Project Portfolio | Portfolio Management | #8E7C42 |
| 16 | Governance Board | Architecture Governance | #4B4B4B |

### 2.3 Rollen-tableau's (8×, één per rol)

| Rol | Icoon | Kern-attribuut(en) | Special Ability |
|---|---|---|---|
| Enterprise Architect | 🏛️ | Strategie 9, Governance 8 | *Big Picture* — 1×: toon samenhang alle locaties, +15 stakeholder bij strategisch artefact |
| Solution Architect | 🧩 | Tech 9, Innovation 7 | *Blueprint Sprint* — 1×: lever Solution Overview met 2× digitalMaturity-bonus |
| Business Architect | 🏢 | Business 10, Communicatie 9 | *Value Stream Insight* — 1×: onthul knelpunt in business-locatie, +10 businessValue bij VSM |
| Information Architect | 🗄️ | Data 10, Governance 8 | *Data Lineage* — 1×: toon data-keten tussen locaties, +50% effectiviteit Information Model |
| Security Architect | 🛡️ | Security 10, Governance 9 | *Threat Shield* — 1×: verlaag security-incident-impact naar nul, +8 security dat beurt |
| CIO | 🎛️ | Strategie 10, Leiderschap 10 | *Executive Mandate* — 1×: +20 budget-per-beurt + versnel artefact-goedkeuring 1 beurt |
| IT-Manager | 💼 | Leiderschap 9, Governance 8 | *Delivery Push* — 1×: lever project uit Portfolio 1 beurt eerder + 6 businessValue |
| Student EA | 🎓 | Innovation 8 | *Fresh Perspective* — 2× XP op elk artefact + 1× architectuur-quiz voor +10 op alle attributen |

Op tableau ook zichtbaar: **start-bonussen** en **9 attribuut-tracks** (waardes 1-10).

### 2.4 Kaartdecks

| Deck | Aantal | Achterkant | Doel |
|---|---|---|---|
| **Artefact**  |  15 | goud    | Dragon1-artefacten (12 verplicht + 3 extra) — met **required-tabs** |
| **Mission**   |  40 | groen   | Modelleer een artefact op een locatie |
| **Challenge** |  40 | rood    | Multiple-choice dilemma's (soms met required-artefact als voorwaarde voor beste keuze) |
| **Event**     |  30 | blauw   | Externe gebeurtenissen (28 met branching) |
| **Achievement** |  47 | zilver | Milestone-kaarten |

Kaartformaat: Euro-poker (63×88 mm).

### 2.5 Dashboard-vel (A3 gedeeld, gemeenschappelijk voor team)

12 metric-tracks in horizontale balken:

```
1.  Business Value            [0 ─────────── 100]
2.  Stakeholder Confidence    [0 ─────────── 100]
3.  Governance                [0 ─────────── 100]
4.  Digital Maturity          [0 ─────────── 100]
5.  Innovation                [0 ─────────── 100]
6.  Security                  [0 ─────────── 100]
7.  Technical Debt            [0 ─────────── 100] (hoger = slechter)
8.  Budget (€1000-startkapitaal, teller schuift)
9.  Budget-per-beurt (max ~50)
10. Beurten-teller (max 20 beurten)
11. XP-team-totaal
12. Chaos-teller (externe druk, 0-40)
```

Elke rol legt gekleurde marker op elke track — verplaatsingen bij missie/challenge/event.

### 2.6 Artefact-cascade-veld

Onder bord ligt de **cascade-graph**:

```
                    A001 Vision Blueprint
                    /       |          \
              A002 Strategy A004 Principles A013 Vision Poster
              /       \                |
        A003 Cap.Map   A010 Roadmap   A009 Governance
       /   |    \        /             |
   A005 A006 A015    A008 Tech      A012 Repository
    |    |   |         |
   A007 A014 A011      |
```

Kaarten worden fysiek op elkaar gelegd in dependency-volgorde: pas als voorloper op tafel ligt, mag opvolger uitgespeeld worden. Dit is **de kern-mechaniek** van v2.

### 2.7 Tokens

| Token | Kleur | Doel |
|---|---|---|
| Rol-pion (8×) | 8 unieke kleuren | Locatie-marker per speler |
| Metric-marker (12×, gedeeld) | zwart | Track-position dashboard |
| Beurten-token | wit | Beurten-teller |
| Artefact-status-token | 3 kleuren | in-uitvoering / opgeleverd / afgekeurd |
| Achievement-kaart-stack | zilver | Behaalde achievements per team |
| RvB-verhaal-kaart | rood | Alleen 1× aan einde van spel |

### 2.8 Dobbelsteen

- **1× D6** (alleen voor event-randomizers)

### 2.9 Facilitator-map

- Regelboek (dit document)
- Dragon1-methodiek-samenvatting (2× A5)
- Score-berekening-vel (8-aspect eindscore)
- RvB-presentatie-template (A4)

---

## 3. Setup

### 3.1 Bord neerleggen

- 4×4 grid platleggen; positioneer volgens onderstaande matrix (rijen = business-lagen):

|             | Kolom A | Kolom B | Kolom C | Kolom D |
|---|---|---|---|---|
| Rij 1 (Bestuur) | Directiekamer | Strategiecentrum | Governance Board | Finance |
| Rij 2 (Business) | Business Domein | Operations | Sales | Klantenservice |
| Rij 3 (Informatie / IT) | Applicatielandschap | Dataplatform | Integratielaag | Cloudplatform |
| Rij 4 (Innovatie / Ops) | HR | Innovatielab | Project Portfolio | Security Operations Center |

Elke tegel toont zijn primary Dragon1-concept.

### 3.2 Cascade-veld en decks

- Leg cascade-veld onder bord met 5 lege slots (Vision / Principles / Business / Applicatie / Technology)
- Leg alle 15 artefact-kaarten **omgekeerd naast bord** (spelers mogen kaartnamen zien, maar niet gebruiken zonder voorloper)
- Shuffle Mission, Challenge, Event, Achievement decks apart

### 3.3 Rol-keuze en start-metrieken

Elke speler kiest een rol-tableau. Start-metrieken worden opgeteld op gedeeld dashboard:

| Rol | Start-bonus |
|---|---|
| EA | +10 BusinessValue, +8 StakeholderConfidence, +5 Governance |
| SA | +6 BusinessValue, +8 DigitalMaturity, +4 StakeholderConfidence |
| BA | +12 BusinessValue, +6 StakeholderConfidence, +3 Governance |
| IA | +10 DigitalMaturity, +6 Governance, +3 BusinessValue |
| SecA | +15 Security, +6 Governance, +3 StakeholderConfidence |
| CIO | +8 BusinessValue, +12 StakeholderConfidence, +6 Governance |
| IT-Mgr | +8 Governance, +6 DigitalMaturity, +5 Budget-per-beurt |
| Student EA | +10 Innovation, +3 StakeholderConfidence, +2 BusinessValue |

Basis-startwaarden voor alle metrieken die niet in start-bonus staan: **20** (van 100).
Startbudget: **€1000**. Startbeurt: **1 van 20**.

### 3.4 Bord-startpositie

Alle rol-pionnen op **Directiekamer** (locatie 1). Elke rol krijgt "Enterprise Vision"-mission-briefing van facilitator.

---

## 4. Speelverloop

### 4.1 Ronde-structuur

Per ronde (= 1 beurt van elke speler):

1. **Facilitator opent** met datum + beurt-teller ("Beurt 3/20 — het is september, Q3-review nadert")
2. **Elke speler op tafel-volgorde:**
   - Beweeg pion max 2 tegels (orthogonaal, geen diagonaal)
   - Speel **één actie-type** (§4.2)
   - Update dashboard-metrieken
3. **Facilitator trekt Event-kaart** aan einde van ronde en past effect toe
4. **Beurt-teller +1**
5. **Facilitator meldt** cumulatieve metric-verandering + Dragon1-cascade-status

### 4.2 Acties per beurt (kies 1)

| Actie | Verloop |
|---|---|
| **A. Modelleer artefact** | Trek een Mission-kaart die aan je locatie hangt; controleer of vereist voorlopig artefact op cascade-veld ligt; leg de Mission af + leg bijbehorende artefact-kaart op cascade-veld; update metrieken |
| **B. Reageer op Challenge** | Trek Challenge-kaart, kies één van 3-4 opties (sommige vereisen artefact); apply effect |
| **C. Facilitator-actie** | Vraag facilitator om extra Event-kaart voor het team; kost 1 stakeholder-token |
| **D. Special Ability** | Speel je rol-special (1× per spel); zie §2.3 |
| **E. Diplomatie** | Overleg met andere speler over ruilen van special-ability-timing; ability blijft echter uniek per rol |
| **F. Overslaan** | Skip beurt (verlies 5 stakeholder-confidence door passiviteit) |

### 4.3 Cascade-check bij artefact-modelleren

Wanneer een speler een artefact wil neerleggen (via Mission of Special Ability), controleer:

```
Kaart X vereist: [A001]           → moet A001 op cascade-veld liggen? Ja/Nee
Kaart X vereist: [A002, A006]     → beide vereist? Ja/Nee
```

Als vereisten niet aanwezig:
- Mission blijft in de hand van speler; volgende beurt opnieuw proberen
- Alternatief: speler mag Mission opgeven → −10 stakeholder-confidence

### 4.4 Kaart-anatomie

**Voorbeeld Mission-kaart:**

```
┌─────────────────────────────────┐
│ M001 · Ontwikkel Enterprise     │
│         Vision voor directie    │
│─────────────────────────────────│
│ Faciliteer directie-sessie en   │
│ leg de Enterprise Vision vast   │
│ als eerste ankerpunt.           │
│─────────────────────────────────│
│ Levert artefact: A001 Vision    │
│ Locatie: Directiekamer          │
│ Difficulty: 3                   │
│─────────────────────────────────│
│ EFFECT:                         │
│ +250 XP · −€100                 │
│ +25 BusinessValue               │
│ +30 StakeholderConfidence       │
│ +10 Governance · +15 Innovation │
│ +10 DigitalMaturity             │
└─────────────────────────────────┘
```

**Voorbeeld Artefact-kaart:**

```
┌─────────────────────────────────┐
│ A007 · Information Model        │
│─────────────────────────────────│
│ Vereist: A005 (Business Ref)    │
│ Categorie: Informatie           │
│─────────────────────────────────│
│ Gestructureerd model van        │
│ kernbegrippen, entiteiten en    │
│ relaties.                       │
│─────────────────────────────────│
│ PASSIVE (zolang gemodelleerd):  │
│ +6 DigitalMaturity              │
│ +4 Governance                   │
│ +3 BusinessValue                │
└─────────────────────────────────┘
```

**Voorbeeld Challenge-kaart:**

```
┌─────────────────────────────────┐
│ CH001 · Legacy mainframe        │
│         onmisbaar               │
│─────────────────────────────────│
│ COBOL-mainframe uit 1987 draait │
│ nog kernprocessen. Leverancier  │
│ stopt met support.              │
│─────────────────────────────────│
│ Locatie: IT-Operations          │
│ Severity: 5                     │
│ Directe impact:                 │
│  +25 TechnicalDebt              │
│  −10 Innovation                 │
│  −15 DigitalMaturity            │
│─────────────────────────────────│
│ KIES ÉÉN:                       │
│ A) Strangler-pattern modernisatie│
│    → −€400 · −20 TechDebt       │
│    +20 DigitalMaturity · +200 XP│
│    ⚠️ Vereist: Transformation   │
│         Roadmap-artefact        │
│ B) Externe COBOL-experts        │
│    → −€250 · +5 TechDebt · +100 XP│
│ C) Big-bang vervanging          │
│    → −€700 · −30 TechDebt       │
│    −15 Stakeholder · +250 XP    │
│ D) Documenteer en freeze        │
│    → +10 TechDebt · +10 Gov ·   │
│      +75 XP                     │
└─────────────────────────────────┘
```

**Voorbeeld Event-kaart:**

```
┌─────────────────────────────────┐
│ E014 · Grote klant vraagt AI    │
│         propositie              │
│─────────────────────────────────│
│ Kies wie het initiatief neemt:  │
│ A) BA + Innovatielab           │
│    → +8 Innovation · +6 BizValue│
│ B) IA + Data Platform          │
│    → +6 DigitalMaturity        │
│    → +4 Governance             │
│ C) Wacht op AI-strategie       │
│    → −5 Stakeholder             │
└─────────────────────────────────┘
```

---

## 5. Cascade-mechanica (kern-mechaniek)

De Dragon1-methodiek eist een **strikte volgorde** van artefacten. Deze wordt in het spel bewaakt door de **required-tab** onderop elke kaart.

### 5.1 Cascade-graaf

```
     Layer 0 (Fundament)
     ┌────────────────────┐
     │ A001 Vision Bp     │
     └────────┬───────────┘
              │
     Layer 1 (Kader)
   ┌──────────┼──────────┐
   │          │          │
   ▼          ▼          ▼
  A002       A004       A013
  Strategy   Arch       Vision
  Map        Principles Poster
   │          │
   ▼          │
   │          ▼
  A003 ──────┴─── A009 Governance
  Cap Map
   ├── A005 ─── A007 Info Model
   ├── A015 (Value Stream)
   └── A010 Roadmap ── A011 Portfolio
              └── ─── A006 App Landscape
                     ├── A008 Tech Blueprint
                     └── A014 Solution Overview

     Layer x (Governance-lock)
      A012 Repository (vereist A004 + A009)
```

Volledig cascade-schema staat groter op facilitator-map (A3).

### 5.2 Speeltactiek

- Vroeg spel: focus Vision + Principles (voorwaarden voor alle latere lagen)
- Midden spel: Capability Map + Application Landscape (nodig voor Roadmap)
- Laat spel: Portfolio Dashboard + Architecture Repository (governance-locks + XP-multipliers)
- Missen van kern-artefact = geen RvB-presentatie mogelijk = verlies

---

## 6. Winstconditie en scoring

### 6.1 Eindsignaal

Het spel eindigt op **beurt 20**. Of eerder als:
- Alle 15 artefacten gemodelleerd → **vroege triomf** (score +50)
- Budget < €0 → **noodscenario** — RvB-presentatie mag nog wél, maar met −20 penalty
- TechnicalDebt > 80 én StakeholderConfidence < 30 → **automatisch verlies** (organisatie in crisis)

### 6.2 RvB-eindpresentatie (facilitator-flow)

Facilitator draait 8-aspect score-schijf en berekent:

| Aspect | Weging | Berekening |
|---|---|---|
| Strategische Richting | 15% | (BusinessValue + StakeholderConfidence) / 2 |
| Business-fit | 15% | BusinessValue |
| Informatie-integriteit | 10% | DigitalMaturity |
| Applicatie-portfolio | 10% | DigitalMaturity − TechnicalDebt/2 |
| Technologie-fundament | 10% | DigitalMaturity + Security/2 |
| Security & Compliance | 10% | Security |
| Innovatie & Groei | 10% | Innovation |
| Governance | 20% | Governance |

**Totaal-score = gewogen som (max 100)**.

### 6.3 Cijfer-uitkomst

| Score | Predicaat | Verbeterpunten |
|---|---|---|
| 90-100 | **Uitzonderlijk** — RvB is enthousiast, transformation-fund uitgebreid | Enkele feinschliff-punten |
| 75-89 | **Goed** — RvB tekent voor volgende fase | 2-3 verbeterpunten in Debrief |
| 60-74 | **Voldoende** — RvB akkoord, mits verbeterpunten | 4-5 verbeterpunten |
| 45-59 | **Onvoldoende** — RvB vraagt heroverweging | 6+ verbeterpunten |
| 0-44 | **Ontoereikend** — RvB stopt programma | Volledige heroverweging |

Facilitator vertelt vanuit RvB-perspectief het uitkomst-verhaal (5 min speech-template als bijlage).

### 6.4 Bonus: verbeterpunten-lijst

Elk aspect waarin < 60 gescoord: schrijf op **verbeterpunten-kaart** en overhandig aan team als vervolg-huiswerk.

---

## 7. Achievements

47 achievements verdeeld over categorieën:

- **Cascade-completion** (bv "Sluit A001 → A010 in ≤ 8 beurten")
- **Metric-max** (bv "Bereik Governance = 100")
- **Rol-specifiek** (bv "Als CIO: gebruik Executive Mandate 3× effectief")
- **Team-samenwerking** (bv "Presenteer alle 15 artefacten voor beurt 15")

Analoge implementatie: 47 achievement-kaarten liggen naast bord. Facilitator markeert vervulling per team.

---

## 8. Print & Play checklist

- [ ] Bord met 4×4-grid + cascade-veld (A2 met 4× A4-tegels of gestikt)
- [ ] 15 artefact-kaarten (met required-tabs onderkant)
- [ ] 40 mission-kaarten
- [ ] 40 challenge-kaarten
- [ ] 30 event-kaarten
- [ ] 47 achievement-kaarten
- [ ] 8 rollen-tableau's (A4)
- [ ] 1 gedeelde dashboard-vel (A3)
- [ ] 1 D6
- [ ] Tokens: rol-pionnen (8×), metric-markers (12×), status-tokens, beurten-token
- [ ] Facilitator-map: regelboek, Dragon1-samenvatting, RvB-template
- [ ] Optioneel: Wallet-card met alle 15 artefact-vereisten voor snelle referentie

Kostenraming:
- Zelf-print A4 kleur: **€35** (thuis)
- Copyshop (bord op 250 g karton): **€90**
- Print-on-demand: **€65-80** per doos (incl. dashboards laminated)

---

## 9. Verschillen digitaal ↔ analoog

| Aspect | Digitaal (HTML5) | Analoog (bordspel) |
|---|---|---|
| Speeltijd | 45-75 min | 90-120 min |
| Speleraantal | 1 speler kiest 1 rol | 2-8 spelers (1 rol per speler) |
| Cascade-check | JavaScript logica | Fysieke kaart-tab moet zichtbaar zijn |
| Random events | JavaScript RNG | D6 + kaart-tabellen |
| Dashboard | Live UI | A3-vel + fysieke tokens |
| RvB-presentatie | Modal met tekst-gen | Facilitator vertelt vanuit template |
| Autosave | LocalStorage | Foto per ronde |
| Dragon1-kennis | Tooltips | Facilitator-Dragon1-samenvatting bijgevoegd |

---

## 10. Facilitator-tips voor workshop-gebruik

- **Sessie-lengte:** 3 uur totaal (10 min intro, 90-100 min spel, 30 min debrief)
- **Team-samenstelling:** ideaal 4-6 spelers; mix van business en IT rollen
- **Reflectie-vragen debrief:**
  1. Welke artefact-cascade heb je gemist en waarom?
  2. Wanneer wilde je Vision Poster (A013) vroeger inzetten om stakeholders te betrekken?
  3. Kwam je in de knel bij Missing A004 → A009 → A012 (governance-lock)?
  4. Vertaalt dit naar jullie eigen organisatie? Waar staan jullie op Governance/DigitalMaturity?
- **Varianten:**
  - "Junior-modus" — alleen 8 kern-artefacten (skip A011, A013, A014, A015 + extra's)
  - "Governance-Focus" — start met TechnicalDebt = 60; forceer governance-first strategie
  - "Startup-modus" — 15 beurten in plaats van 20; nadruk op snel Vision + Application Landscape

---

## 11. Verantwoording ontwerp-keuzes

| Keuze | Alternatief | Argumentatie |
|---|---|---|
| 4×4-grid (16 locaties) | 5×5 met 25 locaties | Digitale versie kent 16 locaties; behoud 1:1 mapping |
| Fysieke cascade-veld | Kaartjes-stack in hand | Zichtbaarheid = kern-leermoment (Dragon1 vereist expliciete voorloper-check) |
| Gedeeld dashboard | Individuele dashboards | Team-samenwerking centraal; niet iedereen jaagt eigen KPI |
| Rol-specials 1× per spel | 1× per fase (per 5 beurten) | Digitale versie: 1× totaal — houd 1:1 |
| 20 beurten harde deadline | Open eind bij consensus | Simuleert Q1-Q4 kwartaal-druk uit realistische EA-praktijk |
| 8-aspect eindscore vs single score | Enkelvoudig totaalcijfer | 8-aspect = Dragon1-doctrine; matches digitale versie |

---

## 12. Openstaande vragen bij playtest

- **Cascade-blokkade:** wat als team pas op beurt 3 A001 kan neerleggen? → alle latere kaarten gestrand
- **Challenge-severity 5**: kan ook artefacten neerslaan? → in analoge versie: nee (te straf)
- **CIO Executive Mandate**: overpowered? →misschien beperken tot +15 budget-per-beurt in plaats van +20
- **Facilitator-load**: kan facilitator écht 3 uur volhouden met event-trekken en scoring bijhouden? Overweeg co-facilitator bij 6+ spelers
- **Print-kwaliteit rol-tableaus**: 9 attribuut-tracks op A4 leesbaar? Overweeg alternatief 3×3-matrix layout

---

## Bijlagen (kaartuitgifte-overzichten)

- **Artefact 15** — zie `v2/content/artefacts.json` (met required-cascade)
- **Mission 40** — zie `v2/content/missions.json`
- **Challenge 40** — zie `v2/content/challenges.json`
- **Event 30** — zie `v2/content/events.json` (28 met branching)
- **Achievement 47** — zie `v2/content/achievements.json`
- **Rollen 8** — zie `v2/content/roles.json`
- **Locaties 16** — zie `v2/content/locations.json`

---

**Versie doc:** analog_v2_dragon1 v0.1
**Gebaseerd op digitale versie:** v0.2.0-Paauwe (commit `7af45ec`)
**Auteur:** Claude Opus 4.7 (1M context) namens Christian Glebbeek
**Licentie:** AGPL-3.0 (matches repo)
**Dragon1-methodiek:** met dank aan Mark Paauwe (Dragon1-grondlegger)
