import random
import numpy as np
import pandas as pd
import sklearn
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

n_features = random.randint(3,7)
n_features_iter = np.arange(n_features)

# Создаем наборы данных 
x, y = make_regression(n_samples=random.randint(2000, 10000), n_features = n_features, noise=random.randint(20,35))

# Создаем для наглядности датасеты
def feature_name():
    col_name = []
    for i in n_features_iter:
      name = "Feature" + str(i)
      col_name.append(name)
    return col_name

data1 = pd.DataFrame(x, columns = feature_name())
data2 = pd.DataFrame(y, columns=["Target"])

data = data1.join(data2)

# Разделяем на тренировочную и тестовую
x_train, x_test, y_train, y_test = train_test_split(x, y,  test_size=0.3, random_state = 42)

# Сохраняем датасеты 
np.savez('train.npz', x_train=x_train, y_train=y_train)
np.savez('test.npz', x_test=x_test, y_test=y_test)

