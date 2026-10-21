# Encargos

Una carpeta por expediente. **No se suben al repositorio**: aquí hay datos de
clientes.

```
encargos/
├─ 2026-014-valoracion-parcelas/
│  ├─ FICHA-ENCARGO.md      lo primero que se genera
│  ├─ entrada/              lo que llega, tal cual: designación, escrituras, catastro,
│  │  └─ jurisprudencia/    resoluciones, hojas de aprecio, testigos, correos…
│  └─ salida/               informe.docx, calculos.xlsx, auditoria.xlsx
└─ promocion-<nombre>/      la línea promotora, siempre en su propia carpeta
   ├─ entrada/              modelo financiero .xlsx y deck de referencia
   └─ salida/
```

En `entrada/` va el material como llegue, sin ordenar. Ese desorden es el punto
de partida normal. Las sentencias que se vayan a citar, en PDF, en
`entrada/jurisprudencia/`: una sentencia que no está ahí no existe.
