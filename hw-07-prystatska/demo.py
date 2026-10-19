from calculation import mean, clamp, weighted_sum, format_record, factorial

def check(test_name, inputs, expected, result):
    status = "збігається" if expected == result else " не збігається"
    print(f"--- Тест функції {test_name} ---")
    print(f"  Вхідні дані: {inputs}")
    print(f"  Очікувано:   {expected}")
    print(f"  Фактично:    {result}")
    print(f"  Результат:   {status}\n")


#  ТЕСТИ 1: mean
check("mean (середнє кількох чисел)", "10, 20, 30", 20.0, mean(10, 20, 30))
check("mean (середнє одного числа)", "10", 10.0, mean(10))
check("mean (порожній виклик)", "без аргументів", None, mean())


#  ТЕСТИ 2: clamp

check("clamp (вихід за верхню межу)", "value=150, lower=0, upper=100", 100, clamp(value=150, lower=0, upper=100))
check("clamp (вихід за нижню межу)", "value=-10, lower=0, upper=100", 0, clamp(value=-10, lower=0, upper=100))
check("clamp (неправильний порядок меж)", "value=0, lower=100, upper=0", None, clamp(value=0, lower=100, upper=0))


#  ТЕСТИ 3: weighted_sum 
check("weighted_sum (звичайний набір)", "values=[1, 2, 3], weights=[10, 20, 30]", 140, weighted_sum([1, 2, 3], [10, 20, 30]))
check("weighted_sum (порожні списки)", "values=[], weights=[]", None, weighted_sum([], []))
check("weighted_sum (різна довжина списків)", "values=[1, 2, 3], weights=[10]", None, weighted_sum([1, 2, 3], [10]))


# ТЕСТИ 4: format_record
name_4_1 = "Анна"
fields_4_1 = {"group": "КН-11", "age": 19, "status": "активний", "телефон": "+3809610101101", "адреса": "вул. Лесі Українки, 10"}
exp_4_1 = "Запис: Анна; характеристики: group: КН-11, age: 19, status: активний, телефон: +3809610101101, адреса: вул. Лесі Українки, 10"
check("format_record (заповнені поля)", f"name='{name_4_1}', fields={fields_4_1}", exp_4_1, format_record(name_4_1, **fields_4_1))


name_4_2 = "Іван"
fields_4_2 = {}
exp_4_2 = "Запис: Іван"  
check("format_record (незаповнені поля)", f"name='{name_4_2}'", exp_4_2, format_record(name_4_2, **fields_4_2))


name_4_3 = "Марія"
fields_4_3 = {"group": "КН-11"}
exp_4_3 = "Запис: Марія; характеристики: group: КН-11"
check("format_record (одне поле)", f"{name_4_3}, {fields_4_3}", exp_4_3, format_record(name_4_3, **fields_4_3))

# --- ТЕСТИ 5: factorial ---
check("factorial (рекурсивний тест)", "n = 4", 24, factorial(4))
