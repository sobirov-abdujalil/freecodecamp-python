# Lab: Build an RPG Character
class RPGCharacter:
    def __init__(self, name, level=1, health=100):
        self.name = name
        self.level = level
        self.health = health

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        return f"{self.name} took {amount} damage. Health: {self.health}"

    def heal(self, amount):
        self.health = min(100, self.health + amount)
        return f"{self.name} healed {amount}. Health: {self.health}"

hero = RPGCharacter("Archer", level=3)
print(hero.take_damage(30))
print(hero.heal(15))
