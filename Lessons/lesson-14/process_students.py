import csv
from pathlib import Path

# ШУКАЄМО ФАЙЛ: використовуємо правильний шлях до файлу, який ми створили раніше
csv_path = Path.cwd() / "lessons" / "lesson-14" / "students_report.csv"

# Перевіряємо, чи файл взагалі існує за цим шляхом перед відкриттям
if not csv_path.exists():
    print(f"❌ Помилка: Файл не знайдено за шляхом {csv_path}")
    exit()

correct_students = []  # Список для зберігання перевірених і валідних даних

print("--- Початок обробки файлу CSV ---")

with csv_path.open("r", encoding="utf-8", newline="") as file:
    # 1. DictReader створює словники, де всі значення — рядки (наприклад, "84")
    reader = csv.DictReader(file)
    
    for row in reader:
        # 2. Перевіряємо, що ключ 'score' існує і рядок у файлі не порожній
        if "score" not in row or not row["score"].strip():
            print(f"⚠️ Пропущено: Рядок для {row.get('name')} не містить балу або порожній.")
            continue
            
        try:
            # 3. int("84") створює число 84 (перетворення типу)
            numeric_score = int(row["score"])
            
            # 4. Окрема предметна перевірка: чи лежить бал у межах від 0 до 100
            if 0 <= numeric_score <= 100:
                # Оновлюємо значення в словнику на вже чисте число
                row["score"] = numeric_score
                
                # 5. Лише після цього запис додається до списку коректних даних
                correct_students.append(row)
                print(f"✅ Успішно валідовано: {row['name']} (Бал: {row['score']})")
            else:
                print(f"❌ Відхилено логікою: Бал {numeric_score} студента {row['name']} поза межами 0-100!")
                
        except ValueError:
            print(f"⚠️ Помилка типу: Бал '{row['score']}' користувача {row['name']} не є числом!")

# Фінальний результат програми
print("\n--- ФІНАЛЬНИЙ СПИСОК КОРЕКТНИХ ДАНИХ ---")
print(correct_students)
