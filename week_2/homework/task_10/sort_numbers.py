with open('numbers.txt', 'r') as file:
    raw_text = file.read()
    numbers_raw_list = [int(number) for number in raw_text.split(",")]
    numbers_sorted_list = sorted(numbers_raw_list)
    print(numbers_sorted_list)