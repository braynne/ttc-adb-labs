import pandas

basename = "producto_licores"
input_csv = basename+".csv"
output_csv = basename+"_limpio.csv"

dataframe = pandas.read_csv(input_csv)

# Mostrar las primeras 5 filas
print(f"Primeras filas del dataset:\n{dataframe.head()}")

# Mostrar las últimas 5 filas
print(f"Últimas filas del dataset:\n{dataframe.tail()}")

# Mostrar información general
print(f"Información general del dataset:\n{dataframe.info()}")

# Valores nulos por columna
print(f"Valores nulos por columna:\n{dataframe.isnull().sum()}")

# Valores duplicados
print(f"Valores duplicados: {dataframe.duplicated().sum()}")

# Numero de filas y columnas
print(f"Numero de filas y columnas:\n{dataframe.shape}")

# Columnas
print(f"columnas:\n{dataframe.columns}")

# Resumen columnas categóricas
for column in dataframe.select_dtypes(include=["object"]).columns:
    print(f"{column}: ")
    print(dataframe[column].unique()[:5])

# Valores únicos por columnas
print(f"Valores únicos por columnas:\n{dataframe.nunique()}")

# Columnas con valores unicos bajos
print("Columnas con pocos valores unicos:")
for column in dataframe.columns:
    unique_count = dataframe[column].nunique()
    if unique_count < 10:
        print(f"{column}: {unique_count} valores únicos")

#Mostrar ejemplos nulos
print(f"Ejemplos de valores nulos:\n{dataframe[dataframe.isnull().any(axis=1)].head()}")

#Describir columnas de texto o cadenas de caracteres
print("Descripcion de columnas de texto:")
for column in dataframe.select_dtypes(include=['object']).columns:
    print(f"{column}: {dataframe[column].str.len().describe()}")

# Valores unicos que podrían ser inconsistencias

print("Inconsistencias potenciales:")
for column in dataframe.select_dtypes(include=['object']).columns:
    print(f"{column}: {dataframe[column].unique()[:10]}")

nulos_antes = dataframe.isnull().sum()
duplicados_antes = dataframe.duplicated().sum()
print(f"Fuplicados y nulos antes de la limpieza:\nDuplicados: {duplicados_antes}\nValores nulos:\n{nulos_antes}")

columnas_criticas = ["ORIGEN", "PRODUCTO", "GRADO DE ALCOHOL", "REGISTRO SANITARIO"]
dataframe = dataframe.dropna(subset=columnas_criticas)
print(dataframe.isnull().sum())

# Rellenar valores nulos en caso de ser necesario
dataframe.fillna({"NOMBRE EMPRESA DISTRIBUIDORA": "Desconocido"}, inplace=True)
print(dataframe.isnull().sum())

dataframe = dataframe.dropna()
nulos_despues = dataframe.isnull().sum()

print(nulos_despues)

dataframe = dataframe.drop_duplicates()
duplicados_despues = dataframe.duplicated().sum()
print(f"Duplicados después: {duplicados_despues}")

print(f"Datos después de nuestra limpieza:\n{dataframe.head()}")

dataframe.to_csv(output_csv, index=False)
print(f"El dataset se ha guardado como '{output_csv}'")

descriptive_stats = dataframe.describe()
print(descriptive_stats)
