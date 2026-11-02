class CurrencyConverter:
    def __init__(self, currency_name):
        self.currency_name = currency_name  # Звичайна властивість об'єкта

    # 1. Звичайний метод (потрібен об'єкт, бо є self)
    def show_info(self):
        return f"Цей конвертер створено для: {self.currency_name}"

    # 2. СТАТИЧНИЙ МЕТОД (об'єкт НЕ потрібен, self НЕМАЄ)
    @staticmethod
    def dollar_to_hryvnia(dollars, rate):
        # Просто бере аргументи, рахує та повертає результат
        return dollars * rate




"""
🕹️ Як викликати статичний метод?

Оскільки статичний метод не залежить від об'єктів, 
його можна викликати напряму через назву класу,
 навіть не створюючи жодного студента, користувача чи автівку!"""


# Варіант 1: Виклик НАПРЯМУ через Клас (найпопулярніший спосіб)
result1 = CurrencyConverter.dollar_to_hryvnia(100, 41.5)
print(f"100 доларів це: {result1} грн")  # Виведе: 4150.0 грн

# Варіант 2: Через об'єкт (теж працює, але використовується рідше)
my_converter = CurrencyConverter("USD")
result2 = my_converter.dollar_to_hryvnia(50, 41.5)
print(f"50 доларів це: {result2} грн")
