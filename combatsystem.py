import random
import Monster_Hunter as mh
import time
import sys


def dice_roll():
    # Simple dice roll function
    dice_number = random.randrange(1, 11)
    return dice_number


def attack():
    """
    This function defines the strength of the player hit. It does so by multiplying player strength by the attack
    statistic of the currently equipped weapon. It then multiplies that by the dice_dict value of the player_roll.
    """
    dice_dict = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4, 5: 0.5, 6: 0.6, 7: 0.7, 8: 0.8, 9: 0.9, 10: 1}

    player_roll = dice_roll()
    print(f"You rolled {player_roll} \n")
    # time.sleep(2)

    player_hit = mh.player.strength * mh.player.equipped_items["Weapon"].attack * dice_dict[player_roll]
    return player_hit


def deal_dmg(some_monster, player_hit):
    # The only purpose of this function is to deal damage to some_monster and to print the result.
    some_monster.hp -= player_hit
    print(f"You hit {some_monster.name} for {player_hit} damage... {some_monster.hp}hp remaining \n")
    # time.sleep(4)


def monster_attack(monster):
    # This function is the same as the attack(), but it is used to perform attacks by monsters.
    dice_dict = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4, 5: 0.5, 6: 0.6, 7: 0.7, 8: 0.8, 9: 0.9, 10: 1}

    monster_roll = dice_roll()
    print(f"The monster rolled {monster_roll} \n")
    # time.sleep(2)

    monster_hit = monster.attack * dice_dict[monster_roll]
    mh.player.hp = mh.player.hp - monster_hit
    print(f"You get hit for {monster_hit} damage... {mh.player.hp}hp remaining\n")
    # time.sleep(4)


def battle(monster):
    """
    This function is the core of the combat system. Whenever a fight is to occur, this function gets called.
    As long as the monster or the player are above 0hp, it will keep asking the player to roll the dice or to flee.
    """
    fight = True
    while fight:
        while monster.hp > 0 and mh.player.hp > 0:

            action = input("\nroll/flee? > ")
            if action == "roll":
                print("\nIt's your turn to roll the dice... \n")
                # time.sleep(2)
                player_hit = attack()
                deal_dmg(monster, player_hit)
                monster_attack(monster)

            elif action == "flee":
                print("You run away like a coward!")
                fight = False
                mh.gameAction()

            elif action == "exit":
                sys.exit()

            else:
                print("Unknown command...")

        print("Monster defeated.")
        fight = False
