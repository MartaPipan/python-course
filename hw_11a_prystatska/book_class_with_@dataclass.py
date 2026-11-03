# Файл: models.py
from dataclasses import dataclass, field

class DuplicateBookError(ValueError):
    pass

@dataclass
class Book:
    title: str
    author: str
    year: int
    tags: list[str] = field(default_factory=list)

    def __str__(self):
        return f"'{self.title}' — {self.author} ({self.year}) | Теги: {', '.join(self.tags)}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        for existing_book in self.books:
            if existing_book is book:
                raise DuplicateBookError(f"Книгу '{book.title}' вже додано в бібліотеку!")
        self.books.append(book)

    def find_by_author(self, author_name: str) -> list[Book]:
        results = []
        search_name = author_name.lower()
        
        for book in self.books:
            if book.author.lower() == search_name:
                results.append(book)
                
        return results

    def available_titles(self) -> list[str]:
        titles = []
        for book in self.books:
            titles.append(book.title)
        return titles
