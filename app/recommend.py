import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("C:/Users/Karan/Desktop/shl-recommendation-engine/data/assessments.csv")

# Combine columns into one searchable text
df["combined"] = (df["skills"] + " " + df["job_role"] + " " + df["level"]).str.lower()

# Convert text into numbers
vectorizer = CountVectorizer()
matrix = vectorizer.fit_transform(df["combined"])

# Recommendation function
def recommend(user_input):
    user_vec = vectorizer.transform([user_input.lower()])
    scores = cosine_similarity(user_vec, matrix)
    top_indexes = scores.argsort()[0][-3:][::-1]
    return df.iloc[top_indexes][["assessment_name"]]

# Test run
if __name__ == "__main__":
    print(recommend("data analyst python sql"))