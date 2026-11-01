def check_registration_age(user_age_text):
    try:
        # 1. Спершу захищаємося від нечислового тексту в полі віку
        age = int(user_age_text)
        
        # 2. Перевіряємо бізнес-правило (заміна небезпечного assert)
        if age < 18:
            raise ValueError(f"Доступ обмежено. Ваш вік: {age}. "
                             f"Реєстрація дозволена лише особам від 18 років.")
        
        # 3. Перевірка на адекватність введення даних
        if age > 120 or age < 0:
            raise ValueError(f"Введено нереалістичний вік: {age}.")
            
        print("🎉 Реєстрацію успішно пройдено!")
        return True
        
    except ValueError as error:
        # Ловимо і помилку тексту від int(), і наші кастомні ValueError від raise
        print(f"❌ Відхилено: {error}")
        return False

# Приклади роботи:
check_registration_age("16")     # Спрацює raise для неповнолітніх
check_registration_age("двадцять") # Спрацює ValueError від функції int()
check_registration_age("25")     # Успішний прохід
