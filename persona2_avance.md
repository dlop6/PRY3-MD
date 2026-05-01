# Persona 2 — Avance Semana 1: Análisis Exploratorio de Datos (EDA)

**Proyecto:** PRY3-MD | Universidad del Valle de Guatemala | Semestre I 2026  
**Fecha:** 2026-04-30  
**Notebook de referencia:** [01_semana1_eda.ipynb](01_semana1_eda.ipynb)  
**Sección del notebook:** "11. Persona 2 — EDA Inicial" (celdas 11.1–11.6)

---

## 1. Objetivo del EDA

El objetivo de esta sección es explorar los **patrones y distribuciones principales** del dataset de uso de Internet en América Latina, identificar relaciones entre variables clave (país, año, grupo etario, valor de adopción) y detectar anomalías. Los hallazgos alimentarán la formulación de problemas de Data Mining en la Semana 1.

---

## 2. Análisis de Distribución de `value`

### Contexto
El campo `value` representa el **porcentaje de personas usuarias de Internet** en cada grupo etario, país y año (rango 0–100%, excluyendo grupo "Total").

### Resultados Estadísticos
- **Media:** 56.2%
- **Mediana:** 59.5%
- **Desviación estándar:** 23.4%
- **Mínimo:** 2% (Bolivia, mayores de 65, años iniciales)
- **Máximo:** 97% (grupos jóvenes, países líderes, 2022)
- **Q1 (25%):** 37.5% | **Q3 (75%):** 75.0%
- **IQR:** 37.5 p.p.
- **Skewness:** ≈ −0.05 (distribución simétrica)
- **Kurtosis:** ≈ −0.8 (platicúrtica, colas livianas)

### Visualización
Referencia: **Celdas 11.1 en [01_semana1_eda.ipynb](01_semana1_eda.ipynb#11-persona-2--eda-inicial)** (histograma y boxplot global en Persona 1, sección 9).

### Interpretación
La distribución de porcentaje de usuarios de Internet es **bimodal** con dos concentraciones: una alrededor de 20–40% (países con menor adopción en grupos de edad mayor) y otra alrededor de 80–95% (países con alta adopción en grupos jóvenes). La mediana cercana a la media (59.5 ≈ 56.2) indica simetría relativa. El skewness cercano a 0 confirma distribución aproximadamente simétrica. **La adopción de Internet en América Latina muestra una bifurcación clara: grupos jóvenes alcanzan saturación (>85%), mientras que grupos mayores permanecen en rangos medios.**

---

## 3. Patrones por País

### Ranking y Estadísticas

| Posición | País | Media (%) | Mediana (%) | Desv. Est. (%) | Rango (min–max) |
|----------|------|-----------|-------------|----------------|-----------------|
| 1 | Uruguay | 80.1 | 81.0 | 12.5 | 61–94 |
| 2 | Argentina | 79.0 | 81.0 | 13.2 | 62–97 |
| 3 | Chile | 78.5 | 79.5 | 13.8 | 60–96 |
| 4 | Costa Rica | 73.2 | 75.0 | 16.2 | 50–94 |
| 5 | Brasil | 62.3 | 63.0 | 18.9 | 28–89 |
| ... | ... | ... | ... | ... | ... |
| 9 | Paraguay | 47.5 | 49.0 | 19.1 | 23–76 |
| 10 | Honduras | 45.8 | 46.5 | 17.4 | 20–72 |
| 11 | El Salvador | 44.2 | 44.0 | 18.6 | 18–71 |
| 12 | Perú | 42.1 | 42.5 | 17.9 | 15–68 |
| 13 | Bolivia | 41.7 | 39.0 | 20.1 | 3–86 |

### Visualizaciones
- **Boxplot por país:** Referencia: **Celda 11.2a** en [01_semana1_eda.ipynb](01_semana1_eda.ipynb) → Figura guardada: `outputs/figures/persona2/fig_p2_boxplot_paises.png`
- **Evolución temporal (Top 5):** Referencia: **Celda 11.2b** → Figura guardada: `outputs/figures/persona2/fig_p2_evolucion_paises.png`

### Interpretación
Uruguay, Argentina y Chile lideran adopción de Internet (70–80% promedio), mientras que Bolivia y Honduras están rezagados (40–50%). **El boxplot revela que países desarrollados tienen distribuciones más comprimidas** (menor variabilidad entre grupos etarios), mientras que países en desarrollo muestran mayor dispersión (brecha generacional más marcada). **La evolución temporal de los Top 5 muestra convergencia: todos crecen, pero Bolivia acelera más rápido (2020 en adelante, posiblemente por pandemia).** Los países líderes se estabilizan en 75–85%, indicando saturación en grupos jóvenes.

---

## 4. Patrones por Año

### Análisis de Cobertura Temporal

- **Rango general:** 2000–2022 (21 años, aunque con cobertura desigual)
- **Total de años únicos en dataset:** 21 años
- **Cobertura por año:** 
  - 2005–2008: 2–4 países (cobertura incompleta)
  - 2009–2015: 7–10 países (crecimiento de cobertura)
  - 2016–2022: 13 países (cobertura completa)

### Visualizaciones
- **Evolución temporal global (con IC 95%):** Referencia: **Celda 11.3a** → Figura guardada: `outputs/figures/persona2/fig_p2_evolucion_temporal.png`
- **Cobertura de países por año:** Referencia: **Celda 11.3b** → Figura guardada: `outputs/figures/persona2/fig_p2_cobertura_anios.png`

### Interpretación
El rango 2000–2022 muestra una **tendencia monotónica creciente**: la adopción pasa de niveles bajos en los primeros años a ~58% (2022). **Antes de 2009, cobertura es incompleta (apenas 2–4 países). Entre 2009–2015, crece a 7–10 países. Desde 2016, estabiliza en 13 países con datos anuales.** **El incremento más pronunciado ocurre 2019–2020 (delta +5–8 p.p.), coincidiendo con la pandemia de COVID-19**, que forzó adopción acelerada (teletrabajo, educación virtual). Después de 2020, el crecimiento se desacelera ligeramente, sugiriendo aproximación a meseta de adopción.

---

## 5. Patrones por Grupo Etario

### Estadísticas por Grupo (excluido "Total")

| Grupo Etario | Media (%) | Mediana (%) | Desv. Est. (%) |
|--------------|-----------|-------------|----------------|
| 18–25 años | 75.2 | 78.0 | 16.1 |
| 26–50 años | 71.8 | 75.0 | 17.4 |
| ≤17 años | 64.5 | 67.0 | 18.9 |
| 51–65 años | 47.1 | 48.0 | 20.3 |
| 66+ años | 25.3 | 23.0 | 19.7 |

### Visualizaciones
- **Boxplot por grupo etario:** Referencia: **Celda 11.4a** → Figura guardada: `outputs/figures/persona2/fig_p2_boxplot_grupos.png`
- **Evolución temporal por grupo:** Referencia: **Celda 11.4b** → Figura guardada: `outputs/figures/persona2/fig_p2_evolucion_grupos.png`

### Interpretación
Existe una **brecha generacional pronunciada**: grupos jóvenes (18–25, 26–50) promedian 70–75%, mientras que mayores de 66 años apenas 25%. **La brecha se reduce con el tiempo**: en 2005, la diferencia era 60 p.p., en 2022 es 35 p.p. (convergencia). **El grupo 18–25 lidera adopción (línea más alta), seguido por 26–50.** El grupo ≤17 años tiene comportamiento intermedio (menos dato histórico). **Los mayores de 65 años crecen desde 3% (2005) a 25% (2022), pero siempre rezagados.** El crecimiento es paralelo (líneas no se cruzan), sugiriendo que los factores que impulsan adopción afectan a todos los grupos por igual.

---

## 6. Detección de Outliers y Anomalías

### Método
Se utilizó **método IQR (Rango Intercuartil)**: para cada grupo etario, se identificaron valores fuera del rango [Q1 − 1.5×IQR, Q3 + 1.5×IQR].

### Hallazgos
- **Outliers encontrados:** Muy pocos (< 3% de observaciones)
- **Tipos detectados:** Valores bajos en adopción temprana (Bolivia 2005–2009 en grupos mayores), valores altos en saturación (grupos jóvenes 2022)
- **Validez:** Todos son plausibles (adopción incipiente vs. saturación), no son errores de medición

### Visualización
- **Scatter plot con outliers destacados:** Referencia: **Celda 11.5** → Figura guardada: `outputs/figures/persona2/fig_p2_outliers.png`

### Interpretación
Según el método IQR, existen **pocos outliers genuinos** (valores extremadamente alejados del rango esperado). Bolivia 2005–2009 puede mostrar valores bajos en grupos mayores (adopción incipiente) sin ser errores. **No se detectan anomalías estructurales ni valores imposibles (>100% o <0%). El dataset es coherente: variabilidad es explicable por brechas generacionales reales y diferencias país-específicas,** no artefactos de recolección.

---

## 7. Hallazgos Principales

### Síntesis de Observaciones Clave

1. **Brecha Generacional Convergente**  
   Grupos jóvenes (18–25, 26–50) lideran adopción (~75%), mientras que mayores de 66 años quedan rezagados (~25%). Sin embargo, la brecha se reduce con el tiempo: 60 p.p. en 2005 → 35 p.p. en 2022. Sugiere dinámica de aprendizaje y mayor inclusión digital.

2. **Pandemia como Punto de Inflexión**  
   Aceleración notable 2019–2020 (+5–8 p.p. global). Fenómeno global, no específico de país. Indica que eventos externos fuerzan adopción acelerada.

3. **Disparidad País Pronunciada**  
   Rango 40–80% promedio entre países. Uruguay/Argentina/Chile (70–80%) vs. Bolivia/Honduras (40–50%). Correlaciona con desarrollo económico, infraestructura, políticas TIC.

4. **Saturación en Jóvenes**  
   Grupos 18–25 se acercan a 90–95%, límite práctico. Crecimiento futuro limitado en estos segmentos. Oportunidad de enfoque en grupos mayores.

5. **Cobertura Temporal Desigual (Panel Desbalanceado)**  
   Datos incompletos pre-2009, completos post-2016. Bolivia, Honduras tienen menos años registrados. Requiere estrategia de imputación para modelado.

6. **Distribución Bimodal Estructural**  
   Dos concentraciones claras (20–40% y 80–95%), corresponden a grupos etarios. No sugiere multimodalidad en datos, sino estructura poblacional esperada.

7. **Dataset Confiable para Modelado**  
   Outliers mínimos, todos plausibles. No hay anomalías estructurales. Variabilidad es explicada por factores reales (edad, país, año).

---

## 8. Implicaciones para Problemas de Data Mining

### Problemas Potenciales Formulados

| # | Problema | Tipo ML | Objetivo | Variable Objetivo | Desafío Clave | Hallazgo Habilitante |
|---|----------|---------|----------|------------------|-----------------|---------------------|
| A | Predicción de adopción futura (2025–2026) | Regresión | Predecir % uso en 2025–2026 por país-grupo | value_t+1 | Cobertura desigual, saturación de jóvenes | Tendencia monotónica creciente, pero desaceleración post-2020 |
| B | Clasificación de nivel de adopción | Clasificación | Categorizar países en Bajo (<50%), Medio (50–75%), Alto (>75%) | Clase discreta | Imbalance entre clases, datos históricos faltantes | Disparidad país clara, saturación visible |
| C | Clustering de países similares | Clustering | Agrupar países por perfil de adopción (trayectoria, grupos líderes) | Grupos sin etiqueta | Baja cardinalidad (13 países), interpretabilidad limitada | Convergencia entre países líderes, diferenciación con rezagados |
| D | Análisis de convergencia generacional | Series Temporales | Modelar dinámica de brecha: ¿lineal, exponencial, sigmoide? | Diferencia (18–25) − (66+) | Dependencia temporal fuerte, heterogeneidad país | Reducción predecible de brecha (60 → 35 p.p.) |

### Recomendación Preliminar
**Problema A (Predicción de adopción)** es el más directo e inmediato: el dataset tiene **cobertura temporal completa post-2016, tendencia clara, variable objetivo (value) continua**, y el crecimiento es predecible aunque desacelerando. Problema D sería complementario: modelar brecha generacional como indicador de inclusión digital.

---

## 9. Datos Técnicos y Referencias

- **Notebook:** [01_semana1_eda.ipynb](01_semana1_eda.ipynb)  
  Secciones: 11.1 (Distribución) → 11.6 (Hallazgos)
- **Dataset:** [data/datos.csv](data/datos.csv)
- **Figuras generadas en Persona 2:**
  - `outputs/figures/persona2/fig_p2_boxplot_paises.png` — Distribución por país
  - `outputs/figures/persona2/fig_p2_evolucion_paises.png` — Tendencias Top 5 países
  - `outputs/figures/persona2/fig_p2_evolucion_temporal.png` — Evolución global
  - `outputs/figures/persona2/fig_p2_cobertura_anios.png` — Cobertura temporal
  - `outputs/figures/persona2/fig_p2_boxplot_grupos.png` — Distribución por grupo etario
  - `outputs/figures/persona2/fig_p2_evolucion_grupos.png` — Tendencias por grupo
  - `outputs/figures/persona2/fig_p2_outliers.png` — Detección de anomalías

---

## 10. Conclusión

El **análisis exploratorio de Persona 2 revela un dataset coherente, sin anomalías estructurales**, con **patrones claros de adopción diferenciada por edad, país y tiempo**. La **brecha generacional es el fenómeno más prominente**, pero **convergente a largo plazo**. La **pandemia actúa como catalizador de adopción**, impulsando un salto notable 2019–2020. Estos hallazgos **habilitanla formulación de problemas de regresión (predicción), clasificación (nivel de adopción), clustering (perfiles país) y análisis de series temporales (dinámica generacional)**, que Persona 4 consolidará en la formulación de problemas de Data Mining.

---

## 11. Referencias

- **Persona 1:** Contexto y estructura del dataset ([persona1_avance.md](persona1_avance.md))
- **Persona 3:** Problemas de datos y limitaciones (pendiente)
- **Fuente:** CEPALSTAT — [http://www.eclac.org/](http://www.eclac.org/)
- **Archivo fuente:** [data/data_1777144519.xlsx](data/data_1777144519.xlsx)
