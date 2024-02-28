from search_functions import search_by_genre_task_17, search_by_actor_task_17


search_genre = input("Search by Genre (y/n): ").lower()
if search_genre == 'y':
    search_by_genre_task_17()
else:
    search_actor = input("Search by Actor (y/n): ").lower()
    if search_actor == 'y':
        search_by_actor_task_17()
    else:
        print("You haven't selected both search criteria.")
