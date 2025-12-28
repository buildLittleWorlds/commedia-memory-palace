# Production Template for Densworld Field Sketches

**Ready-to-use prompt formula for Commedia mnemonic images**

---

## ⚠️ CRITICAL: NO THEMATIC MATCHING ⚠️

**The Dante text you are memorizing has ZERO influence on source selection or prompt content.**

- DO NOT read the Dante lines and then search for matching sources
- DO NOT choose a source because it "fits" the mood of the poetry
- DO NOT let words like "lion," "dark wood," "fear," or "sweet season" guide your choices
- The source is selected STOCHASTICALLY (randomly from rating 3-5)
- The prompt comes entirely from the Densworld source — Dante provides NOTHING

**Wrong:** "These lines mention a lion, so I'll find creature/predator sources..."
**Right:** "I'll pick a random rated source and build the prompt from its imagery alone."

Any resonance between text and image emerges AFTER, during memorization. Never during creation.

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

⚠️ **REMINDER: The Dante lines have NO influence here. Do not even think about them.**

1. Filter for rating 3-5 sources (rich visual content)
2. **RANDOMLY select** from available sources — use a random method, not judgment
3. Read the source file for narrative texture
4. Extract a vivid moment with visual potential
5. Build the prompt around that moment — **the source alone determines content**

This creates variety, prevents region repetition, and maintains the arbitrariness principle.

---

## Workflow

⚠️ **Step 1 is NOT "read the Dante lines." The Dante lines are irrelevant to prompt creation.**

1. **Select source RANDOMLY** from SOURCE_AUDIT_LOG.json (rating 3-5) — do not let Dante influence this
2. **Read the source file** for vivid moments — the source alone provides imagery
3. **Identify the key moment** with visual potential
4. **Determine region** → atmospheric color
5. **Write prompt** using natural language formula above — describe a scene with visual richness
6. **Generate in Gemini (Nano Banana Pro)**
7. **STOP. Wait for user to provide the generated image.**

⚠️ **CRITICAL: Do NOT attempt steps 8-11 until AFTER the user has provided the generated image. Pre-planning loci creates bias that skews your ability to see what's actually in the image. The prompt describes a scene; the IMAGE determines the loci.**

8. **View the generated image** — only now identify arrangement (A: 3+3, B: 4+2, or C: 2+4)
9. **Assign loci** following the path for that arrangement, based on what you SEE
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

## Scene Types: Three Visual Registers

**Critical distinction:** Different scenes require different visual treatments. Know which register you're working in.

### Register 1: W1 Atmospheric/Liminal (WATERCOLOR WASH)

These scenes benefit from the full field sketch treatment:
- Open landscapes (quarry rim, grassland, desert)
- Interiors with ambient light (archive, tent, camp)
- Scenes where the *mood* is the subject
- Geometric voids meant to be seen (the black hole in the grass)

**Characteristics:**
- Watercolor wash dominates
- Loose, hand-drawn line work
- Paper texture visible
- Edges can bleed
- Figures as silhouettes work well
- The "bruised" dens-edge sky, the amber quarry wash — these are the goal

**Example regions:** Yeller Quarry rim, Mirado Desert, Dens edge grassland, Capital Archive

---

### Register 2: W1 Darkness/Horror (TIGHT CROSSHATCHING)

These scenes need more control — the watercolor wash softens horror into mere atmosphere:
- Underground/tunnel scenes with threat
- Dead River (the wrongness is in the *absence* of proper light)
- Any scene with creatures or monsters
- Scenes where darkness itself is the subject

**Characteristics:**
- Tighter line work with crosshatching for shadow
- Darkness should be *black*, not washed
- Light sources should "stop at edges" — specify this explicitly
- Creatures as SILHOUETTES ONLY — never fully rendered
- The void dominates; you should feel it pressing in
- Objects need crisp edges for findability against the dark

**Example regions:** Eastern Tunnels, Dead River, deep Dens interior

---

### Register 3: W2 Scenes (ILLUSTRATED/MUTED)

W2 is *our* world — the outer world that creates and studies Densworld. When a scene is set in W2, use the **same illustration technique** as W1 but with a muted palette and domestic subjects.

**CRITICAL: W2 is NOT photorealistic.** It uses the same ink-and-wash field sketch style as W1 images. The difference is the palette (desaturated sepia/gray) and the subject matter (real-world domestic scenes).

**Characteristics:**
- **Same ink line work** as W1 — hand-drawn, slightly loose
- **Same watercolor wash technique** — but desaturated (sepia, gray-brown)
- **Paper texture visible** — it's still an illustration
- **Crosshatching for shadows** — same as W1 images
- Mundane objects rendered in sketch style (phone cord, cereal box, kitchen chair)
- Window or threshold often present — showing landscape toward W1
- Feels like a quiet moment, not an expedition record

**When to use:**
- Scenes set in the "real world" outside Densworld
- Moments of contact between W2 observer and W1 subject
- Domestic/mundane settings that frame Densworld study
- Any scene where the *observer's* world matters more than the observed

**Visual language:**
- Ink line work with watercolor/sepia wash — NOT photorealistic
- Loose, hand-drawn quality — same as W1 field sketches
- Desaturated palette: gray-brown, sepia, muted tones
- Everyday objects as anchors (phones, mugs, books, furniture)
- Landscape visible through window suggests W1 in the distance

**Example prompt language:**
```
Densworld field sketch: W2 kitchen interior, morning. Sepia and gray-brown
watercolor wash dominates, with ink line work defining forms. Crosshatching
in the wall shadows.

A figure sits at a kitchen table, back to the viewer, phone cord coiled
across the wall. A cereal bowl and spoon on the table. Through the window,
a distant landscape — scrubland fading to horizon. An empty chair opposite.
A cereal box on the table edge.

Illustrated style with visible line work and paper texture. Muted,
desaturated palette. The quiet of early morning.

No text, no caption, no border, no signature.
```

**The W2 mood:** Stillness, observation, the weight of the ordinary. W2 scenes are about someone *looking at* or *thinking about* Densworld, not being inside it. But they are still **illustrations**, not photographs.

---

## Rendering Creatures and Threats

**CRITICAL: Densworld creatures should be glimpsed, not displayed.**

### Wrong (over-rendered)
```
A beast leaps from the tunnel mouth, lion-like mane bristling,
muscular body caught mid-spring, claws extended.
```
This produces a visible monster — like concept art for a video game. Not Densworld.

### Right (silhouette/suggestion)
```
A shape emerges from the tunnel darkness — bristling, wrong,
four-legged but not like any animal. Only its silhouette is
visible against the deeper black of the tunnel mouth.
```
This keeps the horror in the *not-quite-seeing*. The viewer's imagination fills in what the darkness hides.

### The Silhouette Principle

For any creature or threat:
- Describe it as a "shape" or "silhouette"
- Place it against something darker (tunnel mouth, void, shadow)
- Use words like "emerging," "glimpsed," "suggested"
- NEVER describe anatomical details (mane, claws, eyes)
- The darkness is the threat; the creature is evidence of the darkness

---

## Rendering Darkness and Bioluminescence

### Dead River: What "Glows Wrong" Means

The Dead River's bioluminescence should NOT be rendered as:
- Bright green patches on the water surface
- Visible glowing pools
- Swamp-like luminescence

The "wrongness" is that light doesn't behave normally. Render it as:
- Black water that should reflect but doesn't
- A faint sick glow that illuminates nothing
- Light that exists but fails to spread
- The *absence* of expected reflection/illumination

**Prompt language for Dead River:**
```
The water is black — not reflecting the lantern, not catching
the sky. A faint green-sick glow exists somewhere beneath the
surface but illuminates nothing. The light behaves wrong here.
```

### Tunnel/Cave Darkness

For underground scenes, darkness should press in:
- Firelight/lantern light "stops at edges" — include this phrase
- The tunnel mouth should be "deeper black than the walls"
- Crosshatching should suggest void, not just shadow
- The darkness should feel like a presence, not an absence

**Prompt language for tunnels:**
```
The lantern light stops at the edges of its small circle,
refusing to spread. The tunnel mouth behind opens into
deeper black — not shadow but void. The darkness breathes.
```

---

## Quick Reference: Scene Type Decision

Before writing a prompt, ask two questions:
1. **Which world is this scene in?** (W1 interior, or W2 looking in?)
2. **Is the subject what you see, or what you can't see?**

| If the scene is... | Register | Style |
|--------------------|----------|-------|
| W1 landscape, mood, atmosphere | Register 1 | Watercolor wash, loose lines |
| W1 visible geometric void | Register 1 | Watercolor wash |
| W1 pressing darkness, threat | Register 2 | Tight crosshatching, black voids |
| W1 creature or monster | Register 2 | Silhouette only, against darkness |
| W1 light that behaves wrong | Register 2 | Describe wrongness, don't render literally |
| W2 domestic/mundane | Register 3 | **Ink + muted wash** (NOT photorealistic) |
| W2 observer looking toward W1 | Register 3 | **Ink + sepia wash**, window/threshold |
| Boundary between worlds | Register 3 | **Illustrated**, muted palette, W1 in distance |

---

## Revision Log

| Date | Change |
|------|--------|
| 2025-12-28 | Created for Commedia project, adapted from Bible mnemonic template |
| 2025-12-28 | Added scene type distinctions (atmospheric vs. horror), creature rendering rules, darkness/bioluminescence guidance |
| 2025-12-28 | Added Register 3 (W2 scenes) — realistic/monochromatic style for outer-world and boundary scenes |
| 2025-12-28 | **Fixed Register 3** — W2 uses same ink+wash illustration style as W1, just muted palette. NOT photorealistic. |

---

*This template produces Densworld. Use it.*
