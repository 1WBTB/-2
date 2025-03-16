#Завдання 1
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        if self.species == "собака":
            print("Гав!")
        elif self.species == "кіт":
            print("Мяу!")
        else:
            print("Тварина видає звук.")

dog = Animal("Рекс", "собака", 3)
cat = Animal("Мурчик", "кіт", 5)

dog.make_sound()  
cat.make_sound()

#Завдання 2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(7, 3)

print("Площа прямокутника 1:", rectangle1.calculate_area())
print("Площа прямокутника 2:", rectangle2.calculate_area())

#Завдання 3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Це {self.make} {self.model} {self.year} року виробництва.")


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print("Двигун автомобіля запущено.")

    def display_info(self):
        super().display_info()
        print(f"Тип палива: {self.fuel_type}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

    def display_info(self):
        super().display_info()
        print(f"Розмір двигуна: {self.engine_size} куб. см")


class Bicycle(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

    def display_info(self):
        super().display_info()
        print(f"Тип велосипеда: {self.type}")

car = Car("Toyota", "Camry", 2022, "Бензин")
motorcycle = Motorcycle("Honda", "CBR500R", 2021, 471)
bicycle = Bicycle("Giant", "Talon", 2020, "Гірський")

car.display_info()
motorcycle.display_info()
bicycle.display_info()

#Завдання 4
vehicles = [car, motorcycle, bicycle]

for vehicle in vehicles:
    vehicle.display_info()





