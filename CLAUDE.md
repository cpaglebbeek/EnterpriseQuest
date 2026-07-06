# EnterpriseQuest — Project Context

**Ecosysteem:** iCt_Horse
**Repo type:** PUBLIC AGPL-3.0
**Codenaam-thema:** Enterprise Architecture pioniers (Zachman, Sowa, Spewak, Ross, Bernard, Lankhorst, ...)
**GitHub:** cpaglebbeek/EnterpriseQuest
**Deployment (gepland):** icthorse.nl/EnterpriseQuest/ op HC55

## Doel

Single-file HTML5 bordspel: Enterprise Architect moet organisatie redden van chaos.
Fantasy-RPG-flavor over TOGAF/cloud/security/data/AI-content.

## Constraints

- **Één** bestand: `EnterpriseQuest.html`
- Geen externe libs, frameworks, CDN, assets
- Werkt offline door dubbelklik in browser
- Web Audio API voor geluid (geen mp3/wav)
- LocalStorage voor save
- Responsive desktop/tablet/mobiel

## Architectuur

ES6 classes in inline `<script>`:
- `Game` — hoofdstate-machine, screens, event routing
- `Player` — class, HP, XP, level, attributes, inventory
- `Board` — 40 tiles over 12 regio's
- `CardDeck` — 250+ kaarten (quest/chaos/event/artifact)
- `Combat` — D20 mechanics, crits, special abilities
- `AudioEngine` — Web Audio API tones
- `SaveSystem` — LocalStorage autosave/load
- `UI` — rendering, animaties (dobbelsteen, kaarten, level-up)

Content laadt uit inline JS-arrays (initieel in `content/` en later inline).

## Versionering

v0.0.1-Zachman → v0.1.0-Sowa → v0.2.0-Spewak → v0.3.0-Ross → v1.0.0-Bernard

## Sessie-log

Zie `prompts/`.
