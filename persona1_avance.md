# Persona 1 — Avance Semana 1: Exploración del Dataset

**Proyecto:** PRY3-MD | Universidad del Valle de Guatemala | Semestre I 2026  
**Responsable:** Roberto Barreda #23354  
**Fecha:** 2026-04-30  
**Notebook de referencia:** [01_semana1_eda.ipynb](01_semana1_eda.ipynb)

---

## 1. Descripción del dataset

El dataset proviene de **CEPALSTAT**, el repositorio estadístico de la Comisión Económica para América Latina y el Caribe (CEPAL / Naciones Unidas). El archivo descargado es `data/data_1777144519.xlsx`.

**Nombre del indicador:**  
*Personas usuarias de Internet por grupo etario, países seleccionados América Latina y el Caribe, 2000 a 2022*

**Temática:** Tecnologías de Información y Comunicación > Uso individual de TIC  
**ID del indicador:** 4987  
**Última actualización de la fuente:** 19 de mayo de 2025

El indicador mide, para cada país y año, el **porcentaje de personas que usan Internet** dentro de cada grupo de edad. El cálculo es:

```
valor = 100 × (usuarios de Internet en el grupo etario / total de personas en ese grupo)
```

Se contabiliza el uso de Internet desde **cualquier lugar, dispositivo y tipo de conexión** (fija o móvil).

---

## 2. Estructura del archivo Excel

El Excel contiene **cinco hojas** que fueron exportadas individualmente a la carpeta `data/`:

| Hoja | Archivo CSV | Contenido |
|------|-------------|-----------|
| `datos` | `datos.csv` | Serie de tiempo principal (870 filas de datos) |
| `metadatos` | `metadatos.csv` | Descripción, definición, metodología y unidades |
| `fuentes` | `fuentes.csv` | Información de la organización fuente (CEPAL) |
| `notas` | `notas.csv` | Notas aclaratorias (vacío en este dataset) |
| `creditos` | `creditos.csv` | Créditos, fecha de descarga y organización |

El análisis de hojas se realiza en la **Sección 2** del notebook ([01_semana1_eda.ipynb](01_semana1_eda.ipynb#exploración-del-archivo-excel)).

---

## 3. Significado de cada fila

Cada fila del dataset `datos.csv` representa una **observación única** definida por tres coordenadas:

> **País** + **Grupo etario** + **Año** → **Porcentaje de usuarios de Internet**

Por ejemplo, la fila:

```
Argentina | 18 a 25 años de edad | 2020 | 95
```

significa que en Argentina, en el año 2020, el **95 % de las personas de entre 18 y 25 años usaba Internet**.

---

## 4. Descripción de columnas principales

| Columna | Tipo | Descripción |
|---------|------|-------------|
| `indicator` | texto | Nombre completo del indicador. Constante en todo el dataset — no aporta variabilidad al modelo. |
| `País__ESTANDAR` | texto | Nombre estandarizado del país (13 países de América Latina). |
| `Grupos etarios Uso Internet` | texto | Grupo de edad de los usuarios medidos. |
| `Años__ESTANDAR` | entero | Año de la encuesta de hogares. |
| `value` | entero | Porcentaje de personas usuarias de Internet en ese grupo etario y año. Rango: 0–100. |
| `unit` | texto | Unidad de medición. Constante: *"Porcentaje sobre el total de personas en cada grupo etario"*. |
| `notes_ids` | float | ID de nota aclaratoria. Vacío en casi todos los registros. |
| `source_id` | entero | ID de la organización fuente. Valor único: `9353` (CEPAL). |

El análisis detallado de columnas se encuentra en la **Sección 4** del notebook.

---

## 5. Países incluidos

El dataset cubre **13 países** de América Latina y el Caribe:

| # | País |
|---|------|
| 1 | Argentina |
| 2 | Bolivia (Estado Plurinacional de) |
| 3 | Brasil |
| 4 | Chile |
| 5 | Colombia |
| 6 | Costa Rica |
| 7 | Ecuador |
| 8 | El Salvador |
| 9 | Honduras |
| 10 | Panamá |
| 11 | Paraguay |
| 12 | Perú |
| 13 | Uruguay |

> **Nota metodológica:** La edad mínima de medición varía por país. Por ejemplo, Argentina mide desde los 4 años, Chile y Colombia desde los 5 años, y Brasil desde los 10 años. Esto afecta la comparabilidad directa del grupo "≤17 años" entre países.

El listado completo con número de registros por país se genera en la **Sección 5** del notebook.

---

## 6. Años disponibles

El rango general del dataset es **2000–2022**, pero la cobertura **no es uniforme** entre países:

- Algunos países tienen datos desde los primeros años de la década de 2000.
- Otros solo cuentan con cobertura más tardía y esporádica.
- El año más reciente varía según país.
- El número total de años distintos en el dataset es aproximadamente **21**.

Esta heterogeneidad genera un **panel desbalanceado** que debe ser tratado en el preprocesamiento. El análisis de cobertura temporal por país se realiza en la **Sección 6** del notebook.

---

## 7. Grupos etarios incluidos

El dataset registra **6 categorías** de grupo etario:

| Categoría | Descripción |
|-----------|-------------|
| `edad de medicion a 17 años` | Menores de edad (≤17 años) |
| `18 a 25 años de edad` | Jóvenes adultos |
| `26 a 50 años de edad` | Adultos en edad productiva |
| `51 a 65 años` | Adultos mayores en actividad |
| `66 años en adelante` | Adultos mayores (tercera edad) |
| `Total` | Agregado de toda la población — **no es un grupo etario real** |

Los promedios históricos de uso de Internet muestran que los grupos más jóvenes (18–25 y 26–50) tienen consistentemente las tasas más altas, mientras que los mayores de 66 años presentan los valores más bajos. El análisis de grupos se encuentra en la **Sección 7** del notebook.

---

## 8. Observaciones generales sobre el dataset

### Calidad de datos
- La columna `notes_ids` está vacía en la mayoría de registros.
- Las columnas `indicator`, `unit` y `source_id` son constantes en todo el dataset y deben eliminarse antes de modelar.
- El grupo `Total` es un agregado calculado y no debe mezclarse con los grupos etarios reales en un modelo predictivo.

### Cobertura y completitud
- El panel de datos es **desbalanceado**: no todos los países tienen datos en todos los años.
- Algunos países solo tienen observaciones en años no consecutivos (ej. Bolivia tiene 2009, 2012, 2013...).

### Tendencia general observable
- Se observa una **tendencia creciente** en el uso de Internet en todos los grupos etarios y países a lo largo del tiempo.
- El aumento más pronunciado entre 2019 y 2020 en varios países coincide con el contexto de la pandemia de COVID-19.

---

## 9. Por qué el dataset no está listo para Machine Learning

El dataset está en **formato largo** (*long format*): una fila por combinación país + grupo etario + año. Para la mayoría de algoritmos de ML supervisado se requiere un **formato ancho** donde cada instancia (fila) sea una unidad de análisis completa con todas sus características como columnas.

Las transformaciones necesarias antes de modelar son:

1. **Pivotear** el formato largo a ancho (grupos etarios como columnas de features).
2. **Filtrar o imputar** los años con cobertura incompleta entre países.
3. **Eliminar columnas redundantes** (`indicator`, `unit`, `source_id`).
4. **Codificar variables categóricas** (`País__ESTANDAR`, `Grupos etarios Uso Internet`).
5. **Separar el grupo `Total`** del resto de grupos etarios.
6. **Definir la variable objetivo** (¿predecir el valor de un año futuro?, ¿clasificar nivel de adopción?).

El análisis completo de limitaciones se desarrolla en la **Sección 10** del notebook ([01_semana1_eda.ipynb](01_semana1_eda.ipynb)).

---

## 10. Referencias

- **Notebook de análisis:** [01_semana1_eda.ipynb](01_semana1_eda.ipynb)
- **Dataset principal:** [data/datos.csv](data/datos.csv)
- **Metadatos del indicador:** [data/metadatos.csv](data/metadatos.csv)
- **Fuente original:** CEPALSTAT — [http://www.eclac.org/](http://www.eclac.org/)
- **Archivo Excel fuente:** [data/data_1777144519.xlsx](data/data_1777144519.xlsx)
