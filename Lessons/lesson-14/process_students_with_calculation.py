import csv
import sys
from pathlib import Path

# 1. ДОДАЄМО ШЛЯХ ДО ПАПКИ '8', щоб Python міг знайти calculations.py
# (Оскільки папка '8' лежить в корені, ми додаємо її до шляхів пошуку)
folder_hw_08_prystatska_path = Path.cwd() / "hw_08_prystatska"
sys.path.append(str(folder_hw_08_prystatska_path))

# Імпортуємо функції з папки study_tools, яка лежить в hw_08_prystatska
from study_tools.calculations import clamp, mean

# Шлях до вашого CSV-файлу
csv_path = Path.cwd() / "lessons" / "lesson-14" / "students_report.csv"

if not csv_path.exists():
    print(f"❌ Помилка: Файл не знайдено за шляхом {csv_path}")
    exit()

correct_students = []
scores_for_average = []  # Список, куди ми будемо збирати бали для середнього

print("--- Початок обробки файлу CSV з функціями clamp та mean ---")

with csv_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Перевірка на наявність та порожнечу рядка
        if "score" not in row or not row["score"].strip():
            print(f"⚠️ Пропущено: Немає балу для {row.get('name')}")
            continue
            
        try:
            raw_score = int(row["score"])
            
            # ВИКОРИСТОВУЄМО ТВОЮ ФУНКЦІЮ CLAMP
            # Вона автоматично перевірить межі 0-100. 
            # Якщо бал буде 105, вона поверне 100. Якщо -5, вона поверне 0.
            final_score = clamp(raw_score, lower=0, upper=100)
            
            if final_score is not None:
                row["score"] = final_score
                correct_students.append(row)
                scores_for_average.append(final_score)  # додаємо бал для статистики
                
                print(f"✅ Оброблено: {row['name']} -> Оригінальний бал: {raw_score}, "
                      f"Після clamp: {final_score}")
                
        except ValueError:
            print(f"⚠️ Помилка типу: Бал '{row['score']}' не є числом!")

# 2. ВИКОРИСТОВУЄМО ТВОЮ ФУНКЦІЮ MEAN
# Передаємо всі зібрані бали як окремі аргументи за допомогою зірочки (*)
average_score = mean(*scores_for_average)

print("\n--- ФІНАЛЬНИЙ СПИСОК ---")
print(correct_students)

print("\n--- СТАТИСТИКА ПРОЕКТУ ---")
if average_score is not None:
    print(f"📊 Середній бал усіх валідних студентів: {average_score:.2f}")
else:
    print("📊 Не вдалося порахувати середній бал (список порожній).")
