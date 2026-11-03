class DuplicateBookError(ValueError): 
    pass

class Publication:
    def __init__(self, **kwargs):
        # Передаємо залишок аргументів далі по ланцюжку MRO до базового object
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
        

        if year > 2026:  
            raise ValueError("Рік видання не може бути в майбутньому!")
            
        self.title = title.strip()  
        self.author = author.strip()  
        self.year = year  
        self.tags = []  
        
        # Передаємо залишок аргументів далі по MRO (до Publication)
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
            if existing_book is book:
                raise DuplicateBookError(f"Об'єкт книги '{book.title}' вже додано в цю бібліотеку")
        self.books.append(book)

    def find_by_author(self, author_name: str):
        results = []
        if not author_name or not isinstance(author_name, str):
            return results
        search_name = author_name.lower().strip()
   
        for book in self.books:
            if book.author.lower() == search_name:
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
