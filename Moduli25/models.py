from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    director: str

class Movie(MoviesCreate):
    id: int

