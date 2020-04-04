import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

cancer = load_breast_cancer()

print(cancer.keys())

print(cancer["DESCR"])

df = pd.DataFrame(cancer["data"], columns=cancer["feature_names"])

print(df.head())
print(df.info())
print(df.describe())

scaler = StandardScaler()
scaler.fit(df)
scaledData = scaler.transform(df)

pca = PCA(n_components=2)
pca.fit(scaledData)
xPCA = pca.transform(scaledData)
print(scaledData.shape, xPCA.shape)

# plt.figure(figsize=(8,6))
# plt.scatter(xPCA[:,0], xPCA[:,1], c=cancer["target"])
# plt.show()

dfComp = pd.DataFrame(pca.components_, columns=cancer["feature_names"])
plt.figure(figsize=(12,6))
sns.heatmap(dfComp)
plt.show()






