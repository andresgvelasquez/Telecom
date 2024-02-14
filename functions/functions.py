import re
import pandas as pd

def camelcase_to_snakecase(df):
    ''' Convierte las columnas de un dataframe de formato CamelCase
    a snake_case y minúsculas.
    in: dataframe con columnas CamelCase
    out: dataframe con columnas snake_case '''
    columns = df.columns
    new_col_names = []
    for col in columns:
        pattern = r'([a-z])([A-Z])' # Encuentra minúscula seguida de una mayúscula
        replace = r'\1_\2'          # Reemplaza por minúscula_mayúscula
        snke_case_name = re.sub(pattern=pattern, repl=replace, string=col)
        new_col_names.append(snke_case_name.lower())
    df.columns = new_col_names

def column_to_bool(df, columns):
    ''' Convierte el tipo de dato de las columnas con 2 categorias a bool. '''
    df = pd.get_dummies(df, columns=columns, drop_first=True)
    print(df.head())
    for col in df.columns:
        pattern = r'_([A-Z].*)'     # Encuentra el patron que agrega get_dummies
        replace = ''                # El reemplazo es una cadena vacia
        clean_name = re.sub(pattern=pattern, repl=replace, string=col)
        df = df.rename(columns={col:clean_name})
    return df 