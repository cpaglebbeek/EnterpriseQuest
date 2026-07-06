# Digitale Enterprise-simulatie — voorstel voor Staff

**Voor:** Peter v/d Hulst — Staff
**Van:** Christian Glebbeek — iCt Horse
**Datum:** 2026-07-06
**Onderwerp:** Voorstel — digitale workshop-simulatie voor Enterprise-onderdelen, mogelijk whitelabel voor Staff-portfolio

## Kern in één regel

Ik heb een volledig werkende **digitale serious-game** gebouwd — browser-native, direct speelbaar op https://icthorse.nl/EnterpriseQuest/ — die architecten, CIO's, IT-managers en studenten leert werken met de bouwstenen van een organisatie (business-domeinen, applicatie-landschap, data-platforms, SOC, project-portfolio, governance). Ik zie een concreet gezamenlijk product-spoor met Staff en zou graag onderzoeken of Staff daar een rol in wil spelen.

## Wat het is, in normale taal

Iemand kiest een rol (Enterprise Architect, Solution Architect, Business Architect, Information Architect, Security Architect, CIO, IT-Manager, of Student). Vervolgens beweegt hij over een 4×4 bord van **16 organisatie-onderdelen** — van Directiekamer en Strategiecentrum tot Business Domein, HR, Finance, Operations, Sales, Klantenservice, Applicatielandschap, Dataplatform, Integratielaag, Cloudplatform, Security Operations Center, Innovatielab, Project Portfolio en Governance Board.

Op elke locatie krijgt hij te maken met:
- **40 missies** — concrete architectuur-opdrachten die deliverables opleveren (bv. Vision Blueprint, Capability Map, Application Landscape, Governance Framework, Transformation Roadmap)
- **40 uitdagingen** — realistische organisatie-problemen (Legacy-systeem onmisbaar, Ransomware, NIS2/DORA-deadline, Fusie in 6 maanden, Shadow-IT ontdekt, Vendor kondigt EOL aan, Datalek, Talent vertrekt, R&D-budget onder druk) — elke uitdaging heeft **3-4 keuze-opties** die je in rollenspel moet afwegen
- **30 events** — RFP, Architecture Review Board, hackathon, buy-vs-build, multi-cloud dilemma, Copilot-uitrol, GreenOps-metric

Aan het einde presenteert de speler aan een virtuele Raad van Bestuur. Het spel genereert een **evaluatierapport** met scores op 8 aspecten (Samenhang, Strategie-uitlijning, Businesswaarde, Innovatie, Governance, Security, Digitale volwassenheid, Stakeholdertevredenheid) plus concrete verbeterpunten. Trainer kan dit rapport gebruiken als debrief-basis.

## Wat het technisch is

- Één HTML-bestand (156 KB), speel offline door in browser te openen
- Geen installatie, geen registratie, geen dataverzameling buiten LocalStorage van de speler zelf
- Web Audio API voor geluid, autosave
- Responsive desktop / tablet / mobiel
- Content in JSON (missies / uitdagingen / events / artefacten / locaties / rollen / achievements) — **nieuwe content zonder code-werk** toe te voegen
- Open source op https://github.com/cpaglebbeek/EnterpriseQuest (AGPL-3.0)

## Waarom Staff

Staff heeft een sterke Nederlandse voetafdruk in kennis-professionalisering en werkveld-training (uit mijn ervaring met de StaffKennis-portfolio en de manier waarop Staff met opleiding, detachering en klant-organisaties werkt). Wat ik zie:

1. **Digitale training-formats** groeien fors sneller dan klassikale trainingen
2. **Hybride blended learning** (video + simulatie + debrief) is de norm bij grotere organisaties
3. **Facilitator-geleide serious games** blijven waardevol, maar de fysieke-bordspel-vorm heeft schaal-limieten
4. **Staff-klanten** (grote uitzend-/detacherings-doelgroep, klant-organisaties in overheid, zorg, corporate) hebben behoefte aan actuele, herbruikbare workshop-tools

Ik ken de exacte scope van **jouw eigen proces-simulatie** binnen Staff niet — dat is de eerste vraag ik heb: wat is die vandaag, wat mist er nog, en waar zou een aanvullend digitaal instrument passen. Op basis van openbaar zichtbare procesarchitectuur-simulaties in Nederland (De Processpecialisten, Passionned) zie ik dat die typisch procesketen-first zijn (BPMN, value stream, throughput). Wat ik heb gebouwd is architectuur-first (business-domeinen, capability, applicatielandschap, governance). **Waarschijnlijk complementair, niet overlappend** — maar dat wil ik graag met je verifiëren.

## Wat ik voorstel — samenwerkings-opties

Ik zie meerdere formats waarop Staff en iCt Horse dit gezamenlijk kunnen ontsluiten:

### Optie A · Whitelabel voor Staff-portfolio

iCt Horse levert de engine en een architectuur-content-set. Staff verpakt onder eigen branding, integreert in bestaande opleidings- en klant-trajecten. Eenmalige integratie-fee €15k-25k + jaarlijkse content-updates €5k. Staff behoudt volledige klantrelatie, iCt Horse levert onderhoud en uitbreidingen.

### Optie B · Custom-development — proces-editie

Als jouw proces-simulatie behoefte heeft aan een digitale variant naast fysieke sessies, kan ik met dezelfde engine een **proces-architectuur-editie** bouwen — bord met proces-ketens ipv organisatie-onderdelen, kaarten met BPMN-uitdagingen, scoring op procesvolwassenheid en throughput. Development ~€25k-40k, exclusief voor Staff-portfolio.

### Optie C · Revenue-share sales

Staff verkoopt vanuit bestaande klantportefeuille naar architectuur-relevante klanten. Revenue-split 60/40 Staff/iCt Horse per gesloten deal. iCt levert product, Staff levert sales + facilitation.

### Optie D · Content-partnership

Staff-experts leveren case-content (bijv. Staff-klanten anonimiseren, sector-specifieke uitdagingen). iCt Horse verwerkt in game. Content-royalty per verkocht licentie-jaar.

Wat past het beste bij hoe Staff typisch werkt? Ik heb geen voorkeur A priori — dat kan verkennend gesprek zijn.

## Financieel indicatief

Ruwe jaar-1 projectie via Staff-partnership (Nederlandse markt):
- 5-10 Staff-klanten die de workshop-tool inzetten: €25k-75k omzet
- Whitelabel-fee (indien Optie A): €15k-25k eenmalig
- Content-updates + support jaarlijks: €5k-10k

Marges hangen af van gekozen model.

## Wat ik graag zou weten

1. **Wat doet de Staff Proces-game vandaag?** Doelgroep, format, prijspunt, digitale variant of niet? Waar liggen mogelijk overlap of complementariteit?
2. **Werkt Staff met externe product-leveranciers?** Zo ja, welke format-voorkeur (whitelabel / revenue-share / custom-development)?
3. **Wie is bij Staff verantwoordelijk voor productontwikkeling en kennis-portfolio?** Ben jij de juiste ingang, of is er ook een productmanager die ik moet betrekken?
4. **Is er interesse in een 30-min demo?** Ik toon het live en we bespreken vervolg.

## Praktisch

- **Test het nu:** https://icthorse.nl/EnterpriseQuest/ (multi-editie launcher; kies de "Serious Workshop-simulatie" variant)
- **Directe link:** https://icthorse.nl/EnterpriseQuest/v2/EnterpriseQuest.html
- **Open source / code:** https://github.com/cpaglebbeek/EnterpriseQuest
- **Speeltijd voor smaakproef:** ~5 minuten om een korte workshop-run te maken en het evaluatierapport te zien

## Volgende stap

Als je interesse voelt: laat me een **datum voor 30 min video-call** komende 2 weken. Ik doe eerst 10 min live-play zodat je zelf de flow ervaart, dan 20 min zakelijk. Als je nu al twijfelt tussen "misschien" en "nee": speel het gerust eerst zelf 15 minuten en laat me kort weten wat je vindt. Ook een "nee" is waardevol — dan weet ik dat.

Ik zie hier reële kans op iets goeds. Ik hoor graag of Staff daar een rol in wil.

Met vriendelijke groet,

**Christian Glebbeek**
iCt Horse — Connecting the dots
cglebbeek@gmail.com
https://icthorse.nl · https://github.com/cpaglebbeek

---

*Bijlage: de game zelf, LIVE op https://icthorse.nl/EnterpriseQuest/v2/EnterpriseQuest.html*
