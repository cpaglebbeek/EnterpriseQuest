# Enterprise Quest — Deep Dive Analyse (intern)

**Auteur:** Christian Glebbeek (iCt Horse)
**Datum:** 2026-07-06
**Scope:** commerciële haalbaarheid van EnterpriseQuest v1 (fantasy) + v2 (Dragon1) als **serious game + train-de-trainer product**, met twee mogelijke go-to-market-partners: **Mark Paauwe (Dragon1)** en **Peter v/d Hulst (Staff)**.
**Positie:** dit document is intern beslissingsstuk — bevat kruisverwijzingen tussen beide sporen. De losse pitches per partner (zie bijlagen) bevatten dat niet.

## 1 · Samenvatting (management)

**Uniek?** Ja, redelijk. Er zijn digitale serious games rond procesarchitectuur en projectmanagement (Nederland: De Processpecialisten, Passionned, LEGO Serious Play-facilitators; internationaal: Kanbanzine, Prosci-simulaties). Er is echter géén breed-uitgerold digitaal single-file bordspel dat expliciet **Enterprise Architecture volgens een specifieke methode (Dragon1)** in de kern zet. De combinatie **"speelbaar in browser · geen installatie · methode-getrouw · train-de-trainer-optie"** vult een gat dat traditionele klassikale trainingen niet dekken.

**Vermarktbaar?** Voorwaardelijk ja, mits verpakt als **workshop-tool + certificering** en niet als losse app-verkoop. De EA-trainingsmarkt is klein maar hoogwaardig (uurtarieven €120-250 voor trainers). Prijspunt: €2.500-5.000 per organisatie per jaar SaaS-licentie, of €7.500-15.000 train-de-trainer-traject per instructeur.

**1 spel, 2, of meerdere?** Antwoord: **twee sporen naast elkaar**, mogelijk 3 op termijn:
- **v1 (fantasy)** — bekendheid, community, gamification voor juniors/studenten, gratis funnel
- **v2 (Dragon1)** — professioneel, betaalde workshop-tool, senior-doelgroep
- **v3 (proces-editie)** — óptioneel, alleen als Staff/Peter partner-relatie geformaliseerd wordt

**Advies partners:**
- **Mark Paauwe (Dragon1)** — natuurlijke fit. v2 IS Dragon1. Voorstel: gezamenlijke launch als "officiële Dragon1-gamified workshop-tool", train-de-trainer voor Dragon1-community, licentie/royalty-model. **Risico:** bestaande €6k licentie-discussie moet eerst zijn opgelost.
- **Peter v/d Hulst (Staff)** — niet-natuurlijke fit voor v2 (Dragon1 vs procesarchitectuur), wél voor eventuele v3 (proces-editie). Voorstel: white-label proces-editie voor Staff/StaffKennis-portfolio, geen Dragon1-verwijzing. **Risico:** overlap met interne Staff-proces-game (details onbekend — moet Peter vragen).

**Gevaar:** Mark en Peter zijn potentieel concurrenten in EA/BPM-consulting-markt. Aparte gesprekken, aparte pitches, geen kruisreferenties. Dit document blijft intern.

## 2 · Wat hebben we

### v1 · Architect's Dungeon (v0.0.1-Zachman, LIVE)
- Fantasy-RPG-flavor over EA/TOGAF/cloud/security/data/AI
- 6 klassen, 40 tiles / 12 regio's, 250 kaarten, 22 monsters, 51 achievements
- D20 combat, Web Audio, LocalStorage, responsive
- 175 KB single-file HTML, geen dependencies
- LIVE: https://icthorse.nl/EnterpriseQuest/v1/EnterpriseQuest.html
- GitHub PUBLIC AGPL-3.0

### v2 · Dragon1 Architect's Journey (v0.2.0-Paauwe, LIVE)
- Professionele Dragon1-workshop-simulatie
- 8 rollen (EA/SA/BA/IA/SecA/CIO/IT-Mgr/Student), 16 organisatie-onderdelen (4×4 bord)
- 40 missies + 40 uitdagingen + 30 events + 15 Dragon1-artefacten (met cascade-vereisten: Vision Blueprint → Strategy Map → Capability Map → BRM → Application Landscape → …)
- **Geen combat.** Winnen door presentatie aan Raad van Bestuur → eindscore op 8 aspecten (Samenhang / Strategie-uitlijning / Businesswaarde / Innovatie / Governance / Security / Digitale volwassenheid / Stakeholdertevredenheid) + verbeterpunten
- 12 dashboard-metrieken
- 156 KB single-file HTML
- LIVE: https://icthorse.nl/EnterpriseQuest/v2/EnterpriseQuest.html

### Gedeelde technische fundering
- Web Audio API voor geluid (geen assets)
- LocalStorage save/load + autosave
- Responsive (desktop / tablet / mobiel)
- Openbaar op GitHub (AGPL-3.0), free-tier hosting via Hostinger
- Multi-editie-launcher op https://icthorse.nl/EnterpriseQuest/

## 3 · Uniekheidsanalyse

### 3.1 Bestaand landschap

| Segment | Voorbeelden NL | Voorbeelden internationaal | Format |
|---|---|---|---|
| **Klassikale EA-training** | Bosman/Novius, InfoSupport, Xebia, Ordina | Open Group TOGAF, Gartner EA cursus | Fysiek + PDF-cases |
| **BPM / Proces simulaties** | De Processpecialisten, Passionned Group | Prosci, Kanbanzine | Fysieke bordspellen + facilitator |
| **E-learning EA** | Sirius EA, Global Knowledge | Coursera, edX, Pluralsight | Video + quiz |
| **Serious games (breder)** | LEGO Serious Play, Play14 | Beer Distribution Game, Fifth Discipline | Fysiek + workshop |
| **Digitale bordspellen browser** | (zeer beperkt in NL EA-segment) | Board Game Arena varianten | Web-based |

### 3.2 Uniekheid EQ v1

- **Fantasy-flavor bovenop EA-content:** creatieve funnel voor juniors/studenten die TOGAF-materie afschrikwekkend vinden
- **Volledig gratis, browser-based, geen installatie:** lage adoption-drempel
- **250 kaarten met echte EA-terminologie:** herkenbaar voor doelgroep
- **Risico:** RPG-verpakking wordt door senior EA's als "onprofessioneel" gezien → beperkt bruikbaar in enterprise-workshops

**Unique-Selling-Points:**
1. Enige browser-native EA-gamification met Dutch-native content
2. Geen registratie, geen dataverzameling → laagdrempelig
3. Open-source (AGPL-3.0) → community-uitbreidbaar

### 3.3 Uniekheid EQ v2

- **Methode-getrouw Dragon1:** artefact-cascade (Vision → Strategy → Capability → BRM → Application Landscape → …) volgens Paauwe's Dragon1 EA-framework
- **Serious game, geen fantasy:** past in professionele workshop-context (CIO's, boardroom-oefeningen, opleidingen)
- **Eindrapport op 8 aspecten:** direct bruikbaar als reflectie-instrument in trainings-context
- **8 rollen:** rollenspel dimensie (CIO vs EA vs Student ervaart dezelfde case verschillend)

**Unique-Selling-Points:**
1. **Enige** digitale Dragon1-gecertifieerde workshop-simulatie in de markt (naar mijn weten, wacht op Paauwe-verificatie)
2. Herbruikbaar in klaslokaal én asynchroon zelfstudie
3. Uitbreidbaar met eigen missies/uitdagingen (JSON-content-schema)
4. Modulair per organisatie-type: profit / non-profit / overheid / zorg via andere content-set

### 3.4 Vergelijking met Staff-portfolio (op basis van openbare Nederlandse proces-simulatie-markt)

Publieke bronnen tonen dat Nederlandse procesarchitectuur-simulaties (bv. Processpecialisten, Passionned) typisch werken met:
- Fysieke of hybride bordspellen
- Focus op procesketens, bottlenecks, klant-perspectief
- Facilitator-geleide sessies (typisch 4-8 uur)
- Prijspunt €1.000-3.000 per sessie voor 8-16 deelnemers

Wat de exacte "Proces-game van Staff" doet — de aan Peter v/d Hulst gekoppelde variant — is uit openbare bronnen niet vindbaar. **Vraag aan Peter:** hoe wordt dat product exact verpakt? Is er digitale versie? Wat is content-scope (BPM / Six Sigma / procesarchitectuur / value stream mapping)?

**Voorlopige inschatting overlap EQ v2 ↔ Staff Proces-game:**
- **Waarschijnlijk beperkt** — EQ v2 is EA-methodiek-first (Dragon1: capability, vision, roadmap, applicatielandschap), Staff-proces-game is (aangenomen) procesketen-first (BPMN, value stream, throughput)
- **Mogelijke overlap:** rollen (business owner / proces-eigenaar), scoring-mechaniek, workshop-format
- **Complementair vermarktbaar:** dezelfde klant, verschillende agendapunten (proces-inrichting vs. architectuur-governance)

## 4 · Vermarktbaarheid

### 4.1 Doelgroepen

| Doelgroep | v1 | v2 | Prijsbereidheid |
|---|---|---|---|
| Studenten EA (HAN, Nyenrode, Open Universiteit) | ★★★ | ★★ | €0-25/gebruiker |
| Junior architecten (0-3 jr ervaring) | ★★★ | ★★ | €50-100/gebruiker |
| Senior architecten / CIO's | ★ | ★★★ | €150-300/gebruiker |
| Consultancy-firma's (interne training) | ★ | ★★★ | €2.500-5.000/jaar |
| Dragon1-community / partners | — | ★★★ | €5.000-15.000/train-de-trainer |
| Enterprise-klanten (interne workshops) | — | ★★★ | €5.000-25.000/deployment |
| Uitzend/detacheringsbureaus (Staff, Ordina, Xebia) | ★ | ★★★ | €5.000-15.000 whitelabel |

### 4.2 Verdienmodellen

1. **Freemium** — v1 gratis, v2 licentie (€150/jaar per gebruiker, €2.500-5.000 per organisatie)
2. **Workshop-tool licensing** — €300-500 per sessie voor gecertificeerde trainer
3. **Train-de-trainer certificering** — €7.500-15.000 per instructeur, jaarlijkse hercertificering €500-1.000
4. **White-label** — €10.000-25.000 eenmalig + jaarlijkse content-updates €2.500-5.000
5. **Consulting-cross-sell** — game als top-of-funnel voor grotere EA-advies-opdrachten (€25.000-100.000+)
6. **Content-marketplace** — externe experts publiceren eigen missie-sets (revenue-share 70/30)

### 4.3 TAM/SAM/SOM Nederland

- **TAM (Total Addressable Market)** — Nederlandse EA-training/-workshop-markt: ~€25-40M/jaar (geschat op basis van EA-training bureaus × trainer-tarieven)
- **SAM (Serviceable)** — digitale/blended EA-simulaties: ~€3-5M/jaar
- **SOM (year-1 realistisch)** — €50k-150k met 1 productmatige launch + 1 partnerkanaal

### 4.4 Kritische succesfactoren

1. **Content-diepte** — 250 kaarten (v1) en 110 kaarten (v2) is genoeg voor 1-2 sessies. Voor recurring gebruik nodig: 3-5× uitbreiding (procedureel gegenereerd of content-marketplace)
2. **Facilitator-gids** — trainer moet weten hoe hij post-game debrief doet. Ontbreekt nu volledig; is separate deliverable van €5-15k
3. **Certificerings-framework** — Dragon1 heeft methode-eigenaar (Paauwe). Zonder Paauwe's blessing kan v2 niet als "Dragon1 gecertifieerd" verkocht worden
4. **Multi-organisatie ondersteuning** — server-side scoreboards, cross-sessie-analytics — nog niet aanwezig. Bijkomend €15-30k ontwikkelwerk
5. **Content-lokalisatie** — nu 100% NL. Voor internationale markt EN-editie (€3-8k vertaalwerk + content-check)

## 5 · Advies: 1 spel of meerdere?

### Optie A · Één product (EQ v2 alleen)
- **Voor:** simpelste verhaal, focus op professionele markt
- **Tegen:** verlies je de gamification-funnel (v1) en de studenten-doelgroep

### Optie B · Twee producten naast elkaar (v1 + v2) **← huidige situatie**
- **Voor:** funnel-strategie werkt (v1 gratis → v2 betaald), 2 doelgroepen bediend
- **Tegen:** onderhoudslast dubbel, content-fragmentatie
- **Advies:** deze houden, mits duidelijke funnel-strategie geformaliseerd

### Optie C · Drie producten (v1 + v2 + proces-editie v3)
- **Voor:** dekt Dragon1 (EA) én proces-architectuur; kan met Staff/Peter als partner
- **Tegen:** vergt aparte content-lijn (~€15-30k dev), extra positionering
- **Advies:** alleen als Staff-partner-relatie geformaliseerd is

### Optie D · Modulair per organisatie-type
- **Voor:** hoge relevantie per klantsegment (bank vs zorg vs overheid vs retail)
- **Tegen:** content-explosion, marketing-fragmentatie
- **Advies:** dit is een fase 2-optie (na 5+ paying klanten), niet nu

**→ Aanbeveling: Optie B (2 sporen) nu, Optie C (v3 procesarchitectuur) alleen als Peter-samenwerking materieel wordt.**

## 6 · Twee sporen — go-to-market

### Spoor Mark Paauwe (Dragon1)

**Waarde-uitwisseling:**
- **Wat Mark biedt:** Dragon1-methodiek-blessing, community-toegang (Dragon1-partners, licentie-nemers), positionering als "officieel Dragon1"
- **Wat wij bieden:** de eerste digitale Dragon1-workshop-simulatie, opgeleverd, LIVE, deelbaar met community
- **Model-voorstellen:**
  1. Royalty-per-licentie (Dragon1 krijgt 15-25% van SaaS-omzet)
  2. Co-branded certificering (train-de-trainer traject 50/50)
  3. Whitelabel via Dragon1.com (Dragon1 verkoopt, iCt Horse levert; revenue-share 60/40 Dragon1/iCt)
- **Randvoorwaarden:** bestaande licentie-discussie (€6k) eerst opgelost; expliciete methode-eigenaar-verantwoording in game

**Risico's:**
- Mark ziet EQ v2 als afgeleid werk van Dragon1 → licentie-claim
- Mark bouwt zelf een variant → onze investering verloren
- Dragon1-adoptie in NL blijft niche → schaal beperkt

**Mitigatie:**
- Contract vooraf, exclusiviteit voor EQ v2 als officiële Dragon1-serious-game
- Wederzijdse non-compete over serious-game-format 2-3 jaar
- IP: engine blijft van iCt Horse (AGPL-3.0 dekt), content-set kan met Dragon1 gedeeld worden

### Spoor Peter v/d Hulst (Staff)

**Waarde-uitwisseling:**
- **Wat Peter/Staff biedt:** verkoop-kanaal binnen bestaande klantportefeuille, bestaande facilitators, Staff-branding
- **Wat wij bieden:** digitale variant naast fysieke Staff Proces-game; techniek + engine; snelle marktintroductie
- **Model-voorstellen:**
  1. Whitelabel v3 procesarchitectuur-editie voor Staff-portfolio (eenmalig €15-25k + €5k/jaar content-onderhoud)
  2. Revenue-share op verkopen via Staff-kanaal (Staff 60% / iCt Horse 40%)
  3. Custom-development contract voor Staff-specifieke content-varianten
- **Randvoorwaarden:** Peter's Proces-game specificaties verkrijgen; overlap-analyse doen voor je positioneert; **GEEN mention van Dragon1** (positionering-conflict binnen Staff-doelgroep)

**Risico's:**
- Overlap met Staff Proces-game groter dan gedacht → conflict
- Peter ziet ons als leverancier ipv partner → lage marges
- Staff verwacht IP-overdracht → engine kwijt

**Mitigatie:**
- Duidelijke scope-scheiding (proces-KETEN vs proces-ARCHITECTUUR)
- Engine IP nooit overdragen — alleen content-varianten
- Vaste licentie ipv per-sessie (voorspelbare omzet)

## 7 · Advies executie

1. **Deze week:** verstuur pitch aan Mark Paauwe eerst (mail apart, PDF-attachment, geen mention van Peter/Staff)
2. **Week +1:** ontvang reactie Mark → indien positief: contract-onderhandeling; indien "nee": alleen Staff-spoor uitwerken
3. **Week +1 parallel:** verstuur pitch aan Peter v/d Hulst (mail apart, PDF-attachment, geen mention van Dragon1)
4. **Week +2:** eerste demo-sessie plannen (30 min live-play) met partij die eerst positief reageert
5. **Week +3-4:** contract-fase — vast prijspunt, ondersteuningsniveau, IP-clausule
6. **Maand 2:** eerste betaalde workshop-cyclus (5-10 deelnemers) als POC
7. **Maand 3-6:** schaal, content-uitbreiding, mogelijk v3 (Staff spoor)

**Onmisbaar voor go-live:**
- Facilitator-gids (5-10 pagina's per editie) — nog te schrijven — ~€5-10k budget
- Aftermovie / promo-video (2-3 min) — via Plaud+Screen-recording — ~€1-2k
- Sales-pagina op icthorse.nl — bestaat nog niet — ~€2-3k / 8-16 uur werk

**Geen deal-breakers, wel gaten:**
- Multi-user server-side scoreboard
- SSO / SAML voor enterprise-integraties
- Analytics-dashboard voor trainer (sessies, deelnemers, scores)

## 8 · Financiële projectie (jaar 1, indicatief)

| Scenario | Klanten | Omzet | Marge |
|---|---|---|---|
| **Zonder partner** — organische verkoop | 2-5 | €5k-25k | 60% |
| **Met Dragon1 (Paauwe)** — co-branded launch | 8-15 | €40k-120k | 45% (na royalty) |
| **Met Staff (Peter)** — whitelabel v3 | 5-10 (Staff-klanten) | €25k-75k | 40% (na revenue-share) |
| **Beide partners** | 15-25 | €70k-200k | 40-45% |

Sensitiviteit: elke -50% aanname op klantvolume → -50% omzet. Kritische factor is **eerste 3 betaalde klanten** — daarna is schaal proces-gedreven.

## 9 · Openstaande vragen

1. Is Mark Paauwe bereid tot co-branded / royalty-model, of blijft hij bij lump-sum licentie-eis?
2. Wat is de exacte scope, content-diepte en digitalisering-graad van de Staff Proces-game? (vraag rechtstreeks aan Peter, of via netwerk)
3. Zijn er contractuele beperkingen op mijn kant (bijv. Staff-samenwerking, andere klanten) die exclusiviteit met een van beide partners in de weg staan?
4. Is v3 (procesarchitectuur-editie) technisch schaalbaar met huidige content-schema, of vergt het engine-aanpassingen?
5. Wat is de openstaande €6k Dragon1-licentie-situatie (uit `project_dragon1_samenwerking.md`) — vóór of nà nieuwe pitch aankaarten?

## Bijlagen

- `pitch_mark_paauwe.md` (aparte pitch — bevat GEEN mention van Staff)
- `pitch_peter_hulst.md` (aparte pitch — bevat GEEN mention van Dragon1)

*Intern beslissingsstuk — niet doorsturen naar Mark of Peter.*
