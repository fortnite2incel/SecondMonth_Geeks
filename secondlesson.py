#Наследование
#Родительский | Супер класс
# class Hero:

#     def action(self):
#         return f"{self.name} base action!"
    
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp


# kirito = Hero("Ardger", 100, 1000)

# # Дочерний класс

# class MageHero(Hero):
#     pass

# asuna = MageHero("Asuna", 100, 1000, 999)

# class Fly:
#     def action(self):
#         print("fly")

# class Swim:

#     def action(self):
#         print("Swim")

#     def action2(self):
#         pass

# class Animal(Fly, Swim):
#     pass

#diamond problem
# class A:
    
#     def action(self):
#         print("A")
        
# class B(A):
#     def action(self):
#         super().action()
#         print("B")

# class C(A):
#     def action(self):
#         super().action()
#         print("C")

# class D(B, C):
#     def action(self):
#         super().action()
#         print("D")

# test_obj = D()
# test_obj.action()

# print(D.__mro__)       
import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"{self.name}, greetings!!! your level: {self.level}")

    def attack(self):
        print(f"{self.name} hits with {self.strength} damage!")

    def rest(self):
        heal = self.level * 10
        self.health += heal
        print(f"{self.name} resting and healing {heal}. Current health: {self.health}")


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"Воин {self.name} атакует мечом! (Выносливость: {self.stamina})")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"Маг {self.name} кастует заклинание! (Мана: {self.mana})")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"Ассасин {self.name} атакует из-под тишка! (Скрытность: {self.stealth})")


def create_heroes():
    warrior = Warrior("The Warrior", 10, 100, 25, stamina=80)
    mage = Mage("The Mage", 5, 70, 15, mana=120)
    assassin = Assassin("The Assassin", 7, 85, 20, stealth=90)
    return warrior, mage, assassin


def the_winner(player, opponent):
    rules = {
        "Warrior": "Assassin",
        "Assassin": "Mage",
        "Mage": "Warrior"
    }

    if player == opponent:
        return "Ничья!"
    elif rules[player] == opponent:
        return f"{player} победил!"
    else:
        return f"{opponent} победил!"


def all_methods():
    warrior, mage, assassin = create_heroes()

    print(" Warrior")
    warrior.greet()
    warrior.attack()
    warrior.rest()

    print("Mage")
    mage.greet()
    mage.attack()
    mage.rest()

    print("Assassin")
    assassin.greet()
    assassin.attack()
    assassin.rest()

def play_game():
    warrior, mage, assassin = create_heroes()

    hero_choices = {
        "1": ("Warrior", warrior),
        "2": ("Mage", mage),
        "3": ("Assassin", assassin)
    }
    all_heroes = [warrior, mage, assassin]

    print("\nВыберите героя:")
    print("1 — Warrior ")
    print("2 — Mage ")
    print("3 — Assassin ")

    while True:
        choice = input("Введите номер (1/2/3): ")
        if choice in hero_choices:
            player_name, player_hero = hero_choices[choice]
            break
        print("Попробуйте снова")

    opponent = random.choice(all_heroes)
    while opponent == player_hero:
        opponent = random.choice(all_heroes)

    opponent_name = opponent.__class__.__name__

    print(f"\nВы выбрали: {player_name}")
    player_hero.greet()
    player_hero.attack()

    print(f"\nПротивник: {opponent_name}")
    opponent.greet()
    opponent.attack()

    result = the_winner(player_name, opponent_name)
    print(f"\n{player_name} vs {opponent_name}")
    print(f"Результат: {result}")


all_methods()
play_game()

while True:
    again = input("\nХотите сыграть ещё раз? (да/нет): ").lower()
    if again in ["да", "yes"]:
        play_game()
    elif again in ["нет", "no"]:
        print("Покич 👋")
        break
    else:
        print("Так да или нет?")