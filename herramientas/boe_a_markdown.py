#!/usr/bin/env python3
"""Texto consolidado del BOE -> Markdown citable, y aviso de cambios.

Solo biblioteca estándar (Python 3.9 o posterior). Solo lectura: hace GET a la
API oficial de legislación consolidada del BOE y escribe un .md local.

Usos:

  # Bajar una norma (identificador del BOE) y guardarla en Markdown
  python3 herramientas/boe_a_markdown.py BOE-A-1954-15431 \
      -o normativa/estatal-autonomica/LEF-1954-Expropiacion-Forzosa.md

  # La redacción que estaba vigente en una fecha concreta (p. ej. la fecha
  # a la que se refiere una valoración)
  python3 herramientas/boe_a_markdown.py BOE-A-1954-15431 --a-fecha 2024-03-15 \
      -o encargos/EXPEDIENTE/entrada/LEF-vigente-2024-03-15.md

  # Comprobar si ha cambiado algún artículo desde la fecha de descarga
  python3 herramientas/boe_a_markdown.py --comprobar normativa/estatal-autonomica/*.md

Formato de salida: artículos como encabezados de nivel 6 ("###### Artículo
36. ..."), disposiciones y títulos de nivel 2, apartados en negrita ("**1.**"),
notas del BOE como "> [Nota BOE] ..." o "> Téngase en cuenta ...", con su
"Ref. BOE-..." cuando el BOE la da. El inciso que una nota llama "destacado"
(p. ej. el declarado nulo por el Tribunal Constitucional) va en negrita dentro
del párrafo. Las fórmulas que el BOE publica como imagen se sustituyen por su
transcripción en LaTeX si está en FORMULAS (solo las del RD 1492/2011 y la Orden
ECO/805/2003, transcritas a mano: comprobar contra el BOE las que se citen); si
no, queda la marca [IMAGEN SIN TRANSCRIBIR].

Si el archivo de salida ya existe, no se sobrescribe: se escribe al lado con
extensión .nuevo para compararlo. Con --sobrescribir, se reemplaza.

--comprobar mira la fecha de cada artículo en el índice del BOE. Si el texto
no ha cambiado pero la ficha de la norma sí (el BOE añade referencias, como una
sentencia del Tribunal Constitucional), da un AVISO con el enlace al análisis.

Códigos de salida: 0 bien y sin cambios; 1 hay cambios o avisos (--comprobar);
2 error de red, de identificador o de formato.

Fuente de los datos: Agencia Estatal Boletín Oficial del Estado. Texto
consolidado de carácter meramente informativo, sin valor oficial.
"""

import argparse
import datetime
import glob
import json
import os
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

API = "https://www.boe.es/datosabiertos/api/legislacion-consolidada"
BOE = "https://www.boe.es"
UA = "despacho-claude-urbanismo/1.0 (consulta puntual de normativa)"
TIMEOUT = 60

# Formulas que el BOE publica como imagen PNG, transcritas a LaTeX a mano a
# partir de la imagen (clave = nombre del PNG). RD 1492/2011 (17629_*) y
# Orden ECO/805/2003 (07253_*, y 18140_* de su modificacion). Comprobar contra
# el BOE las que se vayan a citar.
FORMULAS = {
    "17629_001": r"V=\frac{R_1}{(1+r)^1}+\frac{R_2}{(1+r)^2}+\dots+\frac{R_n}{(1+r)^n}=\sum_{i=1}^{n\to\infty}\frac{R_i}{(1+r)^i}",
    "17629_002": r"V=\frac{R}{r}",
    "17629_003": r"V=\frac{R_1}{(1+r_2)^1}+\frac{R_2}{(1+r_2)^2}+\dots+\frac{R_n}{(1+r_2)^n}=\sum_{i=1}^{n\to\infty}\frac{R_i}{(1+r_2)^i}",
    "17629_004": r"V=\left[\frac{R_1}{(1+r_2)^1}+\frac{R_2}{(1+r_2)^2}+\dots+\frac{R_k}{(1+r_2)^k}\right]\cdot\left(\frac{(1+r_2)^k}{(1+r_2)^k-1}\right)",
    "17629_005": r"V=\frac{R_1}{(1+r_2)^1}+\frac{R_2}{(1+r_2)^2}+\dots+\frac{R_h}{(1+r_2)^h}+\frac{R}{r_2\cdot(1+r_2)^h}",
    "17629_006": r"V=\frac{R_1}{(1+r_2)^1}+\frac{R_2}{(1+r_2)^2}+\dots+\frac{R_l}{(1+r_2)^l}+\left[\frac{R_{l+1}}{(1+r_2)^{l+1}}+\dots+\frac{R_{l+k}}{(1+r_2)^{l+k}}\right]\cdot\left(\frac{(1+r_2)^k}{(1+r_2)^k-1}\right)",
    "17629_007": r"V=\sum_{i=1}^{h}\frac{R_i}{(1+r_3)^i}+\frac{R}{r_2\cdot(1+r_2)^h}",
    "17629_008": r"h=\frac{Q}{q_1}",
    "17629_009": r"V=\sum_{i=1}^{n\to\infty}\frac{R_i}{(1+r_3)^i}",
    "17629_010": r"V=\sum_{i=1}^{t}\frac{R_i}{(1+r_3)^i}+\frac{V_r}{(1+r_3)^t}+\frac{R}{r_2\cdot(1+r_2)^t}",
    "17629_011": r"V=\frac{R_0}{r_1}",
    "17629_012": r"u_1=1+\left[P_1+\frac{P_2}{3}\right]\cdot\frac{1}{1.000.000}",
    "17629_013": r"\beta=1-\left[1-\frac{(a+a^2)}{2}\right]\cdot C",
    "17629_014": r"EM=\frac{\sum\frac{E_i\cdot S_i\cdot VRS_i}{VRS_r}}{SA-SD}",
    "17629_015": r"VS=\sum E_i\cdot VRS_i",
    "17629_016": r"VRS=\frac{Vv}{K}-Vc",
    "17629_017": r"Vv'=Vv\cdot\frac{1-\beta\cdot F}{1-\beta_i\cdot F}",
    "07253_001": r"VA=\sum\frac{E_j}{(1+i)^{t_j}}-\sum\frac{S_k}{(1+i)^{t_k}}+\frac{\text{Valor de reversión}}{(1+i)^n}",
    "07253_002": r"F=\sum\frac{E_j}{(1+i)^{t_j}}-\sum\frac{S_k}{(1+i)^{t_k}}",
    "07253_003": r"VML+\text{Máximo}\left[0,\left(\frac{VTL}{(1+i)^n}\right)-VML\right]",
    "18140_001": r"\ddot a_{x:n}=\sum_{t=0}^{n-1}C_t\cdot(1+i)^{-t}\cdot{}_tp_x",
    "18140_002": r"\ddot a_{x}=\sum_{t=0}^{w-x-1}C_t\cdot(1+i)^{-t}\cdot{}_tp_x",
    "18140_003": r"\ddot a_{xy:n}=\sum_{t=0}^{n-1}C_t\cdot(1+i)^{-t}\cdot{}_tp_{xy}",
    "18140_004": r"\ddot a_{xy}=\sum_{t=0}^{\infty}C_t\cdot(1+i)^{-t}\cdot{}_tp_{xy}",
    "18140_005": r"\ddot a_{\overline{xy}:n}=\sum_{t=0}^{n-1}C_t\cdot(1+i)^{-t}\cdot{}_tp_{\overline{xy}}=\ddot a_{x:n}+\ddot a_{y:n}-\ddot a_{xy:n}",
    "18140_006": r"\ddot a_{\overline{xy}}=\sum_{t=0}^{\infty}C_t\cdot(1+i)^{-t}\cdot{}_tp_{\overline{xy}}=\ddot a_x+\ddot a_y-\ddot a_{xy}",
}

ID_RE = re.compile(r"^[A-Z]+-[A-Za-z]-\d{4}-\d+$")
NUM = re.compile(r"^(\d{1,3})\.\s+(?=\S)")


class ErrorBOE(Exception):
    pass


# ---------------------------------------------------------------- red

def get(url, accept):
    """GET con la cabecera Accept que exige la API (sin ella devuelve 400)."""
    req = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        pista = " (¿identificador correcto?)" if e.code in (400, 404) else ""
        raise ErrorBOE("HTTP %s en %s%s" % (e.code, url, pista))
    except urllib.error.URLError as e:
        raise ErrorBOE("sin conexión con %s (%s)" % (url, e.reason))


def tamano_remoto(url):
    """Content-Length por HEAD; None si el servidor no lo da."""
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            n = r.headers.get("Content-Length")
            return int(n) if n else None
    except Exception:
        return None


# ---------------------------------------------------------------- render

def inline(el):
    """Texto en linea de un elemento, con negrita, cursiva, sub y sup."""
    out = [el.text or ""]
    for c in el:
        t = c.tag
        if t == "a" and c.get("class") == "refPost":
            # "Ref. BOE-A-..." de las notas: se conserva, como en el BOE
            inner = inline(c)
        elif t == "ins":
            inner = ""
        elif t == "strong":
            s = inline(c).strip()
            inner = "**%s** " % s if s else ""
        elif t == "em":
            s = inline(c).strip()
            inner = "*%s*" % s if s else ""
        elif t == "sub":
            inner = "<sub>%s</sub>" % inline(c)
        elif t == "sup":
            inner = "<sup>%s</sup>" % inline(c)
        else:
            inner = inline(c)
        out.append(inner)
        out.append(c.tail or "")
    return "".join(out)


def clean(s):
    s = s.replace(" ", " ")
    s = re.sub(r"[ \t\r\n]+", " ", s).strip()
    s = re.sub(r"\*\* \*\*", " ", s)
    return s


def pick_version(bloque, fecha):
    """La version del bloque vigente en `fecha` (AAAAMMDD)."""
    best = None
    for v in bloque.findall("version"):
        fv = v.get("fecha_vigencia") or "0"
        if fv <= fecha and (best is None or fv >= best.get("fecha_vigencia")):
            best = v
    return best


def table_md(tbl):
    rows = []
    for tr in tbl.iter("tr"):
        cells = []
        for td in tr:
            if td.tag not in ("td", "th"):
                continue
            parts = [clean(inline(p)) for p in td.iter("p")] or [clean(inline(td))]
            txt = "<br>".join(x for x in parts if x).replace("|", "\\|")
            cells.append(txt)
            cells.extend([""] * (int(td.get("colspan", "1")) - 1))
        rows.append(cells)
    if not rows:
        return ""
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    md = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * n]
    md += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(md)


def render(root, fecha, sin_transcribir):
    out = []
    add = out.append
    for bl in root.iter("bloque"):
        v = pick_version(bl, fecha)
        if v is None:
            continue
        ps = list(v)
        i = 0
        while i < len(ps):
            p = ps[i]
            cls = p.get("class", "")
            if p.tag == "table":
                add(table_md(p))
                i += 1
                continue
            if p.tag == "blockquote":
                cad = p.get("caduca")
                if cad and cad < fecha:
                    i += 1
                    continue
                lines = []
                for q in p:
                    t = clean(inline(q))
                    if t and q.get("class") != "cita_con_pleca":
                        pre = "[Nota BOE] " if q.get("class", "").startswith("nota_pie") else ""
                        lines.append("> " + pre + t)
                if lines:
                    add("\n>\n".join(lines))
                i += 1
                continue
            if p.tag != "p":
                i += 1
                continue
            txt = clean(inline(p))
            if cls == "imagen":
                img = next(p.iter("img"), None)
                if img is not None:
                    src = img.get("src") or ""
                    key = os.path.basename(src).replace(".png", "")
                    if key in FORMULAS:
                        add("$$" + FORMULAS[key] + "$$")
                    else:
                        url = src if src.startswith("http") else BOE + src
                        sin_transcribir.append(url)
                        add("[IMAGEN SIN TRANSCRIBIR: %s — %s]" % (key, url))
                i += 1
                continue
            if not txt:
                i += 1
                continue
            if cls in ("titulo_num", "capitulo_num", "anexo_num"):
                lvl = "##" if cls != "capitulo_num" else "###"
                nxt = ps[i + 1] if i + 1 < len(ps) else None
                tit = ""
                if nxt is not None and nxt.get("class") in ("titulo_tit", "capitulo_tit", "anexo_tit"):
                    tit = clean(inline(nxt))
                    i += 1
                add("%s %s" % (lvl, txt) + (". %s" % tit if tit else ""))
            elif cls in ("titulo_tit", "capitulo_tit", "anexo_tit"):
                add("%s %s" % ("###" if cls == "capitulo_tit" else "##", txt))
            elif cls == "capitulo":
                add("### " + txt)
            elif cls == "seccion":
                add("#### " + txt)
            elif cls == "subseccion":
                add("##### " + txt)
            elif cls in ("articulo", "anexo"):
                add(("###### " if re.match(r"^Art[íi]culo", txt) else "## ") + txt)
            elif cls == "centro_redonda":
                add("**%s**" % txt)
            elif cls in ("nota_pie", "nota_pie_2"):
                add("> [Nota BOE] " + txt)
            elif cls in ("textoCompleto", "siempreSeVe"):
                add("> " + txt)
            else:
                m = NUM.match(txt)
                if m:
                    txt = "**%s.** " % m.group(1) + txt[m.end():]
                add(txt)
            i += 1
    return out


# ---------------------------------------------------------------- descargar

def iso(d8):
    return "%s-%s-%s" % (d8[:4], d8[4:6], d8[6:8])


def metadatos(ident):
    raw = get("%s/id/%s/metadatos" % (API, ident), "application/xml")
    try:
        m = ET.fromstring(raw).find("data/metadatos")
    except ET.ParseError:
        raise ErrorBOE("respuesta no válida para %s" % ident)
    if m is None:
        raise ErrorBOE("el BOE no devuelve metadatos para %s (¿identificador correcto?)" % ident)
    return {c.tag: (c.text or "").strip() for c in m}


def descargar(ident, fecha_iso=None):
    """Devuelve (markdown, avisos)."""
    hoy = datetime.date.today().isoformat()
    vigente = fecha_iso or hoy
    fecha8 = vigente.replace("-", "")
    meta = metadatos(ident)
    raw = get("%s/id/%s/texto" % (API, ident), "application/xml")
    try:
        root = ET.fromstring(raw).find("data/texto")
    except ET.ParseError:
        raise ErrorBOE("el texto de %s no es XML válido" % ident)
    if root is None:
        raise ErrorBOE("el BOE no devuelve texto consolidado para %s" % ident)

    avisos = []
    if meta.get("estatus_derogacion") == "S":
        avisos.append("La norma figura como DEROGADA en el BOE.")
    if meta.get("estatus_anulacion") == "S":
        avisos.append("La norma figura como ANULADA en el BOE.")
    if meta.get("vigencia_agotada") == "S":
        avisos.append("La norma figura con la vigencia AGOTADA en el BOE.")

    sin_transcribir = []
    body = render(root, fecha8, sin_transcribir)
    if sin_transcribir:
        avisos.append("%d imagen(es) sin transcribir (fórmulas o tablas): buscar "
                      "[IMAGEN SIN TRANSCRIBIR] en el archivo." % len(sin_transcribir))

    titulo = meta.get("titulo", ident)
    fa = meta.get("fecha_actualizacion", "")[:8]
    html_url = meta.get("url_html_consolidada") or "%s/buscar/act.php?id=%s" % (BOE, ident)
    eli = meta.get("url_eli", "")
    pdf_url = "%s/buscar/pdf/%s/%s-consolidado.pdf" % (BOE, ident.split("-")[2], ident)
    api_url = "%s/id/%s/texto" % (API, ident)
    pdf_bytes = tamano_remoto(pdf_url)

    if fecha_iso:
        alcance = ("Texto vigente a %s, redacción histórica sacada del consolidado del BOE "
                   "(la versión de cada artículo que estaba en vigor ese día)" % vigente)
    else:
        alcance = ("Texto vigente a %s (solo la última versión de cada artículo; se omiten "
                   "las redacciones históricas)" % vigente)

    body_txt = "\n\n".join(body) + "\n"
    kbmd = 0
    full = ""
    for _ in range(5):
        pdf = ("%.0f KB del PDF original (%s)" % (pdf_bytes / 1000.0, pdf_url)
               if pdf_bytes else "el PDF original (%s)" % pdf_url)
        h = "# %s\n\n" % titulo
        h += ("> **Origen:** %s (texto consolidado vigente, vía API oficial %s) · **Descargado:** %s · "
              "**Tamaño:** %d KB en Markdown frente a %s.\n>\n" % (html_url, api_url, hoy, kbmd, pdf))
        h += ("> **Identificador:** %s · **ELI:** %s · **Última actualización consolidada en el BOE:** %s · "
              "%s. Los apartados van en negrita (**1.**) y los artículos son encabezados de nivel 6 "
              "para poder citar artículo y apartado.\n>\n" % (ident, eli, iso(fa) if fa else "no consta", alcance))
        h += ("> **Fuente de los datos:** Agencia Estatal Boletín Oficial del Estado (https://www.boe.es). "
              "Texto consolidado de carácter meramente informativo, sin valor oficial: para citar en un "
              "escrito, comprobar contra el BOE.\n\n")
        full = h + body_txt
        nuevo = int(round(len(full.encode("utf-8")) / 1000.0))
        if nuevo == kbmd:
            break
        kbmd = nuevo
    return full, avisos


def escribir(destino, texto, sobrescribir):
    if os.path.exists(destino) and not sobrescribir:
        destino = destino + ".nuevo"
        print("Ya existe el archivo: dejo la versión nueva al lado, en %s, para compararla." % destino)
    carpeta = os.path.dirname(destino)
    if carpeta:
        os.makedirs(carpeta, exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(texto)
    return destino


# ---------------------------------------------------------------- comprobar

def cabecera(md_path):
    with open(md_path, encoding="utf-8") as f:
        head = f.read(4000)
    ident = re.search(r"\*\*Identificador:\*\*\s*([A-Z]+-[A-Za-z]-\d{4}-\d+)", head)
    desc = re.search(r"\*\*Descargado:\*\*\s*(\d{4}-\d{2}-\d{2})", head)
    if not ident or not desc:
        raise ErrorBOE("%s no tiene la cabecera de este script (Identificador y Descargado)" % md_path)
    return ident.group(1), desc.group(1)


def bloques_indice(ident):
    raw = get("%s/id/%s/texto/indice" % (API, ident), "application/json")
    try:
        data = json.loads(raw.decode("utf-8"))["data"]
    except (ValueError, KeyError):
        raise ErrorBOE("índice no válido para %s" % ident)
    if isinstance(data, list):
        data = data[0] if data else {}
    bl = data.get("bloque", [])
    return bl if isinstance(bl, list) else [bl]


def comprobar(rutas):
    hay_cambios = False
    errores = False
    for ruta in rutas:
        try:
            ident, desc = cabecera(ruta)
            desde = desc.replace("-", "")
            cambiados = []
            for b in bloques_indice(ident):
                fa = re.sub(r"\D", "", str(b.get("fecha_actualizacion", "")))[:8]
                if fa and fa > desde:
                    cambiados.append((fa, b.get("titulo", ""), b.get("id", "")))
            ficha = re.sub(r"\D", "", metadatos(ident).get("fecha_actualizacion", ""))[:8]
        except ErrorBOE as e:
            errores = True
            print("ERROR  %s: %s" % (os.path.basename(ruta), e))
            continue
        nombre = os.path.basename(ruta)
        if not cambiados and ficha > desde:
            # La ficha de la norma cambia sin que cambie el texto cuando el BOE
            # anade referencias: p. ej. una sentencia del Tribunal Constitucional.
            hay_cambios = True
            print("AVISO  %s (%s): el texto no ha cambiado, pero el BOE actualizó la ficha de la "
                  "norma el %s (referencias nuevas, p. ej. sentencias del Constitucional). Mirar: "
                  "%s/buscar/doc.php?id=%s (pestaña Análisis)" % (nombre, ident, iso(ficha), BOE, ident))
            continue
        if not cambiados:
            print("SIN CAMBIOS  %s (%s) desde la descarga del %s" % (nombre, ident, desc))
            continue
        hay_cambios = True
        print("CAMBIOS  %s (%s): %d bloque(s) actualizado(s) después del %s"
              % (nombre, ident, len(cambiados), desc))
        for fa, tit, bid in sorted(cambiados):
            print("    %s  %s  [bloque %s]" % (iso(fa), tit, bid))
    if errores:
        return 2
    return 1 if hay_cambios else 0


# ---------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description="Texto consolidado del BOE a Markdown citable.")
    ap.add_argument("identificador", nargs="?", help="p. ej. BOE-A-1954-15431")
    ap.add_argument("-o", "--salida", help="archivo .md de destino (sin -o, por pantalla)")
    ap.add_argument("--a-fecha", metavar="AAAA-MM-DD",
                    help="redacción vigente en esa fecha en lugar de la de hoy")
    ap.add_argument("--sobrescribir", action="store_true", help="reemplaza el archivo de destino")
    ap.add_argument("--comprobar", nargs="+", metavar="ARCHIVO.md",
                    help="lista los artículos cambiados en el BOE desde la fecha de descarga")
    a = ap.parse_args(argv)

    try:
        if a.comprobar:
            rutas = []
            for patron in a.comprobar:
                rutas.extend(sorted(glob.glob(patron)) or [patron])
            return comprobar([r for r in rutas if r.endswith(".md")])
        if not a.identificador:
            ap.error("falta el identificador del BOE (o --comprobar)")
        if not ID_RE.match(a.identificador):
            ap.error("identificador con formato no válido: %s (se espera algo como BOE-A-1954-15431)"
                     % a.identificador)
        if a.a_fecha and not re.match(r"^\d{4}-\d{2}-\d{2}$", a.a_fecha):
            ap.error("--a-fecha va como AAAA-MM-DD")
        texto, avisos = descargar(a.identificador, a.a_fecha)
    except ErrorBOE as e:
        print("ERROR: %s" % e, file=sys.stderr)
        return 2

    for av in avisos:
        print("AVISO: " + av, file=sys.stderr)
    if a.salida:
        destino = escribir(a.salida, texto, a.sobrescribir)
        n = sum(1 for l in texto.splitlines() if l.startswith("###### "))
        print("Escrito %s: %d KB, %d artículos como encabezado." % (destino, int(round(len(texto.encode("utf-8")) / 1000.0)), n))
    else:
        sys.stdout.write(texto)
    return 0


if __name__ == "__main__":
    sys.exit(main())
