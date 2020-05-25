import sys
import ItemClass
import PlayerClass
from MonsterClass import gen_ran_pos
import GameBoard


class Npc:
    def __init__(self, name, symbol, npc_type, position, hidden, found):
        self.name = name
        self.symbol = symbol
        self.npc_type = npc_type
        self.position = position
        self.hidden = hidden
        self.found = found

        self.inventory = []
        self.gold = 0


def tradeItem():
    sell_buy = input("Would you like to [sell] or [buy]? else just [leave]! > ")

    if sell_buy == "exit":
        sys.exit()
    elif sell_buy == "leave":
        pass

    elif sell_buy == "buy":
        print("\nExcellent! Here's what I have:")
        print(f"{the_trader.inventory}\n")

        buy_item = input("Which item would you like to buy? > ")
        for i in the_trader.inventory:
            if i.name == buy_item:
                if PlayerClass.char.gold >= i.value:
                    PlayerClass.char.gold -= i.value
                    PlayerClass.char.inventory.append(i)
                    print("\nItem added to your inventory.")
                else:
                    print("\nYou don't have enough gold for that item.")

            elif i.name != buy_item:
                print("\nI don't have that item.")
            else:
                print("\nI don't know what you're saying")

    elif sell_buy == "sell":
        sell_item = input("\nWhat is it that you would like to sell? > ")
        for i in PlayerClass.char.inventory:
            if i.name == sell_item:
                the_trader.inventory.append(i)
                PlayerClass.char.inventory.remove(i)
                PlayerClass.char.gold += i.value
                print("Pleasure to do business with you.")
                print(f"{i.value} gold added to your sack")
            elif i.name != sell_item:
                print("\nYou don't have that item in your backpack.")
            else:
                print("\nI don't understand.")


# Create an NPC
the_trader = Npc("Mystic Trader", "T", "Trader", gen_ran_pos(), " ", False)
the_trader.gold = 1000
the_trader.inventory.append(ItemClass.iron_sword)
