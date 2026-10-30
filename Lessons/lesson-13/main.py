import math_utils  # Спосіб 1: Імпорт усього модуля
from math_utils import add  # Спосіб 2: Імпорт конкретної функції

# ==============================================================================
# ГОЛОВНИЙ ФАЙЛ: main.py
# Імпортує інструменти з модуля calculations.py та запускає всю логіку
# ==============================================================================

import calculations



print(math_utils.multiply(2, 3))  # Виведе: 6
print(add(5, 5))  # Виведе: 10


def run_program():
    """Основна функція програми, де відбувається вся логіка."""
    
    print("--- ЗАПУСК ГОЛОВНОЇ ПРОГРАМИ ---")
    
    # Частина 1: Звичайні математичні обчислення
    part = 20
    whole = 50
    result_pct = calculations.percentage(part, whole)
    print(f"[*] Відсоток від {part} у числі {whole} становить: {result_pct}%")
    
    base_number = 15
    result_double = calculations.double_value(base_number)
    print(f"[*] Подвоєне значення числа {base_number} дорівнює: {result_double}")
    
    print("\n--- КАСОВИЙ АПАРАТ СУПЕРМАРКЕТУ ---")
    
    # Частина 2: Логіка супермаркету
    milk_price = 40.0
    
    # Беремо з калькулятора ТІЛЬКИ функцію обчислення податку
    tax = calculations.calculate_tax(milk_price)
    total = milk_price + tax
    
    print(f"Товар: Молоко ({milk_price} грн)")
    print(f"Податок (ПДВ 20%): {tax} грн")
    print(f"Разом до сплати: {total} грн")
    print("---------------------------------")

# Головний захисний перемикач програми
if __name__ == "__main__":
    run_program()



###     if __name__ == "__main__":
###         назва_вашої_функції()
