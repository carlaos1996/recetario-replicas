# Recetario de Réplicas

Página para hacer réplicas de perfumes en casa con medidas exactas.

**Abrir la página:** https://carlaos1996.github.io/recetario-replicas/

## Qué trae

- Los 1000 perfumes más votados en Fragrantica, con los 300 primeros marcados.
- Una receta por perfume: ml de esencia, fijador y alcohol, también en gotas y gramos. Elegís el tamaño (10, 30, 50, 100 ml u otro) y la intensidad.
- El orden de mezcla y los días de reposo según la familia del perfume.
- Una lista de compras que suma la esencia, el alcohol, el fijador, los frascos y los filtros. La lista se guarda en tu navegador.
- Una guía con instrumentos, paso a paso, problemas comunes y seguridad.

Receta base para 100 ml: 30 ml de esencia + 5 ml de fijador + 65 ml de alcohol de perfumería. Los frescos llevan 5 puntos más de esencia y los dulces u orientales 5 menos.

## Cómo está armado

| Carpeta | Qué hay |
|---|---|
| `index.html` | La página completa, funciona sola (los datos van adentro). |
| `src/template.html` | La página sin datos. Se edita acá. |
| `scripts/` | `build.py` arma `index.html`; `names.py` y `es.py` limpian nombres y traducen notas. |
| `data/perfumes.json` | Los 1000 perfumes ya procesados. |
| `specs/`, `.specify/` | Organización del proyecto con [Spec Kit](https://github.com/github/spec-kit): especificación, plan, investigación y tareas. |

## Volver a generar la página

Hace falta Python 3. Bajá el CSV de datos ([fra_cleaned.csv](https://github.com/lyudmil-apostolov/Fragrance-project/blob/main/data/fra_cleaned.csv)) y corré:

```bash
python scripts/build.py ruta/a/fra_cleaned.csv 1000
```

## Fuentes y límites

- Datos de perfumes: [Fragrance-project](https://github.com/lyudmil-apostolov/Fragrance-project), tomados de Fragrantica, hasta 2024.
- Las proporciones salen de tiendas y guías de perfumería; las fuentes están en la pestaña Guía y en [research.md](specs/001-recetario-replicas/research.md).
- La familia de cada perfume se estima a partir de sus acordes.
- Las fórmulas originales son secretas: el parecido depende sobre todo de la calidad de la esencia.
- Proyecto personal, sin relación con las marcas mencionadas.
