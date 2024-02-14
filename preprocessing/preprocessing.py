import pandas as pd 
import sys
sys.path.append('./functions')

from functions import camelcase_to_snakecase

# Carga de de dataframes
df_contract = pd.read_csv('./files/datasets/input/contract.csv')
df_internet = pd.read_csv('./files/datasets/input/internet.csv')
df_personal = pd.read_csv('./files/datasets/input/personal.csv')
df_phone    = pd.read_csv('./files/datasets/input/phone.csv')

# Darle un formato de minúsculas y snake_case a las columnas
datasets = [df_contract, df_internet, df_personal, df_phone]
for df in datasets:
    camelcase_to_snakecase(df)
