with open('characters.txt', 'r') as file:
    raw_text = file.read()
    characters_list = [character.strip() for character in raw_text.split(",")]
    third_characters_list = [characters_list[i] for i in range(2, len(characters_list), 3)]
    print(third_characters_list)