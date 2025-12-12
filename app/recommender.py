# app/recommender.py
import pickle
import pandas as pd

# Load your saved files
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie_name):
    movie_name = movie_name.lower()

    # Find movie index
    try:
        movie_index = movies[movies['title'].str.lower() == movie_name].index[0]
    except:
        return []

    # Fetch similarity scores
    distances = similarity[movie_index]

    # Top 5 similar movies (excluding itself)
    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]  

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies
