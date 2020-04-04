from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

model = LinearRegression(normalize=True)
print(model)

x,y = np.arange(10).reshape((5,2)), range(5)
print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

print(x_train)
print(x_test)
print(y_train)
print(y_test)

model.fit(x_train, y_train)
predictions = model.predict(x_test)
