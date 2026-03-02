import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from retriever import build_vector_store, retrieve

def load_catalog():
    df = pd.read_csv("C:/Users/Karan/Desktop/shl-recommendation-engine/data/assessments.csv")
    df["combined"] = (df["skills"] + " " + df["job_role"] + " " + df["level"]).str.lower()
    return df

df = load_catalog()

# Convert text into numbers
vectorizer, matrix = build_vector_store(df["combined"])

# Recommendation function
def recommend(user_input):
    results = retrieve(user_input, vectorizer, matrix, df)
    return results[["assessment_name"]]

# Test run
if __name__ == "__main__":
    print(recommend("data analyst python sql"))