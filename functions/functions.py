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
    ''' Convierte el tipo de dato de las columnas con 2 categorias a bool. 
    columns: Columnas a las cuales se les aplicara la transformación. '''
    df = pd.get_dummies(df, columns=columns, drop_first=True)
    for col in df.columns:
        pattern = r'_([A-Z].*)'     # Encuentra el patron que agrega get_dummies
        replace = ''                # El reemplazo es una cadena vacia
        clean_name = re.sub(pattern=pattern, repl=replace, string=col)
        df = df.rename(columns={col:clean_name})
    return df 

def split_dates(df, date_column, prefix):
    ''' Separa la columna de fecha tipo datetime en 3 distinas columnas (dia/mes/año).
    date_column: Columna con las fechas a dividir.
    prefix: nombre de la nueva columna. '''
    df[f'{prefix}_day'] = df[date_column].dt.day
    df[f'{prefix}_month'] = df[date_column].dt.month
    df[f'{prefix}_year'] = df[date_column].dt.year
    return df