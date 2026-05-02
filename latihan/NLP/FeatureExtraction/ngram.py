from nltk.util import ngrams

sentences = [
    "Saya suka makan bakso enak di warung dekat rumah.",
    "Nasi goreng adalah salah satu makanan favorit saya.",
    "Es krim coklat sangat lezat dan menyegarkan.",
    "Saat hari hujan, saya suka minum teh hangat.",
    "Pemandangan pegunungan di pagi hari sangat indah.",
    "Bola basket adalah olahraga favorit saya sejak kecil.",
]

for sentence in sentences:
    words = sentence.split()
    unigrams = list(ngrams(words, 1))
    bigrams = list(ngrams(words, 2))
    trigrams = list(ngrams(words, 3))
    print("\nKalimat: ", sentence)
    print("1-gram: ")
    for gram in unigrams:
        print(gram)
    print("2-gram: ")
    for gram in bigrams:
        print(gram)
    print("3-gram: ")
    for gram in trigrams:
        print(gram)
