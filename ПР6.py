#Завдання 1
class User:
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

user = User("Іван", "ivan@gmail.com", "secure_password")

print("Ім'я:", user.get_name())
print("Електронна пошта:", user.get_email())
print("Пароль:", user.get_password())

user.set_name("Петро")
user.set_email("petro@gmail.com")
user.set_password("new_secure_password")

print("\nЗмінене ім'я:", user.get_name())
print("Змінена електронна пошта:", user.get_email())
print("Змінений пароль:", user.get_password())

#Завдання 2
import math

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

print("Площа кола:", circle.calculate_area())
print("Площа прямокутника:", rectangle.calculate_area())
print("Площа трикутника:", triangle.calculate_area())
