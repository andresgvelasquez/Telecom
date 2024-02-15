import pandas as pd
from sklearn.linear_model import LogisticRegression

# Carga de datos escalados
features_train = pd.read_csv('./files/datasets/intermediate/features_train_encoded_scaled.csv')
features_test = pd.read_csv('./files/datasets/intermediate/features_test_encoded_scaled.csv')
target_train = pd.read_csv('./files/datasets/intermediate/target_train.csv')
target_test = pd.read_csv('./files/datasets/intermediate/target_test.csv')

model = LogisticRegression()

