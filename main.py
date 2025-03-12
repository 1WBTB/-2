import utilities

numbers = [1, 5, 2, 8, 3]

average = utilities.calculate_average(numbers)
maximum = utilities.find_max(numbers)

print("Середнє значення:", average)
print("Максимальне число:", maximum)

numbers2 = []
average2 = utilities.calculate_average(numbers2)
maximum2 = utilities.find_max(numbers2)

print(f"Середнє значення порожнього списку: {average2}")
print(f"Максимальне значення порожнього списку: {maximum2}")
