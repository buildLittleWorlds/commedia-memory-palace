# Quick Start: Commedia Memory Palace Production

The 13-step process for creating memory palace images.

---

## Steps 1-4: Preparation

**1. Identify the next lines**
Check `COMMEDIA_MAPPINGS.json` for the last completed entry. The next image covers the following 6 lines (2 tercets).

**2. Select source randomly**
```python
import json, random
with open('SOURCE_AUDIT_LOG.json') as f:
    sources = json.load(f)
valid = [s for s in sources if s['rating'] >= 3]
print(random.choice(valid))
```
NO THEMATIC MATCHING. The source has nothing to do with Dante's text.

**3. Read the source file**
Find a vivid moment, setting, or action. Extract sensory details.

**4. Write the prompt**
Follow `PRODUCTION_TEMPLATE.md`. Densworld field sketch style. Request 6 distinct objects.

---

## Steps 5-8: Image and HTML

**5. Generate the image**
User generates in Gemini (Nano Banana Pro) and adds to `inferno1-1/images/`.

**CRITICAL: Do NOT attempt to identify loci or plan line-to-object mappings until AFTER the image is generated and provided. Pre-planning creates bias that skews your ability to see what's actually in the image.**

**6. Identify arrangement**
View the image. Count foreground vs background objects:
- **A (3+3)**: 3 foreground, 3 background
- **B (4+2)**: 4 foreground, 2 background
- **C (2+4)**: 2 foreground, 4 background

**7. Assign loci**
Walk the path for that arrangement. Each locus is ONE specific element.
- Use maximum specificity: "steering wheel" not "car"
- Check `object_registry` for recent repeats
- See `LOCUS_PLACEMENT_GUIDE.md` for full details

**8. Create HTML page**
Layout matches arrangement:

| Arrangement | Below Image | Right of Image |
|-------------|-------------|----------------|
| A (3+3) | 3 lines | 3 lines |
| B (4+2) | 4 lines | 2 lines |
| C (2+4) | 2 lines | 4 lines |

Copy previous HTML, update content.

---

## Steps 9-13: Icon and Registry

**9. Create icon prompt**
Select one distinctive object from the image. Use this template:

```
Simple icon of [OBJECT], pure black lines on transparent background,
minimalist line drawing style, centered composition, clean geometric design.
PNG with transparent background. No colors, no grays - only pure black (#000000) strokes.
```

The CSS uses `filter: invert(1)` to display icons as white on dark background.

**10. Generate icon**
User generates icon and adds to `home-icons/`.

**11. Update home page**
Add the new icon with link to the HTML page.

**12. Update COMMEDIA_MAPPINGS.json**
Add entry with:
- `image_id`, `lines`, `source_file`
- `setting`, `arrangement`
- `loci` array (6 objects with line numbers)

**13. Commit and push**
```bash
git add . && git commit -m "Add inf-1-XXX" && git push
```

---

## Key Principles

- **Arbitrariness**: Source selection is random. Connections emerge after, not during.
- **Specificity**: "bent head looking down" not "figure"
- **Single element**: Each locus passes the finger test
- **No recent repeats**: Check object_registry for last 7 images

---

*See COMMEDIA_MANUAL.md for full documentation.*
