import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df1 = pd.read_csv("..\\files\\df1")
df2 = pd.read_csv("..\\files\\df2")

# df1["A"].hist(bins=30)

# df1["A"].plot(kind="hist", bins=30)

# df1["A"].plot.hist(bins=30)

# df2.plot.area(alpha=0.4)

# df2.plot.bar(stacked=True)

# df1.plot.line(x=df1.index, y="B", figsize=(12,3))

# df1.plot.scatter(x="A", y="B", s=df1["C"])

# df2.plot.box()

# df = pd.DataFrame(np.random.randn(1000,2), columns=["a", "b"])
# df.plot.hexbin(x="a", y="b", gridsize=25)

df2.plot.kde()

plt.show()