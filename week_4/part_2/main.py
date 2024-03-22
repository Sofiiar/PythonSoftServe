from data import GENRES, CAST, PG
from pre_search import get_user_age, filter_by_age, prepare
from search_functions import search, movies_by_actors


def movie_picker():
    user_age = get_user_age()
    allowed_movies = filter_by_age(PG, user_age)

    if not allowed_movies:
        print("There are no available movies for you.")
        return

    prepared_genres = prepare(GENRES, PG, user_age)
    genre = search(source=list(prepared_genres.keys()), source_name='genre')

    if prepared_genres[genre]:
        movie = search(source=prepared_genres[genre], source_name='movie')
        if movie:
            print(f"Selected Movie: {movie} in Genre: {genre}")
        else:
            print("No movies found for the selected genre.")
    else:
        print("There are no available movies in this genre for you. Moving on to actor selection.")

    prepared_actors = movies_by_actors(CAST, allowed_movies)

    if prepared_actors:
        actor = search(source=list(prepared_actors.keys()), source_name='actor')
        if not prepared_actors[actor]:
            print(f"No available movies for actor {actor}.")
        else:
            movie = search(source=prepared_actors[actor], source_name='movie')
            if movie:
                print(f"Selected Movie: {movie} Starring: {actor}")
            else:
                print("No movie selection made.")
    else:
        print("No actors available for the selected movies.")


movie_picker()
