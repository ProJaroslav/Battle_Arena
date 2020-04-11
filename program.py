import json
from arena.arena import Arena
from characters.user_warrior import user_warrior
from characters.enemy import enemy


# def setup():
#     pass

def generate_enemy(index):
    with open("C:/Users/jaros/Programming/CURRENT_PROJECTS/arena_final/characters/characters.json", "r") as list:
        enemy_list = json.load(list)
        enemy_stats = enemy_list[index]
        return enemy(enemy_stats["name"].title(), enemy_stats["health"], enemy_stats["life"],enemy_stats["attack"],enemy_stats["defense"])




def main():
    user = user_warrior("Default",1,True,1,1,1,0)
    enemy_warrior = enemy("Default",1,False,1,1)
    user.set_warriorname()
    user.set_skills(5)
    print ("-" * 100)
    # print(f"You create a warrior named {user.name} with {user.health} HP, {user.attack} attack, and {user.defense} defense")
    print(repr(user))


    while user.life and user.enemies_killed != 4:
        if enemy_warrior.life == False:
            if user.enemies_killed > 0:
                print(f"{enemy_warrior.name} died")
                print ("-" * 100)
                print("New level, upgrade your skills: ")
                user.set_skills(3)
            enemy_warrior = generate_enemy(user.enemies_killed)
            print(repr(enemy_warrior))
            print ("-" * 100)

        input("Press any button to continue: ")
        throw_f, damage_f = user.fight(enemy_warrior)
        print(f"{user.name} threw {throw_f} and deals {damage_f} damage to {enemy_warrior.name}")
        print ("-" * 100)
        user.fight(enemy_warrior)
        Arena.decider(user, enemy_warrior)
        if enemy_warrior.life:
            throw_f, damage_f = enemy_warrior.fight(user)
            print(f"{enemy_warrior.name} threw {throw_f} and deals {damage_f} damage to {user.name}")
            print ("-" * 100)
            Arena.decider(user, enemy_warrior)
    if user.life:
        print("Congrats, you won")
    else:
        print("You lost")










if __name__ == "__main__":
    main()
