import xgboost as xgb
import pandas as pd
from sklearn.metrics import roc_auc_score, f1_score, accuracy_score

# Carga de datos no escalados
features_train = pd.read_csv('./files/datasets/intermediate/features_train_encoded.csv')
features_test = pd.read_csv('./files/datasets/intermediate/features_test_encoded.csv')
target_train = pd.read_csv('./files/datasets/intermediate/target_train.csv')
target_test = pd.read_csv('./files/datasets/intermediate/target_test.csv')

# formato de entrnamiento y prueba de XGBoost
dtrain = xgb.DMatrix(features_train, label=target_train)
dtest = xgb.DMatrix(features_test, label=target_test)

# Definir los parámetros del modelo
params = {
    'objective': 'binary:logistic',  # Función objetivo para clasificación binaria
    'eval_metric': 'auc'            # Métrica de evaluación: tasa de error
}

# Entrenar el modelo
num_rounds = 10
bst = xgb.train(params, dtrain, num_rounds, evals=[(dtest, 'test')], early_stopping_rounds=5)

# Hacer predicciones en el conjunto de datos de prueba
predicts = pd.Series(bst.predict(dtest))
predicts = pd.Series([True if x >= 0.5 else False for x in predicts])  # Convertir a True o False

# Imprime las métricas ROC-AUC, F1 y Accuracy
print(f'ROC-AUC: {roc_auc_score(target_test, predicts)}')
print(f'F1: {f1_score(target_test, predicts)}')
print(f'Accuracy: {accuracy_score(target_test, predicts)}')