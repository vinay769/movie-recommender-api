from fastapi import FastAPI
from pydantic import BaseModel
from app.recommender import recommend
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Movie Recommender API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
