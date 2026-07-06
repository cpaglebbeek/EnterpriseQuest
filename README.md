# Enterprise Quest: Architect's Dungeon

Standalone HTML5 bordspel: een Enterprise Architect moet een organisatie redden van chaos.
Combineert TOGAF-principes, cloud, security, data en AI-strategie met tabletop-RPG-sfeer.

**Ecosysteem:** iCt_Horse — showcase EA-capaciteiten
**Codenaam-thema:** Enterprise Architecture pioniers
**Huidige versie:** v0.0.1-Zachman
**Licentie:** AGPL-3.0

## Spelen

Open `EnterpriseQuest.html` in een moderne browser. Geen build, geen server, geen dependencies.

- Kies één van 6 architect-klassen (Enterprise / Solution / Business / Security / Data / DevOps)
- Rol de D20 om over 40 vakken door 12 regio's te reizen
- Vecht monsters (Legacy Dragon, Technical Debt Golem, ...) tot The Chaos Architect
- Verzamel artifacts (TOGAF Scroll, API Sword, Cloud Crystal, ...)
- Level 1 Junior → 10 Legendary Architect
- Save/load via LocalStorage, autosave, achievements, tutorial

## Kaarten

- 100 Quest-kaarten (cloud-migratie, Zero Trust, target architecture, ADM, capability maps, ...)
- 50 Chaos-kaarten (ransomware, budget-freeze, NIS2, vendor faillissement, ...)
- 50 Artifact-kaarten (weapons, armor, scrolls, crowns, crystals)
- 50 Event-kaarten (met branching keuzes)

## Regio's

Business Village · Legacy Dungeon · Cloud Mountains · Security Castle · Data Forest
Innovation Tower · AI Temple · Executive Palace · Integration Bridge · Compliance Swamp
Vendor Market · Digital Portal

## Tech

- Single HTML-bestand — HTML + CSS + vanilla JS (ES6 classes)
- Web Audio API voor geluid (geen externe assets)
- LocalStorage voor save-state
- Responsive: desktop / tablet / mobiel

## Ontwikkelnotes

Zie `prompts/` voor sessie-verslag en `CLAUDE.md` voor project-context.
