#!/usr/bin/env python3
"""
Extract clean Inferno text from Gutenberg files.
Creates line-numbered files for Italian and Longfellow English.
"""

import re

def extract_longfellow_inferno(raw_file, output_file):
    """Extract Longfellow's Inferno, one line per line number."""
    with open(raw_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find start of Inferno (after table of contents)
    inferno_start = content.find("Inferno: Canto I")
    # Find end of Inferno (start of Purgatorio)
    purgatorio_start = content.find("Purgatorio: Canto I")

    if inferno_start == -1 or purgatorio_start == -1:
        print(f"Could not find Inferno boundaries")
        return

    inferno_text = content[inferno_start:purgatorio_start]

    lines = []
    current_canto = 0

    for line in inferno_text.split('\n'):
        line = line.strip()

        # Skip empty lines and canto headers
        if not line:
            continue
        if line.startswith("Inferno: Canto"):
            match = re.search(r'Canto (\w+)', line)
            if match:
                canto_num = match.group(1)
                # Convert Roman to Arabic
                roman_map = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10,
                            'XI':11,'XII':12,'XIII':13,'XIV':14,'XV':15,'XVI':16,'XVII':17,'XVIII':18,
                            'XIX':19,'XX':20,'XXI':21,'XXII':22,'XXIII':23,'XXIV':24,'XXV':25,
                            'XXVI':26,'XXVII':27,'XXVIII':28,'XXIX':29,'XXX':30,'XXXI':31,
                            'XXXII':32,'XXXIII':33,'XXXIV':34}
                current_canto = roman_map.get(canto_num, 0)
            continue

        # This is a verse line
        lines.append((current_canto, line))

    # Write output with global line numbers
    with open(output_file, 'w', encoding='utf-8') as f:
        line_num = 1
        current_canto = 0
        for canto, text in lines:
            if canto != current_canto:
                if current_canto > 0:
                    f.write("\n")
                f.write(f"=== CANTO {canto} ===\n")
                current_canto = canto
            f.write(f"{line_num}\t{text}\n")
            line_num += 1

    print(f"Wrote {line_num - 1} lines to {output_file}")


def extract_italian_inferno(raw_file, output_file):
    """Extract Italian Inferno from Gutenberg."""
    with open(raw_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find Inferno section - Italian file uses "Inferno • Canto I" format
    inferno_match = re.search(r'Inferno\s*[•·]\s*Canto\s+I\b', content)
    purgatorio_match = re.search(r'Purgatorio\s*[•·]\s*Canto\s+I\b', content)

    if not inferno_match or not purgatorio_match:
        print("Could not find Italian Inferno boundaries")
        return

    inferno_text = content[inferno_match.start():purgatorio_match.start()]

    lines = []
    current_canto = 0

    for line in inferno_text.split('\n'):
        line = line.strip()

        if not line:
            continue

        # Check for canto headers - format is "Inferno • Canto X"
        canto_match = re.search(r'Inferno\s*[•·]\s*Canto\s+(\w+)', line, re.IGNORECASE)
        if canto_match:
            canto_str = canto_match.group(1).upper()
            roman_map = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10,
                        'XI':11,'XII':12,'XIII':13,'XIV':14,'XV':15,'XVI':16,'XVII':17,'XVIII':18,
                        'XIX':19,'XX':20,'XXI':21,'XXII':22,'XXIII':23,'XXIV':24,'XXV':25,
                        'XXVI':26,'XXVII':27,'XXVIII':28,'XXIX':29,'XXX':30,'XXXI':31,
                        'XXXII':32,'XXXIII':33,'XXXIV':34}
            current_canto = roman_map.get(canto_str, current_canto)
            continue

        # This is a verse line
        if current_canto > 0:
            lines.append((current_canto, line))

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        line_num = 1
        current_canto = 0
        for canto, text in lines:
            if canto != current_canto:
                if current_canto > 0:
                    f.write("\n")
                f.write(f"=== CANTO {canto} ===\n")
                current_canto = canto
            f.write(f"{line_num}\t{text}\n")
            line_num += 1

    print(f"Wrote {line_num - 1} lines to {output_file}")


if __name__ == "__main__":
    base = "/Users/familyplate/densworld-courses/_mnemonic-system/_source-texts"

    print("Extracting Longfellow English...")
    extract_longfellow_inferno(
        f"{base}/longfellow_inferno_raw.txt",
        f"{base}/inferno_longfellow.txt"
    )

    print("\nExtracting Italian...")
    extract_italian_inferno(
        f"{base}/dante_italian_raw.txt",
        f"{base}/inferno_italian.txt"
    )
