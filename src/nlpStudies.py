import nltk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import  MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix

# nltk.download_shell()

# messages = [line.rstrip() for line in open("..\\files\\SMSSpamCollection")]

messages = pd.read_csv("..\\files\\SMSSpamCollection", sep="\t", names=["label", "message"])

print(messages.head())
print(messages.info())
print(messages.describe())

print(messages.groupby("label").describe())

messages["length"] = messages["message"].apply(len)

print(messages.head())

# messages["length"].plot.hist(bins=50)
# plt.show()

print(messages[messages["length"] == 910]["message"].iloc[0])

# messages.hist(column="length", by="label", bins=60, figsize=(12,4))
# plt.show()

# print(stopwords.words("english"))

def text_process(messagesData):
    noPunctuation = [char for char in messagesData if char not in string.punctuation]
    noPunctuation = "".join(noPunctuation)
    return [word for word in noPunctuation.split() if word.lower() not in stopwords.words("english")]

bow_transformer = CountVectorizer(analyzer=text_process).fit(messages["message"])

print(len(bow_transformer.vocabulary_))

messagesBOW = bow_transformer.transform(messages["message"])

tfid = TfidfTransformer().fit(messagesBOW)

messageTFIDF = tfid.transform(messagesBOW)

spamDetect = MultinomialNB().fit(messageTFIDF,messages["label"])

prediction = spamDetect.predict(messageTFIDF)

msg_train, msg_test, label_train, label_test = train_test_split(messages["message"], messages["label"],
                                                                test_size=0.3, random_state=101)

pipeline = Pipeline([
    ("bow", CountVectorizer(analyzer=text_process)),
     ("tfidf", TfidfTransformer()),
     ("classifier", MultinomialNB())
     ])

pipeline.fit(msg_train, label_train)

prediction = pipeline.predict(msg_test)

print(classification_report(label_test, prediction))

