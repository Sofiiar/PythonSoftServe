from contact import Contact


class ContactList:
    def __init__(self):
        self.contacts = []

    def append(self, contact):
        if not isinstance(contact, Contact):
            raise ValueError("Invalid contact!")
        self.contacts.append(contact)

    def __iter__(self):
        return iter(self.contacts)

    def __str__(self):
        return '\n'.join(str(contact) for contact in self.contacts)
