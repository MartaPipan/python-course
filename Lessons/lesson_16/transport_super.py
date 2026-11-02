class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def start_engine(self):
        return f"Двигун {self.brand} заведено!"


class Truck(Vehicle):
    def __init__(self, brand, max_speed, payload):
        # Передаємо бренд і швидкість "наверх" батьківському класу
        super().__init__(brand, max_speed)
        
        # Додаємо власну унікальну фішку вантажівки
        self.payload = payload

    def load_cargo(self):
        return f"Вантажівка {self.brand} завантажує {self.payload} тонн вантажу."

# Створюємо об'єкт вантажівки
scania = Truck("Scania", 90, 20)

print(scania.start_engine())  # Працює метод батька: Двигун Scania заведено!
print(scania.load_cargo())    # Працює власний метод: Вантажівка Scania завантажує 20 тонн вантажу.
