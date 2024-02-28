from data import GENRES, CAST


def search_by_genre_task_17():
    while True:
        print("Available Genres:", list(GENRES.keys()))
        genre = input("Enter genre: ").lower()
        if genre in GENRES:
            print("Available Movies:", GENRES[genre])
            while True:
                movie = input("Enter movie: ")
                if movie in GENRES[genre]:
                    print(f"Movie to watch: {movie}. Genre: {genre}.")
                    return
                else:
                    print(f"Movie '{movie}' is not found in selected genre.")
        else:
            print("Genre '{genre}' is not found. Please try again.")


def get_movies_with_actor_task_17():
    movies_with_actor = {}
    for movie, actors in CAST.items():
        for actor in actors:
            if actor not in movies_with_actor:
                movies_with_actor[actor] = []
            movies_with_actor[actor].append(movie)
    return movies_with_actor


def search_by_actor_task_17():
    while True:
        movies_with_actor_task_17 = get_movies_with_actor_task_17()
        print("Available Actors:", list(movies_with_actor_task_17.keys()))
        actor = input("Enter actor: ")
        if actor in movies_with_actor_task_17:
            while True:
                print(f"Available movies: {movies_with_actor_task_17[actor]} with {actor}")
                movie = input("Enter movie: ")
                if movie in movies_with_actor_task_17[actor]:
                    print(f"Movie to watch: {movie}. Starring: {actor}.")
                    return
                else:
                    print(f"Movie '{movie}' is not found with selected actor.")
        else:
            print(f"Actor '{actor}' is not found. Please try again.")
