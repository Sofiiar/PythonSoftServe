with open('characters.txt', 'r') as file:
    raw_data = file.read()
    characters_list = raw_data.split(',')
    middle = int(len(characters_list) / 2)
    print(characters_list[:middle], characters_list[middle:])