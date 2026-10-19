# 1. Зміна регістру
text = "python для початківців"

print(text.lower())       # усі літери маленькі
# python для початківців

print(text.upper())       # усі літери великі
# PYTHON ДЛЯ ПОЧАТКІВЦІВ

print(text.title())       # кожне слово з великої літери
# Python Для Початківців

print(text.capitalize())  # тільки перша літера всього рядка
# Python для початківців



                          #2. strip(), lstrip(), rstrip()
text = "   Python   "

print(text.strip())       # прибирає пробіли з обох країв
# Python

print(text.lstrip())      # прибирає пробіли тільки зліва
# Python   

print(text.rstrip())      # прибирає пробіли тільки справа
#    Python

                                 # replace()
text = "Я вивчаю Java"

print(text.replace("Java", "Python"))
# Я вивчаю Python



                                 #split()  Тепер можемо звертатися до окремих слів:
                                 
text = "Python для початківців"
words = text.split()

print(words)
# ['Python', 'для', 'початківців']
print(words[0])
# Python

print(words[1])
# для

print(words[2])
# початківців


                                            #  5. join()
words = ["Python", "для", "початківців"]
text = " ".join(words)
print(text)
# Python для початківців


Через дефіс:
words = ["Python", "для", "початківців"]
text = "-".join(words)
print(text)
# Python-для-початківців

                                #  6. isalpha()      Перевіряє, чи всі символи — літери.Пробіл також робить результат False.

print("Python".isalpha())
# True

print("Python123".isalpha())
# False

print("Python  для".isalpha())
# False


                                         #7. isdigit()
print("12345".isdigit())
# True

print("123a".isdigit())
# False

print("12 34".isdigit())
# False
                                     
                                      #8. isalnum()   Перевіряє, чи є тільки літери або цифри.

print("Python123".isalnum())
# True

print("Python".isalnum())
# True

print("12345".isalnum())
# True

print("Python 123".isalnum())
# False — є пробіл

print("Python_123".isalnum())
# False — є _
                                                
                                        # 9. startswith() Перевіряє, чи рядок починається з певного тексту.

text = "Python для початківців"

print(text.startswith("Python"))
# True

print(text.startswith("Java"))
# False

                                       #   10. endswith()    Перевіряє, чи рядок закінчується певним текстом.

text = "Python для початківців"

print(text.endswith("ців"))
# True

print(text.endswith("Python"))
# False

                                   #  find()   Знаходить індекс першого входження.

text = "Python для початківців"

print(text.find("для"))
# 7

# Подивимося на індекси:
#  P y t h o n   д л я
#  0 1 2 3 4 5 6 7 8 9

print(text.find("Java"))
# -1

                                      #12. rfind()    Шукає останнє входження.

text = "banana"
print(text.find("a"))
# 1

print(text.rfind("a"))
# 5

Тобто:

b a n a n a
0 1 2 3 4 5

                             # 13. count()

Рахує, скільки разів зустрічається символ або текст.

text = "banana"

print(text.count("a"))
# 3

print(text.count("an"))
# 2

                        # 14. len()   Показує кількість символів.

text = "Python"
print(len(text))
# 6

#  Пробіл теж рахується:

text = "Hi Marta"
print(len(text))
# 8


                          # 15. Індекс [ ]   Отримуємо один символ.

text = "Python"

print(text[0])
# P

print(text[1])
# y

print(text[5])
# n

З кінця:

print(text[-1])
# n

print(text[-2])
# o
                              
                              
                                # 16. Зріз [start:end]
text = "Python"

print(text[0:2])
# Py

print(text[2:5])
# tho

print(text[:3])
# Pyt

print(text[3:])
# hon

                              #    17. islower() і isupper()
print("python".islower())
# True

print("Python".islower())
# False

print("PYTHON".isupper())
# True

print("Python".isupper())
# False

                                      # 18. isspace()  Перевіряє, чи рядок складається тільки з пробілів / пробільних символів.

print("   ".isspace())
# True

print("Python".isspace())
# False

print("  Python  ".isspace())
# False