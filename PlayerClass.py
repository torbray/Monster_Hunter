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

        self.inventory = []
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
        print(f"{self.inventory}")
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

    def showStats(self):
        print("-----------------------")
        print("--Character Statistic--")
        print("-----------------------")
        print(f"Your base Health: {self.hp}")
        print(f"Your base Attack: {self.strength}")
        print(f"Your base Defence: {self.defence}")
        print("-----------------------")

        # Calculate defence and damage stats from items
        shield = self.equipped_items['Shield']
        try:
            shield_def = shield.defence
        except AttributeError:
            shield_def = 0

        helmet = self.equipped_items['Helmet']
        try:
            helmet_def = helmet.defence
        except AttributeError:
            helmet_def = 0

        chest = self.equipped_items['Chest']
        try:
            chest_def = chest.defence
        except AttributeError:
            chest_def = 0

        weapon = self.equipped_items['Weapon']
        try:
            weapon_dmg = weapon.damage
        except AttributeError:
            weapon_dmg = 0

        print(f"Your Total Health: {self.hp}")
        print(f"Your Total Strength: {self.strength + weapon_dmg}")
        print(f"Your Total Defence: {self.defence + shield_def + helmet_def + chest_def}")
        print("-----------------------")


char = Player("P", 0, 100, 3, 1)
