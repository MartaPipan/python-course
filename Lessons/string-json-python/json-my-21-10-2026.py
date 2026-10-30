import json
import csv

class Student:
    def __init__(self, name, group, subject, marks):
        self.name = name
        self.group = group
        self.subject = subject
        self.marks = marks if isinstance(marks, list) else [marks]

    def to_dict(self):
        """Перетворює об'єкт студента на словник (dict)."""
        return {
            "name": self.name,
            "group": self.group,
            "subject": self.subject,
            "marks": self.marks
        }

    def to_json(self):
        """Перетворює конкретного студента на JSON-рядок."""
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)

    @classmethod
    def from_dict(cls, data):
        """Створює об'єкт Student зі словника (dict)."""
        return cls(
            name=data.get("name"),
            group=data.get("group"),
            subject=data.get("subject"),
            marks=data.get("marks", [])
        )

    @classmethod
    def from_json(cls, json_str):
        """Створює об'єкт Student із JSON-рядка."""
        data = json.loads(json_str)
        return cls.from_dict(data)


class StudentStorage:

    @staticmethod
    def save_json(students, filename):
        """Записує список об'єктів Student у faint JSON."""
        data = [student.to_dict() for student in students]
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_json(filename):
        """Зчитує дані з файлу JSON та повертає список об'єктів Student."""
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Student.from_dict(item) for item in data]

    @staticmethod
    def save_csv(students, filename):
        """Записує список об'єктів Student у файл CSV."""
        fields = ["name", "group", "subject", "marks"]
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dict())

    @staticmethod
    def load_csv(filename):
        """Зчитує дані з файлу CSV та повертає список об'єктів Student."""
        with open(filename, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            students = []
            for row in reader:
                try:
                    raw_marks = row.get("marks", "")
                    marks = json.loads(raw_marks.replace("'", '"')) if raw_marks else []
                except json.JSONDecodeError:
                    marks = []

                students.append(Student(
                    name=row["name"],
                    group=row["group"],
                    subject=row["subject"],
                    marks=marks
                ))
            return students


#  (Тестування програми) ---
if __name__ == "__main__":
    # 1. Створюємо початковий список студентів
    students = [
        Student("Pavlo", "4sc-21", "Python", [3, 4, 5]),
        Student("Ivan", "4sc-22", "Java", [3, 4, 5]),
        Student("Vasil", "4sc-23", "Python", [3, 4, 5])
    ]

    # 2. Тестуємо поодиноку серіалізацію в JSON-рядок
    json_string = students[0].to_json()
    print("Json string:\n", json_string)

    # 3. Тестуємо відновлення одного студента з JSON-рядка
    student_obj = Student.from_json(json_string)
    print("Restored student:", student_obj.name)

    # 4. Зберігаємо весь список у JSON та CSV файли
    StudentStorage.save_json(students, "students.json")
    StudentStorage.save_csv(students, "students.csv")

    # 5. Завантажуємо дані назад із файлу JSON
    students_from_json = StudentStorage.load_json("students.json")
    print("\nStudents from json:")

    for student in students_from_json:
        print(f" - {student.name} (Група: {student.group}, Предмет: {student.subject}, Оцінки: {student.marks})")
