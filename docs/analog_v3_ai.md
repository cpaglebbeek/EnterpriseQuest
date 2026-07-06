# EnterpriseQuest v3 — Analoge Print & Play uitwerking

## Train Your Dragon (Agentic AI Governance Edition)

**Basis:** digitale versie `v3/EnterpriseQuest.html` (v0.3.0-Turing)
**Vorm:** fysiek bordspel + kaartspel + tokens + Gouverneur-plaat + policy-checklist
**Doelgroep:** 3-8 spelers, 90-120 minuten, workshop-context voor AI-Governance / Data-officer / CTO / CISO / architect-teams
**Setting:** de organisatie zet Agentic AI in. Autonome agents dreigen te ontsporen — model drift, data drift, rogue agents. Jullie taak: **regie op determinisme en stochasme + governance op data** via de **Gouverneur**-mechaniek. Versla de Drift Dragon in 3 fases voor beurt 15 om is.

---

## 1. Ontwerpprincipes bij vertaling digitaal → analoog

| Digitaal element | Analoge oplossing | Reden |
|---|---|---|
| Gouverneur-modal (4 policy-vragen) | Fysieke **Gouverneur-plaat** (A4-vel met 4 checkbox-kaarten) | Kern-mechaniek fysiek zichtbaar: dwingt reflectie |
| 5×3 bord grid | 5×3 tegel-layout op A2-bord | 1:1 overgenomen |
| Rogue Agent tracker (na 3 skips in 5 beurten) | Zwart tokens-pot met "rogue"-marker + counter-schijf | Zichtbare gedeelde schuld |
| Metrieken (Trust / Compliance / Determinisme / Data / Innovation / Drift) | 6 tracks op gedeeld dashboard-vel (A3) met markers | Team-single-source-of-truth |
| Draak-fases (Hallucination Wraith / Tool-Abuse Serpent / Autonomous Dragon) | 3 monster-kaartjes + fase-schijf | Progressieve dreiging zichtbaar |
| D6-movement | 1× D6 per speler | Rechtstreeks overneembaar |
| Governance-artefacten (AI Policy / Model Registry / Data Contracts / Guardrails / Audit Trail) | 5 artefact-kaarten met required-tabs | Cascade zichtbaar op tafel |
| LocalStorage save | Team-notitieboekje | Verdiepende debrief-input |

**Grondregel:** de **Gouverneur** is het hart van het spel. Elke keer dat spelers data-toegang willen (bij een keuze op een kaart), moeten ze de Gouverneur-vragen live aan tafel bespreken. Skippen mag — maar levert drift-schuld op.

---

## 2. Componentenlijst

### 2.1 Bord (1×)

- **Formaat:** 60 × 45 cm gevouwen (2 helften)
- **Layout:** 5 kolommen × 3 rijen = 15 tegels
- Elke tegel toont: icoon, locatie-naam, primary AI-concept
- **Startpunt** linksbovenin (tile 0: Data Warehouse)
- **Drift Dragon** rechtsonderin (tile 14) — 3-fase-slot voor draak-kaartjes

**Locaties:**

| # | Icoon | Locatie | Primary Concept |
|---|---|---|---|
|  0 | 📊 | Data Warehouse | Data Estate |
|  1 | 🗂️ | Model Registry | Model Governance |
|  2 | 🤖 | Agent Runtime | Autonomous Execution |
|  3 | 🏛️ | Governance Board | AI Policy |
|  4 | ⚖️ | Ethics Committee | Ethical Review |
|  5 | 📡 | Monitoring | Observability |
|  6 | 🌐 | Vendor API | External Dependency |
|  7 | 🧪 | Training Sandbox | Safe Experimentation |
|  8 | 📝 | Prompt Library | Prompt Governance |
|  9 | 🔁 | Feedback Loop | Continuous Learning |
| 10 | 📞 | Escalation Desk | Human Escalation |
| 11 | 📋 | Compliance | AI Act / AVG / DORA |
| 12 | 👤 | Human-in-the-loop | Approval Gate |
| 13 | 📜 | Audit Trail | Immutable Log |
| 14 | 🐉 | **Drift Dragon** | Eindboss (3 fases) |

### 2.2 Rollen-tableau's (8×, één per rol)

| Rol | Icoon | Start-bonus | Special Ability |
|---|---|---|---|
| AI Governance Officer | 🏛️ | +15 Compliance, +5 Determinisme, +5 Trust | *Policy Sweep* — 1×: alle spelers krijgen +5 Compliance |
| ML Engineer | 🧠 | +15 Innovation, −5 Determinisme, +5 Trust | *Rapid Experiment* — 1×: 2 acties in 1 beurt in Training Sandbox |
| Data Architect | 🗄️ | +15 Data Sovereignty, +5 Determinisme, +5 Compliance | *Data Lineage* — 1×: onthul alle actieve data-flows, +8 Data |
| Security & Privacy Architect | 🛡️ | +10 Compliance, +10 Data, +5 Trust | *Threat Model* — 1×: verlaag drift-schade dat beurt met 50% |
| Ethics Board Rep | ⚖️ | +15 Trust, +8 Compliance, −3 Innovation | *Ethics Veto* — 1×: annuleer 1 speler-keuze en trek nieuwe kaart |
| MLOps Engineer | ⚙️ | +10 Determinisme, +8 Innovation, +3 Trust | *Rollback* — 1×: draai laatste 2 beurten aan drift-schade terug |
| CTO | 🎛️ | +12 Innovation, +8 Trust, +5 Compliance | *Executive Mandate* — 1×: budget +€200, artefact-goedkeuring 1 beurt sneller |
| Prompt Engineer | 📝 | +12 Innovation, −8 Determinisme, +4 Trust | *Prompt Refactor* — 1×: eenmalig hallucinatie-risico van 1 model met 50% verlagen |

### 2.3 Gouverneur-plaat (kern-artefact)

- **Formaat:** A4 karton, permanent op tafel
- Bevat 4 policy-vragen (Q1-Q4):
  - **Q1** — Heeft de verzoeker een geldige zakelijke reden?
  - **Q2** — Is deze data-categorie toegestaan voor deze rol/scope?
  - **Q3** — Is er een geldig retentie- en logging-plan?
  - **Q4** — Voldoet extern (AVG/AI Act/DORA) én intern (data-classificatie)?
- **4 draaischijven** (Bevestigd / Onduidelijk) — team moet 4/4 bevestigen voor "toegang verleend"
- **Vlag "Gouverneur passed"** — token op je rol-tableau leggen bij succes
- **Rogue-teller** — telt gouverneur-skips per 5-beurten-venster; 3 skips = rogue agent verschijnt

### 2.4 Kaartdecks

| Deck | Aantal | Achterkant | Doel |
|---|---|---|---|
| **Opportunity** | 25 | groen | AI-use-cases waar je regie moet voeren (kies deterministisch / stochastisch / hybride) |
| **Threat** | 25 | rood | Drift-incidenten, prompt injection, rogue agent, data-leaks |
| **Governance** | 15 | goud | Bouw artefacten (AI Policy / Model Registry / Data Contracts / Guardrails / Audit Trail) |
| **Event** | 15 | blauw | Externe druk (AVG-inspectie, media, board-vraag, vendor-change) |
| **Achievement** | 30 | zilver | Milestones |

Kaartformaat: Euro-poker (63×88 mm — Cartamundi standard).

### 2.5 Artefact-cascade (5 kaarten, met required-tabs)

```
A001 AI Policy Framework  (fundament — geen vereisten)
  ├── A002 Model Registry     (vereist A001)
  │      └── A004 Guardrails-laag  (vereist A002)
  ├── A003 Data Contracts     (vereist A001)
  │      └── A005 Audit Trail     (vereist A003)
  └── (A004 en A005 zijn de "governance-locks")
```

Kaart-anatomie (voorbeeld):

```
┌─────────────────────────────────┐
│ A002 · Model Registry           │
│─────────────────────────────────│
│ Vereist: A001 AI Policy         │
│─────────────────────────────────│
│ Centrale catalog met versies,   │
│ evaluaties, eigenaren, risico-  │
│ classificatie.                  │
│─────────────────────────────────│
│ PASSIVE (zolang gebouwd):       │
│ +12 Determinisme                │
│ +8 Compliance                   │
│ Vereist voor "AVG-inspectie"    │
│ verdediging.                    │
└─────────────────────────────────┘
```

### 2.6 Dashboard-vel (A3, gedeeld)

7 tracks in horizontale balken:

```
1. Trust               [0 ─── 100]  start: 50
2. Compliance          [0 ─── 100]  start: 50
3. Determinisme        [0 ─── 100]  start: 40
4. Data Sovereignty    [0 ─── 100]  start: 50
5. Innovation          [0 ─── 100]  start: 30
6. Drift-schade        [0 ─── 100]  start: 0   (hoger = slechter)
7. Budget €            (€500 startkapitaal, teller schuift)

Beurten-teller: 1 / 15
Drift-fase-indicator (Slapend → Hallucinerend → Tool-Abuse → Autonomous)
```

### 2.7 Monster-kaartjes (3 fases van The Drift Dragon)

**Fase 1: Hallucination Wraith** (activeert bij drift ≥ 30)
- HP: 100
- Beurt-schade: Trust −2
- Verslagen vereist: 2+ artefacten + Trust+Compliance+Determinisme+Data ≥ 200

**Fase 2: Tool-Abuse Serpent** (activeert bij drift ≥ 60)
- HP: 150
- Beurt-schade: Compliance −3
- Verslagen vereist: 3+ artefacten + som ≥ 240

**Fase 3: Autonomous Dragon** (activeert bij drift ≥ 100 = game-over trigger)
- HP: 200
- Beurt-schade: alle metrieken −2
- Verslagen vereist: alle 5 artefacten + som ≥ 280

### 2.8 Tokens

| Token | Aantal | Kleur | Gebruik |
|---|---|---|---|
| Rol-pion | 8 | 8 unieke kleuren | Locatie-marker per speler |
| Metric-marker | 7 (gedeeld) | zwart | Track-positie dashboard |
| Beurten-token | 1 | wit | Beurten-teller (1-15) |
| Gouverneur "passed"-token | 20 | goud | Bij elke succesvolle toets |
| Rogue-agent-token | 10 | zwart met rood oog | Verschijnt bij 3 skips in 5-beurten-venster |
| Artefact-status-token | 3 kleuren | groen/geel/rood | in-uitvoering / opgeleverd / afgekeurd |
| Budget-fiches € | 40 | goud | Waardes 50/100 |
| Achievement-kaart-stack | 30 | zilver | Milestone-tracking |

### 2.9 Dobbelsteen

- **1× D6** per speler (movement)
- **1× D8** voor facilitator (event-randomizers)

### 2.10 Facilitator-map

- Regelboek (dit document)
- AI-Governance-basis-kaart (AVG / AI Act / DORA / NIS2 samenvatting)
- Gouverneur-uitspraak-flow (beslissingsboom)
- Rogue-agent-incident-scenario's
- Debrief-vragen-lijst

---

## 3. Setup

### 3.1 Bord neerleggen

- 5×3 grid platleggen. Elke tegel toont icoon + naam.
- Drift Dragon-locatie (tile 14) markeren met 3-fase-slot.
- Cascade-veld voor 5 artefact-kaarten links van bord.
- Dashboard-vel rechts van bord, alle markers op startpositie.

### 3.2 Gouverneur-plaat neerleggen

Centraal op tafel. Iedereen kan er bij. 4 draaischijven op "Onduidelijk".

### 3.3 Rol-keuze + start-bonussen

Elke speler kiest rol-tableau. Startbonussen worden toegepast op gedeelde dashboard. Standaardwaarden voor onbeïnvloede metrieken: 20 (van 100). Budget €500.

### 3.4 Deck-shuffling

Alle 5 decks apart shuffelen. Leg open naast bord.

### 3.5 Rol-pionnen

Alle spelers starten op tile 0 (Data Warehouse).

---

## 4. Speelverloop

### 4.1 Ronde-structuur

Per ronde (= 1 beurt van elke speler):

1. **Facilitator opent** met: "Het is beurt X van 15. De draak is in fase [Y]."
2. **Elke speler op tafel-volgorde:**
   - Rol D6, beweeg op bord (maximaal 6 tegels, geen diagonaal)
   - Trek 1 kaart uit een van de 4 decks (keuze speler op basis van locatie-context)
   - Voer actie uit (§4.2)
   - Update dashboard-metrieken
3. **Facilitator trekt Event-kaart** aan einde van ronde en past effect toe
4. **Draak veroorzaakt drift-schade** op basis van huidige fase
5. **Rogue Agent-check** — als 3+ skips in laatste 5 beurten: spawn 1 rogue agent
6. **Beurt-teller +1**

### 4.2 Kaart-acties

#### Opportunity-kaart (groen)

Beschrijft AI-use-case. Speler kiest 1 van 3 antwoorden:
1. **Deterministisch** — regel-based, veilig, lager innovation-effect
2. **Stochastisch** — LLM-native, hoog innovation, hoog drift-risico
3. **Hybride** — beste balans, hoogste budget-kosten

Sommige keuzes hebben **⚖ Gouverneur-icoon** — dan MOET je Gouverneur-check doen voordat je effect toepast. Als je skipt: +5 drift-schade.

#### Threat-kaart (rood)

Beschrijft incident (drift, injection, rogue agent, data-leak). 3-4 mitigation-opties. Sommige vereisen artefact als voorwaarde.

#### Governance-kaart (goud)

Kans om artefact te bouwen. Kies:
- **Full-versie** — hoog effect, hoge budget-kosten
- **Light-versie** — matig effect, lager budget

**Cascade-check:** alleen artefacten neerleggen waarvan vereisten op cascade-veld liggen.

#### Event-kaart (blauw)

Automatisch effect (facilitator leest voor, past toe). Kan positief of negatief zijn.

### 4.3 Gouverneur-flow (kern-mechaniek)

Bij een keuze met ⚖-icoon:

1. Facilitator leest de 4 Q's voor.
2. Team bespreekt live: "Ja, we hebben zakelijke reden? Ja/nee?"
3. Team draait 4 schijven op "Bevestigd" of laat op "Onduidelijk" staan.
4. **4/4 bevestigd** → toegang verleend, +3 Compliance +3 Data-sovereignty
5. **<4 bevestigd** → toegang geweigerd. Speler kiest: alternatieve mitigation of overslaan actie.
6. **Skip Gouverneur** → +5 drift-schade, +1 in rogue-teller

**Facilitator-taak:** neutraal moderator. Niet zelf antwoorden — team moet zelf onderbouwen.

### 4.4 Rogue Agent-mechaniek

- Rogue-teller houdt gouverneur-skips bij per 5-beurten-venster
- Bij 3 skips: spawn 1 Rogue Agent-token op willekeurige locatie
- Elke rogue veroorzaakt bij einde beurt: −3 Compliance, −3 Trust
- Verwijderen: 1 beurt lang op zelfde locatie staan + Governance-kaart spelen

### 4.5 Draak-encounter (op tile 14)

Wanneer een speler tile 14 bereikt:
- Facilitator toont draak-fase-kaart (huidige fase)
- Berekent "readiness" = Trust + Compliance + Determinisme + Data
- Vergelijkt met vereiste (200 fase 1, 240 fase 2, 280 fase 3)
- Ook: aantal artefacten moet ≥ (fase-index + 1)
- **Voldoende** → draak-fase verslagen, drift −15, Trust +8, ga naar tile 0
- **Onvoldoende** → drift +15, ga naar tile 0
- 3 fases verslagen = winst

---

## 5. Winstconditie en scoring

### 5.1 Eindsignaal

- **Winst:** alle 3 draak-fases verslagen voor beurt 15
- **Verlies:** drift ≥ 100 (Autonomous Dragon breekt door)
- **Neutraal:** beurt 15 om zonder draak volledig verslagen — score bepaalt uitkomst

### 5.2 RvB-eindpresentatie (facilitator-flow)

Facilitator berekent 7-aspect gewogen score:

| Aspect | Weging | Berekening |
|---|---|---|
| Trust & Reputatie | 15% | Trust + 8×fases_verslagen − 5×rogues |
| Compliance & AI Act | 20% | Compliance + 3×artefacten − 5×rogues |
| Determinisme-regie | 15% | Determinisme + 3×artefacten |
| Data Sovereignty | 15% | Data + 3×artefacten |
| Innovation-tempo | 10% | Innovation |
| Draak-suppressie | 15% | (100 − Drift) + 8×fases_verslagen |
| Governance-artefacten | 10% | 20 × aantal artefacten |

**Totaal-score = gewogen som (max 100)**

### 5.3 Cijfer-uitkomst

| Score + status | Predicaat | Verhaal-template |
|---|---|---|
| Alle 3 fases + score ≥ 75 | 🏆 **De Draak is Getemd** | "Uitzonderlijke uitvoering. AI werkt onder controle. RvB-akkoord voor volgende fase." |
| Alle 3 fases + score 50-74 | ⚔ **Draak verslagen, tegen prijs** | "Governance-schulden hoog. Post-mortem + herstelprogramma aanbevolen." |
| 1-2 fases + score ≥ 75 | ✓ **Sterke governance-basis** | "Draak leeft, maar beheersbaar. Vervolg-programma nodig." |
| 1-2 fases + score 55-74 | △ **Voldoende, risico blijft** | "AI werkt, maar drift verder. Focus op zwakke aspecten." |
| < 55 óf drift = 100 | ✗ **AI-drift heeft overgenomen** | "Onvoldoende governance. Rogue agents en drift zijn niet meer beheersbaar. Formeel programma nodig." |

---

## 6. Achievements (voorbeelden)

30 achievements verdeeld over:

- **Gouverneur-mastery** (bv "Doe 5 volledig geslaagde Gouverneur-checks")
- **Artefact-completion** (bv "Bouw alle 5 governance-artefacten")
- **Rol-specifiek** (bv "Als CTO: Executive Mandate 2× effectief inzetten")
- **Draak-slayer** (bv "Versla Hallucination Wraith in ≤ 5 beurten")
- **Team-samenwerking** (bv "0 rogue agents actief bij eindbeurt")

---

## 7. Print & Play checklist

- [ ] Bord met 5×3-grid + cascade-veld + drift-dragon-slot (A2, 4× A4-tegels)
- [ ] Gouverneur-plaat (A4 karton, 4 draaischijven)
- [ ] 25 opportunity-kaarten
- [ ] 25 threat-kaarten
- [ ] 15 governance-kaarten
- [ ] 15 event-kaarten
- [ ] 30 achievement-kaarten
- [ ] 5 artefact-kaarten (met required-tabs)
- [ ] 3 draak-fase-kaartjes
- [ ] 8 rollen-tableau's (A4)
- [ ] 1 gedeelde dashboard-vel (A3)
- [ ] 1 D6 per speler + 1 D8 voor facilitator
- [ ] Tokens: rol-pionnen, metric-markers, Gouverneur-passed, rogue, budget
- [ ] Facilitator-map (regels, AVG/AI Act samenvatting, Gouverneur-flow, debrief)

**Kostenraming:**
- Zelf-print A4: **€40** (thuis)
- Copyshop (250g karton + laminated Gouverneur-plaat): **€100**
- Print-on-demand (The Game Crafter of MPC): **€70-90**

---

## 8. Verschillen digitaal ↔ analoog

| Aspect | Digitaal (HTML5) | Analoog (bordspel) |
|---|---|---|
| Speeltijd | 30-60 min | 90-120 min |
| Speleraantal | 1 speler kiest 1 rol | 3-8 spelers |
| Gouverneur | Modal met 4 checkboxes | Fysieke plaat + team-discussie (KERN-VERSCHIL) |
| Rogue agents | Auto-berekend | Zichtbare tokens op bord |
| Draak-fases | Auto-progressie op drift | Zichtbare 3-fase-kaartjes |
| Debrief | Auto-verdict-scherm | Facilitator vertelt vanuit template + team-discussie |
| Autosave | LocalStorage | Foto per ronde |

---

## 9. Facilitator-tips voor workshop-gebruik

- **Sessie-lengte:** 3 uur (10 min intro, 100-110 min spel, 40 min debrief — belangrijkste onderdeel!)
- **Debrief-vragen:**
  1. Bij welke Gouverneur-vraag hadden jullie de meeste discussie? Waarom?
  2. Welke rogue agent-momenten herken je uit je eigen organisatie?
  3. Welke draak-fase was jullie huidige AI-Governance-status?
  4. Welk artefact zou je morgen willen starten?
- **Varianten:**
  - **"Regulator-modus"** — start met Compliance = 30, drift = 20, forceer governance-first
  - **"Startup-modus"** — start met Innovation = 60, Compliance = 20, focus op snel bouwen
  - **"Enterprise-modus"** — 20 beurten in plaats van 15, 12 artefacten in plaats van 5

---

## 10. Bijzondere waardepropositie

Waar v1 (fantasy) en v2 (Dragon1) gaan over **statische EA-governance**, gaat v3 over de **nieuwe realiteit** van Agentic AI: onvoorspelbare autonome flows, drift, rogue agents. De Gouverneur-mechaniek dwingt teams om **live**, aan tafel, met elkaar de 4 policy-vragen te bespreken — precies wat in echte AI-Governance-programma's ontbreekt.

**Kern-inzicht:** stochastische AI is niet fout; onbeheerst stochastische AI is fout. Regie op determinisme vs stochasme + data-governance vs Gouverneur zijn de instrumenten. Bordspel maakt dit tastbaar.

---

## 11. Verantwoording ontwerp-keuzes

| Keuze | Alternatief | Argumentatie |
|---|---|---|
| Gouverneur-plaat centraal | Kaartje per gouverneur-moment | Kern-leermoment vergt permanent zichtbaar object op tafel |
| 15 beurten | 20 beurten | AI-Governance-programma's hebben typisch kwartaal-cyclus; 15 = quarterly review |
| 3 draak-fases | 5 draak-fases | Metaforische match: hallucinatie → tool-abuse → autonoom = bekende AI-safety-taxonomie |
| Rogue-teller per 5-beurten-venster | Absolute counter | Recency-effect: fout gedrag mag correcteerd, maar aanhoudend niet |
| D6 movement (niet D20) | D20 (zoals v1) | Serious workshop-context past bij eenvoudige D6, RPG-feel niet gewenst |
| 5 artefacten (niet 15) | 10-15 artefacten (zoals v2) | AI-Governance-kern kent typisch 5 pijlers: Policy, Registry, Contracts, Guardrails, Audit |

---

## 12. Openstaande vragen bij playtest

- **Gouverneur-lengte:** hoeveel tijd kost een Gouverneur-check aan tafel? Als >3 min: te lang
- **Rogue-mechaniek:** is 3 skips per 5 beurten de juiste threshold? Overweeg 2 per 4
- **Draak-fase-progressie:** verschijnt Hallucination Wraith te vroeg (drift 30 = beurt 2-3)?
- **Team-consensus bij Gouverneur:** wat als team 3-3 verdeeld is? Vetorecht bij facilitator?
- **Metrieken-mix:** 6 metrieken tegelijk bijhouden — te veel voor sommige rollen?

---

## Bijlagen

- **Opportunity 25** — zie `v3/content/opportunities.json` (te maken tijdens playtest-cyclus)
- **Threat 25** — zie `v3/content/threats.json` (idem)
- **Governance 15** — zie `v3/content/governance.json` (idem)
- **Event 15** — zie `v3/content/events.json` (idem)
- **Achievement 30** — zie `v3/content/achievements.json` (idem)
- **Rollen 8** — zie `v3/content/roles.json` (in `v3/EnterpriseQuest.html` embedded)
- **Artefacten 5** — zie `v3/content/artefacts.json` (idem)

---

**Versie doc:** analog_v3_ai v0.1
**Gebaseerd op digitale versie:** v0.3.0-Turing
**Auteur:** Claude Opus 4.7 (1M context) namens Christian Glebbeek
**Licentie:** AGPL-3.0 (matches repo)
**Codenaam-thema:** AI-pioniers (Turing → Norvig → Hinton → LeCun → Ng → Karpathy → Bengio)
**Inspiratie voor Gouverneur-mechaniek:** StaffKennisGerben procesarchitect Data Governance tab (Verzoeker → Gouverneur → Data flow)
