#!/usr/bin/env python3
"""Remove Pandoc `::: notes` fenced divs (revealjs speaker notes) from a .qmd file.

Usage: python3 strip_speaker_notes.py <input.qmd> <output.qmd>

The notes divs are always fenced with exactly three colons in this project's
slides (outer containers like columns use four), so a line that is exactly
"::: notes" opens a block and the next line that is exactly ":::" closes it.
"""
import sys


def strip_notes(lines):
    out = []
    skipping = False
    for line in lines:
        stripped = line.strip()
        if not skipping and stripped == "::: notes":
            skipping = True
            continue
        if skipping:
            if stripped == ":::":
                skipping = False
            continue
        out.append(line)

    # Collapse runs of 2+ blank lines left behind by removed blocks.
    collapsed = []
    blank_run = 0
    for line in out:
        if line.strip() == "":
            blank_run += 1
            if blank_run <= 1:
                collapsed.append(line)
        else:
            blank_run = 0
            collapsed.append(line)
    return collapsed


def main():
    if len(sys.argv) != 3:
        sys.exit(f"Usage: {sys.argv[0]} <input.qmd> <output.qmd>")
    input_path, output_path = sys.argv[1], sys.argv[2]

    with open(input_path, encoding="utf-8") as f:
        lines = f.readlines()

    result = strip_notes(lines)

    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(result)

    print(f"Wrote {output_path} ({len(result)} lines, from {len(lines)})")


if __name__ == "__main__":
    main()
