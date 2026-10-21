---
description: Comprueba en el BOE si ha cambiado algún artículo de las leyes del despacho, y baja una norma nueva o la redacción de una fecha concreta
---

Mantenimiento de `normativa/estatal-autonomica/` con la API oficial de
legislación consolidada del BOE: solo lectura, sin clave, y solo para normas que
el BOE consolida (estatales y leyes y decretos-ley autonómicos). Todo pasa por
`herramientas/boe_a_markdown.py`.

Tenerlas al día es, sobre todo, trabajo de quien mantiene el kit: las leyes
refrescadas le llegan con `/actualizar`. En su Mac esto sirve para dos cosas:
saber si ha cambiado algo desde la descarga y bajar la redacción de una fecha
concreta a la carpeta de un expediente (paso 4).

## 0. Con qué se ejecuta

- Si `xcode-select -p` responde con una ruta: `python3 herramientas/boe_a_markdown.py …`
- Si no, pero existe `~/.local/bin/uv` (lo deja el conector de Archicad):
  `~/.local/bin/uv run --no-project --managed-python --python 3.13 herramientas/boe_a_markdown.py …`
- Si no hay ninguno de los dos, **no instales nada**. Dile que esto lo hace quien
  mantiene el kit, y que las leyes refrescadas le llegan con `/actualizar`.

No ejecutes `python3` para probar si existe: sin Command Line Tools abre un
diálogo de instalación.

## 1. ¿Ha cambiado algo?

```bash
python3 herramientas/boe_a_markdown.py --comprobar normativa/estatal-autonomica/*.md
```

Compara la fecha de actualización de cada artículo en el índice del BOE con la
fecha de descarga de la cabecera de cada archivo. Cuéntale el resultado en
lenguaje llano: qué ley, qué artículos y desde cuándo. Si no ha cambiado nada,
una línea con la fecha.

Si sale un `AVISO` (el texto no ha cambiado, pero sí la ficha de la norma), dale
el enlace y dile que mire el apartado «Análisis»: ahí el BOE anota, por ejemplo,
las sentencias del Constitucional sobre un artículo. No las resumas de memoria.

## 2. Si ha cambiado algo

- **Esta carpeta es un clon de `git`** (tiene `.git`): no reemplaces las leyes
  del repositorio aquí, que el siguiente `/actualizar` chocaría. Dile qué ha
  cambiado y que la versión refrescada le llega con `/actualizar` cuando quien
  mantiene el kit la publique. Si la necesita ya para un expediente, baja la
  redacción vigente a la carpeta de ese expediente (paso 4).
- **No es un clon** (llegó por pendrive o ZIP), **o quien lo ejecuta mantiene el
  kit**: vuelve a generar la ley con `-o` sobre su archivo. El script no
  sobrescribe: deja la versión nueva al lado, con extensión `.nuevo`. Enséñale
  con `diff` qué artículos cambian, y con su visto bueno reemplaza el archivo
  con `mv`. Quien mantiene el kit hace después el commit a mano, revisando
  `git status`, y añade una entrada en `BITACORA.md`.

En el Reglamento de valoraciones y en la Orden ECO/805/2003, el script repone
las fórmulas transcritas a mano. Si sale alguna `[IMAGEN SIN TRANSCRIBIR]`, es
una fórmula nueva: hay que transcribirla mirando el BOE.

## 3. Añadir una norma nueva

Él te da el enlace del BOE (`…act.php?id=BOE-A-…`) o el identificador. Genérala
en `normativa/estatal-autonomica/` con un nombre como los demás
(`SIGLA-ANNO-tema.md`) y comprueba que salen los artículos como encabezados.
Si el BOE la marca derogada o anulada, el script avisa: díselo.

## 4. La redacción de una fecha concreta

Para un expediente que se refiere a otra fecha (la de la valoración, la del acto
impugnado):

```bash
python3 herramientas/boe_a_markdown.py BOE-A-… --a-fecha AAAA-MM-DD -o encargos/<expediente>/entrada/<LEY>-vigente-AAAA-MM-DD.md
```

Va a la carpeta del expediente, no a `normativa/`.

## Lo que no se automatiza

- **BORM**: lo que el BOE no consolida (decretos, órdenes, aprobaciones de
  planeamiento) se baja a mano en PDF y va al expediente, o a
  `normativa/municipal/<municipio>/` si es planeamiento.
- **Jurisprudencia**: cada sentencia, a mano y en PDF, a
  `encargos/<expediente>/entrada/jurisprudencia/`. Nada de descargas masivas ni
  de herramientas que las automaticen.

Recuerda la fuente al citar: «Fuente de los datos: Agencia Estatal Boletín
Oficial del Estado». El texto consolidado no tiene valor jurídico oficial.
