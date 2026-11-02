# ==========================================
# БАТЬКО 1: Мобільний телефон
# ==========================================
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def make_call(self, target_number):
        return f"📞 Дзвонимо з номера {self.phone_number} на номер {target_number}..."

    # Спільна назва методу для перевірки конфлікту (MRO)
    def power_saving_mode(self):
        return "🔋 Режим енергозбереження ТЕЛЕФОНУ: вимикаємо фонові додатки."


# ==========================================
# БАТЬКО 2: Лазерний проєктор
# ==========================================
class Projector:
    def __init__(self, brightness_lumens):
        self.brightness = brightness_lumens

    def project_video(self, movie_title):
        return f"🎬 Проєктуємо фільм '{movie_title}' на стіну з яскравістю {self.brightness} люмен!"

    # Спільна назва методу для перевірки конфлікту (MRO)
    def power_saving_mode(self):
        return "💡 Режим енергозбереження ПРОЄКТОРА: зменшуємо яскравість лампи на 50%."


# ==========================================
# ГІБРИДНИЙ КЛАС (Множинне успадкування)
# ==========================================
# Першим у дужках вказано Phone, другим — Projector
class SmartProjectorPhone(Phone, Projector):
    def __init__(self, phone_number, brightness_lumens, model_name):
        # Явно ініціалізуємо обох батьків
        Phone.__init__(self, phone_number)
        Projector.__init__(self, brightness_lumens)
        self.model_name = model_name

    def show_info(self):
        return f"📱 Гібридний пристрій: {self.model_name}"


# ==========================================
# 🎮 ТЕСТУВАННЯ ГІБРИДА В ДІЇ
# ==========================================
if __name__ == "__main__":
    print("--- 1. Створення гібридного пристрою ---")
    my_device = SmartProjectorPhone("+380991112233", 1200, "LaserPhone X1")
    print(my_device.show_info())

    print("\n--- 2. Перевірка функцій обох батьків ---")
    # Працює метод від класу Phone
    print(my_device.make_call("+380507778899"))
    
    # Працює метод від класу Projector
    print(my_device.project_video("Інтерстеллар"))

    print("\n--- 3. Перевірка конфлікту методів (MRO) ---")
    # Обидва батьки мають метод power_saving_mode(). Хто переможе?
    print(my_device.power_saving_mode())

    print("\n--- 4. Дивимося на точну черговість MRO ---")
    # Виведемо список пріоритетів пошуку методів
    for class_path in SmartProjectorPhone.mro():
        print(f" -> {class_path}")
"""
🔍 Розбір результатів тестування:

1. Гібрид працює ідеально: Наш об'єкт my_device без жодних проблем викликав і make_call() (хоча цей метод написаний тільки в Phone), і project_video() (який є тільки в Projector).
2. Хто переміг у конфлікті? У терміналі ви побачите рядок:
🔋 Режим енергозбереження ТЕЛЕФОНУ: вимикаємо фонові додатки.
Чому так? Тому що в описі класу ми вказали class SmartProjectorPhone(Phone, Projector):. Клас Phone стоїть першим (лівіше). Python знайшов метод power_saving_mode у нього і припинив пошук, навіть не заглядаючи в клас Projector.
3. Якби ми поміняли черговість:
Якщо змінити рядок на class SmartProjectorPhone(Projector, Phone):, то при виклику тієї ж команди пристрій видав би логіку проєктора (зменшив яскравість лампи на 50%).
"""