# Laboratorio 30

## Sesión #30 Exploración, Limpieza y estadística descriptiva de los datos

**Título del Laboratorio:** Exploración, Limpieza y estadística descriptiva de los datos de las encuestas de Listado de colegios en Bogotá.

**Duración:** 2 horas

**Objetivos del Laboratorio:**

1. Desarrollar habilidades en la exploración y limpieza de datos utilizando la herramienta de Python, para asegurar que el conjunto de datos esté preparado para análisis posteriores.

**Materiales Necesarios:**

1. Computador con conexión a internet.
2. Dataset confiable de https://www.datos.gov.co
3. Herramientas de limpieza Python.

**Estructura del Laboratorio:**

Cargar el archivo `Listado_Colegios.csv` en la herramienta (Python) y realizar una exploración inicial.

1. Realizar la limpieza del Dataset y usando una herramienta de Python (revisar la estructura del dataset, identificando valores nulos o inconsistencias).

```python
import pandas

basename = "Listado_Colegios"
input_csv = basename+".csv"
output_csv = basename+"_limpio.csv"

dataframe = pandas.read_csv(input_csv)

print(f"Filas y columnas del dataset:\n{dataframe.shape}")

df_clean = dataframe.drop_duplicates()

print(f"Filas y columnas del dataset sin duplicados:\n{dataframe.shape}")

print(f"Verificar si hay valores nulos en el dataset:\n{df_clean.isnull().sum()}")

column_names = df_clean.columns
```
[Enlace a código completo de Python](lab30.py)

[Enlace a dataset limpio](Listado_Colegios_limpio.csv)

2. Realizar una descripción estadística básica (instituciones educativas vs. centros educativos, etc.).

    **Distribución de Tipos de Instituciones:** El dataset contiene información que puede ser clasificada en instituciones educativas (colegios) y centros educativos. Este desglose estadístico puede proporcionar información sobre la proporción entre distintos tipos de instituciones, su ubicación y cobertura.

    **Rango de Variables Numéricas:** La descripción estadística incluye la media, mínima y máxima de las variables numéricas (si las hubiera), lo cual ayuda a entender la variabilidad en el dataset.

3. Generar un informe preliminar con conclusiones y recomendaciones derivadas de esta fase.

#### Conclusiones:

1. La limpieza realizada elimina duplicados y rellena valores faltantes de una manera que respeta el tipo de cada variable.

2. La eliminación de columnas completamente nulas reduce la complejidad del dataset sin perder información relevante.

#### Recomendaciones:

1. Realizar una visualización gráfica de la distribución de tipos de instituciones para entender la proporción y distribución geográfica.

2. Realizar un análisis de correlación si existen variables numéricas, lo cual puede ayudar a detectar relaciones entre características del dataset.

3. Explorar posibles valores atípicos en variables numéricas importantes, lo cual puede mejorar la precisión del análisis futuro.
