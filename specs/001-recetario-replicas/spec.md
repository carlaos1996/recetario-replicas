# Feature Specification: Recetario de réplicas de perfume

**Feature Branch**: `001-recetario-replicas`

**Created**: 2026-11-17

**Status**: Draft

**Input**: User description: "Quiero hacer réplicas de lociones que huelan como las originales. Una página HTML con las
lociones más famosas (top 300) y las medidas exactas de esencia, fijador y alcohol; la lista de todo lo que tengo que
comprar, el total, y el orden en que se colocan. Ya compro esencias de buena calidad en una tienda y les pongo fijador."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ver la receta de un perfume famoso (Priority: P1)

Busco un perfume (por nombre o marca), elijo el tamaño del frasco y la concentración, y veo cuántos ml de esencia,
fijador y alcohol lleva, en qué orden se ponen y cuánto tiempo reposa.

**Why this priority**: Es el corazón del pedido: medidas exactas para que huela rico.

**Independent Test**: Buscar "Sauvage", elegir 100 ml, ver ml de cada ingrediente que suman 100 ml.

**Acceptance Scenarios**:

1. **Given** la página abierta, **When** escribo "sauv", **Then** aparece Sauvage de Dior con sus notas.
2. **Given** un perfume elegido, **When** cambio de 100 ml a 50 ml, **Then** todas las medidas se recalculan y suman 50 ml.
3. **Given** un perfume cítrico/fresco, **When** veo la receta, **Then** lleva más esencia que uno oriental pesado, con la razón explicada.

---

### User Story 2 - Armar la lista de compras total (Priority: P2)

Marco los perfumes que quiero hacer y cuántos frascos de cada uno; la página suma todo: esencia de cada perfume,
alcohol total, fijador total, frascos, y los instrumentos que necesito una sola vez.

**Why this priority**: El usuario quiere ir a su tienda sabiendo exactamente qué y cuánto comprar.

**Independent Test**: Agregar 3 perfumes × 2 frascos de 100 ml y ver totales correctos.

**Acceptance Scenarios**:

1. **Given** 2 perfumes en la lista, **When** subo la cantidad de frascos, **Then** los totales suben en proporción.
2. **Given** una lista armada, **When** cierro y abro la página, **Then** la lista sigue ahí.
3. **Given** una lista, **When** toco "copiar/imprimir", **Then** obtengo un texto limpio para llevar a la tienda.

---

### User Story 3 - Aprender el proceso y los instrumentos (Priority: P3)

Una guía paso a paso: qué instrumentos sirven, el orden de mezcla, el reposo (maceración), cómo filtrar, cómo
ajustar si no dura o si huele a alcohol, y cómo llevar registro de pruebas.

**Why this priority**: El usuario ya hace mezclas básicas; esto sube la calidad y la repetibilidad.

**Independent Test**: Leer la guía y poder hacer un frasco sin consultar nada más.

**Acceptance Scenarios**:

1. **Given** la guía, **When** la sigo, **Then** sé qué va primero (esencia), luego fijador, luego alcohol, reposo y filtrado.

### Edge Cases

- Tamaño de frasco no estándar (ej. 35 ml o 8 ml de bolsillo): se calcula igual.
- La tienda vende el fijador ya mezclado con alcohol o vende "fijador" de otro tipo: la guía explica cómo ajustar.
- Perfume que no está en el top 300: receta genérica por familia olfativa.
- Lista de compras vacía: mensaje claro, no tabla vacía.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: La página MUST mostrar al menos 300 perfumes famosos con marca, año, género, familia y notas (salida, corazón, fondo).
- **FR-002**: La página MUST permitir buscar por nombre, marca o nota y filtrar por género y familia.
- **FR-003**: Para cada perfume MUST mostrar la receta en ml (esencia, fijador, alcohol) para el tamaño elegido, que sume exactamente el total.
- **FR-004**: La receta MUST ajustarse por familia olfativa (frescos más carga, orientales menos) y por concentración (EDT / EDP / Extracto).
- **FR-005**: La página MUST mostrar equivalencias en gotas y gramos.
- **FR-006**: La página MUST mostrar el orden de mezcla y el tiempo de reposo recomendado.
- **FR-007**: Los usuarios MUST poder armar una lista de compras con varios perfumes y cantidades, y ver totales de cada insumo.
- **FR-008**: La lista MUST incluir los instrumentos y materiales de una sola vez (probetas, pipetas, frascos, embudo, filtros, etc.).
- **FR-009**: La lista MUST guardarse en el navegador y poder copiarse/imprimirse.
- **FR-010**: La página MUST incluir advertencias de seguridad (alcohol correcto, inflamable, prueba en piel).
- **FR-011**: La página MUST incluir la investigación de repositorios de GitHub sobre perfumería (con estrellas reales).

### Key Entities

- **Perfume**: nombre, marca, año, género, familia, acordes principales, notas, popularidad (votos), carga de esencia recomendada.
- **Receta**: tamaño, concentración, ml de esencia / fijador / alcohol, reposo.
- **Ítem de compra**: insumo, cantidad total, unidad.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Encontrar un perfume y ver su receta en menos de 15 segundos.
- **SC-002**: Las medidas de cada receta suman exactamente el tamaño del frasco (error 0 ml).
- **SC-003**: La lista de compras de 5 perfumes se arma en menos de 2 minutos.
- **SC-004**: La página funciona en celular de 375 px de ancho sin scroll horizontal.

## Assumptions

- El usuario compra **esencias "tipo"** (aceites que ya imitan al original) en su tienda; la página no inventa la fórmula
  química del original, da la dilución correcta.
- El "fijador" de tienda se usa al 5–10 % del total; si la tienda indica otra dosis, manda la de la tienda.
- Alcohol: etílico de perfumería (96°, ideal desnaturalizado para perfumería); no se usa alcohol isopropílico.
- Precios: no se incluyen porque varían por tienda y país; la lista da cantidades.
- La popularidad se toma de un conjunto de datos público de Fragrantica (cantidad de votos).
