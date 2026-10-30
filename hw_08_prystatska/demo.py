from study_tools.calculations import mean, clamp, weighted_sum
from study_tools.formatting import format_report

def main():
    """
    Головна функція для запуску демонстрації роботи модулів. (docstring).
    """
    hello_message = """Починаємо демонстрацію обчислень..."""
    print(hello_message)

    # 1. Тест mean
    avg_value = mean(10, 20, 30, 40, 50)
    print(format_report("Середнє арифметичне", avg_value))

    # 2. Тест clamp
    clamped_value = clamp(150, lower=0, upper=100)
    print(format_report("Обмеження діапазону (Clamp)", clamped_value))

    # 3. Тест weighted_sum
    items = [2, 4, 6]
    weights = [0.2, 0.5, 0.3]
    w_sum = weighted_sum(items, weights)
    print(format_report("Зважена сума", w_sum))

if __name__ == "__main__":
    main()
