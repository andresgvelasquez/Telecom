import pandas as pd
from catboost import CatBoostClassifier, Pool
from sklearn.metrics import roc_auc_score, f1_score, accuracy_score

# Carga de datos no escalados
features_train = pd.read_csv('./files/datasets/intermediate/features_train_encoded.csv')
features_test = pd.read_csv('./files/datasets/intermediate/features_test_encoded.csv')
target_train = pd.read_csv('./files/datasets/intermediate/target_train.csv')
target_test = pd.read_csv('./files/datasets/intermediate/target_test.csv')

# Crear el conjunto de datos de entrenamiento y prueba eficiente con Pool
train_pool = Pool(data=features_train, label=target_train)
test_pool = Pool(data=features_test)

# Entrenar el modelo
model = CatBoostClassifier(iterations=40, learning_rate=0.1, depth=6, loss_function='Logloss')
model.fit(train_pool)

# Hacer predicciones
predicts = model.predict(test_pool)

# Convertir las predicciones a valores booleanos
predicts = pd.Series(list(map(lambda x: True if x == 'True' else False, predicts)))

# Guardar las predicciones
predicts.to_csv('./files/datasets/output/catboost_predicts.csv', index=False)

# Imprime las métricas ROC-AUC, F1 y Accuracy
print(f'ROC-AUC: {roc_auc_score(target_test, predicts)}')
print(f'F1: {f1_score(target_test, predicts)}')
print(f'Accuracy: {accuracy_score(target_test, predicts)}')