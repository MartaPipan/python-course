import math

# 1. ЗВИЧАЙНИЙ БАТЬКІВСЬКИЙ КЛАС (Без магії абстракцій)
class Shape:
    def area(self):
        # Якщо хтось забуде створити цей метод у дочірньому класі, 
        # програма видасть чітку помилку під час виклику.
        raise NotImplementedError("Підклас повинен реалізувати метод area()!")

# 2. ПІДКЛАС 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# 3. ПІДКЛАС 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# ==========================================
# 🎮 ТЕСТУВАННЯ (Працює абсолютно так само!)
# ==========================================
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    # Поліморфізм працює ідеально!
    print(f"Площа: {shape.area():.2f}")
