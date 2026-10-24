import sqlite3
from models import Movie,MovieBase
from typing import Any

def create_connection()->Any:
    '''
    create a database connection between the server and the database
    :return: Connection variable
    '''
    conn= sqlite3.connect("pyadvanced24.db")
    conn.row_factory=sqlite3.Row
    return conn

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    director text NOT NULL,
    genre text NOT NULL,
    year_of_release text NOT NULL
    ); 
    ''')

    connection.commit()
    cursor.close()
    connection.close()


def create_movie(movie: MovieBase) -> int:
    """
    Stores a new movie in the database.

    :param movie: A Pydantic model containing the title,
                  director, genre, and year_of_release
                  of the movie to be created.
    :return: The ID of the newly created movie.
    """

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO movies (title, director, genre, year_of_release) VALUES (?, ?, ?, ?)",
        (
            movie.title,
            movie.director,
            movie.genre,
            movie.year_of_release
        )
    )

    connection.commit()
    movie_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return movie_id


def main():
    movie1=MovieBase(title='Odyssey',director='XYZ',genre='Fiction',year_of_release='2026')
    print(create_movie(movie1))

if __name__ == "__main__":
    main()