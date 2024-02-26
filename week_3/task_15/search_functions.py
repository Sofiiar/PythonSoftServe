from data import GENRES, ACTORS


def search_by_genre():
    print("Available Genres:", list(GENRES.keys()))
    genre = input("Enter genre: ").lower()
    if genre in GENRES:
        print("Available Movies:", GENRES[genre])
        movie = input("Enter movie: ")
        if movie in GENRES[genre]:
            print(f"Movie to watch: '{movie}'. Genre: {genre}.")
        else:
            print(f"Movie '{movie}' is not found in selected genre {genre}.")
    else:
        print(f"Genre {genre} is not found.")


def search_by_actor():
    print("Available Actors:", list(ACTORS.keys()))
    actor = input("Enter actor: ")
    if actor in ACTORS:
        print(f"Available movies: {ACTORS[actor]} with {actor}")
        movie = input("Enter movie: ")
        if movie in ACTORS[actor]:
            print(f"Movie to watch: '{movie}'. Starring: {actor}.")
        else:
            print(f"Movie ''{movie}'' is not found with selected actor {actor}.")
    else:
        print(f"Actor '{actor}' is not found.")
