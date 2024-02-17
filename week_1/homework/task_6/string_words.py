import sys

if len(sys.argv) > 1:
    text = " ".join(sys.argv[1:])
    words = text.split()
    print("Words in the text are:")
    for word in words:
        print(word)
else:
    print("You should type to the console valid arguments. Example: python string_words.py some text here")
