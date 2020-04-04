from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

# start = datetime.datetime(2006,1,1)
# end = datetime.datetime(2016,1,1)
# bac = data.DataReader("BAC", "google", start, end)
# print(bac.head())

df = pd.read_pickle('..\\files\\all_banks')
print(df.head())
print(df.info())

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

for tick in tickers:
    print(tick, df[tick]["Close"].max())

df.xs(key="Close", axis=1, level="Stock Info").max()

returns = pd.DataFrame()
for tick in tickers:
    returns[tick+" Return"] = df[tick]["Close"].pct_change()
print(returns.head())

# sns.pairplot(returns[1:])
# plt.show()

print(returns.idxmin())
print(returns.idxmax())

# print(returns.ix["2015-01-01":"2015-12-31"].std())

# df.xs(key="Close", axis=1, level="Stock Info").plot()
# plt.show()

sns.heatmap(df.xs(key="Close",axis=1,level="Stock Info").corr(), annot=True)
plt.show()
