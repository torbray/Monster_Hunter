import random


class Monster:
    # The monster class defines a name, position and whether the monster is currently hidden on the board

    def __init__(self, name, symbol, position, hidden, found, hp, attack, defence, defeated):
        self.name = name
        self.symbol = symbol
        self.position = position
        self.hidden = hidden
        self.found = found
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.defeated = defeated


# Generate a random position for the monsters
def gen_ran_pos():
    random_monster_position = random.randrange(1, 99)
    return random_monster_position


# Create 10 orcs on the board
army_of_orcs = [Monster("Bald Orc", "m", gen_ran_pos(), " ", False, 100, 11, 2, False) for _ in range(10)]

orc_boss = Monster("Destroyer Orc", "M", gen_ran_pos(), " ", False, 500, 15, 8, False)
