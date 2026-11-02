from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    price: float

    # Валідація складних правил після автоматичної ініціалізації
    def __post_init__(self):
        if not self.title.strip():
            raise ValueError("Назва книги не може бути порожньою!")
        if not self.author.strip():
            raise ValueError("Автор має бути вказаний!")
        if self.price < 0:
            raise ValueError("Ціна книги не може бути від'ємною!")

    # Метод форматованого опису (Логіка об'єкта)
    def get_formatted_description(self) -> str:
        return f"📖 '{self.title}' – {self.author} | Ціна: {self.price:.2f} грн"


# ==========================================
# 🎮 ТЕСТУВАННЯ В ДІЇ
# ==========================================
if __name__ == "__main__":
    print("--- 1. Успішне створення книги ---")
    # Конструктор __init__ згенеровано автоматично через @dataclass
    book1 = Book("Місто", "В. Підмогильний", 250.00)
    
    # Викликаємо метод форматованого опису
    print(book1.get_formatted_description())

    print("\n--- 2. Спроба створити книгу з некоректною ціною ---")
    try:
        # Валідація в __post_init__ заблокує створення цієї книги
        invalid_book = Book("Тигролови", "І. Багряний", -15.50)
    except ValueError as e:
        print(f"🔒 Захист моделі успішно спрацював! Помилка: {e}")
