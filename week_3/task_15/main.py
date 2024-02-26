from search_functions import search_by_genre, search_by_actor


def main():
    search_genre = input("Search by Genre (y/n): ").lower()
    if search_genre == 'y':
        search_by_genre()
    else:
        search_actor = input("Search by Actor (y/n): ").lower()
        if search_actor == 'y':
            search_by_actor()
        else:
            print("You haven't selected any search criteria.")


if __name__ == '__main__':
    main()
