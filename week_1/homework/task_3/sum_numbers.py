import sys

if len(sys.argv) == 3:
    try:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        print(f"The sum of {x} and {y} is: {x + y}")
    except ValueError:
        print("You should provide valid numbers.")
else:
    print("You should type: python sum_numbers.py <number1> <number2>")