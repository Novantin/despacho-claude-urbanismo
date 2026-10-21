---
name: memoria-urbanistica
description: Procedimiento para memorias urbanísticas (autorizaciones excepcionales, planes parciales y especiales, programas de actuación): requisitos legales con artículo, índice anclado y Word.
---

# Memoria urbanística

Procedimiento para memorias de autorizaciones excepcionales por interés público,
planes parciales y especiales, estudios de detalle, programas de actuación e
informes de viabilidad. **Es un procedimiento, no un contenido:** qué hay que
justificar lo dice la ley; cómo se justifica en este caso lo dicen los datos del
expediente y él.

## Antes de empezar

- `FICHA-ENCARGO.md` de tipo urbanístico (`plantillas/FICHA-EXPEDIENTE-URBANISTICO.md`).
  Si no existe, skill `ficha-encargo`.
- La ley urbanística autonómica en `normativa/estatal-autonomica/`.
- El planeamiento municipal del ámbito en `normativa/municipal/<municipio>/`:
  la ficha del ámbito y las normas que apliquen, no el plan entero.
- En `entrada/`: planos, catastro, documentación del promotor, informes
  sectoriales o estudios de terceros que ya existan.

## Procedimiento

### 1. El supuesto

Qué instrumento es y en qué supuesto legal encaja. Si hay duda entre dos, es
una pregunta para él, no una decisión tuya.

### 2. Mapa de requisitos

1. Busca en la ley urbanística de `normativa/` los artículos que regulan: el
   supuesto (qué se puede autorizar o planear y con qué condiciones), la
   documentación que exige ese instrumento, el procedimiento y el órgano que
   resuelve. Los encabezados de los artículos ayudan: busca los que hablan de
   «autorización excepcional», «interés público» o «Documentos de los Planes».
2. Haz una tabla y enséñasela antes de seguir:

   | Requisito | Artículo | Cita literal | Dónde se justifica en la memoria | Con qué dato o documento |

3. Añade los requisitos de la ficha del ámbito municipal, con su referencia.
4. Informes sectoriales y estudios exigidos: solo los que nombre un documento
   disponible. Los demás, `[VERIFICAR: ¿exige informe de …?]`.

### 3. Índice anclado

1. Propón el índice de modo que cada apartado justifique uno o varios requisitos
   del mapa, y cada requisito tenga su apartado. Lo que no esté cubierto, dilo.
2. Si tiene una memoria suya anterior del mismo tipo en `recursos/`, toma su
   estructura, nunca su texto.
3. Espera su corrección.

### 4. Datos y parámetros

1. Superficies, edificabilidades, ocupaciones y alturas salen de documentos o
   del modelo de Archicad (skill `archicad-zonas`), nunca estimadas.
2. Tabla de cumplimiento:

   | Parámetro | Exigido (artículo o ficha) | Proyectado (fuente) | Cumple |

   La columna «Cumple» la confirma él. Si falta un dato: `[DATO]`.

### 5. Redacción

1. Apartado por apartado, de los descriptivos a los de justificación.
2. **En la justificación del interés público y de la excepcionalidad, hechos y
   argumentación separados:** primero los datos (ubicación, demanda, servicio,
   infraestructuras, con su fuente); después por qué cumplen cada requisito del
   mapa.
3. Los estudios de terceros (paisaje, ruido, tráfico) se citan y se resumen con
   su referencia; no se reescriben ni se completan.
4. Estilo: `estilo/GUIA-ESTILO-PERICIAL.md`, salvo que él tenga una guía propia
   para memorias.
5. Cierra cada entrega con `PENDIENTE DE VERIFICAR`.

### 6. Word y auditoría

`.docx` en `salida/` con estilos reales y las marcas resaltadas. Auditoría en
conversación nueva con `auditoria-normativa`, contra el mapa de requisitos.

## Reglas que no se saltan

- Ningún requisito sin artículo y cita literal. Ningún artículo de memoria.
- Ningún parámetro urbanístico de memoria: sale de la ficha del ámbito o del
  plan, con su referencia.
- No imites el estilo de documentos de otros autores que haya en `entrada/`.
- Lo que decide la Administración no lo da por hecho la memoria.
