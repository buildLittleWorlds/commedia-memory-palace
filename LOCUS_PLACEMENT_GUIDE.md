# Locus Placement Guide

How to assign lines to objects in Commedia memory images.

---

## The Path Schema

The eye travels through the image in a specific order. Lines are assigned to objects along this path:

```
┌─────────────────────────────────────────┐
│                                         │
│   (6)            (5)            (4)     │   ← TOP HALF
│  left third    middle third   right third
│                                         │
├─────────────────────────────────────────┤
│                                         │
│   (1)            (2)            (3)     │   ← BOTTOM HALF
│  left third    middle third   right third
│                                         │
└─────────────────────────────────────────┘
```

**Order:**
1. Line 1 → Left third, bottom half
2. Line 2 → Middle third, bottom half
3. Line 3 → Right third, bottom half
4. Line 4 → Right third, top half
5. Line 5 → Middle third, top half
6. Line 6 → Left third, top half

The path moves left-to-right across the bottom, then right-to-left across the top.

---

## HTML Layout Follows the Schema

Because lines 1-3 (first tercet) map to the **bottom half** of the image:
- First tercet goes **below** the image

Because lines 4-6 (second tercet) map to the **top half** of the image:
- Second tercet goes **to the right** of the image

The eye reads the bottom tercet, then follows up to the right tercet—mirroring the path through the image.

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
4. **No recent repeats** — Avoid objects used within the last week (~7 images)
5. **Long-term uniqueness** — Ideally, objects are unique across the entire project (this becomes harder over time)

---

## Example: Inferno I, 7-12 (Yeller Quarry)

Image contains: open ledger (left foreground), pickaxe (center foreground), ore cart (center-right foreground), lunch pail (right foreground), gnarled tree with roots (right background), telescope on tripod (center background), crumbling canyon floor (center-left background), rope on spike (left edge background).

**Walking the path:**

| Line | Zone | Best Object | Reasoning |
|------|------|-------------|-----------|
| 7 | Left bottom | open ledger with quill | Clear object in correct zone |
| 8 | Middle bottom | pickaxe | Perfect placement |
| 9 | Right bottom | lunch pail | Ore cart is too close to pickaxe; lunch pail is in correct zone |
| 10 | Right top | tree roots | Gnarled tree roots are in correct zone, distinctive |
| 11 | Middle top | telescope on tripod | Perfect placement |
| 12 | Left top | crumbling canyon floor | Rope/spike would be perfect BUT too similar to line 3's "rope coil with stake"; canyon floor is next closest object moving left from telescope |

**Rejected alternatives:**
- Ore cart for line 9 — Too close to pickaxe (clumping)
- Rope on spike for line 12 — Too similar to recent object (line 3 used "rope coil with stake")

---

## Quick Checklist

Before finalizing locus assignments:

- [ ] Does each line follow the path order (bottom L→M→R, then top R→M→L)?
- [ ] Are objects spatially separated (not clumped)?
- [ ] Is each object visually distinct from the others in this image?
- [ ] Have I checked `object_registry` for recent repeats?
- [ ] If an ideal object was skipped, is there a clear reason documented?

---

*Last updated: 2025-12-26*
