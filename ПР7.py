#Завдання 1
print('Завдання 1')
class UserCreator:
    def create(self, name, email):
        print(f"Створено: {name} ({email})")
        return {"name": name, "email": email}
class UserUpdater:
    def update(self, user, name=None, email=None):
        if name: user["name"] = name; print(f"Ім'я змінено на {name}")
        if email: user["email"] = email; print(f"Email змінено на {email}")
        return user
class UserDeleter:
    def delete(self, user_id):
        print(f"Видалено користувача з ID {user_id}")

creator = UserCreator()
updater = UserUpdater()
deleter = UserDeleter()

user = creator.create("Іван", "ivan@example.com")
updater.update(user, name="Іван Петренко")
deleter.delete(123)

#Завдання 2
print('Завдання 2')
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, r): self.radius = r
    def area(self): return math.pi * self.radius**2
class Rectangle(Shape):
    def __init__(self, w, h): self.width, self.height = w, h
    def area(self): return self.width * self.height
class AreaCalculator:
    def calculate(self, shape: Shape): return shape.area()
calc = AreaCalculator()
print(f"Коло: {calc.calculate(Circle(5))}")
print(f"Прямокутник: {calc.calculate(Rectangle(4, 6))}")
class Triangle(Shape):
    def __init__(self, b, h): self.base, self.height = b, h
    def area(self): return 0.5 * self.base * self.height
print(f"Трикутник: {calc.calculate(Triangle(3, 8))}")

#Завдання 3
print('Завдання 3')
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self): pass
class Rectangle(Shape):
    def __init__(self, w, h): self._w, self._h = w, h
    @property
    def width(self): return self._w
    @width.setter
    def width(self, v): self._w = v
    @property
    def height(self): return self._h
    @height.setter
    def height(self, v): self._h = v
    def area(self): return self._w * self._h
class Square(Rectangle):
    def __init__(self, s): super().__init__(s, s)
    @Rectangle.width.setter
    def width(self, v): self._w = self._h = v
    @Rectangle.height.setter
    def height(self, v): self._w = self._h = v
class Circle(Shape):
    def __init__(self, r): self.radius = r
    def area(self): return math.pi * self.radius**2
def print_area(s: Shape): print(f"Площа: {s.area()}")
def resize_rect(r: Rectangle, w, h): r.width, r.height = w, h; print(f"Розміри: {r.width}x{r.height}, Площа: {r.area()}")

rect = Rectangle(4, 6)
square = Square(5)
circle = Circle(3)

print_area(rect)
print_area(square)
print_area(circle)

resize_rect(rect, 5, 7)
resize_rect(square, 8, 8)

#Завдання 4
print('Завдання 4')
from abc import ABC, abstractmethod
class Printable(ABC):
    @abstractmethod
    def print_doc(self, doc): pass
class Scannable(ABC):
    @abstractmethod
    def scan_doc(self, doc): pass
class Copyable(ABC):
    @abstractmethod
    def copy_doc(self, doc): pass
class Printer(Printable):
    def print_doc(self, doc): print(f"Друк: {doc}")
class Scanner(Scannable):
    def scan_doc(self, doc): print(f"Скан: {doc}")
class MFP(Printable, Scannable, Copyable):
    def print_doc(self, doc): print(f"Друк MFP: {doc}")
    def scan_doc(self, doc): print(f"Скан MFP: {doc}")
    def copy_doc(self, doc): print(f"Копія MFP: {doc}")

p = Printer()
s = Scanner()
mfp = MFP()

p.print_doc("звіт.pdf")
s.scan_doc("договір.docx")
mfp.copy_doc("стаття.txt")

#Завдання 5
print('Завдання 5')
from abc import ABC, abstractmethod
class MsgSender(ABC):
    @abstractmethod
    def send(self, to, msg): pass
class EmailSender(MsgSender):
    def send(self, to, msg): print(f"Email на {to}: {msg}")
class SMSSender(MsgSender):
    def send(self, to, msg): print(f"SMS на {to}: {msg}")
class Notifier:
    def __init__(self, sender: MsgSender): self.sender = sender
    def notify(self, user_id, msg):
        recipient = "user1@example.com" if user_id == 1 else "+380123456789" if user_id == 2 else "unknown"
        self.sender.send(recipient, f"Для {user_id}: {msg}")

email_s = EmailSender()
sms_s = SMSSender()
notifier_email = Notifier(email_s)
notifier_sms = Notifier(sms_s)

notifier_email.notify(1, "Замовлення оброблено.")
notifier_sms.notify(2, "Нове сповіщення.")
