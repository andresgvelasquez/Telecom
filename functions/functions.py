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
    ''' Separa la columna de fecha tipo datetime en 2 distinas columnas (mes/año).
    date_column: Columna con las fechas a dividir.
    prefix: nombre de la nueva columna. '''
    df[f'{prefix}_month'] = df[date_column].dt.month
    df[f'{prefix}_year'] = df[date_column].dt.year
    return df

#def real_end_date(user_info, last_date):
#    ''' Para las observaciones con valores NaT, se reemplazara la fecha de terminación
#    por la fecha en la que acaba su contrato. 
#    last_date: fecha actual'''
#    # Solo aplicar a los usuarios sin fecha de terminación
#    if user_info['end_date'] == pd.NaT:
#        type_contract = user_info['type'] # Extraer el tipo de contrato
#        # Para los usuarios mes a mes
#        if type_contract == 'Month-to-month':
#            user_info['end_date'] = user_info['end_date']
    