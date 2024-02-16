import sys

if len(sys.argv) > 1:
    text = " ".join(sys.argv[1:])
    words = text.split()
    print("Words in the text are:")
    for word in words:
        print(word)
else:
    print("You haven't provided the text as an argument.")
