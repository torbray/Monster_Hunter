class Player:
    """
        Player class defines the name, position and whether a player has found the monster.
        The class also holds an inventory for a player.
        There are two methods, one which adds an item to the inventory
        and another which displays the content of the inventory
    """

    def __init__(self, name, position, hp, strength, defence):
        self.name = name
        self.position = position
        self.hp = hp
        self.strength = strength
        self.defence = defence

        self.inventory = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.equipped_items = {"Helmet": None,
                               "Chest": None,
                               "Weapon": None,
                               "Shield": None
                               }
        self.gold = 0

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("---------------------")
        print("--Small Leather Bag--")
        print("---------------------")
        print(f"| {self.inventory[0]} |")
        print("---------------------")
        print(f"| {self.inventory[1]} |")
        print("---------------------")
        print(f"| {self.inventory[2]} |")
        print("---------------------")
        print(f"| {self.inventory[3]} |")
        print("---------------------")
        print(f"| {self.inventory[4]} |")
        print("---------------------")
        print(f"| {self.inventory[5]} |")
        print("---------------------")
        print(f"| {self.inventory[6]} |")
        print("---------------------")
        print(f"| {self.inventory[7]} |")
        print("---------------------")
        print(f"| {self.inventory[8]} |")
        print("---------------------")
        print(f"| {self.inventory[9]} |")
        print("---------------------")
        print("------Equipped-------")
        print("---------------------")
        print("       Helmet        \n")
        print(f"       {self.equipped_items['Helmet']}")
        print("---------------------")
        print("       Armour        \n")
        print(f"       {self.equipped_items['Chest']}")
        print("---------------------")
        print("       Weapon        \n")
        print(f"       {self.equipped_items['Weapon']}")
        print("---------------------")
        print("       Shield        \n")
        print(f"       {self.equipped_items['Shield']}")
        print("---------------------")
        print(f"Gold: {self.gold}")


char = Player("P", 0, 100, 3, 5)
