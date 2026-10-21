---
description: Trae las mejoras del kit y cuenta qué ha cambiado, sin tocar nada tuyo
---

Trae las novedades del kit y explícaselas. Sus cosas no se tocan nunca:
`CLAUDE.local.md`, `encargos/`, `normativa/municipal/`, `recursos/` y sus guías
de `estilo/` están fuera del control de versiones a propósito.

El kit vive en GitHub, en `Novantin/despacho-claude-urbanismo`, rama `main`.
Puede ser público o privado: con `git` da igual; sin `git`, cambia de dónde
sale el kit nuevo (paso 3).

## 1. ¿Por dónde se actualiza?

- **Con `git`**: si esta carpeta tiene `.git` y `xcode-select -p` responde con
  una ruta. Ve al paso 2.
- **Sin `git`** (la carpeta llegó en un pendrive o en un ZIP, o este Mac no tiene
  Command Line Tools): ve al paso 3. No ejecutes `git` para comprobarlo: sin
  Command Line Tools abre un diálogo de instalación.

## 2. Con `git`

1. `git status`. Si hay cambios en archivos del kit (no en los suyos), para y
   enséñaselos: alguien ha tocado `CLAUDE.md`, una skill o una plantilla, y eso
   se habla antes de pisarlo.
2. `git pull --ff-only origin main`.

Si el repositorio es privado, `git pull` usa el acceso que se dejó preparado al
clonarlo. Si pide usuario, contraseña o token, para: ni lo teclees tú ni le
pidas que lo pegue en la conversación; que se lo comente a quien le montó el
kit. Si `--ff-only` se niega, para también y díselo en una frase.

## 3. Sin `git`

Las variables no se conservan de un comando a otro: cuando un comando imprima
una ruta, apúntala y escríbela tal cual en los siguientes.

### De dónde sale el kit nuevo

- **Si el repositorio es público**: pide permiso y descarga el ZIP de la rama
  `main` en una carpeta temporal:

  ```bash
  T=$(mktemp -d) && curl -fL -o "$T/kit.zip" https://github.com/Novantin/despacho-claude-urbanismo/archive/refs/heads/main.zip && unzip -q "$T/kit.zip" -d "$T" && echo "$T/despacho-claude-urbanismo-main"
  ```

  Si `curl` falla con un 404, el repositorio es privado: no insistas ni pruebes
  otras direcciones, y sigue con el punto siguiente.
- **Si es privado**: las novedades le llegan en un ZIP o en un pendrive de quien
  le montó el kit. Pregúntale dónde lo tiene. Si es un ZIP, descomprímelo en una
  carpeta temporal (`T=$(mktemp -d) && unzip -q "<ZIP>" -d "$T" && ls "$T"`).
  La carpeta del kit nuevo es la que tiene `CLAUDE.md` dentro. Si no tiene
  ninguno de los dos, para: que se lo pida.

Antes de seguir, mira que en la carpeta del kit nuevo no haya nada suyo:
`CLAUDE.local.md`, `entrega/`, guías en `estilo/` ni contenido en `encargos/`,
`recursos/` o `normativa/municipal/` aparte de sus `README.md`. Si lo hay, para
y no copies nada.

### Compara y copia

1. Compara con esta carpeta (`diff -rq <kit nuevo> .`) y enséñale en una lista
   corta qué archivos del kit cambian. Ignora todo lo que solo existe aquí: es
   suyo. En `normativa/estatal-autonomica/*.md` compara la fecha `Descargado`
   de la cabecera: si la de aquí es más reciente que la del kit nuevo (se
   refrescó con `/actualizar-normativa`), esa ley no se copia; díselo en una
   línea.
2. Con su visto bueno, aparta primero las leyes del punto anterior fuera de la
   carpeta del kit nuevo, para que no se copien
   (`mv <kit nuevo>/normativa/estatal-autonomica/<LEY>.md <carpeta temporal>/`),
   y copia encima lo que queda (`cp -R <kit nuevo>/. .`). El kit nuevo no trae
   nada suyo, así que no puede pisarlo.

## 4. Cuéntale qué ha cambiado

Lee `BITACORA.md` y cuéntale **en lenguaje llano** qué ha entrado desde su
última actualización: skills nuevas, reglas, plantillas, leyes refrescadas. Si
algo le cambia la forma de trabajar, una frase con lo que haría distinto.

Confirma en una línea que sus cosas siguen intactas.

## Si algo falla

No lo arregles con fuerza bruta ni borres nada suyo. Explícale qué ha pasado en
una frase y que se lo comente a quien le montó el kit.
