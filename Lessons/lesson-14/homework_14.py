import csv
import re
from pathlib import Path

# Визначаємо робочу папку для завдань цієї теми
work_dir = Path.cwd() / "lessons" / "lesson-14"   # 1. Define o caminho exato para a pasta lesson-14
work_dir.mkdir(parents=True, exist_ok=True)       # 2. Garante que a pasta existe (se não existir, o Python cria-a agora)


print(" ЗАВДАННЯ 1: Запис і читання нумерованих нотаток")
notes_path = work_dir / "notes.txt"
notes_to_write = [
    "Вивчити роботу з модулем pathlib.",
    "Розібратися з валідацією числових полів у CSV.",
    "Завжди використовувати newline='' при записі таблиць.",
]

# Записуємо нотатки у файл (кожна з нового рядка)
with notes_path.open("w", encoding="utf-8") as file:
    for note in notes_to_write:
        file.write(note + "\n")

# Читаємо файл і виводимо з нумерацією
with notes_path.open("r", encoding="utf-8") as file:
    for index, line in enumerate(file, start=1):
        # strip() прибирає зайвий символ переносу рядка \n при виведенні
        print(f"{index}. {line.strip()}")


print("\n ЗАВДАННЯ 2: Підрахунок слів за правилом")
text_path = work_dir / "sample_text.txt"
sample_text = "Python — це чудова мова! Вона проста, елегантна та потужна."

with text_path.open("w", encoding="utf-8") as file:
    file.write(sample_text)

with text_path.open("r", encoding="utf-8") as file:
    content = file.read()

# Явно визначаємо правило поділу: слово — це послідовність букв або цифр.
# Використовуємо регулярні вирази \w+ (літери, цифри, підкреслення), ігноруючи розділові знаки та тире.
words = re.findall(r"\w+", content)

print(f"Текст: '{content}'")
print(f"Список знайдених слів: {words}")
print(f" Загальна кількість слів у файлі: {len(words)}")


print("\n=== ЗАВДАННЯ 3: Читання CSV, середній бал та пропуск порожніх оцінок")
# Створимо тестовий файл оцінок, де є порожні значення та пробіли
marks_path = work_dir / "marks.csv"
with marks_path.open("w", encoding="utf-8", newline="") as file:
    file.write("name,score\nАндрій,90\nОксана, \nІгор,80\nСвітлана,\n")

total_score = 0
valid_count = 0

with marks_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Перевіряємо правило 2 підручника: наявність ключа та порожнечу рядка
        if "score" not in row or not row["score"].strip():
            print(f" Повідомлення: Пропущено студента {row['name']}, оскільки оцінка порожня.")
            continue
        
        try:
            # Перетворення типу та підрахунок
            score_value = int(row["score"])
            total_score += score_value
            valid_count += 1
        except ValueError:
            print(f" Помилка: Некоректний формат оцінки у {row['name']}.")

if valid_count > 0:
    average = total_score / valid_count
    print(f" Середній бал (серед {valid_count} успішних студентів): {average:.2f}")
else:
    print(" Немає коректних оцінок для обчислення середнього балу.")


print("\n ЗАВДАННЯ 4: Запис через DictWriter та порівняння кількості")
users_data = [
    {"username": "dev_alex", "role": "admin"},
    {"username": "user_olena", "role": "user"},
    {"username": "test_mark", "role": "guest"},
]
users_csv_path = work_dir / "users.csv"

# 1. Записуємо за допомогою DictWriter
with users_csv_path.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["username", "role"])
    writer.writeheader()
    writer.writerows(users_data)

# 2. Знову читаємо для перевірки відповідності вимогам
read_records_count = 0
with users_csv_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        read_records_count += 1

# 3. Порівнюємо початкову кількість рядків і прочитану
original_count = len(users_data)
print(f"Початкова кількість записів для запису: {original_count}")
print(f"Прочитана кількість записів із файлу: {read_records_count}")

# Стверджуємо (assert) правильність структури
assert original_count == read_records_count, " Помилка: Кількість записів не збігається!"
print(" Кількість записів повністю збігається, структура валідна.")


print("\nЗАВДАННЯ 5: CSV-рядок, який ламає split(',')")
# Класичний приклад рядка з комою всередині значення, взятого в лапки
broken_csv_line = '14,\"Марко, молодший\",КН-12,76'

print(f"Оригінальний рядок таблиці: {broken_csv_line}")

# Спроба поділити через звичайний split(',')
split_result = broken_csv_line.split(",")
print(f" Результат split(','): {split_result} (Довжина списку: {len(split_result)})")
print("   Чому зламався: Ім'я розірвалося на два елементи '\"Марко' та ' молодший\"'. Структура полів порушена.")

# Як цей самий рядок правильно прочитає вбудований модуль csv
parsed_with_csv = list(csv.reader([broken_csv_line]))[0]
print(f" Результат модуля csv: {parsed_with_csv} (Довжина списку: {len(parsed_with_csv)})")
print("   Чому працює: Модуль csv знає правила цитування та ігнорує кому всередині лапок.")
