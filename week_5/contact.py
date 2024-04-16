import re


class Contact:
    def __init__(self, name=None, email=None, age=None):
        self._name = None
        self._email = None
        self._age = None
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if age is not None:
            self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is not None and len(value) > 50:
            raise ValueError("Name is too large!")
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value is not None:
            pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if not re.match(pattern, value):
                raise ValueError("Invalid email!")
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value is not None:
            try:
                value = int(value)
                if value <= 0:
                    raise ValueError("Age must be greater than zero!")
            except ValueError:
                raise ValueError("Invalid age!")
        self._age = value

    def __str__(self):
        return f"Name: {self._name}, Email: {self._email}, Age: {self._age}"
