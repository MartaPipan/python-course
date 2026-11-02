class Course:
    def __init__(self, title):
        # Перед створенням курсу, можемо скористатися нашим статичним методом для валідації
        if not self.validate_title(title):
            raise ValueError("Назва курсу занадто коротка!")
        self.title = title
        self.students = []  # Список для збереження студентів

    # Звичайний метод (потребує self), бо додає студента до конкретного курсу
    def enroll(self, student):
        self.students.append(student)
        print(f"  + Студента {student} успішно зараховано на курс '{self.title}'")

    # СТАТИЧНИЙ МЕТОД: йому байдуже до конкретного об'єкта або списку студентів.
    # Він просто виконує допоміжну функцію перевірки тексту.
    @staticmethod
    def validate_title(title):
        return len(title.strip()) >= 3


# ==========================================
# 🎮 ДЕМОНСТРАЦІЯ РОБОТИ
# ==========================================
if __name__ == "__main__":
    # 1. Виклик статичного методу НАПРЯМУ через Клас без створення об'єктів
    is_valid = Course.validate_title("Python для початківців")
    print(f"Чи коректна назва курсу? -> {is_valid}")  # Виведе: True

    print("\n--- Створення курсу та зарахування студентів ---")
    # 2. Створюємо об'єкт курсу
    python_course = Course("Python")
    
    # 3. Зараховуємо студентів через звичайний метод
    python_course.enroll("Олена")
    python_course.enroll("Данило")

    print(f"Усього студентів на курсі: {len(python_course.students)}")  # Виведе: 2
