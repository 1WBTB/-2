#Умовні конструкції:
#Перевірка паролю
password = "password123"
user_password = "password123"
if user_password == password:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

#Визначення днів тижня
day_number = 3
if day_number == 1:
    print("Понеділок")
elif day_number == 2:
    print("Вівторок")
elif day_number == 3:
    print("Середа")
elif day_number == 4:
    print("Четвер")
elif day_number == 5:
    print("П'ятниця")
elif day_number == 6:
    print("Субота")
elif day_number == 7:
    print("Неділя")
else:
    print("Неправильний номер дня")

#Цикли:
#Таблиця множення
number = 7
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#Сума чисел
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Сума чисел: {total}")

#Факторіал числа
number = 5
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Факторіал {number}: {factorial}")

#Парні числа
for i in range(2, 51, 2):
    print(i)

#Пошук простих чисел
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
for num in range(2, 51):
    if is_prime(num):
        print(num)

#Списки:
#Робота із списками
my_list = [1, 2, 3, 4, 5]
my_list.append(10)
my_list.append(20)
my_list.remove(10)
print(my_list)

#Знаходження суми
my_list = [1, 2, 3, 4, 5]
total = sum(my_list)
print(f"Сума: {total}")

#Подвійні значення
my_list = [1, 2, 3, 4, 5]
doubled_list = [num * 2 for num in my_list]
print(doubled_list)

#Кортежі:
#Робота із кортежами
my_tuple = ("яблуко", "банан", "апельсин")
for item in my_tuple:
    print(item)

#Об'єднання кортежів
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

#Словники:
#Робота із словниками
athlete = {
    "ім'я": "Усейн Болт",
    "вік": 34,
    "спорт": "легка атлетика",
    "команда": "Ямайка"
}
for key, value in athlete.items():
    print(f"{key}: {value}")

#Оновлення словника:
favorite_books = {
    "Майстер і Маргарита": 1967,
    "1984": 1949
}

favorite_books["Гаррі Поттер і філософський камінь"] = 1997
print(favorite_books)

#Пошук значення
capitals = {
    "Україна": "Київ",
    "Франція": "Париж",
    "Німеччина": "Берлін"
}
country = "Україна"
if country in capitals:
    print(f"Столиця {country}: {capitals[country]}")
else:
    print(f"Країна {country} не знайдена")















































