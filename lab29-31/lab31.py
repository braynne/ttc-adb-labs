import matplotlib.pyplot as plt
import seaborn
import pandas

file_path = "listado_colegios_limpio.csv"
df_visualizacion = pandas.read_csv(file_path)

df_visualizacion.columns = df_visualizacion.columns.str.lower()
print(f"Nombre de las columnas del dataset:\n{df_visualizacion.columns}")

seaborn.set_theme(style="darkgrid")

if 'tipo_establecimiento' in df_visualizacion.columns:
    plt.figure(figsize=(10, 6))
    distribucion_tipo = df_visualizacion['tipo_establecimiento'].value_counts()
    distribucion_tipo.plot(kind='bar', color=['#1f77b4', '#ff7f0e'], edgecolor='black')
    plt.title('Distribución por Tipo de Establecimiento', fontsize=16, weight='bold')
    plt.xlabel('Tipo de Establecimiento', fontsize=12)
    plt.ylabel('Cantidad de Colegios', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.tight_layout()
    plt.show()
else:
    print("La columna 'tipo_establecimiento no existe en el dataset.'")

if 'zona' in df_visualizacion.columns:
    plt.figure(figsize=(8, 8))
    distribucion_zona = df_visualizacion['zona'].value_counts()
    colors = ['#2ca02c', '#d62728', '#ffbb78']
    distribucion_zona.plot(kind='pie', autopct='%1.1f%%', colors=colors, startangle=90, explode=[0.05, 0.05, 0.05], shadow=True)
    plt.title('Distribución de Colegios por Zona (Urbana vs Rural)', fontsize=16, weight='bold')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()
else:
    print("La columna 'zona' no existe en el dataset.")

if 'zona' in df_visualizacion.columns and 'tipo_establecimiento' in df_visualizacion:
    crosstab = pandas.crosstab(df_visualizacion['zona'], df_visualizacion['tipo_establecimiento'])
    crosstab.plot(kind='bar', stacked=True, color=['#1f77b4', '#ff7f0e'], figsize=(10, 6), edgecolor='black')
    plt.title('Distribución de Colegios por Zona y Tipo de Establecimiento', fontsize=16, weight='bold')
    plt.xlabel('Zona', fontsize=12)
    plt.ylabel('Cantidad de Colegios', fontsize=12)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
else:
    print("No se encontró la columna 'zona' o 'tipo_establecimiento' en el dataset.")