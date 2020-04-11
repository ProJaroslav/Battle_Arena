from characters.character import character
from arena.dice import dice

class user_warrior(character):




    def __init__ (self, name, health, life, attack, defense, level, enemies_killed):
        super().__init__(name, health, life)
        self.attack = attack
        self.defense = defense
        self.level = level
        self.enemies_killed = enemies_killed

    def __repr__(self):
        return repr("You create a warrior named " + self.name + " with " + str(self.health) + " HP, " + str(self.attack) + " attack, and " + str(self.defense) + " defense")

    def fight(self, target):
        throw = dice.throw_dice()
        damage_done = self.attack + throw - target.defense
        if damage_done >-1:
            target.health = target.health - (self.attack + throw - target.defense)
        else:
            damage_done = 0
        return (throw, damage_done)

    def set_warriorname(self):
        while True:
            try:
                input_name = str(input("set the name of your warrior: ").title())
                if input_name.isalpha():
                    self.name = input_name
                    break
                else:
                    raise TypeError
            except TypeError:
                print("Only letters")
                continue

    def set_skills(self, set_points):
        while set_points != 0:
            print(f"Skills points left {set_points}")
            choice = input("Choose your upgrade, type health/attack/defense: ")
            if choice == "health":
                self.health += 1
            elif choice == "defense":
                self.defense += 1
            elif choice == "attack":
                self.attack += 1
            else:
                print("wrong input")
                continue
            set_points -= 1
