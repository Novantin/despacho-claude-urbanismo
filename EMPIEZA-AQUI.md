# Empieza aquí

En el taller montamos el despacho en tu cuenta de Claude: el Proyecto, las
guías de estilo, las leyes y la skill. Esto es lo mismo en forma de carpeta de
tu Mac, para trabajar con Claude Code dentro de tus expedientes. Tres pasos.

## Antes, una vez: Claude Code

Lo deja instalado quien te monta el kit, con los pasos del final de esta
página. No se usa el instalador de una línea de la web de Claude
(`curl … install.sh | bash`): ejecuta siempre la versión más reciente, aunque
se le pida otra, y en tu Mac hay que probar antes la versión que se instala.

Cuando esté, comprueba en una ventana nueva de la Terminal que responde:
`claude --version`.

**Dicho claro: en un Mac con macOS 12 (Monterey), Claude Code funciona sin
soporte oficial.** Anthropic pide macOS 13 o superior. Hoy funciona en Macs
como el tuyo, pero en septiembre de 2026 una actualización automática lo dejó
sin arrancar en macOS 12, hasta que salió el arreglo. El kit sigue el canal
`stable`, que no siempre lleva la última versión: reduce el riesgo, pero no lo
evita, porque un fallo que solo afecte a macOS 12 puede llegar también a
`stable`. Por eso cada versión se prueba en tu Mac antes de instalarla, se
apunta la que funciona y, si un día falla, se fija esa (al final de esta
página). Es el de la Terminal: la pestaña Code de la app de escritorio no sirve
en tu Mac.

## 1. Traer la carpeta

Con `git`, si tu Mac tiene las herramientas de desarrollo de Apple (lo dice
`xcode-select -p`: si responde con una ruta, las tiene; no lo compruebes con
`git --version`, que si no las tiene abre su instalador):

```bash
git clone https://github.com/Novantin/despacho-claude-urbanismo.git ~/despacho-claude
```

Si el repositorio es privado, el acceso lo deja preparado quien te monta el kit.

Sin `git`: te la dejo copiada en `~/despacho-claude` desde un pendrive o, si el
repositorio es público, la bajas en ZIP desde su página en GitHub (botón
*Code* → *Download ZIP*), la descomprimes y la carpeta que sale la llamas
`despacho-claude`, dentro de tu carpeta de usuario. Funciona igual; solo cambia
cómo se actualiza, y `/actualizar` ya sabe las dos formas.

## 2. Meter lo tuyo

Copia dentro de `~/despacho-claude` la carpeta **`entrega`** que te llevas del
taller, tal cual, sin abrirla ni ordenarla. Lleva tus datos de firma y tus dos
guías de estilo.

## 3. Arrancar

```bash
cd ~/despacho-claude
claude
```

Y dentro, la primera vez:

```
/instalar
```

Coloca cada cosa en su sitio, comprueba que sale un Word de verdad y que
Archicad contesta, apunta la versión de Claude Code que funciona en tu Mac y te
dice qué puedes pedirle. Para trabajar, a partir de ahí, solo los dos primeros
comandos: `cd ~/despacho-claude` y `claude`.

---

## Cuando te avise de que hay novedades

```
/actualizar
```

Trae las mejoras del kit y te cuenta qué ha cambiado. Tus cosas no se tocan
nunca.

## Si un día Claude Code no arranca

No reinstales nada a ciegas: reinstalar no lo arregla, porque el instalador
ejecuta siempre la versión más reciente, que puede ser justo la que falla.
Avísame. Lo que se hace es fijar la versión que funcionaba, la que `/instalar`
dejó apuntada en `CLAUDE.local.md`. Los pasos están al final de esta página;
los hace quien te monta el kit.

## Las tres reglas que no cambian

1. Una conversación por tarea. Redactar y revisar, en conversaciones distintas.
2. Documento delante siempre. Lo que no está en la carpeta, se lo inventa con
   muy buena letra.
3. Lo que firmas, lo lees entero. **La IA redacta, tú firmas.**

---

## Para quien monta el kit: instalar o fijar Claude Code en macOS 12

Un solo procedimiento, para la primera instalación y para volver a una versión
que funciona. **No se ha ejecutado en un Monterey real.**

**Por qué no `install.sh`.** Leído como texto el 22-10-2026,
`https://claude.ai/install.sh` redirige a `bootstrap.sh`, que baja y ejecuta
siempre la versión `latest` y solo después le pide que instale la indicada
(`bash -s stable` o un número): la versión no queda fijada ni probada. Si la
`latest` no arranca en macOS 12, fallan a la vez la instalación y la vuelta
atrás. Aquí se baja el binario de la versión que se quiere, con la ruta y la
huella (SHA-256) de su `manifest.json`, las mismas que usa `bootstrap.sh`, y se
prueba antes de instalar nada.

**Versiones a 22-10-2026** (`downloads.claude.ai`): `stable` 2.1.306
(compilada el 21-10) y `latest` 2.1.307. Ninguna está comprobada en macOS 12.
La última confirmada por usuarios en un Mac Intel con macOS 12.7.6 es la
**2.1.280** (septiembre de 2026). Admite Opus 5.5: fijarla deja sin los modelos
siguientes, no sin el actual.

**Pega las líneas de una en una**, todas en la misma ventana de la Terminal
(las variables `D`, `V` y `S` solo existen en esa ventana), y lee la respuesta
de cada una antes de pegar la siguiente. Los bloques no llevan comentarios a
propósito: en la Terminal de macOS (zsh), un `#` al final de una línea pegada
no es un comentario y estropea el comando.

### 1. Qué versión

```bash
D=https://downloads.claude.ai/claude-code-releases
V=$(curl -fsSL $D/stable); echo $V
```

Para fijar una versión, en lugar de la segunda línea: `V=2.1.280`, o la que
esté apuntada en `CLAUDE.local.md` como la que funciona en este Mac.

### 2. Bajarla y probarla, sin instalar nada

```bash
S=$(curl -fsSL "$D/$V/manifest.json" | grep -A3 '"darwin-x64"' | sed -n 's/.*"checksum": *"\([0-9a-f]\{64\}\)".*/\1/p'); echo $S
curl -fL -o ~/claude-$V "$D/$V/darwin-x64/claude"
[ -n "$S" ] && [ "$(shasum -a 256 ~/claude-$V | cut -d' ' -f1)" = "$S" ] && chmod +x ~/claude-$V && echo HUELLA CORRECTA
~/claude-$V --version
```

La primera línea tiene que enseñar una huella de 64 caracteres. La descarga es
de unos 280 MB (la 2.1.280, unos 225 MB). Si no sale `HUELLA CORRECTA`, el
archivo no se ha marcado como ejecutable: `rm ~/claude-$V` y no sigas.

Si `--version` contesta con el número, esa versión arranca en este Mac: paso 3.
Si no contesta, `rm ~/claude-$V` y vuelve al paso 1 con `V=2.1.280`. Si esa
tampoco arranca, Claude Code no vale en este Mac: hace falta otro con macOS 13
o posterior.

### 3. Instalar

Siguiendo `stable`, lo normal:

```bash
~/claude-$V install stable
rm ~/claude-$V
~/.local/bin/claude --version
```

Con la versión fijada, y después el paso 4 antes de abrir ninguna sesión:

```bash
~/claude-$V install $V
rm ~/claude-$V
~/.local/bin/claude --version
```

`install` deja el lanzador en `~/.local/bin/claude`. Si al acabar avisa de que
`~/.local/bin` no está en el `PATH`, pega la línea que propone y cierra y abre
la Terminal. Después (con la versión fijada, después del paso 4), una sesión
corta en una carpeta vacía, `cd "$(mktemp -d)" && ~/.local/bin/claude`: inicia
sesión con su cuenta y `/exit`. La versión que funciona, con la fecha, va a `CLAUDE.local.md`
(`/instalar` la apunta).

### 4. Solo con la versión fijada: parar las actualizaciones

Antes de volver a abrir `claude`, para que no se actualice sola en el siguiente
arranque:

```bash
[ -e ~/.claude/settings.json ] && echo "YA EXISTE: añade la clave a mano" || { mkdir -p ~/.claude && printf '{"env":{"DISABLE_AUTOUPDATER":"1"}}\n' > ~/.claude/settings.json; }
```

Si ya existía, ábrelo con `nano ~/.claude/settings.json` y añade
`"DISABLE_AUTOUPDATER": "1"` dentro de `"env"` (o `"env": {"DISABLE_AUTOUPDATER": "1"}`
si no hay `env`), cuidando las comas. Se comprueba con
`~/.local/bin/claude doctor`, que debe decir
`Auto-updates: disabled (set by env: DISABLE_AUTOUPDATER)`.

El precio: no llegan los modelos nuevos que pidan una versión más reciente de
Claude Code. Lo decide él.

### Probar una versión nueva o volver a `stable`

Pasos 1 y 2 tal cual, con la `stable` del día: se prueba sin instalar nada. Si
arranca, quita `DISABLE_AUTOUPDATER` de `~/.claude/settings.json` y sigue con
el paso 3, «siguiendo `stable`». Si no arranca, `rm ~/claude-$V` y todo sigue
como estaba.
