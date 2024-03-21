def search(source, source_name='genre'):
    print(f'Available {source_name}(s): {', '.join(sorted(source))}')
    while True:
        choice = input(f"Enter {source_name}: ")
        if choice in source:
            return choice
        else:
            print(f"{source_name.capitalize()} '{choice}' is not found. Please try again.")


def search_movie(movies):
    print(f'Available movies: {", ".join(sorted(movies))}')
    while True:
        movie = input("Enter movie: ")
        if movie in movies:
            print(f"Movie to watch: {movie}.")
            return movie
        else:
            print(f"Movie '{movie}' is not found. Please try again.")


def movies_by_actors(cast):
    actors = {}
    for movie, actors_in_movie in cast.items():
        for actor in actors_in_movie:
            actors.setdefault(actor, []).append(movie)
    return actors
