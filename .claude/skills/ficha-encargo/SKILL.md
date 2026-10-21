---
name: ficha-encargo
description: Ficha de un encargo nuevo (pericial, urbanístico o procesal) por entrevista, una pregunta cada vez, a partir del material del expediente. Primer paso antes de redactar nada.
---

# Ficha del encargo

## Cuándo se usa

Al abrir un expediente, **antes de redactar nada**. Informe, memoria, demanda,
cuadro de superficies y correo al cliente salen de aquí. Una ficha por
expediente; si el expediente lleva informe y escrito, la misma ficha con las dos
secciones.

## Procedimiento

1. **Carpeta.** Comprueba que existe `encargos/<AAAA-NNN-descripcion>/` con
   `entrada/` y `salida/`. Si no, propón el nombre y créala.
2. **Lee todo lo de `entrada/`**: designación o encargo, escrituras, notas
   simples, catastro, resoluciones, hojas de aprecio, demanda, ficha del sector,
   testigos, correos. Si un PDF es un escaneo sin texto, dilo: de ahí no se
   puede citar literalmente.
3. **Qué tipo de encargo es**: pericial, urbanístico o procesal. Si no está
   claro, es la primera pregunta.
4. **Entrevista** como un colaborador que se incorpora al expediente y necesita
   ponerse al día:
   - Una pregunta cada vez. Espera la respuesta.
   - Empieza por lo que condiciona todo lo demás:
     - **Pericial:** quién encarga y en qué calidad (designación judicial,
       parte, Jurado), la pregunta exacta que hay que contestar, la fecha de
       referencia de la valoración, la situación básica del suelo y el
       instrumento de planeamiento que manda.
     - **Urbanístico:** qué instrumento es, quién promueve, clase y categoría
       del suelo, planeamiento vigente en el ámbito, uso o actuación que se
       pretende y qué órgano resuelve.
     - **Procesal:** órgano y procedimiento, acto o resolución que se impugna y
       fecha de notificación, partes y representación, pretensión, cuantía y
       trámite en que está el asunto.
   - Antes de preguntar, mira si la respuesta ya está en `entrada/`. Si está,
     no la preguntes: di qué has deducido y de qué documento, y pide que lo
     confirme.
   - Si la respuesta es vaga, insiste una vez pidiendo el dato concreto.
   - Máximo 20 preguntas. Cuando tengas lo esencial, párate y dilo.
5. **Genera `FICHA-ENCARGO.md`** en la carpeta del expediente:
   - Pericial: estructura de `plantillas/FICHA-ENCARGO-PERICIAL.md`.
   - Urbanístico: estructura de `plantillas/FICHA-EXPEDIENTE-URBANISTICO.md`.
   - Procesal: órgano y procedimiento; partes, representación y dirección
     letrada; acto impugnado y fechas que constan (notificación, interposición,
     remisión del expediente); pretensiones; cuantía y de dónde sale;
     documentos del expediente numerados; hechos clave con el documento que
     los acredita; prueba prevista; marco normativo aplicable.
6. Si la quiere en Word, genérala también en `.docx` en `salida/`.

## Reglas

- Ningún dato inventado ni interpretado. Lo que no te hayan dicho ni conste en
  un documento: `[DATO: qué falta]`.
- Cada dato que sale de un documento lleva al lado de qué documento sale.
- No propongas soluciones, valores ni argumentos durante la entrevista. Solo
  recoges.
- El marco normativo lista **qué habrá que consultar, no qué dice**. Para cada
  norma, si está en `normativa/` o no: `[VERIFICAR: no está en normativa/]`.
- **Plazos:** la ficha recoge las fechas que constan en los documentos. El
  plazo legal se apunta con `[VERIFICAR: artículo que lo fija]` y no se calcula
  en la ficha.
- Cierra con `PENDIENTE DE VERIFICAR`.
