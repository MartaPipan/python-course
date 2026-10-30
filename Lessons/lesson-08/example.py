# 1. Покажіть числа від 10 до 1 і після них слово «Старт».

for number in range(10, 0, -1):  # Йдемо від 10 до 1    krok -1
    print(number)                # Виводимо число

print("Старт")                   # Після циклу виводимо "Старт"



initial_number = 10
for number in range(initial_number, 0, -1):
    print(number)

print("Старт") 

#  2. Знайдіть суму парних чисел від 2 до 100.
total = 0

for i in range(2, 100):
    total = total + i

print(total)  # 1+2+3+4+5...+100=4949


#Для готової послідовності scores = [58, 60, 73, 41, 90] обчисліть кількість оцінок не нижче 60, не змінюючи її елементів.
scores = [58, 60, 73, 41, 90]

count = 0
find_number = 60

for score in scores:
    if score >= find_number:
        count += 1

print(count)


#без змінної
scores = [58, 60, 73, 41, 90]

count = 0                    # Лічильник оцінок

for score in scores:
    if score >= 60:          # Якщо оцінка 60 або більше
        count += 1           # Збільшуємо лічильник на 1

print(count)