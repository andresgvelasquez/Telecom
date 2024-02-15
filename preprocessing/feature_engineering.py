import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Carga del dataframe limpio
df_telecom_clean = pd.read_csv('./files/datasets/intermediate/clean_data.csv')

# Definir las características y el objetivo
features = df_telecom_clean.drop('is_active')
target = df_telecom_clean['is_active']

# Dividir el dataframe en entrenamiento, validación y prueba


# type a label encoding
label_enc = LabelEncoder()
# payment_method a ohe

print(features.info())