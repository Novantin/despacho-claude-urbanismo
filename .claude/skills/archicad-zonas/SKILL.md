---
name: archicad-zonas
description: Lee las zonas del modelo de Archicad abierto por el conector en solo lectura (planta, número, nombre, categoría, superficie) y saca un Excel con una hoja por planta. Sin teclear superficies.
---

# Zonas de Archicad, sin teclear

Las superficies salen del modelo, no de las manos. Esto es lo contrario de una
herramienta que te hace meter a mano lo que ya tienes en Archicad.

## Antes de empezar

- Archicad abierto con el proyecto, y el add-on Tapir cargado.
- El conector `archicad-mcp` activo en esta carpeta (`.mcp.json`, modo
  `readonly`). Si no aparece entre tus herramientas, los pasos están en
  [INSTALACION.md](INSTALACION.md). No lo instales sin su permiso expreso.
- La carpeta del expediente donde va el resultado.

## Procedimiento

1. **Conexión.** Ejecuta `TestConnection`. Dile qué proyecto y qué versión de
   Archicad y de Tapir responden, y en qué idioma está Archicad. Si falla, ve a
   «Si el conector no responde».
2. **Zonas.** Busca las herramientas con `search_tools` y llámalas con
   `call_tool`. Las que hacen falta, todas de lectura:
   - `GetElementsByType` con `{"elementType": "Zone"}`: los identificadores.
   - `GetDetailsOfElements`: nombre, número, categoría y planta de cada zona.
   - `GetZoneCategories` y `GetStories`: los nombres de categorías y plantas.
   - `GetAllProperties`: las propiedades de tipo superficie. **Enséñale las
     candidatas** (medida, neta, calculada…) y que elija él cuál va. No la
     elijas tú por el nombre.
   - `GetPropertyValuesOfElements`: el valor de esa propiedad en cada zona.
3. **La superficie llega como texto**, con los decimales y la unidad que tenga
   configurados el proyecto. Dala tal como la devuelve Archicad, sin redondear
   más. Si una zona no tiene superficie, dilo; no la estimes.
   Si entre las herramientas aparece `GetQuantitiesOfElements` (solo si se
   actualizaron las definiciones, ver [INSTALACION.md](INSTALACION.md)), da la
   superficie como número en m²: úsala, y que elija él entre medida, neta y
   calculada.
4. **Tabla en el chat**, agrupada por planta: planta, número, nombre, categoría y
   superficie, con subtotal por planta y total del edificio.
5. **Excel** en `salida/` del expediente, una hoja por planta y una de resumen:
   - Columnas: Planta · Número · Nombre · Categoría · Superficie (texto de
     Archicad) · Superficie (número).
   - El número se saca del texto sin redondear. Si el texto no se puede leer
     sin ambigüedad, celda vacía y `[DATO]`.
   - Subtotales y total con fórmulas de Excel, no con cifras escritas (al
     escribirlas por script, `=SUM(...)`; Excel en español las muestra como
     `SUMA`).
6. **Cierra el círculo**: ese Excel es el cuadro de superficies de la memoria o
   del informe. Se cita por su nombre de archivo, no se vuelve a teclear.

## Si el conector no responde

No se pelea. Versión «exporta y lee»: él exporta desde Archicad el listado de
zonas a Excel o PDF, y los planos a PDF, a `entrada/` del expediente. Se lee de
ahí con el mismo procedimiento desde el paso 3.

## Reglas que no se saltan

- **Solo lectura.** Nunca uses una herramienta que cree, modifique, borre,
  guarde, cierre o publique. Si una petición lo exigiera, para y díselo.
- Nunca propongas cambiar `ARCHICAD_MCP_MODE` a otro valor.
- Ninguna superficie estimada, redondeada ni completada a mano.
