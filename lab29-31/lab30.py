import pandas

basename = "listado_colegios"
input_csv = basename+".csv"
output_csv = basename+"_limpio.csv"

dataframe = pandas.read_csv(input_csv)

print(f"Filas y columnas del dataset:\n{dataframe.shape}")

df_clean = dataframe.drop_duplicates()

print(f"Filas y columnas del dataset sin duplicados:\n{dataframe.shape}")

print(f"Verificar si hay valores nulos en el dataset:\n{df_clean.isnull().sum()}")

column_names = df_clean.columns

for name in column_names:
    if df_clean[name].dtype == "object":
        df_clean[name] = df_clean[name].fillna("Desconocido")
    elif df_clean[name].dtype in ["int64", "float64"]:
        df_clean[name] = df_clean[name].fillna(df_clean[name].mean())

print(f"Limpio:\n{df_clean.isnull().sum()}")

for name in column_names:
    if df_clean[name].isnull().sum() == len(df_clean):
        df_clean = df_clean .drop(name, axis=1)

print(f"Totalmente limpio:\n{df_clean.isnull().sum()}")

df_clean.to_csv(output_csv)
