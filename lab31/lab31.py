import matplotlib.pyplot as plot
import seaborn
import pandas

file_path = "Listado_Colegios_limpio.csv"
df_visualizacion = pandas.read_csv(file_path)

df_visualizacion.columns = df_visualizacion.columns.str.lower()
print(f"Nombre de las columnas del dataset:\n{df_visualizacion.columns}")

seaborn.set_theme(style="darkgrid")

TIPO_ESTABLECIMIENTO = "tipo_establecimiento"
ZONA = "zona"

if TIPO_ESTABLECIMIENTO in df_visualizacion.columns:
    plot.figure(figsize=(10, 6))
    distribucion_tipo = df_visualizacion[TIPO_ESTABLECIMIENTO].value_counts()
    distribucion_tipo.plot(kind="bar", color=["#1f77b4", "#ff7f0e"], edgecolor="black")
    plot.title("Distribución por Tipo de Establecimiento", fontsize=16, weight="bold")
    plot.xlabel("Tipo de Establecimiento", fontsize=12)
    plot.ylabel("Cantidad de Colegios", fontsize=12)
    plot.xticks(rotation=45, ha="right", fontsize=10)
    plot.tight_layout()
    plot.show()
else:
    print(f"La columna \"{TIPO_ESTABLECIMIENTO}\" no existe en el dataset.")

if ZONA in df_visualizacion.columns:
    plot.figure(figsize=(8, 8))
    distribucion_zona = df_visualizacion[ZONA].value_counts()
    colors = ["#2ca02c", "#d62728", "#ffbb78"]
    distribucion_zona.plot(kind="pie", autopct="%1.1f%%", colors=colors, startangle=90, explode=[0.05, 0.05, 0.05], shadow=True)
    plot.title("Distribución de Colegios por Zona (Urbana vs Rural)", fontsize=16, weight="bold")
    plot.ylabel("")
    plot.tight_layout()
    plot.show()
else:
    print(f"La columna \"{ZONA}\" no existe en el dataset.")

if ZONA in df_visualizacion.columns and TIPO_ESTABLECIMIENTO in df_visualizacion:
    crosstab = pandas.crosstab(df_visualizacion[ZONA], df_visualizacion[TIPO_ESTABLECIMIENTO])
    crosstab.plot(kind="bar", stacked=True, color=["#1f77b4", "#ff7f0e"], figsize=(10, 6), edgecolor="black")
    plot.title("Distribución de Colegios por Zona y Tipo de Establecimiento", fontsize=16, weight="bold")
    plot.xlabel("Zona", fontsize=12)
    plot.ylabel("Cantidad de Colegios", fontsize=12)
    plot.xticks(rotation=0)
    plot.tight_layout()
    plot.show()
else:
    print(f"No se encontró la columna \"{ZONA}\" o \"{TIPO_ESTABLECIMIENTO}\" en el dataset.")
