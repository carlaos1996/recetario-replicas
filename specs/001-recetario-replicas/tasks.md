# Tasks: Recetario de réplicas de perfume

**Input**: spec.md, plan.md, research.md, data-model.md

## Phase 1: Setup
- [x] T001 Inicializar Spec Kit y escribir la constitución (.specify/memory/constitution.md)
- [x] T002 Investigar repos de GitHub y fuentes de proporciones (research.md)

## Phase 2: Datos (bloquea todo lo demás)
- [x] T003 Bajar el CSV público de Fragrantica y ordenar por votos
- [x] T004 [P] scripts/names.py: nombres legibles de marcas y perfumes
- [x] T005 [P] scripts/es.py: traducción de notas y acordes, familia por acorde
- [x] T006 scripts/build.py: generar data/perfumes.json e incrustarlo en la página

## Phase 3: User Story 1 — Receta de un perfume (P1) 🎯 MVP
- [x] T007 [US1] src/template.html: buscador, filtros (género, familia, solo top 300) y lista
- [x] T008 [US1] Ficha del perfume: notas, acordes, link a Fragrantica
- [x] T009 [US1] Calculadora: tamaño, intensidad, fijador, ajuste fino de %; ml + gotas + gramos; suma exacta
- [x] T010 [US1] Orden de mezcla y días de reposo según familia

## Phase 4: User Story 2 — Lista de compras (P2)
- [x] T011 [US2] Agregar a la lista con tamaño, cantidad e intensidad; guardar en el navegador
- [x] T012 [US2] Totales: esencia por perfume (ml y oz), alcohol, fijador, frascos, filtros, etiquetas
- [x] T013 [US2] Instrumentos de una sola vez y botón "Copiar lista"

## Phase 5: User Story 3 — Guía (P3)
- [x] T014 [US3] Instrumentos, paso a paso, problemas comunes, seguridad, fuentes y repos de GitHub

## Phase 6: Verificación
- [x] T015 Probar en navegador: búsqueda, cálculo (suma exacta), lista persistente, 375 px sin scroll lateral
- [x] T016 Publicar la página (https://claude.ai/artifact/WwMEHMoRHH66ghyGY8wBcY)
- [x] T017 Subir el proyecto a GitHub y publicar la página con GitHub Pages (https://carlaos1996.github.io/recetario-replicas/)
