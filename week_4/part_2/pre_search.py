def get_user_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            return age
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def filter_by_age(pg_rate, age):
    allowed_movies = []
    for age_limit, movies in pg_rate.items():
        if age >= age_limit:
            allowed_movies.extend(movies)
    return allowed_movies


def prepare(genres, pg_rate, age):
    new_genres = {}
    allowed_movies = filter_by_age(pg_rate, age)
    for genre, movies in genres.items():
        new_genres[genre] = [movie for movie in movies if movie in allowed_movies]
    return new_genres
