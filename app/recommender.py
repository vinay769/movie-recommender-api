import os
import pickle
import requests

MOVIE_LIST_URL = "https://huggingface.co/1Vin4y/movie-recommender-model/resolve/main/movie_list.pkl"
SIMILARITY_URL = "https://huggingface.co/1Vin4y/movie-recommender-model/resolve/main/similarity.pkl"

def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        r = requests.get(url)
        open(filename, "wb").write(r.content)
        print(f"{filename} downloaded successfully.")

# Download if not exists
download_file(MOVIE_LIST_URL, "movie_list.pkl")
download_file(SIMILARITY_URL, "similarity.pkl")

# Load pickles
movies = pickle.load(open("movie_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie_name, top_k=5):
    if movie_name not in movies['title'].values:
        return []

    idx = movies[movies['title'] == movie_name].index[0]
    distances = sorted(
        list(enumerate(similarity[idx])),
        reverse=True, 
        key=lambda x: x[1]
    )
    recs = [movies.iloc[i[0]].title for i in distances[1:top_k+1]]
    return recs
