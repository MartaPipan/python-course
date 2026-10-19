#append() — додати елемент у кінець
scores = [72, 88, 91]
scores.append(84)
print(scores) #[72, 88, 91, 84]


scores.append([84, 90])
#[72, 88, 91, [84, 90]]


#extend() — extend = розширити список елементами іншої послідовності 
# Якщо потрібно додати кожен елемент окремо, використовуємо extend():
scores = [72, 88, 91, 84]
scores.extend([81, 98])
print(scores)
. insert() — вставити елемент

#insert() дозволяє вказати позицію, куди потрібно вставити елемент.
scores = [72, 88, 91]
scores.insert(1, 80)
print(scores) #[72, 80, 88, 91]


# remove() — видалити за значенням.remove() видаляє перше знайдене значення.
scores = [72, 88, 91, 88]
scores.remove(88)
print(scores)

#pop() — видалити за позицією pop() відрізняється від remove().
# remove() шукає значення.
# pop() працює з індексом.
scores = [72, 88, 91]
removed = scores.pop(1)
print(scores)
print(removed)

#Ми видалили елемент з індексом 1 і одночасно зберегли його в змінній removed.


# pop() без індексу
Якщо написати:
scores.pop()

# буде видалено останній елемент.
scores = [72, 88, 91]
removed = scores.pop()
print(scores)
print(removed)

#Результат:[72, 88] 91

#  del — видалити елемент  del видаляє елемент, але не повертає його.
Можна також використати del:
scores = [72, 88, 91]
del scores[1]
print(scores)

#    Перевірка in  Можна перевірити, чи є елемент у списку:
scores = [72, 88, 91]
print(88 in scores)

# Перебір списку через for  Можна пройти по кожному елементу:
scores = [72, 88, 91]
for score in scores:
    print(score)


#1. Якщо потрібне тільки значення  (Python по черзі бере кожен елемент:)
#Тут позиція елемента нам не потрібна, тому немає сенсу працювати з індексами.
scores = [85, 92, 78, 95]
for score in scores:
    print(score)



    #  enumerate() — коли потрібні і позиція, і значення
for position, score in enumerate(scores):
    print(position, score)


    #Що означає start=1?  починає рахувати не з 0, а з 1.
for position, score in enumerate(scores, start=1):
    print(position, score)


scores = [85, 92, 78, 95]
for position, score in enumerate(scores, start=1):
    print(f"Оцінка №{position}: {score}")

# Зріз створює новий список
values = [10, 20, 30, 40, 50]
middle = values[1:4]
print(middle) # [20, 30, 40]