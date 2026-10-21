# Normativa

Dos carpetas, con reglas distintas:

| Carpeta | Qué va | ¿Se sube al repositorio? |
|---|---|---|
| `estatal-autonomica/` | Leyes y reglamentos que valen para todos los expedientes, en Markdown, sacados del BOE | **Sí**: son texto público del BOE |
| `municipal/` | Planeamiento y ordenanzas de cada municipio, y lo que solo esté en el BORM | **No**: es tuyo y depende de cada expediente |

## `estatal-autonomica/` — las seis normas del despacho

Descargadas el **19-10-2026** de la API oficial de legislación consolidada del
BOE. El 21-10-2026 se comprobó, artículo por artículo, que ninguna había
cambiado desde la descarga, y se regeneraron desde esa misma descarga para
conservar en las notas las referencias «Ref. BOE-…» (el texto de los artículos
no cambió).

| Archivo | Norma | Identificador BOE | Última actualización en el BOE |
|---|---|---|---|
| `LOTURM-Ley-13-2015-Murcia.md` | Ley 13/2015, de ordenación territorial y urbanística de la Región de Murcia | BOE-A-2015-4790 | 14-07-2026 |
| `TRLSRU-RDLeg-7-2015.md` | Real Decreto Legislativo 7/2015, texto refundido de la Ley de Suelo y Rehabilitación Urbana | BOE-A-2015-11723 | 13-10-2026 |
| `RD-1492-2011-Reglamento-valoraciones.md` | Real Decreto 1492/2011, Reglamento de valoraciones de la Ley de Suelo | BOE-A-2011-17629 | 19-12-2025 |
| `LEF-1954-Expropiacion-Forzosa.md` | Ley de 16 de diciembre de 1954, de Expropiación Forzosa | BOE-A-1954-15431 | 16-12-2025 |
| `LJCA-Ley-29-1998.md` | Ley 29/1998, reguladora de la Jurisdicción Contencioso-administrativa | BOE-A-1998-16718 | 05-03-2026 |
| `ECO-805-2003-Valoracion-inmuebles.md` | Orden ECO/805/2003, normas de valoración de bienes inmuebles | BOE-A-2003-7253 | 18-12-2025 |

Cada archivo dice en su cabecera de dónde sale, cuándo se descargó, a qué fecha
es vigente el texto y la fuente de los datos. Solo trae la última redacción de
cada artículo; las notas del BOE van como `> [Nota BOE]` o `> Téngase en
cuenta…`, con su `Ref. BOE-…`. El texto es el del BOE tal cual: lo único añadido
es la cabecera.

### Cómo se cita

- Artículos: `###### Artículo 36.` En la Ley de Expropiación Forzosa, en letra:
  `###### Artículo cincuenta y dos.`
- Disposiciones: `## Disposición adicional séptima.` Apartados: `**1.**`
- Las fórmulas del Reglamento de valoraciones y de la Orden ECO/805/2003 son
  imágenes en el BOE y aquí están transcritas a mano a LaTeX (`$$…$$`):
  **comprobar contra el BOE las que se vayan a citar.**

### Cómo se refresca

`/actualizar-normativa` en Claude Code. Comprueba en el BOE la fecha de cada
artículo, dice cuáles han cambiado y vuelve a generarlas con
`herramientas/boe_a_markdown.py`. También baja una norma nueva o la redacción
que estaba vigente en una fecha concreta.

### Fuente y valor

Fuente de los datos: Agencia Estatal Boletín Oficial del Estado
(https://www.boe.es). Texto consolidado de carácter meramente informativo, sin
valor oficial: lo que vaya a un escrito se cita por la norma y su artículo, y se
comprueba contra el BOE.

Las declaraciones de nulidad —del Constitucional sobre una ley, o del Supremo
sobre un reglamento, como el de valoraciones— sí están: van como nota del
artículo. Cuando la nota habla del «inciso destacado», es el texto en
negrita dentro de ese apartado, y no se cita como vigente. Otras sentencias del
Tribunal Constitucional —por ejemplo, las que desestiman un recurso— no están
aquí, sino en el apartado «Análisis» de la página de la norma en el BOE
(`https://www.boe.es/buscar/doc.php?id=<identificador>`): antes de basar un
motivo en un artículo, se mira ahí.

## `municipal/` — lo tuyo, por municipio

Ver `municipal/README.md`.
