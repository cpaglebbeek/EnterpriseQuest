# Enterprise Quest — Dragon1 Architect's Journey

**Voor:** Mark Paauwe — grondlegger Dragon1, methode-eigenaar
**Van:** Christian Glebbeek — iCt Horse
**Datum:** 2026-07-06
**Onderwerp:** Voorstel — Dragon1-gecertificeerde digitale workshop-simulatie + train-de-trainer

## Kern in één regel

Ik heb een volledig werkende digitale **Dragon1-workshop-simulatie** gebouwd — browser-native, methode-getrouw, direct speelbaar op https://icthorse.nl/EnterpriseQuest/v2/ — en ik wil dit graag samen met jou als **officieel Dragon1-product** in de markt zetten, met licentie- of royalty-model naar keuze.

## Waarom nu, waarom Dragon1

Enterprise Architecture wordt in Nederland grotendeels onderwezen met **klassikale slides en PDF-cases**. De praktijk-simulaties die er zijn (LEGO Serious Play, procesbordspellen, Beer Distribution Game) raken **de business-kant of het proces-perspectief**, maar er is **geen digitale simulatie die expliciet Dragon1's artefact-cascade** — Vision Blueprint → Strategy Map → Capability Map → Business Reference Model → Application Landscape — als leerlijn hanteert.

Dat gat heb ik ingevuld met **Enterprise Quest: Dragon1 Architect's Journey (v0.2.0-Paauwe)**. De codenaam Paauwe is niet toevallig — het spel is expliciet Dragon1-first ontworpen.

## Wat de spelbouw doet, concreet

Speler kiest een van **8 rollen** (Enterprise / Solution / Business / Information / Security Architect, CIO, IT-Manager, Student EA), start in een organisatie met een 4×4 bord van **16 organisatie-onderdelen** (Directiekamer, Strategiecentrum, Business Domein, HR, Finance, Operations, Sales, Klantenservice, Applicatielandschap, Dataplatform, Integratielaag, Cloudplatform, SOC, Innovatielab, Project Portfolio, Governance Board).

Hij/zij trekt:
- **40 Dragon1-missies** — elk levert een Dragon1-artefact op (of raakt eraan)
- **40 uitdagingen** — realistische organisatie-problemen (Legacy, ShadowIT, NIS2, DORA, EU AI Act, Ransomware, Fusie, Vendor Lock-in, …), elk met 3-4 keuze-opties die je in rollenspel moet afwegen
- **30 events** — waarvan 28 met branching-keuzes (RFP, ARB, buy-vs-build, hackathon, multi-cloud dilemma, …)

**15 Dragon1-artefacten** vormen de scoringskern:

| # | Artefact | Vereist |
|---|---|---|
| A001 | Vision Blueprint | — |
| A002 | Strategy Map | — |
| A003 | Capability Map | Strategy Map |
| A004 | Architecture Principles | — |
| A005 | Business Reference Model | Capability Map |
| A006 | Application Landscape | — |
| A007 | Information Model | — |
| A008 | Technology Blueprint | Application Landscape |
| A009 | Governance Framework | Architecture Principles |
| A010 | Transformation Roadmap | — |
| A011 | Portfolio Dashboard | Transformation Roadmap |
| A012 | Architecture Repository | Governance Framework |
| A013 | Enterprise Vision Poster | Vision Blueprint |
| A014 | Solution Overview | Application Landscape |
| A015 | Value Stream Map | — |

De **cascade-vereisten** dwingen speler in Dragon1-volgorde te werken.

## Eindspel: presentatie aan Raad van Bestuur

Speler beslist zelf wanneer hij "af" is en presenteert aan een virtuele Raad. Het spel genereert een **evaluatierapport op 8 aspecten**:

1. Samenhang (cascade-integriteit van artefacten)
2. Strategie-uitlijning
3. Businesswaarde
4. Innovatie
5. Governance
6. Security
7. Digitale volwassenheid
8. Stakeholdertevredenheid

Elk aspect krijgt een score 0-100 met letter-grade A-E, plus concrete verbeterpunten. Dit is direct bruikbaar als reflectie-instrument in een trainings-context — trainer kan het rapport gebruiken als debrief-basis.

## Wat het spel technisch is

- **Één HTML-bestand** (156 KB), speel offline door in browser te openen
- **Geen installatie, geen registratie, geen dataverzameling** buiten LocalStorage
- **Web Audio API** voor geluid (geen assets), autosave via LocalStorage
- **Responsive** desktop / tablet / mobiel
- **Open source (AGPL-3.0)** op https://github.com/cpaglebbeek/EnterpriseQuest
- **Content-schema** in JSON — nieuwe missies/uitdagingen/artefacten kunnen zonder code-werk toegevoegd worden

## Wat ik nu voorstel — samenwerking

Ik wil dit niet solo neerzetten. Dragon1 is jouw methode. Dat betekent:

1. **Jouw blessing als methode-eigenaar** — expliciete positionering "Dragon1-approved / officieel Dragon1-gamification-instrument"
2. **Gezamenlijke launch** — via Dragon1.com én icthorse.nl, met co-branding
3. **Train-de-trainer-traject** — instructeurs uit de Dragon1-community leren de simulatie te faciliteren (post-sessie debrief, aanvullende cases). Certificering + jaarlijkse hercertificering
4. **Model-opties** — kies wat past bij Dragon1:
   - **Optie A · Royalty-per-licentie:** Dragon1 krijgt 15-25% van SaaS-licentie-omzet (verkopen via icthorse.nl, jij ontvangt kwartaal-afrekening)
   - **Optie B · Co-branded certificering:** train-de-trainer trajecten 50/50 revenue-split
   - **Optie C · Whitelabel via Dragon1.com:** Dragon1 verkoopt, iCt Horse levert engine + content-updates. Revenue-share 60/40 Dragon1/iCt

## Waarom voor jou aantrekkelijk

- **Verbreding Dragon1-adoptie** naar studenten en juniors — instroom-versterking van je community
- **Modern gamification-format** — differentiator ten opzichte van klassikale trainingen en TOGAF-cursussen
- **Snelle time-to-market** — het spel is al gebouwd, LIVE, direct demo-baar
- **Passieve inkomstenstroom** via royalty of whitelabel-model
- **Positionering:** "Dragon1 is niet alleen methodiek, maar ook ervaring" — verhaal voor conferenties, boardroom-pitches
- **Toegang tot Nederlandse EA-opleidingsmarkt** die wij samen kunnen ontsluiten

## Wat ik van jou vraag

- **30 minuten demo-sessie** — ik toon het live, jij ervaart zelf de flow
- **Feedback op Dragon1-getrouwheid** — welke artefact-details / methodologische aanscherpingen moeten door voordat we "Dragon1-approved" mogen zeggen
- **Beslissing** — Optie A / B / C samenwerking, of eigen alternatief voorstel

## Financieel indicatief

Ruwe jaar-1 projectie (Nederlandse markt, zonder internationale schaal):
- 8-15 organisaties/consultancies als workshop-tool licentie: €40k-120k omzet
- Train-de-trainer-trajecten voor 5-10 instructeurs uit Dragon1-community: €35k-75k omzet
- Marge na jouw royalty/split: ~45% aan iCt-kant, ~25-35% aan Dragon1-kant

Sensitiviteit: eerste 3 betaalde klanten zijn de kritische horde — daarna is groei proces-gedreven.

## Praktisch

- **Test het nu:** https://icthorse.nl/EnterpriseQuest/v2/ (30 sec om Enterprise Architect te kiezen, 5 min voor een korte run + presentatie)
- **Code / open source:** https://github.com/cpaglebbeek/EnterpriseQuest
- **v1** (fantasy-editie, voor studenten/awareness) draait naast v2, kan onderdeel worden van gezamenlijke funnel: https://icthorse.nl/EnterpriseQuest/

## Volgende stap

Als je hier iets in ziet: laat me een **datum voor 30 min video-call** komende 2 weken. Dan doen we eerst 15 min live-play en 15 min zakelijk. Als je "misschien" denkt: speel het eerst zelf 15 minuten en laat me kort weten wat je vindt. Als het "nee" is: dan is dit signaal ook waardevol.

Ik ben overtuigd dat Dragon1 met dit format een substantiële adoption-boost kan krijgen, en dat wij samen sneller marktaandeel pakken dan afzonderlijk.

Groet,

**Christian Glebbeek**
iCt Horse — Connecting the dots
cglebbeek@gmail.com
https://icthorse.nl · https://github.com/cpaglebbeek

---

*Bijlage: de game zelf, LIVE op https://icthorse.nl/EnterpriseQuest/v2/EnterpriseQuest.html*
