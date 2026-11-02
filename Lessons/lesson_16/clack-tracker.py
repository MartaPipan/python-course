"""У Python для множинного успадкування ми просто перелічуємо батьківські класи через кому в дужках: class СмартГодинник(Годинник, ФітнесТрекер):"""

class Clock:
    def __init__(self, time_format="24h"):
        self.time_format = time_format

    def show_time(self):
        return f"⏰ Зараз котрась година у форматі {self.time_format}"


class FitnessTracker:
    def __init__(self, target_steps=10000):
        self.target_steps = target_steps

    def track_steps(self, steps):
        return f"👣 Ви пройшли {steps} з {self.target_steps} кроків."


# МНОЖИННЕ УСПАДКУВАННЯ: беремо фішки обох класів
class SmartWatch(Clock, FitnessTracker):
    def __init__(self, time_format, target_steps, model_name):
        # Як ініціалізувати обох батьків? Викликаємо їхні __init__ напряму:
        Clock.__init__(self, time_format)
        FitnessTracker.__init__(self, target_steps)
        self.model_name = model_name

    def show_summary(self):
        return f"⌚ Годинник {self.model_name} готовий до роботи!"


# Створюємо об'єкт смарт-годинника
my_watch = SmartWatch("24h", 8000, "Apple Watch")

# Об'єкт має доступ до методів ОБОХ батьків:
print(my_watch.show_summary())  # Власний метод: ⌚ Годинник Apple Watch готовий до роботи!
print(my_watch.show_time())     # Метод від Clock: ⏰ Зараз котрась година...
print(my_watch.track_steps(5400)) # Метод від FitnessTracker: 👣 Ви пройшли 5400...
