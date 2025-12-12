# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.recommender import recommend

app = FastAPI(title="Movie Recommender API")

class MovieRequest(BaseModel):
    movie: str

@app.get("/")
def root():
    return {"message": "Movie Recommender API is running"}

@app.post("/recommend")
def get_recommendations(req: MovieRequest):
    results = recommend(req.movie)
    return {"recommendations": results}
