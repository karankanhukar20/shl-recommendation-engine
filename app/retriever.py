from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_vector_store(texts):
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(texts)
    return vectorizer, matrix

def retrieve(query, vectorizer, matrix, df, top_k=3):
    q_vec = vectorizer.transform([query.lower()])
    scores = cosine_similarity(q_vec, matrix)
    idx = scores.argsort()[0][-top_k:][::-1]
    return df.iloc[idx]