class ContactList:
    def __init__(self):
        self.contacts = []

    def append(self, contact):
        self.contacts.append(contact)

    def __len__(self):
        return len(self.contacts)

    def __iter__(self):
        return iter(self.contacts)