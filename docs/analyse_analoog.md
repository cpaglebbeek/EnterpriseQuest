# Enterprise Quest — Deep Dive Analyse: Analoge Versies (intern)

**Auteur:** Christian Glebbeek (iCt Horse)
**Datum:** 2026-07-07
**Scope:** commerciële haalbaarheid van **analoge Print & Play bordspel-uitwerkingen** van EnterpriseQuest v1 (fantasy-RPG) + v2 (Dragon1) als **fysiek serious game + workshop-product**, apart van (én in combinatie met) de digitale versies.
**Position:** intern beslissingsstuk — vervolg op `analyse_deepdive.md` (dat de digitale versies analyseerde). Focus hier: **wat verandert er als je het spel op tafel legt in plaats van in de browser?**

---

## 1 · Samenvatting (management)

**Uniek?** Ja, sterker dan bij de digitale versies. In de wereld van serious-game-bordspellen bestaan er varianten voor **agile/scrum, kanban, procesarchitectuur, cyber-security, projectmanagement** — maar **niet voor Enterprise Architecture volgens een specifieke methode (Dragon1)**. De analoge EQ v2 is daarmee — voor zover bekend — de eerste fysieke Dragon1-workshop-tool ter wereld. EQ v1 (fantasy-RPG) heeft méér concurrenten in de "tech-humor board game"-hoek (bv. *The Manager*, *Kanban Pizza Game*, *Scrumble*) maar geen enkele daarvan combineert **RPG-mechanica + volledige EA-content-set**.

**Vermarktbaar?** Ja, maar via een fundamenteel ander verdienmodel dan de digitale versies. Fysieke bordspellen worden **niet per gebruiker-licentie** verkocht; ze worden verkocht als:
1. **Fysiek eindproduct** — €40-120 per doos (via Bol.com, boardgamestore.nl, Kickstarter/Gamefound)
2. **Facilitator-tool** — €500-2.500 per sessie (inhouse workshop, incl. facilitator)
3. **Train-de-trainer certificering** met de fysieke set als bijgevoegd materiaal — €5.000-15.000 per instructeur
4. **Corporate gift / conferentie-uitgifte** — 50-500 dozen voor branded events — €30-80 per doos in bulk

**Belangrijk verschil t.o.v. digitaal:** een fysiek spel wordt **onthouden** (op de plank in de werkkamer, jaarlijkse team-day, herhaald gebruik). Digitale versies hebben veel hogere adoptie-friction. Fysiek is duurder om te distribueren, maar levert een hogere gepercipieerde waarde-per-verkoop op.

**1 spel of meerdere in de analoge lijn?** Antwoord: **beide fysieke edities uitbrengen (v1 én v2)**, met dezelfde funnel-logica als bij digitaal — maar met **omgekeerde prijsposities**:
- **v1 fysiek** — €50-70 retail, mainstream tech-enthousiast, mogelijk retail
- **v2 fysiek** — €90-150 workshop-edition, alleen via iCt Horse of Dragon1-kanaal, gebundeld met facilitator-gids

**Advies partners:**
- **Mark Paauwe (Dragon1)** — fysieke EQ v2 is een véél sterker gesprek dan de digitale versie. Bordspel = tastbaar, boardroom-legitimiteit, tijdens Dragon1-events uit te delen. Voorstel: co-productie fysieke Dragon1-editie.
- **Peter v/d Hulst (Staff)** — fysieke workshop-tool past bij Staff's traditie van klassikale-training-materiaal. Overweging: white-label procesarchitectuur-editie (v3-analoog).
- **Nieuwe optie:** **Kickstarter/Gamefound crowdfunding** voor v1 (fantasy-RPG-editie) — bereikt board-gamer-community rechtstreeks, valideert markt zonder partner nodig.

**Gevaar:** productie- en logistiek-risico. Fysieke productie = MOQ's (minimum order quantities), voorraadrisico, retourbeleid, verzendkosten. Anders dan digitaal, dat marginaal-nul-kosten is.

---

## 2 · Wat hebben we in de analoge lijn

### 2.1 · Analog v1 · Architect's Dungeon PnP-editie

Gebaseerd op `docs/analog_v1_rpg.md`:

- **Vorm:** bord (40 tiles, 12 regio's) + 250 kaarten (100 Quest / 50 Chaos / 50 Artifact / 50 Event) + 22 monster-kaarten + 6 klassen-tableau's + tokens + D20's
- **Speelbaarheid:** 1-6 spelers, 90-150 min
- **Doelgroep:** tech-enthousiast, junior architecten, EA-studenten, workshop-facilitators
- **Print-on-demand kostenraming:** €45-90 per doos (via The Game Crafter of MakePlayingCards)
- **Zelf-print kosten (PnP):** €25-30 thuis, €80 copyshop
- **Kleinschalige oplage (100 stuks):** €25-32 per doos via BoardGameLab/MPC
- **Status:** design-document compleet, playtest nog niet uitgevoerd

### 2.2 · Analog v2 · Dragon1 Architect's Journey PnP-editie

Gebaseerd op `docs/analog_v2_dragon1.md`:

- **Vorm:** 4×4 bord (16 organisatie-locaties) + 15 artefact-kaarten (met cascade-tabs) + 40 missions + 40 challenges + 30 events + 47 achievements + 8 rollen-tableau's + gedeeld dashboard (A3) + tokens + 1 D6
- **Speelbaarheid:** 2-8 spelers, 90-120 min, workshop-context
- **Doelgroep:** senior EA's, CIO's, consultancy-firma's, Dragon1-community, EA-cursussen (HAN, Nyenrode, Open Universiteit)
- **Print-on-demand kostenraming:** €65-80 per doos
- **Zelf-print kosten (PnP):** €35 thuis, €90 copyshop
- **Kern-innovatie:** fysieke Dragon1-cascade zichtbaar op tafel (leermoment ipv abstracte software-check)
- **Status:** design-document compleet, playtest nog niet uitgevoerd

### 2.3 · Gedeelde productie-kenmerken

- **Formaat:** Euro-poker kaarten (63×88 mm — Cartamundi/industry standard)
- **Bord:** 60×60 cm gevouwen (2 helften)
- **Doos:** standaard board-game-doos (30×30×7 cm, past in retail-schappen)
- **Componenten:** kaarten laminated of in Ultra Pro sleeves; kartonnen tableau's + tokens (kunststof of hout)
- **PnP-versie:** direct downloadbaar als PDF (met snijlijnen)
- **Print-on-demand:** via The Game Crafter (bestaande wereldleider PoD board games sinds 2009 met >380.000 gebruikers en >300.000 titels; bron: thegamecrafter.com/BoardGameGeek), MakePlayingCards, BoardGameLab

---

## 3 · Uniekheidsanalyse — analoge markt

### 3.1 · Bestaand landschap fysieke serious games (tech/EA/BPM)

| Segment | Bekende titels | Prijs | Format |
|---|---|---|---|
| **Agile/Scrum** | *Kanban Pizza Game*, *Ball Point Game*, *Scrumble* | €30-60 (of gratis PnP) | Kartonnen bord + kaartjes |
| **Procesarchitectuur / BPM** | Passionned BPM-simulaties, De Processpecialisten' proces-game | €500-1.500 per set (facilitator-inclusief) | Fysiek bordspel + workshop |
| **Cyber-security** | *Backdoors & Breaches* (Black Hills), *Riskio*, *[d0x3d!]* | €25-100 | Kaartspel + soms bord |
| **Projectmanagement** | *The Manager*, *Project Manager Simulation*, PMBOK-simulaties | €40-200 | Kaartspel + scenario-boek |
| **Enterprise Architecture** | **(vrijwel niets bekends)** — TOGAF/ArchiMate zijn certificerings-cursussen, geen games | n/a | n/a |
| **Business-strategie klassiek** | *Beer Distribution Game* (MIT Sloan, Jay W. Forrester, 1960), *The Fresh Connection* (Inchainge/Involvation), *Buckminster Fuller World Game* | €50-500+ | Fysiek bord + facilitator |
| **RPG-tech-crossover** | *Bureaucracy* (Avalon Hill, 1981, satire), *Red Tape Game*, diverse office-humor kaartspellen | €30-80 | Kaartspel/hybride |

### 3.2 · Uniekheid analog EQ v1

**Wat maakt het anders dan concurrenten in het fantasy/tech-humor segment:**

1. **RPG-mechanica (D20, klassen, XP-progressie) + volledige EA-content-set** — nergens anders gezien. RPG-spellen met tech-humor bestaan (Bureaucracy: The Board Game), maar behandelen EA niet inhoudelijk
2. **250 kaarten met echte EA-terminologie** — TOGAF ADM, ArchiMate, Zero Trust, GDPR, NIS2, MLOps, Kubernetes — direct herkenbaar voor doelgroep
3. **Chaos Architect als 3-fase eindboss** — creatief metaforisch: de "witte-bord-fase" → "implementatie-chaos" → "chaos-ascendant" — herkenbaar EA-verhaal
4. **Nederlandstalig** — enige Nederlandse RPG-bordspel over enterprise IT

**Unique Selling Points (analog v1):**
- Enige Nederlandse EA-gamification-bordspel op RPG-basis
- Directe fysieke overname van bekende D&D-conventies (D20, klassen, kaarten) → lage leerdrempel voor RPG-geïnteresseerde tech-community
- Print & Play beschikbaar → geen productierisico voor early-adopters
- Open-source content (AGPL-3.0) → community-uitbreiding mogelijk (nieuwe klassen, monsters, artifacten)

**Risico's:**
- RPG-verpakking kan door senior EA's als "onprofessioneel" gezien worden — beperkte inzet in enterprise-workshops
- Fysieke productie MOQ's onbekend, valideren nodig
- Concurrentie *Backdoors & Breaches* (cyber-security kaartspel) heeft al €25-50 prijspunt bezet in aangrenzende markt

### 3.3 · Uniekheid analog EQ v2

**Wat maakt het onvergelijkelijk:**

1. **Enige fysieke bordspel-implementatie van de Dragon1-methodiek** (voor zover bekend — check bij Mark Paauwe)
2. **Fysieke artefact-cascade** — kaarten met required-tabs die op tafel worden gestapeld → **zichtbaar leermoment** dat je in software niet even sterk krijgt
3. **8 rollen simultaan spelen** — bevordert cross-perspectief-inzicht (BA vs SecA vs CIO vs Student EA) op dezelfde case, iets wat digitale single-player nooit oplevert
4. **Facilitator-geleide RvB-eindpresentatie** — professioneel workshop-format, vertaalbaar naar boardroom-oefening
5. **Gedeeld A3-dashboard** — team op één single-source-of-truth → sluit aan bij hedendaagse teamwork-trends (Miro/Mural analogieën in fysiek)

**Unique Selling Points (analog v2):**
- Enige Dragon1-workshop-tool die je op tafel kunt leggen (analog + tastbaar)
- Direct bruikbaar in EA-cursussen op universitaire/HBO-niveau (HAN, Nyenrode, Open Universiteit, Universiteit van Amsterdam)
- Sluit aan bij Dragon1-doctrine (Mark Paauwe erkent 4 'ways': way of thinking / working / representing / supporting — bordspel = alle 4 tegelijk)
- Herbruikbaar in klaslokaal én bij inhouse workshops → hoge herbruikbaarheids-waarde

**Risico's:**
- Zonder Paauwe's blessing kan v2 niet als "officieel Dragon1" verkocht worden
- Complexer dan v1 → langere onboarding-tijd voor facilitator
- Prijspunt hoger (€90-150) → smallere markt

### 3.4 · Bijzondere waardepropositie: fysiek versus digitaal

Kern-inzicht: fysieke bordspellen worden waardevoller in de post-2023-context (Zoom-moeheid, hybride werk, offline-focus, digital-detox trend). CIO's/EA's zoeken workshop-formats die **teams tastbaar samen doen** — niet nog een Miro-board of nog een Zoom-call.

**Waarom fysiek EQ v2 in 2026 kan werken:**

| Trend | Fysiek voordeel |
|---|---|
| **Zoom-moeheid** | Fysieke bordspel-sessie = mensen weg van scherm |
| **Team-building post-COVID** | Boardroom-oefening + spel = herstellend voor cultuur |
| **Digital-detox** | Kaarten shuffelen, dobbelen, tokens verschuiven = zintuiglijk |
| **In-person meetings terug** | Board-room-tafel = eenvoudige set-up (bord + kaarten) |
| **AI-vermoeidheid** | Fysiek = geen chatbot, wel echte deliberatie |
| **Boardroom-legitimiteit** | Card-game op tafel = professioneler dan iPad-app |

Bordspel-sector groeit gestaag (BoardGameGeek Kickstarter-cijfers, Gamefound-launches, Essen Spiel bezoekersgroei) — serious games sub-niche groeit sneller dan mainstream board games (bron: SeriousGames Interactive market reports).

---

## 4 · Vermarktbaarheid — analoge productlijnen

### 4.1 · Doelgroepen (analog)

| Doelgroep | v1 fysiek | v2 fysiek | Prijsbereidheid per doos |
|---|---|---|---|
| Tech-enthousiast / boardgamer-community | ★★★ | ★ | €40-70 |
| Studenten EA (HAN, Nyenrode, Open Universiteit, UvA) | ★★★ | ★★ | €30-50 (bulk-korting via cursus) |
| Junior architecten (persoonlijke aankoop) | ★★ | ★★ | €50-80 |
| Senior architecten / CIO's | ★ | ★★★ | €90-150 |
| Consultancy-firma's (interne trainingsmiddel) | ★★ | ★★★ | €150-300 per set, 5-10 sets per firma |
| Universiteiten / HBO-cursusleiders | ★ | ★★★ | €200-400 per set (curriculum-inclusief) |
| Dragon1-community-events | — | ★★★ | Kadobox (gratis/subsidie) |
| Retail (Bol, boardgamestore.nl) | ★★ | ★ | €40-70 retail-consumer |
| Kickstarter/Gamefound-backers | ★★★ | ★★ | €50-100 (early-bird) |
| Corporate-gift (bank/verzekeraar/consulting) | ★ | ★★★ | €50-80 per doos bulk |

### 4.2 · Verdienmodellen (analog)

1. **Print & Play PDF-verkoop** — €5-15 per download (via itch.io, gumroad, iCt Horse-shop). Marginaal nul-kosten. Voor **early revenue en validatie**
2. **Print-on-demand fysiek** — via The Game Crafter (auteur zet €0-15 marge op basis-productiekosten). Geen eigen voorraad. Marge lager, drempel voor koper hoger (verzending +25%)
3. **Kleinschalige eigen productie** (100-500 stuks) — MOQ €2.500-15.000, marge 60-70% op retail-prijs. Vergt voor-financiering
4. **Kickstarter/Gamefound crowdfunding** — validatie + voor-financiering in één. Fantasy-editie geschikter dan Dragon1-editie voor deze route
5. **Retail-distributie** — via boardgamestore.nl, Bol.com, 999 Games. Marges 30-45% (retail neemt 40-55%)
6. **Workshop-tool licensing (fysiek incl.)** — facilitator koopt licentie (€500-1.500 per sessie) inclusief spel + gids
7. **Train-de-trainer** — trainer krijgt spel + gids + certificering — €7.500-15.000 per instructeur
8. **Corporate gift / branded editie** — banks/consultancy/verzekeraars kopen 50-500 dozen met eigen logo — €30-80 per doos bulk
9. **Universitair curriculum-pakket** — €200-400 per set inclusief docentenhandleiding, jaarlijkse update

### 4.3 · TAM/SAM/SOM Nederland (analog)

- **TAM** — Nederlandse markt fysieke serious-game/workshop-materialen (EA/BPM/PM samen): ~€8-15M/jaar (geschat op basis van bekende BPM-simulatie-tarieven × sessie-volumes + universitair curriculum-materiaal)
- **SAM** — fysieke EA-simulaties (specifiek Dragon1/TOGAF/ArchiMate): **niet-bestaande markt vandaag** — geschatte latent SAM: €500k-2M/jaar
- **SOM** (jaar 1) — realistisch met 1 launch + PnP + 1 partner:
  - Zelf-launch v1 fysiek: 100-300 stuks × €60 = €6k-18k
  - Kickstarter v1 (met €10k crowdfunding-goal): 200-600 backers = €10k-40k
  - Workshops v2 (5-15 sessies à €1.500): €7,5k-22,5k
  - **Totaal jaar 1 zonder partner: €20k-80k**
  - **Met Dragon1-partner en curriculum-deals: €50k-180k**

### 4.4 · Kritische succesfactoren (analog)

1. **Playtest** — je hebt minimaal 5-8 playtest-sessies nodig met echte EA/CIO's. Zonder valideren is retail-launch riskant. **Kosten: €0 (eigen tijd) tot €5k (facilitator-huur)**
2. **Facilitator-gids** — voor v2 vitaal (workshop-context); voor v1 optioneel (self-service). **Kosten: €5-10k voor 2 gidsen**
3. **Doos + productie-artwork** — professioneel design nodig voor retail/Kickstarter. **Kosten: €2k-5k grafisch design + fotografie**
4. **Distributie-kanaal** — Kickstarter (self-service), retail (via 999 Games of import), of directe verkoop (icthorse.nl/shop bouwen). **Kosten: €3k-8k voor shop + payments-integratie**
5. **Voorraad-financiering** — bij eigen productie €5k-15k initieel; met Kickstarter voorgefinancierd
6. **Retail-relatie** — 999 Games, boardgamestore.nl of Bol.com verkopers-account nodig. Boardgamestore accepteert doorgaans nieuwe uitgevers na sample-test; 999 Games heeft strengere selectie
7. **Localisation** — NL-only versus EN — voor internationale markt EN-editie nodig (€3-8k vertaling + review)
8. **BoardGameGeek-listing** — voor community-zichtbaarheid essentieel. Gratis, vergt kwaliteit-check

### 4.5 · Vergelijking analog EQ met bekende PnP-successen

| Titel | Type | Prijs | Waarom werkte het? |
|---|---|---|---|
| **The Manager** (D. Rothwein, PnP) | Free download → zelf print | Gratis | Community-driven, developer-humor |
| **Backdoors & Breaches** (Black Hills) | PnP + retail box | Gratis PnP / $30 retail | Cyber-community, klein & krachtig |
| **Kanban Pizza Game** (agile42) | PnP alleen | Gratis | Trainer-tool, snel te leren |
| **Cards Against Humanity** | Retail + PnP | $25 / gratis PnP | Viraal, controverse |
| **Wingspan** (Stonemaier) | Alleen retail | €60 | Beauty + strategy + educative |
| **Terraforming Mars** (FryxGames) | Retail + expansions | €50-80 | Hardcore strategy fans |

**Lessen voor EQ analog:**
1. **Gratis PnP als voorportaal** genereert bewustzijn en early-adoption (Backdoors & Breaches-model)
2. **Retail-editie na PnP-validatie** — als PnP >1000 downloads bereikt, retail-versie rechtvaardigen
3. **Community-content-support** vroeg openzetten (custom missies, custom monsters via GitHub)
4. **Facilitator-track parallel** — training-tool licenties zijn hogere-marge dan retail

---

## 5 · Advies: hoe vermarkt je de analoge lijn?

### Optie A · Alleen PnP (gratis PDF)

- **Voor:** Nul-risico, brede reach, ideaal voor validatie
- **Tegen:** Geen directe omzet, moeilijk professioneel te positioneren
- **Rol in geheel:** funnel/awareness (top-of-funnel)

### Optie B · PnP + Print-on-Demand (Game Crafter/MPC)

- **Voor:** Fysiek beschikbaar zonder voorraad-risico
- **Tegen:** Prijspunt hoog (€80-120 door PoD-marge), langere levertijd
- **Rol in geheel:** enthousiast-hobbyisten-markt, cadeau-verkoop

### Optie C · Eigen kleinschalige oplage (100-500 stuks)

- **Voor:** Voorraad-marge, professionele retail-prijs (€50-70), professionele doos
- **Tegen:** Vereist voor-financiering, MOQ-risico, voorraad-management
- **Rol in geheel:** eerste 500 stuks voor workshops + gerichte verkoop, marge 60-70%

### Optie D · Kickstarter/Gamefound (v1 fantasy-editie)

- **Voor:** Validatie + voor-financiering + community in één; ideal voor RPG-fantasy-doelgroep
- **Tegen:** Vergt marketing-inspanning vooraf (video, artwork, campagne 30 dagen), fulfillment achteraf
- **Rol in geheel:** launch-moment voor v1, marktvalidatie zonder eigen risico

### Optie E · Dragon1-branded partner-editie (v2, met Mark Paauwe)

- **Voor:** Dragon1-community afzet-kanaal, gedeelde marketing, methodiek-legitimatie
- **Tegen:** Vergt goede partner-deal, mogelijk royalty-model (15-25%)
- **Rol in geheel:** flagship-workshop-product, high-margin B2B

### Optie F · Curriculum-pakket via HBO/universiteit

- **Voor:** Voorspelbare bulk-inkomsten, jaarlijkse licentie
- **Tegen:** Lange sales-cyclus (6-12 maanden voor eerste cursus-adoptie), curriculum-committee bureaucratie
- **Rol in geheel:** stabiele achtergrond-omzet, prestige

**→ Aanbevolen combinatie:**

1. **Fase 1 (maanden 1-3):** Optie A (gratis PnP) — zowel v1 als v2 downloadbaar via icthorse.nl. **Validatie**
2. **Fase 2 (maanden 3-6):** Optie B (PoD via Game Crafter) — voor hobbyisten die niet zelf willen printen. **Eerste omzet**
3. **Fase 3 (maanden 4-8):** Optie E (Dragon1 partner v2) — als Mark Paauwe akkoord — parallel-track. **B2B workshop-omzet**
4. **Fase 4 (maanden 6-9):** Optie D (Kickstarter v1 fantasy) — mits fase 1 en 2 positieve signalen geven. **Retail launch**
5. **Fase 5 (maanden 9-12):** Optie F (curriculum-deal) — begin met 1 pilot HBO/uni. **Stabiele omzet**
6. **Fase 6 (jaar 2):** Optie C (kleinschalige eigen oplage) — als schaal en klantenkennis dat rechtvaardigen

---

## 6 · Twee sporen — go-to-market analog

### Spoor Mark Paauwe (Dragon1)

**Waarde-uitwisseling (fysiek versterkt):**
- Wat Mark biedt: methodiek-blessing, community-toegang, Dragon1-events (product uitgedeeld op conferentie)
- Wat wij bieden: eerste fysieke Dragon1-workshop-set ooit, tastbaar merch-artikel voor Dragon1-community, uitbreiding boekverkoop (Paauwe's "Dragon1 Fundamentals" boek + het spel als workshop-companion)
- Model-voorstellen:
  1. Co-productie fysieke Dragon1-editie — Dragon1 subsidieert 50% van eerste oplage (200 stuks), krijgt 50% inventaris voor eigen community
  2. Royalty per verkocht spel (15-20% van retail)
  3. Bundeling met Paauwe's boek "Dragon1 Fundamentals" (ISBN 9789490873004) — cross-promotion
  4. Dragon1-training + spel gebundeld — trainer krijgt fysieke set bij certificering

**Fysiek als "boardroom-legitimiteit"-argument:**
- CIO's die niet mee-doen aan digitale workshop-simulaties, doen wel mee aan fysieke sessies
- Fysieke set kan op de plank in Paauwe's kantoor staan — visueel merken-anker

**Risico's:**
- Paauwe wil eigen productie doen (verlies aan iCt-controle)
- Retail-prijs conflict tussen Dragon1-editie (€150 workshop-editie) en publieke retail (€70)
- MOQ eerste productie €5-10k — wie financiert?

### Spoor Peter v/d Hulst (Staff)

**Waarde-uitwisseling (fysiek versterkt):**
- Wat Peter/Staff biedt: bestaande trainings-set voor procesarchitectuur; kanalen voor levering; klant-portefeuille
- Wat wij bieden: kant-en-klare fysieke set voor procesarchitectuur-workshop (v3-analoog, aangepast content-set)
- Model-voorstellen:
  1. White-label proces-editie (Staff-branding + Staff-content) — €15k-25k eenmalige ontwikkeling + €5k/jaar content-updates
  2. Fysieke Staff-editie als geschenk bij Staff-training — 50-200 dozen op maat gedrukt — €30-50 per doos bulk
  3. Revenue-share bij verkoop via Staff-kanaal (Staff 60% / iCt Horse 40%)

**Risico's:**
- Peter's bestaande proces-game is óók fysiek — mogelijk kannibalisme
- Staff-training verwacht IP-overdracht (engine + content)
- Eventuele conflict met Dragon1-versie in dezelfde markt

**Mitigatie:**
- Overlap-analyse als eerste stap (vraag Peter naar Staff Proces-game specificaties)
- Aparte content-set (procesarchitectuur — value stream, BPMN — versus EA-Dragon1)
- Engine-IP nooit overdragen

### Nieuwe spoor: **Kickstarter/Gamefound-onafhankelijk**

**Fysieke Kickstarter-campagne v1 (fantasy-RPG-editie):**
- **Doelgroep:** RPG/D&D-community + tech-hobbyisten
- **Goal:** €10k-15k (conservatief, gedekt eerste MOQ 200 stuks)
- **Stretch goals:** extra content-uitbreidingen, deluxe-editie met houten tokens, EN-editie
- **Timeline:** 3-6 maanden voorbereiding + 30 dagen campagne + 6-12 maanden fulfillment
- **Kosten:** €3-8k marketing + fees + fulfillment-partner
- **Waarom voor v1 en niet v2:** RPG-fantasy = boardgamer-taal, Dragon1 is te niche voor mass crowdfunding

**Voordeel:** geen partner nodig, directe validatie of markt bestaat.

---

## 7 · Advies executie (analog)

1. **Deze week:** playtest sessie organiseren met 3-5 EA-collega's (v2 fysiek) + tech-vriendengroep (v1 fysiek). Gebruik zelfgeprint PnP-materiaal. Facilitator = ik zelf. Duur: 2-3 uur.
2. **Week +1-2:** playtest-bevindingen verwerken in `docs/analog_v*_rpg.md` (versie 0.2)
3. **Week +2-3:** PnP-versies (PDF) publiceren op icthorse.nl. Free downloads. Meten: downloads/week.
4. **Week +3-4:** contact leggen met The Game Crafter voor upload PoD-materiaal (v1 first). Fee: setup gratis, per verkoop 30% commissie
5. **Maand 2:** gesprek met Mark Paauwe over v2-fysiek co-productie (parallel aan digital pitch die al loopt)
6. **Maand 2-3:** eerste betaalde workshop v2 als POC (facilitator = ik zelf, klant = 1 consultancy-firma of 1 team op Werk-DB)
7. **Maand 4-6:** afhankelijk van signalen: Kickstarter v1 opstarten (2-3 maanden voorbereiding vereist) OF curriculum-pilot HBO/uni
8. **Maand 6-9:** eerste eigen kleinschalige oplage (200-500 stuks) — mits validatie voldoende is
9. **Maand 9-12:** internationale variant (EN-editie) alleen als NL-editie zich bewezen heeft

**Onmisbaar voor go-live analog:**
- Playtest (minimaal 5 rondes) → **€0-2k (eigen tijd + koffie)**
- Facilitator-gids v1 + v2 → **€5-10k schrijven**
- Doos + grafisch design → **€2-5k**
- PnP-PDF met snijlijnen → **€1-2k opmaak**
- Shop-integratie op icthorse.nl (Gumroad of Woo Commerce) → **€1-3k**
- Kickstarter-video (2-3 min) → **€2-5k**

**Totaal go-live budget (voorzichtig):** **€10k-25k**
**Time-to-first-euro:** ~3-4 maanden (PnP PDF-verkoop)
**Time-to-materiële-omzet:** ~6-9 maanden (workshop-verkoop + Kickstarter)

---

## 8 · Financiële projectie (jaar 1, indicatief analog)

| Scenario | Verkoop-volume | Omzet | Marge |
|---|---|---|---|
| **Alleen PnP PDF-verkoop** | 200-500 downloads à €10 | €2k-5k | 90% |
| **PnP + PoD via Game Crafter** | 30-80 fysieke sets | €2k-6k (bruto), €500-2k marge | 25-30% |
| **PnP + Workshops v2** | 5-15 workshop-sessies à €1.500 | €7,5k-22,5k | 65% |
| **Alle bovenstaande + Dragon1-partner** | 100-300 branded sets + 10-25 workshops | €25k-75k | 40-55% |
| **Kickstarter v1 fantasy (succesvol)** | 200-600 backers à €55 | €11k-33k | 40-50% (na fulfillment) |
| **Optimistisch scenario: alle sporen tegelijk** | 400-1000 units + 20-40 workshops | €50k-150k | 40-55% |

**Sensitiviteits-scenario:**
- **Ondergrens:** alleen PnP + 3-5 workshops → €10k-15k jaar 1
- **Realistisch:** PnP + PoD + Dragon1-samenwerking + 10 workshops → €30k-60k jaar 1
- **Bovengrens:** alle sporen actief, Kickstarter geslaagd → €80k-150k jaar 1

---

## 9 · Voor- en nadelen versus digitaal

| Aspect | Digitaal | Analog |
|---|---|---|
| **Productiekosten** | Nul (single-file HTML) | €25-90 per doos |
| **Distributie-kosten** | Nul (URL) | €5-15 verzending per doos |
| **Marginale kosten** | Nul | 20-40% van retail |
| **Bruto-marge** | ~95% | 30-70% (afhankelijk van kanaal) |
| **Adoptie-drempel** | Zeer laag (klik URL) | Hoger (koop, printen, opzet) |
| **Herbruikbaarheid** | Onbeperkt | Onbeperkt (fysiek slijt maar niet snel) |
| **Team-dynamiek** | Beperkt (single-player of remote) | Hoog (tafel-sessie 2-8 spelers) |
| **Boardroom-legitimiteit** | Middelmatig (nog altijd "app") | Hoog (professioneel object) |
| **Retail-kanaal** | Niet realistisch | Bol.com, boardgamestore.nl, 999 Games |
| **Community-signal** | Website-visits | BoardGameGeek-listing, Kickstarter-tracker |
| **Prijs-perceptie** | Verwachting: €0-25 | Verwachting: €40-150 |
| **Prijspunt-headroom** | Klein | Groter |
| **Piraterij-risico** | Zeer hoog (open URL) | Laag (fysiek dupliceerbaar met moeite) |
| **Playtest-cyclus** | Iteratie binnen dagen | Iteratie in weken/maanden |
| **Kwaliteitseisen** | Software-testing | Print-kwaliteit, componenten |
| **Persoonlijk cadeau/plank-waarde** | Nul | Hoog (op de plank blijft "iets") |

**Kern-inzicht:** analog en digitaal zijn **complementaire** productlijnen, geen vervanger van elkaar. Bepaalde doelgroepen (workshop-facilitators, docenten, corporate-gifts) willen fysiek; anderen (studenten, junior architecten, remote-teams) willen digitaal. **De ideale strategie is beide aanbieden — met bewuste positionering per klantsegment.**

---

## 10 · Openstaande vragen

1. Zijn er contractuele beperkingen op productie/verkoop van fysieke items via iCt Horse (BTW-nummer, verkoop-registratie, retour-beleid)?
2. Wat is de exacte kostenstructuur van The Game Crafter voor board+kaartset in retail-formaat? (offerte aanvragen)
3. Kan Kickstarter/Gamefound legaal + praktisch vanuit Nederland (BTW-implicaties, EU-shipping, VS-fulfillment)?
4. Zijn universiteiten (HAN, UvA, Nyenrode, Open Universiteit) geïnteresseerd in EA-curriculum-materiaal? Testen door 1-2 curriculum-committee-benaderingen
5. Wat is de MOQ voor kwaliteits-kaartendrukwerk in NL (via bv. Cartamundi of Boda)? Prijs per doos bij 100/250/500/1000 stuks?
6. Wil 999 Games (Nederlandse retail-distributeur) fungeren als distributiepartner? Vergt eerst review, sample-versie sturen
7. Is er behoefte aan een **hybride** editie (fysieke set + digitale companion-app voor scoring, achievements-tracking)?
8. Kan de fysieke v2 als "Dragon1-officieel" gecertifieerd worden zonder €6k-licentie-conflict eerst op te lossen?

---

## Bijlagen

- `docs/analog_v1_rpg.md` — Print & Play design v1 (fantasy-RPG)
- `docs/analog_v2_dragon1.md` — Print & Play design v2 (Dragon1)
- `docs/analyse_deepdive.md` — Deep-dive analyse digitale versies (context)
- `docs/pitch_mark_paauwe.md` — Digital-versie-pitch (parallel spoor)
- `docs/pitch_peter_hulst.md` — Digital-versie-pitch (parallel spoor)

*Intern beslissingsstuk — niet doorsturen naar Mark of Peter (bevat cross-referenties tussen beide sporen).*

**Datum eerste versie:** 2026-07-07
**Auteur:** Claude Opus 4.7 (1M context) namens Christian Glebbeek
