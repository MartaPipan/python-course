def calculate_discount_price(original_price, discount_percent):
    # Перевірка правила: відсоток має бути строго в межах від 0 до 100
    if not 0 <= discount_percent <= 100:
        raise ValueError(f"Порушення контракту: знижка не може бути {discount_percent}%. "
                         f"Дозволений діапазон відсотків: від 0 до 100 включно.")
    
    final_price = original_price * (1 - discount_percent / 100)
    return final_price

# Приклад тестування:
try:
    # Спроба поставити некоректну знижку 120%
    print(calculate_discount_price(500, 120))
except ValueError as error:
    # Перехоплюємо наше повідомлення і виводимо його
    print(f" Виявлено помилку логіки: {error}")
