import random as random


class Dice:

    def __init__(self, type):
        self.type = type

    # def which_type(self):
    #     print(f"you chose {self.type} sided dice")
    #     return None

    def generate_number(self):
        return random.randint(1, int(self.type))

    def throw(self, thrown_amount):
        print(f"You threw {self.generate_number()}")
        return None

    # def create_dice():
    #     user_dice = ProgramController.dice_choice()
    #     return user_dice
