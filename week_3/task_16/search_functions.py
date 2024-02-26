from data import GENRES, CAST


def search_by_genre():
    print("Available Genres:", list(GENRES.keys()))
    genre = input("Enter genre: ").lower()
    if genre in GENRES:
        print("Available Movies:", GENRES[genre])
        movie = input("Enter movie: ")
        if movie in GENRES[genre]:
            print(f"Movie to watch: {movie}. Genre: {genre}.")
        else:
            print(f"Movie '{movie}' is not found in selected genre.")
    else:
        print("Genre '{genre}' is not found.")


def get_movies_with_actor():
    movies_with_actor = {}
    for movie, actors in CAST.items():
        for actor in actors:
            if actor not in movies_with_actor:
                movies_with_actor[actor] = []
            movies_with_actor[actor].append(movie)
    return movies_with_actor


def search_by_actor():
    movies_with_actor = get_movies_with_actor()
    print("Available Actors:", list(movies_with_actor.keys()))
    actor = input("Enter actor: ")
    if actor in movies_with_actor:
        print(f"Available movies: {movies_with_actor[actor]} with {actor}")
        movie = input("Enter movie: ")
        if movie in movies_with_actor[actor]:
            print(f"Movie to watch: {movie}. Starring: {actor}.")
        else:
            print(f"Movie '{movie}' is not found with selected actor.")
    else:
        print(f"Actor '{actor}' is not found.")
