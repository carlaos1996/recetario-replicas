# Research: Recetario de réplicas de perfume

Fecha: 2026-11-17

## 1. Repositorios de GitHub sobre perfumería (pedido: más de 1000 estrellas)

**Resultado: no existe ningún repositorio de creación de perfumes con más de 1000 estrellas.**
Búsquedas hechas con `gh search repos` por: perfume, fragrance, perfumery, olfactory, olfaction, odor, scent,
smell, pyrfume, fragrantica, "perfume formula", "aroma chemical", "perfume dataset", "essential oil".
Los únicos resultados con más de 1000 estrellas son falsos positivos (comparten la palabra, no el tema):

| Repo | Estrellas | Por qué no sirve |
|---|---|---|
| Zizzamia/perfume.js | 3202 | Mide la velocidad de páginas web |
| Lidarr/Lidarr | 5830 | Descarga música ("looks and smells like…") |
| troessner/reek | 4137 | Detecta "malos olores" en código Ruby |
| LemonBoy/bar | 1688 | Barra de escritorio "con aroma a limón" |

Los mejores repos reales del tema (todos por debajo de 1000):

| Repo | Estrellas | Tipo | Para qué sirve |
|---|---|---|---|
| kellypeng/scentmate_rec | 117 | Información | Recomendador de perfumes con aprendizaje automático |
| pyrfume/pyrfume-data | 105 | Información | Datos científicos de moléculas olorosas |
| 5KG-UCAS/CosmeticsKG | 95 | Información | Grafo de conocimiento de labiales y perfumes |
| pyrfume/pyrfume | 77 | Herramienta | Librería Python para datos de olfato |
| jbparfum/parfumvault | 73 | **Herramienta** | Gestor de fórmulas para perfumistas (el más útil para formular) |
| FragDB/fragrance-database | 72 | Información | 134 mil perfumes; gratis solo 10 registros de muestra |
| ARY2260/openpom | 68 | Herramienta | Réplica del "Mapa Principal de Olores" (predice olor por molécula) |
| rdemarqui/perfume_recommender | 40 | Información | Recomendador de perfumes |
| osmoai/taxonomy | 31 | Información | Taxonomía de olores de Osmo |

## 2. Fuente del top de perfumes

- Conjunto de datos público de Fragrantica (`fra_cleaned.csv`, 24 063 perfumes, datos hasta 2024), copia en
  GitHub: https://github.com/lyudmil-apostolov/Fragrance-project/blob/main/data/fra_cleaned.csv
- Campos: marca, perfume, género, año, nota media, **cantidad de votos**, notas de salida/corazón/fondo, 5 acordes.
- **Decisión**: popularidad = cantidad de votos. Top 300 marcado como "Top"; se incluyen hasta el puesto 1000
  porque varios favoritos de Latinoamérica quedan después del 300 (CH Men #331, 212 VIP #357, 212 VIP Men #438,
  Bad Boy #619, Invictus Victory #808).
- Verificación puntual: las notas de Sauvage (bergamota de Calabria, pimienta; ambroxan, cedro, ládano) coinciden
  con lo publicado por la marca.

## 3. Proporciones de mezcla

| Fuente | Esencia | Fijador | Alcohol | Reposo |
|---|---|---|---|---|
| Aromaniak (tienda, El Salvador) | 30 ml por 100 ml (estándar), 45 ml (Plus) | 1–2 gotas, o alcohol que ya trae fijador | alcohol de perfumería | 7–15 días |
| Gran Velada (proveedor, España) | 30 % | dimeticona copoliol 0,5 % (o fijador universal 10 g en 100 g) | alcohol 96° | ~10 días |
| Floris / guías de concentración | EDT 5–15 %, EDP 15–20 %, Extracto 20–40 % | — | — | — |
| Fragrance Forte (industria) | — | — | — | 2–3 semanas; enfriar y filtrar si se enturbia |
| Foros Basenotes (aficionados) | — | — | — | 3–6 semanas; filtro de café mojado en alcohol |

**Decisiones**
- Tres intensidades: Suave (EDT) 15 %, Réplica estándar 30 %, Intenso/Plus 38 % (máximo 45 %).
- Ajuste por familia (regla práctica, no ley): frescos/cítricos +5 puntos (se evaporan rápido),
  orientales/dulces −5 (son densos y empalagan si se cargan). Florales y amaderados sin cambio.
- Fijador: por defecto 5 % del total (punto medio entre "1–2 gotas" y "10 %"); presets para DPG 5 %,
  dimeticona copoliol 0,5 % y "alcohol que ya trae fijador" 0 %. Si la etiqueta del fijador dice otra dosis, manda la etiqueta.
- Sin agua: en réplicas a 30 % el agua enturbia la mezcla.
- Orden: esencia → fijador → alcohol hasta completar → agitar suave → reposo → refrigerador 24–48 h → filtrar → envasar.
  (Gran Velada pone el alcohol primero; da igual químicamente. Se elige la esencia primero porque es lo que más
  importa medir exacto y el alcohol de después arrastra lo que quedó pegado en la probeta.)
- Reposo: fresco 14 días, floral y amaderado 21, oriental 28 (mínimo absoluto 7–10 días).
- Equivalencias: 1 ml ≈ 20 gotas de pipeta (varía 18–25); 1 oz de tienda ≈ 30 ml. Densidades aproximadas:
  esencia 0,97 g/ml, alcohol 96° 0,81 g/ml, DPG 1,02 g/ml.

## 4. Seguridad
- Nunca alcohol isopropílico (irrita la piel y huele fuerte).
- El alcohol es inflamable: lejos de fuego y calor.
- Prueba en piel (antebrazo, 24 h) antes de usar o regalar.
- Las esencias tienen límites de uso (IFRA); no pasar de 45 % de esencia.
