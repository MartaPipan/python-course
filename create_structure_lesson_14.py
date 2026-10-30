import csv
from pathlib import Path

# 1. Шлях до нової папки: корінь / lessons / lesson-14
lesson_dir = Path.cwd() / "lessons" / "lesson-14"

# 2. Створюємо всю структуру папок автоматично
# parents=True дозволяє створити і lessons, і lesson-14 за один раз
lesson_dir.mkdir(parents=True, exist_ok=True)

# 3. Визначаємо шлях до CSV-файлу, який хочемо там створити
csv_path = lesson_dir / "students_report.csv"

# Дані для запису
data_to_save = [
    {"name": "Олена", "group": "КН-11", "score": 84},
    {"name": "Марко", "group": "КН-12", "score": 76},
]

# 4. Записуємо файл безпосередньо у нову папку
with csv_path.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "group", "score"])
    writer.writeheader()
    writer.writerows(data_to_save)

print(f" Папку створено за шляхом: {lesson_dir}")
print(f" Файл успішно записано сюди: {csv_path}")

print("\n--- Читання файлу CSV ---")        
with csv_path.open(encoding="utf-8", newline="") as file:     # Відкриваємо файл у режимі читання (за замовчуванням "r")
    reader = csv.DictReader(file)                             # Створюємо DictReader, який автоматично візьме заголовки ["name", "group", "score"]
   
    for row in reader:                                 # Перебираємо рядки таблиці
        row["score"] = int(row["score"])                                                     # Перетворюємо текст балу на ціле число
        print(f"Студент: {row['name']}, Група: {row['group']}, Бал: {row['score']}")         # Виводимо кожен рядок у термінал

