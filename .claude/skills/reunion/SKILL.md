---
name: reunion
description: Antes de una reunión de un encargo, prepara las preguntas que faltan para poder redactar; después, convierte la transcripción en hechos, puntos para el escrito y pendientes, dentro de la carpeta del encargo.
---

# Reunión de un encargo: antes y después

## Cuándo se usa

Cuando hay una reunión con un perito, un cliente, un técnico municipal o la
otra parte, y lo que se hable tiene que acabar en un informe o en un escrito.
Ejemplo típico: reunión con el perito agrónomo que valora un suelo expropiado,
antes de redactar la demanda contra la valoración del Jurado.

## Antes de la reunión

1. **Carpeta.** Trabaja en `encargos/<encargo>/`. Si no existe, créala con
   `entrada/`, `salida/` y `reuniones/`. Si existe, crea `reuniones/` si falta.
2. **Lee lo que hay**: ficha del encargo si existe, resoluciones, hojas de
   aprecio, informes, borradores.
3. **Prepara la reunión** en `reuniones/AAAA-MM-DD-<con-quien>-preparacion.md`:
   - Qué hay que sacar de esta reunión para poder redactar, en una frase.
   - **Las preguntas**, ordenadas por importancia y agrupadas por tema. Solo las
     que no se contestan con los documentos que ya están en la carpeta. Para
     una valoración rebatida: los puntos débiles de la valoración de la
     Administración, uno a uno, con el dato y el criterio que el perito usa en
     su lugar y la fuente que lo sostiene.
   - Qué documentos hay que pedirle que aporte.
4. Díselo en pantalla, corto, para que lo lleve abierto.

## Durante

Él graba la reunión con su app de notas, con permiso de los presentes. Al
acabar, exporta la transcripción como texto plano (`.txt`) a `reuniones/`.

## Después de la reunión

Con la transcripción en `reuniones/`:

1. **Lee la transcripción entera.** Viene de un dictado automático: nombres,
   cifras, siglas y referencias pueden venir mal escritos. Corrige por contexto
   lo evidente y marca `[VERIFICAR: dicho en reunión, confirmar]` todo número,
   referencia o nombre propio que no puedas contrastar con un documento de la
   carpeta.
2. Escribe `reuniones/AAAA-MM-DD-<con-quien>-acta.md` con cuatro apartados:
   - **Hechos y datos aportados**, cada uno con quién lo dijo.
   - **Argumentos para el escrito o el informe**, en el orden en que irían, cada
     uno con el dato que lo sostiene y el documento donde se verifica (o
     `[VERIFICAR]` si solo está dicho en la reunión).
   - **Documentos comprometidos**: quién los manda y cuándo.
   - **Pendientes**.
3. Si el encargo tiene ficha, propón qué añadir a la ficha. No la cambies sin su
   visto bueno.
4. Lo dicho en una reunión **no es fuente**: no se cita como si fuera un
   documento. Sirve para saber qué buscar y qué argumentar; la prueba es el
   informe del perito y los documentos.

## Reglas

- Nada de lo que se diga en la reunión sale de la carpeta del encargo.
- Lo que se hable de otros asuntos o de forma personal, ni se resume ni se
  guarda.
- Para redactar el escrito después, la skill que toque (`escrito-contencioso`,
  `informe-pericial-valoracion`) usa el acta como entrada, con sus mismas reglas
  de cita.
