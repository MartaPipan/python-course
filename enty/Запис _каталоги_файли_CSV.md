• os (Operating System) — це інструмент для роботи зовні програми (ваш жорсткий диск, папки, файли, вікна).
• sys (System) — це інструмент для роботи всередині самої системи Python (налаштування інтерпретатора, пам'ять, аргументи запуску коду).


# основні команди для роботи з каталогами, файлами, CSV

 Команда	Що вона робить	Приклад використання
cd ..	Повертає на один рівень назад (у батьківську папку)	cd ..
cd назва_папки	Заходить всередину вказаної папки	cd hw_08_prystatska
cd ..\..	Повертає на два рівні назад	cd ..\..
pwd або ls	pwd показує, де ви стоїте. ls виводить список файлів у папці	ls


## 2. Робота з каталогами в Python (pathlib)

Перед використанням завжди пишемо: from pathlib import Path
• Path.cwd() — повертає шлях до поточної робочої папки терміналу.
• Path(__file__).parent — повертає шлях до папки, де лежить сам файл скрипта (найнадійніший спосіб шукати сусідні файли).
• шлях.mkdir(parents=True, exist_ok=True) — створює папку.
	• parents=True дозволяє створити дерево папок (наприклад, Lessons/lesson-14).
	• exist_ok=True захищає від помилки, якщо папка вже існує.
• шлях.iterdir() — перебирає всі елементи всередині папки.
• шлях.glob("*.csv") — шукає файли за маскою тільки в цій папці.
• шлях.rglob("*.csv") — шукає файли за маскою в цій папці та в усіх її підпапках (рекурсивно).
• елемент.is_file() / елемент.is_dir() — перевіряє, чи це файл, чи папка.

## 3. Робота з файлами в Python (Текст та лог-файли)

Для безпечного відкриття файлів використовується конструкція with, яка сама закриває файл після завершення роботи:
• Читання всього файлу:python
with шлях.open("r", encoding="utf-8") as file:
    content = file.read()

• Запис у файл (перезапис вмісту):python
with шлях.open("w", encoding="utf-8") as file:
    file.write("Новий текст")


## 4. Робота з таблицями в Python (csv)
Для роботи зі складними структурами та словниками завжди використовуйте класи DictReader та DictWriter.
• Правильне читання CSV (у форматі словників):python
import csv

with csv_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)            # Бере ключі із заголовка таблиці
    for row in reader:
        print(row["name"])                   # Доступ до колонки за її назвою


(Пам'ятайте: row["score"] спочатку зчитається як рядок "84", його треба перетворити за допомогою int()).

# 1. Зчитуємо (отримуємо рядок "84")
raw_score = row["score"]  

# 2. Перетворюємо (отримуємо число 84)
row["score"] = int(raw_score)  

# 3. Перевіряємо (валідуємо за правилами бізнес-логіки)
if 0 <= row["score"] <= 100:
    print("Бал коректний")



• Правильний запис у CSV:python
import csv

дані = [{"name": "Олена", "score": 84}]

with csv_path.open("w", encoding="utf-8", newline="") as file:      # fieldnames обов'язково має збігатися з ключами у словниках
    writer = csv.DictWriter(file, fieldnames=["name", "score"])

    writer.writeheader()          # Записує перший рядок-заголовок (name, score)
    writer.writerows(дані)        # Записує весь список словників

Параметр newline="" захищає від появи порожніх рядків у файлі на Windows.  -->




## Блок 1. Робота з папками та пошук файлів (pathlib)

Головна ідея: Для переміщення по папках і пошуку файлів у Python використовують модуль pathlib. 
Він дозволяє не просто дивитися вміст однієї папки, а й шукати файли «вглиб» (рекурсивно).
Приклад: Пошук усіх звітів у проекті
Уявіть, що у вашій папці з проектом є багато підпапок, і вам потрібно знайти всі файли налаштувань .json.

python
from pathlib import Path

                                                 
base_dir = Path("data")     # Визначаємо шлях до папки з даними
print("--- Пошук за допомогою rglob (lob заглядає в саму папку data та в усі її підпапки) ---")
for file_path in base_dir.rglob("*.json"):
    print(f"Знайдено файл: {file_path.name} за шляхом: {file_path}")


Пояснення до прикладу:
• Якщо ви викориstate метод glob("*.json"), Python подивиться тільки всередині папки data. 
Якщо там є підпапка data/2026/, файли всередині неї будуть пропущені.

• Метод rglob("*.json") діє як рентген: він проходить крізь усі рівні вкладеності 
(наприклад, знайде і data/settings.json, і data/archive/users/old_settings.json).


## Блок 2. Безпечне та правильне читання CSV (DictReader)
Головна ідея: Файли CSV — це таблиці. 
Якщо всередині тексту є коми (наприклад, адреса або ім'я "Марко, молодший"), звичайний метод .split(",") розірве це ім'я навпіл 
і зіпсує таблицю. Модуль csv вміє це обходити. 
Крім того, під час читання всі дані є текстом, тому перетворення типів і перевірку логіки потрібно робити окремо.

Приклад: Читання та валідація користувачів
Припустимо, у нас є файл users.csv із вмістом:

csv

name,score
"Марко, молодший",76
Анна,150



python

import csv
from pathlib import Path
file_path = Path("data") / "users.csv"


# Відкриваємо файл (newline="" обов'язково для CSV)
with file_path.open(encoding="utf-8", newline="") as file:
    # DictReader автоматично робить з кожного рядка словник

    reader = csv.DictReader(file)
    valid_users = []
    for row in reader:                  # КРОК 1: Розбір вже зроблено модулем csv (ім'я Марка не розірвалося, попри кому)
    user_score = int(row["score"])      # КРОК 2: Перетворення типу (текст "76" стає числом 76)
        if 0 <= user_score <= 100:      # КРОК 3: Валідація правил (перевіряємо, чи бал адекватний)
            row["score"] = user_score
            valid_users.append(row)
        else:
            print(f" Помилка логіки: Користувач {row['name']} має некоректний бал {user_score}!")

print("\nУспішно завантажені правильні користувачі:", valid_users)

Пояснення до прикладу:
1. csv.DictReader побачив лапки навколо "Марко, молодший", зрозумів, що це одне ціле, і зберіг ім'я правильно.
2. Програма успішно відфільтрувала Анну, тому що її бал 150 не пройшов валідацію (крок 3). Модуль csv сам по собі пропустив би цей бал, адже він не знає, що максимальна оцінка — 100.






## Блок 3. Надійний запис у CSV (DictWriter)

Головна ідея: При записі даних у файл потрібно переконатися, що папка для файлу взагалі існує. 
Також важливо правильно записати рядок-заголовок (назви колонок) 
і використовувати параметр newline="", щоб на Windows не з'являлися пусті рядки між даними.



Приклад: Створення папки та запис нових результатів

python

import csv
from pathlib import Path
new_results = [                                                     # Список словників, які ми хочемо зберегти
    {"name": "Олена", "score": 84},
    {"name": "Денис", "score": 91}
]
output_path = Path("export") / "results.csv"

output_path.parent.mkdir(exist_ok=True)                              # Гарантуємо, що папка "export" створиться, якщо її немає
with output_path.open("w", encoding="utf-8", newline="") as file:    # Відкриваємо файл у режимі запису ("w")
    writer = csv.DictWriter(file, fieldnames=["name", "score"])      # Вказуємо назви колонок, які мають бути в таблиці
    
    writer.writeheader()                  # 1. Записуємо перший рядок з назвами колонок
    writer.writerows(new_results)         # 2. Записуємо всі дані
print(f"Дані успішно записано у файл: {output_path}")


Пояснення до прикладу:
• Команда output_path.parent.mkdir(exist_ok=True) захищає програму від падіння. Якщо папки export не існувало, Python створить її автоматично перед тим, як створювати файл всередині.
• writer.writeheader() створює верхній рядок таблиці (name,score), без якого інші програми (наприклад, Excel) не змогли б зрозуміти, де які дані знаходяться.
Який із цих трьох процесів — пошук файлів за шаблоном, читання з валідацією чи запис із створенням папок — ви хочете спробувати написати самостійно у вашому поточному проекті?


# Блок 2. Безпечне та правильне читання CSV (DictReader)

Головна ідея: Файли CSV — це таблиці. Якщо всередині тексту є коми (наприклад, адреса або ім'я "Марко, молодший"), звичайний метод .split(",") розірве це ім'я навпіл і зіпсує таблицю. Модуль csv вміє це обходити. Крім того, під час читання всі дані є текстом, тому перетворення типів і перевірку логіки потрібно робити окремо.

Приклад: Читання та валідація користувачів

Припустимо, у нас є файл users.csv із вмістом:

csv
name,score
"Марко, молодший",76
Анна,150


python
import csv
from pathlib import Path

file_path = Path("data") / "users.csv"
with file_path.open(encoding="utf-8", newline="") as file:      # Відкриваємо файл (newline="" обов'язково для CSV)
    reader = csv.DictReader(file)                               # DictReader автоматично робить з кожного рядка словник
    valid_users = []
    for row in reader:                          # КРОК 1: Розбір вже зроблено модулем csv (ім'я Марка не розірвалося, попри кому)
        user_score = int(row["score"])          # КРОК 2: Перетворення типу (текст "76" стає числом 76)
        if 0 <= user_score <= 100:              # КРОК 3: Валідація правил (перевіряємо, чи бал адекватний)
            row["score"] = user_score
            valid_users.append(row)
        else:
            print(f" Помилка логіки: Користувач {row['name']} має некоректний бал {user_score}!")
print("\nУспішно завантажені правильні користувачі:", valid_users)


Пояснення до прикладу:

1. csv.DictReader побачив лапки навколо "Марко, молодший", зрозумів, що це одне ціле, і зберіг ім'я правильно.
2. Програма успішно відфільтрувала Анну, тому що її бал 150 не пройшов валідацію (крок 3). Модуль csv сам по собі пропустив би цей бал, адже він не знає, що максимальна оцінка — 100.

# Блок 3. Надійний запис у CSV (DictWriter)

Головна ідея: При записі даних у файл потрібно переконатися, що папка для файлу взагалі існує. Також важливо правильно записати рядок-заголовок (назви колонок) і використовувати параметр newline="", щоб на Windows не з'являлися пусті рядки між даними.

Приклад: Створення папки та запис нових результатів

python
import csv
from pathlib import Path

new_results = [                             # Список словників, які ми хочемо зберегти
    {"name": "Олена", "score": 84},
    {"name": "Денис", "score": 91}
]
output_path = Path("export") / "results.csv"
output_path.parent.mkdir(exist_ok=True)                             # Гарантуємо, що папка "export" створиться, якщо її немає
with output_path.open("w", encoding="utf-8", newline="") as file:            # Відкриваємо файл у режимі запису ("w")
    writer = csv.DictWriter(file, fieldnames=["name", "score"])              # Вказуємо назви колонок, які мають бути в таблиці
    writer.writeheader()                                             # 1. Записуємо перший рядок з назвами колонок
    writer.writerows(new_results)                                    # 2. Записуємо всі дані

print(f" Дані успішно записано у файл: {output_path}")

Пояснення до прикладу:
• Команда output_path.parent.mkdir(exist_ok=True) захищає програму від падіння. Якщо папки export не існувало, Python створить її автоматично перед тим, як створювати файл всередині.
• writer.writeheader() створює верхній рядок таблиці (name,score), без якого інші програми (наприклад, Excel) не змогли б зрозуміти, де які дані знаходяться.


# Запис і дописування
path.parent.mkdir(parents=True, exist_ok=True)
with path.open("w", encoding="utf-8") as file:
file.write("Перша нотатка\n")
with path.open("a", encoding="utf-8") as file:
file.write("Друга нотатка\n")




ПРИКЛАДИ ЗА ПІДРУЧНИКОМ: 
14.1. Поточна папка і pathlib

from pathlib import Path
print(Path.cwd())
data_path = Path("data") / "notes.txt"
print(data_path.resolve())

14.2. Читання тексту
from pathlib import Path
path = Path("data") / "notes.txt"
with path.open("r", encoding="utf-8") as file:
text = file.read()
print(text)

with закриває файл навіть при винятку. read() повертає весь текст; ве
ликі файли краще перебирати рядок за рядком:

with path.open(encoding="utf-8") as file:
for line in file:
print(line.rstrip("\n"))


14.3. Запис і дописування
path.parent.mkdir(parents=True, exist_ok=True)
with path.open("w", encoding="utf-8") as file:
file.write("Перша нотатка\n")
with path.open("a", encoding="utf-8") as file:
file.write("Друга нотатка\n")

Режим w очищає наявний файл.a додає в кінець.Передз аписом переконайтеся, що саме така поведінка потрібна


14.4. Каталоги й файли
for item in Path("data").iterdir():
if item.is_file():
print("файл", item.name)
elif item.is_dir():
print("папка", item.name)


14.5. CSV — таблиця з правилами цитування
name,group,score
Олена,КН-11,84
"Марко, молодший",КН-12,76
Кома всередині значення взята в лапки, тому split(',') дасть непра
вильні поля. Використовуйте модуль csv

14.6. Читання CSV
import csv
from pathlib import Path
path = Path("data") / "students.csv"
with path.open(encoding="utf-8", newline="") as file:
reader = csv.DictReader(file)
students = []
for row in reader:
row["score"] = int(row["score"])
students.append(row)
print(students)

14.7. Запис CSV
import csv
from pathlib import Path
students = [
{"name": "Олена", "group": "КН-11", "score": 84},
{"name": "Марко", "group": "КН-12", "score": 76},
]
path = Path("data") / "students.csv"
path.parent.mkdir(exist_ok=True)
with path.open("w", encoding="utf-8", newline="") as file:
writer = csv.DictWriter(file, fieldnames=["name", "group", "score"])
writer.writeheader()
writer.writerows(students)