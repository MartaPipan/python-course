class Student:
    def __init__(self, name: str, group: str):
        self.name = name
        self.group = group
        self.scores = []  # ІНДИВІДУАЛЬНИЙ список для кожного об'єкта

    def add_score(self, score: int):
        if not 0 <= score <= 100:
            raise ValueError("Оцінка має бути від 0 до 100")
        self.scores.append(score)

    def __repr__(self):
        return f"Student(name={self.name!r}, group={self.group!r}, scores={self.scores})"


# ==========================================
# 🎮 ДЕМОНСТРАЦІЯ ТА ДОВЕДЕННЯ НЕЗАЛЕЖНОСТІ
# ==========================================
if __name__ == "__main__":
    print("--- 1. Створюємо двох незалежних студентів ---")
    olena = Student("Олена", "КН-11")
    danylo = Student("Данило", "КН-11")

    print(f"Початковий стан Олени: {olena}")
    print(f"Початковий стан Данила: {danylo}")

    print("\n--- 2. Додаємо оцінку ТІЛЬКИ Олені ---")
    olena.add_score(95)
    olena.add_score(88)

    print("\n--- 3. Фінальна перевірка списків оцінок ---")
    print(f"Оцінки Олени : {olena.scores} -> (Має 2 оцінки)")
    print(f"Оцінки Данила: {danylo.scores} -> (Залишився порожнім!)")

    # Перевірка через порівняння id об'єктів у пам'яті комп'ютера
    print("\n--- 4. Доказ на рівні пам'яті комп'ютера (id списків) ---")
    print(f"Адреса списку Олени : {id(olena.scores)}")
    print(f"Адреса списку Данила: {id(danylo.scores)}")
    
    if id(olena.scores) != id(danylo.scores):
        print("\n✅ ДОВЕДЕНО: Списки оцінок мають різні адреси в пам'яті. Вони повністю НЕЗАЛЕЖНІ!")
    else:
        print("\n❌ ПОМИЛКА: Списки ділять одну адресу (пастка атрибута класу).")
