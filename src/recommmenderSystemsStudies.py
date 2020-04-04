import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

columnsNames = ["user_id", "item_id", "rating", "timestamp"]

df = pd.read_csv("..\\files\\u.data", sep="\t", names=columnsNames)

print(df.head())

movieTitles = pd.read_csv("..\\files\\Movie_Id_Titles")

df = pd.merge(df, movieTitles, on="item_id")

print(df.head())

sns.set_style("white")

print(df.groupby("title")["rating"].mean().sort_values(ascending=False).head())

print(df.groupby("title")["rating"].count().sort_values(ascending=False).head())

ratings = pd.DataFrame(df.groupby("title")["rating"].mean())
ratings["num of ratings"] = pd.DataFrame(df.groupby("title")["rating"].count())
print(ratings.head())

# ratings["num of ratings"].hist(bins=100)
# plt.show()

# ratings["rating"].hist(bins=100)
# plt.show()

# sns.jointplot(x="rating", y="num of ratings", data=ratings, alpha=0.5)
# plt.show()

moviemat = df.pivot_table(index="user_id", columns="title", values="rating")

starwarsUserRatings = moviemat["Star Wars (1977)"]
liarliarUserRatings = moviemat["Liar Liar (1997)"]

similarStarWars = moviemat.corrwith(starwarsUserRatings)

similarLiarLiar = moviemat.corrwith(liarliarUserRatings)

corrStarWars = pd.DataFrame(similarStarWars, columns=["Correlation"])
corrStarWars.dropna(inplace=True)

print(corrStarWars.head())

corrStarWars = corrStarWars.join(ratings["num of ratings"])
print(corrStarWars[corrStarWars["num of ratings"]>50].sort_values("Correlation", ascending=False).head(10))

corrLiarLiar = pd.DataFrame(similarLiarLiar, columns=["Correlation"])
corrLiarLiar.dropna(inplace=True)

corrLiarLiar = corrLiarLiar.join(ratings["num of ratings"])
print(corrLiarLiar[corrLiarLiar["num of ratings"]>200].sort_values("Correlation", ascending=False).head(10))


