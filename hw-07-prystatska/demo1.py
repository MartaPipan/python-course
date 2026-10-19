from calculation import format_record, mean, clamp, weighted_sum, format_record, factorial


#  ТЕСТ 1.1 mean (середнє кількох чисел) 
expected_mean_1 = 20.0
result_mean_1 = mean(10, 20, 30)

print("--- Тест функції mean (середнє кількох чисел) ---")
print("Вхідні дані: 10, 20, 30")
print(f"Очікуваний результат: {expected_mean_1}")
print(f"Фактичний результат: {result_mean_1}")
print(f"Результат перевірки: {'збігається' if result_mean_1 == expected_mean_1 else 'не збігається'}\n")


#  ТЕСТ 1.2 mean (середнє одного числа)
expected_mean_2 = 10.0
result_mean_2 = mean(10)

print("--- Тест функції mean (середнє одного числа) ---")
print("Вхідні дані: 10")
print(f"Очікуваний результат: {expected_mean_2}")
print(f"Фактичний результат: {result_mean_2}")
print(f"Результат перевірки: {'збігається' if result_mean_2 == expected_mean_2 else 'не збігається'}\n")


#  ТЕСТ 1.3: mean (порожній виклик) 
expected_mean_3 = None
result_mean_3 = mean()

print("--- Тест функції mean (порожній виклик(повертає None)) ---")
print("Вхідні дані: без аргументів")
print(f"Очікуваний результат: {expected_mean_3}")
print(f"Фактичний результат: {result_mean_3}")
print(f"Результат перевірки: {'збігається' if result_mean_3 == expected_mean_3 else 'не збігається'}\n")



#  ТЕСТ 2.1: clamp (Вихід за верхню межу) 
expected_clamp_1 = 100
result_clamp_1 = clamp(value=150, lower=0, upper=100)

print("--- Тест функції clamp (вихід за верхню межу) ---")
print("Вхідні дані: value = 150, lower = 0, upper = 100")
print(f"Очікуваний результат: {expected_clamp_1}")
print(f"Фактичний результат: {result_clamp_1}")
print(f"Результат перевірки: {'збігається' if result_clamp_1 == expected_clamp_1 else 'не збігається'}\n")



#  ТЕСТ 2.2: clamp (Вихід за нижню межу) 
expected_clamp_2 = 0
result_clamp_2 = clamp(value=-10, lower=0, upper=100)

print("--- Тест функції clamp (вихід за нижню межу) ---")
print("Вхідні дані: value = -10, lower = 0, upper = 100")
print(f"Очікуваний результат: {expected_clamp_2}")
print(f"Фактичний результат: {result_clamp_2}")
print(f"Результат перевірки: {'збігається' if result_clamp_2 == expected_clamp_2 else 'не збігається'}\n")


# ТЕСТ 2.3: clamp (неправильний порядок меж) 
expected_clamp_3 = None
result_clamp_3 = clamp(value=0, lower=100, upper=0)

print("--- Тест функції clamp (неправильний порядок меж) ---")
print("Вхідні дані: value = 0, lower = 100, upper = 0")
print(f"Очікуваний результат: {expected_clamp_3}")
print(f"Фактичний результат: {result_clamp_3}")
print(f"Результат перевірки: {'збігається' if result_clamp_3 == expected_clamp_3 else 'не збігається'}\n")



#  ТЕСТ 3.1: weighted_sum (Звичайний набір)
values = [1, 2, 3]
weights = [10, 20, 30]
expected_1 = 140  # (1*10) + (2*20) + (3*30) = 10 + 40 + 90 = 140
result_1 = weighted_sum(values, weights)

print("--- Тест функції weighted_sum (звичайний набір) ---")
print(f"Вхідні дані: values = {values}, weights = {weights}")
print(f"Очікуваний результат: {expected_1}")
print(f"Фактичний результат: {result_1}")
print(f"Результат перевірки: {'збігається' if result_1 == expected_1 else 'не збігається'}\n")


# ТЕСТ 3.2: weighted_sum (Порожні списки)
values = []
weights = []
expected_2 = None
result_2 = weighted_sum(values, weights)

print("--- Тест функції weighted_sum (порожні списки) ---")
print(f"Вхідні дані: values = {values}, weights = {weights}")
print(f"Очікуваний результат: {expected_2}")
print(f"Фактичний результат: {result_2}")
print(f"Результат перевірки: {'збігається' if result_2 == expected_2 else 'не збігається'}\n")


#  ТЕСТ 3.3: weighted_sum (Різна довжина списків) 
values = [1, 2, 3]
weights = [10]
expected_3 = None
result_3 = weighted_sum(values, weights)

print("--- Тест функції weighted_sum (різна довжина списків) ---")
print(f"Вхідні дані: values = {values}, weights = {weights}")
print(f"Очікуваний результат: {expected_3}")
print(f"Фактичний результат: {result_3}")
print(f"Результат перевірки: {'збігається' if result_3 == expected_3 else 'не збігається'}\n")


#  ТЕСТ 4.1: format_record (Заповнені поля)
title = "Анна"
fields = {"group": "КН-11", "age": 19, "status": "активний", "телефон": "+3809610101101", "адреса": "вул. Лесі Українки, 10"}
expected_record = "Запис: Анна; характеристики: group: КН-11, age: 19, status: активний, телефон: +3809610101101, адреса: вул. Лесі Українки, 10"
result_record = format_record(title, **fields)

print("--- Тест функції format_record (заповнені поля) ---")
print("Вхідні дані: name='Анна', group='КН-11', age=19, status='активний', телефон='+3809610101101', адреса='вул. Лесі Українки, 10'")
print(f"Очікуваний результат: {expected_record}")   
print(f"Фактичний результат: {result_record}")
print(f"Результат перевірки: {'збігається' if result_record == expected_record else 'не збігається'}\n")


#  ТЕСТ 4.2: format_record (незаповнені поля) 
title = "Іван"
fields = {}
expected_record = "Запис: Іван"
result_record = format_record(title, **fields)

print("--- Тест функції format_record (незаповнені поля) ---")
print("Вхідні дані: name='Іван'")
print(f"Очікуваний результат: {expected_record}")   
print(f"Фактичний результат: {result_record}")
print(f"Результат перевірки: {'збігається' if result_record == expected_record else 'не збігається'}\n")


#  ТЕСТ 4.3: format_record (заовнене одне поле характеристики) 
title = "Марія"
fields = {"group": "КН-11"}
expected_record = "Запис: Марія; характеристики: group: КН-11"
result_record = format_record(title, **fields)

print("--- Тест функції format_record (заповнене одне поле характеристики) ---")
print("Вхідні дані: name='Марія', group='КН-11'")
print(f"Очікуваний результат: {expected_record}")   
print(f"Фактичний результат: {result_record}")
print(f"Результат перевірки: {'збігається' if result_record == expected_record else 'не збігається'}\n")


# ТЕСТ 5.1: factorial (рекурсивний тест) 
n = 4
expected_factorial = 24  # 4! = 4 * 3 * 2 * 1 = 24
result_factorial = factorial(n)

print("--- Тест функції factorial (рекурсивний тест) ---")
print(f"Вхідні дані: n = {n}")
print(f"Очікуваний результат: {expected_factorial}")
print(f"Фактичний результат: {result_factorial}")
print(f"Результат перевірки: {'збігається' if result_factorial == expected_factorial else 'не збігається'}\n")
