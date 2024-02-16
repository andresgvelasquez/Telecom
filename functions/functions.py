import re
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import roc_curve, auc

def camelcase_to_snakecase(df):
    ''' Convierte las columnas de un dataframe de formato CamelCase
    a snake_case y minúsculas.
    in: dataframe con columnas CamelCase
    out: dataframe con columnas snake_case '''
    columns = df.columns
    new_col_names = []
    for col in columns:
        pattern = r'([a-z])([A-Z])' # Encuentra minúscula seguida de una mayúscula
        replace = r'\1_\2'          # Reemplaza por minúscula_mayúscula
        snke_case_name = re.sub(pattern=pattern, repl=replace, string=col)
        new_col_names.append(snke_case_name.lower())
    df.columns = new_col_names

def column_to_bool(df, columns):
    ''' Convierte el tipo de dato de las columnas con 2 categorias a bool. 
    columns: Columnas a las cuales se les aplicara la transformación. '''
    df = pd.get_dummies(df, columns=columns, drop_first=True)
    for col in df.columns:
        pattern = r'_([A-Z].*)'     # Encuentra el patron que agrega get_dummies
        replace = ''                # El reemplazo es una cadena vacia
        clean_name = re.sub(pattern=pattern, repl=replace, string=col)
        df = df.rename(columns={col:clean_name})
    return df 

def split_dates(df, date_column, prefix):
    ''' Separa la columna de fecha tipo datetime en 2 distinas columnas (mes/año).
    date_column: Columna con las fechas a dividir.
    prefix: nombre de la nueva columna. '''
    df[f'{prefix}_month'] = df[date_column].dt.month
    df[f'{prefix}_year'] = df[date_column].dt.year
    return df

def caculate_end_date_by_year(user_info, last_year=2020, last_month=2, add_n_years=None, add_n_months=None):
    ''' Calcula la fecha de terminacion de contrato de 1 o mas años.'''
    # Contrato por años
    # Para los que empezaron en el año actual
    if (user_info['begin_date'].year == last_year) & (add_n_years):
        return user_info['begin_date'] + pd.DateOffset(years=add_n_years) # Agrega años
    # Para los que empezaron el año anterior
    else:
        return pd.to_datetime(f'{last_year-1}-{user_info['begin_date'].month}-01') + pd.DateOffset(years=add_n_years)

def real_end_date(user_info):
    ''' Para las observaciones con valores NaT, se reemplazara la fecha de terminación
    por la fecha en la que acaba su contrato. 
    last_date: fecha actual'''
    last_date = '20-03-01'
    # Solo aplicar a los usuarios sin fecha de terminación
    if pd.isna(user_info['end_date']):
        type_contract = user_info['type'] # Extraer el tipo de contrato

        # Contrato mes a mes 
        # Para los que empezaron su contrato en febrero
        if (type_contract == 'Month-to-month') & (user_info['begin_date'].month == 2):
            return user_info['begin_date'] + pd.DateOffset(months=1) # Agregar un mes
        # Para los que empezaron su contrato en enero
        elif (type_contract == 'Month-to-month') & (user_info['begin_date'].month == 1):
            return pd.to_datetime('2020-02-01') # Vence en febrero
        
        # Dependiendo los años del contrato regresa una fecha
        elif type_contract == 'One year':
            return caculate_end_date_by_year(user_info, add_n_years=1)
        else:
            return caculate_end_date_by_year(user_info, add_n_years=2)
    else:
        return user_info['end_date']
    
def calculate_active_days(user_info):
    ''' Calcula los días en las que un usuario estuvo activo, limitado por el último dia registrado
    de cancelación/terminación de contrato. '''
    end_active_day = user_info['end_date']
    # Limitar la fecha al último día registrado
    if end_active_day > pd.to_datetime('2020-01-01'):
        end_active_day = pd.to_datetime('2020-01-01')
    return (end_active_day - user_info['begin_date']).days

def is_active(user_info):
    ''' Verifica si la persona sigue activa.
    Si tiene NaT, significa que la persona esta activa y se pondra un True.
    En caso contrario se agrega un False.'''
    return pd.isna(user_info['end_date'])

def roc_auc_graph(target_test_filepath, model_predicts_filepath, ):
    # Cargar las predicciones
    target_test = pd.read_csv(target_test_filepath)
    model_predicts = pd.read_csv(model_predicts_filepath)

    # Calcular la curva ROC
    fpr, tpr, thresholds = roc_curve(target_test, model_predicts)

    # Calcular el área bajo la curva ROC (AUC)
    roc_auc = auc(fpr, tpr)

    # Grafica la curva ROC
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC)')
    plt.legend(loc="lower right")
    plt.show()