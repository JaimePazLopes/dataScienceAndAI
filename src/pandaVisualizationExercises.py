import pandas as pd
import matplotlib.pyplot as plt 

df3 = pd.read_csv('..\\files\\df3')

df3.info()
print(df3.head())

# df3.plot.scatter(x="a",y="b", figsize=(12,3), c="red")

# df3["a"].hist(bins=10)

# plt.style.use("ggplot")
# df3["a"].hist(bins=25 )

# df3[["a","b"]].plot.box()

# df3["d"].plot.kde(lw=5,ls="--")

# df3.ix[0:30].plot.area(alpha=0.4)

# df3.plot.area(alpha=0.4)
# plt.legend(loc="center left", bbox_to_anchor=(1,0.5))

plt.show()