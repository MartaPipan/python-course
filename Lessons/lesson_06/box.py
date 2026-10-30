#     17 / 5  → 3.4       ділення
#     17 // 5 → 3         повні частини
#     17 % 5  → 2         залишок

notebooks = 53
box_capacity = 8
full_boxes = notebooks // box_capacity
remainder = notebooks % box_capacity
boxes_needed = full_boxes + (remainder > 0)
print("Повних коробок:", full_boxes)
print("Залишилося зошитів:", remainder)
print("Потрібно коробок:", boxes_needed)


import math
count1 = 18 - 2 * 5
print("count", count1)  #8

count2 = (18 - 2) * 5  #80
print("count", count2)

# піднесення до степеня ** виконується справа наліво
count3 = 2 ** (3 ** 2)  #512
print("count", count3)


#Перетворити 367 секунд на хвилини й секунди
seconds = 367

minutes = seconds // 60
remaining_seconds = seconds % 60

print(minutes)
print(remaining_seconds)

print(minutes, "хв", remaining_seconds, "сек")

#   84 студенти, група по 18 студентів
students = 84
group_size = 18

full_groups = students // group_size
remainder = students % group_size

groups_needed = full_groups

if remainder > 0:
    groups_needed += 1

print("Повних груп:", full_groups)
print("Залишок:", remainder)
print("Потрібно груп:", groups_needed)

# Площа круга для введеного радіуса
import math

radius = float(input("Введіть радіус: "))

area = math.pi * radius ** 2

print(f"Площа круга: {area:.2f}")



count11 = (2 + 3) * 4
print("count", count11)  #20