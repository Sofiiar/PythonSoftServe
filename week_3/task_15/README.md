# Task 15

### Part 1. If statement.
Now, we start from a program which uses only if statement. This is a simpleprogram, which should ends, when user's input is wrong. We are not covering repeats yet here.

Example of a program (search based on `Genre`).

```bash
# Input: > Search by Genre: y
# Output: Available Genres: ['comedy', 'adventures', 'romantic', 'drama', 'thriller', 'action']
# Input: > Enter genre: comedy
# Output: Available Movies: ['Meet the Parents', 'Anger Management']
# Input: > Enter movie: Anger Management
# Output: Movie to watch: Anger Management. Genre: comedy.
```

Example of a program (search based on Actor).
```bash
# Input: > Search by Genre: n
# Input: Search by Actor: y
# Output: Available Actors: ['Robert De Niro', 'Ben Stiller', 'Adam Sandler', 'Jack Nicolson', 'Brendon Fraser','Rachel Weisz', 'Tom Cruise', 'Penelope Cruz', 'Cameron Diaz', 'Brad Pitt', 'Anthony Hopkins', 'Jeremy Renner']
# Input: > Enter actor: Tom Cruise
# Output: Available movies: ['Vanilla Sky', 'Mission Impossible'] with Tom Cruise
# Input: > Enter movie: Mission Impossible
# Output: Movie to watch: Mission Impossible. Starring: Tom Cruise.
```

### Commit your changes.
```bash
git add week_3/movie_picker/movie_picker.py
git commit -m "movie_picker (task 15)"
git push
```