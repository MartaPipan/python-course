student_name = input("Введіть ім'я та прізвище: ")
group = input("Введіть код групи: ")

student_name = student_name.strip()  # strip() прибирає пробіли на краях
group = group.strip()



name_parts = student_name.split()  # звести кілька внутрішніх пробілів імені до одного
student_name = " ".join(name_parts)

# Перевірка імені

if len(name_parts) != 2:
    print("Помилка: ім'я повинно складатися рівно з двох слів")
else:
    first_name = name_parts[0]
    last_name = name_parts[1]


if not first_name.isalpha() or not last_name.isalpha():  #isalpha() кожнa частинa імені- літери
    print("Помилка: ім'я та прізвище повинні складатися тільки з літер")
else:
    first_name = first_name.title()  # first_name. імені з великої літери
    last_name = last_name.title()     # last_name. з великої літери

    
    group = group.upper()       # привести літери групи до верхнього регістру

          
    if len(group) != 5:                               # Перевірка довжини
        print("Помилка: код групи повинен мати 5 символів: 2 літери, дефіс і 2 цифри")

    elif group[2] != "-":                              # Перевірка позиції дефіса
        print("Помилка: дефіс повинен знаходитися на позиції 3")

    elif not group[:2].isalpha():
        print("Помилка: перші два символи групи повинні бути літерами")   # Перевірка перших 2 символів

    elif not group[3:].isdigit():                                          # Перевірка останніх 2 символів
        print("Помилка: останні два символи групи повинні бути цифрами")

    else:
        print("Прізвище -", last_name, "Ім'я -", first_name, "Код групи", group)
        print("Ініціали:", first_name[0] + ". " + last_name[0] + ".")

   