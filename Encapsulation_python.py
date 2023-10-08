class Person:
    def __init__(self, name, age, email):
        self.__name = name  # Private attribute "_ _ "
        self.__age = age    # Private attribute
        self.__email = email  # Private attribute

    # Public methods to set attributes
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_email(self, email):
        self.__email = email

    # Public methods to get attributes
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

# Create a Person object
person = Person("Alice", 30, "alice@example.com")

# Access and modify attributes using public methods
print(f"Name: {person.get_name()}")
print(f"Age: {person.get_age()}")
print(f"Email: {person.get_email()}")

person.set_name("Bob")
person.set_age(25) 
person.set_email("bob@example.com")

print(f"Updated Name: {person.get_name()}")
print(f"Updated Age: {person.get_age()}")
print(f"Updated Email: {person.get_email()}")

# output :
Name :Alice
Age:30
Email:alice@example.com

Updated Name:Bob
Update Age:25
Updated Email:bob@example.com
