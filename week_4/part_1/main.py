from data import GENRES, CAST
from search_functions import search, movies_by_actors


def movie_picker():
    genre = search(source=list(GENRES.keys()))
    movie = search(source=GENRES[genre], source_name='movie')
    print(f"Selected Movie: {movie} in Genre: {genre}")

    actors = movies_by_actors(CAST)
    actor = search(source=list(actors.keys()), source_name='actor')
    movie = search(source=actors[actor], source_name='movie')
    print(f"Selected Movie: {movie} Starring: {actor}")


movie_picker()
