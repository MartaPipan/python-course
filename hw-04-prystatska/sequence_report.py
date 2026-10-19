#count_positive
#count_negative
#non_zero
#especial_number =13
#number


count_positive = 0
count_negative = 0
non_zero = 0
especial_number = 0

total = 0
minimum_number = None
maximum_number = None

while True:    # while повторює, поки умова істинна
    number = int(input("Введіть число: "))

    if number == 0:
        break        # break завершує найближчий цикл

    if number == 13:
        especial_number += 1
        continue  #не обробляємо 13 далі; continue пропускає решту поточної ітерації і переходить до наступного числа ,
                  # pass = "тут поки нічого не робимо"

    non_zero += 1     # збільшуємо кількість прийнятих чисел
    total += number

    if number > 0:
        count_positive += 1
    elif number < 0:
        count_negative += 1

    if minimum_number is None:
        minimum_number = number   # присвоюєм першому введеному числу мін і мах знач. 
        maximum_number = number
    else:
        if number < minimum_number:
            minimum_number = number       #кожне нове число порівнюю з попереднім min - i maximum_number

        if number > maximum_number:
            maximum_number = number


if non_zero == 0 and especial_number == 0:
    print("Даних немає")
else:
    summary = [
    "Додатних чисел: " + str(count_positive) + ",  Від'ємних чисел: " + str(count_negative),
    "Всього чисел:" + str(non_zero) + " Сума: " + str(total),
    "Мінімум: " + str(minimum_number) + " Максимум: " + str(maximum_number) +
    " Пропущено 13: " + str(especial_number)
]

    # range(1, 4) дає 1, 2, 3 — номери трьох рядків
    for number in range(1, 4):

        if number == 1:
            print("1. Додатних чисел:", count_positive,
                  "Від'ємних чисел:", count_negative)

        elif number == 2:
            print("2. Всього чисел:", non_zero,
                  "Сума:", total)

        elif number == 3:
            print("3. Мінімум:", minimum_number,
                  "Максимум:", maximum_number,
                  "Пропущено числo 13:", especial_number)