from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import TreebankWordTokenizer
import re

text = "Ini adalah contoh tokenisasi kata dalam pemrosesan teks. Apakah ini kalimat kedua? Ya, ini kalimat kedua."
tokens = word_tokenize(text)
print(tokens, "\n")

sentences = sent_tokenize(text)
print(sentences, "\n")

# Misalkan kita ingin memisahkan frasa berdasarkan tanda baca koma
text = "Pemrosesan teks adalah cabang ilmu komputer yang berfokus pada pengolahan teks dan dokumen."
tokenizer = TreebankWordTokenizer()
phrases = tokenizer.tokenize(text)
print(phrases, "\n")

text = "Pertama, kita perlu menyiapkan bahan-bahan yang diperlukan."
tokens = re.findall(r"\w+|\d+", text)
print(tokens, "\n")

# Model-based Tokenization
# Misalnya menggunakan spasi sebagai pemisah kata
text = "Ini adalah contoh tokenisasi berbasis model."
tokens = text.split()
print(tokens, "\n")
