with open('numbers.txt', 'r') as file:
    raw_numbers = [int(number.strip()) for number in file.read().split(',')]
    unique_numbers = sorted(set(raw_numbers))
    occurrences = {number: raw_numbers.count(number) for number in unique_numbers}

    print(f"Unique: {unique_numbers}")
    print(f"Occurrences: {occurrences}")
