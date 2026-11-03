from models import Book, PrintedBook, EBook, Library, DuplicateBookError

library = Library()
print(f"Порожня бібліотека: {library.available_titles()}")

print("--- 1. Демонстрація створення книг із валідацією для порожньої бібліотеки ---")

book1 = PrintedBook(title=1984, author="Джордж Орвелл", year=1949, pages_count=320)
book2 = EBook(title="Колгосп тварин", author="Джордж Орвелл", year=1945, download_url="https://library.com")
book3 = PrintedBook(title="Гаррі Поттер і філософський камінь", author="Джоан Роулінг", year=1997, pages_count=320)
book4 = EBook(title="Гобіт, або Туди і назад", author="Джон Р. Р. Толкін", year=1937, download_url="https://library.com")
book5 = PrintedBook(title="Кобзар", author="Тарас Шевченко", year=1840, pages_count=450)

print(f"Книга 1 (Printed, числова назва): {book1}")
print(f"Книга 2 (EBook): {book2}")
print(f"Книга 3 (Printed): {book3}")
print(f"Книга 4 (EBook): {book4}")
print(f"Книга 5 (Printed): {book5}")


print("\n--- 2. Перевірка незалежності списків tags (додаємо унікальні жанри) ---")
book1.add_tag("антиутопія")
book1.add_tag("класика")

book3.add_tag("фентезі")
book3.add_tag("пригоди")

book4.add_tag("фентезі")

book5.add_tag("поезія")

print("\n Перевірка захисту від порожнього жанру ")
try:
    print("Намагаємося додати порожній жанр до Книги 2 (EBook)")
    book2.add_tag("   ") 
except ValueError as error:
    print(f" Перехоплено помилку: {error}")


print(f"Книга 1 (Орвелл) після тегів: {book1}")
print(f"Книга 2 (Орвелл, має бути без тегів): {book2}")
print(f"Книга 3 (Роулінг) після тегів: {book3}")

if len(book2.tags) == 0:
    print("Списки tags незалежні для кожного об'єкта")


print("\n--- 3. Додавання каталогу книг до бібліотеки ---")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
print(f"Усі назви книг в бібліотеці: {library.available_titles()}")


print("\n пошук за автором")
print("Шукаємо автора 'дЖоРдЖ оРвЕлЛ':")
orwell_books = library.find_by_author("дЖоРдЖ оРвЕлЛ")
for b in orwell_books:
    print(f"  Знайдено: {b}")

print("\nШукаємо автора 'Тарас Шевченко':")
shevchenko_books = library.find_by_author("Тарас Шевченко")
for b in shevchenko_books:
    print(f"Знайдено: {b}")


print("\nШукаємо автора 'Стівен Кінг':")
not_found = library.find_by_author("Стівен Кінг")
print(f"Автор, якого немає: {not_found}")


print("\n пошук за жанром")

print("Шукаємо книги з жанром 'ФЕНТЕЗІ':")
fantasy_books = library.find_by_tag("ФЕНТЕЗІ")
for b in fantasy_books:
    print(f"Знайдено за жанром: {b.title} (автор: {b.author})")


print("\nШукаємо книги з жанром 'поезія':")
poetry_books = library.find_by_tag("поезія")
for b in poetry_books:
    print(f" Знайдено за жанром: {b.title}")


print("\nШукаємо книги з жанром 'детектив':")
detectives = library.find_by_tag("детектив")
print(f" Результат пошуку (має бути порожнім): {detectives}")


print("\n ПЕРЕВІРКА BOOK (ВАЛІДАЦІЯ)")


try:
    print("Тест 1: Спроба створити книгу з порожніми пробілами замість назви...")
  
    bad_book = PrintedBook(title="   ", author="Джордж Орвелл", year=1949, pages_count=120)
except ValueError as error:
    print(f" Перехоплено помилку назви: {error}")

try:
    print("\nТест 2: Спроба створити книгу без автора...")

    bad_book = EBook(title="Колгосп тварин", author="", year=1945, download_url="https://link.com")
except ValueError as error:
    print(f" Перехоплено помилку автора: {error}")


try:

    bad_book = PrintedBook(title="Тестова Книга", author="Автор", year="2026", pages_count=100)
except ValueError as error:
    print(f"Перехоплено помилку типу року: {error}")


try:
    print("\nТест 4: Спроба передати логічне значення True замість року...")
   
    bad_book = PrintedBook(title="Тестова Книга", author="Автор", year=True, pages_count=100)
except ValueError as error:
    print(f"Перехоплено помилку bool-року: {error}")


try:
    print("\nТест 5: Спроба передати від'ємний рік (-500 рік)...")

    bad_book = PrintedBook(title="Антична Книга", author="Філософ", year=-500, pages_count=150)
except ValueError as error:
    print(f"Перехоплено помилку від'ємного року: {error}")


try:
    print("\nТест 6: Спроба створити книгу з майбутнього (2028 рік)...")
  
    bad_book = PrintedBook(title="Книга з майбутнього", author="Фантаст", year=2028, pages_count=200)
except ValueError as error:
    print(f" Перехоплено помилку майбутнього часу: {error}")
 


print("\n ПеревіркаDuplicateBookError")
try:
    print("Додаєм існуючий екземпляр книги (book3) удруге...")
    library.add_book(book3)
except DuplicateBookError as error:
    print(f" Результат DuplicateBookError: {error}")
    if isinstance(error, ValueError):
        print(" DuplicateBookError наслідує ValueError")
except Exception as error:
    print(f"ПОМИЛКА: {type(error)}")


print("\n Перевірка Поліморфізму. Викликаємо метод доставки для ВСІХ книг бібліотеки без перевірки їхнього точного типу:")
for current_book in library.books:
    print(f"  {current_book.delivery_description()}")

    print(" АВТОМАТИЧНА ОБРОБКА ТА ФІЛЬТРАЦІЯ МАСИВУ ДАНИХ")
    book_data = [
        {"title": "Тигролови", "author": "Іван Багряний", "year": "1944", "tags": "пригоди, класика", "type": "printed", "pages_count": 320},
        {"title": "Місто", "author": "Валер'ян Подмогильний", "year": "1928", "tags": "модернізм", "type": "printed", "pages_count": 290},
        {"title": "Фелікс Австрія", "author": "Софія Андрухович", "year": "2014", "tags": "історія", "type": "ebook", "download_url": "https://library.com"},
        # Невалідні дані для перевірки фільтрації:
        {"title": " ", "author": "Ліна Костенко", "year": "2010", "type": "printed", "pages_count": 150},
        {"title": "Майбутній вік", "author": "Футурист", "year": "2035", "type": "printed", "pages_count": 200},
        {"title": "Тигролови", "author": "Іван Багряний", "year": "1944", "tags": "пригоди, класика", "type": "printed", "pages_count": 320},
        {"title": "Місто", "author": "Валер'ян Подмогильний", "year": "1928", "tags": "модернізм", "type": "printed", "pages_count": 290},
        {"title": "Фелікс Австрія", "author": "Софія Андрухович", "year": "2014", "tags": "історія", "type": "ebook", "download_url": "https://library.com"},
        
        # НОВІ КНИГИ ЯК EBOOK ДЛЯ ПЕРЕВІРКИ (Мають успішно записатися, бо тип інший!)
        {"title": "Фелікс Австрія", "author": "Софія Андрухович", "year": "2014", "tags": "історія", "type": "printed", "pages_count": 290},
        {"title": "Тигролови", "author": "Іван Багряний", "year": "1944", "tags": "пригоди, класика, аудіо", "type": "ebook", "download_url": "https://library.com"},
        {"title": "Місто", "author": "Валер'ян Подмогильний", "year": "1928", "tags": "модернізм, урбаністика", "type": "ebook", "download_url": "https://library.com"},
        
        # Дані для перевірки ігнорування тотожних дублікатів (Не мають записатися вдруге):
        {"title": "Фелікс Австрія", "author": "Софія Андрухович", "year": "2014", "tags": "історія", "type": "ebook", "download_url": "https://library.com"},
        
        # Невалідні дані для перевірки фільтрації помилок (Блокуються валідаторами класу):
        {"title": " ", "author": "Ліна Костенко", "year": "2010", "type": "printed", "pages_count": 150},
        {"title": "Майбутній вік", "author": "Футурист", "year": "2035", "type": "printed", "pages_count": 200}
    ]

    print("Запускаємо імпорт, фільтрацію та збереження в CSV...")
    library.save_valid_books_to_csv(book_data)


    print("Запускаємо імпорт та збереження...")

    library.save_valid_books_to_csv(book_data) 
    
    print(f"Кількість книг у пам'яті після імпорту: {len(library.books)}\n")

    # 5. Перевірка пошуку та поліморфізму
    print("--- 4. ПЕРЕВІРКА ПОШУКУ ТА ПОЛІМОРФІЗМУ ---")
    print("Шукаємо книги автора 'Орвелл':")
    for b in library.find_by_author("Орвелл"):
        print(f"   Знайдено: {b.title} | {b.delivery_description()}")

    print("\n" + "=" * 60)
    print(" ДЕМО ЗАВЕРШЕНО ")
    print("=" * 60)

