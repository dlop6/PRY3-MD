import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from scipy import stats

CSV_PATH = os.path.join('data','datos.csv')
OUTPUTS_DIR = 'outputs'
PERSONA2_FIGURES_DIR = os.path.join(OUTPUTS_DIR, 'figures', 'persona2')
os.makedirs(PERSONA2_FIGURES_DIR, exist_ok=True)

print('Leyendo datos...')
df = pd.read_csv(CSV_PATH, sep=';', encoding='latin-1')
# Preparar df_p2
if 'Grupos etarios Uso Internet' in df.columns:
    df_p2 = df[df['Grupos etarios Uso Internet'] != 'Total'].copy()
else:
    df_p2 = df.copy()

# uso_pais
uso_pais = df_p2.groupby('País__ESTANDAR')['value'].agg(['mean','median','std','min','max','count']).round(2)
uso_pais = uso_pais.sort_values('mean', ascending=False)

# Fig 1: boxplot por pais
try:
    fig, ax = plt.subplots(figsize=(14,6))
    paises_ordenados = uso_pais.index.tolist()
    data_box_paises = [df_p2[df_p2['País__ESTANDAR']==p]['value'].dropna().values for p in paises_ordenados]
    bp = ax.boxplot(data_box_paises, patch_artist=True, medianprops=dict(color='darkred', linewidth=2))
    for patch in bp['boxes']:
        patch.set_facecolor('#87CEEB')
    ax.set_xticklabels(paises_ordenados, rotation=45, ha='right', fontsize=9)
    ax.set_ylabel('% usuarios de Internet', fontsize=11)
    ax.set_title('Distribución de adopción de Internet por país (excluyendo Total)')
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    out = os.path.join(PERSONA2_FIGURES_DIR, 'fig_p2_boxplot_paises.png')
    plt.savefig(out, dpi=120, bbox_inches='tight')
    plt.close(fig)
    print('Generado:', out)
except Exception as e:
    print('Error generando boxplot pais:', e)

# Fig 2: evolución temporal global
try:
    evol_anio = df_p2.groupby('Años__ESTANDAR')['value'].agg(['mean','std','count']).reset_index()
    evol_anio['se'] = evol_anio['std'] / np.sqrt(evol_anio['count'])
    evol_anio['ci_lower'] = evol_anio['mean'] - 1.96 * evol_anio['se']
    evol_anio['ci_upper'] = evol_anio['mean'] + 1.96 * evol_anio['se']
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(evol_anio['Años__ESTANDAR'], evol_anio['mean'], marker='o', linewidth=2.5, color='#2c3e50')
    ax.fill_between(evol_anio['Años__ESTANDAR'], evol_anio['ci_lower'], evol_anio['ci_upper'], alpha=0.3, color='#3498db')
    ax.set_xlabel('Año')
    ax.set_ylabel('% usuarios de Internet (promedio)')
    ax.set_title('Evolución temporal global del uso de Internet en ALC')
    ax.grid(True, alpha=0.3)
    ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    plt.tight_layout()
    out = os.path.join(PERSONA2_FIGURES_DIR, 'fig_p2_evolucion_temporal.png')
    plt.savefig(out, dpi=120, bbox_inches='tight')
    plt.close(fig)
    print('Generado:', out)
except Exception as e:
    print('Error generando evolucion temporal:', e)

# Fig 3: cobertura por año (n países con dato)
try:
    paises_por_anio = df_p2.groupby('Años__ESTANDAR')['País__ESTANDAR'].nunique()
    fig, ax = plt.subplots(figsize=(12,5))
    ax.bar(paises_por_anio.index, paises_por_anio.values, color='#27ae60', alpha=0.8, edgecolor='black', linewidth=1.2)
    ax.set_xlabel('Año')
    ax.set_ylabel('Número de países con dato')
    ax.set_title('Cobertura de países por año')
    ax.set_ylim(0, 14)
    ax.axhline(y=13, color='r', linestyle='--', alpha=0.5)
    ax.grid(axis='y', alpha=0.3)
    ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    plt.tight_layout()
    out = os.path.join(PERSONA2_FIGURES_DIR, 'fig_p2_cobertura_anios.png')
    plt.savefig(out, dpi=120, bbox_inches='tight')
    plt.close(fig)
    print('Generado:', out)
except Exception as e:
    print('Error generando cobertura por año:', e)

# Fig 4: boxplot por grupos
try:
    grupos_orden_list = [
        'edad de medicion a 17 años',
        '18 a 25 años de edad',
        '26 a 50 años de edad',
        '51 a 65 años',
        '66 años en adelante'
    ]
    data_box_grupos = [df_p2[df_p2['Grupos etarios Uso Internet'] == g]['value'].dropna().values for g in grupos_orden_list]
    fig, ax = plt.subplots(figsize=(12,6))
    bp = ax.boxplot(data_box_grupos, patch_artist=True, medianprops=dict(color='darkred', linewidth=2))
    colors_grupos = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f']
    for patch, color in zip(bp['boxes'], colors_grupos):
        patch.set_facecolor(color)
    labels_grupos = ['≤17 años', '18–25', '26–50', '51–65', '66+']
    ax.set_xticklabels(labels_grupos)
    ax.set_ylabel('% usuarios de Internet')
    ax.set_title('Distribución de adopción de Internet por grupo etario')
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    out = os.path.join(PERSONA2_FIGURES_DIR, 'fig_p2_boxplot_grupos.png')
    plt.savefig(out, dpi=120, bbox_inches='tight')
    plt.close(fig)
    print('Generado:', out)
except Exception as e:
    print('Error generando boxplot grupos:', e)

# Fig 5: evolucion por grupos
try:
    fig, ax = plt.subplots(figsize=(12,6))
    colors_lineas = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f']
    labels_grupos_full = ['≤17 años', '18–25', '26–50', '51–65', '66+']
    for grupo, color, label in zip(grupos_orden_list, colors_lineas, labels_grupos_full):
        grupo_data = df_p2[df_p2['Grupos etarios Uso Internet'] == grupo].groupby('Años__ESTANDAR')['value'].mean().sort_index()
        ax.plot(grupo_data.index, grupo_data.values, marker='o', linewidth=2.5, label=label, color=color)
    ax.set_xlabel('Año')
    ax.set_ylabel('% usuarios de Internet (promedio)')
    ax.set_title('Evolución temporal del uso de Internet por grupo etario')
    ax.legend(loc='lower right')
    ax.grid(True, alpha=0.3)
    ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ax.set_ylim(-5,105)
    plt.tight_layout()
    out = os.path.join(PERSONA2_FIGURES_DIR, 'fig_p2_evolucion_grupos.png')
    plt.savefig(out, dpi=120, bbox_inches='tight')
    plt.close(fig)
    print('Generado:', out)
except Exception as e:
    print('Error generando evolucion grupos:', e)

# Fig 6: outliers scatter
try:
    outliers_list = []
    for grupo in grupos_orden_list:
        grupo_data = df_p2[df_p2['Grupos etarios Uso Internet'] == grupo]['value']
        Q1 = grupo_data.quantile(0.25)
        Q3 = grupo_data.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df_p2[(df_p2['Grupos etarios Uso Internet'] == grupo) & ((df_p2['value'] < lower_bound) | (df_p2['value'] > upper_bound))]
        if len(outliers) > 0:
            outliers_list.append(outliers)
    if outliers_list:
        all_outliers = pd.concat(outliers_list).drop_duplicates()
    else:
        all_outliers = pd.DataFrame()
    fig, ax = plt.subplots(figsize=(12,6))
    if not all_outliers.empty:
        outlier_mask = df_p2.index.isin(all_outliers.index)
        ax.scatter(df_p2[~outlier_mask]['Años__ESTANDAR'], df_p2[~outlier_mask]['value'], alpha=0.5, s=50, color='#3498db')
        ax.scatter(df_p2[outlier_mask]['Años__ESTANDAR'], df_p2[outlier_mask]['value'], alpha=0.8, s=150, color='#e74c3c', marker='X', edgecolors='black')
    else:
        ax.scatter(df_p2['Años__ESTANDAR'], df_p2['value'], alpha=0.5, s=50, color='#3498db')
    ax.set_xlabel('Año')
    ax.set_ylabel('% usuarios de Internet')
    ax.set_title('Detección de outliers: value vs año')
    ax.grid(True, alpha=0.3)
    ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    plt.tight_layout()
    out = os.path.join(PERSONA2_FIGURES_DIR, 'fig_p2_outliers.png')
    plt.savefig(out, dpi=120, bbox_inches='tight')
    plt.close(fig)
    print('Generado:', out)
except Exception as e:
    print('Error generando outliers:', e)

print('Proceso terminado')
