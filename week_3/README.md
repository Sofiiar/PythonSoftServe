# Task 15- 17
Movie picker. Idea behind this task is to cover `if`, `while`, `for`. So there are 3 parts. Beforeyou start, pull the latest changes first:
In your branch feat/<yourname>.

```bash
# pull into your branch latest changes (commits) from `main`
git pull origin main
```
Our program picks a movie based on user's input. Consider `GENRES` and `ACTORS` as database table (or key & value storage). As a user, I want to search a movie:
1. based on `Genre`
2. based on `Actor`

```python
GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}


ACTORS = {
    'Robert De Niro': ['Meet the Parents'],
    'Ben Stiller': ['Meet the Parents'],
    'Adam Sandler': ['Anger Management'],
    'Jack Nicholson': ['Anger Management'],
    'Brendan Fraser': ['Mummy'],
    'Rachel Weisz': ['Mummy'],
    'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
    'Penelope Cruz': ['Vanilla Sky'],
    'Cameron Diaz': ['Vanilla Sky'],
    'Brad Pitt': ['Meet Joe Black'],
    'Anthony Hopkins': ['Meet Joe Black'],
    'Jeremy Renner': ['Mission Impossible']
}
```