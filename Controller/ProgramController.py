from Models.Warrior import Warrior

class ProgramController:

    def __init_():
        pass
    @staticmethod
    def dice_choice():
        user_input = ""
        checker = True
        while checker == True:
                user_input = input("Choose number of dice sides, type 6 or 10: ")
                if user_input == "6" or user_input == "10":
                    checker == False
                    return user_input
                else:
                    print("wrong input")



    @staticmethod
    def warrior_setname():
        name = input("Type the name of your warrior: ")
        return name


    @staticmethod
    def warrior_upgrade(set_points):
        skill_points = set_points
        health = 0
        attack = 0
        defense = 0
        print("Updrage your warrior: ")
        while skill_points != 0:
            print(f"{skill_points} points left")
            user_input = input("Type health/defense/attack to upgrade: ")
            if user_input == "health":
                health += 1
                skill_points -=1
            elif user_input == "attack":
                attack += 1
                skill_points -=1
            elif user_input == "defense":
                defense += 1
                skill_points -=1
            else:
                print("WRONG INPUT")
        if skill_points == 0:
            print("OUT OF POINTS")
        return health, attack, defense


    @staticmethod
    def next_round():
        checker = False
        go = input("Hit 1 for next round")
        print("***************************************************************")
        while checker == False:
            if go == "1":
                checker == True
                return False
            else:
                print("Wrong input !")
