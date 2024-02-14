import pandas as pd 
import sys
sys.path.append('./functions')

from functions import camelcase_to_snakecase, column_to_bool, split_dates

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

# Separar la columna begin_date de df_contract en año, mes y día
df_contract = split_dates(df_contract, 'begin_date', 'begin')

# Separar la columna end_date de df_contract en año, mes y día
df_contract = split_dates(df_contract, 'end_date', 'end')

print(df_contract.head(5))

# Separar la columna end_date en año, mes y día
#df_contract['end_day'] = df_contract['end_date'].dt.day
#df_contract['end_month'] = df_contract['end_date'].dt.month
#df_contract['end_year'] = df_contract['end_date'].dt.year


#print(df_contract.info())
#print(df_contract.info())