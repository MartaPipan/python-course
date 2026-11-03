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


import csv
from pathlib import Path

class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, book: Book):
        for existing_book in self.books:
            if existing_book is book:
                raise DuplicateBookError(f"Об'єкт книги '{book.title}' вже додано в цю бібліотеку")
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
        Бере вже створені, перевірені та додані через add_book об'єкти
        зі списку self.books і зберігає їх у файл books.csv, уникаючи дублікатів.
        """
        data_folder = Path.cwd() / "hw_11_prystatska"
        data_folder.mkdir(parents=True, exist_ok=True) 
        file_path = data_folder / "books.csv"
        
        headers = ["title", "author", "year", "tags", "type", "pages_count", "download_url", "delivery_type"]
        
        # 1. Зчитуємо книги, які ВЖЕ є у файлі, щоб не дописувати їх повторно
        existing_books = set()
        if file_path.exists() and file_path.stat().st_size > 0:
            with open(file_path, mode="r", encoding="utf-8") as file:
               
                reader = csv.DictReader(file)
                for row in reader:
                    title = row.get("title", "").strip().lower()
                    author = row.get("author", "").strip().lower()
                    if title and author:
                        # Зберігаємо (назва, автор) як унікальний ключ
                        existing_books.add((title, author))

        valid_rows = []
        
        #  у пам'яті та фільтруємо дублікати
        for book_obj in self.books:
            current_key = (book_obj.title.strip().lower(), book_obj.author.strip().lower())
        
            if current_key in existing_books:
                continue

            if isinstance(book_obj, PrintedBook):
                pages_csv = book_obj.pages_count
                url_csv = ""
                b_type = "printed"
            else:
                pages_csv = ""
                url_csv = book_obj.download_url
                b_type = "ebook"

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

        if not valid_rows:
            print(f"ℹУсі книги з пам'яті бібліотеки вже існують у файлі {file_path.name}. Нічого не додано.")
            return

        file_is_empty = not file_path.exists() or file_path.stat().st_size == 0
        
        with open(file_path, mode="a", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            
            if file_is_empty:
                writer.writeheader()
             
            writer.writerows(valid_rows)
            
        print(f" Успішно додано нових книг ({len(valid_rows)}) до CSV за шляхом: {file_path}")
