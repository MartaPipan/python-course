is_registered = True
has_ticket = False
print(type(is_registered)) # <class 'bool'>

print(bool(False))

#  7.2. and, or, not
completion = 82
has_academic_debt = False
enough_work = completion >= 70
can_join_exam = enough_work and not has_academic_debt
print(can_join_exam) # True

# Перший if: один блок, два запуски
temperature = 3
if temperature < 5:
    print("Одягніть теплу куртку")
print("Перевірку завершено")

#  else 
age = int(input("Ваш вік: "))
if age >= 18:
    print("Повнолітній користувач")
else:
    print("Неповнолітній користувач")



    #elif
score = int(input("Бал: "))
if score >= 90:
    grade = "відмінно"
elif score >= 75:
    grade = "добре"
elif score >= 60:
    grade = "задовільно"
else:
    grade = "потрібне доопрацювання"
print(grade)



raw_answer = input("Крихкий товар (так/ні)? ")
answer = raw_answer.strip().lower()

# .strip() — прибирає зайві пробіли 
raw_answer = "      так  "
print(raw_answer.strip())

#   .lower() — переводить усі літери в нижній регістр  
# .lower()  → зробити літери маленькими
# .upper()  → зробити літери великими
"Так".lower()     # "так"
"ТАК".lower()     # "так"
"ТаК".lower()     # "так"


#7.9. Істинність непорожніх значень У логічному контексті порожні значення зазвичай хибні: 0, 0.0, "", [], {},None.
#  Непорожні — зазвичай істинні.

name = input("Ім'я: ").strip()
if name:
    print("Вітаю,", name)
else:
    print("Ім'я не введено")
# Це не означає, що name змінив тип на bool. if лише перевірив його істинність.

denominator = 0
if denominator != 0 and 10 / denominator > 2:
    print("Частка більша за 2")


#Вимога: студент допускається, якщо виконав щонайменше 70% робіт і не має академічного боргу.
completion = int(input("Виконано робіт, %: "))
debt_answer = input("Є академічний борг? (так/ні): ").strip().lower()
has_academic_debt = debt_answer == "так"
if completion >= 70 and not has_academic_debt:
    print("Допущено")
else:
    print("Допуску немає")
if completion >= 70:
    if has_academic_debt:
        print("Закрийте академічний борг")
    else:
        print("Допущено")
else: print("Завершіть потрібну кількість робіт")


#Напишіть програму, що визначає знак числа: додатне, від’ємне або нуль.

number = float(input("Введіть число: "))

if number > 0:
    print("Додатне число")
elif number < 0:
    print("Від'ємне число")
else:
    print("Нуль")

#2. Перевірте високосний рік із винятками для років, кратних 100 і 400.    
year = int(input("Введіть рік: "))

if year % 400 == 0:
    print("Високосний рік")
elif year % 100 == 0:
    print("Не високосний рік")
elif year % 4 == 0:
    print("Високосний рік")
else:
    print("Не високосний рік")


#Визначте стан води за температурою; окремо перевірте 0 і 100.
temperature = float(input("Введіть температуру: "))

if temperature < 0:
    print("Лід")
elif temperature == 0:
    print("Точка замерзання/плавлення")
elif temperature < 100:
    print("Рідина")
elif temperature == 100:
    print("Точка кипіння")
else:
    print("Пара")   

#4. Виправте if role == "admin" or "teacher":.

role = "admin" or "teacher"

if role in ("admin", "teacher"):
    print("Доступ дозволено")


#  Складіть таблицю для «квиток і (студентський або вік до 12)».
has_ticket = True
is_student = True
age = 20

if has_ticket and (is_student or age < 12):
    print("Умова виконана")
else:
    print("Умова не виконана")    

#  Напишіть калькулятор з вибором +, -, *, / і окремою перевіркою ділення на нуль.
    