import random
import Monster_Hunter
import PlayerClass
import time
import sys
import GameBoard
import ItemClass


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

    # Hit damage calculation
    player_hit = PlayerClass.char.strength * PlayerClass.char.equipped_items["Weapon"].damage * dice_dict[player_roll]
    return player_hit


def deal_dmg(some_monster, player_hit):
    # The purpose of this function is to apply defensive bonus, deal damage to some_monster and to print the result.
    reduced_hit = player_hit - some_monster.defence
    if reduced_hit <= 0:
        # This prevents the damage from going negative
        reduced_hit = 0

    some_monster.hp -= reduced_hit
    print("-------------------------------------------------")
    print(f"You hit {some_monster.name} for {round(reduced_hit, 2)} damage... {some_monster.name}"
          f" has {round(some_monster.hp, 2)}hp remaining")
    print("-------------------------------------------------")
    # time.sleep(4)


def castSpell(a_spell, monster):
    if a_spell in ItemClass.spell_dict:
        ItemClass.spell_dict[a_spell](monster)


def monster_attack(monster):
    # This function is the same as the attack(), but it is used to perform attacks by monsters.
    dice_dict = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4, 5: 0.5, 6: 0.6, 7: 0.7, 8: 0.8, 9: 0.9, 10: 1}

    monster_roll = dice_roll()
    monster_special_roll = dice_roll()
    print(f"\nThe monster rolled {monster_roll} \n")
    if monster_roll >= 6:
        if monster_special_roll >= 7:
            print("The monster was able to use his special move!")
    # time.sleep(2)
    if monster_special_roll >= 6:
        monster_hit = (monster.attack * dice_dict[monster_roll])+(monster.attack * dice_dict[monster_special_roll])
    else:
        monster_hit = monster.attack * dice_dict[monster_roll]
    reduced_hit = monster_hit - PlayerClass.char.defence

    # --- Decide whether it's a hit or miss (Dexterity) --- ###
    chance_to_avoid = (PlayerClass.char.dexterity / dice_dict[monster_roll]) / 3
    x = random.randint(0, 100)
    if x >= chance_to_avoid:
        pass
    else:
        print("You were able to avoid the attack!")
        reduced_hit = 0
        
    if reduced_hit <= 0:
        reduced_hit = 0


    PlayerClass.char.hp -= reduced_hit
    print("-------------------------------------------------")
    print(f"You get hit for {round(reduced_hit, 2)} damage... You have {round(PlayerClass.char.hp, 2)}hp remaining")
    print("-------------------------------------------------")
    # time.sleep(4)


def battle(monster):
    """
    This function is the core of the combat system. Whenever a fight is to occur, this function gets called.
    As long as the monster or the player are above 0hp, it will keep asking the player to roll the dice or to flee.
    """
    fight = True
    while fight:
        while monster.hp > 0:
            if PlayerClass.char.hp <= 0:
                print("You're dead, game over.")
                sys.exit()
            else:
                action = input("\nDo you want to [roll], use a [spell] or [flee]? > ")
                if action == "roll":
                    print("\nIt's your turn to roll the dice... \n")
                    # time.sleep(2)
                    player_hit = attack()
                    deal_dmg(monster, player_hit)
                    monster_attack(monster)

                elif action == 'spell':
                    cast = True
                    while cast:
                        spell = input("Which spell to cast? > ")
                        for i in PlayerClass.char.inventory:
                            try:
                                if i.name == spell:
                                    if PlayerClass.char.intelligence < i.int_req:
                                        print("You don't have enough intelligence to cast this spell")
                                        battle(monster)
                                    else:
                                        castSpell(spell, monster)
                                        monster_attack(monster)
                                        cast = False
                            except AttributeError:
                                pass

                elif action == "flee":
                    GameBoard.draw_board(GameBoard.theBoard)
                    print("You run away like a coward!")
                    fight = False
                    Monster_Hunter.gameAction()

                elif action == "exit":
                    sys.exit()

                else:
                    print("Unknown command...")

        monster.defeated = True
        print("Monster defeated.")
        PlayerClass.char.gold += monster.gold_loot
        PlayerClass.char.xp += monster.xp
        print(f"You pick up {monster.gold_loot} gold")
        PlayerClass.char.levelUp()
        fight = False
