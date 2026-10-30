from math import sqrt
print(sqrt(81))  
# • dir(math) — повертає список усіх доступних атрибутів...
# • help(math.sqrt) — виводить офіційну документацію...

# Стандартна бібліотека Python — це набір модулів, які вже вбудовані в Python за замовчуванням 
# (наприклад, math, csv, json, sys, os). Їх не потрібно встановлювати через pip.



# csv
# • dir(csv) — покаже всі доступні інструменти модуля...
# • help(csv.reader) — виведе документацію про те...

import csv

# Дані, які ми хочемо зберегти
data = [
    ["Ім'я", "Професія", "Місто"],
    ["Олександр", "Розробник", "Київ"],
    ["Марія", "Дизайнер", "Львів"]
]

# Відкриваємо файл для запису ('w' - write)
with open("users.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Записує всі рядки разом

# Відкриваємо файл для читання ('r' - read)
with open("users.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# додано print(), щоб список атрибутів з'явився в терміналі
print(dir(csv))

import csv

print("--- Читання через DictReader ---")

# Відкриваємо той самий файл users.csv
with open("users.csv", mode="r", encoding="utf-8") as file:
    # Використовуємо DictReader замість звичайного reader
    reader = csv.DictReader(file)
    
    for row in reader:
        # Тепер row — це словник!
        print(row)
        # Ми можемо звертатися до конкретних колонок за їхніми назвами:
        print(f"Користувач {row['Ім\'я']} працює як {row['Професія']}.")
