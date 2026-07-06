# EnterpriseQuest v3 — Deep Dive Analyse: Train Your Dragon (Agentic AI Governance)

**Auteur:** Christian Glebbeek (iCt Horse)
**Datum:** 2026-07-07
**Scope:** commerciële haalbaarheid van v3 (Train Your Dragon — Agentic AI Governance Edition) als **workshop-tool + serious game + train-de-trainer product**, in zowel digitale als analoge (Print & Play) vorm.
**Positie:** intern beslissingsstuk — vervolg op `analyse_deepdive.md` (v1+v2 digitaal) + `analyse_analoog.md` (v1+v2+v3 analoog). Focus hier: **wat maakt v3 uniek en verkoopbaar in de exploderende AI Governance-markt?**

---

## 1 · Samenvatting (management)

**Uniek?** **Ja, extreem sterk.** In tegenstelling tot v1 (fantasy-RPG in bekende EA-hoek) en v2 (Dragon1-methodiek waar concurrenten indirect bestaan) is v3 in een **latente-nul-concurrentie-markt**: er is voor zover bekend **geen enkel bordspel of interactief serious game specifiek voor Agentic AI Governance**. Bestaande AI-Governance-training bestaat als:

- E-learning modules (Coursera, edX, IAPP, LinkedIn Learning)
- Consultancy-workshops (Deloitte, PwC, EY, Accenture)
- Certificerings-cursussen (ISO/IEC 42001 Lead Auditor, IAPP AIGP)
- Whitepapers en frameworks (NIST AI RMF, EU AI Act text, ISO 42001)

**Geen** van deze biedt een **speelbaar, teamgericht, kwesties-live-uitvechten-format** waar teams Q1-Q4 policy-vragen fysiek (Gouverneur-plaat) of digitaal (modal) moeten uitspreken. Dit is de kern-USP.

**Vermarktbaar?** **Ja, hoger prijspunt dan v1/v2 mogelijk.** AI Governance is boardroom-onderwerp geworden na EU AI Act inwerkingtreding (1 augustus 2024) en verplichte compliance-fases (augustus 2025 general-purpose AI; augustus 2026 high-risk systems). CISO's, DPO's, AI Governance Officers en CTO's hebben concreet **budget** dat begroot is voor "AI-Governance-implementatie". Prijspunt-headroom: €5.000-25.000 per workshop-dag met team, €15.000-45.000 per train-de-trainer-traject, €25.000-75.000 per enterprise-licentie/jaar.

**Positionering:** **niet** als vervanger van certificering — juist als **uitkomstgerichte simulatie** die aanvult op ISO 42001 / IAPP AIGP / NIST AI RMF. "Je hebt de theorie geleerd — nu moet je ermee spelen om te ervaren wat drift, rogue agents en governance-locks in de praktijk doen."

**1 spel of meer?** v3 staat **op zichzelf** — content-domein is fundamenteel anders dan v1/v2. De landingspagina toont ze naast elkaar, maar functioneel zijn het aparte producten. Advies: **v3 als flagship-B2B-product** positioneren; v1 als top-of-funnel (community + studenten); v2 als workshop-tool voor Dragon1-community.

**Nieuwe partner-opties (t.o.v. eerdere analyses):**
- **AI Impact Alliance** — NL AI-ethiek-consortium
- **NL AI Coalitie (NL AIC)** — publiek-privaat netwerk, distributiekanaal via bedrijfsleden
- **TNO AI Governance Lab** — mogelijk academisch/onderzoeksbureau als validator/co-branding
- **Autoriteit Persoonsgegevens (AP)** — educatief kanaal, doelgroep DPO's
- **CISO Platform Nederland** — bereikt >2000 CISO's in NL
- **VNG (Vereniging Nederlandse Gemeenten)** — gemeenten moeten AI-governance opzetten, cursusmateriaal nodig

**Gevaar:** timing. EU AI Act-implementatie is nu (2025-2026) op piek van awareness. Als je in 2026 niet in de markt staat, verlies je een kansvenster van 12-18 maanden waarin adoptie gemakkelijk was. Later wordt de markt bezet door big-4 consultancy die simulatoren of e-learning ontwikkelen.

---

## 2 · Wat is v3

### v3 · Train Your Dragon (v0.3.0-Turing, LIVE)

**Basis-thema:** de architect verslaat de **draak** (AI drift + rogue agents + governance-gaten) door regie op **determinisme vs stochasme** + data-governance via de **Gouverneur**.

**Digitale versie:** `v3/EnterpriseQuest.html`
- 8 rollen: AI Governance Officer / ML Engineer / Data Architect / Security & Privacy Architect / Ethics Board Rep / MLOps Engineer / CTO / Prompt Engineer
- 5×3 bord met 15 AI-landscape locaties (Data Warehouse → Drift Dragon)
- Gouverneur-modal met 4 policy-vragen (Q1-Q4)
- 5 Governance-artefacten met cascade (AI Policy → Model Registry / Data Contracts → Guardrails / Audit Trail)
- Drift Dragon 3-fase eindboss (Hallucination Wraith → Tool-Abuse Serpent → Autonomous Dragon)
- Rogue Agent tracker (3 skips in 5 beurten = rogue spawn)
- 6 metrieken: Trust, Compliance, Determinisme, Data Sovereignty, Innovation, Drift
- LocalStorage autosave, Web Audio, responsive
- LIVE: https://icthorse.nl/EnterpriseQuest/v3/EnterpriseQuest.html

**Analoge versie:** `docs/analog_v3_ai.md` + PDF
- Fysieke Gouverneur-plaat (A4 karton, 4 draaischijven) — team discussieert live
- 5×3 bord (60×45 cm)
- 25 opportunity + 25 threat + 15 governance + 15 event + 30 achievement kaarten
- 3-8 spelers, 90-120 min
- LIVE: https://icthorse.nl/EnterpriseQuest/docs/analog_v3_ai.pdf

**Gouverneur-mechaniek** (kern-innovatie): geïnspireerd door StaffKennisGerben procesarchitect Data Governance tab. **Verzoeker → Gouverneur → Data** flow met 4 policy-vragen:
- Q1: Zakelijke reden?
- Q2: Data-scope juist voor rol?
- Q3: Retentie- en logging-plan?
- Q4: Voldoet AVG/AI Act/DORA + intern beleid?

4/4 bevestigd → toegang. Skippen mag — maar +5 drift-schade + 1 in rogue-teller. 3 skips in 5 beurten = rogue agent spawn.

---

## 3 · Uniekheidsanalyse

### 3.1 · Bestaand landschap AI Governance

| Segment | Voorbeelden | Format | Prijs |
|---|---|---|---|
| **E-learning** | Coursera "AI For Everyone" · edX "AI Governance" · IAPP AIGP self-study · LinkedIn Learning | Video + quiz | €0-€500/gebruiker |
| **Certificering** | ISO/IEC 42001 Lead Auditor · IAPP AIGP · CIPP/E · CIPM · Certified AI Governance Professional | Examen + cursus | €800-€3.500 |
| **Consultancy** | Deloitte AI Impact Analysis · PwC AI Governance · EY AI Trust · Accenture Responsible AI | Advies-traject | €25.000-€250.000 |
| **Frameworks** | NIST AI RMF (Risk Management Framework) · ISO/IEC 42001 · EU AI Act · OECD AI Principles | Document/richtlijn | Gratis |
| **Tools** | IBM watsonx.governance · Credo AI · Fairly AI · Holistic AI · Cranium | SaaS-tool | €500-€5.000/mnd |
| **Workshops (klassikaal)** | AI Impact Alliance · Delve Insights · AI4Belgium · Dutch AI Coalition | Fysieke sessies | €1.500-€5.000/dag |
| **Serious games / bordspel-vorm** | **(vrijwel niets)** — enkele niche startups experimenteren | n/a | n/a |
| **Simulaties / labs** | AI Verify Foundation testing tools · MITRE ATLAS red-team framework | Software + test-cases | Gratis / betaald |

### 3.2 · Uniekheid v3 — kern

Nul directe concurrenten voor gecombineerd **speelbaar + AI-governance + Gouverneur-mechaniek**. Dichtstbijzijnde referentie-punten:

1. **Backdoors & Breaches** (Black Hills, cyber-security kaartspel) — dichtstbij qua vorm, maar security niet AI-governance
2. **NIST Risk Management Framework tabletop-oefeningen** — bestaan als PDF-scenario's, geen game
3. **AI Verify Foundation testing tools** — technische validatie, geen team-game
4. **AI Ethics Card Deck** (Digital Catapult, UK, gratis PnP) — 40 conversatie-kaarten, geen bord/spel-mechaniek
5. **Deloitte "Trustworthy AI" workshop** — advies-traject, geen zelfstandig speelbaar product

**Unique Selling Points v3:**

1. **Enige serious game voor Agentic AI Governance** (voor zover bekend, wereldwijd)
2. **Gouverneur-mechaniek** — live team-uitspraak op 4 policy-vragen — dwingt reflectie en team-consensus (leermoment dat theorie niet levert)
3. **Determinisme/Stochasme keuze per opportunity** — beslissingskader voor elke AI-use-case-vraag ("regel-based of LLM?")
4. **Rogue Agent-mechaniek** — visualiseert cumulatieve governance-schuld (3 skips in 5 beurten = ontsporing)
5. **Drift Dragon 3-fase** — sluit aan bij bekende AI-safety-taxonomie (hallucinatie → tool-abuse → autonoom rogue)
6. **Beide vormen (digital + analog)** — remote-teams via browser; boardroom-workshops via fysiek bord
7. **Direct verhaal-links naar EU AI Act artikel 6/9, AVG, DORA, NIS2** — audit-defensible
8. **Nederlandstalig** — enige NL-Governance-simulatie in productieklare vorm
9. **Open source (AGPL-3.0)** — organisatie kan self-host, forks maken voor branche-specifiek gebruik (banken, zorg, overheid)

### 3.3 · Markttiming — waarom nu

**Regelgevings-druk (EU AI Act timeline, na Digital Omnibus juni 2026):**

- **1 augustus 2024**: EU AI Act inwerking getreden
- **2 februari 2025**: verbod op onaanvaardbare AI (bijv. social scoring, real-time biometrie in publieke ruimte)
- **2 augustus 2025**: general-purpose AI (GPAI) modellen: transparency + code of practice
- **2 december 2027**: **high-risk AI systems Annex III** conformiteitseisen (recruiting, credit-scoring, education, law enforcement etc.) — deadline **uitgesteld van augustus 2026 naar december 2027** door Digital Omnibus (Council 29 juni 2026)
- **2 augustus 2028**: high-risk Annex I (product-geïntegreerd: medical devices, radio equipment, lifts) — uitgesteld van augustus 2027

**Business-implicatie**: NL-organisaties met high-risk AI hebben ongeveer **17-18 maanden** (juli 2026 → december 2027) om compliance-programma's live te hebben. Boetes tot **€35M of 7% wereldwijde omzet** voor overtredingen. Het uitstel kan het gevoel van urgentie tijdelijk verlagen — maar organisaties die serieus zijn, gebruiken de extra tijd om **grondiger** te implementeren, niet om te wachten. Marketing-argument voor v3 wordt hierdoor "gebruik de extra 16 maanden om je governance-programma echt in te trainen".

**Trend-signaal:**
- Gartner's Hype Cycle 2025-2026: "AI TRiSM" (Trust Risk Security Management) is nu op **peak of expectations**
- **AI Governance Officer** is Gartner's snelst groeiende rol-titel (2024→2025 +180% jobposts EU)
- Nederlandse AP legt in 2026 boetes op voor AI-gerelateerde AVG-overtredingen
- Corporate AI-Governance-budgetten zijn geëxplodeerd: gemiddeld **1-3% van IT-budget** in enterprises

**Gevaar zijde:** Big-4 (Deloitte, PwC, EY, Accenture) ontwikkelen simulatoren en labs — met de uitstel-deadline december 2027 hebben zij nu meer tijd voor eigen launches (2027-Q1/Q2 realistischer). Voor iCt Horse betekent dit: **het extra jaar is een kans om marktaandeel op te bouwen voor Big-4-concurrentie serieus wordt**. Kies snel — nu = maximaal voordeel.

### 3.4 · Doelgroep-fit-matrix

| Doelgroep | Fit v3 digitaal | Fit v3 analoog | Waarom |
|---|---|---|---|
| AI Governance Officer | ★★★ | ★★★ | Direct rolgebonden |
| CISO | ★★★ | ★★★ | AI in security-scope |
| DPO / Privacy Officer | ★★★ | ★★★ | AVG + AI Act overlap |
| CTO | ★★ | ★★★ | Strategisch boardroom |
| ML/AI Engineering-teams | ★★★ | ★★ | Praktisch relevant |
| MLOps Engineer | ★★★ | ★★ | Drift/rogue-realiteit |
| Ethics Board / AI Ethics Committee | ★★★ | ★★★ | Rol expliciet aanwezig |
| Legal + Compliance | ★★ | ★★★ | AVG/AI Act/DORA referenties |
| Consultancy trainers (Deloitte, PwC, ...) | ★★★ | ★★★ | Train-de-trainer materiaal |
| Universiteiten (AI-studies, EA-studies) | ★★★ | ★★★ | Curriculum-verrijking |
| HBO/MBO (IT-management) | ★★ | ★★ | Simpelere varianten nodig |
| Publieke sector (VNG, ministeries) | ★★ | ★★★ | AI-strategie training-materiaal |

---

## 4 · Vermarktbaarheid

### 4.1 · Prijspositie (v3 t.o.v. v1/v2)

| Product | Prijs per gebruiker/dag | Prijs per organisatie/jaar | Prijs per workshop-sessie |
|---|---|---|---|
| v1 (fantasy) — funnel/community | €0-25 | €0-500 | €0-500 |
| v2 (Dragon1) — workshop-tool | €50-200 | €2.500-10.000 | €500-2.500 |
| **v3 (AI Governance) — flagship B2B** | **€150-500** | **€10.000-50.000** | **€2.500-10.000** |

**Rationale voor hoger v3-prijspunt:**
- Budget-eigenaar = AI Governance Officer / CISO (koopt in "AI-Governance-programma"-lijnen)
- Compliance-argument = €35M boete-verzekering (kosten-baten sterk)
- Onderscheidend product (nul directe concurrenten)
- Boardroom-legitimiteit (fysieke Gouverneur-plaat als merch-artikel)

### 4.2 · Verdienmodellen

1. **Enterprise SaaS-licentie** — bedrijf koopt jaarlijkse licentie voor eigen team-gebruik → **€10k-50k/jaar**
2. **Workshop-tool per sessie** — externe facilitator gebruikt v3 voor klant-sessie → **€2,5k-10k/sessie**
3. **Train-de-trainer certificering** — trainer krijgt licentie + gids + certificering → **€7,5k-15k eenmalig + €1k/jaar hercertificering**
4. **Consulting cross-sell** — v3 als top-of-funnel voor grotere AI-Governance-advies-opdrachten (€25k-200k+)
5. **Corporate branded editie** — bank/verzekeraar/zorgverlener koopt eigen editie voor teamdagen — 100-500 dozen à **€40-80 bulk**
6. **Universiteits-curriculum-pakket** — €200-500/set inclusief docentenhandleiding
7. **AP/VNG/ministerie-programma** — publieke-sector-editie met verplichte modules — **€25k-100k eenmalig**
8. **Sponsored version voor branche-federatie** — VNO-NCW, NLdigital, Nederland AI — branche financiert, gratis voor leden → **€50k-150k**
9. **PoD-analog voor certificerings-instituten** — IAPP / ISO / Fed-NL branded fysieke set → **eenmalig licentie + royalty per set**

### 4.3 · TAM/SAM/SOM

**TAM (globaal):** AI Governance / trust markt (software + services) — geschat **€25-40 miljard/jaar in 2026** groeiend naar **€100+ miljard in 2030** (bron: Gartner, McKinsey market reports 2025-2026). Serious-game/simulation sub-niche daarvan: **€200-500 miljoen/jaar**.

**TAM Nederland:** NL AI-Governance-training/-tool-markt: **~€150-250 miljoen/jaar** (schatting op basis van enterprise-IT-budgetten × AI-share × Governance-share)

**SAM Nederland:** speelbaar/simulatie-based AI-Governance-training: **~€8-15 miljoen/jaar** — dit is een latente markt zonder concurrentie

**SOM (jaar 1 realistisch):**
- Zelf-launch + PnP: 30-80 licenties/organisatie = €300k-1,2M
- + 1-2 branche-federaties (VNG of NLdigital): +€100k-300k
- + 5-15 workshop-sessies via facilitator-netwerk: +€25k-100k
- **Totaal jaar 1 realistisch: €150k-500k** (afhankelijk van sales-cyclus AI-Governance-Officers)

Als je timing goed pakt (voor augustus 2026 in de markt): **€500k-1,5M jaar 1 goed haalbaar**.

### 4.4 · Kritische succesfactoren

1. **Endorsement door bekende AI-Governance-expert** — bijv. via [SIG AI](https://www.nldigital.nl/sig-ai/) of AI Impact Alliance. Zonder credibility van iemand met NL-naam blijft product marketing-orphan
2. **Pilot bij 1 bekende NL-organisatie** — bank, verzekeraar of gemeente met AI-Governance-programma → **case study** cruciaal voor sales
3. **Facilitator-gids** — voor v3 werkelijk noodzakelijk (Gouverneur-flow, debrief, rogue-scenario's) — nog te schrijven — **€8-15k budget**
4. **EU AI Act-annotaties** — elke opportunity/threat-kaart met concrete artikel-verwijzing (bijv. "AI Act art. 9 vereist risk management system") → verhoogt audit-defensibiliteit
5. **Multi-language** — voor internationale schaal EN-editie (€8-15k vertaling + review + juridische check)
6. **Publieke-sector-modus** — VNG-editie met gemeenten-specifieke cases (BSN-data, WMO/WLZ AI, gemeente-diensten-AI) → grootste single-segment-omzet
7. **Server-side scoreboards + trainer-analytics** — voor enterprise-adoptie noodzakelijk (nu single-player LocalStorage) → **€20-40k dev**
8. **Integratie met bestaande GRC-tools** — RSA Archer, ServiceNow GRC, MetricStream — via SSO of API — voor enterprise-inbedding

### 4.5 · Vergelijking met aangrenzende serious-game-successen

| Titel | Doelgroep | Model | Waarom werkte het? | v3-les |
|---|---|---|---|---|
| **Backdoors & Breaches** (Black Hills) | Cyber-security teams | Gratis PnP + retail | Community-driven, small & mighty | v3 kan zelfde model: gratis PnP + retail |
| **AI Ethics Card Deck** (Digital Catapult, UK) | AI-teams (gratis) | Gratis PnP | 40 conversatie-kaarten, geen game — beperkt gebruik | v3 kan beter: échte game, niet alleen kaartenset |
| **Beer Distribution Game** (MIT 1960) | Supply chain training | Classroom + online | Klassieker, 60+ jaar in gebruik | v3 kan analoog vast in curriculum landen |
| **Kanban Pizza Game** (agile42) | Agile teams | Gratis PnP + Creative Commons | Trainer-tool, snel te leren | v3 kan zelfde: facilitator-tool + community-uitbreiding |
| **Backdoors & Breaches** cyber-tabletop | CIS + security | Card game + free PnP | Doelgroep-fit + community-multiplier | v3-fit voor CISO's + AI Governance Officers |

**Lessen:**
- Gratis PnP als voorportaal genereert bewustzijn en early-adoption
- Community-content-support vroeg openzetten (custom scenario's via GitHub)
- Trainer-focus (facilitator-materiaal) is hogere-marge dan retail
- Wachten tot regelgeving-implementatie-deadline (nu tot augustus 2026) genereert verkoop-druk

---

## 5 · Advies: hoe vermarkten?

### Optie A · Alleen digitaal (huidige situatie: LIVE)
- **Voor:** nul-marketing-cost, kan gratis online staan
- **Tegen:** geen directe omzet zonder pay-wall
- **Rol:** funnel / awareness

### Optie B · Digitaal + analoog PnP-download (huidige situatie: LIVE)
- **Voor:** twee vormen voor twee doelgroepen (remote + fysiek)
- **Tegen:** nog geen betaald element
- **Rol:** community-uitrol, awareness-fase

### Optie C · SaaS-licentie enterprise
- **Voor:** voorspelbare omzet, hoog marge (~95%), schaalbaar
- **Tegen:** vergt server-side scoreboards + SSO + analytics (€20-40k dev)
- **Rol:** hoofd-verdienmodel voor enterprises

### Optie D · Workshop-tool licensing
- **Voor:** hoog prijspunt (€2,5-10k/sessie), passief inkomen via facilitator-partners
- **Tegen:** vereist facilitator-gids + eerste-klant-case
- **Rol:** mid-market-verdienmodel

### Optie E · Train-de-trainer certificering
- **Voor:** €7,5-15k per trainer, netwerk-effect
- **Tegen:** logistiek + tijdsintensief
- **Rol:** exclusiviteit + prijs-premium

### Optie F · Branche-federatie sponsoring
- **Voor:** bulk-adoptie via netwerk (VNG, NLdigital, Fed-NL, NL AIC), publieke funding mogelijk
- **Tegen:** lange sales-cyclus (6-12 maanden)
- **Rol:** stabiele bulk-omzet

### Optie G · Publiek-sector-editie (VNG-Gemeenten)
- **Voor:** gemeenten hebben verplicht AI-strategie, budget aanwezig, minimale competitie
- **Tegen:** aanbesteding-formaliteit, langdurige inkoop
- **Rol:** stabiel volumelijk, jaarlijkse licenties

### Optie H · Partner met NL AI-consultancy (AI Impact Alliance / Delve Insights)
- **Voor:** validatie door NL-experts, distributie via bestaande klant-portefeuille
- **Tegen:** revenue-share (60/40 or 50/50)
- **Rol:** boost-adoptie fase 1-2

**→ Aanbevolen combinatie:**

1. **Fase 0 (nu, LIVE):** Optie A + B — digitale + analoge PnP-download live op icthorse.nl. **Awareness fase**.
2. **Fase 1 (maanden 1-3):** Optie H — 1 partner-gesprek met AI Impact Alliance of Delve Insights voor validatie + eerste pilot-klant. **Endorsement fase**.
3. **Fase 2 (maanden 3-6):** Optie D — eerste 3-5 betaalde workshops als facilitator. **Cash-flow start**.
4. **Fase 3 (maanden 6-9):** Optie E — train-de-trainer certificering openzetten voor 2-3 externe trainers. **Multiplicator**.
5. **Fase 4 (maanden 9-12):** Optie C — SaaS-licentie enterprise als server-side backend af is. **Schaal**.
6. **Fase 5 (jaar 2):** Optie F + G — VNG + NLdigital + branche-federaties. **Volume**.

---

## 6 · Twee sporen — go-to-market

### Spoor A: Partner-driven (via NL AI Consultancy)

**Partner-opties:**
- **AI Impact Alliance** — NL AI-ethiek-consortium, klant-portefeuille tech + publieke sector
- **Delve Insights** — NL AI-consultancy, focus op AI-strategie
- **Nederlandse AI Coalitie (NL AIC)** — publiek-privaat netwerk, distributie via 400+ bedrijfsleden
- **TNO AI Governance Lab** — mogelijk academisch/onderzoek co-branding
- **Erasmus Center for AI Governance** — academische validering

**Waarde-uitwisseling:**
- Wat partner biedt: klant-toegang, NL-naam, sales-team
- Wat wij bieden: kant-en-klaar product, snelle time-to-market

**Model:**
- Revenue-share 40/60 (partner/iCt) op licenties via partner-kanaal
- Co-branding als "Powered by iCt Horse" of eigen brand met licentie

### Spoor B: Publieke-sector-track (VNG / ministeries / AP)

**Doelgroep:**
- **VNG** — Vereniging Nederlandse Gemeenten (352 gemeenten)
- **Rijksdienst voor de Digitale Overheid** (VNG + Rijk)
- **Autoriteit Persoonsgegevens (AP)** — educatief kanaal, doelgroep DPO's en organisaties
- **Ministerie van Binnenlandse Zaken** — AI-in-de-publieke-sector-programma

**Waarde:** gemeenten hebben verplichte AI-strategie én AI-Governance-training-behoefte. VNG-editie kan door VNG worden gefinancierd als publiek-goed.

**Model:**
- Custom-editie voor VNG (aangepaste cases voor gemeente-context) — eenmalig €50-100k development + jaarlijkse content-updates
- Licentie per gemeente (bijv. €500-2.500/jaar voor gemeente-brede toegang)
- Facilitator-training via VNG-netwerk

### Spoor C: Direct enterprise sales (CISO / AI Governance Officer)

**Doelgroep:** grote NL-organisaties met AI-programma's — banken (ING, Rabobank, ABN AMRO), verzekeraars (NN, Achmea, Aegon), zorgverleners (grote ziekenhuizen), retail (Bol, Ahold, Coolblue), telecom (KPN, VodafoneZiggo)

**Sales-tactiek:**
- Direct outreach via LinkedIn naar AI Governance Officer / CISO / DPO
- Referral-programma via CISO Platform Nederland
- Content-marketing (whitepapers, webinars) op eigen kanaal

**Prijspunt:** €10-50k/organisatie/jaar SaaS-licentie, €25-75k enterprise-workshop-inzet

### Spoor D: Internationale positioning

**Doelgroep:** internationale AI-Governance-community
- **Europees** — via EU AI Office (Brussel) contact leggen voor educatief materiaal
- **Wereldwijd** — via ISO/IEC 42001 Lead Auditor certificerings-instanties en IAPP-community

**Voorwaarden:** EN-editie klaar (€8-15k vertaling + review + juridische check op AI Act EN-terminologie)

---

## 7 · Advies executie

1. **Deze week:** endorsement-gesprek plannen — 2-3 contact-opnamen (LinkedIn + mail) met bekende NL AI-Governance-namen (bijv. Sennay Ghebreab, Coen Van Gulijk, Marieke Van Erp, ...). Vraag: "Wil je vroege access + feedback?"
2. **Week +2-3:** eerste pilot-organisatie vinden voor 1 workshop-sessie (kan iCt Horse-relatie zijn, of via netwerk Peter/Mark). Doel: 1 gestest case-study
3. **Maand 1-2:** facilitator-gids schrijven (Gouverneur-flow, EU AI Act-annotaties per kaart, debrief-vragen). **€8-15k budget**
4. **Maand 2-3:** eerste 3-5 workshops als betaalde facilitator. Prijs: €2,5-5k/sessie. Verzamelen: case-materiaal + testimonials
5. **Maand 3-4:** VNG-pilot voorstellen (via netwerk of directe outreach). 1 gemeente als lighthouse-klant
6. **Maand 4-6:** server-side backend uitbouwen (multi-user scoreboards, SSO, analytics). Enterprise-SaaS-launch voorbereiden
7. **Maand 6-9:** partner-deal met AI Impact Alliance of NL AIC. Officiële launch
8. **Maand 9-12:** internationale variant (EN-editie), aanwezigheid op AI-Governance-conferenties (IAPP Global Privacy Summit, ISO 42001-events)

**Onmisbaar voor go-live:**
- Facilitator-gids (5-10 pagina's) — **€8-15k**
- 1 case-study met bekend NL-bedrijf — **€2-5k** (of gratis via netwerk)
- EU AI Act-annotaties per kaart — **€3-5k juridische review**
- Landingspagina met sales-content — **€2-3k**
- Aftermovie / demo-video (2-3 min) — **€2-4k**
- Multi-user backend (voor SaaS) — **€20-40k**

**Totaal go-live budget (voor SaaS-launch):** **€40-75k**
**Time-to-first-euro:** ~2-3 maanden (workshop-verkoop)
**Time-to-materiële-omzet:** ~6-9 maanden (SaaS + eerste partners)

---

## 8 · Financiële projectie (jaar 1, indicatief)

| Scenario | Volume | Omzet | Marge |
|---|---|---|---|
| **Alleen huidige LIVE-versie** — organische adoptie | 0-500 downloads | €0 | n/a |
| **+ 5-10 workshops** (facilitator = ik) | 5-10 workshops à €3k | €15k-30k | 70% |
| **+ 1 pilot enterprise-licentie** (bank/verzekeraar) | 1 klant | €15k-30k | 85% |
| **+ NL AIC / AI Impact-partnerschap** | 5-10 klanten via partner | +€30-100k | 45% (na share) |
| **+ VNG-pilot** (1 gemeente + regio-uitrol) | 5-10 gemeenten | +€25-100k | 60% |
| **+ Train-de-trainer voor 2-3 externe trainers** | 2-3 trainers | +€15-45k | 90% |
| **Realistisch totaal jaar 1** | | **€100k-300k** | **~60-70%** |
| **Optimistisch (voor augustus 2026-deadline in markt)** | | **€300k-800k** | **~55-65%** |

**Sensitiviteits-scenario's:**
- **Ondergrens** (alleen huidig LIVE + 3-5 workshops): **€10-20k jaar 1**
- **Basis** (workshops + 1 partner + VNG-pilot): **€100-200k jaar 1**
- **Bovengrens** (alles + case-study bij grote bank): **€400-800k jaar 1**

**Key driver:** eerste 3 betaalde klanten voor case-material. Zonder testimonials blijft SaaS-verkoop moeizaam. Met 2-3 testimonials versnelt sales-cyclus fors.

---

## 9 · Vergelijking v3 versus v1/v2 als vermarktbaar product

| Aspect | v1 (Fantasy) | v2 (Dragon1) | **v3 (AI Governance)** |
|---|---|---|---|
| **Doelgroep-scope** | Klein (EA-nerds + studenten) | Middel (Dragon1-community) | **Groot (elke org met AI)** |
| **Marktvolwassenheid** | Latent (small niche) | Latent (Dragon1-community) | **Actief (regelgeving-druk)** |
| **Prijspunt-headroom** | Klein (€0-500) | Middel (€500-5k) | **Groot (€2,5k-50k)** |
| **Concurrentie** | Beperkt | Beperkt | **Vrijwel nihil** |
| **Boardroom-legitimiteit** | Laag | Middel | **Hoog** |
| **Regelgeving-hefboom** | Geen | Geen | **EU AI Act, AVG, DORA, NIS2** |
| **Partner-opties** | Weinig | Dragon1 (via Mark Paauwe) | **Meerdere (AI Impact, NL AIC, VNG, ...)** |
| **Timing-druk** | Neutraal | Neutraal | **Hoog (aug 2026 EU AI Act deadline)** |
| **Content-diepte-vereiste** | Laag (fantasy vrijheid) | Middel (Dragon1-getrouw) | **Hoog (juridische correctheid)** |
| **Marge-potentieel** | Laag-middel | Middel | **Hoog** |

**Conclusie:** v3 is **verreweg** het meest vermarktbare product van de drie. v1 blijft top-of-funnel/community-tool. v2 blijft Dragon1-community-tool. **v3 is flagship B2B**.

---

## 10 · Openstaande vragen

1. Wie is de bekende NL-AI-Governance-naam die endorsement wil geven? Netwerk-verkenning nodig.
2. Welke NL-organisatie is bereid tot pilot-workshop (gratis of tegen kostprijs) voor case-material?
3. Kan AI Impact Alliance of NL AIC als eerste partner-gesprek worden ingericht?
4. Is er contact-mogelijkheid met VNG rond AI-strategie voor gemeenten?
5. Wat is de exacte EU AI Act artikel-mapping voor elke kaart? Juridische review nodig (€3-5k budget)
6. Hoe positioneren t.o.v. ISO/IEC 42001 en IAPP AIGP? Aanvullend, niet-vervangend — hoe expliciet in marketing?
7. Timing van EN-editie: nu al vertalen of eerst NL-market bewijzen (Q4 2026)?
8. Kan Autoriteit Persoonsgegevens als educatief kanaal fungeren voor DPO's? Of zien zij ons als concurrent?
9. Multi-user server-side backend: build zelf of open-source samenwerking (bijv. via NL AI Coalitie tech-werkgroep)?
10. Corporate branded editie: wie is eerste ambassadeur-organisatie (financieel of niet-financieel gemotiveerd)?

---

## Bijlagen

- `docs/analog_v3_ai.md` + `.pdf` — Print & Play design v3
- `v3/EnterpriseQuest.html` — digitale versie v3 LIVE
- `docs/analyse_deepdive.md` — deep-dive digitale v1+v2 (context)
- `docs/analyse_analoog.md` — deep-dive analoge versies (context)

*Intern beslissingsstuk — niet doorsturen naar Mark, Peter, of externe partners zonder aanpassing per partner-doelgroep.*

**Datum eerste versie:** 2026-07-07
**Auteur:** Claude Opus 4.7 (1M context) namens Christian Glebbeek
