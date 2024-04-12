from contact import Contact, validate_email, validate_age, validate_name
from contact_list import ContactList


def get_valid_input(prompt, validation_function):
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'finish':
            return None
        try:
            validation_function(user_input)
            return user_input
        except ValueError as exception:
            print(exception)
            print("Type 'finish' to stop inputting this field.")


def main():
    contact_list = ContactList()
    print("Enter contact details or type 'finish' at any prompt to stop:")

    while True:
        name = get_valid_input('Name: ', validate_name)
        if name is None:
            break

        email = get_valid_input('Email: ', validate_email)
        if email is None:
            break

        age = get_valid_input('Age: ', validate_age)
        if age is None:
            break

        contact = Contact(name=name, email=email, age=age)
        contact_list.append(contact)
        print('-' * 10)
        print(contact)
        print('-' * 10)

        proceed = input('Add another one? (y/n): ')
        if proceed.lower() != 'y':
            break

    if len(contact_list.contacts) > 0:
        print("Contacts List:")
        print(contact_list)
    else:
        print("There are no contacts to be printed.")


if __name__ == '__main__':
    main()
