# Родительский/Супер класс
class Hero:
    # Конструктор класса
    def __init__(self, nick, hp, lvl):
        # Атрибуты класса
        self.nick = nick
        self.hero = hp
        self.lvl = lvl

    # методы класса
    def action(self):
        return f"{self.nick} base action activate!!"

# Дочерний класс
class MageHero(Hero):

    def __init__(self, nick, hp, lvl, mp):
        super().__init__(nick, hp, lvl)
        self.mp = mp

    def action(self):
        return f"Это новый метод дочернего класса {self.nick}"

# asuna = Hero("Asuna", 999, 9999)
# mage_kirito = MageHero("Ardager", 100, 1000, 99)

# print(mage_kirito.action())
# print(asuna.action())




class Animal:
    def action(self):
        print(f"Animal action")

class Fly(Animal):
    def action(self):
        super().action()
        print(f"Fly action")

class Swim(Animal):
    def action(self):
        # super().action()
        print(f"Swin action")

class Duck(Fly,Swim):
    def action(self):
        super().action()
        print(f"Dunk action")

donald_duck = Duck()
donald_duck.action()
print(Duck.__mro__)