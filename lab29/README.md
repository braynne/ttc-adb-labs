# Laboratorio 29

## Sesión #29 Carga y Exploración de Datos

**Título del Laboratorio:** Análisis Inicial de Datos de Colegios en Bogotá.

**Duración:** 2 horas

**Objetivos del Laboratorio:**

1. Realizar un proceso integral de búsqueda, cargue y exploración del dataset de colegios, utilizando herramienta de Python (Google Colab), con el fin de comprender la estructura de los datos, identificar posibles problemas de calidad, y preparar un informe que resuma los hallazgos iniciales.

**Materiales Necesarios:**

1. Computador con conexión a internet.
2. Dataset confiable de https://www.datos.gov.co
3. Herramienta (Python).

**Estructura del Laboratorio:**

Cargar los datos del dataset `Listado_Colegios.csv`

1. **Informe de Resultados de la Búsqueda, Cargue y Exploración de Datos:**

    - **Descripción del Dataset:** Incluyendo el origen de los datos, las variables clave, y la relevancia para el análisis.
    
        El archivo `Listado_Colegios.csv` contiene datos de colegios, que posiblemente incluye variables como nombres, ubicaciones, tipos de colegios, niveles educativos, entre otros. Esta información es relevante para entender la distribución de colegios y sus características, lo que puede ser útil para tomar decisiones en sectores educativos o administrativos.
    
    - **Resumen de la Carga de Datos:** Evidencia de que los datos se cargaron correctamente en Excel y Google Colab.
    
        En el código proporcionado (`lab29.py`), los datos son cargados utilizando `pandas.read_csv`, y se explora el dataset para verificar que se haya cargado correctamente. El script muestra las primeras y últimas filas (`dataframe.head(10)` y `dataframe.tail(10)`) para una revisión inicial.
    
    - **Exploración Inicial:** Resultados del análisis exploratorio, incluyendo tablas y gráficos que describen la estructura y características básicas de los datos.
    
      Se realiza una exploración inicial en la que se revisan varios aspectos de los datos:
      
      - **Duplicados:** Con `dataframe.duplicated()` se identifican filas duplicadas y su conteo.
      - **Nombres de las columnas y valores únicos:** `dataframe.columns` y `dataframe.nunique()` muestran los nombres de las columnas y la cantidad de valores únicos en cada columna.
      - **Valores nulos:** `dataframe.isnull().sum()` muestra la cantidad de valores nulos en cada columna y su porcentaje relativo.
      - **Tipos de datos:** El script examina las columnas con datos de tipo objeto y numérico para evaluar su estructura y variación.
      - **Columnas constantes:** También se verifica si hay columnas con valores constantes que podrían no aportar información útil.
    
    - **Problemas Identificados:** Listado de problemas detectados (valores nulos, duplicados, errores de formato) y sugerencias iniciales para la limpieza de los datos.
    
      - **Valores Nulos:** Se evalúan y reportan mediante `dataframe.isnull().sum()` y se calcula el porcentaje de valores nulos por columna.
      - **Duplicados:** Se identifican y cuentan las filas duplicadas.
      - **Formato de Datos:** Las columnas con tipo `object` y numérico se evalúan para detectar posibles errores de formato.
      - **Columnas Constantes:** Las columnas con un único valor también se listan, ya que podrían eliminarse o ignorarse en análisis futuros.

2. **Formulación de las preguntas con la respectiva respuesta del análisis:**

    - ¿Qué problemas se quieren resolver con el análisis?
        
        El objetivo es identificar patrones en los datos, como la cantidad de colegios por región o tipo de institución, la cobertura de niveles educativos, o localizar posibles deficiencias (por ejemplo, áreas con pocos colegios), para después hacer una limpieza de datos no necesarios para el análisis.
    
    - ¿Qué decisiones pueden derivarse de este análisis?
    
        Las decisiones podrían incluir la asignación de recursos para mejorar la infraestructura educativa en áreas específicas, la apertura de nuevos colegios en áreas con alta demanda, o iniciativas para resolver problemas detectados (como falta de datos o registros incorrectos).

3. **Archivos de Trabajo:** Scripts de Python (Google Colab) utilizados para el cargue y la exploración de los datos. Archivos del dataset.

```python
import pandas

basename = "Listado_Colegios"
input_csv = basename+".csv"
output_csv = basename+"_limpio.csv"

dataframe = pandas.read_csv(input_csv)

def informacion():
    print(f"Primeras 10 filas del dataset:\n{dataframe.head(10)}")
    print("Información general del dataset:")
    print(dataframe.info())
    print(f"Últimas 10 filas del dataset:\n{dataframe.tail(10)}")

def nulos_y_duplicados():
    duplicated_rows = dataframe[dataframe.duplicated()]
    if not duplicated_rows.empty:
        print(f"Filas duplicadas:\n{duplicated_rows}")
        print(f"Valores duplicados dentro del dataset: {dataframe.duplicated().sum()}")
    else:
        print("No hay valores duplicados")
```
[Enlace a código completo de Python](lab29.py)

[Enlace a archivo del dataset](Listado_Colegios.csv)
