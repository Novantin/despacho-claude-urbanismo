---
name: deck-desde-modelo
description: Deck .pptx para inversores de una promoción con las cifras leídas del modelo financiero en Excel, cada una con su hoja y celda de origen. Ningún número tecleado ni rentabilidad no calculada.
---

# Deck desde el modelo financiero

Para la línea promotora, no para el despacho: carpeta aparte en `encargos/`
(por ejemplo `encargos/promocion-<nombre>/`), conversación aparte, tono aparte.
**La presentación sale del Excel, no de volver a escribir las cifras.**

## Antes de empezar

- En `entrada/`: el modelo financiero `.xlsx` de esa promoción y el deck de
  referencia (`.pptx` o `.pdf`) que marca la secuencia, el tono y el formato.
- Que diga cuál de sus decks es el vigente si tiene varias versiones.

## Procedimiento

1. **Lee el Excel.** Hojas, celdas de entrada (parámetros) y celdas calculadas.
   Lee los valores calculados tal como Excel los guardó.
2. **Tabla de cifras**, antes de generar nada:

   | Cifra del deck | Hoja!Celda | Valor | Entrada o fórmula |

   Enséñasela. Si una cifra que el deck necesita no está en el modelo:
   `[DATO: qué falta]`.
3. **Si cambian los parámetros** (unidades, precio, aportación), los cambia él en
   Excel y guarda. Si los cambias tú con un script, Excel no ha recalculado: no
   uses esas cifras hasta que lo abra, se recalcule y lo guarde.
4. **Genera el `.pptx`** en `salida/` con la secuencia del deck de referencia.
   Una idea por diapositiva, sin párrafos.
5. **Origen de cada cifra**: en las notas de la diapositiva y en una diapositiva
   final con la lista de cifras y su hoja y celda.
6. **`[DATO]` en rojo** para todo lo que no esté en el modelo ni en el deck de
   referencia.
7. **Comprobación delante de él:** abre el `.pptx` y contrasta un número contra
   el Excel.
8. **Correcciones por escrito** («quita la diapositiva 4», «menos texto en
   hitos»): se relanza lo que cambia, no el deck entero.

## Reglas que no se saltan

- Ningún número que no salga del modelo: precios, unidades, superficies,
  aportaciones, calendario, plazos, porcentajes y retornos.
- Si el deck de referencia y el modelo no coinciden, manda el modelo. Señala la
  discrepancia; no la corrijas en silencio.
- Ninguna rentabilidad, ahorro o retorno que no esté calculado en el modelo, y
  ninguna promesa de resultado. Si el deck de referencia trae una frase de
  garantía, señálala y que decida él.
- Conserva los avisos legales del deck de referencia junto al ejemplo económico
  y al cierre.
- Nada del despacho en esta conversación, y nada de la promoción en las del
  despacho.
