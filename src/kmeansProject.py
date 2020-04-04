import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

df = pd.read_csv("..\\files\\College_Data", index_col=0)

print(df.head())
print(df.info())
print(df.describe())

# sns.scatterplot(x="Room.Board", y="Grad.Rate", hue="Private", data=df)
# plt.show()

# sns.scatterplot(x="Outstate", y="F.Undergrad", hue="Private", data=df)
# plt.show()

# g = sns.FacetGrid(df, hue="Private", palette="coolwarm", size=6, aspect=2)
# g = g.map(plt.hist, "Outstate", bins=20, alpha=.7)
# plt.show()

# g = sns.FacetGrid(df, hue="Private", palette="coolwarm", height=6, aspect=2)
# g = g.map(plt.hist, "Grad.Rate", bins=20, alpha=.7)
# plt.show()

print(df[df["Grad.Rate"]>100])
df["Grad.Rate"]["Cazenovia College"] = 100

# g = sns.FacetGrid(df, hue="Private", palette="coolwarm", height=6, aspect=2)
# g = g.map(plt.hist, "Grad.Rate", bins=20, alpha=.7)
# plt.show()

kmeans = KMeans(n_clusters=2)
kmeans.fit(df.drop("Private", axis=1))

print(kmeans.cluster_centers_)

def converter(private):
    if private == "Yes":
        return 1
    else:
        return 0

df["Cluster"] = df["Private"].apply(converter)
print(df.head())



print(confusion_matrix(df["Cluster"], kmeans.labels_))
print(classification_report(df["Cluster"], kmeans.labels_))



