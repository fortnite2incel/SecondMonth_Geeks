# class Hero:

#     def __init__(self, name, hp, lvl):
#         self.name = name
#         self.hp = hp
#         self.lvl = lvl
    
#     def action(self):
#         return f"{self.name} hero base action"



# kirito = Hero("Kirito", 1000, 100)
# asuna = Hero("Asuna", 1000, 100)

# print(kirito.action())
# print(asuna.action)
"""
📌 Задание
Вам необходимо создать класс Hero со следующими характеристиками
🔹 Атрибуты класса:
name — имя героя
level — уровень героя
health — здоровье героя
strength — сила героя 
🔹 Методы класса:
1️⃣ greet()
Метод должен выводить сообщение:
Привет, я {имя героя}, мой уровень {уровень}
2️⃣ attack()
Метод должен:
выводить сообщение:
{имя героя} наносит удар!
уменьшать силу героя на 1
3️⃣ rest()
Метод должен:
выводить сообщение:
{имя героя} отдыхает…
увеличивать здоровье героя на 1
📌 Дополнительное требование
Создать минимум 2 объекта класса Hero.
Вызвать у каждого объекта все созданные методы.
Проверить, что параметры действительно изменяются.
"""
class Hero: 
    def __init__(self, name, level, health, strength):
        self.name = name 
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"WAZZ GOOD {self.name} your level is {self.level}")
    
    def attack(self):
        self.strength -= 1
        print(f"player {self.name} strikes a blow!")
    

    def rest(self):
        self.health += 1
        print(f"player {self.name} is resting...")
    

martin = Hero("Martin", 10, 100, 1000)
william = Hero("William", 10, 150, 1050)

martin.greet()

if martin.health < 50:
    martin.rest()
else:
    martin.attack()
print(f"Martin's: HP {martin.health}, strength {martin.strength}")

william.greet()

if william.health < 50:
    william.rest
else:
    william.attack()
william.rest()
print(f"William's HP {william.health}, strength {william.strength}")
