# Locus Placement Guide

How to assign lines to objects in Commedia memory images.

---

## Flexible Arrangements

Images are generated with creative freedom — the model arranges objects naturally rather than to a rigid grid. After generation, identify which arrangement the image follows, then assign loci accordingly.

### Arrangement A: 3 Foreground + 3 Background

The classic zigzag. Three objects in foreground, three in background.

```
┌─────────────────────────────────────────┐
│                                         │
│   (6)            (5)            (4)     │   ← BACKGROUND
│   left         center         right     │
│                                         │
├ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┤
│                                         │
│   (1)            (2)            (3)     │   ← FOREGROUND
│   left         center         right     │
│                                         │
└─────────────────────────────────────────┘
```

**Path:** Foreground L→C→R, then Background R→C→L

1. Line 1 → Foreground left
2. Line 2 → Foreground center
3. Line 3 → Foreground right
4. Line 4 → Background right
5. Line 5 → Background center
6. Line 6 → Background left

---

### Arrangement B: 4 Foreground + 2 Background

Common when the scene has a dominant foreground action. Four objects up front, two in the distance.

```
┌─────────────────────────────────────────┐
│                                         │
│        (6)                  (5)         │   ← BACKGROUND
│        left                right        │
│                                         │
├ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┤
│                                         │
│   (1)       (2)       (3)       (4)     │   ← FOREGROUND
│   left    center-L  center-R   right    │
│                                         │
└─────────────────────────────────────────┘
```

**Path:** Foreground L→CL→CR→R, then Background R→L

1. Line 1 → Foreground left
2. Line 2 → Foreground center-left
3. Line 3 → Foreground center-right
4. Line 4 → Foreground right
5. Line 5 → Background right
6. Line 6 → Background left

---

### Arrangement C: 2 Foreground + 4 Background

Less common. Two objects close to viewer, four spread across the background (often figures or scene elements).

```
┌─────────────────────────────────────────┐
│                                         │
│   (6)       (5)       (4)       (3)     │   ← BACKGROUND
│   left    center-L  center-R   right    │
│                                         │
├ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┤
│                                         │
│        (1)                  (2)         │   ← FOREGROUND
│        left                right        │
│                                         │
└─────────────────────────────────────────┘
```

**Path:** Foreground L→R, then Background R→CR→CL→L

1. Line 1 → Foreground left
2. Line 2 → Foreground right
3. Line 3 → Background right
4. Line 4 → Background center-right
5. Line 5 → Background center-left
6. Line 6 → Background left

---

## Identifying the Arrangement

After generating an image:

1. **Count foreground objects** — How many distinct objects are in the lower half / closer to viewer?
2. **Count background objects** — How many are in the upper half / farther away?
3. **Match to arrangement:**
   - A (3+3) — balanced foreground and background
   - B (4+2) — foreground-heavy
   - C (2+4) — background-heavy
4. **Assign loci** — Follow the path for that arrangement

If the image doesn't fit any pattern cleanly, adapt: the principle is always **foreground left-to-right, then background right-to-left**.

---

## HTML Layout Follows the Arrangement

The HTML page layout mirrors the image composition. **Foreground loci go below the image; background loci go to the right.**

### Layout by Arrangement

| Arrangement | Below Image (foreground) | Right of Image (background) |
|-------------|--------------------------|----------------------------|
| **A (3+3)** | 3 lines (1-3) | 3 lines (4-6) |
| **B (4+2)** | 4 lines (1-4) | 2 lines (5-6) |
| **C (2+4)** | 2 lines (1-2) | 4 lines (3-6) |

### Why This Matters

The physical layout reinforces the memory path:
- The eye naturally reads **below** first (foreground), then moves **right** (background)
- This mirrors walking through the image: foreground left-to-right, then background right-to-left
- The HTML structure matches the image structure

---

## Locus Specificity: One Thing Only

**Each locus is ONE visual element — not a cluster, not a person-with-accessories, not a machine-with-screen.**

The eye needs a single anchor point. When you look at that spot in the image, you should land on ONE thing.

### Wrong (too many elements)
- "Redbox machine with alien movie on screen" — that's a machine + a screen + an image
- "Boy in tie-dye shirt, finger on RENT button" — that's a person + clothing + hand + button
- "Woman with beanie and shopping cart" — that's a person + hat + cart
- "Ox dragging Truck" — that's two people + an action

### Right (single visual anchor)
- "Alien face on screen"
- "Tie-dye spiral pattern"
- "Shopping cart handle"
- "Ox's hands pulling Truck's shirt"

### The Finger Test

Can you point to it with one finger? If describing it requires "with" or "and," you've included too much.

**Person → pick ONE detail** (their hat, their hand position, their distinctive clothing feature)
**Machine → pick ONE part** (the screen, a button, a slot)
**Scene element → pick the tightest visual anchor**

---

## Handling Imperfect Images

### No object in the expected zone

Find the object **closest** to the correct zone. The path order matters more than exact positioning.

### Object is in the right zone but repeats a recent object

Skip it and find the **next closest** distinct object. Check `object_registry` in `COMMEDIA_MAPPINGS.json` for recent usage.

### Objects are clumped together

Prefer objects that are spatially separated from each other. A well-spaced path is easier to walk mentally.

---

## Object Selection Principles

1. **Follow the path** — The zone order (1→2→3→4→5→6) is primary
2. **Spatial separation** — Objects should not be adjacent; prefer spread across the image
3. **Distinctness** — Each object should be visually unique
4. **One object per locus** — Never combine two objects into one locus (e.g., "inkwell with wax seals" is wrong—choose either "inkwell" OR "wax seals", not both)
5. **Tight visual anchors** — The locus must be a specific point the eye can land on, not a whole scene or action. "The Boss" is a whole person—use "maze-braided red hair" or "the Boss's raised arm."
6. **No recent repeats** — Avoid objects used within the last week (~7 images)
7. **Long-term uniqueness** — Ideally, objects are unique across the entire project (this becomes harder over time)
8. **Specificity over generality** — Choose the most specific name for the object. "Front doors of building" is better than "institutional building." "Steering wheel" is better than "car interior." "Bent head looking down" is better than "figure at car door." The more specific, the less likely to repeat across 2,372 images.

---

## Example: Inferno I, 7-12 (Yeller Quarry)

Image contains: open ledger (left foreground), pickaxe (center foreground), ore cart (center-right foreground), lunch pail (right foreground), gnarled tree with roots (right background), telescope on tripod (center background), crumbling canyon floor (center-left background), rope on spike (left edge background).

**Arrangement identified:** B (4+2) — four foreground objects, two background

**Walking the path:**

| Line | Zone | Best Object | Reasoning |
|------|------|-------------|-----------|
| 7 | Foreground left | open ledger with quill | Clear object in correct zone |
| 8 | Foreground center-left | pickaxe | Perfect placement |
| 9 | Foreground center-right | ore cart wheel | Lunch pail too close to edge; cart wheel is in correct zone |
| 10 | Foreground right | lunch pail | Correct zone |
| 11 | Background right | tree roots | Gnarled tree roots are in correct zone, distinctive |
| 12 | Background left | telescope on tripod | Perfect placement |

**Rejected alternatives:**
- Rope on spike for line 12 — Too similar to recent object (line 3 used "rope coil with stake")
- Full "gnarled tree" — Too large; "tree roots" is the tight visual anchor

---

## Example: Inferno I, 43-48 (W2 Parking Lot)

Image contains: briefcase spilling papers (left foreground), manila folders fanned on ground (right foreground), metal thermos (background right near car), steering wheel visible through open door (background center-right), figure with bent head looking down (background center-left), institutional building with front doors visible (background left).

**Arrangement identified:** C (2+4) — two foreground objects, four background

**Walking the path:**

| Line | Zone | Best Object | Reasoning |
|------|------|-------------|-----------|
| 43 | Foreground left | open briefcase | Clear object in correct zone |
| 44 | Foreground right | manila folders | Distinct from briefcase, correct zone |
| 45 | Background right | metal thermos | Specific object, not "car" or "tire" |
| 46 | Background center-right | steering wheel | More specific than "car interior" — won't repeat |
| 47 | Background center-left | bent head looking down | More specific than "figure" — captures the posture |
| 48 | Background left | front doors of building | More specific than "building" — the doors are the anchor |

**Specificity decisions:**
- "Steering wheel" not "car" — cars appear often; steering wheels are specific
- "Bent head looking down" not "figure at car door" — the posture is the visual anchor
- "Front doors of building" not "institutional building" — the doors are what the eye lands on
- This specificity prevents collision with future images containing cars, figures, or buildings

---

## Quick Checklist

Before finalizing locus assignments:

- [ ] Have I identified the arrangement (A: 3+3, B: 4+2, or C: 2+4)?
- [ ] Does each line follow the path order for that arrangement?
- [ ] Are objects spatially separated (not clumped)?
- [ ] Is each object visually distinct from the others in this image?
- [ ] Is each locus a SINGLE element (passes the finger test)?
- [ ] Have I checked `object_registry` for recent repeats?
- [ ] **Is each object named as specifically as possible?** ("steering wheel" not "car", "front doors" not "building", "bent head" not "figure")
- [ ] If an ideal object was skipped, is there a clear reason documented?

---

*Last updated: 2025-12-28*
