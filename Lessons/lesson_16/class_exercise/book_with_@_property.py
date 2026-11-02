class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        # ВИПРАВЛЕНО: викликаємо сеттер (без підкреслення), щоб ціна перевірялася при створенні!
        self.price = price  

    @property
    def price(self):
        """Геттер: повертає значення ціни без дужок ()"""
        return self._price

    @price.setter
    def price(self, value: float):
        """Сеттер: перевіряє ціну перед її зміною"""
        if value < 0:
            raise ValueError(f"Ціна для книги '{self.title}' не може бути від'ємною!")
        self._price = value

    def __str__(self):
        # Метод форматованого опису (викликає властивість price)
        return f"Книга: '{self.title}' | Автор: {self.author} | Ціна: {self.price:.2f} грн"

# ВИПРАВЛЕНО: прибрано зайвий відступ перед списком
valid_books = []
invalid_books = []  # Список для невалідних даних

books_data = [
    {"title": "Майстер і Маргарита", "author": "Михайло Булгаков", "price": 300.00},
    {"title": "1984", "author": "Джордж Орвелл", "price": 200.00},
    {"title": "Бракована Книга", "author": "Невідомий", "price": -50.00}, # Тепер тут точно спрацює помилка
    {"title": "Гаррі Поттер", "author": "Дж. К. Роулінг", "price": 400.00}
]

for data in books_data:
    try:
        # Пробуємо створити книгу
        new_book = Book(data["title"], data["author"], data["price"])
        # Якщо помилки немає — додаємо до списку валідних
        valid_books.append(new_book)
    except ValueError as error:
        # Якщо ціна від'ємна, перехоплюємо помилку і просто виводимо попередження
        print(f"Помилка валідації: {error}")
        invalid_books.append(data)


print("\n--- СПИСОК НЕВАЛІДНИХ КНИГ ---")
for data in invalid_books:
    print(f"Книга: '{data['title']}' | Автор: {data['author']}' | Ціна: {data['price']} грн")


print("\n--- ПЕРЕВІРКА РОБОТИ ГЕТТЕРА ТА СЕТТЕРА ---")
# Беремо першу книгу зі списку валідних ("Майстер і Маргарита")
test_book = valid_books[0]

# Звертаємось до price як до звичайної змінної (працює геттер)
print(test_book.price)  # Виведе: 300.0

# Змінюємо ціну (працює сеттер)
test_book.price = 350.50
print(test_book)  # Виведе оновлений опис

# Спроба встановити некоректну ціну викличе помилку
try:
    test_book.price = -50
except ValueError as e:
    print(f"Помилка: {e}")  # Виведе: Помилка: Ціна для книги 'Майстер і Маргарита' не може бути від'ємною!
