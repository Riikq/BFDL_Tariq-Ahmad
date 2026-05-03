import pandas as pd
import re
import string
import csv
import requests
from io import StringIO
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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
    youtube_noise = {"br"}
    final_stop_words.update(youtube_noise)
    filtered = []
    for txt in text:
        if txt not in stop_words:
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


result = clean_df["text_clean"].apply(get_vader_label)
result = list(zip(*result))

clean_df["polarity_score"] = result[0]
clean_df["polarity"] = result[1]

print(clean_df["polarity"].value_counts())
