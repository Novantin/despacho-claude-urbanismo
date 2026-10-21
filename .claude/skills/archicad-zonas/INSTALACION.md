# Instalar el conector de Archicad (una vez, con red, 15-20 minutos)

Para un Mac Intel con macOS 12 (Monterey) y Archicad 27. Comprobado contra el
código y la documentación de cada pieza el 21-10-2026. **No se ha ejecutado en
un Monterey real:** si algo falla, no se pelea; se usa la versión «exporta y
lee» de la skill.

Lo hace quien monta el kit, con él delante, o él siguiendo esto paso a paso.
Claude no instala nada de aquí sin permiso expreso en cada paso. Nada de esta
ruta pide contraseña de administrador: todo queda en su carpeta de usuario. Si
algo la pide, para.

El kit ya trae `.mcp.json` apuntando a `~/archicad-mcp/.venv/bin/archicad-mcp`
en modo `readonly`. Si el servidor queda en esa ruta, Claude Code lo encuentra
sin tocar nada.

Las piezas, fijadas:

| Pieza | Versión |
|---|---|
| Tapir, add-on para Archicad 27 Mac | **1.7.2** (si no carga, 1.7.1; la 1.5.9 solo como último recurso) |
| uv | **0.13.4** |
| Servidor `lgradisar/archicad-mcp` | commit **13b8645cf9d6c59543a9c2f6b0021ac76e2b0b36** (= tag v1.1), desde su ZIP |
| Python | **3.13**, gestionado por uv |
| Modo del conector | `ARCHICAD_MCP_MODE=readonly` |

**Pega las líneas de una en una.** Los bloques no llevan comentarios a
propósito: en la Terminal de macOS (zsh), un `#` al final de una línea pegada
no es un comentario y estropea el comando. Las URL no se teclean: se copian de
aquí.

## 0. Comprobaciones (no abren ningún instalador)

```bash
sw_vers -productVersion
uname -m
whoami
xcode-select -p
```

Tienen que dar 12.7.6, x86_64 y su usuario (NOMBRE, para el JSON del paso 4).
`xcode-select -p` dice si hay Command Line Tools: una ruta es que sí, un error
es que no, y las dos cosas valen, porque esta ruta no las necesita. No uses
`git --version` ni `python3` para comprobar: sin Command Line Tools, abren el
diálogo de instalación.

## 1. Tapir 1.7.2

Primero mira en Archicad, en el Gestor de complementos, si ya tiene Tapir. Si es
1.7.1 o posterior, sáltate este paso. Si es más antiguo, quítalo de la lista
antes de añadir el 1.7.2, para que no haya dos.

```bash
mkdir -p ~/Documents/Tapir && cd ~/Documents/Tapir
curl -L -O https://github.com/ENZYME-APD/tapir-archicad-automation/releases/download/1.7.2/TapirAddOn_AC27_Mac.zip
unzip -q TapirAddOn_AC27_Mac.zip
```

Tiene que salir `TapirAddOn_AC27_Mac.bundle`. Si `unzip` protesta:
`ditto -x -k TapirAddOn_AC27_Mac.zip .` (o doble clic en Finder).

En Archicad: Opciones → Gestor de complementos → Editar lista de complementos
disponibles → Añadir → `~/Documents/Tapir/TapirAddOn_AC27_Mac.bundle` →
Aceptar (en inglés: *Options → Add-On Manager → Edit List of Available Add-Ons
→ Add*; los nombres en español no están comprobados). Si no aparece cargado,
reinicia Archicad. No muevas ni borres `~/Documents/Tapir`: Archicad lo carga
de ahí.

Si no carga, la 1.7.1 (misma URL cambiando la versión). La 1.5.9 solo como
último recurso: devuelve mal los nombres de categoría con tilde.

## 2. uv 0.13.4

```bash
curl -LsSf https://astral.sh/uv/0.13.4/install.sh | sh
~/.local/bin/uv --version
```

Tiene que decir `uv 0.13.4`. El instalador deja `uv` en `~/.local/bin` y no
usa ni `git` ni `realpath`. Aquí se llama siempre por su ruta completa, así que
no hace falta reabrir la Terminal.

## 3. El servidor, desde el ZIP del commit, con Python 3.13

```bash
export UV_PYTHON_PREFERENCE=only-managed
cd ~
curl -L -o archicad-mcp.zip https://github.com/lgradisar/archicad-mcp/archive/13b8645cf9d6c59543a9c2f6b0021ac76e2b0b36.zip
unzip -q archicad-mcp.zip
mv archicad-mcp-13b8645cf9d6c59543a9c2f6b0021ac76e2b0b36 archicad-mcp
rm archicad-mcp.zip
cd ~/archicad-mcp
~/.local/bin/uv python install 3.13
~/.local/bin/uv python pin 3.13
~/.local/bin/uv sync --frozen
```

- **El `export` va primero**, antes de `uv python install` y `uv python pin`:
  así uv solo usa los Python que gestiona él y no prueba `/usr/bin/python3`, que
  sin Command Line Tools abre su instalador. Si abres otra ventana de la
  Terminal, repite el `export`.
- **El `pin 3.13` es imprescindible.** Sin él, uv 0.13 coge Python 3.15, y para
  3.15 el lockfile no tiene paquetes Intel de cffi, PyYAML, pydantic-core y
  rpds-py: intentaría compilarlos y fallaría.
- `sync --frozen` usa el `uv.lock` tal cual; descarga Python y las
  dependencias.

Comprobaciones:

```bash
~/archicad-mcp/.venv/bin/python -c "import cryptography, fastmcp, archicad_mcp.server; print(cryptography.__version__)"
head -1 ~/archicad-mcp/.venv/bin/archicad-mcp
ARCHICAD_MCP_MODE=readonly ~/archicad-mcp/.venv/bin/python -c "from archicad_mcp.server import create_server; create_server(); print('ok')"
```

La primera tiene que dar `45.0.6`. La segunda, una línea que empieza por
`#!/Users/NOMBRE/archicad-mcp/.venv/bin/python` y no dice `realpath`. La
tercera, `ok`.

**No muevas ni borres `~/archicad-mcp`:** la instalación es editable y apunta a
esa carpeta, y el `.mcp.json` del kit también.

## 4. App de escritorio de Claude (si se usa también ahí)

**Cmd+Q en Claude** (cerrar la ventana no basta). Después, en la Terminal, este
bloque (se pega entero) escribe la entrada en
`~/Library/Application Support/Claude/claude_desktop_config.json`. Respeta lo
que ya hubiera, guarda antes una copia `…antes-de-archicad` y pone la ruta
absoluta sin teclear el usuario:

```bash
~/archicad-mcp/.venv/bin/python - <<'EOF'
import json, os, shutil
p = os.path.expanduser("~/Library/Application Support/Claude/claude_desktop_config.json")
cfg = {}
if os.path.exists(p):
    shutil.copy2(p, p + ".antes-de-archicad")
    texto = open(p, encoding="utf-8").read().strip()
    cfg = json.loads(texto) if texto else {}
cfg.setdefault("mcpServers", {})["archicad-mcp"] = {
    "command": os.path.expanduser("~/archicad-mcp/.venv/bin/archicad-mcp"),
    "args": [],
    "env": {"ARCHICAD_MCP_MODE": "readonly"},
}
os.makedirs(os.path.dirname(p), exist_ok=True)
with open(p, "w", encoding="utf-8") as f:
    json.dump(cfg, f, indent=2, ensure_ascii=False)
print(open(p, encoding="utf-8").read())
EOF
```

Lo que tiene que quedar, si lo editas a mano, cambiando NOMBRE por lo que dio
`whoami`. Si el archivo no existe, entero; si ya tiene `mcpServers`, solo la
entrada `"archicad-mcp": {…}` dentro, cuidando las comas:

```json
{"mcpServers":{"archicad-mcp":{"command":"/Users/NOMBRE/archicad-mcp/.venv/bin/archicad-mcp","args":[],"env":{"ARCHICAD_MCP_MODE":"readonly"}}}}
```

Ruta absoluta siempre: ni `~` ni `${HOME}` en este archivo. (El `.mcp.json`
del kit sí usa `${HOME}`, porque es para Claude Code, que expande variables en
`command`.)

Abre Claude otra vez. Registros de errores: `~/Library/Logs/Claude/mcp.log` y
`~/Library/Logs/Claude/mcp-server-archicad-mcp.log`.

En su Mac, **no actualices ni reinstales la app de escritorio**: la versión
actual pide macOS 13 y no abriría.

## 5. Claude Code (este kit)

Nada que tocar: `.mcp.json` ya apunta a esa ruta. La primera vez, Claude Code
pregunta si aprueba el servidor `archicad-mcp` del proyecto: sí. Con `/mcp` se ve
si está conectado.

## 6. Prueba

1. Archicad abierto **con un proyecto suyo** y Tapir en el Gestor de
   complementos.
2. **En la Terminal, sin Claude** (separa los fallos de Archicad de los de
   Claude):

   ```bash
   ~/archicad-mcp/.venv/bin/python -c "from archicad_mcp.tools.custom_tools import connection_info; print(connection_info())"
   ```

   Tiene que devolver `port`, `archicad_version`, `archicad_build`,
   `language`, `tapir_installed` (1.7.2) y `tapir_definitions` (1.5.9). Que no
   coincidan las dos de Tapir es normal: los comandos de lectura de zonas tienen
   la misma entrada en las dos versiones.
3. **En Claude**, conversación nueva: «comprueba la conexión con Archicad».
   Tiene que dar lo mismo. `language` dice si su Archicad está en español.
4. Una lectura corta: «¿cuántas zonas tiene el modelo?».

## 7. Más adelante: superficies como número (sin probar)

El conector trae las definiciones de comandos de Tapir 1.5.9, y en ellas la
superficie de una zona llega como texto formateado. Tapir 1.7.2 añade
`GetQuantitiesOfElements`, que la da como número en m² (medida, neta y
calculada). Para verla hay que actualizar las definiciones, según el README del
servidor:

```bash
cd ~/archicad-mcp && ~/.local/bin/uv run --frozen scripts/update_tapir.py 1.7.2
```

Después, Cmd+Q y abrir de nuevo la app de Claude, o `/mcp` → reconectar en
Claude Code. Nadie lo ha probado en este Mac: se hace con calma, nunca delante
de un cliente, y si algo deja de funcionar se repite el paso 3 desde el ZIP.

## Si algo falla

| Síntoma | Qué hacer |
|---|---|
| Salta la ventana de instalar las herramientas de línea de comandos | **Cancelar.** Algo ha llamado a `git` o a `python3`. Nada de esta ruta las necesita |
| `mv: … Directory not empty`, o queda una carpeta dentro de otra | Restos de un intento anterior: `rm -rf ~/archicad-mcp` y repetir el paso 3 desde el `curl` |
| `uv sync` intenta compilar (`Failed to build` cffi, pyyaml, pydantic-core o rpds-py) | Falta el pin: `cat ~/archicad-mcp/.python-version` tiene que decir `3.13`. `uv python pin 3.13`, `rm -rf ~/archicad-mcp/.venv` y `uv sync --frozen` otra vez |
| `cryptography` no es 45.0.6 | Se instaló sin el lockfile. Borrar `.venv` y repetir con `--frozen` |
| `head -1` enseña `realpath` | Borrar `.venv` y repetir; si vuelve, plan B |
| «Archicad is not running or the Tapir add-on is not loaded» | Abrir un proyecto en Archicad y mirar que Tapir esté en el Gestor |
| «is not available in the installed Tapir add-on» | Tapir más antiguo que las definiciones (1.5.9): instalar la 1.7.2 |
| La Terminal conecta, pero la app no ve el conector | Cmd+Q de verdad y abrir. Mirar `mcp.log`. Validar el JSON: `~/archicad-mcp/.venv/bin/python -m json.tool ~/Library/Application\ Support/Claude/claude_desktop_config.json` |
| `ENOENT` o «spawn …» en `mcp.log` | La ruta del `command` está mal (NOMBRE, `~` o `${HOME}`). Repetir el paso 4 |

## Plan B, si fallan `uv` o `uv sync`

Instalador oficial de Python 3.13.17 (según python.org, para macOS 10.13 o
posterior; pide la contraseña de administrador, que teclea él):
https://www.python.org/ftp/python/3.13.17/python-3.13.17-macos11.pkg

```bash
mkdir -p ~/archicad-mcp
/usr/local/bin/python3.13 -m venv --clear ~/archicad-mcp/.venv
~/archicad-mcp/.venv/bin/python -m pip install "cryptography<49" "archicad-mcp @ https://github.com/lgradisar/archicad-mcp/archive/13b8645cf9d6c59543a9c2f6b0021ac76e2b0b36.zip"
```

Así el ejecutable queda en la misma ruta y ni `.mcp.json` ni el JSON de la app
cambian. `cryptography<49` porque desde la 49 no hay paquetes para Mac Intel.
Sin lockfile entran versiones que nadie ha probado juntas.

## Plan C

La versión «exporta y lee» de la skill. Sin instalar nada.

## No usar

- `uvx` (en macOS 12 necesita `realpath` y `git`, y resolvería una
  `cryptography` sin paquete para Intel).
- `uvx archicad-mcp` ni `pip install archicad-mcp` a secas: en PyPI,
  `archicad-mcp` es **otro proyecto**, no el de lgradisar.
- `uv tool install` sin restringir `cryptography`.
- Homebrew: en Mac Intel ya no tiene soporte ni paquetes precompilados nuevos.
- El `.mcpb` de otro servidor de Archicad que circula: no tiene modo de solo
  lectura.
