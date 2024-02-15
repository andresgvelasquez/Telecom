from imblearn.over_sampling import RandomOverSampler
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

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

# Guardar el objetivo de entrenamiento y prueba
target_train.to_csv('./files/datasets/intermediate/target_train_encoded.csv', index=False)
target_test.to_csv('./files/datasets/intermediate/target_test_encoded.csv', index=False)

# payment_method a ohe
features_train_encoded = pd.get_dummies(features_train, columns=['payment_method'], drop_first=True)
features_test_encoded = pd.get_dummies(features_test, columns=['payment_method'], drop_first=True)

# type a label encoding
label_encoder = LabelEncoder()
features_train_encoded['type'] = label_encoder.fit_transform(features_train['type'])
features_test_encoded['type'] = label_encoder.transform(features_test['type'])

# Guardar las características y objetivo con encoder
features_train_encoded.to_csv('./files/datasets/intermediate/features_train_encoded.csv', index=False)
features_test_encoded.to_csv('./files/datasets/intermediate/features_test_encoded.csv', index=False)

# Escalar las características de prueba y entrenamiento
scaler = MinMaxScaler()
features_train_encoded_scaled = features_train_encoded.copy()
features_test_encoded_scaled = features_test_encoded.copy()
columns_to_scale = ['type', 'monthly_charges', 'total_charges','begin_month','begin_year', 'end_month', 'end_year','active_days']
features_train_encoded_scaled[columns_to_scale] = scaler.fit_transform(features_train_encoded[columns_to_scale])
features_test_encoded_scaled[columns_to_scale] = scaler.transform(features_test_encoded[columns_to_scale])

# Guardar las características de entrenamiento y prueba con encoder y escalado
features_train_encoded_scaled.to_csv('./files/datasets/intermediate/features_train_encoded_scaled.csv', index=False)
features_test_encoded_scaled.to_csv('./files/datasets/intermediate/features_test_encoded_scaled.csv', index=False)