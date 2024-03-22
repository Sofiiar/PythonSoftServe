def search(source, source_name='item'):
    sorted_source = sorted(source)
    print(f'Available {source_name}(s): {", ".join(sorted_source)}')

    while True:
        choice = input(f"Enter {source_name}: ")
        if choice in map(str, sorted_source):
            for item in source:
                if item == choice:
                    return item
        else:
            print(f"{source_name.capitalize()} '{choice}' is not found. Please try again.")


def movies_by_actors(cast, allowed_movies):
    actors = {}
    for movie, actors_in_movie in cast.items():
        if movie in allowed_movies:
            for actor in actors_in_movie:
                actors.setdefault(actor, []).append(movie)
    return actors
