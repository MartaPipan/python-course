import math

radius = 3
area = math.pi * radius ** 2

print(area)
print(math.sqrt(81))
print(math.ceil(4.2))
print(math.floor(4.8))

#     Обчислення площі круга
import math
radius = 3
area = math.pi * radius ** 2

print(area)

#   ** — це оператор піднесення до степеня.

3 ** 2    # 9
2 ** 3    # 8
5 ** 2    # 25

#     math.sqrt() — квадратний корінь
print(math.sqrt(81))    #  √81 = 9
math.sqrt(16)  # 4.0
math.sqrt(25)  # 5.0
math.sqrt(2)   # 1.414...

#    math.ceil() — округлення вгору
math.ceil(4.1)  # 5
math.ceil(4.8)  # 5
math.ceil(4.0)  # 4

math.ceil(-4.8)  # -4

#   floor = підлога → округлення до найближчого меншого цілого.

math.floor(4.2)  # 4
math.floor(4.8)  # 4
math.floor(4.0)  # 4

math.floor(-4.2)  # -5

import math
print(math.isclose(0.1 + 0.2, 0.3)) # True

math.isclose(10.00001, 10.00002)  #true