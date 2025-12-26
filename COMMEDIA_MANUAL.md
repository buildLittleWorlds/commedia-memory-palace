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

**When selecting locations, choose based on:**
- Variety (haven't used this region recently)
- Visual interest (rich in potential objects)
- Avoiding repetition (check `region_usage` in the JSON)

### 2. The W1/W2 Framework

W2 (our world) creates W1 (Densworld) as a mnemonic system. As you use W1 for memory, W1 shapes you back. The Commedia will come to be understood *through* Densworld structures.

Each generated image is a **build-stone**—a physical-visual anchor for both the imaginary world and the memorized text simultaneously.

### 3. Stochastic Resonance

Resonances between Dante and Densworld will emerge—but not by design. Document these in a separate journal (the W2 memorizer's voice), not in the tracking JSON. This becomes narrative material.

---

## Daily Workflow

### Step 1: Select the Lines

Get the next 6 lines (2 tercets) from where you left off.

### Step 2: Choose a Region

Check `COMMEDIA_MAPPINGS.json` → `region_usage` to see what's been used recently. Pick something different.

**Available regions (37 total):**

| Primary Regions | Character |
|-----------------|-----------|
| Capital | Institutional, bureaucratic |
| The Dens | Primordial, unstable |
| Tower of Mirado | Silver architecture, siege history |
| Yeller Quarry | Industrial, dangerous |
| Densmok | High instability |
| Northtown/Northo | Austere, religious |
| Capeast | Eastern expansion, grimslew territory |
| Dead River | Underground connections |
| Mirado Sticks | "Rehab town," country club |
| Mirado Desert | Post-linguistic, surrounding Tower |

Plus 12+ sub-regions, 8 specialized anomalies, and W2 locations.

### Step 3: Choose a Sub-location

Be specific. Not just "Capital" but "Archive reading room" or "Senate gallery balcony."

### Step 4: Choose Time/Weather

Vary these for distinctiveness:
- **Time:** dawn, midday, dusk, night
- **Weather:** clear, overcast, storm

### Step 5: Select 6 Objects

Each line gets one object. Distribute them spatially:
- 3 in foreground (left, center, right)
- 3 in background (right, center, left)

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

### Step 6: Write the Prompt

Use natural language, not JSON. Describe the scene as if standing in a doorway looking in.

**Template:**
```
A unified interior/exterior illustration of [location], viewed as if standing in [vantage point] looking [direction].

In the foreground on the left, [object 1 with detail]. Beside it in the center foreground, [object 2 with detail]. To the right foreground, [object 3 with detail].

In the middle distance/background, [object 4] on the right side. At center back, [object 5]. On the left in the background, [object 6].

[Optional: distant landmark or atmospheric detail]

The color palette draws from Densworld materials: [2-4 colors from visual_materials_catalog.csv with hex codes].

Cartographic illustration style with clean lines, unified lighting from top-left, deep focus keeping all elements sharp. Aspect ratio 16:9. One continuous scene, not separate panels. Six distinct objects clearly separated by negative space.
```

**Do NOT request:**
- Numbered loci (Nano Banana gets these wrong)
- Grid layouts or panels
- Compass showing East (Densworld has no East)

### Step 7: Generate the Image

Use Nano Banana Pro (Gemini 3 Pro Image with Thinking enabled).

### Step 8: Evaluate

Check:
- All 6 objects visible and distinct?
- Objects well-separated spatially?
- Unified scene (not panels)?
- Densworld visual vocabulary present?

If problems, regenerate or note in `recall.problem_loci`.

### Step 9: Create the HTML Page

Create folder: `_mnemonic-system/inferno{canto}-{image}/`

HTML structure:
- Header with canto/lines
- Image centered (max-width 900px)
- First tercet below image (left-justified, centered as block)
- Second tercet to right of image

Each line formatted as:
```
[Italian line] :: [object description]
```

### Step 10: Update the JSON

Add new entry to `COMMEDIA_MAPPINGS.json`:
- Increment `sequence`
- Update `adjacent` links (previous image's `next`, new image's `previous`)
- Add objects to `object_registry` by category
- Add image ID to `region_usage`

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
| Region repetition | Check `region_usage` before selecting |
| Object repetition | Check `object_registry` before selecting |

---

## File Structure

```
_mnemonic-system/
├── COMMEDIA_MANUAL.md          ← This file
├── COMMEDIA_PROJECT.md         ← Project overview and principles
├── COMMEDIA_MAPPINGS.json      ← Tracking data (images, objects, regions)
├── W1_W2_REFRAME.md            ← W1/W2 framework documentation
├── ART_OF_MEMORY_SUMMARY.md    ← Memory palace techniques
├── EXPERIMENT_LOG.md           ← Image generation experiments
├── inferno1-1/
│   ├── lines-1-6.png
│   └── lines-1-6.html
├── inferno1-2/
│   ├── lines-7-12.png
│   └── lines-7-12.html
└── ...
```

---

## Instructions for Claude

When helping with this project:

1. **Check the JSON first** before suggesting regions or objects—avoid repetition
2. **Write natural language prompts**, not JSON—Nano Banana handles these better
3. **Don't number loci** in prompts—the model gets these wrong
4. **Don't match Dante to Densworld thematically**—the mapping is arbitrary
5. **Track everything** in `COMMEDIA_MAPPINGS.json` after each image
6. **Create HTML pages** with the established layout (image centered, tercet 1 below, tercet 2 right)
7. **Categorize objects** when adding to the registry
8. **Update adjacent links** when adding new images
9. **Leave resonance observations** for the W2 journal—don't put them in the JSON

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
2. Check `region_usage` → pick unused/underused region
3. Check `object_registry` → pick 6 new objects (varied categories)
4. Write natural language prompt (no JSON, no numbers)
5. Generate in Nano Banana Pro
6. Create folder + HTML page
7. Update JSON (new image entry, object registry, region usage, adjacent links)

**JSON location:** `_mnemonic-system/COMMEDIA_MAPPINGS.json`

**Image ID format:** `inf-{canto}-{sequence}` (e.g., `inf-1-001`, `inf-1-002`)

**Folder format:** `inferno{canto}-{image}` (e.g., `inferno1-1`, `inferno1-2`)

---

*Last updated: 2025-12-26*
