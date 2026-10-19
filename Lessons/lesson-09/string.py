text = " Python для початківців "

clean = text.strip()                  # strip() — прибирає пробіли з початку та кінця

print(clean.lower())                  # lower() — переводить усі літери в нижній регістр

print(clean.upper())                  # upper() — переводить усі літери у верхній регістр

print(clean.title())                  # title() — робить першу літеру кожного слова великою

print(clean.replace("початківців", "студентів"))
# replace() — замінює один текст на інший

print(clean.startswith("Python"))
# startswith() — перевіряє, чи починається рядок із вказаного тексту

print(clean.endswith("ців"))
# endswith() — перевіряє, чи закінчується рядок вказаним текстом

print(clean.find("для"))
# find() — знаходить індекс першого входження тексту
# якщо текст не знайдено → повертає -1


print(clean.count("і"))
# count() — рахує, скільки разів вказаний символ або текст зустрічається в рядку


print(clean.split())
# split() — розділяє рядок на частини та створює список
# тут результат: ['Python', 'для', 'початківців']


words = clean.split()

print(" ".join(words))
# join() — об'єднує елементи списку в один рядок
# " " означає, що між словами буде пробіл


print(clean.isalpha())
# isalpha() — перевіряє, чи складається весь рядок тільки з літер
# тут False, тому що в рядку є пробіли


print("Python".isalpha())
# True — Python складається тільки з літер


print("12345".isdigit())
# isdigit() — перевіряє, чи складається рядок тільки з цифр
# True


print("Python123".isdigit())
# False — тут є літери


print(clean.islower())
# islower() — перевіряє, чи всі літери в нижньому регістрі


print(clean.isupper())
# isupper() — перевіряє, чи всі літери у верхньому регістрі


print(clean.isspace())
# isspace() — перевіряє, чи складається рядок тільки з пробілів та інших пробільних символів


print(clean.find("Python"))
# find() — повертає індекс, з якого починається "Python"


print(clean[0])
# [0] — отримує символ за індексом 0


print(clean[:6])
# [:6] — зріз: бере символи від початку до індексу 6
# індекс 6 НЕ включається


print(len(clean))
# len() — повертає кількість символів у рядку


# 9.1. Лапки обмежують значення
course = "Основи Python"
message = "Натисніть 'Enter'"

#Потрійні лапки зберігають переноси:
notice = """Розклад:
понеділок — лекція
середа — практика"""

#          \n   означає перейти на новий рядок.
print("Привіт\nМарта")

#          \t — вставляє табуляцію, тобто горизонтальний відступ.
print("Ім'я:\tМарта")

print("Ім'я\tВік")
print("Марта\t30")
print("Інна\t25")



# Навіщо потрібен r перед рядком?
# C:\new\test
# у \new і сприймає \n як новий рядок, як і \t --\test 
print("C:\new\test")
path = "C:\new\test"

#Тому для Windows-шляхів зручно використовувати сирий рядок:raw — сприймай зворотні слеші переважно буквально.
path = r"C:\new\test"

 #9.2.                      Кожний символ має індекс   [початок:кінець] — початок включається, а права межа не включається
word = "Python"
print(word[0]) # P
print(word[5]) # n
print(word[-1]) # n


#         9.3. Зріз бере діапазон без правої межі    Загальна форма — text[start:stop:step].

#                             Загальна форма — text[start:stop:step].  

word = "Python"
print(word[1:4]) # yth
print(word[:2]) # Py
print(word[2:]) # thon
print(word[::-1]) # nohtyP

#        Рядки незмінні
word = "cat"
# word[0] = "b" # TypeError
word = "b" + word[1:]
print(word) # bat

#    Методи рядків теж не змінюють вихідний об’єкт:
raw_name = " Олена "
clean_name = raw_name.strip()
print(raw_name) # пробіли залишилися
print(clean_name) # Олена


# Метод — це дія, яку ми можемо виконати над рядком.

text = " Python для початківців "
clean = text.strip()
print(clean.lower())
print(clean.upper())
print(clean.title())  #title() створює рядок, у якому кожне слово починається з великої літери.
print(clean.replace("початківців", "студентів"))
print(clean.startswith("Python"))
print(clean.endswith("ців"))
print(clean.find("для"))

# split() без аргументу прибирає повторні проміжки
# len(parts) рахує отримані частини
# індекси [0] і [1] читають першу та другу частини після перевірки довжини

raw_name = " олЕНА КОВАЛЬ "
parts = raw_name.split()
if len(parts) == 2:
first_name = parts[0].title()
last_name = parts[1].title()
label = f"{last_name}, {first_name}"
print(label) # Коваль, Олена
else:
print("Очікується рівно ім'я та прізвище")


                                                #  for char in ...
                                                # Взяти кожен символ рядка по одному.

                                                # п
                                                # р
                                                # о
                                                # г
                                                # р
                                                # а
                                                # м
                                                # у
                                                # в
                                                # а
                                                # н
                                                # н
                                                # я

                                                # if char in vowels:
                                                # in означає: чи міститься цей елемент всередині?
                                                vowels = "аеєиіїоуюя"
count = 0
for char in "програмування".lower():
if char in vowels:
count += 1
print(count)