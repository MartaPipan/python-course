import csv
from pathlib import Path
from datetime import datetime

class DuplicateBookError(ValueError): 
    pass

class Publication:
    def __init__(self, **kwargs):
        # Передаємо залишок аргументів далі до базового object
        super().__init__(**kwargs)  

    def delivery_description(self) -> str:
        return f"Публікація '{self.title}': спосіб доставки не визначено."


class Book:
    def __init__(self, title, author: str, year: int, **kwargs):
       
        if isinstance(title, (int, float)) and not isinstance(title, bool):
            title = str(title)

        if not title or not isinstance(title, str) or not title.strip(): 
            raise ValueError("Заповніть назву книги")
            
        if not author or not isinstance(author, str) or not author.strip():  
            raise ValueError("Заповніть автора книги")
            
        if isinstance(year, bool) or not isinstance(year, int) or year <= 0:  
            raise ValueError("Рік має бути коректним числом!")
        

        current_year = datetime.now().year
        if year > current_year:  
            raise ValueError(f"Рік видання не може бути в майбутньому (більше ніж {current_year})!")
            
        self.title = title.strip()  
        self.author = author.strip()  
        self.year = year  
        self.tags = []  
        
        super().__init__(**kwargs)  

    def add_tag(self, tag: str):  
      
        if not tag or not isinstance(tag, str) or not tag.strip():  
            raise ValueError("Заповніть жанр книги")  
            
        cleaned_tag = tag.strip()
        if cleaned_tag not in self.tags:
            self.tags.append(cleaned_tag)

    def __str__(self):  
        return f"'{self.title}' — {self.author} ({self.year}) | Жанри: {self.tags}"


class PrintedBook(Book, Publication):
    def __init__(self, pages_count: int, **kwargs):
        if isinstance(pages_count, bool) or not isinstance(pages_count, int) or pages_count <= 0:
            raise ValueError("Кількість сторінок має бути додатним числом")
            
        self.pages_count = pages_count
        super().__init__(**kwargs)

    def delivery_description(self) -> str:
        return f"Друкована книга '{self.title}' ({self.pages_count} стор.) буде доставлена поштою або кур'єром."


class EBook(Book, Publication):
    def __init__(self, download_url: str, **kwargs):
        if not download_url or not isinstance(download_url, str) or not download_url.strip():
            raise ValueError("Заповніть посилання на книгу")
            
        self.download_url = download_url.strip()
        super().__init__(**kwargs)

    def delivery_description(self) -> str:
        return f"Електронна книга '{self.title}' доступна за посиланням: {self.download_url}"



class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, book: Book):
        for existing_book in self.books:
            # Перевірка 1: Чи це той самий об'єкт у пам'яті
            if existing_book is book:
                raise DuplicateBookError(f"Об'єкт книги '{book.title}' вже додано в цю бібліотеку")
            
            # Перевірка 2: Унікальність за назвою, автором ТА типом класу
            if (existing_book.title.lower().strip() == book.title.lower().strip() and
                existing_book.author.lower().strip() == book.author.lower().strip() and
                type(existing_book) == type(book)):
                raise DuplicateBookError(f"Книга '{book.title}' ({type(book).__name__}) цього автора вже є в бібліотеці")
        self.books.append(book)

    def find_by_author(self, author_name: str):
        results = []
        if not author_name or not isinstance(author_name, str):
            return results
        search_name = author_name.lower().strip()
        for book in self.books:
            if search_name in book.author.lower():
                results.append(book)
        return results

    def find_by_tag(self, tag_name: str):
        results = []
        if not tag_name or not isinstance(tag_name, str):
            return results
        search_tag = tag_name.lower().strip()
        for book in self.books:
            for tag in book.tags:
                if tag.lower() == search_tag:
                    results.append(book)
                    break 
        return results

    def available_titles(self):
        titles = []
        for book in self.books:
            titles.append(book.title)
        return titles   

    def save_valid_books_to_csv(self, book_data=None):
        """
        Обробляє сирі дані, створює правильні об'єкти PrintedBook/EBook,
        перевіряє наявність книг у пам'яті та у CSV, блокуючи будь-які дублікати.
        """
        # Крок 2. Спочатку налаштуємо шлях до файлу, бо він потрібен для Кроку 1
        data_folder = Path.cwd() / "hw_11_prystatska"
        data_folder.mkdir(parents=True, exist_ok=True) 
        file_path = data_folder / "books.csv"
        
        # Крок 3. Зчитуємо книги, які ВЖЕ є у файлі CSV, за ключем (назва, автор, тип)
        existing_csv_books = set()
        if file_path.exists() and file_path.stat().st_size > 0:
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    t = row.get("title", "").strip().lower()
                    a = row.get("author", "").strip().lower()
                    c_type = row.get("type", "").strip().lower()
                    if t and a and c_type:
                        existing_csv_books.add((t, a, c_type))

        # Крок 1. Обробка переданого масиву словників book_data
        if book_data is not None:
            for item in book_data:
                try:
                    b_type = str(item.get("type", "")).strip().lower()
                    title = str(item.get("title", "")).strip()
                    author = str(item.get("author", "")).strip()
                    
                    if not title or not author:
                        continue

                    # 🌟 ГОЛОВНЕ ВИПРАВЛЕННЯ: Перевіряємо, чи книга вже є у файлі CSV
                    if (title.lower(), author.lower(), b_type) in existing_csv_books:
                        continue

                    # 🌟 ГОЛОВНЕ ВИПРАВЛЕННЯ: Перевіряємо, чи книга вже є у пам'яті бібліотеки self.books
                    already_in_memory = False
                    for existing_book in self.books:
                        current_obj_type = "printed" if isinstance(existing_book, PrintedBook) else "ebook"
                        if (existing_book.title.lower().strip() == title.lower() and
                            existing_book.author.lower().strip() == author.lower() and
                            current_obj_type == b_type):
                            already_in_memory = True
                            break
                    
                    if already_in_memory:
                        continue # Пропускаємо створення, якщо вона вже є в пам'яті

                    # Безпечне приведення року видання
                    raw_year = item.get("year")
                    if isinstance(raw_year, bool):
                        raise ValueError()
                    year = int(raw_year) if raw_year else None
                    
                    # Створюємо відповідний об'єкт
                    if b_type == "printed":
                        raw_pages = item.get("pages_count")
                        if isinstance(raw_pages, bool):
                            raise ValueError()
                        pages = int(raw_pages) if raw_pages else None
                        book = PrintedBook(title=title, author=author, year=year, pages_count=pages)
                    elif b_type == "ebook":
                        url = str(item.get("download_url", "")).strip()
                        book = EBook(title=title, author=author, year=year, download_url=url)
                    else:
                        continue 
                        
                    tags_str = item.get("tags", "")
                    if isinstance(tags_str, str) and tags_str:
                        for tag in tags_str.split(","):
                            if tag.strip():
                                book.add_tag(tag.strip())
                                
                    self.add_book(book)
                except Exception:
                    pass

        headers = ["title", "author", "year", "tags", "type", "pages_count", "download_url", "delivery_type"]
        
        # Оновлюємо список вже наявних книг у CSV на випадок, якщо під час парсингу щось змінилося
        existing_books = set()
        if file_path.exists() and file_path.stat().st_size > 0:
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    t = row.get("title", "").strip().lower()
                    a = row.get("author", "").strip().lower()
                    csv_type = row.get("type", "").strip().lower()
                    if t and a and csv_type:
                        existing_books.add((t, a, csv_type))

        # Крок 4. Фільтрація об'єктів перед безпосереднім записом
        valid_rows = []
        for book_obj in self.books:
            if isinstance(book_obj, PrintedBook):
                pages_csv = book_obj.pages_count
                url_csv = ""
                b_type = "printed"
            else:
                pages_csv = ""
                url_csv = book_obj.download_url
                b_type = "ebook"

            current_key = (book_obj.title.strip().lower(), book_obj.author.strip().lower(), b_type)
        
            if current_key in existing_books:
                continue

            valid_rows.append({
                "title": book_obj.title,
                "author": book_obj.author,
                "year": book_obj.year,
                "tags": ", ".join(book_obj.tags),
                "type": b_type,
                "pages_count": pages_csv,
                "download_url": url_csv,
                "delivery_type": book_obj.delivery_description()
            })

        # Крок 5. Запис унікальних рядків
        if not valid_rows:
            print(f"ℹ️ Усі унікальні книги з пам'яті бібліотеки вже існують у файлі {file_path.name}. Нічого не додано.")
            return

        file_is_empty = not file_path.exists() or file_path.stat().st_size == 0
        
        with open(file_path, mode="a", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            if file_is_empty:
                writer.writeheader()
            writer.writerows(valid_rows)
            
        print(f"Успішно додано нових унікальних книг ({len(valid_rows)}) до CSV за шляхом: {file_path}")
