import nltk
from nltk.stem import PorterStemmer

# Inisiasi stemmer
stemmer = PorterStemmer()

# Kata-kata asli
words = [
    "running",
    "runs",
    "runner",
    "ran",
    "easily",
    "fairness",
    "better",
    "best",
    "cats",
    "cacti",
    "geese",
    "rocks",
    "oxen",
]

# Melakukan stemming pada setiap kata
for word in words:
    stemmed_word = stemmer.stem(word)
    print(f"Kata asli: {word}\nKata setelah stemming: {stemmed_word}\n")

from nltk.stem import WordNetLemmatizer

# Download wordnet jika belum di-download
nltk.download("wordnet")

# Inisialisasi lemmatizer
lemmatizer = WordNetLemmatizer()

# Kata-kata asli
words = [
    "running",
    "cats",
    "good",
    "goose",
    "rocks",
    "cities",
    "big",
    "happy",
    "run",
    "sleep",
]

# lematisasi
for word in words:
    lemma_word = lemmatizer.lemmatize(word.lower())
    print(f"Kata asli: {word}\nKata setelah lematisasi: {lemma_word}\n")
