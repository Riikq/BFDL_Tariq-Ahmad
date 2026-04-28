from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "Ini adalah contoh dokumen pertama.",
    "Ini adalah dokumen kedua.",
    "Ini adalah dokumen ketiga.",
    "Ini adalah contoh contoh contoh.",
]

vectorizer = CountVectorizer()

bow_matrix = vectorizer.fit_transform(documents)

features = vectorizer.get_feature_names_out()

print("Matrix BoW: ")
print(bow_matrix.toarray())

print("\nDaftar Fitur:")
print(features)
