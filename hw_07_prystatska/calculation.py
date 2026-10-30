#---Обов’язкове ядро---

"""середнє одного або кількох чисел; порожній виклик повертає None"""
def mean (*values):
    if not values:
        return None
    return sum(values) / len(values)

""" повертає найближчу межу,якщо значення вийшло за діапазон; для lower > upper повертає None"""
def clamp(value, lower=0, upper=100):
    if lower > upper:
        return None
    if value < lower:
        return lower
    if value > upper:
        return upper
    return value


""" зважена сума двох списків однакової непорожньої довжини"""
def weighted_sum(values, weights):
    if not values or not weights or len(values) != len(weights):
        return None
    total = 0
    for index in range(len(values)):
        total += values[index] * weights[index]
    return total



# --- Розширення після ядра  ---

"""Форматує запис про об'єкт з довільним набором іменованих характеристик."""

def format_record(title, **fields):
    final_output = f"Запис: {title}"
    if fields:
        details = ", ".join(f"{key}: {value}" for key, value in fields.items())
        final_output += f"; характеристики: {details}"
    return final_output



"""Рекурсивно обчислює факторіал цілого невід'ємного числа n."""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
