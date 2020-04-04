import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

ads = pd.read_csv("..\\files\\advertising.csv")
print(ads.head())
print(ads.info())
print(ads.describe())
print(ads.columns)

print(ads["Ad Topic Line"].nunique())
print(ads["City"].nunique())
print(ads["Country"].nunique())

# sns.heatmap(ads.isnull(), yticklabels=False, cbar=False, cmap="viridis")
# plt.show()

# sns.countplot(x="Age", data=ads)
# plt.show()

# sns.distplot(ads["Age"], kde=False, bins=30)
# plt.show()

# sns.jointplot(x="Age", y="Area Income", data=ads)
# plt.show()

# sns.jointplot(x="Age", y="Daily Time Spent on Site", data=ads, kind="kde")
# plt.show()

# sns.jointplot(x="Daily Time Spent on Site", y="Daily Internet Usage", data=ads)
# plt.show()

# sns.pairplot(data=ads, hue="Clicked on Ad", diag_kind="hist")
# plt.show()

ads.drop(["Ad Topic Line", "City", "Country", "Timestamp"], axis=1, inplace=True)

X = ads.drop("Clicked on Ad", axis=1)
y = ads["Clicked on Ad"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)

print(classification_report(y_test, predictions))

print(confusion_matrix(y_test, predictions))














