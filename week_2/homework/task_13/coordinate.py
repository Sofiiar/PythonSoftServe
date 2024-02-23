def get_integer_input(data):
    while True:
        try:
            return int(input(data))
        except ValueError:
            print(f"Invalid input - {data}, please enter an integer.")


coordinates_list = [get_integer_input(f"Input `{coordinate}`: ") for coordinate in ['x', 'y', 'z']]
print(f"Output: Coordinate {tuple(coordinates_list)}")
