import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download korpus stopwords bahasa Indonesia dari NLTK jika belum terunduh
nltk.download("stopwords")
nltk.download("punkt_tab")  # Untuk tokenisasi kata

teks = "Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan."

# Tokenisasi teks menjadi kata-kata
tokens_kata = word_tokenize(teks)

# Ambil daftar stopwords bahasa Indonesia dari NLTK
stopwords_indonesia = set(stopwords.words("indonesian"))

# Filtering kata-kata dengan menghapus stopwords
kata_penting = [kata for kata in tokens_kata if kata.lower() not in stopwords_indonesia]

# Gabungkan kata-kata penting kembali menjadi teks
teks_tanpa_stopwords = " ".join(kata_penting)

print("Teks asli: ", teks)
print("Teks setelah filtering stopwords NLTK: ", teks_tanpa_stopwords)

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Inisialisasi objek StopWordRemover dari Sastrawi
factory = StopWordRemoverFactory()
stopwords_sastrawi = factory.get_stop_words()

tokens_kata = word_tokenize(teks)

# Filtering kata-kata dengan menghapus stopwords Sastrawi
kata_penting = [kata for kata in tokens_kata if kata.lower() not in stopwords_sastrawi]

# Gabungkan kata-kata penting kembali menjadi teks
teks_tanpa_stopwords = " ".join(kata_penting)

print("Teks asli: ", teks)
print("Teks setelah filtering stopwords Sastrawi: ", teks_tanpa_stopwords)
