import random


class InitialStats:

    def base(statpoints):
        statpoints = int(statpoints)

        while statpoints > 0:
            print(f"\nYou have {statpoints} points left to spend.\n")
            print(f"HP: {stats['hp']}")
            print(f"STR: {stats['str']}")
            print(f"ARMOR: {stats['armor']}")
            print(f"DEX: {stats['dex']}")
            print("Select a stat to put points into. HP increases by 10, the rest by 1.\n\n"
                  "HP is how much damage you can take. If you lose all your HP, you lose the game.\n"
                  "STR is how much damage you can do. Damage dealt is between 1 and 10 times your strength.\n"
                  "ARMOR is how much damage is negated. Each point of armor reduces damage by 5%.\n"
                  "DEX is how likely you are to dodge an attack. Each point of DEX increases dodge chance by 5%.\n")
            selection = input("Which stat would you like to put points in? \n (HP, STR, ARMOR, DEX)\n >>  ").lower()
            if not stats.get(selection):
                print('\n\nPlease type in either HP, STR, ARMOR, or DEX.\n\n')
            else:
                stattoalter = selection
                if stattoalter == 'hp':
                    stats["hp"] = stats["hp"] + 10
                    statpoints = statpoints - 1
                else:
                    stats[stattoalter] = stats[stattoalter] + 1
                    statpoints = statpoints - 1


class Character:

    def __init__(self, name, hitpoints, strength, armor, dex):
        self.name = name
        self.hitpoints = hitpoints
        self.strength = strength
        self.armor = armor * 0.05
        self.dex = dex * .05

    def is_dead(self):
        return self.hitpoints <= 0

    def attack(self, target):

        damage = self.strength * random.randrange(1,10)
        print(f"{self.name} is attacking {target.name} for {damage} damage!")
        target.take_damage(int(damage))


    def take_damage(self, damage):
        damage = int(damage - damage * self.armor)
        if random.randrange(1,100) * self.dex < 5:
            self.hitpoints = self.hitpoints - damage
            print(f"{self.name} took {damage} damage")
        elif self.is_dead():
            print(f"{self.name} is ded. F")
        elif random.randrange(1,100) * self.dex >= 5:
            print(f"{self.name} dodges the attack!")

    def __repr__(self):
        return f"{self.name} has {self.hitpoints} health"


class Darryl(Character):

    def __init__(self):
        super().__init__("Darryl", 500, 10, 1, 1)

    def attack(self, target):
        multiplier = random.randrange(1, 10)
        damage = self.strength * multiplier
        if multiplier % 2 == 0:
            self.take_damage(int(damage))
            print(f"That retard {self.name} is attacking himself for {int(damage)}!")
        else:
            print(f"{self.name} is attacking {target.name} for {int(damage)}")
            target.take_damage(int(damage))



print("WELCOME TO HELL\n")
print("Spend your 10 points wisely.\n")
stats = {"hp": 100, 'str': 3, 'armor': 1, 'dex': 1}
InitialStats.base(10)

enemies = [Character("Centaur", 100, 5, 3, 4), Character("Minotaur", 120, 3, 1, 1), Character("Chicken", 20, 2, 0, 10),
           Character("Ford Taurus", 500, 2, 2, 5), Character("Tank", 300, 5, 10, 0), Darryl()]
player = Character("player", stats["hp"], stats['str'], stats['armor'], stats['dex'])


gameon = True
while gameon:
    print("Choose your enemy.\n"
          "The mighty Centaur, a noble and balanced fighter.\n"
          "The Minotaur, a less noble, tankier Centaur.\n"
          "The Chicken, one fast motherfucker.\n"
          "A 2003 Ford Taurus, it's a car that boasts several JDPower and Associates awards for safety.\n"
          "A T-34 Soviet Army Tank, your fists aren't going to do much against it.\n"
          "Or Darryl.\n")
    enemy = int(input("Will you fight: \n"
                  "(1) CENTAUR\n"
                  "(2) MINOTAUR\n"
                  "(3) CHICKEN\n"
                  "(4) TAURUS\n"
                  "(5) TANK\n"
                  "(6) DARRYL\n"
                  ">>  ").lower())
    enemy = enemies[enemy-1]
    enemyhptemp = enemy.hitpoints
    while not player.is_dead() and not enemy.is_dead():
        enemy.attack(player)
        print(f"""Your HP: {int(player.hitpoints)}/{stats["hp"]}""")
        if not player.is_dead():
            player.attack(enemy)
            print(f"Enemy HP: {int(enemy.hitpoints)}")

    if player.is_dead():
        print("You died. Loser.")
    if enemy.is_dead():
        print(f"Player killed {enemy.name}!")
        print(f"Player fought {enemy.name}")
        print(f"""Your HP: {int(player.hitpoints)}/{stats["hp"]}""")
        print(f"Enemy HP: {int(enemy.hitpoints)}")
        yn = input("Continue playing? Y/N\n>>  ").lower()
        if yn == 'y':
            player.hitpoints = stats["hp"]
            print(f"Your current stats: \n"
                  f"HP: {player.hitpoints}\n"
                  f"STR: {stats['str']}\n"
                  f"ARMOR: {stats['armor']}\n"
                  f"DEX: {stats['dex']}\n")
            print('You have earned one stat point. Please select the stat you would like to put it in.')
            InitialStats.base(1)
            enemy.hitpoints = enemyhptemp
        elif yn == 'n':
            print("Thanks for playing this stupid game. ")
            gameon = False
        else:
            print("Please use Y or N")

    else:
        break




