# Modelos y cuota

Las dos dudas de siempre: *«¿cómo sé lo que llevo gastado?»* y *«¿qué modelo
uso?»*.

## Cómo se gasta

Pagas al mes, pero la cuota se mide en **dos ventanas a la vez**:

- **Una ventana de 5 horas**, que arranca cuando empiezas a usar Claude y se
  renueva al cumplirse. Existe para que una tarde intensa no agote la semana.
- **Un límite semanal**, que es la bolsa grande.

**Las dos se comparten** entre la web, la app de escritorio y Claude Code. Lo
que gastes aquí, no lo tienes en el chat, y al revés. Anthropic no publica un
número de mensajes: depende de lo que leas y de cómo trabajes.

**Dónde mirarlo:** en Claude Code, escribe `/usage`. En la web, en Ajustes, la
página de uso: sesión actual y límite semanal.

Si se acaba: esperas a que se renueve, o sigues con créditos de uso, que se
pagan aparte. Eso lo decides tú, no Claude.

## Qué consume

Consume **leer y pensar**, no solo escribir. Según la ayuda de Claude, suben el
consumo el tamaño de los archivos, la longitud de la conversación, el modelo, el
nivel de esfuerzo y las tareas que ejecutan código o crean archivos.

Las reglas que más ahorran:

1. **El texto, lo más crudo posible.** Mejor `.md` que Word, y Word que PDF.
   Las seis leyes del despacho ya están en Markdown: en total pesan la mitad que
   sus PDF del BOE, y sin maquetación que navegar.
2. **Se convierte una vez.** Si pasas un PDF a Markdown, se guarda en la carpeta
   del expediente y se usa siempre ese.
3. **Se busca el artículo, no se lee la ley.** Claude busca el encabezado del
   artículo y lee ese trozo. Pedirle «léete la LOTURM» gasta la cuota sin
   necesidad.
4. **Una conversación por tarea.** Al terminar una, `/clear`. Una conversación
   larga relee todo lo anterior en cada turno, y además así el revisor no hereda
   lo que pensó el redactor.

## Qué modelo usar

Con Pro tienes Opus, Sonnet y Haiku. Fable solo con créditos de uso, es decir,
pagando aparte.

| Modelo | Para qué, en tu caso |
|---|---|
| **Haiku** | Casi nunca. |
| **Sonnet** | Lo mecánico: pasar una tabla a Excel, renombrar, buscar un dato en una carpeta. |
| **Opus** | **El tuyo por defecto.** Leer expedientes y redactar informes, demandas y memorias. |
| **Fable** | Solo con créditos de uso. Para algo que de verdad lo pida y vayas a firmar, y si lo decides tú. |

Se cambia con `/model`. Y aparte está el **esfuerzo** (`/effort`): bajo va rápido
y gasta poco; alto piensa más y gasta más. Un esfuerzo alto en un modelo pequeño
sigue siendo un modelo pequeño.

**La regla práctica:** el índice y la auditoría, con esfuerzo alto; pasar a
Word o a Excel, con esfuerzo bajo.

## Una cosa de este Mac

Claude Code va en el canal `stable`, que no siempre lleva la última versión.
Según su documentación, un modelo recién salido puede necesitar una versión más
nueva que la del canal `stable`: si un modelo nuevo aparece en la web y aquí no,
es eso. Se esperan unos días o se pregunta. Si en este Mac se ha fijado una versión
(final de `EMPIEZA-AQUI.md`), los modelos nuevos no llegan hasta que se pruebe y
se fije una más reciente.
