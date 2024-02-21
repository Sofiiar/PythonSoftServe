with open('numbers.txt', 'r') as f:
    numbers = f.read()
    numbers_raw_list = [int(number) for number in numbers.split(",")]
    numbers_sorted_list = sorted(numbers_raw_list)
    print(numbers_sorted_list)