import pandas as pd 
import sys
sys.path.append('./functions')

from functions import camelcase_to_snakecase

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

# Separar la columna begin_date de df_contract en año, mes y día
df_contract['begin_day'] = df_contract['begin_date'].dt.day
df_contract['begin_month'] = df_contract['begin_date'].dt.month
df_contract['begin_year'] = df_contract['begin_date'].dt.year


# Separar la columna end_date en año, mes y día
#df_contract['end_day'] = df_contract['end_date'].dt.day
#df_contract['end_month'] = df_contract['end_date'].dt.month
#df_contract['end_year'] = df_contract['end_date'].dt.year

print(df_contract.head(10))
#print(df_contract.info())