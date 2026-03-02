# SHL Assessment Recommendation System (RAG-based)

This project implements a retrieval-based recommendation system that suggests SHL assessments based on user skills, job roles, and experience level.

The system follows a lightweight Retrieval-Augmented Generation (RAG) style pipeline consisting of catalog ingestion, vector-based retrieval, and recommendation output.

---

## 🔹 Features

- Catalog ingestion module for loading assessment metadata  
- Text preprocessing and feature construction  
- Retrieval stage using TF-IDF vectorization and cosine similarity  
- Recommendation engine returning relevant SHL assessments  
- Flask-based web interface for user interaction  
- JSON API endpoint for programmatic access  
- Basic evaluation module for validating recommendation quality  

---

## 🔹 Project Pipeline

1. **Catalog ingestion**  
   Assessment data is loaded and preprocessed from CSV.

2. **Vector store creation**  
   Assessment metadata is converted into numerical vectors.

3. **Retrieval stage**  
   User queries are matched against stored vectors to find the most relevant assessments.

4. **Recommendation output**  
   Top matching assessments are returned to the user via web interface or API.

---

## 🔹 Tech Stack

Python, Pandas, Scikit-learn, Flask, TF-IDF vectorization, Cosine similarity

---

## 🔹 API Endpoint


## Tech Stack
Python, Pandas, Scikit-learn, Flask

## How to Run
1. pip install pandas scikit-learn flask
2. python app.py
3. Open http://127.0.0.1:5000

## Example Input
data analyst python sql

## Output
Recommended SHL assessments based on similarity.
