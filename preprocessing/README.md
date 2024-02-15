# Preprocessing

## Descripción

**p00_preprocessing.py** 
Se encarga de juntar los dataframes (contract, internet, personal, phone) que el cliente proporciono (la información cruda). 
Finalmente crea un nuevo dataframe limpio llamado clean_data. 
+ Carga los dataframes.
+ Da un formato snake_case a las columnas.
+ Convirte las columnas al tipo de dato correcto.
+ Agrega nuevas columnas.
+ Elimina columnas innecesarias.
+ Elimina valores ausentes.

**p01_feature_engineering.py**
Obtiene el dataframe limpio clean_data y prepara la información para que pueda ser introducida en los distintos modelos,
es decir, divide el dataframe en entrenamiento/prueba y crea distintos dataframes con escaladado, sin escalar, con one hot encoding y con label encoder.
Se obtienen los dataframes target_train, target_test, features_test_encoded, features_train_encoded, features_test_encoded_scaled y features_train_encoded_scaled.