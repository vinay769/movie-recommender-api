# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.recommender import recommend

# 1. Create FastAPI app first
app = FastAPI(title="Movie Recommender API")

# 2. Add CORS after creating the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # during development
    allow_methods=["*"],
    allow_headers=["*"],
)

class MovieRequest(BaseModel):
    movie: str

@app.get("/")
def root():
    return {"message": "Movie Recommender API is running"}

@app.post("/recommend")
def get_recommendations(req: MovieRequest):
    results = recommend(req.movie)
    return {"recommendations": results}
