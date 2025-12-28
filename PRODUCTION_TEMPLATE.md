# Production Template for Densworld Field Sketches

**Ready-to-use prompt formula for Commedia mnemonic images**

---

## Generator

**Use Gemini (Nano Banana Pro)** — produces rich crosshatching and atmospheric depth appropriate for Densworld imagery.

Enable Thinking mode for best results.

---

## Prompt Formula

```
Densworld field sketch: [LOCATION AND TIME]. [ATMOSPHERIC COLOR] watercolor
wash dominates the [sky/walls/space], with ink line work defining forms.

[SCENE DESCRIPTION — what is happening, who is present, what objects are visible.
Weave specific visual details INTO the scene description naturally. Do NOT
list objects separately or create a "zoomed details" section — this causes
the model to generate segmented images with inset panels.]

[BACKGROUND ELEMENTS — rendered softer, part of atmosphere]

No text, no caption, no border, no signature.
```

### Critical: No Zoom Sections

**DO NOT** include sections like:
- "Zoomed details:"
- "Close-up on:"
- "Detail shots:"

These cause the image model to create segmented compositions with circular inset panels instead of a single coherent scene. Weave all visual details directly into the scene description.

---

## Atmospheric Color by Region

| Region | Primary Atmosphere | Light Behavior |
|--------|-------------------|----------------|
| Yeller Quarry | Amber/rust wash | Amber glow that weighs, presses down |
| Eastern Tunnels | Blue-dark wash | Lantern light that stops at edges |
| The Dens | Gray-purple wash | Sourceless light, no shadows because everything is shadow |
| Denstone edge | Purple-gray bruise | Sick glow where dens meets sky |
| Capital Archive | Dust-yellow/blue-black | Candlelight confined, doesn't spread |
| Tower of Mirado | Steel gray/fountain blue | Light that rejects, anti-illumination |
| Dead River | Green-black | Bioluminescence, water that glows wrong |
| Northo | Cold gray/white-blue | Austere light, frost-touched |
| Capeast | Brown-amber | Warm but heavy, grimslew territory |
| Mirado Desert | Bleached ochre/white | Harsh, post-linguistic emptiness |

---

## Color Variety: Accents and Highlights

While one atmospheric color dominates each image, **add variety through accents**:

### Red Accents
- Rust stains on metal equipment
- Dried blood on bone fragments
- Faded red cloth (tent patches, rope bindings)
- Ember glow from dying fires
- Ochre-red mineral deposits on cave walls

### Yellow Accents
- Lantern flames (small, intense)
- Brass fittings on equipment (spyglass, compass edge)
- Yeller mineral deposits
- Parchment/journal pages catching light
- Sick yellow where bioluminescence fails

### Blue Accents (in warm scenes)
- Steel of blades or tools
- Shadow edges that go cold
- Reflected sky in still water
- Ink on open pages

### Secondary Glow Technique
Add to prompt when appropriate:
```
A secondary [color] glow from [source] picks out [specific objects],
creating contrast against the dominant [atmospheric color].
```

**Example:** "A secondary red glow from dying embers picks out the brass compass and journal spine, creating contrast against the dominant blue-dark."

---

## Object Selection Rules

**Each image needs 6 findable objects as mnemonic loci.**

### Good Objects (Clear Silhouettes)
- Lantern (glass and metal frame)
- Boots (distinctive shape)
- Coiled rope
- Open journal/book
- Surveying equipment (tripod, spyglass)
- Compass (circular, readable)
- Canteen/water skin
- Bone piles (countable)
- Crate/box
- Chair/stool
- Mug/cup

### Avoid
- Objects that merge into background
- Too-similar objects (two lanterns, two books)
- Objects used in recent images (check registry)
- Abstract or unclear shapes

### Position Template
```
Foreground left:   [Object 1]
Foreground center: [Object 2]
Foreground right:  [Object 3]
Middle left:       [Object 4]
Middle center:     [Object 5]
Middle right/back: [Object 6]
```

Or for interior scenes:
```
Left side:    [Objects 1-2]
Center:       [Objects 3-4]
Right side:   [Objects 5-6]
```

---

## Example Prompts

### Interior/Cave (Blue-Dark)

```
Densworld field sketch: Deep tunnel in eastern Yeller Quarry. Blue-dark
watercolor wash dominates the cave walls, with ink line work defining
the rock faces. Crosshatching in the deep tunnel mouth suggests a void
that breathes.

An old woman sits hunched near a single oil lantern, pale eyes catching
the small flame. Bone piles — yellowed femurs and skull fragments — are
stacked to her left. A clay water bowl rests near her feet, surface still.
The lantern sits on a wooden crate, its light stopping at the edges rather
than spreading. A second, smaller bone pile to her right has been carefully
sorted. The tunnel mouth opens behind her, deeper black than the walls.

The cave walls rendered with crosshatch texture. The floor scattered with
smaller bone fragments.

No text, no caption, no border, no signature.
```

### Exterior/Ridge (Amber)

```
Densworld field sketch: Ridge at Yeller Quarry at dusk. Amber and rust
watercolor wash dominates the sky, bleeding into gray-purple clouds.
Ink line work defines the rock formations and equipment.

A surveying tripod stands in the left foreground, brass and wood catching
the last light. A second tripod with instrument sits left of center,
slightly behind the first. A canvas tent to the right shows its darker
interior through a half-open flap. Camp supplies — crates and folded
equipment — cluster in the center ground. A coiled rope lies in the
foreground right, its spiral shape distinct against the rock.

The quarry walls and distant terrain rendered softer, part of the
atmospheric wash.

No text, no caption, no border, no signature.
```

### Interior/Tent (Gray-Purple)

```
Densworld field sketch: Interior of expedition tent at dens edge, gray dawn.
Gray-purple watercolor wash dominates the canvas walls, sourceless light
filtering through fabric. Ink lines define the objects within.

Wet boots stand in the foreground center, a black pool forming beneath them.
A camp cot to the left has blankets thrown back, rumpled. A wooden crate
beside the cot holds a tin mug on top. The central tent pole anchors the
composition vertically. The tent flap opening on the right shows gray
exterior. A pillow on the cot still holds the indent where the sleeper was.

The canvas walls rendered with wash texture, draping folds suggested by
lighter and darker areas.

No text, no caption, no border, no signature.
```

---

## Stochastic Source Selection

**Use SOURCE_AUDIT_LOG.json for prompt inspiration.**

1. Filter for rating 3-5 sources (rich visual content)
2. Randomly select from available sources
3. Read the source file for narrative texture
4. Extract a vivid moment with visual potential
5. Build the prompt around that moment

This creates variety and prevents region repetition.

---

## Workflow

1. **Select source stochastically** from SOURCE_AUDIT_LOG.json (rating 4-5)
2. **Read the source file** for vivid moments
3. **Identify the key moment** with visual potential
4. **Determine region** → atmospheric color
5. **Select 6 objects** appropriate to location (check registry for repeats)
6. **Write prompt** using natural language formula above
7. **Generate in Gemini (Nano Banana Pro)**
8. **Identify arrangement** (A: 3+3, B: 4+2, or C: 2+4) — see LOCUS_PLACEMENT_GUIDE.md
9. **Assign loci** following the path for that arrangement
10. **Save image** to appropriate folder
11. **Update registries** (object registry, region usage)

---

## Locus Assignment (MUST FOLLOW)

**See `LOCUS_PLACEMENT_GUIDE.md` for full details.**

After generating the image, identify which arrangement it follows:
- **A (3+3):** 3 foreground, 3 background — classic zigzag
- **B (4+2):** 4 foreground, 2 background — foreground-heavy
- **C (2+4):** 2 foreground, 4 background — background-heavy

Then assign loci following the path for that arrangement.

**Key principle:** Each locus is ONE visual element — not a cluster, not a person-with-accessories. The eye needs a single anchor point.

---

## Quality Checklist

Before using an image for mnemonic work:

- [ ] All 6 objects findable within 5 seconds
- [ ] Atmospheric color dominates (not just accents)
- [ ] Light behaves appropriately for region
- [ ] Crosshatching adds texture without obscuring
- [ ] No text, caption, border, or signature in image
- [ ] No Earth-specific architecture or cultural markers
- [ ] Loci assigned following LOCUS_PLACEMENT_GUIDE.md

---

## Revision Log

| Date | Change |
|------|--------|
| 2025-12-28 | Created for Commedia project, adapted from Bible mnemonic template |

---

*This template produces Densworld. Use it.*
