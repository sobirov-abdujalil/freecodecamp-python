# Lab: Build a Game Character Stats Tracker
class Character:
    def __init__(self, name, strength=10, agility=10, intelligence=10):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

    @property
    def power_level(self):
        return self.strength + self.agility + self.intelligence

    def train(self, stat, amount):
        setattr(self, stat, getattr(self, stat) + amount)
        return f"{self.name} trained {stat}. New value: {getattr(self, stat)}"

hero = Character("Hero", strength=15, agility=12)
print(f"Power: {hero.power_level}")
print(hero.train("strength", 5))
