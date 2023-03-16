import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

import warnings
warnings.filterwarnings('ignore')


# Создадим и обучим модель линейной регрессии на построенных данных
# Загружаем данные
train = np.load('train.npz')
x_train = train["x_train"]
y_train = train["y_train"]

# Обучение линейной регрессии 
reg = LinearRegression()
reg.fit(x_train, y_train)
print(f'Train score: {reg.score(x_train, y_train):.4f}')

# Сохраняем обученную модель
pkl_reg = "reg.pkl"
with open(pkl_reg, 'wb') as file:
    pickle.dump(reg, file)

