class Arena():

    def decider(warrior_1, warrior_2):
        if warrior_1.health <= 0:
            warrior_1.life = False
        elif warrior_2.health <= 0:
             warrior_2.life = False
             warrior_1.enemies_killed += 1
