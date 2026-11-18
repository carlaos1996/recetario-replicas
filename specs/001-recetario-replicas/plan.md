# Implementation Plan: Recetario de réplicas de perfume

**Branch**: `001-recetario-replicas` | **Date**: 2026-11-17 | **Spec**: [spec.md](spec.md)

## Summary

Una sola página HTML, sin servidor, con el top de perfumes de Fragrantica (300 destacados, 1000 en total), una
calculadora de receta por perfume (esencia / fijador / alcohol en ml, gotas y gramos, orden y reposo), una lista
de compras que suma todo, y una guía de proceso e instrumentos. Los datos se generan con un script de Python a
partir del CSV público y se incrustan en la página.

## Technical Context

**Language/Version**: HTML + CSS + JavaScript sin librerías; Python 3.11 solo para generar los datos
**Primary Dependencies**: ninguna en la página; fuentes de Google Fonts con respaldo del sistema
**Storage**: `localStorage` del navegador para la lista de compras (comodidad, se puede copiar como texto)
**Testing**: prueba manual en navegador (escritorio y 375 px) + verificación de que cada receta suma el total
**Target Platform**: navegador de celular y computadora; publicada como Artifact privado
**Project Type**: página web estática de un solo archivo
**Constraints**: funciona sin internet una vez abierta; < 1 MB
**Scale/Scope**: 1000 perfumes, 3 vistas (Perfumes, Mi lista, Guía)

## Constitution Check

| Principio | Cumple | Cómo |
|---|---|---|
| I. Datos comprobados | Sí | Fuente citada, link a Fragrantica en cada perfume; la familia se marca como estimada |
| II. Medidas medibles | Sí | ml + gotas + gramos, cualquier tamaño, la suma cuadra exacto |
| III. Seguridad | Sí | Avisos visibles en receta y guía |
| IV. Simple y sin internet | Sí | Un archivo HTML, datos incrustados |
| V. Español llano | Sí | Glosario corto en la guía |

## Project Structure

```text
specs/001-recetario-replicas/   # spec.md, plan.md, research.md, data-model.md, tasks.md
scripts/
├── build.py                    # CSV → data/perfumes.json → index.html
├── names.py                    # nombres legibles de marcas y perfumes
└── es.py                       # traducciones de notas y acordes; familia por acorde
src/template.html               # la página (con marcador de datos)
data/perfumes.json              # datos generados
index.html                      # página final (se publica en GitHub Pages)
```

**Structure Decision**: página única porque el usuario la usa en la tienda desde el celular; los datos se
generan aparte para poder actualizarlos si sale un CSV más nuevo.
