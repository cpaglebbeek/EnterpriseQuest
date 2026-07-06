---
resume: false
status: closed
sessie_date: 2026-07-07
project: EnterpriseQuest
version: v0.3.0-Turing
---

# 2026-07-07 — v3 Train Your Dragon + analoge PnP-series + 6 demo-videos + 2 analyses

## Triggers (chronologisch)

Meerdere user-prompts in dezelfde sessie:

1. "verderr met EA game" — sessie-start op EQ na v1/v2 sessie 2026-07-06
2. "werk van zowel de RPG als de D1 versie een analoge versie uit die gespeeld kan worden met een kaartspel en bord. .md en render pdf en mail. /loopuntilverified"
3. "maak opnieuw analyse uniciteit en vermarktbaarheid van analoge versie. .md. render pdf. mail. /loopuntilverified"
4. "werk landingspagina bij en stuur mij link voor alle nieuwe content; nieuwe variant: spel versie voor inzet van (Agentic) AI: train your dragon: versla (als een eindboss) de draak. De draak is AI drift en rogue agents. bewijs regie op determinisme en stochasme en governance op Data. Zie AI Governour bij Staffkennis van Gerben (governeur). werk variant digitaal en analoog uit. bereikbaar via landingpage. /loopuntilverified"
5. "feature: voeg een placeholder toe aan de landingspage: animatie van de nu 3 analoge spellen zodat je ziet hoe deze gespeeld worden. /loopuntilverified"
6. "deep dive analyse uniciteit en vermarktbaarheid hiervan maak md render pdf en mail /loopuntilverified"
7. "maak voor alle spellen, analoog en digitaal ook animatie/video met uitleg hoe het te spelen, met voorbeeld beurten (zie ook video's bij staff proces games)"
8. "ja maak"

## Opgeleverd

### Digitaal
- **v3/EnterpriseQuest.html** — v0.3.0-Turing single-file HTML5 (~43 KB)
  - 8 rollen: AI Governance Officer / ML Engineer / Data Architect / Security & Privacy Architect / Ethics Board Rep / MLOps Engineer / CTO / Prompt Engineer
  - 5×3 bord met 15 AI-landscape locaties (Data Warehouse → Drift Dragon)
  - **Gouverneur-modal** met 4 policy-vragen (Q1 zakelijke reden / Q2 data-scope / Q3 retentie-logging / Q4 AVG-AI Act-DORA)
  - Drift Dragon 3-fase eindboss (Hallucination Wraith / Tool-Abuse Serpent / Autonomous Dragon)
  - Rogue Agent tracker (3 skips in 5 beurten = rogue spawn, -3 Compliance/-3 Trust per beurt)
  - 5 Governance-artefacten met cascade (AI Policy → Model Registry / Data Contracts → Guardrails / Audit Trail)
  - 6 metrieken: Trust, Compliance, Determinisme, Data Sovereignty, Innovation, Drift
  - LocalStorage autosave, Web Audio tones
  - Codenaam-thema: AI-pioniers (Turing → Norvig → Hinton → LeCun → Ng → Karpathy → Bengio)

### Analoge Print & Play uitwerkingen
- **docs/analog_v1_rpg.md + PDF** — v1 fantasy-RPG (40 tiles, 250 kaarten, 22 monsters, 6 klassen, D20 combat, 2-6 spelers, 90-150 min)
- **docs/analog_v2_dragon1.md + PDF** — v2 Dragon1 (4×4 bord, 15 artefacten met cascade, 8 rollen, 12 metrieken, 8-aspect eindscore, 2-8 spelers, 90-120 min)
- **docs/analog_v3_ai.md + PDF** — v3 Train Your Dragon (5×3 bord, Gouverneur-plaat A4 karton met 4 draaischijven, 25+25+15+15+30 kaarten, 3-8 spelers, 90-120 min)

### Deep-dive analyses
- **docs/analyse_analoog.md + PDF** — uniciteit + vermarktbaarheid analoge versies (PoD kosten, Kickstarter-optie, workshop-tool licensing, corporate-gift)
- **docs/analyse_v3_ai.md + PDF** — uniciteit + vermarktbaarheid Train Your Dragon (EU AI Act timing na Digital Omnibus, NL AI-partner-opties, prijspunt-headroom EUR 10-50k enterprise SaaS/jaar, flagship-B2B-positionering)

### 6 demo-videos (60s elk, 1280×720 @ 30fps)
Via **tools/build_videos.py** — SVG-beats → cairosvg PNG → ffmpeg concat → MP4:
- videos/v1_digital_demo.mp4 (329 KB) — klasse-keuze, D20, kaart, combat, level-up
- videos/v1_analog_demo.mp4 (430 KB) — componenten, setup, beurt-flow, kaart-anatomie, combat
- videos/v2_digital_demo.mp4 (364 KB) — 8 rollen, 4×4 bord, mission M001, cascade, challenge, dashboard
- videos/v2_analog_demo.mp4 (524 KB) — componenten, setup dashboard+cascade, artefact opleveren, team-overleg, RvB 78/100
- videos/v3_digital_demo.mp4 (359 KB) — AI-rollen, 5×3 bord, opportunity+Gouverneur, threat drift, draak-encounter fase 1 verslagen
- videos/v3_analog_demo.mp4 (362 KB) — Gouverneur-plaat centraal, opportunity-overleg, 4 Q's op tafel (3/4→geweigerd), rogue spawn, RvB 68/100

### Landing page (index.html — volledig herbouwd)
- **3 digitale cards** met autoplay-video previews (muted, loop, playsinline)
- **3 analoge cards** met autoplay-video + controls
- **Docs-grid** met 5 tegels: deep dive digitaal + deep dive analoog + deep dive v3 + pitch Paauwe + pitch Peter

## Deploy — icthorse.nl (Hostinger)

Alle content live op `~/domains/icthorse.nl/public_html/EnterpriseQuest/`:
- `/` — landing (index.html)
- `/v1/EnterpriseQuest.html` (v0.0.1-Zachman)
- `/v2/EnterpriseQuest.html` (v0.2.0-Paauwe)
- `/v3/EnterpriseQuest.html` (v0.3.0-Turing)
- `/videos/{v1,v2,v3}_{digital,analog}_demo.mp4` (6 videos)
- `/docs/analog_v{1,2,3}_*.{md,pdf}` (3 PnP-docs)
- `/docs/analyse_{deepdive,analoog,v3_ai}.{md,pdf}` (3 analyses)
- `/docs/pitch_{mark_paauwe,peter_hulst}.{md,pdf}` (2 pitches uit vorige sessie)

Smoke-test: **11 URLs geven HTTP 200** (getest per LUV-run).

## /loopuntilverified × 4

1. **analog_v1+v2 PnP** — 3 iteraties, fixed point, 35 feiten, 100% verifieerbaar (0 correcties). Werkmap `~/.claude/loopuntilverified/20260706T221150Z/`, mail `19f3982c5d166f28`.
2. **analyse_analoog** — 3 iteraties, fixed point, 42 feiten, 100% verifieerbaar, **2 correcties**: Beer Distribution Game MIT 1961→1960 (Jay Forrester); Cthulhu Confidential niet business-humor maar noir-RPG (vervangen door Bureaucracy Avalon Hill 1981). Werkmap `~/.claude/loopuntilverified/20260706T222523Z/`, mail `19f398f005cb4d04`.
3. **v3 digitaal + analoog + landing** — 3 iteraties, fixed point, 38 feiten, 100% verifieerbaar (0 correcties). Cross-consistency v3 digital↔analog: 12/12 match. Externe: EU AI Act art 6+Annex III, MLflow. Werkmap `~/.claude/loopuntilverified/20260706T224943Z/`, mail `19f39a4bdcdf74b2`.
4. **analyse_v3_ai** — 3 iteraties, fixed point, 32 feiten, 100% verifieerbaar, **2 correcties**: EU AI Act Annex III deadline augustus 2026 → **december 2027** (Digital Omnibus, Council 29 juni 2026 — 16 mnd uitstel); Annex I augustus 2027 → augustus 2028. Marketing-argument omgezet: het uitstel = kans voor iCt Horse (Big-4 schuift ook op). Werkmap `~/.claude/loopuntilverified/20260706T230521Z/`, mail `19f39b257a491b73`.

## Kern-innovaties v3

### Gouverneur-mechaniek
Geïnspireerd door **StaffKennisGerben procesarchitect Data Governance tab** (Verzoeker → Gouverneur → Data flow, prompt 2026-06-12_fase2-5_capacity_datagov_bugfix.md).

Digitaal: modal met 4 checkboxes. Analoog: fysieke A4-plaat met 4 draaischijven, team-consensus vereist.

4 policy-vragen:
- Q1 — Geldige zakelijke reden?
- Q2 — Data-categorie toegestaan voor rol/scope?
- Q3 — Geldig retentie- en logging-plan?
- Q4 — Voldoet extern (AVG/AI Act/DORA) én intern (data-classificatie)?

4/4 bevestigd → toegang + Compliance/Data +3. Skip → +5 drift + 1 in rogue-teller.

### Rogue Agent-mechaniek
3 skips in 5-beurten-venster → Rogue Agent-token op willekeurige locatie. Elke rogue: -3 Compliance, -3 Trust per beurt. Verwijderen: 1 beurt zelfde locatie + Governance-kaart spelen.

### Drift Dragon 3-fase
- Fase 1: **Hallucination Wraith** (drift ≥ 30, HP 100, -2 Trust/beurt)
- Fase 2: **Tool-Abuse Serpent** (drift ≥ 60, HP 150, -3 Compliance/beurt)
- Fase 3: **Autonomous Dragon** (drift = 100 = game-over trigger, HP 200)

Verslagen vereist per fase: team-readiness (Trust+Compliance+Determinisme+Data) ≥ threshold én N+1 artefacten gebouwd.

## Video-generatie-patroon

Overgenomen van **StaffKennisGerben/processgame/tools/build_video.py**:

```python
# SVG-beats renderen naar PNG
cairosvg.svg2png(bytestring=svg.encode("utf-8"),
                 output_width=1280, output_height=720,
                 write_to=str(png_path))

# ffmpeg concat naar MP4
ffmpeg -f concat -safe 0 -i concat.txt \
       -c:v libx264 -pix_fmt yuv420p -r 30 \
       -vf scale=1280:720 output.mp4
```

Per video: 7-8 beats × 60s = ~7-8s per beat. Concat.txt met `duration` en herhaalde laatste file voor ffmpeg-concat-vereiste.

Total render-tijd: ~30 sec voor alle 6 videos. Bestandsgrootte: 329-524 KB per video.

## Openstaand voor volgende sessie

- **Playtest v3** (digitaal én analoog) — Gouverneur-flow-lengte testen (>3 min = te lang?)
- **Facilitator-gids v1+v2+v3** — €5-15k budget per gids, workshop-debrief materiaal
- **EU AI Act artikel-mapping per opportunity/threat-kaart** — juridische review €3-5k voor audit-defensibiliteit
- **Partner-outreach** — AI Impact Alliance / NL AI Coalitie / TNO AI Governance Lab / CISO Platform NL / VNG
- **Server-side backend v3** — multi-user scoreboards + SSO + trainer-analytics (€20-40k dev) voor enterprise-SaaS
- **EN-editie v3** — voor internationale schaal (€8-15k vertaling + juridische review op AI Act EN)
- **Kickstarter v1 fantasy** — als PoD-sales positieve signalen geven
- **Antwoord Mark Paauwe / Peter v/d Hulst** — afwachten (uit vorige sessie)

## Bestandsstructuur na sessie

```
EnterpriseQuest/
├── index.html                        # landing (nieuw)
├── v1/EnterpriseQuest.html           # LIVE
├── v2/EnterpriseQuest.html           # LIVE
├── v3/EnterpriseQuest.html           # NIEUW LIVE (v0.3.0-Turing)
├── content/                          # v1 content JSONs
├── v2/content/                       # v2 content JSONs
├── docs/
│   ├── analog_v1_rpg.{md,pdf,html}   # NIEUW
│   ├── analog_v2_dragon1.{md,pdf,html} # NIEUW
│   ├── analog_v3_ai.{md,pdf,html}    # NIEUW
│   ├── analyse_deepdive.{md,pdf,html} # (bestaand)
│   ├── analyse_analoog.{md,pdf,html} # NIEUW
│   ├── analyse_v3_ai.{md,pdf,html}   # NIEUW
│   ├── pitch_mark_paauwe.{md,pdf,html} # (bestaand)
│   └── pitch_peter_hulst.{md,pdf,html}  # (bestaand)
├── videos/                           # NIEUW dir
│   ├── v1_digital_demo.mp4
│   ├── v1_analog_demo.mp4
│   ├── v2_digital_demo.mp4
│   ├── v2_analog_demo.mp4
│   ├── v3_digital_demo.mp4
│   └── v3_analog_demo.mp4
├── tools/                            # NIEUW dir
│   └── build_videos.py
├── prompts/
│   ├── 2026-07-06_bootstrap.md
│   ├── 2026-07-06_v2_deploy_analyse.md
│   └── 2026-07-07_v3_analog_analyse_videos.md  # DEZE
└── LICENSE, README.md, CLAUDE.md
```

## Commits deze sessie

- `fb8ee30` — v3 Train Your Dragon + landing + analog PnP docs (v1+v2+v3)
- `5476cff` — 6 demo-videos + v3 deep-dive analyse + landing update met echte MP4-embeds

Push naar `cpaglebbeek/EnterpriseQuest` main. AGPL-3.0 PUBLIC.

## Mails deze sessie (7 stuks)

- `19f397b1fbb95ef4` — analog v1+v2 docs + PDFs
- `19f3982c5d166f28` — LUV rapport analog v1+v2
- `19f39881ec59d804` — deep-dive analyse analoog docs + PDF
- `19f398f005cb4d04` — LUV rapport analyse_analoog (2 correcties)
- `19f39a4bdcdf74b2` — v3 LIVE (digitaal + analoog + landing) met LUV-verificatie
- `19f39b257a491b73` — v3 deep-dive analyse + LUV (2 correcties EU AI Act deadlines)
- `19f39c19038a0296` — 6 demo-videos LIVE + landing update
