try:
    x = int(input("Type the base (x): "))
    y = int(input("Type the exponent (y): "))
    result = pow(x, y)
    print(f"{x} raised to the power of {y} is: {result}")
except ValueError:
    print("You should type valid numbers.")