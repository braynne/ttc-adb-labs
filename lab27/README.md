# Laboratorio 27

## Sesión #27 Limpieza, estadistica descriptiva

**Título del Laboratorio:** Limpieza y estadistica descriptiva de los datos en los productos de licor registrados en Risaralda para la distribución.

**Duración:** 2 horas

**Objetivos del Laboratorio:**

1. Llevar a cabo un proceso completo de limpieza de datos y aplicar técnicas de estadística descriptiva al dataset de productos de licor, con el fin de mejorar la calidad de los datos y proporcionar insights significativos que puedan ser utilizados para la toma de decisiones estratégicas.

2. Esto incluye identificar y resolver problemas de datos como valores nulos, duplicados e inconsistencias, y resumir las principales características del dataset mediante medidas estadísticas que faciliten la comprensión y análisis de la información

**Materiales Necesarios:**

1. Computador con conexión a internet.

2. Herramientas de limpieza de los datos y aplicación de estadistica descriptiva.

**Estructura del Laboratorio:**

1. Entregar un informe escrito que detalle el paso a paso, debe incluir las primeras observaciones sobre la estructura de los datos, los hallazgos, conclusiones y recomendaciones, se debe entregar en PDF o Word.

    1. Se eliminaron filas en las que haya valores nulos en columnas críticas: [`ORIGEN`, `PRODUCTO`, `GRADO DE ALCOHOL`, `REGISTRO SANITARIO`].
    2. Se cambiaron valores nulos en `NOMBRE EMPRESA DISTRIBUIDORA` a `Desconocido`.
    3. Se eliminaron duplicados.

2. Responder las preguntas planteadas.

    - ¿Qué información se debe analizar en el Dataset para garantizar el cumplimiento de las normativas sanitarias y optimizar la distribución de los productos?
    
       *"Registro Sanitario", "Vigencia de Registro Sanitario", y "Grado de Alcohol" para garantizar que los productos cumplen los requisitos legales de seguridad y salubridad.*
        
    - ¿Cómo pueden los valores nulos y las inconsistencias en el texto afectar la precisión y calidad del análisis de los datos?
        
        *Los valores nulos y las inconsistencias pueden dificultar la agrupación y resumen de datos. Por ejemplo, inconsistencias en los nombres de productores o distribuidores pueden llevar a análisis erróneos sobre la cantidad y el tipo de productos gestionados por cada empresa.*
        
    - ¿Qué estrategias se pueden implementar para asegurar que el análisis de datos sea preciso y útil para la toma de decisiones estratégicas?
    
        *Implementar reglas de validación y limpieza para reducir inconsistencias. Usar herramientas de limpieza y normalización de datos como Python o Excel, y desarrollar scripts automatizados para procesar los datos de forma consistente.*

3. Adjunta el Dataset, los script o archivo de la exploración.

[Enlace a dataset](../lab26/Productos_licores.csv)
    
[Enlace a dataset limpio](Productos_licores_limpio.csv)

[Enlace a script](lab27.py)
