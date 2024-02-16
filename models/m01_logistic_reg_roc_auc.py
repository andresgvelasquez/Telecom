import sys
sys.path.append('./functions') # Cargar la carpeta con funciones
import pandas as pd 
from functions import roc_auc_graph

# Cargar las predicciones
model_predicts_filepath = './files/datasets/output/logistic_regression_predicts.csv'
image_name = 'logistic_reg_roc_auc'
title = 'ROC-AUC for Logistic Rgressión model'

roc_auc_graph(model_predicts_filepath, image_name, title)