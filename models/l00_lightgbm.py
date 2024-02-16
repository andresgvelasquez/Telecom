import lightgbm as lgb
import pandas as pd
from sklearn.metrics import roc_auc_score, f1_score, accuracy_score

# Carga de datos no escalados
features_train = pd.read_csv('./files/datasets/intermediate/features_train_encoded.csv')
features_test = pd.read_csv('./files/datasets/intermediate/features_test_encoded.csv')
target_train = pd.read_csv('./files/datasets/intermediate/target_train.csv')
target_test = pd.read_csv('./files/datasets/intermediate/target_test.csv')


# formato LightGBM
lgb_train = lgb.Dataset(features_train, target_train)
lgb_test = lgb.Dataset(features_test, target_test, reference=lgb_train)

# Definir los parámetros del modelo
params = {
    'objective': 'binary',
    'metric': 'auc',
    'num_leaves': 6,
    'learning_rate': 0.05,
    'feature_fraction': 0.9
}

# Entrenar el modelo
num_round = 40
bst = lgb.train(params, lgb_train, num_round, valid_sets=[lgb_train, lgb_test])

# Predicciones
predicts = bst.predict(features_test, num_iteration=bst.best_iteration)
predicts = pd.Series([True if x >= 0.5 else False for x in predicts])  # Convertir a True o False

# Guardar las predicciones
predicts.to_csv('./files/datasets/output/lightgbm_predicts.csv', index=False)

# Imprime las métricas ROC-AUC, F1 y Accuracy
print(f'ROC-AUC: {roc_auc_score(target_test, predicts)}')
print(f'F1: {f1_score(target_test, predicts)}')
print(f'Accuracy: {accuracy_score(target_test, predicts)}')
