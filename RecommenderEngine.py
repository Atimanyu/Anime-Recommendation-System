from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import joblib
import numpy as np
import joblib
data = pd.read_csv('anime-dataset-2023.csv')
data = data[['anime_id','Name','Genres','Synopsis','Image URL']]
data = data[~data['Genres'].str.contains('Ecchi|Hentai|Yaoi|Yuri')]
tfidf = TfidfVectorizer(stop_words='english')
data['content'] = data['Name'] + ' ' + data['Genres'] + ' ' + data['Synopsis'];
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['content'])
#saving the tfidf vectorizer and the matrix
# joblib.dump(tfidf, 'tfidf.joblib')
# joblib.dump(tfidf_matrix, 'tfidf_matrix.joblib')
tfidf = joblib.load('tfidf.joblib')
tfidf_matrix = joblib.load('tfidf_matrix.joblib')


def get_recommendations_from_query(query, top_n=5):
    query_vec = tfidf.transform([query])  # No fit, just transform
    sim_scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = sim_scores.argsort()[-top_n:][::-1]
    return data[['Name','Genres','Image URL']].iloc[top_indices]
