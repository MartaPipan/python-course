import json
import csv

class Student:
    def __init__(self, name, group, subject, marks):
        self.name = name
        self.group = group
        self.subject = subject
        # Відразу конвертуємо в int, якщо це рядок (наприклад, "4" -> 4)
        self.marks = int(marks) 

      ##"перетворює обєкт студента на словник dict"
    def to_dict(self):
        return {
            "name": self.name,
            "group": self.group,
            "subject": self.subject,
            "marks": self.marks
        }
    ##def to_json(self):
         ##"перетворює конктетного студента на рядок"
         ##return json.dumps(self.to_dict(),ident=4)
    
        
    @classmethod
    def from_dict(cls, data):
        ##створює обєкт студента зі словника dict
        # Тепер тут не потрібно викликати int(), бо це зробить конструктор
        return cls(data["name"], data["group"], data["subject"], data["marks"])
    
    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return cls.from_dict(data)

    def __str__(self):
        return f"{self.name}, {self.group}, {self.subject}, {self.marks}"

class StudentStorage:
    @staticmethod
    def save_json(students, filename):
        data = [student.to_dict() for student in students]
        with open(filename, "w", encoding="utf-8") as file:
            # ДОДАНО ensure_ascii=False, щоб кирилиця у файлі зберігалася красиво
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_json(filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Student.from_dict(item) for item in data]

    @staticmethod
    def save_csv(students, filename):
        fields = ["name", "group", "subject", "marks"]
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dict())

    @staticmethod
    def load_csv(filename):
        with open(filename, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            return [Student.from_dict(row) for row in reader]

# Тестування програми
students = [
    Student("Павло", "4sc-21", "Python", "3"),
    Student("Іван", "4sc-22", "Java", "4"),
    Student("Василь", "4sc-23", "Python", "5")
]

json_string = students[0].to_json()
print("Json string:", json_string)

student = Student.from_json(json_string)
print("Restored student:", student.name)

# Збереження у файли
StudentStorage.save_json(students, "students.json")
StudentStorage.save_csv(students, "students.csv")

# Завантаження з JSON
students_from_json = StudentStorage.load_json("students.json")
print("\nStudents from json:")
for student in students_from_json:
    print(student)

# Завантаження з CSV
students_from_csv = StudentStorage.load_csv("students.csv")
print("\nStudents from csv:")
for student in students_from_csv:
    print(student)
