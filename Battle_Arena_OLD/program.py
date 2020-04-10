
from Models.Dice import Dice
from Controller.ProgramController import ProgramController
from Models.Warrior import Warrior

# def create_dice():
#     user_dice = ProgramController.dice_choice()
#     return user_dice

# def create_enemy():
#     enemy_list = []
#     with open ("enemies.txt", "r") as file:
#         enemy_list = list
#     enemy_from_list = enemy_list[user_warrior.enemies_killed]
#     enemy_split = enemy_from_list("-", E)
#     name, hp, defense, attack = E
#     return name, hp, defense, attack


def choose_enemy(user_level):
    enemy_list = ["Ajax-5-2-2-True-2-1", "Achin-8-3-3-True-2-1", "Arkantos-10-4-4-True-2-1", "DVORAK-15-5-5-True-2-1"]
    enemy_from_list = enemy_list[user_level]
    enemy_name, enemy_hp, enemy_defense, enemy_attack, enemy_life, enemy_level, user_killed =  enemy_from_list.split("-")
    return enemy_name, enemy_hp, enemy_defense, enemy_attack, enemy_life, enemy_level, user_killed

def debug():
    pass

def main():
    warrior_name = ProgramController.warrior_setname()
    warrior_hp, warrior_defense, warrior_attack = ProgramController.warrior_upgrade(10)
    user_warrior = Warrior(warrior_name, warrior_hp + 1, warrior_defense + 1, warrior_attack + 1, True, level = 1, enemies_killed = 0)
    print("You have created a warrior: ")
    user_warrior.display_warrior()
    battle_turn = 0
    enemy_warrior = Warrior("empty", 1, 1, 1, True, 1, 1)

    while user_warrior.life is True:
        if enemy_warrior.life == False:
            battle_turn = 0
            user_warrior.enemies_killed += 1
            print("YOU HAVE BEATEN YOUR OPPONENT AND GAINED 3 SKILL POINTS")
            hp, attack, defense = ProgramController.warrior_upgrade(3 + battle_turn)
            user_warrior.update(hp, attack, defense)
        if battle_turn == 0:
            enemy_name, enemy_hp, enemy_defense, enemy_attack, enemy_life, enemy_level, user_killed = choose_enemy(user_warrior.enemies_killed)
            enemy_warrior = Warrior(enemy_name, enemy_hp, enemy_defense, enemy_attack, enemy_life, enemy_level, user_killed)
            print("++++++++++++++++++++++++++++++++++")
            print("You are facing an enemy:")
            enemy_warrior.display_warrior()

        if ProgramController.next_round() == False:
            print(f"Battle turn: {battle_turn + 1}")
            battle_turn += 1
            user_dice = Dice(6)
            thrown_amount = user_dice.generate_number()
            print(f"\n{user_warrior.name} IS PLAYING: ")
            user_dice.throw(thrown_amount)
            user_warrior.fight(thrown_amount, enemy_warrior)
            print(f"Health of the enemy is: {enemy_warrior.HP}")
            enemy_warrior.life_stat()
            if enemy_warrior.life == "True":
                print(f"\n{enemy_warrior.name} is playing: ")
                print(f"Enemy has thrown: {thrown_amount}")
                enemy_warrior.fight(thrown_amount, user_warrior)
                user_warrior.life_stat()
                print(f"The health of your warrior is: {user_warrior.HP}")



if __name__ == "__main__":
    main()
