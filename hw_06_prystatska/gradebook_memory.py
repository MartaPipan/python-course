# Початкова база даних студентів
students_data = [
    {
        "id": ("AB-123", 1),
        "name": "Ann Smith",
        "group": "AB-123",
        "scores": [90, 85, 100, 90]  # Студент із повторюваною оцінкою (90)
    },
    {
        "id": ("AB-456", 2),
        "name": "Clara Sousa",
        "group": "AB-201",
        "scores": []  # Студент без оцінок
    },
    {
        "id": ("AB-202", 1),
        "name": "Ann Smith",  # Таке ж ім'я, але інша група та ID
        "group": "AB-202",
        "scores": [95, 88, 92]
    },
    {
        "id": ("AB-202", 2),
        "name": "Luis Bravo",
        "group": "AB-202",
        "scores": [75, 80]
    },
    {
        "id": ("AB-201", 3),
        "name": "Jorge Lopez",
        "group": "AB-201",
        "scores": [100, 100, 95]
    },
    {
        "id": ("AB-201", 4),
        "name": "Maria Bell",
        "group": "AB-201",
        "scores": [85, 90, 88]
    },
    {
        "id": ("AB-201", 5),
        "name": "Carl Ben",
        "group": "AB-201",
        "scores": [70, 75, 80]
    },
    {
        "id": ("AB-123", 2),
        "name": ("Brett Pit"),
        "group": "AB-123",
        "scores": [60, 65]
    },
    {
        "id": ("AB-123", 3),
        "name": "Diana Ross",
        "group": "AB-123",  
        "scores": [85, 70] # Перший дублікат (має 2 оцінки) - має залишитися
    },
    {
        "id": ("AB-123", 3),
        "name": "Diana Ross",
        "group": "AB-123",  
        "scores": [85]     # Другий дублікат (має 1 оцінку) - буде відфільтрований
    }
]

print("1. Початковий журнал студентів (порядок збережено)")
#1.  Цикл for проходить по кожному студенту та виводить його початкові дані
for student in students_data:  
    print(f"ID: {student['id']} | Ім'я: {student['name']} | Група: {student['group']} | Оцінки: {student['scores']}")



"""# Очищення через множину (якщо кількість оцінок не має значення) 
1. Створюємо порожню множину для відстеження ID, які ми вже бачили
seen_ids = set()
cleaned_students_data = []

# 2. Фільтруємо в один цикл
for student in students_data:
    if student["id"] not in seen_ids:
        cleaned_students_data.append(student)
        seen_ids.add(student["id"])  # Додаємо ID в множину за допомогою .add()

students_data = cleaned_students_data"""

#2. ВИЯВЛЕННЯ ТА ФІЛЬТРАЦІЯ ДУБЛІКАТІВ 

filtered_list = {}        # Словник для зберігання унікальних записів (ключ - ID)
duplicates_list = []      # Список для зберігання дублікатів

print("\nПеревірка наявності дублікатів і збереження варіанту з найбільшою кількістю оцінок")

for student in students_data:
    student_id = student["id"]
    
    # Перевіряємо за допомогою оператора 'in', чи цей ID вже зустрічався раніше
    if student_id in filtered_list:
        print(f"[УВАГА/ALARM] Знайдено дублікат ID {student_id}! Студент: {student['name']}")
        
        # Використовуємо len(), щоб порівняти кількість оцінок поточного студента та вже збереженого
        current_best = filtered_list[student_id]
        if len(student["scores"]) > len(current_best["scores"]):
            # Якщо у нового дубліката оцінок більше: старий відправляємо в дублікати за допомогою .append()
            duplicates_list.append(current_best)
            # Записуємо нового студента як найкращий варіант для цього ID
            filtered_list[student_id] = student
        else:
            # Якщо у старого варіанту оцінок більше або стільки же, новий студент відправляється в дублікати
            duplicates_list.append(student)
    else:
        # Якщо ID зустрічається вперше, просто додаємо його в наш словник
        filtered_list[student_id] = student



# Реконструкція списку для збереження оригінального порядку розташування студентів
#(Коли шукали дублікати+словник: filtered_list[student_id] = student. Словники не гарантують збереження черговості, яка була в початковому списку.)

cleaned_students_data = [] #новий порожній список, будемо додавати студентів (без дублікатів), які успішно пройшли перевірку.
checked_ids = set() # порожн множина (set) унікальних ID, будемо записувати ID тих студентів, яких уже занесли до чистого журналу, щоб не записати їх двічі.

for student in students_data:
    student_id = student["id"]
    if student_id in filtered_list and student_id not in checked_ids:   # Якщо цей студент є у списку filtered_list і його ID ще немає в checked_ids
        cleaned_students_data.append(filtered_list[student_id])
        checked_ids.add(student_id)    # Позначаємо ID як доданий за допомогою .add()
students_data = cleaned_students_data   # Оновлюємо оригінальну змінну очищеними даними


# пошук та створення множини груп вже з чистими даними
print("\n--- Створення пошукових структур на основі очищених даних ---")

# швидкий пошук за кортежем-ID
student_by_id = {student["id"]: student for student in students_data}
# Множина унікальних груп (автоматично видаляє дублікати назв груп)
groups_set = {student["group"] for student in students_data}

print(f"Кількість виявлених дублікатів: {len(duplicates_list)}")
print(f"Кількість студентів в журналі після очищення: {len(students_data)}")
print(f"Унікальні групи: {sorted(list(groups_set))}")#спочатку перетворює множину groups_set (яка не має порядку) на звичайний список list+ sorted

# 3. СЕРЕДНІЙ БАЛ ТА ПОШУК НАЙБІЛЬШОГО СЕРЕДНЬОГО БАЛУ
print("\n2. Середній бал кожного студента")
# Беремо першого студента зі списку [0]
first_student = students_data[0]
best_student = first_student["name"]

# Перевіряємо, чи є в нього оцінки, і обчислюємо стартовий max_avg
if first_student["scores"]:
    max_avg = sum(first_student["scores"]) / len(first_student["scores"])
else:
    max_avg = 0.0  # Якщо в першого студента немає оцінок, ставимо 0.0


# Запускаємо цикл зрізом [1:], щоб пропустити першого студента, 
# бо ми його вже взяли за основу і немає сенсу порівнювати його самого з собою
for student in students_data[1:]:
    scores = student["scores"]
    if scores:
        # Обчислення середнього балу через sum() та len()
        avg = sum(scores) / len(scores)
        print(f"Студент: {student['name']} (ID: {student['id']}) -> Середній бал: {avg:.2f}")
        
        # пошук максимального значення
        if avg > max_avg:
            max_avg = avg
            best_student = student["name"]
    else:
        # Обробка випадку, коли у студента немає оцінок (захист від ділення на нуль) # ТЕСТ: Студент без оцінок (Clara Sousa) обробляється тут
        print(f"Студент: {student['name']} (ID: {student['id']}) -> немає оцінок")

if best_student:
    print(f"\nНайбільший середній бал: {max_avg:.2f} (Студент: {best_student})")


"""# --- 4. КОПІЮВАННЯ ТА ЗМІНА ОРИГІНАЛУ (Поверхневе копія) ---
print("\n3. Перевірка ЗАЛЕЖНОСТІ копії оцінок (Зміна копії змінює оригінал)")

# Копіюємо тільки словники студентів
updated_students_data = [student.copy() for student in students_data]

# Вибираємо студента з НОВОГО списку
target_student_new = updated_students_data[0]

# Змінюємо дані у НОВОМУ списку (додаємо 99)
target_student_new["scores"].append(99)
print("\nДо оцінок студента у новому списку додано 99")

# Тепер обидва списки покажуть однакові зміни!
print(f"Оригінальні оцінки після зміни у новому списку: {target_student_new['scores']}")
print(f"Початковий список (students_data) ТЕЖ ЗМІНИВСЯ:   {students_data[0]['scores']}")

# Доказ
print(f"Чи змінився оригінал разом із копією? {'ТАК' if students_data[0]['scores'] == target_student_new['scores'] else 'НІ'}")"""



   # 4. КОПІЮВАННЯ ТА ЗМІНА ОРИГІНАЛУ    (Оригінальні оцінки після зміни у новому списку)
   #копія списку оцінок не залежить від оригіналу. Створюємо новий список студентів.

print("\n3. Перевірка незалежності копії оцінок та створення нового списку")

  # Створюємо повністю новий список студентів шляхом копіювання елементів(незмінність початкового списку students_data)
updated_students_data = [student.copy() for student in students_data]

# Робимо копію вкладених списків оцінок для кожного студента у новому списку
for student in updated_students_data:
    student["scores"] = student["scores"].copy()

  # Вибираємо цільового студента для тесту з НОВОГО списку (Ann Smith)
target_student_new = updated_students_data[0]

  # Робимо незалежну копію списку оцінок для перевірки
scores_copy = target_student_new["scores"].copy()

print(f"Оригінальні оцінки у новому списку до зміни: {target_student_new['scores']}")
print(f"Скопійовані оцінки до зміни: {scores_copy}")

  # Змінюємо дані лише у НОВОМУ списку студентів
target_student_new["scores"].append(99)
print("\n До оцінок студента у новому списку додано 99")

print(f"Оригінальні оцінки після зміни у новому списку: {target_student_new['scores']}")
print(f"Початковий список (students_data) без змін:     {students_data[0]['scores']}")
print(f"Скопійовані оцінки після зміни:                 {scores_copy}")
print(f"Доказ: Чи залишилася копія оцінок незмінною? {'ТАК' if scores_copy != target_student_new['scores'] else 'НІ'}")

  # результат:
  # До оцінок студента у новому списку додано 99
  #Оригінальні оцінки після зміни у новому списку: [90, 85, 100, 90, 99]
  #Початковий список (students_data) без змін:     [90, 85, 100, 90]
  #Скопійовані оцінки після зміни:                 [90, 85, 100, 90]
  #Доказ: Чи залишилася копія оцінок незмінною? ТАК"""


# 5. ТЕСТИ ТА ПЕРЕВІРКИ
# Пошук за відомим та невідомим ID через get()

print("\n4. Тести та перевірки")

# Перевірка: відомий ID за допомогою методу .get()
known_id = ("AB-202", 1)
found_student = student_by_id.get(known_id)
print(f"Пошук ID {known_id}: {found_student['name'] if found_student else 'Не знайдено (невідомий ID)'}")

# Перевірка: невідомий ID (поверне None замість помилки)
unknown_id = ("AB-202", 19)
failed_student = student_by_id.get(unknown_id)
print(f"Пошук ID {unknown_id}: {failed_student['name'] if failed_student else 'Не знайдено (невідомий ID)'}")

# ТЕСТ: Однакове ім'я в різних групах (Ann Smith)
print("\n-> Перевірка: Однакове ім'я в різних групах")
ann_1 = student_by_id.get(("AB-123", 1))
ann_2 = student_by_id.get(("AB-202", 1))
print(f"   Знайдено першу {ann_1['name']} у групі {ann_1['group']} за ID ('AB-123', 1)")
print(f"   Знайдено другу {ann_2['name']} у групі {ann_2['group']} за ID ('AB-202', 1)")

# Виведення фінального списку всіх груп, відсортованих за алфавітом через sorted()
print(f"\nВідсортовані групи: {sorted(list(groups_set))}")

