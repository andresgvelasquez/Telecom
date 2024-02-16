import pandas as pd
import matplotlib.pyplot as plt
from sklearn.dummy import DummyClassifier
from sklearn.metrics import roc_auc_score, f1_score, accuracy_score

# Carga de datos escalados
features_train = pd.read_csv('./files/datasets/intermediate/features_train_encoded_scaled.csv')
features_test = pd.read_csv('./files/datasets/intermediate/features_test_encoded_scaled.csv')
target_train = pd.read_csv('./files/datasets/intermediate/target_train.csv')
target_test = pd.read_csv('./files/datasets/intermediate/target_test.csv')

#Entrenamiento
model = DummyClassifier()
model.fit(features_train, target_train)

# Predicciones
predicts = pd.Series(model.predict(features_test))

# Guardar las predicciones
predicts.to_csv('./files/datasets/output/dummy_predicts.csv', index=False)

# Imprime las métricas ROC-AUC, F1 y Accuracy
print(f'ROC-AUC: {roc_auc_score(target_test, predicts)}')
print(f'F1: {f1_score(target_test, predicts)}')
print(f'Accuracy: {accuracy_score(target_test, predicts)}')