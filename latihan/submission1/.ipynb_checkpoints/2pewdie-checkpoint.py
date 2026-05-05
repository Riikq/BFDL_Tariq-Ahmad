import pandas as pd
import re
import string
import csv
import requests
from io import StringIO
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, precision_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

nltk.download("stopwords")

df = pd.read_csv("./youtube_comments.csv")
print(df.head())
print(df.info())

clean_df = df.dropna(subset=["Comment"])
clean_df = df.drop_duplicates()
jumlah_ulasan_setelah_hapus_duplikat, jumlah_kolom_setelah_hapus_duplikat = (
    clean_df.shape
)
clean_df.info()


def cleaningText(text):
    text = str(text)
    text = re.sub(r"@[A-Za-z0-9]+", "", text)
    text = re.sub(r"#[A-Za-z0-9]+", "", text)
    text = re.sub(r"RT[\s]", "", text)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[0-9]+", "", text)
    text = re.sub(r"[^\w\s]", "", text)

    text = text.replace("\n", " ")
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.strip(" ")
    return text


def casefoldingText(text):
    text = text.lower()
    return text


def tokenizingText(text):
    text = word_tokenize(text)
    return text


def filteringText(text):
    stop_words = set(stopwords.words("english"))
    negation_words = {"not", "no", "never", "neither", "nor", "but", "none"}
    final_stop_words = stop_words - negation_words
    youtube_noise = {"br", "href"}
    final_stop_words.update(youtube_noise)
    filtered = []
    for txt in text:
        if txt not in final_stop_words:
            filtered.append(txt)
    text = filtered
    return text


def toSentence(list_words):  # Mengubah daftar kata menjadi kalimat
    sentence = " ".join(word for word in list_words)
    return sentence


clean_df["text_clean"] = clean_df["Comment"].apply(cleaningText)
clean_df["text_casefoldingText"] = clean_df["text_clean"].apply(casefoldingText)
clean_df["text_tokenizingText"] = clean_df["text_casefoldingText"].apply(tokenizingText)
clean_df["text_stopword"] = clean_df["text_tokenizingText"].apply(filteringText)
clean_df["text_akhir"] = clean_df["text_stopword"].apply(toSentence)

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()


def get_vader_label(text):
    score = sia.polarity_scores(text)
    if score["compound"] >= 0:
        polarity = "positive"
    else:
        polarity = "negative"

    return score["compound"], polarity


result = clean_df["text_akhir"].apply(get_vader_label)
result = list(zip(*result))

clean_df["polarity_score"] = result[0]
clean_df["polarity"] = result[1]

print(clean_df["polarity"].value_counts())


def show_wordcloud(data, title):
    text = " ".join(review for review in data)
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white",
        max_words=100,
        colormap="viridis",
    ).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.title(title, fontsize=20)
    plt.axis("off")
    plt.show()


# show_wordcloud(clean_df["text_akhir"], "All Comments WordCloud")
# pos_data = clean_df[clean_df["polarity"] == "positive"]["text_akhir"]
# show_wordcloud(pos_data, "Positive Sentiment WordCloud")
# neg_data = clean_df[clean_df["polarity"] == "negative"]["text_akhir"]
# show_wordcloud(neg_data, "Negative Sentiment WordCloud")

X = clean_df["text_akhir"]
y = clean_df["polarity"]

tfidf = TfidfVectorizer(max_features=200, min_df=17, max_df=0.8)
X_tfidf = tfidf.fit_transform(X)

features_df = pd.DataFrame(X_tfidf.toarray(), columns=tfidf.get_feature_names_out())

features_df

X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.2, random_state=42
)

naive_bayes = BernoulliNB()

naive_bayes.fit(X_train.toarray(), y_train)

y_pred_train_nb = naive_bayes.predict(X_train.toarray())
y_pred_test_nb = naive_bayes.predict(X_test.toarray())

accuracy_train_nb = accuracy_score(y_pred_train_nb, y_train)
accuracy_test_nb = accuracy_score(y_pred_test_nb, y_test)

print("Naive Bayes - accuracy train: ", accuracy_train_nb)
print("Naive Bayes - accuracy test: ", accuracy_test_nb)


random_forest = RandomForestClassifier()

random_forest.fit(X_train.toarray(), y_train)

y_pred_train_rf = random_forest.predict(X_train.toarray())
y_pred_test_rf = random_forest.predict(X_test.toarray())

accuracy_train_rf = accuracy_score(y_pred_train_rf, y_train)
accuracy_test_rf = accuracy_score(y_pred_test_rf, y_test)

print("Random Forest - accuracy_train:", accuracy_train_rf)
print("Random Forest - accuracy_test:", accuracy_test_rf)


logistic_regression = LogisticRegression()

logistic_regression.fit(X_train.toarray(), y_train)

y_pred_train_lr = logistic_regression.predict(X_train.toarray())
y_pred_test_lr = logistic_regression.predict(X_test.toarray())

accuracy_train_lr = accuracy_score(y_pred_train_lr, y_train)

accuracy_test_lr = accuracy_score(y_pred_test_lr, y_test)

print("Logistic Regression - accuracy_train:", accuracy_train_lr)
print("Logistic Regression - accuracy_test:", accuracy_test_lr)


decision_tree = DecisionTreeClassifier()

decision_tree.fit(X_train.toarray(), y_train)

y_pred_train_dt = decision_tree.predict(X_train.toarray())
y_pred_test_dt = decision_tree.predict(X_test.toarray())

accuracy_train_dt = accuracy_score(y_pred_train_dt, y_train)
accuracy_test_dt = accuracy_score(y_pred_test_dt, y_test)

print("Decision Tree - accuracy_train:", accuracy_train_dt)
print("Decision Tree - accuracy_test:", accuracy_test_dt)
