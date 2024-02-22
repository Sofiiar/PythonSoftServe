with open('numbers.txt', 'r') as file:
    raw_data = file.read()
    numbers_raw_list = [int(number) for number in raw_data.split(",")]
    numbers_sorted_list = sorted(numbers_raw_list)
    print(numbers_sorted_list)