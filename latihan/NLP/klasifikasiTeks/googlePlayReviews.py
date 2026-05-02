from google_play_scraper import app, reviews, Sort, reviews_all

import pandas as pd

pd.options.mode.chained_assignment = None
import numpy as np
import csv
import requests
from io import StringIO

seed = 0
np.random.seed(seed)
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score

import datetime as dt
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

from wordcloud import WordCloud

import nltk

nltk.download("punkt")
nltk.download("stopwords")

scrapreview = reviews_all(
    "com.byu.id", lang="id", country="id", sort=Sort.MOST_RELEVANT, count=1000
)

# with open("./ulasan_aplikasi.csv", mode="w", newline="", encoding="utf-8") as file:
#    writer = csv.writer(file)
#    writer.writerow(["Review"])
#    for review in scrapreview:
#        writer.writerow([review["content"]])

app_reviews_df = pd.DataFrame(scrapreview)
app_reviews_df.shape
# app_reviews_df.head()
app_reviews_df.to_csv("./ulasan_aplikasi.csv", index=False)

app_reviews_df = pd.DataFrame(scrapreview)

jumlah_ulasan, jumlah_kolom = app_reviews_df.shape

# app_reviews_df.head()
# app_reviews_df.info()

clean_df = app_reviews_df.dropna()
clean_df = clean_df.drop_duplicates()

jumlah_ulasan_setelah_hapus_duplikat, jumlah_kolom_setelah_hapus_duplikat = (
    clean_df.shape
)
clean_df.info()


def cleaningText(text):
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
    listStopwords = set(stopwords.words("indonesian"))
    listStopwords1 = set(stopwords.words("english"))
    listStopwords.update(listStopwords1)
    listStopwords.update(
        [
            "iya",
            "yaa",
            "gak",
            "nya",
            "na",
            "sih",
            "ku",
            "di",
            "ga",
            "ya",
            "gaa",
            "loh",
            "kah",
            "woi",
            "woii",
            "woy",
        ]
    )
    filtered = []
    for txt in text:
        if txt not in listStopwords:
            filtered.append(txt)
    text = filtered
    return text


def stemmingText(text):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    words = text.split()
    stemmed_words = [stemmer.stem(word) for word in words]
    stemmed_text = " ".join(stemmed_words)

    return stemmed_text


def toSentence(list_words):
    sentence = " ".join(word for word in list_words)
    return sentence


slangwords = {
    "@": "di",
    "abis": "habis",
    "wtb": "beli",
    "masi": "masih",
    "wts": "jual",
    "wtt": "tukar",
    "bgt": "banget",
    "maks": "maksimal",
}


def fix_slangwords(text):
    words = text.split()
    fixed_words = []

    for word in words:
        if word.lower() in slangwords:
            fixed_words.append(slangwords[word.lower()])
        else:
            fixed_words.append(word)

    fixed_text = " ".join(fixed_words)
    return fixed_text


clean_df["text_casefoldingText"] = clean_df["text_clean"].apply(casefoldingText)
clean_df["text_slangwords"] = clean_df["text_casefoldingText"].apply(fix_slangwords)
clean_df["text_tokenizingText"] = clean_df["text_slangwords"].apply(tokenizingText)
clean_df["text_stopword"] = clean_df["text_tokenizingText"].apply(filteringText)
clean_df["text_akhir"] = clean_df["text_stopword"].apply(toSentence)
