# class BankAccount:
#     _init_(self, login, password, balance):
#     self.login = login
#     self ._ balance = balance
#     self.password = password

#     def get_balance(self, password): 1 usage
#     if password == self.password:
#     return self ._ balance
#     else:
#     return "Не верный пароль !! "

#     ardager = BankAccount ( login: "ardager",

# print(ardager.get_balance("123321"))
# print(ardager. login)
# print(ardager.password)

# password: "123321",

# balance: 1000)
from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, strength):
        self.name = name
        self.level = level
        self.__health = 100  
        self.strength = strength
    
    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")
    
    def rest(self):
        self.__health += 1  #Доступен только внутри класса Hero
                            # Нельзя напрямую изменить извне: hero.__health вызовет ошибку
                            # Для доступа можно добавить геттер (метод get_health())
        print(f"{self.name} отдыхает")
    
    def get_health(self):
        
        return self.__health
    
    @abstractmethod
    def attack(self):
        pass
class Warrior(Hero):
    def attack(self):
        print(f"Воин {self.name} атакует мечом!")


class Mage(Hero):
    def attack(self):
        print(f"Маг {self.name} использует магию!")


class Assassin(Hero):
    def attack(self):
        print(f"Ассасин {self.name} атакует из-под тишка!")

warrior = Warrior("Saikal", 10, 25)
mage = Mage("The Mage", 5, 15)
assassin = Assassin("The Assassin", 5, 20)

heroes = [warrior, mage, assassin]

for hero in heroes:
    hero.greet()
    hero.attack()
    hero.rest()
    