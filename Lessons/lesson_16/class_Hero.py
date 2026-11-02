# 1. БАТЬКІВСЬКИЙ КЛАС
class Personagem:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        return f"{self.name} робить базову атаку!"

# 3. УСПАДКУВАННЯ та 4. ПОЛІМОРФІЗМ
class Mag(Personagem):
    def attack(self):
        return f"{self.name} вистрілює блискавкою з долонь!"

class Warrior(Personagem):
    def attack(self):
        return f"{self.name} з розгону б'є мечем!"

# 2. СТВОРЕННЯ ОБ'ЄКТІВ
player1 = Mag("Мерлін", 80)
player2 = Warrior("Рагнар", 120)

# Демонстрація поліморфізму: команда одна (.attack()), а результат різний!
party = [player1, player2]

for hero in party:
    print(hero.attack())
