from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Inisialisasi objek StopWordRemover dari Sastrawi
factory = StopWordRemoverFactory()
stopwords_sastrawi = factory.get_stop_words()

teks = input("Teks: ")

tokens_kata = word_tokenize(teks)

# Filtering kata-kata dengan menghapus stopwords Sastrawi
kata_penting = [kata for kata in tokens_kata if kata.lower() not in stopwords_sastrawi]

# Gabungkan kata-kata penting kembali menjadi teks
teks_tanpa_stopwords = " ".join(kata_penting)

print("Teks asli: ", teks)
print("Teks setelah filtering stopwords Sastrawi: ", teks_tanpa_stopwords)
