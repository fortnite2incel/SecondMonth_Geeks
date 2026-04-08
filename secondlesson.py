#Наследование
#Родительский | Супер класс
class Hero:

    def action(self):
        return f"{self.name} base action!"
    
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp


kirito = Hero("Ardger", 100, 1000)

# Дочерний класс

class MageHero(Hero):
    pass

asuna = MageHero("Asuna", 100, 1000, 999)

class Fly:
    def action(self):
        print("fly")

class Swim:

    def action(self):
        print("Swim")

    def action2(self):
        pass

class Animal(Fly, Swim):
    pass


class A:
    
    def action(self):
        print("A")
        
class B(A):
    def action(self):
        super().action()
        print("B")

class C(A):
    def action(self):
        super().action()
        print("C")

class D(B, C):
    def action(self):
        super().action()
        print("D")

test_obj = D()
test_obj.action()

print(D.__mro__)       