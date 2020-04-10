from Models.Dice import Dice



class Warrior:

    def __init__(self, name, HP, attack, defense, life, level, enemies_killed):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.defense = defense
        self.life = life
        self.level = level
        self.enemies_killed = enemies_killed

    def throw_dice(self):
        thrown_amount = Dice.generate_number()
        return thrown_amount




    def display_warrior(self):
        print(f"Warrior named {self.name} with {self.HP} HP, {self.attack} attack, and {self.defense} defense")
        # return f"a warrior named {self.name} with {self.HP} HP, {self.attack} attack, and {self.defense} defense"

    def display_skills(self):
        print(f"HP: {self.HP}, Attack: {self.attack}, Defense: {self.defense}")

    def life_stat(self):
        if self.HP <= 0:
            self.life = False


    def fight(self, dice_throw, warrior):
        damage = 0
        damage = int(self.attack) + dice_throw - int(warrior.defense)
        warrior.HP = int(warrior.HP) - damage
        print (f"{self.name} attacks. Damage done: {damage} ")
        return damage

    def update(self, HP, attack, defense):
        self.HP += HP
        self.attack += attack
        self.defense += defense
