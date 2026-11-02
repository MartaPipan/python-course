# ==========================================
# 1. БАТЬКІВСЬКИЙ КЛАС ТА ІНКАПСУЛЯЦІЯ
# ==========================================
class Wizard:
    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty
        self.__mana = 100  # ПРИВАТНА змінна (інкапсуляція)

    # ГЕТТЕР через @property (красиве читання)
    @property
    def mana(self):
        return self.__mana

    # СЕТТЕР через .setter (захист даних)
    @mana.setter
    def mana(self, value):
        if value < 0:
            self.__mana = 0
        elif value > 100:
            self.__mana = 100
        else:
            self.__mana = value

    # ПОЛІМОРФНИЙ МЕТОД (базова дія)
    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"{self.name} чаклує базове заклинання!"
        return f"{self.name} виснажений! Немає мани."

    # МАГІЧНИЙ МЕТОД __repr__ (для розробника)
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, faculty={self.faculty!r}, mana={self.mana})"


# ==========================================
# 3. УСПАДКУВАННЯ ТА 4. ПОЛІМОРФІЗМ
# ==========================================
class Alchemist(Wizard):
    # Поліморфізм: Алхімік чаклує інакше і витрачає менше мани
    def cast_spell(self):
        if self.mana >= 5:
            self.mana -= 5
            return f"🧪 {self.name} кидає вибухову колбу з зіллям!"
        return f"🧪 У {self.name} закінчилися інгредієнти."


class DarkWizard(Wizard):
    # Поліморфізм: Темний маг атакує потужно, але витрачає багато мани
    def cast_spell(self):
        if self.mana >= 25:
            self.mana -= 25
            return f"⚡ {self.name} використовує темну магію розряду блискавки!"
        return f"⚡ {self.name} збирає темні сили..."


# ==========================================
# 5. КЛАС-КОНТЕЙНЕР ТА МАГІЧНІ МЕТОДИ
# ==========================================
class MagicSquad:
    def __init__(self, squad_name):
        self.squad_name = squad_name
        self.members = []

    def add_wizard(self, wizard):
        if isinstance(wizard, Wizard):
            self.members.append(wizard)
            print(f"➕ {wizard.name} доданий до загону '{self.squad_name}'")

    # Магічний метод __len__ (рахує кількість магів у загоні)
    def __len__(self):
        return len(self.members)

    # Магічний метод __add__ (об'єднує два загони в один новий через знак +)
    def __add__(self, other):
        if isinstance(other, MagicSquad):
            new_squad = MagicSquad(f"{self.squad_name} + {other.squad_name}")
            new_squad.members = self.members + other.members
            return new_squad
        raise TypeError("Можна об'єднувати тільки загін із загоном!")

    def __repr__(self):
        return f"MagicSquad(name={self.squad_name!r}, members_count={len(self)})"


# ==========================================
# 🎮 ДЕМОНСТРАЦІЯ РОБОТИ ПРОГРАМИ
# ==========================================
if __name__ == "__main__":
    print("--- Створення магів (Класи та Об'єкти) ---")
    harry = Wizard("Гаррі", "Грифіндор")
    harry.mana = 150 # Спрацює захист сеттера, мана стане 100
    
    nicolas = Alchemist("Ніколас", "Хаффлпафф")
    voldemort = DarkWizard("Волдеморт", "Слизерин")

    print(harry)      # Викличе __repr__ -> Wizard(name='Гаррі', faculty='Грифіндор', mana=100)
    print(nicolas)    # Alchemist(name='Ніколас', faculty='Хаффлпафф', mana=100)
    print(voldemort)  # DarkWizard(name='Волдеморт', faculty='Слизерин', mana=100)

    print("\n--- Демонстрація Поліморфізму (Різні атаки) ---")
    print(harry.cast_spell())     # Базове заклинання (-10 мани)
    print(nicolas.cast_spell())   # Колба зілля (-5 мани)
    print(voldemort.cast_spell()) # Блискавка (-25 мани)

    print(f"Поточна мана Волдеморта: {voldemort.mana}") # Перевірка через геттер @property (75)

    print("\n--- Робота з загонами та Магічними методами ---")
    squad_light = MagicSquad("Орден Фенікса")
    squad_light.add_wizard(harry)
    squad_light.add_wizard(nicolas)

    squad_dark = MagicSquad("Смертежери")
    squad_dark.add_wizard(voldemort)

    # Перевірка __len__
    print(f"Кількість магів у світлому загоні: {len(squad_light)}") # Виведе: 2

    # Перевірка магії додавання загонів через оператор + (__add__)
    mega_battle_squad = squad_light + squad_dark
    print(mega_battle_squad) # MagicSquad(name='Орден Фенікса + Смертежери', members_count=3)
"""
🔍 Короткий путівник по коду:

• self.__mana: ніхто ззовні не може написати harry.__mana = -20. Дані сховані в "капсулу".
• @property та @mana.setter: дозволяють перевіряти, щоб мана не перевищувала 100 і не падала нижче 0, навіть якщо ми пишемо harry.mana = 150.
• Alchemist та DarkWizard: успадкували від Wizard вміння мати ім'я та ману, але повністю змінили функцію cast_spell() (поліморфізм).
• len(squad_light): магічно переспрямовує дію на __len__ і рахує магів всередині.
• squad_light + squad_dark: магічно викликає __add__, об'єднуючи списки всередині об'єктів та повертаючи новий загін.
"""