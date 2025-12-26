# Prompt Enrichment Process

How to gather Densworld-specific material before writing image prompts.

---

## The Problem

Generic prompts produce generic images:
- "A clay jug" → any jug
- "Pilgrim's sandals" → catalog display
- "A field with objects" → arranged still life, not a scene

What we need:
- "The cracked offering bowl from the Collapsed Chapel, still holding ash from Quonxy's last visit"
- "Novice Tommel Gren's discipline board, left behind when he fled the Trial Field"
- "A scene of arrival, interruption, departure — not arrangement"

---

## Before Writing Each Prompt

### Step 1: Check Region Sources

For the selected region, gather:

**From `densworld_places.csv`:**
- Specific sub-locations (not just "Northo" but "Trial Field of Northo," "House of Stones," "Collapsed Chapel")
- Risk levels (physical and symbolic) — affects mood
- Boundary status — liminal spaces are more interesting

**From `creatures.csv`:**
- What creatures inhabit this region?
- What traces do they leave?
- Can one appear in the image?

**From `WORLD_NOTES.md`:**
- What patterns or phenomena affect this region?
- Center/margins dynamic? Oscillating dimensions? Institutional presence?

### Step 2: Find a Narrative Anchor

Every image needs a **moment**, not an arrangement. Ask:

- Who was just here?
- What were they doing?
- Why did they leave?
- What evidence remains?

**Good anchors:**
- A novice fled mid-trial, leaving belongings
- A ferryman abandoned his post at the sound from the bridge
- An archivist fell asleep at their desk, candle burning down
- A Gritsmuck Crawler picked through debris left by a departing expedition

**Bad anchors:**
- Objects arranged for viewing
- A "scene" with no implied before/after
- Generic location with generic objects

### Step 3: Source Specific Objects

For each of the 6 loci, ask:

1. **Who does this belong to?** (named character, institution, creature)
2. **What happened to it?** (worn, broken, abandoned, half-used)
3. **What makes it Densworld-specific?** (three-direction compass, Guild seal, yeller-stained cloth)

**Object specificity ladder:**
| Level | Example | Quality |
|-------|---------|---------|
| Generic | "a lantern" | Bad |
| Typed | "a tin lantern" | Acceptable |
| Sourced | "a ferryman's lantern, soot-stained" | Good |
| Narrative | "the ferryman's lantern, still lit though he fled an hour ago" | Best |

### Step 4: Add One Densworld Signature

Each image should have at least ONE element that could only exist in Densworld:

- A creature (Gritsmuck Crawler, Metal-Beaked Finch, Tunnel Cat)
- A named location visible (Broken Deadriver Bridge, Tower of Mirado)
- An institutional artifact (Guild cartographer's burned report, Bureau form 112-R)
- A world-physics detail (compass with three directions, oscillating-year calendar)

---

## Source Files to Check

| Source | Location | Use |
|--------|----------|-----|
| Places | `_source/all-data-sets/densworld_places.csv` | Sub-locations, risk levels |
| Creatures | `_source/all-data-sets/creatures.csv` | Regional fauna |
| World Notes | `_source/WORLD_NOTES.md` | Patterns, phenomena |
| Scholars | `_planning/encyclopedia/people.md` | Named characters |
| Living Ledger | `_source/living-ledger/EVENT_LOG.jsonl` | Historical events |
| Ore Fragments | `_source/ore-fragments/` | Narrative texture |

---

## Example: Northo (Corrected)

**Bad prompt:** "Trial Field of Northo with discipline board, jug, sandals, cairn, gatehouse, post"

**Enriched approach:**

1. **Region sources:**
   - Trial Field: risk 4 physical, 8 symbolic, boundary location
   - House of Stones: stone rituals after difficult talks
   - Collapsed Chapel: "badly remembered saint story site"
   - No creatures native to Northo in CSV — but pilgrims bring things

2. **Narrative anchor:**
   - A novice named Carten (from Iterative Cartography ore) was sent to Northo for "re-education" after his heterodox mapping work
   - He's been standing at the obedience post since dawn
   - The scene is his view: what he sees while waiting

3. **Specific objects:**
   - His surveyor's satchel (confiscated, lying in the dirt)
   - A stone from the Collapsed Chapel (placed as offering by previous penitent)
   - The water jug that won't be brought to him until he demonstrates submission
   - Frost on the grass (Northo is cold, austere)
   - The House of Stones' blocked door (he can't enter until approved)

4. **Densworld signature:**
   - The discipline board has a Guild of Cartographers seal — burned into the wood as punishment

**Revised prompt:**

"A unified exterior illustration of the Trial Field of Northo at dawn, viewed from the obedience post looking across the frozen field toward the House of Stones. The scene is what a waiting novice sees.

In the foreground on the left, a confiscated surveyor's satchel lies in the frost, its brass buckle stamped with the Guild of Cartographers seal. In the center foreground, a chipped stone from the Collapsed Chapel sits on the boundary marker, left by some previous penitent. To the right foreground, the discipline board leans against a frost-covered rock, its surface branded with a cartographer's compass showing only three directions.

In the middle distance on the right, a stone cairn marks where the trial zones divide, lichened and ancient. At center back, the House of Stones rises—its door blocked by a massive boulder that will not be rolled away until the novice's submission is accepted. On the left in the background, the iron ring of the obedience post catches cold light, its rope frayed from use.

No monks are visible. The field is silent. The novice has been waiting since before dawn."

---

## Checklist Before Writing Prompt

- [ ] Checked `densworld_places.csv` for specific sub-location
- [ ] Checked `creatures.csv` for regional fauna
- [ ] Checked `WORLD_NOTES.md` for relevant patterns
- [ ] Identified narrative anchor (who, what happened, why)
- [ ] Each object has a source or story
- [ ] At least one Densworld-specific signature element
- [ ] Prompt describes a moment, not an arrangement

---

*Created: 2025-12-26*
