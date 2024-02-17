try:
    s = input("Type a string: ")
    start = int(input("Type start index: "))
    end = int(input("Type end index: "))
    print("The substring (from start to end) is:", s[start:end])
except ValueError:
    print("Type valid integer values for start and end indexes.")
except IndexError:
    print("The start or end index is out of the string's range.")
except Exception as exception:
    print(f"An unexpected error occurred: {exception}")