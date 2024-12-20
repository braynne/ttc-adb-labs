## Escenario 2: Sector Salud

Un hospital está llevando a cabo un estudio para analizar cómo diferentes factores afectan el riesgo de desarrollar diabetes en pacientes. Se han recolectado datos sobre la edad, el género, los niveles de glucosa en sangre, el índice de masa corporal (IMC) y si el paciente tiene antecedentes familiares de diabetes. El objetivo es identificar patrones en los datos para detectar a los pacientes con mayor riesgo de desarrollar esta enfermedad.

**Data:** `datos_salud glu.csv`

### Paso a paso

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Escenario 2

df_salud = pd.read_csv('source/datos_salud glu.csv')
print(f"""Valores Originales:
{df_salud.describe()}""")

print(f"""\nVerificación valores nulos:
{df_salud.isnull().sum()}""")

df_salud['Glucosa'].fillna(df_salud['Glucosa'].median(), inplace=True)
df_salud['IMC'].fillna(df_salud['IMC'].median(), inplace=True)
```

[Código completo del escenario 2](lab20_2.py)

### Conclusión

Este análisis de factores de riesgo permite identificar patrones entre variables como la edad, el género, los niveles de glucosa, el IMC y los antecedentes familiares, ayudando a detectar pacientes con mayor probabilidad de desarrollar diabetes. Al comprender cómo estos factores influyen en el riesgo, el hospital puede implementar estrategias preventivas y personalizar el seguimiento médico para los pacientes con mayor vulnerabilidad.

[Escenario 1](../lab20_1)

[Laboratorio 20](../../lab20)
