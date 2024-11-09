# Laboratorio 26

## Sesión #26 Carga y Exploración de Datos

**Título del Laboratorio:** Carga y Exploración de Datos de las encuesta de Empresas en Bogotá

**Duración:** 2 horas

**Objetivos del Laboratorio:**

1. Análisis es determinar cómo diversos factores (tipo de empresa, respuestas a preguntas clave y factores ponderados) influyen en el desempeño y las decisiones estratégicas de estas empresas.

2. El análisis busca proporcionar insights que revelen oportunidades de mejora para las organizaciones.

**Materiales Necesarios:**

1. Computador con conexión a internet.
2. Dataset confiable de https://www.datos.gov.co/

**Estructura del Laboratorio:**

Cargar el archivo `Productos_licores.csv` en la herramienta de tu elección (Excel, Python, Power BI) y realizar una exploración inicial.

1. Realizar el cargue del Dataset y explorar la información.

2. Formulación de las preguntas iniciales para guiar el análisis, responderlas.

    - ¿Cuál es el objetivo del análisis de datos?
        *Identificar patrones y tendencias en los productos de licor, tales como origen, grado alcohólico, y fechas de vencimiento de registros, para entender la oferta y cumplir normativas.*
    - ¿Qué problemas específicos se quieren resolver?
        *Verificar el cumplimiento de normativas sanitarias en cuanto a registros y resoluciones. Identificar productos con grado de alcohol elevado que puedan requerir controles especiales. Detectar productores y distribuidores dominantes en el mercado.*
    - ¿Qué decisiones estratégicas se derivarán del análisis?
        *Decisiones relacionadas con la renovación de registros sanitarios. Evaluar necesidades de cumplimiento y regulaciones en productos con mayor grado alcohólico. Posibles ajustes en la distribución según los productores más comunes y la cantidad de productos importados versus nacionales.*

3. **Conclusiones (10 minutos):**

Hasta ahora, el dataset parece completo y adecuado para analizar tendencias y cumplimiento de normativas en productos de licor. Se podría profundizar en áreas específicas, como distribuidoras más activas, productos con fechas de vigencia cercanas a expirar, y origen del producto en relación con el grado alcohólico.

```python
import pandas

basename = "Productos_licores"
input_csv = basename+".csv"
output_csv = basename+"_limpio.csv"

dataframe = pandas.read_csv(input_csv)

# Mostrar las primeras 5 filas
print(f"Primeras filas del dataset:\n{dataframe.head()}")

# Mostrar las últimas 5 filas
print(f"Últimas filas del dataset:\n{dataframe.tail()}")

# Mostrar información general
print(f"Información general del dataset:\n{dataframe.info()}")
```

[Código completo](../lab27/lab27.py)
