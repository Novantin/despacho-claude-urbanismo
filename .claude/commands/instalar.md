---
description: Deja el despacho listo en este ordenador — coloca lo del taller, prueba que sale un Word de verdad y comprueba Archicad
---

Puesta a punto del despacho en este ordenador. Él es un profesional
técnico-jurídico, no informático: no le enseñes comandos ni le expliques qué es
un paquete. Pregunta lo mínimo,
hazlo tú y, antes de cada bloque, dile en una línea qué vas a comprobar.

## 1. La máquina

Comprueba, sin abrir ningún instalador: `sw_vers -productVersion`, `uname -m` y
`xcode-select -p`. **No ejecutes `git --version` ni `python3`** para comprobar:
sin Command Line Tools abren un diálogo de instalación.

Si el macOS es anterior al 13, díselo en dos frases y sin dramatismo: Claude
Code funciona en este Mac sin soporte oficial de Anthropic, y una actualización
ya lo dejó sin arrancar una vez. El canal `stable` reduce ese riesgo, pero no lo
evita.

Anota la versión que funciona hoy (`claude --version`): en el paso 2 se
escribe en `CLAUDE.local.md`, con la fecha. Si algún día deja de arrancar, esa
es la versión que se fija, como explica el final de `EMPIEZA-AQUI.md`. Eso lo
hace quien le montó el kit: no lo intentes tú desde aquí.

Escribe en `.claude/settings.local.json` la clave
`"syncClaudeAiSkills": false` (si el archivo existe, añade solo la clave). Así,
en esta carpeta no se cargan las skills de su cuenta de claude.ai, pensadas
para el Proyecto del chat (la del taller, si la subió, se llama igual que
`informe-pericial-valoracion`), ni las `docx`, `pptx` y `xlsx` de Anthropic, que
piden herramientas que este kit no usa. En el chat siguen igual. Díselo en una
línea.

## 2. Coloca lo que traiga del taller

Si existe la carpeta `entrega/`:

| Lo que viene en `entrega/` | Dónde va |
|---|---|
| `CLAUDE.local.md` | raíz |
| `GUIA-ESTILO-PERICIAL.md`, `GUIA-ESTILO-PROCESAL.md` | `estilo/` |
| carpetas de expediente | `encargos/` |

Muévelos con `mv`, borra la carpeta vacía con `rmdir` y confírmalo en dos
líneas. Si queda algo que no está en la tabla, déjalo donde está, no borres la
carpeta y díselo. No abras los documentos para resumirlos.

Si no existe `CLAUDE.local.md`, pregunta lo mínimo, de una en una: nombre como
firma; titulaciones y colegiaciones (colegio y número); ciudad y ámbito donde
ejerce; tipografía y tamaño de sus documentos de Word. Escríbelo y sigue. Si
existe pero tiene algún `[DATO]`, pregunta solo esos. Nada de DNI ni datos
bancarios. Escribe también la versión de Claude Code anotada en el paso 1.

## 3. Word: lo que de verdad importa

Todo el despacho depende de poder generar `.docx` con estilos reales. Cómo se
generan en este ordenador está en `herramientas/README.md`: léelo y sigue ese
orden.

1. Si falta la herramienta, dile qué es en una frase llana y **pide permiso
   antes de instalar nada**.
2. Genera `prueba-word.docx` en la raíz: una página con Título 1, Título 2, un
   párrafo justificado, una tabla de dos columnas, un texto resaltado en
   amarillo y un índice automático.
3. Que lo abra en Word y confirme cuatro cosas: que se abre, que los títulos
   aparecen en el panel de estilos, que puede **editarlo y guardarlo**, y que el
   índice se actualiza.
4. Si abre pero no deja editar ni guardar, no es el kit: es la versión de Office.
   Que mire Word → Acerca de Word y te diga qué pone, y se lo pase a quien le
   montó el kit.

**No pases de este punto hasta que el Word salga bien.** Después, una prueba
rápida igual con un `.xlsx` y un `.pptx`.

## 4. Archicad

1. ¿Existe `~/archicad-mcp/.venv/bin/archicad-mcp`? Si no, díselo en una frase:
   el conector no está instalado, los pasos están en
   `.claude/skills/archicad-zonas/INSTALACION.md` y se hacen con calma, con red
   y con quien le montó el kit. **No lo instales ahora sin su permiso expreso.**
   Mientras tanto vale la versión «exporta y lee».
2. Si existe, mira la primera línea de ese archivo: tiene que ser una ruta
   absoluta a un `python`, sin `realpath`.
3. Avísale de que Claude Code le preguntará si aprueba el servidor
   `archicad-mcp` de este proyecto: que diga que sí.
4. Con Archicad abierto y un proyecto cargado, ejecuta `TestConnection` y dile
   qué responde: versión de Archicad, de Tapir e idioma. Si no responde, no se
   pelea: versión «exporta y lee».

## 5. Qué tienes disponible

Tabla corta, con una columna «para qué te sirve» en su idioma:

- Skills: `ficha-encargo`, `informe-pericial-valoracion`,
  `escrito-contencioso`, `memoria-urbanistica`, `auditoria-normativa`,
  `archicad-zonas`, `deck-desde-modelo`.
- Comandos: `/actualizar`, `/actualizar-normativa`.
- Si el conector de Archicad está activo.

No le ofrezcas más conectores. Si pregunta, una frase: se añaden cuando un
expediente real los pida.

## 6. Carpetas

Tabla corta de qué hay y qué falta:

- `normativa/estatal-autonomica/`: las seis leyes y la fecha de descarga de su
  cabecera.
- `normativa/municipal/`: si está vacía, dile que ahí van, por municipio, la
  ficha del ámbito y las normas del plan de cada expediente, en PDF con texto
  seleccionable o en Markdown. No te ofrezcas a buscarlas.
- `estilo/`, `encargos/`, `recursos/`.

## 7. Cierre

Cinco líneas: qué ha quedado montado y qué puede pedirte a partir de ahora, con
sus palabras —ficha del encargo, informe de valoración, demanda, memoria,
auditoría, superficies de Archicad, deck—.

Y la última: la IA redacta, tú firmas.
