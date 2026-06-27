from fastapi import HTTPException, FastAPI
from typing import List
import database
import models
from models import Movie, MovieCreate

#get lexon te dhenat prej serveri
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to the Movies CRUD API"}
#post shton te dhena ne server
@app.post("/movies/", response_model=Movie)
def create_movie(movie: MovieCreate):
    movie_id = database.create_movie(movie)
    return models.Movie(id=movie_id, **movie.dict())

@app.get("/movies/", response_model=List[Movie])
def read_movies():
    return database.read_movies()

@app.get("/movies/{movie_id}", response_model=Movie)  #na kthen veq 1 filum me id tcaktume
def read_movie(movie_id: int):
    movie = database.read_movie(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

#put update te dhenat ne server
@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, movie: MovieCreate):
    updated = database.update_movie(movie_id, movie)
    if not updated:
        raise HTTPException(status_code=404, detail="Movie not found")
    return models.Movie(id=movie_id, **movie.dict())

#delete fshin te dhenat ne server
@app.delete("/movies/{movie_id}", response_model=dict)
def delete_movie(movie_id: int):
    deleted = database.delete_movie(movie_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Movie not found")
    return { "message": "Movie successfully deleted" }

