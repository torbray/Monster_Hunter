import random
import Monster_Hunter as mh
import time
import sys


def dice_roll():
    dice_number = random.randrange(1, 11)
    return dice_number


def attack():
    dice_dict = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4, 5: 0.5, 6: 0.6, 7: 0.7, 8: 0.8, 9: 0.9, 10: 1}
    player_roll = dice_roll()
    print(f"You rolled {player_roll} \n")
    # time.sleep(2)

    player_hit = mh.player.player_damage * mh.player.equipped_items["Weapon"].item_attack * dice_dict[player_roll]
    return player_hit


def deal_dmg(some_monster, player_hit):
    some_monster.monster_hp = some_monster.monster_hp - player_hit
    print(f"You hit {some_monster.monster_name} for {player_hit} damage... {some_monster.monster_hp}hp remaining \n")
    # time.sleep(4)


def monster_attack(monster):
    dice_dict = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4, 5: 0.5, 6: 0.6, 7: 0.7, 8: 0.8, 9: 0.9, 10: 1}
    monster_roll = dice_roll()
    print(f"The monster rolled {monster_roll} \n")
    # time.sleep(2)

    monster_hit = monster.monster_attack * dice_dict[monster_roll]
    mh.player.player_hp = mh.player.player_hp - monster_hit
    print(f"You get hit for {monster_hit} damage... {mh.player.player_hp}hp remaining\n")
    # time.sleep(4)


def battle(monster):
    fight = True
    while fight:
        while monster.monster_hp > 0 and mh.player.player_hp > 0:

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


"""
roll dice for player

Take player attack value * his weapon attack value and store as X

Take monster defence store as Y

Y - X = hit

if you roll 10, it hits with 100% potential

if you roll 1, it hits with 1% potential
"""
