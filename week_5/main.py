from contact import Contact
from contact_list import ContactList


def get_validated_input(prompt, attribute_name):
    temp_contact = Contact()
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'finish':
            return None
        try:
            setattr(temp_contact, attribute_name, user_input)
            return user_input
        except ValueError as exception:
            print(exception)
            print("Please try again or type 'finish' to stop inputting.")


def main():
    contact_list = ContactList()
    print("Enter contact details or type 'finish' at any prompt to stop:")

    while True:
        name = get_validated_input('Name: ', 'name')
        if name is None:
            break

        email = get_validated_input('Email: ', 'email')
        if email is None:
            break

        age = get_validated_input('Age: ', 'age')
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

    if len(contact_list) > 0:
        print("Contacts List:")
        for contact in contact_list:
            print(contact)
    else:
        print("No contacts were added.")


if __name__ == '__main__':
    main()
