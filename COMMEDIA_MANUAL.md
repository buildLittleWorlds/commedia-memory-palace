# Commedia Memorization Manual

**A working guide for memorizing Dante's Divine Comedy through Densworld imagery**

---

## The Project

Memorize 14,233 lines of Italian poetry using AI-generated Densworld images as memory palaces.

| Metric | Value |
|--------|-------|
| Daily target | 6 lines (2 tercets) |
| Lines per image | 6 |
| Objects per image | 6 (one per line) |
| Total images needed | ~2,372 |
| Timeline | ~13 months |

---

## Core Principles

### 1. The Arbitrariness Principle

**The mapping between Dante's text and Densworld locations is arbitrary.**

Do NOT choose locations or objects based on what's happening in Dante. The "dark wood" does not go to the Dens. The celestial spheres do not go to the Tower.

**Why this matters:** If the mnemonic scaffold "made sense," you'd be tempted to reconstruct through reasoning instead of through the image. Reasoning is slow and error-prone. The arbitrary image, once learned, is simply *there*—immediate, stable, independent of interpretation.

**When selecting sources, use stochastic selection** from SOURCE_AUDIT_LOG.json rather than deliberate thematic matching.

### 2. The W1/W2 Framework

W2 (our world) creates W1 (Densworld) as a mnemonic system. As you use W1 for memory, W1 shapes you back. The Commedia will come to be understood *through* Densworld structures.

Each generated image is a **build-stone**—a physical-visual anchor for both the imaginary world and the memorized text simultaneously.

### 3. Stochastic Resonance

Resonances between Dante and Densworld will emerge—but not by design. Document these in a separate journal (the W2 memorizer's voice), not in the tracking JSON. This becomes narrative material.

---

## Daily Workflow

### Step 1: Select the Lines

Get the next 6 lines (2 tercets) from where you left off.

### Step 2: Select Source Stochastically

**Use SOURCE_AUDIT_LOG.json for prompt inspiration.**

1. Filter for rating 3-5 sources (rich visual content)
2. Randomly select from available sources
3. Read the source file for narrative texture
4. Extract a vivid moment with visual potential

This replaces manual region selection and ensures variety.

### Step 3: Determine Region and Atmosphere

Based on the selected source:
- Identify the region (Capital, Dens, Quarry, etc.)
- Determine atmospheric color (see PRODUCTION_TEMPLATE.md)
- Note time of day and weather for the scene

### Step 4: Select 6 Objects

Each line gets one object. The image generator will arrange them naturally—you'll identify the arrangement after generation.

**Check `object_registry` in the JSON** to avoid reusing objects. Categorize new objects:
- containers
- equipment
- fire
- military
- furniture
- nature
- documents
- creatures
- food/drink
- tools

**Spacing principle:** Don't cluster similar objects. If position 1 has a container, position 2 should be something else.

### Step 5: Write the Prompt

**Use natural language, not JSON.** See PRODUCTION_TEMPLATE.md for the full formula.

Basic structure:
```
Densworld field sketch: [LOCATION AND TIME]. [ATMOSPHERIC COLOR] watercolor
wash dominates the [sky/walls/space], with ink line work defining forms.

[SCENE DESCRIPTION — weave objects into the narrative naturally]

[BACKGROUND ELEMENTS — rendered softer, part of atmosphere]

No text, no caption, no border, no signature.
```

**Do NOT request:**
- Numbered loci (model gets these wrong)
- Grid layouts or panels
- "Zoomed details" or "close-up" sections (causes segmented images)
- Compass showing East (Densworld has no East)

### Step 6: Generate the Image

Use **Gemini (Nano Banana Pro)** with Thinking enabled.

### Step 7: Identify the Arrangement

After generation, count foreground and background objects:

- **A (3+3):** 3 foreground, 3 background — classic zigzag
- **B (4+2):** 4 foreground, 2 background — foreground-heavy
- **C (2+4):** 2 foreground, 4 background — background-heavy

See LOCUS_PLACEMENT_GUIDE.md for the path through each arrangement.

### Step 8: Assign Loci

Follow the path for the identified arrangement. Each locus must be:
- **One element only** (passes the finger test)
- **Spatially separated** from adjacent loci
- **Visually distinct** from other objects in the image

### Step 9: Create the HTML Page

Create folder: `inferno{canto}-{image}/`

HTML structure:
- Header with canto/lines
- Image centered (max-width 900px)
- First tercet below image (foreground loci)
- Second tercet to right of image (background loci)

Each line uses `<details>/<summary>` for **quiz mode**:
- Locus label visible by default (clickable)
- Italian + English text hidden until clicked
- Visual indicators: ▶ collapsed, ▼ expanded

```html
<details>
    <summary>satchel with rolled maps</summary>
    <div class="text-content">
        <span class="italian">Nel mezzo del cammin di nostra vita</span>
        <span class="english">Midway upon the journey of our life</span>
    </div>
</details>
```

**Quiz workflow:** Look at image → recall line for each locus → click to verify.

### Step 10: Update the JSON

Add new entry to `COMMEDIA_MAPPINGS.json`:
- Increment `sequence`
- Update `adjacent` links (previous image's `next`, new image's `previous`)
- Add objects to `object_registry` by category
- Add image ID to `region_usage`
- Note the source from SOURCE_AUDIT_LOG.json

### Step 11: Memorize

Use the image. Walk through the loci. Attach the lines.

### Step 12: Record Recall Feedback (Later)

After using the image for a few days:
- `recall.difficulty`: 1-5 scale
- `recall.problem_loci`: which positions caused confusion
- `recall.notes`: what worked, what didn't

---

## Color Palette Reference

From `visual_materials_catalog.csv`:

| Material | Hex | Use |
|----------|-----|-----|
| Densmuck Black | #1A1A1A | Boundaries, voids |
| Quarry Ochre | #B45309 | Warm earth tones |
| Iron Gall Black | #1F2937 | Archive ink, formal |
| Tower Steel Gray | #9CA3AF | Tower, metal |
| Fountain Blue | #60A5FA | Tower crown, water |
| Knocker-bug Gold | #CA8A04 | Gilding, accents |
| Clod-mud Earth | #A16207 | Camp structures, dried earth |
| Desert Maize Yellow | #FCD34D | Desert scenes, food |
| Dead River Silt Gray | #78716C | River, passage |
| Grimslew Scale Black | #030712 | Deepest black |

---

## Failure Modes to Avoid

| Problem | Solution |
|---------|----------|
| Grid of panels | Emphasize "ONE continuous scene" |
| Objects too similar | Check categories, vary types |
| Objects clustered | Specify placements explicitly |
| Compass shows East | Mention "three directions" or omit |
| Numbered loci wrong | Don't request numbers |
| Region repetition | Use stochastic source selection |
| Object repetition | Check `object_registry` before selecting |
| Segmented images | Don't use "zoomed details" or "close-up" sections |

---

## File Structure

```
_commedia-mnemonics/
├── COMMEDIA_MANUAL.md          ← This file
├── COMMEDIA_PROJECT.md         ← Project overview and principles
├── COMMEDIA_MAPPINGS.json      ← Tracking data (images, objects, regions)
├── PRODUCTION_TEMPLATE.md      ← Prompt formula and examples
├── LOCUS_PLACEMENT_GUIDE.md    ← Flexible arrangements (A/B/C)
├── SOURCE_AUDIT_LOG.json       ← Stochastic source selection (1,968 rated files)
├── EXPERIMENT_LOG.md           ← Image generation experiments
├── _prompt-sources/
│   └── PROMPT_ENRICHMENT_PROCESS.md  ← How to enrich prompts with lore
├── _source-texts/
│   ├── inferno_italian.txt     ← Clean Italian (4,721 lines, by canto)
│   ├── inferno_longfellow.txt  ← Longfellow translation (4,721 lines)
│   └── extract_inferno.py      ← Extraction script
├── inferno1-1/
│   ├── images/lines-1-6.png
│   └── lines-1-6.html
├── inferno1-2/
│   ├── images/lines-7-12.png
│   └── lines-7-12.html
└── ...
```

---

## Instructions for Claude

When helping with this project:

1. **Use SOURCE_AUDIT_LOG.json** for stochastic source selection—filter for rating 3-5
2. **Write natural language prompts**, not JSON—see PRODUCTION_TEMPLATE.md
3. **Don't number loci** in prompts—the model gets these wrong
4. **Don't match Dante to Densworld thematically**—the mapping is arbitrary
5. **Identify arrangement after generation** (A: 3+3, B: 4+2, C: 2+4)—see LOCUS_PLACEMENT_GUIDE.md
6. **Each locus is ONE element**—passes the finger test
7. **Track everything** in `COMMEDIA_MAPPINGS.json` after each image
8. **Create HTML pages** with the established layout (image centered, tercet 1 below, tercet 2 right)
9. **Categorize objects** when adding to the registry
10. **Update adjacent links** when adding new images
11. **Leave resonance observations** for the W2 journal—don't put them in the JSON

---

## The W2 Journal

Separate from this system, maintain a journal documenting:
- Unexpected resonances between Dante and Densworld
- How images shape understanding of the text
- The experience of thinking *through* W1
- Stochastic meanings that emerge

This is narrative material, not tracking data. It becomes part of the world.

---

## Quick Reference

**To add a new image:**
1. Get next 6 lines
2. Select source stochastically from SOURCE_AUDIT_LOG.json (rating 4-5)
3. Read source file, extract vivid moment
4. Write natural language prompt (see PRODUCTION_TEMPLATE.md)
5. Generate in Gemini (Nano Banana Pro)
6. Identify arrangement (A/B/C) after generation
7. Assign loci following the path (see LOCUS_PLACEMENT_GUIDE.md)
8. Create folder + HTML page
9. Update JSON (new image entry, object registry, region usage, adjacent links)

**JSON location:** `COMMEDIA_MAPPINGS.json`

**Image ID format:** `inf-{canto}-{sequence}` (e.g., `inf-1-001`, `inf-1-002`)

**Folder format:** `inferno{canto}-{image}` (e.g., `inferno1-1`, `inferno1-2`)

---

*Last updated: 2025-12-28*

---

## Changelog

- **2025-12-28:** Integrated SOURCE_AUDIT_LOG.json for stochastic source selection; updated to use PRODUCTION_TEMPLATE.md and flexible arrangements (A/B/C); replaced JSON prompts with natural language
- **2025-12-26:** Added quiz mode (details/summary) to all HTML pages; added Longfellow translations; extracted source texts to `_source-texts/`; documented LOCUS_PLACEMENT_GUIDE.md and PROMPT_ENRICHMENT_PROCESS.md
