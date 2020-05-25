import PlayerClass


class Item:
    # The item class defines an item name, type, whether it is hidden on the board and its position

    def __repr__(self):
        return self.name

    def __init__(self, name, i_type, hidden, position, damage, defence):
        self.name = name
        self.i_type = i_type
        self.hidden = hidden
        self.position = position
        self.damage = damage
        self.defence = defence


def showStats():
    # Shows item statistics to the player
    item = input("Lookup item stats for: ").lower()

    if item in item_stats:
        print(f"\n{item_stats[item][0]}: Damage: {item_stats[item][1]} Defence: {item_stats[item][2]}")

    else:
        print("Invalid item.")



# Create items
wooden_stick = Item("Wooden Stick", "Weapon", " ", None, 5, 0)
wooden_shield = Item("Wooden Shield", "Shield", " ", None, 0, 5)

# Item statistics dictionary, hold names, damage and defence stats for an item
item_stats = {
    "wooden stick": [wooden_stick.name, wooden_stick.damage, wooden_stick.defence],
    "wooden shield": [wooden_shield.name, wooden_shield.damage, wooden_shield.defence]
}


def equip():
    # This function allows the user to equip items from inventory to the equipped items dict
    item = input("Which item to equip? ")
    for i in PlayerClass.char.inventory:
        if item != i.name:
            pass
        elif item == i.name:
            type_of_item = i.i_type
            PlayerClass.char.equipped_items[type_of_item] = i
            print(f"\n{i.name} is now equipped")
            PlayerClass.char.inventory.remove(i)
        else:
            print("Invalid item.")


def unequip():
    # This function acts as the opposite to the equip function.
    item = input("Which item to unequip? Helmet/Armour/Weapon/Shield ")
    if item in PlayerClass.char.equipped_items:
        i = PlayerClass.char.equipped_items[item]
        PlayerClass.char.equipped_items[item] = None
        print(f"\n{i.name} is now unequipped")
        PlayerClass.char.inventory.append(i)
    else:
        print("Invalid item.")
