import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("..\\files\\Classified Data", index_col=0)
scaler = StandardScaler()
scaler.fit(df.drop("TARGET CLASS", axis=1))
scaled_features = scaler.transform(df.drop("TARGET CLASS", axis=1))

df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
print(df_feat.head())

X = df_feat
y = df["TARGET CLASS"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

predictions = knn.predict(X_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

error_rate = []
for i in range(1,41):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    predictionsI = knn.predict(X_test)
    error_rate.append(np.mean(predictionsI != y_test))


plt.figure(figsize=(10,6))
plt.plot(range(1,41), error_rate, color="blue", linestyle="dashed", marker="o", markerfacecolor="red", markersize=10)
plt.title("Error Rate vc K Value")
plt.xlabel("K")
plt.ylabel("Error Rate")
plt.show()











