try:
    s = input("Type a string: ")
    print("The size of the typed string is:", len(s))
except Exception as exception:
    print("An error occurred:", exception)
