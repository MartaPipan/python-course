import csv
import sys
from pathlib import Path

folder_hw_08_prystatska_path = Path.cwd() / "hw_08_prystatska"
sys.path.append(str(folder_hw_08_prystatska_path))
from study_tools.calculations import mean


csv_path = Path.cwd() / "hw_09_prystatska" / "data" / "attendance.csv"
if not csv_path.exists():
    print(f"Файл не знайдено за шляхом {csv_path}")
    exit()


total_filled_rows = 0  
valid_records_count = 0  
parsed_with_csv = []  # список для збереження результатів


print("Розрахунок середнього балу для кожного студента)")

with csv_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_filled_rows += 1
        
        name = row.get("name", "")
        group = row.get("group", "")
        attended = row.get("attended", "")
        total_raw = row.get("total", "")
        
        if not any([name.strip(), group.strip(), attended.strip(), total_raw.strip()]):
            print(f"Рядок {total_filled_rows}: Рядок порожній (пропущено)")
            continue
            
        student_name = name.strip() if name else "Невказане ім'я"
        
        if not total_raw.strip():
            print(f" Рядок {total_filled_rows}: Немає балів для студента {student_name}")
            continue
            
        student_scores = []
        for part in total_raw.split(","):
            part = part.strip()
            if part.isdigit():  # лише додатні числа
                student_scores.append(int(part))
        
        # текст "сімдесять"
        if not student_scores:
            print(f"Рядок {total_filled_rows}: Бали студента {student_name} '{total_raw.strip()}' не містять чисел")
            continue
            
         # Розрахунок бала
        student_average = mean(*student_scores)
        
        if student_average is not None:
            valid_records_count += 1
            
            # додати бал у словник
            row["average"] = round(student_average, 2)
            parsed_with_csv.append(row)  #збереження валід. рядка у список
            
            print(f"Рядок {total_filled_rows} | {student_name} ({group.strip() or 'Без групи'}) "
                  f"Бали: {student_scores} | Середнє: {student_average:.2f}")

print(f"\nЗагальна кількість рядків: {total_filled_rows}")
print(f"Кількість валідних записів: {valid_records_count}")
print(f"Результат модуля csv: {parsed_with_csv}")
print(f"Довжина списку: {len(parsed_with_csv)}")
print(f"Запуск Python-скрипта за командою у терміналі: 'python ./hw_09_prystatska/check_students_with_hw_08.py'")







