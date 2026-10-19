
#  for:      «Пройди всі елементи / зроби певну кількість разів».

#1. Повторити дію 5 разів
for i in range(5):
    print("Hello")

##2. Вивести числа від 1 до 5    
for i in range(1, 6):
    print(i)

# Вивести числа від 0 до 4    
for i in range(5):
    print(i)

#4. Вивести парні числа    
for i in range(2, 11, 2):  #2 — початок  11 — до цього числа, але не включаючи 11   i  2 — крок
    print(i)

 #5. Пройтися по списку   
names = ["Marta", "Anna", "Igor"]

for name in names:
    print(name)

#  6. Пройтися по слову
word = "Python"

for letter in word:
    print(letter)   
#P
#y
#t
#h
#o
#n

#  7. Порахувати суму чисел
total = 0

for i in range(1, 6):
    total = total + i

print(total)  # 1+2+3+4+5 =15

# 8. Таблиця множення на 5
for i in range(1, 11):
    print(f"5 × {i} = {5 * i}")   #5 × 1 = 5    5 × 2 = 10    5 × 3 = 15...   5 × 10 = 50

 # 9.  for + if
for i in range(1, 11):   #створити послідовність чисел від 1 до 10. для кожного числа з range(1, 11) поклади це число в змінну i.
    if i % 2 == 0:       #чи ділиться i на 2 без залишку?
        print(i)   



# 8.4. Вкладений for
for row in range(1, 3):                    #Для кожного значення row внутрішній цикл проходить усі три column
    for column in range(1, 4):
        print(row, column)        