# SOL191 · Sociología del Género · 2026

Repositorio del curso SOL191, Pontificia Universidad Católica de Chile.

## Estructura del proyecto

```
SOL191-2026/
├── _quarto.yml        # Configuración del sitio web
├── index.qmd          # Programa del curso (página principal)
├── docs/              # Output generado por Quarto (GitHub Pages)
└── .gitignore
```

## Cómo trabajar

Requiere [Quarto](https://quarto.org) y Positron (o RStudio / VS Code).

```bash
# Previsualizar en vivo
quarto preview

# Compilar sitio completo
quarto render
```

El output va a `/docs`. Para publicar en **GitHub Pages**, configura el repositorio en:
> Settings → Pages → Source: `Deploy from a branch` → Branch: `main` → Folder: `/docs`

## Para agregar clases

1. Crea un archivo `clases/c01.qmd`, `clases/c02.qmd`, etc.
2. Agrégalo a la barra de navegación en `_quarto.yml`.
