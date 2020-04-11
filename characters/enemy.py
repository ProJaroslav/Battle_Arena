from characters.character import character
from arena.dice import dice

class enemy(character):
    def __init__ (self, name, health, life, attack, defense):
        super().__init__(name, health, life)
        self.attack = attack
        self.defense = defense


    def __repr__(self):
        return repr("You are facing a warrior named " + self.name + " with " + str(self.health) + " HP, " + str(self.attack) + " attack, and " + str(self.defense) + " defense")


    def fight(self, target):
        throw = dice.throw_dice()
        damage_done = self.attack + throw - target.defense
        if damage_done >-1:
            target.health = target.health - (self.attack + throw - target.defense)
        else:
            damage_done = 0
        return (throw, damage_done)
