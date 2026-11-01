import csv
from pathlib import Path

# 1. Шлях до оригінального файлу (він лежить прямо в корені)
FILE_PATH = Path.cwd() / "hw_09_prystatska" / "data" / "attendance.csv"

# 2. Шлях для збереження чистого файлу в папку lesson-15
OUTPUT_PATH = Path.cwd() / "lessons" / "lesson-15" / "cleaned_attendance.csv"

# 2. Новий шлях для чистих даних (збережеться в ту саму папку 'data')
#    OUTPUT_PATH = FILE_PATH.parent / "cleaned_attendance.csv"

REQUIRED_HEADERS = ["name", "attended", "total"]
issues_list = []
valid_rows_to_save = []  # Список, куди ми будемо збирати чисті рядки

print(f"Шукаю файл за шляхом: {FILE_PATH.resolve()}\n")

if not FILE_PATH.exists():
    print(f" Помилка: Не вдалося знайти файл за шляхом: {FILE_PATH}")
    exit()

# ЧИТАННЯ ТА ОБРОБКА ДАНИХ
try:
    with FILE_PATH.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        
        if not reader.fieldnames:
            print(" Помилка: Файл порожній або не має заголовків!")
            exit()

        print("файл запущено за допомогою команди: python lessons/lesson-15/process_attendance_09.py")
        print(" Файл успішно відкрито. Починаю обробку даних...\n")
        
        for index, row in enumerate(reader, start=1):
            if not any(row.get(key, "").strip() for key in REQUIRED_HEADERS if row.get(key)):
                continue
                
            name = row.get("name", "").strip()
            raw_attended = row.get("attended", "").strip()
            raw_total = row.get("total", "").strip()
            
            if not name:
                issues_list.append(f"Рядок {index}: Помилка -> Ім'я студента порожнє")
                continue
            try:
                attended = int(raw_attended)
                total = sum(int(part.strip()) for part in raw_total.split(",") if part.strip())

                
                if total == 0:
                    raise ZeroDivisionError
                
                # [НОВИЙ ЗАХИСТ]: Перевіряємо, чи відвідані заняття не перевищують загальну кількість
                if attended > total:
                    issues_list.append(
                        f"Рядок {index} ({name}): Помилка -> Відвідано ({attended}) "
                        f"більше, ніж усього занять ({total})"
                    )
                    continue  # Пропускаємо цього студента, не зберігаємо в чистий файл
                    
                percentage = (attended / total) * 100
                print(f"Студент: {name} | Відвідуваність: {percentage:.1f}%")
                
                # Зберігаємо лише правильні дані
                valid_rows_to_save.append({
                    "name": name,
                    "attended": attended,
                    "total": total,
                    "percentage_%": round(percentage, 1)
                })
                
            except ValueError:
                issues_list.append(f"Рядок {index} ({name}): Помилка -> Некоректні цифри ('{raw_attended}' або '{raw_total}')")
                
            except ZeroDivisionError:
                issues_list.append(f"Рядок {index} ({name}): Помилка -> Кількість занять = 0")

except Exception as e:
    print(f" Сталася непередбачувана помилка при читанні: {e}")
    exit()

# [НОВЕ] ЗАПИС ЧИСТИХ ДАНИХ У НОВИЙ ФАЙЛ
if valid_rows_to_save:
    try:
        # Переконуємося, що папка для збереження існує (якщо раптом її видалили)
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        
        # Визначаємо нові заголовки для фінального файлу
        output_headers = ["name", "attended", "total", "percentage_%"]
        
        # Відкриваємо новий файл для запису ('w' - write)
        with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as out_file:
            writer = csv.DictWriter(out_file, fieldnames=output_headers)
            
            # Записуємо рядок із заголовками колонок
            writer.writeheader()
            # Записуємо всі зібрані чисті рядки
            writer.writerows(valid_rows_to_save)
            
        print(f"\n💾 Успішно збережено {len(valid_rows_to_save)} студентів у файл: {OUTPUT_PATH.name}")
        
    except Exception as e:
        print(f" Помилка при збереженні файлу: {e}")
else:
    print("\nНовий файл не було створено, оскільки немає жодного валідного рядка даних.")

# ВИВІД ЗВІТУ ПРО ПОМИЛКИ
print("\n--- ЗВІТ ПРО ПРОБЛЕМИ В ТАБЛИЦІ ---")
if issues_list:
    for issue in issues_list:
        print(issue)
else:
    print("Усі дані оброблено успішно, помилок не знайдено!")