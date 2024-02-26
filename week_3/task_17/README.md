# Task 17
### Part 3. While loop.
Now, we want to NOT end our program, when user inputs wrong answers. We want to handle repeats now.
Example of program (search based on `Genre`).

```bash
# Input: > Search by Genre: y
# Output: Available Genres: ['comedy', 'adventures', 'romantic', 'drama', 'thriller', 'action']
# Input: > Enter genre: comed
# Output: Genre comed not found. Please try again.
# Input: > Enter genre: advent
# Output: Genre advent not found. Please try again.
# Input: > Enter genre: romantic
# Output: Available Movies: ['Vanilla Sky', 'Meet Joe Black']
# Input: > Enter movie: Vanilla Ski
# Output: Movie Vanilla Ski not found. Please try again.
# Input: > Enter movie: Vanilla Sky
# Output: Movie to watch: Vanilla Sky. Genre: romantic.
```

Example of a program (search based on Actor).
```bash
# Input: > Search by Genre: n
# Input: > Search by Actor: y
# Output: Available Actors: ['Robert De Niro', 'Ben Stiller', 'Adam Sandler', 'Jack Nicholson', 'Brendan Fraser', 'Rachel Weisz', 'Tom Cruise', 'Penelope Cruz', 'Cameron Diaz', 'Brad Pitt', 'Anthony Hopkins', 'Jeremy Renner']
# Input: > Enter actor: Tom Cru
# Output: Actor Tom Cru not found. Please try again.
# Input: > Enter actor: Tom Cruis
# Output: Actor Tom Cruis not found. Please try again.
# Input: > Enter actor: Tom Cruise
# Output: Available movies: ['Vanilla Sky', 'Mission Impossible'] with Tom Cruise
# Input: > Enter movie: Mission Impossi
# Output: Movie Mission Impossi with actor Tom Cruise not found. Please try again.
# Input: > Enter movie: Mission Impossible
# Output: Movie to watch: Mission Impossible. Starring: Tom Cruise.
```

Commit your changes. 
```bash
git add week_3/movie_picker/movie_picker.py
git commit -m "movie_picker (task 17)"
git push
```