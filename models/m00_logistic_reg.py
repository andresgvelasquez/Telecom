import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
# Carga de datos escalados
features_train = pd.read_csv('./files/datasets/intermediate/features_train_encoded_scaled.csv')
features_test = pd.read_csv('./files/datasets/intermediate/features_test_encoded_scaled.csv')
target_train = pd.read_csv('./files/datasets/intermediate/target_train.csv')
target_test = pd.read_csv('./files/datasets/intermediate/target_test.csv')

# Entrenar el modelo
model = LogisticRegression()
model.fit(features_train, target_train)
predicts = model.predict(features_test)
print(roc_auc_score(target_test, predicts))
