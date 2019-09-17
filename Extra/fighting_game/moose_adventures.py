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
        damage = self.strength + random.randrange(1,20)
        target.take_damage(damage)

    def take_damage(self, damage):
        self.hitpoints = self.hitpoints - damage
        print(f"{self.name} took {damage} damage")
        if self.is_dead():
            print(f"{self.name} is ded. F")

    def __repr__(self):
        return f"{self.name} has {self.hitpoints} health"


class Ooze(Character):

    def __init__(self):
        super().__init__("Grey Ooze", 100, 1)

    def take_damage(self, damage):
        self.hitpoints = self.hitpoints - damage
        print(f"{self.name} took {damage} damage")
        if player.strength > 0:
            player.strength = player.strength - 1
            print(f"Oh shit, {player.name}'s weapons were corroded!")
        if self.is_dead():
            print(f"{self.name} is ded. F")

class Ford_Taurus(Character):

    def __init__(self):
        super().__init__("The Dread Ford Taurus", 20, 10)

    def take_damage(self, damage):
        if damage < 22:
            print(f"Your attack is useless as the Taurus is built Ford Tough!")
        else:
            self.hitpoints = self.hitpoints - damage
            print(f"{self.name} took {damage} damage")
        if self.is_dead():
            print(f"{self.name} is ded. F")

enemies = [Character("Centaur", 100, 5), Character("Minotaur", 120, 3), Character("Chicken", 20, 1), Ford_Taurus(), Ooze()]
player = Character("Challenger", 300, 5)

fight = 'Y'

while fight != 'N' and not player.is_dead():
    fight = input(f"Would you like to fight in this round? Y/N").upper()
    while fight == 'N':
        print("Well, you survived I guess")
        quit()
    enemy = random.choice(enemies)
    while not player.is_dead() and not enemy.is_dead():
        attack = enemy.attack(player)
        if player.is_dead():
            break
        player.attack(enemy)
        if enemy.is_dead():
            enemies.remove(enemy)
            print(f"You have won this round!")
            print('You still have these enemies left:', enemies)
        print(f"Player fought {enemy.name}")
        print(f"Your HP is: {player.hitpoints}")
        print(f"Your Strength is: {player.strength}")
        if not enemy.is_dead():
            print(f"Enemy still has {enemy.hitpoints}")
    while not enemies:
        print("All have been defeated! You win!")
        quit()


