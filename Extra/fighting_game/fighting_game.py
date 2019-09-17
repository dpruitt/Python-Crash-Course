import random

class Character:

    def __init__(self, name, hitpoints, strength):
        self.name = name
        self.hitpoints = hitpoints
        self.strength = strength

    def is_dead(self):
        return self.hitpoints <= 0

    def attack(self, target):
        print(f"{self.name} is attacking {target.name}")
        damage = self.strength * random.randrange(1,10)
        target.take_damage(damage)

    def take_damage(self, damage):
        self.hitpoints = self.hitpoints - damage
        print(f"{self.name} took {damage} damage")
        if self.is_dead():
            print(f"{self.name} is ded. F")

    def __repr__(self):
        return f"{self.name} has {self.hitpoints} health"


class Darryl(Character):

    def __init__(self):
        super().__init__("Darryl", 9000, 100)

    def attack(self, target):
        multiplier = random.randrange(1, 10)
        damage = self.strength * multiplier
        if multiplier % 2 == 0:
            print(f"That retard {self.name} is attacking himself")
            self.take_damage(damage)
        else:
            print(f"{self.name} is attacking {target.name}")
            target.take_damage(damage)



enemies = [Character("Centaur", 100, 5), Character("Minotaur", 120, 3), Character("Chicken", 20, 1), Character("Ford Taurus", 500, 2), Darryl()]
player = Character("player", 100, 3)

enemy = Darryl()

while not player.is_dead() and not enemy.is_dead():
    enemy.attack(player)
    player.attack(enemy)

print(f"Player fought {enemy.name}")
print(player.hitpoints)
print(enemy.hitpoints)

