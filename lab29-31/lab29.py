import pandas

basename = "listado_colegios"
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

def informacion_columnas():
    print(f"Nombres de las columnas del dataset:\n{dataframe.columns}")
    print(f"Valores únicos de las columnas:\n{dataframe.nunique()}")

def informacion_nulos():
    print(f"Valores nulos dentro del dataset:\n{dataframe.isnull().sum()}")
    print(f"Porcentaje de valores nulos por columna:\n{100 * dataframe.isnull().sum() / len(dataframe)}")
    columns_with_null = dataframe.columns[dataframe.isnull().any()]
    print(f"Columnas con valores nulos:\n{columns_with_null}")

def tipos_de_datos_objeto():
    print(f"Tipos de datos en nuestro dataframe:\n{dataframe.dtypes}")
    object_columns = dataframe.select_dtypes(["object"]).columns
    print(f"Columnas con el tipo de dato objeto\n{object_columns}")
    for col in object_columns:
        print(f"Ejemplos de valores en la columna {col}:\n{dataframe[col].dropna().unique()[:5]}")

def tipos_de_datos_numerico():
    number_columns = dataframe.select_dtypes(["int64", "float64"]).columns
    print(f"Columnas con el tipo de dato numérico\n{number_columns}")
    for col in number_columns:
        print(f"Rango columna {col}:\n \
    Mínimo: {dataframe[col].min()}, Máximo: {dataframe[col].max()}")

def columnas_constantes():
    constant_columns = [col for col in dataframe.columns if dataframe[col].nunique() == 1]
    if constant_columns:
        print(f"Columna(s) con datos constantes:\n{constant_columns}")
    else:
        print("No hay columnas con datos constantes")

informacion()
nulos_y_duplicados()
informacion_columnas()
informacion_nulos()
tipos_de_datos_objeto()
tipos_de_datos_numerico()
columnas_constantes()
