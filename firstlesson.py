class Hero:

    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
    
    def action(self):
        return f"{self.name} hero base action"



kirito = Hero("Kirito", 1000, 100)
asuna = Hero("Asuna", 1000, 100)

print(kirito.action())
print(asuna.action)