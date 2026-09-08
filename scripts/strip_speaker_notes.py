#!/usr/bin/env python3
"""Elimina las notas del presentador (<aside class="notes">...</aside>)
de los HTML de revealjs ya renderizados en docs/, para que no queden
publicadas en GitHub Pages.

Las notas siguen existiendo en los .qmd fuente (bloques `::: notes`) y
en la vista de orador al presentar localmente con `quarto preview`;
esto solo limpia la copia pública generada en docs/.
"""
import re
import sys
from pathlib import Path

NOTES_RE = re.compile(r"<aside class=\"notes\">.*?</aside>\s*", re.DOTALL)

def strip_file(path: Path) -> int:
    html = path.read_text(encoding="utf-8")
    cleaned, n = NOTES_RE.subn("", html)
    if n:
        path.write_text(cleaned, encoding="utf-8")
    return n

def main():
    docs_dir = Path(__file__).resolve().parent.parent / "docs"
    total = 0
    for html_file in docs_dir.rglob("*.html"):
        n = strip_file(html_file)
        if n:
            print(f"  - {html_file.relative_to(docs_dir.parent)}: {n} nota(s) eliminada(s)")
            total += n
    print(f"strip_speaker_notes: {total} nota(s) del presentador eliminadas de docs/.")

if __name__ == "__main__":
    sys.exit(main())
