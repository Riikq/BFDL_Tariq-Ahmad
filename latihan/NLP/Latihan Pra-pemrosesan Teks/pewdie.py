import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Case folding
teks_asli = "Ini Adalah Contoh Teks yang Akan Dikonversi Menjadi Lowercase."

teks_lowercase = teks_asli.lower()
print("Teks asli: ", teks_asli)
print("Teks setelah diubah menjadi lowercase: ", teks_lowercase, "\n")


# Special characters removal
def hapus_angka(teks):
    teks_tanpa_angka = "".join([char for char in teks if not char.isdigit()])
    return teks_tanpa_angka


teks_dengan_angka = "Ini adalah contoh teks dengan angka 12345 yang akan dihapus."
teks_tanpa_angka = hapus_angka(teks_dengan_angka)

print("Teks asli: ", teks_dengan_angka)
print("Teks tanpa angka: ", teks_tanpa_angka, "\n")


def remove_punctuation(teks):
    punctuation_set = set(string.punctuation)

    teks_tanpa_tanda_baca = "".join(
        char for char in teks if char not in punctuation_set
    )
    return teks_tanpa_tanda_baca


teks_dengan_tanda_baca = """Dalam dunia ini, banyak hal terjadi, dari yang kecil hingga yang besar. Tak peduli apapun yang terjadi!"""

teks_tanpa_tanda_baca = remove_punctuation(teks_dengan_tanda_baca)

print("Teks asli: ", teks_dengan_tanda_baca)
print("Teks tanpa tanda baca: ", teks_tanpa_tanda_baca, "\n")

teks_dengan_whitespace = (
    "   Ini adalah contoh kalimat dengan spasi di awal dan akhir.   "
)
teks_setelah_strip = teks_dengan_whitespace.strip()
print("Teks asli: ", teks_dengan_whitespace)
print("Teks tanpa whitespace: ", teks_setelah_strip, "\n")

teks_dengan_whitespace = "Ini adalah    contoh kalimat  dengan spasi    di dalamnya."
teks_tanpa_whitespace = teks_dengan_whitespace.replace(" ", "")
print("Teks asli: ", teks_dengan_whitespace)
print("Teks tanpa whitespace: ", teks_tanpa_whitespace, "\n")


# Stopwords removal
nltk.download("stopwords")
nltk.download("punkt_tab")  # untuk tokenisasi

teks = "Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan."
tokens_kata = word_tokenize(teks)

stopwords_indonesia = set(stopwords.words("indonesian"))

kata_penting = [kata for kata in tokens_kata if kata.lower() not in stopwords_indonesia]
teks_tanpa_stopwords = " ".join(kata_penting)

print("\n", "Teks asli: ", teks)
print("Teks setelah filtering stopwords NTLK: ", teks_tanpa_stopwords, "\n")

# Word Tokenization
teks = "Ini adalah contoh kalimat untuk tokenisasi kata."
phrases = teks.split(" ")
print(phrases)

teks = "Ini adalah contoh kalimat pertama. Dan ini adalah contoh kalimat kedua."
sentences = re.split(r"(?<=[.!?]) +", teks)
print(sentences)

teks = "Apel, jeruk, pisang, dan mangga."
phrases = teks.split(",")
print(phrases)

teks = "Pertama, kita perlu menyiapkan bahan-bahan yang diperlukan."
tokens = re.findall(r"\w+|\d+", teks)
print(tokens)

teks = "Ini adalah contoh tokenisasi berbasis model."
tokens = teks.split()
print(tokens, "\n")

# Stemming
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["running", "easily", "bought", "crying", "leaves"]
stemmed = [stemmer.stem(word) for word in words]
print(f"Teks asli: {words}")
print(f"Stemmed: {stemmed}", "\n")

# Lemmatization
nltk.download("wordnet")
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

lemmatizer = WordNetLemmatizer()
words = ["running", "easily", "bought", "crying", "leaves"]

lemmatized = [lemmatizer.lemmatize(word, pos=wordnet.VERB) for word in words]
print(f"Teks asli: {words}")
print(f"Lemmatized: {lemmatized}", "\n")
