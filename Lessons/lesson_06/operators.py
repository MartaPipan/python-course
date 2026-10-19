# 6.3. Частка й остача розкладають кількість

minutes_total = 137
hours = minutes_total // 60
minutes = minutes_total % 60
print(hours, "год", minutes, "хв") # 2 год 17 хв       137 = 2 * 60 + 17   


# 6.5. Скорочене присвоєння змінює наявне значення Аналогічно працюють +=, *=, /=, //=, %= і **=. 
balance = 500
balance = balance - 120 #Другий рядок можна записати коротше:
balance -= 120

#  in            in перевіряє належність елемента колекції:
allowed_rooms = [101, 203, 305]
print(203 in allowed_rooms)  #true

print(404 not in allowed_rooms) #Чи немає 404 у списку?  True

names = ["Anna", "Marta", "Iryna"]

print("Marta" in names) #true
print("Olena" in names) #false



# is   «Чи це буквально один і той самий об'єкт у пам'яті?»
a = [1, 2, 3]
b = a

print(a is b) #true

result = None

#None   «немає значення» / «значення відсутнє»
print(result is None)


result = 25

if result is None:
    print("Результату немає")
else:
    print("Результат є")
    