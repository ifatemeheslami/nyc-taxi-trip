import numpy as np
import pandas as pd
from pathlib import Path
import sys

current_dir = Path(__file__).resolve().parent
preprocessing_folder = (current_dir / r'./data_preprocessing').resolve()
sys.path.append(str(preprocessing_folder))
current_dir = Path(__file__).resolve().parent
model_folder = (current_dir / r'./model').resolve()
sys.path.append(str(model_folder))

#  -------------- Loadind data ---------------
from Preprocessing.data_loader import Data_loader
data_loader = Data_loader()
df = data_loader.loading(r'./x_test.csv')
# print(df.head())

import joblib
config = joblib.load(r"./model_config.joblib")

X = df
sample = X.iloc[2]

from Model.training import model_predictor
lr_pred = model_predictor(sample, config)
print(lr_pred)