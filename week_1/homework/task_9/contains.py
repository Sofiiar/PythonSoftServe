import sys

try:
    if len(sys.argv) > 2:
        word = sys.argv[1]
        letter = sys.argv[2]
        print(f"Letter {letter} is in the word." if letter in word else f"Letter {letter} is not in the word.")
except TypeError:
    print("You should type into the console valid arguments. Example: python contains.py python p")
