temperature_text = "21.5"  #string
temperature = float(temperature_text)    #float
room_text = str(305)           #str 
print("Температура:", temperature)
print("Аудиторія:", room_text)

# Вираз       |Значення| Тип або помилка |
# int("12")    |      12| int           |  Текстовий рядок конвертується в тип int.
# float(12.0)  |   12.0 | float         |
# str(8)       |    "8" | str           |Ціле число конвертується в текстовий рядок.
# int(8.9)     |      8 | int           |int() не округлює — він відкидає дробову частину.
# int("8.9")   |      — |  ValueError   |int() не може напряму конвертувати рядок із дробовим числом. Спочатку треба використати float().
# round(8.9)   |    9   | int           |
# round("8.9") |      — | TypeError     |Помилка. Функція round() працює лише з числами (int або float) і не може приймати рядки.

#print() надсилає результат до термінала


result = 3 + 0.5
print("Результат:", result)   #float 3.5
print(type(result))

# "20" + "6" → "206"  (текст + текст)
# 20 + 6     → 26     (число + число)
# price = int("19.90")         price=float(19.90)

value_zero = int(254465)
first_value = int("8.5")    # ValueError
second_value = int("hello")  # ValueError




#Напишіть програму, що перетворює "125" на число, друкує тип до й після перетворення та не змінює початкове текстове ім’я

number_text = "125"

print(type(number_text))

number = int(number_text)

print(type(number))