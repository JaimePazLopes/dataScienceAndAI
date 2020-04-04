import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")
# flights = sns.load_dataset("flights")
# iris = sns.load_dataset("iris")

# print(tips.head())

# sns.distplot(tips["total_bill"], bins=30)
# plt.show()

# sns.jointplot(x="total_bill", y="tip", data=tips, kind="kde")
# plt.show()

# sns.pairplot(tips, hue="sex", palette="coolwarm")

# sns.rugplot(tips["total_bill"])

# sns.barplot(x='smoker',y='tip',data=tips, estimator=np.std)

# sns.countplot(x="sex", data= tips)

# sns.boxenplot(x="day", y="total_bill", data=tips, hue="smoker")

# sns.violinplot(x="day", y="total_bill", data=tips, hue="smoker", split=True)

# sns.stripplot(x="day", y="total_bill", data=tips, hue="smoker", split=True)

# sns.swarmplot(x="day", y="total_bill", data=tips)

# sns.factorplot(x="day", y="total_bill", data=tips, kind="violin")

# tipcorr = tips.corr()
# sns.heatmap(tipcorr, annot=True, cmap='coolwarm')

# pivotFlights = flights.pivot_table(index="month", columns="year", values="passengers")
# sns.heatmap(pivotFlights, linecolor="white", linewidths=2)

# sns.clustermap(pivotFlights)

# grid = sns.PairGrid(iris)
# grid.map_diag(sns.distplot)
# grid.map_upper(plt.scatter)
# grid.map_lower(sns.kdeplot)

# grid = sns.FacetGrid(data=tips, col="time",row="smoker")
# grid.map(sns.distplot, "total_bill")

# sns.lmplot(x="total_bill", y="tip", data=tips, hue="sex")

# sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm', aspect=0.6, size=8)








plt.show()