import numpy as np
from sklearn.preprocessing import StandardScaler


# Предобработка данных
# Загружаем данные
train = np.load('train.npz')
test = np.load('test.npz')

x_train = train["x_train"]
y_train = train["y_train"]
x_test = test["x_test"]
y_test = test["y_test"]

# Применяем StandardScaler
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Сохраняем данные
np.savez('train.npz', x_train=x_train_scaled, y_train=y_train)
np.savez('test.npz', x_test=x_test_scaled, y_test=y_test)

