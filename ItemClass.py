class Item:
    # The item class defines an item name, type, whether it is hidden on the board and its position

    def __repr__(self):
        return self.name

    def __init__(self, name, i_type, hidden, position, attack, defence):
        self.name = name
        self.i_type = i_type
        self.hidden = hidden
        self.position = position
        self.attack = attack
        self.defence = defence


# Create an item a sword and place it in player inventory
wooden_stick = Item("Wooden stick", "Sword", " ", None, 5, 0)
