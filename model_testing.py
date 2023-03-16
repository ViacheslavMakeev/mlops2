import numpy as np
import pandas as pd
import pickle

import warnings
warnings.filterwarnings('ignore')


# Проверим модель машинного обучения на построенных данных из папки “test”
# Загружаем обученную модель
pkl_reg = "reg.pkl"
with open(pkl_reg, 'rb') as file:
    pickle_model = pickle.load(file)

# Загружаем данные test
test = np.load('test.npz')
x_test = test["x_test"]
y_test = test["y_test"]

# Оцениваем качество работы алгоритма 
score = pickle_model.score(x_test, y_test)
print("Test score: {0:.4f}".format(score))

