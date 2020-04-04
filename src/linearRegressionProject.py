import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_csv("..\\files\\Ecommerce Customers")
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)

# sns.jointplot(x=df["Time on Website"], y=df["Yearly Amount Spent"], data=df)
# plt.show()
# sns.jointplot(x=df["Time on App"], y=df["Yearly Amount Spent"], data=df)
# plt.show()
# sns.jointplot(x=df["Time on App"], y=df["Length of Membership"], data=df, kind="hex")
# plt.show()
# sns.pairplot(df)
# plt.show()
# sns.lmplot(y="Yearly Amount Spent", x="Length of Membership", data=df)
# plt.show()

x = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = df["Yearly Amount Spent"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)
lm = LinearRegression()
lm.fit(x_train, y_train)
print(lm.coef_)

predictions = lm.predict(x_test)

# sns.scatterplot(y_test, predictions)
# plt.show()
print("MAE", metrics.mean_absolute_error(y_test, predictions))
print("MSE", metrics.mean_squared_error(y_test, predictions))
print("RMSE", np.sqrt(metrics.mean_squared_error(y_test, predictions)))

# sns.distplot(y_test-predictions, bins=50)
# plt.show()

labels = ["Avg. Session Length", "Time on App", "Time on Website", "Length of Membership"]
coeffecient = lm.coef_
list_of_tuples = list(zip(labels, coeffecient))
df = pd.DataFrame(list_of_tuples, columns = ['', 'Coeffecient'])
print(df)

d = {"Coeffecient": pd.Series(coeffecient, index=labels)}
df = pd.DataFrame(d)
print(df)






