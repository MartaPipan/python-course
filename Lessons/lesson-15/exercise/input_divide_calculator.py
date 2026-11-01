
# Калькулятор ділення з повною обробкою помилок 
# Програма обробляє правильні числа, захищає від ділення на нуль (ZeroDivisionError)
#  та ловить некоректне введення тексту (ValueError).


def divide_calculator():
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        
        result = num1 / num2
        print(f"✅ Результат ділення: {result}")
        
    except ZeroDivisionError:
        print("❌ Помилка: Ділити на нуль (0) математично неможливо!")
    except ValueError:
        print("❌ Помилка: Введено нечисловий текст! Будь ласка, використовуйте лише цифри.")

# Виклик функції для перевірки
divide_calculator()
