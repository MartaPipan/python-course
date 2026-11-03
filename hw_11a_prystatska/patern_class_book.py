import csv
from pathlib import Path  # 1

class DuplicateBookError(Exception):  # 2
    pass  # 3

class Book:  # 4
    def __init__(self, title: str, author: str, year: int):  # 5
        if not title or not title.strip():  # 6
            raise ValueError("Заповніть назву книги")  # 7
        if not author or not author.strip():  # 8
            raise ValueError("Заповніть автора книги")  # 9
        if not isinstance(year, int) or year <= 0:  # 10
            raise ValueError("Рік має бути коректним числом!")  # 11
            
        self.title = title.strip()  # 12
        self.author = author.strip()  # 13
        self.year = year  # 14
        self.tags = []  # 15

    def delivery_description(self):
        return f"Книга '{self.title}': спосіб доставки не визначено."  

    def add_tag(self, tag: str):  
        tag = tag.strip()  
        if not tag:  
            raise ValueError("Заповніть жанр книги")  
        self.tags.append(tag)  

    def __str__(self):  
        return f"'{self.title}' — {self.author} ({self.year}) | Жанри: {self.tags}"  


# Дочірній клас для паперових книг
class PrintedBook(Book):
    def __init__(self, title: str, author: str, year: int, pages_count: int):
        super().__init__(title, author, year)  
        if not isinstance(pages_count, int) or pages_count <= 0:
            raise ValueError("Кількість сторінок має бути додатним числом!")
        self.pages_count = pages_count

    def delivery_description(self) -> str:
        return f"Паперова книга '{self.title}' ({self.pages_count} стор.) буде доставлена поштою."


# Дочірній клас для електронних книг
class EBook(Book):
    def __init__(self, title: str, author: str, year: int, download_url: str):
        super().__init__(title, author, year)  
        if not download_url or not download_url.strip():
            raise ValueError("Заповніть посилання на книгу")
        self.download_url = download_url.strip()

    def delivery_description(self) -> str:
        return f"Електронна книга '{self.title}' доступна за посиланням: {self.download_url}"  


class Library:  # 23
    def __init__(self):  # 24
        self.books = []  # 25

    def add_book(self, book: Book):  # 26
        for existing_book in self.books:  # 27
            if existing_book.title.lower() == book.title.lower() and existing_book.author.lower() == book.author.lower():  # 28
                raise DuplicateBookError(f"Книгу '{book.title}' ({book.author}) вже додано в бібліотеку")  # 29
        self.books.append(book)  # 30

    def available_titles(self):  # 31
        return [book.title for book in self.books]  # 32

    def find_by_author(self, author_name: str):  # 33
        results = []  # 34
        search_name = author_name.lower()  # 35
        for book in self.books:  # 36
            if book.author.lower() == search_name:  # 37
                results.append(book)  # 38
        return results  # 39


# --- Глобальний об'єкт бібліотеки ---
library = Library()  # 40


# --- Правильно оформлена функція імпорту з використанням Path ---
def import_books(file_name: str = "books.csv"):
    csv_path = Path.cwd() / "hw_11a_prystatska" / file_name    
    
    print(f"Шукаю файл за шляхом: {csv_path}\n")
    
    try:
        with open(csv_path, mode='r', encoding='utf-8') as file:  # 41
            reader = csv.DictReader(file)  # 42
            
            for row_num, row in enumerate(reader, start=1):  # 43
                try:  # 44
                    raw_title = row.get('title')  # 45
                    raw_author = row.get('author')  # 46
                    raw_year = row.get('year')  # 47
                    
                    if not raw_year or not raw_year.strip():  # 48
                        raise ValueError("Рік видання відсутній у файлі CSV")  # 49
                        
                    validated_year = int(raw_year)  # 50
                    
                    # --- РОЗУМНЕ ВИЗНАЧЕННЯ ТИПУ КНИГИ З CSV ---
                    raw_pages = row.get('pages_count') or row.get('pages')
                    raw_url = row.get('download_url') or row.get('url')
                    
                    if raw_url and raw_url.strip():

                        new_book = EBook(raw_title, raw_author, validated_year, raw_url)
                    elif raw_pages and raw_pages.strip():
                        # Якщо є сторінки, створюємо Друковану книгу
                        new_book = PrintedBook(raw_title, raw_author, validated_year, int(raw_pages))
                    else:
                        # За замовчуванням створюємо Базову книгу
                        new_book = Book(raw_title, raw_author, validated_year)  # 51
                    
                    raw_tags = row.get('tags', '')  # 52
                    if raw_tags:  # 53
                        for tag in raw_tags.split(','):  # 54
                            if tag.strip():  # 55
                                new_book.add_tag(tag)  # 56
                        
                    library.add_book(new_book)  # 57
                    print(f"[Рядок {row_num}] Додано: {new_book}")  # 58
                    
                except DuplicateBookError as error:  # 59
                    print(f"[Рядок {row_num}] Пропущено дублікат: {error}")  # 60
                except ValueError as error:  # 61
                    print(f"[Рядок {row_num}] Помилка даних (пропущено): {error}")  # 62
                    
    except FileNotFoundError:
        print(f"Помилка: Файлу '{file_name}' не знайдено в папці 'hw_11a_prystatska'!")


# =====================================================================
# ПЕРЕВІРКА АВТОМАТИЧНОГО ІМПОРТУ ТА ПОЛІМОРФІЗМУ
# =====================================================================

# 1. Запуск імпорту книг із файлу
import_books("books.csv")

print("\nУсі назви книг в бібліотеці:")  # 63
print(library.available_titles())  # 64

# 2. Один цикл викликає delivery_description() для ВСІХ імпортованих книг без перевірки типу!
print("\n--- Автоматична обробка доставки для ВСІХ книг бібліотеки (Поліморфізм) ---")
for current_book in library.books:
    print(current_book.delivery_description())






"""# Базовий клас для всіх публікацій
class Publication:
    def __init__(self, title: str):
        self.title = title

    def delivery_description(self) -> str:
        # Цей метод буде перевизначено в підкласах
        return f"Публікація '{self.title}': спосіб доставки не визначено."


# Підклас для друкованих книг
class PrintedBook(Publication):
    def __init__(self, title: str, weight_grams: int):
        super().__init__(title)  # Передаємо назву в базовий клас
        self.weight_grams = weight_grams

    def delivery_description(self) -> str:
        # Своя логіка доставки для друкованої книги
        return f"Друкована книга '{self.title}' (вага: {self.weight_grams}г) буде доставлена кур'єром або поштою."


# Підклас для електронних книг
class EBook(Publication):
    def __init__(self, title: str, download_url: str):
        super().__init__(title)  # Передаємо назву в базовий клас
        self.download_url = download_url

    def delivery_description(self) -> str:
        # Своя логіка доставки для електронної книги
        return f"Електронна книга '{self.title}' доступна для миттєвого завантаження за посиланням: {self.download_url}"


# --- Перевірка роботи в одному циклі (Поліморфізм) ---

# Створюємо список, де лежать об'єкти різних класів
publications_list = [
    PrintedBook("Гаррі Поттер", 650),
    EBook("1984", "https://library.com"),
    PrintedBook("Кобзар", 400),
    EBook("Колгосп тварин", "https://library.com")
]

print("--- Обробка доставки публікацій ---")

# Один спільний цикл для всіх об'єктів
for pub in publications_list:
    # Викликаємо метод БЕЗ перевірки типу (Python сам знає, чий метод запустити)
    print(pub.delivery_description())
"""