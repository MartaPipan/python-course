# ==========================================
# 1. КЛАС ФАКУЛЬТЕТУ ТА ІНКАПСУЛЯЦІЯ
# ==========================================
class Faculty:
    def __init__(self, title):
        self.title = title
        self.__budget_places = 5  # Приватне поле: кількість бюджетних місць

    @property
    def budget_places(self):
        return self.__budget_places

    @budget_places.setter
    def budget_places(self, value):
        if value < 0:
            raise ValueError("Кількість місць не може бути від'ємною!")
        self.__budget_places = value

    def __repr__(self):
        return f"Faculty(title={self.title!r})"


# ==========================================
# 2. УСПАДКУВАННЯ ТА ПОЛІМОРФІЗМ УЧНІВ
# ==========================================
class Student:
    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty
        self.grades = {}  # Словник для оцінок: {"Математика":}

    # Додавання оцінки з перевіркою
    def add_grade(self, subject, score):
        if not 0 <= score <= 100:
            raise ValueError("Оцінка має бути від 0 до 100!")
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(score)

    # Поліморфний метод: розрахунок середнього бала
    def get_average_score(self):
        if not self.grades:
            return 0.0
        all_scores = [score for scores in self.grades.values() for score in scores]
        return round(sum(all_scores) / len(all_scores), 2)

    # Поліморфний метод для виведення статусу
    def get_status(self):
        return f"Студент {self.name} навчається на загальних умовах."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, faculty={self.faculty.title!r})"


# Успадкування: Студент-відмінник (Стипендіат)
class ScholarStudent(Student):
    # Поліморфізм: перевизначаємо статус
    def get_status(self):
        return f"🌟 Студент {self.name} отримує підвищену стипендію за успіхи!"


# Успадкування: Студент-іноземець
class InternationalStudent(Student):
    def __init__(self, name, faculty, country):
        super().__init__(name, faculty)  # Виклик конструктора батька
        self.country = country  # Унікальна властивість іноземця

    # Поліморфізм: перевизначаємо статус
    def get_status(self):
        return f"🌍 Студент {self.name} прибув на навчання з країни: {self.country}."


# ==========================================
# 3. КЛАС-КОНТЕЙНЕР ГРУПА ТА МАГІЧНІ МЕТОДИ
# ==========================================
class StudentGroup:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            print(f"  + {student.name} зараховано до групи {self.group_name}")

    # Магічний метод __len__ (Кількість учнів у групі)
    def __len__(self):
        return len(self.students)

    # Магічний метод __add__ (Об'єднання двох груп через знак +)
    def __add__(self, other):
        if isinstance(other, StudentGroup):
            merged_group = StudentGroup(f"{self.group_name}+{other.group_name}")
            merged_group.students = self.students + other.students
            return merged_group
        raise TypeError("Можна об'єднувати лише групу з групою!")

    def __repr__(self):
        return f"StudentGroup(name={self.group_name!r}, students_count={len(self)})"


# ==========================================
# 🎮 ДЕМОНСТРАЦІЯ РОБОТИ ПРОГРАМИ
# ==========================================
if __name__ == "__main__":
    print("--- 1. Створення Факультету (Інкапсуляція) ---")
    it_faculty = Faculty("Кібернетика")
    it_faculty.budget_places = 10  # Зміна через сеттер
    print(f"Факультет: {it_faculty.title}, Бюджетних місць: {it_faculty.budget_places}")

    print("\n--- 2. Створення Учнів (Класи, Об'єкти, Успадкування) ---")
    olena = Student("Олена", it_faculty)
    danylo = ScholarStudent("Данило", it_faculty)
    john = InternationalStudent("Джон", it_faculty, "Великобританія")

    print(olena)  # Викличе __repr__ -> Student(name='Олена', faculty='Кібернетика')
    print(danylo) # ScholarStudent(name='Данило', faculty='Кібернетика')
    print(john)   # InternationalStudent(name='Джон', faculty='Кібернетика')

    print("\n--- 3. Вивчення Дисциплін та Оцінки ---")
    # Олена вчить Програмування та Математику
    olena.add_grade("Програмування", 95)
    olena.add_grade("Програмування", 90)
    olena.add_grade("Математика", 85)

    # Данило вчить ті ж дисципліни
    danylo.add_grade("Програмування", 100)
    danylo.add_grade("Математика", 98)

    print(f"Середній бал Олени: {olena.get_average_score()}") # 90.0
    print(f"Середній бал Данила: {danylo.get_average_score()}") # 99.0

    print("\n--- 4. Демонстрація Поліморфізму (Різні статуси) ---")
    students = [olena, danylo, john]
    for s in students:
        print(s.get_status())

    print("\n--- 5. Робота з Групами (Магічні методи __len__ та __add__) ---")
    group_a = StudentGroup("КН-11")
    group_a.add_student(olena)
    group_a.add_student(danylo)

    group_b = StudentGroup("КН-12")
    group_b.add_student(john)

    # Перевірка __len__
    print(f"Кількість учнів у групі А: {len(group_a)}") # 2

    # Перевірка __add__ (Об'єднуємо КН-11 та КН-12 через звичайний плюс)
    combined_group = group_a + group_b
    print(combined_group) # StudentGroup(name='КН-11+КН-12', students_count=3)

"""
(Короткий чек-лист теми):

1. Інкапсуляція: Ми закрили кількість бюджетних місць __budget_places на замок від випадкового запису від'ємних чисел завдяки @property та @budget_places.setter.
2. Успадкування: Класи ScholarStudent та InternationalStudent перейняли від батька Student логіку роботи зі словником оцінок self.grades та метод add_grade(). При цьому Джон отримав додаткове власне поле self.country.
3. Поліморфізм: Метод get_status() викликається однаково для всіх, але кожний тип студента виводить у термінал свій унікальний текст.
4. Магічні методи: __len__ дозволив рахувати кількість студентів у групі стандартною функцією len(), а __add__ навчив Python об'єднувати два об'єкти груп через звичайний оператор +.
"""