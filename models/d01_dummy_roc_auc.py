import sys
sys.path.append('./functions') # Cargar la carpeta con funciones
import pandas as pd 
from functions import roc_auc_graph

# Cargar las predicciones
model_predicts_url = './files/datasets/output/dummy_predicts.csv'
image_name = 'dummy_roc_auc'
title = 'ROC-AUC for Dummy model'
roc_auc_graph(model_predicts_url, image_name, title)