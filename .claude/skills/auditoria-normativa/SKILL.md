---
name: auditoria-normativa
description: Revisa un borrador (informe, memoria o escrito) y verifica cada cita de norma, sentencia y dato contra normativa/ y el expediente. Tabla VERIFICADO, DISCREPANCIA o NO VERIFICABLE. Antes de firmar.
---

# Auditoría de normativa y jurisprudencia

La «policía»: un revisor en una conversación limpia, con los documentos delante
y prohibido aprobar nada que no pueda señalar con el dedo.

## Cuándo se usa

Antes de dar por cerrado cualquier documento que lleve firma. **Siempre en una
conversación nueva** (`/clear` o sesión nueva), nunca en la misma donde se
redactó: el revisor no puede ser el que ha escrito, porque arrastra sus
suposiciones.

## Qué cuenta como documento disponible

- Las normas de `normativa/` (estatal, autonómica y la municipal del expediente).
- Lo que hay en `encargos/<expediente>/entrada/`: resoluciones impugnadas, hojas
  de aprecio, expediente administrativo, sentencias aportadas en PDF.
- Lo que él adjunte en esta conversación.

Nada más. Lo que sepas de otras fuentes no cuenta.

## Procedimiento

1. **Avisa antes de empezar** de lo que va a salir como NO VERIFICABLE por
   construcción: toda sentencia que no esté en PDF en el expediente, y toda
   norma que no esté en `normativa/`. Es el resultado correcto, no un fallo.
2. Lee el borrador entero y localiza **toda** afirmación de carácter normativo
   o legal: artículos citados, plazos, competencia, procedimiento, método de
   valoración, coeficientes y factores, tipo de capitalización, citas de
   sentencias, y cada afirmación sobre lo que dicen las resoluciones o
   documentos del expediente.
3. Localiza también los **datos del expediente**: superficies, fechas, importes,
   referencias, cifras de cálculo. Cada uno contra el documento o la celda de
   donde dice salir.
4. Verifica una a una. En `normativa/`, busca el encabezado del artículo
   (`###### Artículo N.`; en la Ley de Expropiación Forzosa el número va en
   letra) y lee ese artículo con sus notas (`> [Nota BOE]`, `> Téngase en
   cuenta…`), no la ley entera. Si el pasaje citado incluye un apartado o un
   inciso destacado (en negrita) con nota de nulidad, el estado es
   **DISCREPANCIA**: el borrador cita como vigente algo declarado nulo.
5. Devuelve una tabla:

   | # | Afirmación literal del borrador | Documento y artículo donde se verifica | Cita literal de la fuente | Estado |

   Estado solo puede ser uno de estos tres:
   - **VERIFICADO** — está literalmente en un documento disponible.
   - **DISCREPANCIA** — está y no coincide con el borrador. Explica en qué.
   - **NO VERIFICABLE** — no está en los documentos disponibles. Di qué
     documento haría falta.
6. **La fecha.** Si verificas contra el texto de `normativa/` (vigente el día de
   su descarga) y el documento se refiere a otra fecha, dilo en la columna de
   documento: «redacción a DD-MM-AAAA; comprobar la vigente a la fecha del
   caso».
7. Al final, **ordena por riesgo**: qué revisaría él primero si solo tuviera 20
   minutos.
8. Ofrece la tabla en Excel (`salida/AUDITORIA-<documento>-<fecha>.xlsx`) con dos
   columnas vacías más: «Comprobado por mí» y «Observaciones».

## Reglas

- No apruebes nada por parecerte razonable o por conocerlo de otras fuentes.
  **Si no está en los documentos disponibles, es NO VERIFICABLE. Sin
  excepciones.**
- Una sentencia citada con número, fecha y recurso que no está aportada es NO
  VERIFICABLE aunque te suene. No completes ni corrijas sus datos de memoria.
- Tu trabajo es encontrar errores, no validar. Una auditoría sin ningún
  hallazgo es sospechosa: revisa otra vez.

## Segunda opinión en otra herramienta

Si quiere pasar el mismo control por otro modelo, prepárale en `salida/` un
`.md` con estas instrucciones y la tabla vacía, para pegar junto al borrador y
las leyes. Recuérdale que **decide él, como abogado, qué datos de su cliente
salen de este ordenador**: por defecto, ninguno.
