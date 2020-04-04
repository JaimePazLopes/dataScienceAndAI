import nltk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix

yelp = pd.read_csv("..\\files\\yelp.csv")

print(yelp.head())
print(yelp.info())
print(yelp.describe())

yelp["text length"] = yelp["text"].apply(len)

print(yelp.head())

# sns.FacetGrid(yelp, col="stars").map(plt.hist, "text length", bins=50)
# plt.show()

# sns.boxplot(x="stars", y="text length", data=yelp)
# plt.show()

# sns.countplot(x="stars", data=yelp)
# plt.show()

print(yelp.groupby(by=["stars"], axis=0).mean())

print(yelp.groupby(by=["stars"], axis=0).mean().corr())

# sns.heatmap(yelp.groupby(by=["stars"], axis=0).mean().corr(), annot=True, cmap="YlGnBu")
# plt.show()

yelpClass = yelp[(yelp["stars"] == 1) | (yelp["stars"] == 5)]
print(yelpClass.head())
print(yelpClass.info())
print(yelpClass.describe())

X = yelpClass["text"]
y = yelpClass["stars"]

cv = CountVectorizer()
X = cv.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

nb = MultinomialNB()

nb.fit(X_train, y_train)

prediction = nb.predict(X_test)

print(confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction))

pipeline = Pipeline([
    ("bow", CountVectorizer()),
     ("tfidf", TfidfTransformer()),
     ("classifier", MultinomialNB())
     ])

X = yelpClass["text"]
y = yelpClass["stars"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

pipeline.fit(X_train, y_train)

prediction = pipeline.predict(X_test)

print(confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction))