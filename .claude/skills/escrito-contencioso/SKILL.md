---
name: escrito-contencioso
description: Procedimiento para demandas y escritos contencioso-administrativos (expropiación, justiprecio): esqueleto, hechos con su documento, fundamentos con cita literal, huecos marcados, Word y auditoría.
---

# Escrito contencioso-administrativo

Procedimiento para redactar demandas y escritos en el orden
contencioso-administrativo, sobre todo de expropiación y justiprecio. **Es un
procedimiento, no un formulario:** de un escrito anterior se toman la
estructura y el estilo, nunca su texto.

## Antes de empezar

- `FICHA-ENCARGO.md` de tipo procesal. Si no existe, skill `ficha-encargo`.
- En `entrada/`: el acto o las resoluciones que se impugnan, el expediente
  administrativo o lo que haya de él, las hojas de aprecio, el informe pericial
  si lo hay, y en `entrada/jurisprudencia/` las sentencias en PDF que se quieran
  citar.
- En `normativa/estatal-autonomica/`: la Ley de la Jurisdicción
  Contencioso-administrativa, la de Expropiación Forzosa, el texto refundido de
  la Ley de Suelo y el Reglamento de valoraciones.
- `estilo/GUIA-ESTILO-PROCESAL.md`.

## Procedimiento

### 1. Qué escrito y en qué trámite

1. Qué escrito es (interposición, demanda, contestación, conclusiones, recurso,
   otro) y en qué trámite está el procedimiento, según la ficha.
2. Localiza en la ley procesal de `normativa/` los artículos que regulan su
   contenido y su plazo. Cítalos con su texto. Si no están: `[VERIFICAR]`.
3. El plazo se apunta con su artículo. **No calcules la fecha final por tu
   cuenta**: propón el cómputo con el artículo delante y que lo confirme él.

### 2. Esqueleto

Propón la estructura antes de redactar y espera su corrección:

- Encabezamiento al órgano y número de procedimiento (`[DATO]` si no consta).
- Comparecencia: representación y dirección letrada, de la ficha y de
  `CLAUDE.local.md`.
- Objeto del escrito, en un párrafo.
- **HECHOS**, numerados, cada uno con un título que enuncia lo que prueba.
- **FUNDAMENTOS DE DERECHO**: primero los procesales (jurisdicción,
  competencia y procedimiento; legitimación y representación; acumulación si
  procede; cuantía), después los materiales, un motivo por infracción, con un
  título que dice qué norma se infringe y por qué.
- **SUPLICO**, con los pedimentos numerados.
- **OTROSÍES**, solo los que procedan en ese trámite, cada uno con el artículo
  que lo ampara, buscado en `normativa/`.

Para cada parte, una línea con lo que va a contener en ESTE caso. Marca lo que
no aplica.

### 3. Hechos

1. Cada hecho, anclado a un documento del expediente: «documento n.º [DATO:
   número]» hasta que se fije la numeración.
2. Lo que dicen las resoluciones impugnadas se cita literal y con su página o
   apartado. Nada de paráfrasis que cambie el sentido.
3. Los hechos no argumentan: lo que se discute va a los fundamentos.

### 4. Fundamentos

1. Cada motivo tiene tres piezas: la norma infringida (artículo y cita literal
   de `normativa/`), el hecho del expediente que lo demuestra (con su
   documento) y el razonamiento que las une.
2. **Jurisprudencia:** solo la que está en `entrada/jurisprudencia/`, con la cita
   literal del fundamento que se invoca. Si pide «jurisprudencia que apoye
   esto», no la des de memoria: dile qué criterio buscar para que la traiga él
   de su base de datos, y deja `[VERIFICAR: aportar sentencia sobre …]`.
3. Las cifras (valores, superficies, rentas, tipos) salen del informe pericial,
   de las hojas de aprecio o de las resoluciones, con su referencia. Si se
   calcula algo, en un `.xlsx` de `salida/`.
4. Al cerrar los fundamentos, lista los artículos en que descansa cada motivo.
   De cada uno, lee sus notas en `normativa/`: si un apartado o un inciso
   destacado (en negrita) tiene nota de nulidad (del Constitucional o, en un
   reglamento, del Supremo), no se invoca como vigente; dilo. Y recuérdale
   mirar el apartado «Análisis» de cada norma en el BOE: las sentencias del
   Constitucional que no anulan (por ejemplo, las que desestiman un recurso) no
   están en `normativa/`.

### 5. Suplico y otrosíes

1. Cada pedimento se apoya en un motivo concreto. Si un pedimento no tiene
   motivo, o un motivo no tiene pedimento, dilo.
2. La cuantía, con el cálculo a la vista y de dónde sale cada sumando.

### 6. Redacción y Word

1. Una parte por entrega, empezando por los hechos. Cierra cada entrega con
   `PENDIENTE DE VERIFICAR`.
2. Estilo: `estilo/GUIA-ESTILO-PROCESAL.md`.
3. `.docx` en `salida/` con estilos reales, `[VERIFICAR]` y `[DATO]` en
   amarillo.
4. Recuérdale la auditoría en conversación nueva (`auditoria-normativa`). Lo
   firma él ante el tribunal.

## Reglas que no se saltan

- Ninguna norma, artículo ni sentencia sin documento delante. Ningún número de
  recurso, fecha o ECLI de memoria.
- Ningún dato del expediente sin el documento que lo acredita: `[DATO]`.
- Ningún plazo calculado sin el artículo delante y su confirmación.
- Los huecos se marcan, no se disimulan con una frase vaga.
