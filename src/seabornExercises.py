import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')

# sns.jointplot(x='fare',y='age',data=titanic,kind='scatter')

# sns.distplot(titanic['fare'],kde=False, bins=30)

# sns.boxplot(x="class", y="age", data=titanic,palette='rainbow')

# sns.swarmplot(x="class", y="age", data=titanic)

# sns.countplot(x='sex',data=titanic)

# sns.heatmap(titanic.corr(),cmap='coolwarm',vmin=-1)
# plt.title("Titanic")

grid = sns.FacetGrid(titanic,col='sex')
grid.map(plt.hist, "age")

plt.show()