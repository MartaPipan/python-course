import csv
from pathlib import Path

# шлях відносно робочої папки
root_dir = Path.cwd() / "hw_09_prystatska"
input_path = root_dir / "data" / "attendance.csv"
output_dir = root_dir / "output"
summary_csv_path = output_dir / "attendance_summary.csv"
issues_text_path = output_dir / "issues.txt"

# Ств. output 
output_dir.mkdir(parents=True, exist_ok=True)

if not input_path.exists():
    print(f"Не існує файл за шляхом {input_path}")
    exit()

REQUIRED_HEADERS = ["name", "group", "attended", "total"]
valid_data = []
valid_sum = 0
issues_list = []

print("Bалідація:")
with input_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    
    # заголовки
    if not reader.fieldnames or not all(h in reader.fieldnames for h in REQUIRED_HEADERS):
        print("Помилка: У файлі відсутні заголовки таблиці!")
        exit()

    for row in reader:
        # Пропускає порожні рядки
        if not any(row[key].strip() for key in REQUIRED_HEADERS if row[key]):
            continue
   
        name = row["name"].strip() if row["name"] else ""
        group = row["group"].strip() if row["group"] else ""
        raw_attended = row["attended"].strip() if row["attended"] else ""
        raw_total = row["total"].strip() if row["total"] else ""
        
        if not name:
            issues_list.append("Помилка: Ім'я студента порожнє")
            continue

        # ВАЛІДАЦІЯ 
         # Перевірка студента
        allowed_symbols = " ,'-"  
        is_name_valid = True
        
        for char in name:
            if not (char.isalpha() or char in allowed_symbols):
                is_name_valid = False
                break 
        if not is_name_valid:
            issues_list.append(f"Некоректне ім'я (містить цифри або заборонені знаки): '{name}'")
            continue

        # Перевірка attended (з рядка в число)
        if not raw_attended.isdigit():
            issues_list.append(f"Не є числом або порожні дані 'attended' для '{name}': '{raw_attended}'")
            continue
        attended = int(raw_attended)

        # для Мар'яна - помилка "сімдесять"
        total_parts = [part.strip() for part in raw_total.split(",") if part.strip()]
        
        if not total_parts or not all(part.isdigit() for part in total_parts):
            issues_list.append(f"Некоректний формат 'total' для '{name}': '{raw_total}'")
            continue
            
        total = sum(int(part) for part in total_parts)

        # ділення на нуль i attended > total
        if total == 0:
            issues_list.append(f"Помилка 'total' == 0 для студента '{name}'")
            continue
            
        if attended > total:
            issues_list.append(f"Помилка 'attended' > total для студента '{name}' (attended={attended}, total={total})")
            continue

    
        # Вимога: 2 букви, дефіс, 2 цифри
        is_group_valid = True
        if len(group) != 5 or group[2] != "-":
            is_group_valid = False
        else:
            letters_part = group[0:2]  
            digits_part = group[3:5]   
            if not letters_part.isalpha() or not digits_part.isdigit():
                is_group_valid = False

        if not is_group_valid:
            issues_list.append(f"Некоректна група для '{name}': '{group}'")
            continue

        # Результат
        percent = round((attended / total) * 100, 1)
        status = "достатньо" if percent >= 75.0 else "потрібно надолужити"

        valid_data.append({
            "name": name,
            "group": group,
            "percent": percent,
            "status": status
        })
        valid_sum += 1
        print(f"  + Успішно додано: {name} з відсотком {percent}%")

# Запис issue_file
with issues_text_path.open("w", encoding="utf-8") as issue_file:
    for issue in issues_list:
        issue_file.write(issue + "\n")

with summary_csv_path.open("w", encoding="utf-8", newline="") as file: 
    writer = csv.DictWriter(file, fieldnames=["name", "group", "percent", "status"])
    writer.writeheader()
    writer.writerows(valid_data)

print(f"\nРезультати записано.")
print(f"Згенеровано успішних звітів: {valid_sum}. Знайдено помилок: {len(issues_list)}.")

# Повторно читає створений CSV і перевіряє кількість записів 
print("\n Повторне перевірочне читання створеного CSV")
verified_count = 0
with summary_csv_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        verified_count += 1
        print(f"Перевірено: {row['name']} | Група: {row['group']} | Відсоток: {row['percent']}% | Статус: {row['status']}")

print(f"\nКількість успішних записів: {valid_sum}")
print(f"Кількість фактичних записів: {verified_count}")

# Перевірка твердження (assert)
assert valid_sum == verified_count, "Кількість записів не збігається!"
