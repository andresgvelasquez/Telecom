import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler

# Carga del dataframe limpio
df_telecom_clean = pd.read_csv('./files/datasets/intermediate/clean_data.csv')

# Definir las características y el objetivo
features = df_telecom_clean.drop('is_active', axis=1)
target = df_telecom_clean['is_active']

# Aplicar sobremuestreo para balancear el objetivo
over_sampler = RandomOverSampler(random_state=42)
features_oversampled, target_oversampled = over_sampler.fit_resample(features, target)

# Dividir el dataframe en entrenamiento y prueba
features_train, features_test, target_train, target_test = train_test_split(
    features_oversampled, target_oversampled, test_size=0.2, random_state=42
)

# payment_method a ohe
features_train_encoded = pd.get_dummies(features_train, columns=['payment_method'], drop_first=True)
features_test_encoded = pd.get_dummies(features_test, columns=['payment_method'], drop_first=True)

# type a label encoding
#label_encoder = LabelEncoder()
#features_train['type'] = label_encoder.fit_transform(features_train['type'])
#features_test['type'] = label_encoder.transform(features_test[type])


# Guardar el dataset
#df_all.to_csv('./files/datasets/intermediate/clean_data.csv', index=False)

print(features_train_encoded.info())