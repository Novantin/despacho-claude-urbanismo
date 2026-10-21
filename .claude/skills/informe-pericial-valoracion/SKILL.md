---
name: informe-pericial-valoracion
description: En la carpeta del despacho (encargos/ y normativa/): informe pericial de valoración inmobiliaria con ficha por entrevista, índice del informe modelo, redacción por apartados, Word y auditoría.
---

# Informe pericial de valoración

El procedimiento del despacho para un informe pericial de valoración
inmobiliaria, de la ficha del encargo a la auditoría. **Es un procedimiento, no
una plantilla:** de un informe anterior se toman la estructura y el estilo,
nunca su texto ni sus cifras.

## Cuándo se usa

- Al empezar un informe de valoración (procedimiento civil,
  contencioso-administrativo o Jurado de Expropiación), o al retomarlo con la
  ficha ya hecha.
- En la conversación de auditoría de un informe ya redactado (paso 6).

## Antes de empezar

- `encargos/<expediente>/` con `entrada/` y, si ya existe, `FICHA-ENCARGO.md`.
- `estilo/GUIA-ESTILO-PERICIAL.md` y `plantillas/INDICE-INFORME-VALORACION.md`.
- La normativa de valoración en `normativa/estatal-autonomica/` y la ficha del
  ámbito en `normativa/municipal/<municipio>/` o en `entrada/`.
- Si falta algo, dilo antes de seguir.

## Procedimiento

### 1. Ficha del encargo

Si no existe `FICHA-ENCARGO.md`, hazla con la skill `ficha-encargo` (tipo
pericial). No redactes nada antes.

### 2. Índice

1. Propón el índice completo con la estructura de
   `plantillas/INDICE-INFORME-VALORACION.md`, adaptado a este encargo.
2. Para cada apartado, una línea con lo que va a contener en ESTE caso.
3. Marca los apartados que no apliquen y di por qué los quitas.
4. **Si el método no es comparación con comprobación por residual** —por
   ejemplo, suelo rural por capitalización de rentas—, sustituye los apartados
   VIII y IX por los del método que toque. Saca de la normativa de
   `normativa/` qué exige cada paso, con artículo; si no está, `[VERIFICAR]`.
5. No redactes. Espera a que corrija el índice y no sigas sin su visto bueno.

### 3. Cálculos

1. Todo cálculo —homogeneización, residual, capitalización, actualización— se
   hace en un `.xlsx` en `salida/`, con fórmulas a la vista y una hoja por
   cálculo. Nada de cifras calculadas de cabeza en el texto.
2. Cada dato de entrada del cálculo lleva su origen: documento del expediente,
   testigo o artículo. Si no lo hay: `[DATO]`.
3. Los coeficientes y parámetros que fija una norma se citan con su artículo y
   su texto; los que son criterio del perito se dicen como criterio suyo, y los
   decide él.

### 4. Redacción apartado por apartado

1. Un apartado por entrega, el que pida. Si no dice cuál, de los mecánicos a los
   delicados: objeto y alcance, documentación examinada y objeto de valoración
   antes que mercado, metodología y conclusiones.
2. Fuentes: solo la ficha, lo que hay en `entrada/`, el cálculo de `salida/` y
   `normativa/`.
3. **Perito informante:** con los datos de `CLAUDE.local.md`. Las declaraciones
   que exija la ley procesal del procedimiento (en civil, la Ley de
   Enjuiciamiento Civil) solo con esa ley delante: no está en `normativa/`, así
   que se añade con `/actualizar-normativa` o queda `[VERIFICAR]`.
4. Estilo: `estilo/GUIA-ESTILO-PERICIAL.md`. Extensión: la que pida el
   contenido.
5. Cierra cada entrega con `PENDIENTE DE VERIFICAR`, una marca por línea.
6. Espera la corrección antes de pasar al siguiente.

### 5. Salida a Word

1. Cuando lo pida, `.docx` en `salida/` con todo lo redactado: estilos reales
   Título 1, 2 y 3; índice automático al principio; numeración de páginas;
   cuerpo justificado con la tipografía y el tamaño de `CLAUDE.local.md`;
   tablas como tablas de Word; `[VERIFICAR]` y `[DATO]` resaltados en amarillo.
2. Avísale de que, al abrirlo, Word puede preguntar si actualiza los campos del
   índice: es normal, se contesta que sí. Si el índice sale vacío, clic derecho
   sobre él y «Actualizar campo».
3. Si el `.docx` no sale o sale mal, dilo y entrega el Markdown limpio para
   pegarlo como texto sin formato y aplicar su plantilla encima.
4. Recuérdale que la auditoría va en una conversación nueva. No te ofrezcas a
   hacerla en esta.

### 6. Auditoría, en conversación nueva

Skill `auditoria-normativa` sobre el borrador de `salida/`, contra `normativa/`
y `entrada/`. Además de normas y sentencias, comprueba los datos del
expediente: superficies, fechas, importes, testigos y coeficientes contra el
documento o la celda de donde dicen salir.

## Reglas que no se saltan

1. **Ninguna cita normativa sin documento.** Documento, artículo o apartado, y
   cita literal cuando proceda. Si no está: `[VERIFICAR: falta documento X,
   apartado Y]`.
2. **Ningún dato inventado.** Superficies, referencias, nombres, fechas,
   importes, testigos y coeficientes salen de la ficha y de los documentos. Si
   falta: `[DATO: qué falta]`.
3. **Hechos y valoración separados.** Lo que consta y lo observado, en sus
   apartados; el juicio técnico y los cálculos, en los suyos. Ninguna conclusión
   sin el hecho o el cálculo que la sostiene.
4. **Ninguna medición estimada desde una fotografía.** Si no hay documento,
   modelo o medición: `[DATO: medición pendiente]`.
5. **Ni interpretación jurídica ni adjetivos de parte en el pericial.** Lo que
   corresponde al juzgador no lo decide el informe.
