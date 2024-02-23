name = input("Enter your name: ")

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print(f"Invalid age. Value should be an integer.")

address = input("Enter your address: ")
phone = input("Enter your phone: ")

contact = {'name': name, 'age': age, 'address': address, 'phone': phone}
print(f"Contact created: {contact}")
