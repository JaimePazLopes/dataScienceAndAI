import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import  DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("..\\files\\loan_data.csv")
print(df.head())
print(df.info())
print(df.describe())

# df[df["credit.policy"] == 1]["fico"].hist(bins=30, label="credit.policy = 1", alpha=.6)
# df[df["credit.policy"] == 0]["fico"].hist(bins=30, label="credit.policy = 0", alpha=.6)
# plt.legend()
# plt.show()

# df[df["not.fully.paid"] == 0]["fico"].hist(bins=30, label="not.fully.paid = 0", alpha=.6)
# df[df["not.fully.paid"] == 1]["fico"].hist(bins=30, label="not.fully.paid = 1", alpha=.6)
# plt.legend()
# plt.show()

# sns.countplot(x="purpose", hue="not.fully.paid", data=df)
# plt.show()

# sns.jointplot(x="fico", y="int.rate", data=df)
# plt.show()

# sns.lmplot(x="fico", y="int.rate", data=df, hue="credit.policy", col="not.fully.paid")
# plt.show()

df = pd.get_dummies(df,columns=["purpose"],drop_first=True)
print(df.info())

X = df.drop(["not.fully.paid"], axis=1)
y = df["not.fully.paid"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)
pred = dtree.predict(X_test)
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))

rfc = RandomForestClassifier(n_estimators=600)
rfc.fit(X_train, y_train)
pred = rfc.predict(X_test)
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))




