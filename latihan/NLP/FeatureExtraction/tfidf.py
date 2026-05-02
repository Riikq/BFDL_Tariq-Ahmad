from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Saya suka makan bakso",
    "Bakso enak dan lezat",
    "Makanan favorit saya adalah nasi goreng",
    "Nasi goreng pedas adalah makanan favorit saya",
    "Saya suka makanan manis seperti es krim",
]

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

print("Vocabulary: ", tfidf_vectorizer.vocabulary_)

print("TF-IDF Matrix: ")
print(tfidf_matrix.toarray())
