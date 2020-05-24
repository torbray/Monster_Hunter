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
    item = input("Lookup item stats for: ").lower()
    while True:
        if item in item_stats:
            if item in PlayerClass.char.equipped_items or item in PlayerClass.char.inventory:
                print(f"\n{item_stats[item][0]}: Damage: {item_stats[item][1]} Defence: {item_stats[item][2]}")
                break
        else:
            print("Invalid item.")
            break


# Create items
wooden_stick = Item("Wooden Stick", "Sword", " ", None, 5, 0)
wooden_shield = Item("Wooden Shield", "Shield", " ", None, 0, 5)

item_stats = {
    "wooden stick": [wooden_stick.name, wooden_stick.damage, wooden_stick.defence],
    # "wooden shield": [wooden_shield.name, wooden_shield.damage, wooden_shield.defence]
}
