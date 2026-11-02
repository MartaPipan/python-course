class Credits:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # Якщо правий об'єкт іншого класу — чемно кажемо Python, що не вміємо з цим працювати
        if not isinstance(other, Credits):
            return NotImplemented
        # Якщо класи однакові — повертаємо НОВИЙ об'єкт Credits із сумою балів
        return Credits(self.value + other.value)

    # Додаємо для зручної діагностики
    def __repr__(self):
        return f"Credits(value={self.value})"


# ==========================================
# 🎮 ТЕСТУВАННЯ В ДІЇ
# ==========================================
if __name__ == "__main__":
    c1 = Credits(40)
    c2 = Credits(60)

    # 1. Сценарій 1: Правильне додавання однакових класів
    total = c1 + c2
    print(f"Результат додавання: {total}")  # Виведе: Credits(value=100)

    # 2. Сценарій 2: Спроба додати число (Некоректна операція)
    try:
        corrupted = c1 + 5  # 5 — це int, а не Credits
    except TypeError as e:
        print(f"🔒 Захист спрацював! Помилка: {e}")
        # Виведе: unsupported operand type(s) for +: 'Credits' and 'int'



"""
 А як зробити так, щоб до Кредитів МОЖНА було додавати звичайні числа?

Якщо у твоїй програмі бізнес-логіка вимагає, щоб до кредитів можна було додавати як інші кредити, так і звичайні числа int, ми можемо просто розширити твій if!
python
class Credits:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # Варіант А: Додаємо такий самий об'єкт Credits
        if isinstance(other, Credits):
            return Credits(self.value + other.value)
        
        # Варіант Б: Додаємо звичайне ціле число
        if isinstance(other, int):
            return Credits(self.value + other)
            
        # Для всього іншого (рядків, списків) — відмова
        return NotImplemented"""