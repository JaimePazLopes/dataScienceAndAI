import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_csv("..\\files\\USA_Housing.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)

# sns.pairplot(df)
# plt.show()

# sns.distplot(df["Price"])
# plt.show()

# sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")
# plt.show()

x = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']]

y = df["Price"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=101)

lm = LinearRegression()
lm.fit(x_train, y_train)
print(lm.intercept_)
print(lm.coef_)
cdf = pd.DataFrame(lm.coef_, x.columns, columns=["Coeff"])
print(cdf)

predictions = lm.predict(x_test)
# plt.scatter(y_test, predictions)
# plt.show()

# sns.distplot(y_test-predictions)
# plt.show()

print("MAE", metrics.mean_absolute_error(y_test, predictions))
print("MSE", metrics.mean_squared_error(y_test, predictions))
print("RMSE", np.sqrt(metrics.mean_squared_error(y_test, predictions)))





