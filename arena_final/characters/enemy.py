class character:

    def __init__ (self, name, health, life):
        self.name = name
        self.health = health
        self.life = life

class offensive_unit(character):
    def __init__ (self, name, health, life, attack, defense, level, enemies_killed):
        super().__init__(name, health, life)
        self.attack = attack
        self.defense = defense
        self.level = level
        self.enemies_killed = enemies_killed

        def attack():
            pass


class user_warrior(offensive_unit):
    def update_warrior():
        pass

    def set_warriorname():
        pass

    def set_skills():
        pass



class enemy(offensive_unit):
    pass
