# Persona 1 — Avance Semana 2: Diseño del Dataset Transformado

**Fecha:** Semana 2  
**Responsable:** Persona 1  
**Entregable:** Diseño de estructura final + documentación

---

## Problema a Resolver

**Tipo:** Regresión  
**Objetivo:** Estimar el porcentaje de uso de Internet por país, año y grupo etario  
**Variable objetivo:** `porcentaje_internet` (0–100)  
**Referencia:** [informe_semana1.tex](docs/informe_semana1.tex) — Sección "Problema seleccionado"

---

## Unidad de Análisis

**Definición:** Cada observación (fila) representa el porcentaje de usuarios de Internet en un **país, año y grupo etario específico**.

**Período:** 2016–2022 (datos confiables post-2016, según Semana 1)  
**Filtros:** 
- Solo años 2016–2022
- Solo grupos etarios específicos (sin "Total")

**Tamaño esperado:** ~455 filas (13 países × 7 años × 5 grupos etarios)

---

## Columnas del Dataset Transformado

| Columna | Tipo | Origen | Descripción |
|---------|------|--------|-------------|
| `pais` | string | `País__ESTANDAR` | Nombre del país (13 únicos) |
| `año` | int | `Años__ESTANDAR` | Año (2016–2022) |
| `years_since_2016` | int | derivada | Años desde 2016 (0–6); captura tendencia temporal |
| `grupo_etario` | string | `Grupos etarios Uso Internet` | Grupo de edad (5 grupos) |
| `porcentaje_internet` | float | `value` | **Variable objetivo** (0–100) |

---

## Transformaciones Necesarias

### Columnas a CONSERVAR
- `País__ESTANDAR` → renombrar a `pais`
- `Grupos etarios Uso Internet` → renombrar a `grupo_etario`
- `value` → renombrar a `porcentaje_internet`

### Columnas a TRANSFORMAR
- `Años__ESTANDAR` → crear columna derivada `years_since_2016` (valor - 2016)

### Columnas a ELIMINAR
- `indicator` — valor fijo sin variabilidad
- `unit` — valor fijo
- `notes_ids` — mayormente vacío
- `source_id` — identificador de fuente, sin valor predictivo

---

## Justificación de la Estructura

### ¿Por qué el formato original no sirve para ML?

1. **Carencia de variables temporales numéricas**
   - Año es dimensión, no variable. Necesitamos capturar tendencia explícitamente.

2. **Columnas redundantes**
   - `indicator`, `unit`, `source_id` son constantes. Ruido para el modelo.

3. **Formato tabular directo requerido**
   - Para regresión: variables independientes en columnas, variable objetivo aislada, una fila = una observación.

### Ventajas del diseño propuesto

✅ **Tabular:** Cada fila es independiente, estructura estándar para ML  
✅ **Temporal:** `years_since_2016` permite capturar dinámicas de crecimiento  
✅ **Limpio:** Sin redundancias ni ruido  
✅ **Alineado:** Estructura 1-a-1 con el problema de regresión  
✅ **Período confiable:** Solo 2016–2022 (datos post-2016 validados en Semana 1)

---

## Decisiones Registradas

| Decisión | Valor | Justificación |
|----------|-------|---------------|
| Unidad de análisis | país-año-grupo | Estructura requerida para regresión supervisada |
| Período | 2016–2022 | Confiabilidad post-2016 (Semana 1) |
| Grupo "Total" | Eliminar | Solo grupos etarios específicos para modelar variabilidad por edad |
| Variables derivadas | `years_since_2016` solo | Persona 2 añade dummies, retardos, etc. si necesita en implementación |
| Columnas eliminadas | `indicator`, `unit`, `notes_ids`, `source_id` | Sin valor predictivo |

---

## Referencias en el Notebook

- **Sección:** `PERSONA 1: Diseño del Dataset Transformado`
- **Subsecciones:**
  1. Análisis del Formato Original
  2. Clasificación de Columnas
  3. Propuesta de Estructura Final
  4. Justificación del Diseño

- **Archivo:** [notebooks/02_semana2_transformacion.ipynb](notebooks/02_semana2_transformacion.ipynb)

---

## Próximos Pasos

**→ Persona 2:** Implementar transformación del CSV según diseño  
**→ Persona 3:** Validar calidad y manejo de faltantes  
**→ Persona 4:** Integrar y preparar entrega final

---

**Estado:** ✅ Diseño completado  
**Bloqueadores:** Ninguno  
**Notas:** El diseño está listo. Persona 2 puede comenzar implementación inmediatamente.
