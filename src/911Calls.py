import numpy as np
import pandas as pd
# import matplotlib as plt
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("..\\files\\911.csv")
print(df.info())
print(df.head())

print(df["zip"].value_counts().head())
print(df["twp"].value_counts().head())
print(df["title"].nunique())

df["Reason"] = df["title"].apply(lambda title: title.split(":")[0])
print(df["Reason"].value_counts())

# sns.countplot(x="Reason", data=df)
# plt.show()

print(type(df["timeStamp"].iloc[0]))
df["timeStamp"] = pd.to_datetime(df["timeStamp"])
print(type(df["timeStamp"].iloc[0]))

df["Hour"] = df["timeStamp"].apply(lambda time: time.hour)
df["Month"] = df["timeStamp"].apply(lambda time: time.month)
df["DayofWeek"] = df["timeStamp"].apply(lambda time: time.dayofweek)

dmap = {0:"Mon", 1:"Tue", 2:"Wed", 3:"Thu", 4:"Fri", 5:"Sat", 6:"Sun"}
df["DayofWeek"] = df["DayofWeek"].map(dmap)

# sns.countplot(x="DayofWeek", data=df, hue="Reason")
# plt.legend(bbox_to_anchor=(1,1), loc=2, borderaxespad=0)
# plt.show()

# sns.countplot(x="Month", data=df, hue="Reason")
# plt.show()

byMonth = df.groupby("Month").count()
# byMonth["lat"].plot()
# plt.show()

# sns.lmplot(x="Month",y="twp", data=byMonth.reset_index())
# plt.show()

df["Date"] = df["timeStamp"].apply(lambda t:t.date())
# df.groupby("Date").count()["lat"].plot()
# plt.tight_layout()
# plt.show()

# df[df["Reason"] == "Traffic"].groupby("Date").count()["lat"].plot()
# plt.tight_layout()
# plt.show()

dayhour = df.groupby(by=["DayofWeek", "Hour"]).count()["Reason"].unstack()
# sns.heatmap(dayhour)
# plt.show()

sns.clustermap(dayhour,cmap="viridis")
plt.show()

