def mean(*values):
    """Середнє одного або кількох чисел; порожній виклик повертає None."""
    if not values:
        return None
    return sum(values) / len(values)

def clamp(value, lower=0, upper=100):
    """Повертає найближчу межу, якщо значення вийшло за діапазон."""
    if lower > upper:
        return None
    if value < lower:
        return lower
    if value > upper:
        return upper
    return value

def weighted_sum(values, weights):
    """Зважена сума двох списків однакової непорожньої довжини."""
    if not values or not weights or len(values) != len(weights):
        return None
    total = 0
    for index in range(len(values)):
        total += values[index] * weights[index]
    return total
