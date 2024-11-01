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

print(f"""\nVerificación valores nulos después de limpieza:
{df_salud.isnull().sum()}""")

print(f"""\nGuardado de datos limpios:
{df_salud.to_csv('./source/clean/datos_salud_limpios.csv')}""")

plt.figure(figsize=(10, 6))
plt.scatter(df_salud['Edad'], df_salud['Glucosa'], c='blue', alpha=0.5)
plt.title('Relación entre Edad y Niveles de Glucosa', fontsize=15)
plt.xlabel('Edad', fontsize=12)
plt.ylabel('Niveles de Glucosa', fontsize=12)
plt.grid(True)

z = np.polyfit(df_salud['Edad'], df_salud['Glucosa'], 1)
p = np.poly1d(z)
plt.plot(df_salud['Edad'], p(df_salud['Edad']), color='red', label='Tendencia')
plt.legend()

plt.show()

plt.figure(figsize=(8, 6))
df_salud['Antecedentes_Familiares'].value_counts().plot(kind='bar', color='green', edgecolor='black')
plt.title('Distribución de Antecedentes Familiares de Diabetes', fontsize=15)
plt.xlabel('Antecedentes Familiares', fontsize=12)
plt.ylabel('Cantidad de Pacientes', fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()