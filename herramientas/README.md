# Herramientas

Dos cosas, y ninguna más: bajar normativa del BOE y escribir documentos de
Office. Lo usa Claude, o quien mantiene el kit; tú no tienes que tocar nada de
aquí.

## `boe_a_markdown.py` — normativa del BOE en Markdown citable

Solo biblioteca estándar de Python (3.9 o posterior) y solo lectura: pide el
texto consolidado a la API oficial de legislación consolidada del BOE (sin clave)
y escribe un `.md` con los artículos como encabezados `######`, igual que las
seis leyes de `normativa/`.

```bash
# ¿Ha cambiado algún artículo desde la descarga?
python3 herramientas/boe_a_markdown.py --comprobar normativa/estatal-autonomica/*.md

# Bajar una norma
python3 herramientas/boe_a_markdown.py BOE-A-1954-15431 -o normativa/estatal-autonomica/LEF-1954-Expropiacion-Forzosa.md

# La redacción vigente en una fecha concreta (la de la valoración, la del acto)
python3 herramientas/boe_a_markdown.py BOE-A-1954-15431 --a-fecha 2024-03-15 -o encargos/<expediente>/entrada/LEF-vigente-2024-03-15.md
```

- No sobrescribe: si el destino existe, deja la versión nueva al lado con
  extensión `.nuevo`. Con `--sobrescribir`, reemplaza.
- `--comprobar` mira la fecha de cada artículo en el índice del BOE, no la fecha
  general de la norma, que cambia aunque el texto no cambie. Si el texto sigue
  igual pero la ficha de la norma se ha actualizado (por ejemplo, el BOE ha
  anotado una sentencia del Constitucional), da un `AVISO` con el enlace al
  análisis de la norma.
- Sale con 0 si todo está al día, 1 si hay cambios o avisos, 2 si hay un error.
- Las fórmulas que el BOE publica como imagen (Reglamento de valoraciones y
  Orden ECO/805/2003) se reponen con la transcripción hecha a mano; si aparece
  una nueva, queda marcada `[IMAGEN SIN TRANSCRIBIR]`.
- Las notas del BOE conservan su referencia («Ref. BOE-…», «Ref. BORM-…»), que
  es la que sirve para buscar la sentencia o la norma que modifica o anula un
  artículo. El inciso que una nota llama «destacado» va en negrita.
- Sin Command Line Tools no hay `python3` (y ejecutarlo abre su instalador). Si
  está `uv` (lo deja el conector de Archicad), se ejecuta así:
  `~/.local/bin/uv run --no-project --managed-python --python 3.13 herramientas/boe_a_markdown.py …`

Probado el 21-10-2026 con el Python 3.9.6 de las Command Line Tools, en un Mac
con macOS 26 (no en Monterey): las seis leyes regeneradas salen idénticas a las
de `normativa/` salvo la fecha de descarga; `--comprobar` no encuentra cambios
en ninguna y, con una fecha de descarga anterior puesta a propósito, encuentra
los bloques de la LOTURM cambiados el 07-07-2026 y avisa de la ficha de la Ley
de Suelo actualizada el 13-10-2026; `--a-fecha 2026-07-01` devuelve la LOTURM
sin el artículo 100 bis, que entró en vigor después.

Fuente de los datos: Agencia Estatal Boletín Oficial del Estado. Texto
consolidado de carácter meramente informativo, sin valor oficial.

## `ofimatica.txt` — para escribir `.docx`, `.pptx` y `.xlsx`

Las bibliotecas de Python con las que Claude genera Word, PowerPoint y Excel,
con versiones fijadas. Comprobado en PyPI el 21-10-2026: todas son Python puro
salvo `lxml` y `pillow`, que tienen paquete precompilado para Mac Intel (macOS
10.13 o posterior) y Python 3.13. Fijarlas evita que un día se cuele una
versión sin paquete para Intel y haya que compilarla, que en este Mac no sale.

Orden para generarlos en este ordenador:

1. **Si existe `~/.local/bin/uv`** (lo deja el conector de Archicad), el script
   de generación va en `salida/` del expediente y se ejecuta así, sin instalar
   nada en el sistema:

   ```bash
   ~/.local/bin/uv run --no-project --managed-python --python 3.13 --with-requirements herramientas/ofimatica.txt python encargos/<expediente>/salida/generar.py
   ```

2. **Si no existe**, se instala `uv` con su instalador oficial y la versión
   fijada (`curl -LsSf https://astral.sh/uv/0.13.4/install.sh | sh`), **con
   permiso**, y se vuelve al punto 1.
3. Nunca Homebrew en este Mac, y nunca `pip install` sobre el Python del sistema.

Detalles que importan en Word:

- Estilos integrados («Heading 1/2/3»): Word en español los muestra como Título
  1/2/3 y salen en el panel de estilos.
- Índice como campo de Word y la actualización de campos al abrir activada
  (`w:updateFields` en la configuración del documento), para que Word pregunte
  y lo rellene. Si no pregunta: clic derecho en el índice → Actualizar campo.
- Numeración de páginas como campo `PAGE` en el pie.
- `[VERIFICAR]` y `[DATO]` con resaltado amarillo, no con color de letra.

## Lo que no está, y por qué

- **Catastro.** Sus servicios web libres responden sin clave, pero por ahora la
  consulta descriptiva y gráfica entra como PDF en la carpeta de cada
  expediente. Una herramienta propia solo compensa con volumen de valoraciones
  de rústico o de expropiación, y con consultas puntuales: el Catastro corta el
  servicio por IP a quien abusa.
- **BORM y jurisprudencia.** No se automatizan. El BORM no tiene API y tiene una
  capa antibots; el aviso legal del CENDOJ prohíbe la descarga masiva y el uso
  comercial. Van a mano, en PDF, a la carpeta del expediente.
- **Servidores MCP de terceros** para BOE o Catastro. El único conector es el de
  Archicad, en solo lectura.
