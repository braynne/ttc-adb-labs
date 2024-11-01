## Escenario 1: Sector Financiero

Una institución bancaria desea analizar la relación entre las características demográficas de sus clientes y su historial crediticio para mejorar la gestión del riesgo de crédito. El banco ha recolectado datos sobre la edad, el género, el historial crediticio, el salario anual y la deuda de sus clientes. Se desea estudiar la relación entre estas variables para identificar patrones de comportamiento y mejorar el proceso de toma de decisiones en la concesión de créditos.

**Data:** `datos_financieros.csv`

### Paso a paso

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Escenario 1

df_financiero = pd.read_csv('source/datos_financieros.csv')
print(df_financiero)

print(f"""\nResumen de los datos:
{df_financiero.describe()}""")

print(f"""\nVerificación de valores nulos:
{df_financiero.isnull().sum()}""")
```

[Código completo del escenario 1](lab20_1.py)

### Conclusión

Este análisis financiero permite estudiar la relación entre las características demográficas y el historial crediticio de los clientes, ayudando a identificar patrones en el comportamiento crediticio. Al entender cómo factores como la edad, el género, el salario y la deuda impactan el riesgo de crédito, el banco puede mejorar la gestión de riesgo y optimizar su proceso de toma de decisiones en la concesión de créditos.

[Laboratorio 20](../../lab20)

[Escenario 2](../lab20_2)
