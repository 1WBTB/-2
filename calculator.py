def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    return "Помилка: ділення на нуль!"
  return a / b

if __name__ == "__main__":
  try:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    operation = input("Введіть операцію (+, -, *, /): ")

    if operation == '+':
      result = add(num1, num2)
    elif operation == '-':
      result = subtract(num1, num2)
    elif operation == '*':
      result = multiply(num1, num2)
    elif operation == '/':
      result = divide(num1, num2)
    else:
      result = "Невірна операція"

    print("Результат:", result)
  except ValueError:
    print("Помилка: введено не числове значення!")
