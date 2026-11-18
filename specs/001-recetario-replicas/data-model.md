# Data Model

## Perfume (data/perfumes.json)

| Campo | Significado | Ejemplo |
|---|---|---|
| r | Puesto por popularidad (votos en Fragrantica) | 10 |
| n | Nombre | Sauvage |
| b | Marca | Dior |
| g | Género: M mujer, H hombre, U unisex | H |
| y | Año de lanzamiento (puede faltar) | 2015 |
| f | Familia para dosificar: F fresco, L floral/frutal, M amaderado, O oriental/dulce | F |
| a | Acordes principales en español (hasta 5) | especiado fresco, ámbar, cítrico… |
| t / m / s | Notas de salida / corazón / fondo | bergamota de Calabria… |
| v | Votos | 23727 |
| p | Nota media (1–5) | 4.0 |
| u | Ruta de la ficha en fragrantica.com/perfume/ | dior/Sauvage-31861.html |

## Receta (calculada en la página)

- `pctEsencia = base[intensidad] + ajuste[familia]`, limitado a 8–45 %. Base: Suave 15, Estándar 30, Plus 38.
  Ajuste: F +5, L 0, M 0, O −5. El usuario puede mover el porcentaje a mano.
- `pctFijador` según el tipo elegido: tienda 5 %, DPG 5 %, dimeticona 0,5 %, alcohol con fijador 0 %.
- `mlEsencia`, `mlFijador` se redondean a 0,5 ml (frascos ≥ 30 ml) o 0,1 ml (más chicos);
  `mlAlcohol = total − mlEsencia − mlFijador`, así la suma es exacta.
- Reposo: F 14 días, L 21, M 21, O 28.

## Ítem de la lista de compras (localStorage `recetario.lista.v1`)

`{ id: puesto, ml: tamaño del frasco, n: cantidad de frascos, nivel: 'suave'|'estandar'|'plus' }`
Totales: esencia por perfume (ml y onzas, +5 % por pérdidas), alcohol total, fijador total, frascos por tamaño,
filtros y etiquetas.
