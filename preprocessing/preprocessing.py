import pandas as pd 
import sys
sys.path.append('./functions')
from pandas._libs.tslibs.nattype import NaTType
from functions import camelcase_to_snakecase, column_to_bool, split_dates, real_end_date, calculate_active_days, is_active

# Cargar la carpeta con funciones

# Carga de de dataframes
df_contract = pd.read_csv('./files/datasets/input/contract.csv', parse_dates=['BeginDate'])
df_internet = pd.read_csv('./files/datasets/input/internet.csv')
df_personal = pd.read_csv('./files/datasets/input/personal.csv')
df_phone    = pd.read_csv('./files/datasets/input/phone.csv')

# Darle un formato de minúsculas y snake_case a las columnas de cada dataframe
datasets = [df_contract, df_internet, df_personal, df_phone]
for df in datasets:
    camelcase_to_snakecase(df)

# Convertir la columna end_date a datetime
df_contract['end_date'] = pd.to_datetime(df_contract['end_date'], errors='coerce')

# Reemplazar las cadenas vacias con '0', debido a que el mes no ha empezado
# el cliente no ha tenido cargos. Y cambiar el tipo de dato a float. 
df_contract['total_charges'] = df_contract['total_charges'].replace(' ', '0').astype(float)

# Convertir las columas de 2 valores a bool
# Contract
df_contract = column_to_bool(df_contract, ['paperless_billing'])

#Internet 
df_internet = column_to_bool(df_internet, ['internet_service', 'online_security', 'online_backup', 'device_protection',
                                           'tech_support', 'streaming_tv', 'streaming_movies'])
df_internet = df_internet.rename(columns={'internet_service':'internet_fiber_optic'})

# Personal
df_personal = column_to_bool(df_personal, ['gender', 'partner', 'dependents'])
df_personal = df_personal.rename(columns={'gender':'gender_male'}) 

# Phone
df_phone = column_to_bool(df_phone, ['multiple_lines'])

# Crear una columna que diga si la persona esta activa o no
df_contract['is_active'] = df_contract.apply(is_active, axis=1)

# Reemplazar los valores ausentes de end_date por el vencimiento del contrato
df_contract['end_date'] = df_contract.apply(real_end_date, axis=1)

# Separar la columna begin_date de df_contract en año, mes
df_contract = split_dates(df_contract, 'begin_date', 'begin')

# Separar la columna end_date de df_contract en año, mes
df_contract = split_dates(df_contract, 'end_date', 'end')

# Crear una columna con los días activo en contract
df_contract['active_days'] = df_contract.apply(calculate_active_days, axis=1)

# Eliminar columnas innecesarias para el modelo begin_date, end_date
df_contract.drop(['begin_date', 'end_date'], axis=1, inplace=True)

# Mezclar todos los dataframes (contrct, internet, personal y phone)
df_all = pd.merge(df_contract, df_internet, on='customer_id', how='outer')
df_all = pd.merge(df_all, df_personal, on='customer_id', how='outer')
df_all = pd.merge(df_all, df_phone, on='customer_id', how='outer')

# Reemplazar los valores ausentes por el merge, por False
df_all.fillna(False, inplace=True)

# Eliminar la columna de ids
df_all.drop('customer_id', axis=1, inplace=True)

print(df_all.info())
# Guardar el dataset
df_all.to_csv('./files/datasets/intermediate/clean_data.csv', index=False)