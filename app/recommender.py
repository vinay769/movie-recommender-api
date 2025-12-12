import os
import pickle
import requests

MOVIE_LIST_URL = "https://huggingface.co/YOUR_USERNAME/movie-recommender-model/resolve/main/movie_list.pkl"
SIMILARITY_URL = "https://huggingface.co/YOUR_USERNAME/movie-recommender-model/resolve/main/similarity.pkl"

def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        r = requests.get(url)
        r.raise_for_status()
        with open(filename, "wb") as f:
            f.write(r.content)
        print(f"{filename} downloaded.")

# Download both files if missing:
download_file(MOVIE_LIST_URL, "movie_list.pkl")
download_file(SIMILARITY_URL, "similarity.pkl")

# Load them
movies = pickle.load(open("movie_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie_name):
    if movie_name not in movies['title'].values:
        return []
    
    idx = movies[movies['title'] == movie_name].index[0]
    distances = sorted(
        list(enumerate(similarity[idx])),
        reverse=True,
        key=lambda x: x[1]
    )
    recs = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recs
