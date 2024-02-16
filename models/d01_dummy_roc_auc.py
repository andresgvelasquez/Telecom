import sys
sys.path.append('./functions') # Cargar la carpeta con funciones
import pandas as pd 
from functions import roc_auc_graph

# Cargar las predicciones
target_test_url = './files/datasets/intermediate/target_test.csv'
model_predicts_url = './files/datasets/output/dummy_predicts.csv'
image_name = 'dummy_roc_auc'

roc_auc_graph(target_test_url, model_predicts_url, image_name)