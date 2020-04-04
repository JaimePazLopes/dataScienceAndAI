import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV

iris = sns.load_dataset('iris')

print(iris.head())
print(iris.info())
print(iris.describe())

# sns.pairplot(iris, hue="species", diag_kind="hist")
# plt.show()

# sns.kdeplot(iris[iris["species"] == "setosa"]["sepal_width"], iris[iris["species"] == "setosa"]["sepal_length"],
#             cmap="plasma", shade=True, shade_lowest=False)
# plt.show()

X = iris.drop("species", axis=1)
y = iris["species"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

svc = SVC()
svc.fit(X_train, y_train)
pred = svc.predict(X_test)

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

param_grid = {"C": [0.1,1,10,100,1000], "gamma": [1,.1,.01,.001,.0001]}

grid = GridSearchCV(SVC(), param_grid, verbose=3)

grid.fit(X_train, y_train)

print(grid.best_params_)
print(grid.best_estimator_)

grid_predictions = grid.predict(X_test)

print(confusion_matrix(y_test, grid_predictions))
print(classification_report(y_test, grid_predictions))





