import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

train = pd.read_csv("..\\files\\titanic_train.csv")
test = pd.read_csv("..\\files\\titanic_test.csv")

# print(train.head())
# print(train.info())
# print(train.describe())
# print(train.columns)
#
# print(train.isnull())

# sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap="viridis")
# plt.show()

sns.set_style("whitegrid")

# sns.countplot(x="Survived", data=train, hue="Sex")
# plt.show()

# sns.countplot(x="Survived", data=train, hue="Pclass")
# plt.show()

# sns.distplot(train["Age"].dropna(), kde=False, bins=30)
# plt.show()

# sns.countplot(x="SibSp", data=train)
# plt.show()

# train["Fare"].hist(bins=40, figsize=(10,4))
# plt.show()

# sns.boxplot(x="Pclass", y="Age", data=train)
# plt.show()

def inpute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 19
        else:
            return 24
    else:
        return Age

train["Age"] = train[["Age", "Pclass"]].apply(inpute_age, axis=1)

# sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap="viridis")
# plt.show()

train.drop("Cabin", axis=1, inplace=True)
# sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap="viridis")
# plt.show()

train.dropna(inplace=True)
# sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap="viridis")
# plt.show()

sex = pd.get_dummies(train["Sex"], drop_first=True)
# print(sex.head())

embark = pd.get_dummies(train["Embarked"], drop_first=True)
# print(embark.head())
pclass = pd.get_dummies(train["Pclass"], drop_first=True)
train = pd.concat([train, sex, embark, pclass], axis=1)
# print(train.info())

train.drop(["Sex", "Embarked", "Name", "Ticket", "Pclass"], axis=1, inplace=True)
# print(train.info())

train.drop("PassengerId", axis=1, inplace=True)

X = train.drop("Survived", axis=1)
y = train["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)

# print(classification_report(y_test, predictions))

# print(confusion_matrix(y_test, predictions))

test["Age"] = test[["Age", "Pclass"]].apply(inpute_age, axis=1)
test.drop("Cabin", axis=1, inplace=True)
test.dropna(inplace=True)
sex = pd.get_dummies(test["Sex"], drop_first=True)
embark = pd.get_dummies(test["Embarked"], drop_first=True)
pclass = pd.get_dummies(test["Pclass"], drop_first=True)
test = pd.concat([test, sex, embark, pclass], axis=1)
test.drop(["Sex", "Embarked", "Name", "Ticket", "Pclass"], axis=1, inplace=True)
test.drop("PassengerId", axis=1, inplace=True)

X_train = train.drop("Survived", axis=1)
X_test = test
y_train = train["Survived"]

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)

pred = pd.DataFrame({"Survived": predictions})
test = pd.concat([test, pred], axis=1)
print(test.head())


sns.countplot(x="Survived", data=test, hue="male")
plt.show()
