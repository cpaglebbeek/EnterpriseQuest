---
resume: false
status: closed
sessie_date: 2026-07-06
project: EnterpriseQuest
version: v0.2.0-Paauwe
---

# 2026-07-06 — v2 Dragon1 + deploy + analyse-suite

## Trigger

3 user-prompts in dezelfde sessie:
1. "maak versie /v2 zie hiervoor gmail van joyce kaag. Dragon1 methodiek als basis. /loopuntilverified"
2. "plaats versie 1.0 en 2.0 beide op icthorse.nl/EnterpriseQuest/v1 en /v2"
3. "voor beide versies: deep dive analyse: hoe uniek en vermarktbaar is dit. Samen met Mark Paauwe verkopen als idee, gaem en train de tainer. en//of met Peter v/d Hulst van Staff. vergelijk met Proces game van Staff en kijk of er overlap is, beter 1 spel of 2 of 3 of 4 of per soort orgnisateie .maak managemnet aalyse en ptich. apart voor mark en peter. die weten niet van elkaar. .md render pdf en mail"

## Bron-mail v2

Joyce Kaag-Glebbeek — "Enterprise Architect Quest" (2026-07-06 22:58, messageId `19f39397dfa6edb1`) met ChatGPT share-link `https://chatgpt.com/s/t_6a4c164bc3fc8191a412b3aad27554d3`. Volledige spec gefetcht via headless Chrome (JSDOM/WebFetch krijgt alleen login-UI; Puppeteer wél).

Kern-verschil t.o.v. v1: **Dragon1 centraal**, geen fantasy, GEEN combat/HP/monsters, winnen door **toekomstbestendige organisatie realiseren** en aan RvB presenteren.

## Beslissingen

- Locatie: `v2/`-subfolder naast v1 (niet in-place patch — fundamenteel ander spel)
- Codenaam: **Paauwe** (Mark Paauwe = Dragon1-grondlegger)
- Deploy: naast v1 op icthorse.nl (Hostinger, NIET HC55 — icthorse.nl draait op Hostinger)
- Launcher `index.html` op `/EnterpriseQuest/` biedt keuze v1/v2

## Wat gemaakt is (v2)

- `v2/EnterpriseQuest.html` — 156 KB single-file
- 8 rollen (EA/SA/BA/IA/SecA/CIO/IT-Mgr/Student EA)
- 4×4 bord met 16 organisatie-onderdelen
- 40 missies + 40 uitdagingen (3-4 keuzes elk) + 30 events (28 met branching)
- 15 Dragon1-artefacten (12 verplichte + 3 extra) met cascade-vereisten
- 47 achievements (da01-da47)
- 12 dashboard-metrieken
- 8-aspect eindscore + verbeterpunten in RvB-presentatie
- Web Audio API + LocalStorage + responsive
- 3 content-agents parallel + main-context engine + build.py merger

## Deploy

- `~/domains/icthorse.nl/public_html/EnterpriseQuest/{v1,v2}/` op Hostinger
- Launcher `index.html` op `/EnterpriseQuest/`
- Alle 3 URLs HTTP/2 200 gecheckt

## Analyse-suite

- `docs/analyse_deepdive.md/pdf` — intern: uniekheid + vermarktbaarheid + 1-vs-N spellen + partner-strategie
- `docs/pitch_mark_paauwe.md/pdf` — Dragon1-framing (royalty/whitelabel/train-de-trainer)
- `docs/pitch_peter_hulst.md/pdf` — procesarchitectuur-framing voor Staff-portfolio
- Beide pitches strikt gescheiden, geen kruisreferenties
- "Staff Proces-game" niet publiek vindbaar → analyse op basis van De Processpecialisten + Passionned; pitch vraagt Peter zelf om aanvulling

## /loopuntilverified v2

- 22/22 feiten = **100% verifieerbaar**, fixed point op iteratie 2
- Werkmap: `~/.claude/loopuntilverified/20260706T212403Z/`
- Rapport + PDF verzonden naar cglebbeek@gmail.com

## Mails verzonden

- v1 verificatie (msg `19f393a4`)
- Analyse-suite met 3 PDF's + 3 MD's (msg `19f3950d`)
- v2 verificatie (msg `19f3953b`)

## Openstaand

- LICENSE-header naar kale AGPL-3.0 boilerplate voor GitHub-classifier
- Facilitator-gids v1 én v2 (workshop-debrief materiaal, ~€5-10k budget)
- Server-side scoreboard / SSO / trainer-analytics (fase 2)
- Antwoord Mark Paauwe / Peter v/d Hulst afwachten
