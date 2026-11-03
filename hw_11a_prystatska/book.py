import csv
from pathlib import Path

class DuplicateBookError(Exception):
    pass

class Publication:
    def __init__(self, **kwargs):
        # Передаємо залишок аргументів далі по ланцюжку MRO
        super().__init__(**kwargs)  

    def delivery_description(self):
        return f"Книга '{self.title}': спосіб доставки не визначено."  


class Book:  # 4
    def __init__(self, title: str, author: str, year: int, **kwargs):  # 5
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


    def add_tag(self, tag: str):  
        tag = tag.strip()  
        if not tag:  
            raise ValueError("Заповніть жанр книги")  
        self.tags.append(tag)  

    def __str__(self):  
        return f"'{self.title}' — {self.author} ({self.year}) | Жанри: {self.tags}"  



class PrintedBook(Book, Publication):
    def __init__(self, pages_count: int, **kwargs):
        super().__init__(**kwargs)  
        
        if not isinstance(pages_count, int) or pages_count <= 0:
            raise ValueError("Кількість сторінок має бути додатним числом!")
        self.pages_count = pages_count

    def delivery_description(self):
        return f"Друкована книга '{self.title}' ({self.pages_count} стор.) буде доставлена поштою."



class EBook(Book, Publication):
    def __init__(self, download_url: str, **kwargs):
        super().__init__(**kwargs) 
        
        if not download_url or not download_url.strip():
            raise ValueError("Заповніть посилання на книгу")
        self.download_url = download_url.strip()

    def delivery_description(self):
        return f"Електронна книга '{self.title}' доступна за посиланням: {self.download_url}"
