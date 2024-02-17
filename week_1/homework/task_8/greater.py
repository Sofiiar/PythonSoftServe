import sys

try:
    if len(sys.argv) > 2:
        x = sys.argv[1]
        y = sys.argv[2]
        print("y is greater than x" if y > x else "y is not greater than x")
except ValueError:
    print("You should type into the console valid arguments. Example: python greater.py 4 5")