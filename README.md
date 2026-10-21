# Despacho · kit de trabajo con Claude Code

Para un despacho técnico-jurídico: peritaciones de valoración inmobiliaria,
memorias urbanísticas y escritos en el contencioso-administrativo.

Lo que en el taller vivía en un Proyecto de Claude —instrucciones, guías de
estilo, normativa fija y procedimientos— aquí es una carpeta de tu Mac. Claude
Code la lee al arrancar dentro de ella y trabaja con tus expedientes, no en una
ventana de chat aparte. **La herramienta va a tus archivos; tú no vas a la
herramienta.**

## Puesta en marcha (una vez)

Los tres pasos, explicados, están en `EMPIEZA-AQUI.md`. En corto:

```bash
git clone https://github.com/Novantin/despacho-claude-urbanismo.git ~/despacho-claude
cd ~/despacho-claude
claude
```

Y dentro de Claude Code, la primera vez: `/instalar`.

**En un Mac con macOS 12 (Monterey), Claude Code funciona sin soporte
oficial**: Anthropic pide macOS 13 o superior. Solo el de la Terminal; la
pestaña Code de la app de escritorio, en ese Mac, no sirve. En septiembre de
2026 una actualización automática lo dejó sin arrancar en macOS 12 (lo rompió
la 2.1.255 y lo arregló la 2.1.258). El kit sigue el canal `stable`, que reduce
ese riesgo pero no lo evita, y `/instalar` apunta la versión que funciona.
Claude Code se instala, y se fija si una actualización lo rompe, con un solo
procedimiento: se baja el binario de esa versión, se comprueba su huella con el
`manifest.json` oficial, se prueba sin instalar y, si arranca, se instala en
`~/.local/bin/claude`; con la versión fijada, además, se paran las
actualizaciones automáticas. Los pasos están al final de `EMPIEZA-AQUI.md`. El
instalador de una línea (`install.sh`) no sirve para esto, porque ejecuta
siempre la versión más reciente.

## Qué hay aquí

| Carpeta o archivo | Qué es |
|---|---|
| `CLAUDE.md` | Las reglas del despacho. Se aplican solas en cada conversación. **No lo edites**: se actualiza con `/actualizar`. |
| `CLAUDE.local.md` | Tus datos de firma y tus preferencias. Solo tuyo, no se sube. |
| `.claude/skills/` | Los procedimientos: `ficha-encargo`, `informe-pericial-valoracion`, `escrito-contencioso`, `memoria-urbanistica`, `auditoria-normativa`, `archicad-zonas`, `deck-desde-modelo`. |
| `.claude/commands/` | Los atajos: `/instalar`, `/actualizar`, `/actualizar-normativa`. |
| `normativa/estatal-autonomica/` | LOTURM, Ley de Suelo, Reglamento de valoraciones, LEF, LJCA y Orden ECO/805/2003, en Markdown citable, del BOE. |
| `normativa/municipal/` | Tu planeamiento, por municipio. No se sube. |
| `plantillas/` | Estructuras de la ficha pericial, la ficha urbanística y el índice del informe de valoración. Sin texto. |
| `estilo/` | Tus dos guías de estilo, pericial y procesal. No se suben. |
| `encargos/` | Una carpeta por expediente. No se suben. |
| `recursos/` | Tu plantilla de Word y documentos tuyos de referencia. No se suben. |
| `herramientas/` | Lo que usa Claude para bajar normativa del BOE y escribir Word, PowerPoint y Excel. |
| `.mcp.json` | El conector de Archicad, en solo lectura. |
| `GUIA-MODELOS-Y-CREDITOS.md` | Qué modelo usar y por qué se gasta la cuota. |
| `BITACORA.md` | Qué entró en cada actualización. |

## Actualizar cuando mejore el kit

Dentro de Claude Code: `/actualizar`. Trae las novedades y te cuenta qué ha
cambiado. Con `git`, hace `git pull` de la rama `main`, sea el repositorio
público o privado. Sin `git`, si el repositorio es público, lo trae del ZIP de
GitHub; si es privado, del ZIP o el pendrive que te pase quien te monta el kit.

Nunca da conflictos con lo tuyo: `CLAUDE.local.md`, `encargos/`,
`normativa/municipal/`, `estilo/` y `recursos/` están fuera del control de
versiones a propósito.

Para las leyes: `/actualizar-normativa` mira en el BOE si ha cambiado algún
artículo desde la descarga.

## Lo que este repositorio no tiene, a propósito

Ningún dato de ningún cliente, expediente ni finca. Las leyes son texto público
del BOE. Fuente de los datos: Agencia Estatal Boletín Oficial del Estado; texto
consolidado de carácter meramente informativo, sin valor oficial.

Lo tuyo no sale de tu Mac, salvo lo que Claude lee para trabajar, que va a
Anthropic igual que en el chat. Si eso se usa o no para entrenar modelos lo
decide un ajuste de tu cuenta, el mismo para el chat y para Claude Code:
claude.ai/settings/data-privacy-controls.

## Lo que no cambia

La IA redacta, tú firmas. Ninguna cita de norma ni de sentencia sin el documento
delante.
