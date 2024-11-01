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

df_financiero['Salario_Anual'].fillna(df_financiero['Salario_Anual'].median(), inplace=True)
df_financiero['Deuda'].fillna(df_financiero['Deuda'].median(), inplace=True)

print(f"""\nVerificación de valores nulos después de limpieza
{df_financiero.isnull().sum()}""")

print(f"""\nGuardado de datos limpios
{df_financiero.to_csv('source/clean/datos_financieros_limpios.csv')}""")

plt.figure(figsize=(10, 6))
plt.scatter(df_financiero['Edad'], df_financiero['Deuda'], c='green', alpha=0.5)
plt.title('Relación entre Edad y Deuda', fontsize=15)
plt.xlabel('Edad', fontsize=12)
plt.ylabel('Deuda', fontsize=12)
plt.grid(True)

z = np.polyfit(df_financiero['Edad'], df_financiero['Deuda'], 1)
p = np.poly1d(z)
plt.plot(df_financiero['Edad'], p(df_financiero['Edad']), color='red', label='Tendencia')
plt.legend()

plt.show()

plt.figure(figsize=(8, 6))
df_financiero['Historial_Crediticio'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Distribución del Historial Crediticio', fontsize=15)
plt.xlabel('Historial Crediticio', fontsize=12)
plt.ylabel('Cantidad de Clientes', fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()