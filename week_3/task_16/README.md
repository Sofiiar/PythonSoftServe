# Task 16
### Part 2. For loop.
Now, business have changed the requirements, they don't support `ACTORS` table anymore, but there is another table called `CAST` now.
Business does not want users to see any changes (from console program perspective, everything should be the same). Rework your program in order to use `CAST` instead of `ACTORS`.

```python
GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}


# (!) ACTORS storage does not exist anymore.
# ACTORS = {
#     'Robert De Niro': ['Meet the Parents'],
#     'Ben Stiller': ['Meet the Parents'],
#     'Adam Sandler': ['Anger Management'],
#     'Jack Nicholson': ['Anger Management'],
#     'Brendan Fraser': ['Mummy'],
#     'Rachel Weisz': ['Mummy'],
#     'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
#     'Penelope Cruz': ['Vanilla Sky'],
#     'Cameron Diaz': ['Vanilla Sky'],
#     'Brad Pitt': ['Meet Joe Black'],
#     'Anthony Hopkins': ['Meet Joe Black'],
#     'Jeremy Renner': ['Mission Impossible']
# }


CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}
```

Example of a program (search based on `Genre`) (unchanged).
```bash
# Input: > Search by Genre: y
# Output: Available Genres: ['comedy', 'adventures', 'romantic', 'drama', 'thriller', 'action']
# Input: > Enter genre: comedy
# Output: Available Movies: ['Meet the Parents', 'Anger Manager']
# Input: > Enter movie: Mission Impossible
# Output: Movie to watch: Mission Impossible. Starring: Tom Cruise.
```

Commit your changes.
```bash
git add week_3/movie_picker/movie_picker.py
git commit -m "movie_picker (task 16)"
git push
```
