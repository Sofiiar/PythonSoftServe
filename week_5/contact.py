import re


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, email):
        raise ValueError("Invalid email!")


def validate_age(age):
    try:
        age = int(age)
        if age <= 0:
            raise ValueError("Age must be greater than zero!")
    except ValueError:
        raise ValueError("Invalid age!")


def validate_name(name):
    if len(name) > 50:
        raise ValueError("Name is too large!")


class Contact:
    def __init__(self, name, email, age):
        validate_name(name)
        validate_email(email)
        validate_age(age)
        self.name = name
        self.email = email
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Age: {self.age}"
