import random
import sys
import combatsystem as cs


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

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print(self.inventory)


class Monster:
    # The monster class defines a name, position and whether the monster is currently hidden on the board

    def __init__(self, name, position, hidden, found, hp, attack,
                 monster_defence):
        self.name = name
        self.position = position
        self.hidden = hidden
        self.found = found
        self.hp = hp
        self.attack = attack
        self.defence = monster_defence


class Item:
    # The item class defines an item name, type, whether it is hidden on the board and its position

    def __repr__(self):
        return self.name

    def __init__(self, name, type, hidden, position, attack, defence):
        self.name = name
        self.type = type
        self.hidden = hidden
        self.position = position
        self.attack = attack
        self.defence = defence


def draw_board(board):
    """
    This function takes board as a parameter, which is a list of empty strings -> ' '. It holds 99 indices.
    This function also checks whether the player encountered a monster and if he did, it changes the position of the
    monster from hidden to monster_name.
    """

    print('----------------------------------------')
    print('----------------------------------------')
    print('----------------------------------------')
    print(
        f' {board[90]} | {board[91]} | {board[92]} | {board[93]} | {board[94]} | {board[95]} | {board[96]} | {board[97]} | {board[98]} | {board[99]} |')
    print('----------------------------------------')
    print(
        f' {board[80]} | {board[81]} | {board[82]} | {board[83]} | {board[84]} | {board[85]} | {board[86]} | {board[87]} | {board[88]} | {board[89]} |')
    print('----------------------------------------')
    print(
        f' {board[70]} | {board[71]} | {board[72]} | {board[73]} | {board[74]} | {board[75]} | {board[76]} | {board[77]} | {board[78]} | {board[79]} |')
    print('----------------------------------------')
    print(
        f' {board[60]} | {board[61]} | {board[62]} | {board[63]} | {board[64]} | {board[65]} | {board[66]} | {board[67]} | {board[68]} | {board[69]} |')
    print('----------------------------------------')
    print(
        f' {board[50]} | {board[51]} | {board[52]} | {board[53]} | {board[54]} | {board[55]} | {board[56]} | {board[57]} | {board[58]} | {board[59]} |')
    print('----------------------------------------')
    print(
        f' {board[40]} | {board[41]} | {board[42]} | {board[43]} | {board[44]} | {board[45]} | {board[46]} | {board[47]} | {board[48]} | {board[49]} |')
    print('----------------------------------------')
    print(
        f' {board[30]} | {board[31]} | {board[32]} | {board[33]} | {board[34]} | {board[35]} | {board[36]} | {board[37]} | {board[38]} | {board[39]} |')
    print('----------------------------------------')
    print(
        f' {board[20]} | {board[21]} | {board[22]} | {board[23]} | {board[24]} | {board[25]} | {board[26]} | {board[27]} | {board[28]} | {board[29]} |')
    print('----------------------------------------')
    print(
        f' {board[10]} | {board[11]} | {board[12]} | {board[13]} | {board[14]} | {board[15]} | {board[16]} | {board[17]} | {board[18]} | {board[19]} |')
    print('----------------------------------------')
    print(
        f' {board[0]} | {board[1]} | {board[2]} | {board[3]} | {board[4]} | {board[5]} | {board[6]} | {board[7]} | {board[8]} | {board[9]} |')
    print('----------------------------------------')
    print('----------------------------------------')
    print('----------------------------------------')


def gameAction():
    """
    This function holds a game action dictionary, which maps valid user inputs to either other functions
    or converts player movement to equivalent integers. For example: If the player wants to move up the board,
    it has to add 10 to the current position of the player, if the player wants to move left it has to minus 1
    from the current position.
    """
    game_action_dict = {
        "help": printHelp, "exit": sys.exit, "inventory": player.show_inventory,
        "up": 10, "down": -10, "left": -1, "right": 1
    }
    valid_move = False
    while not valid_move:
        game_action = input("\n> ")
        if game_action in game_action_dict:
            # Try calling a function, if the action is not a function, catch the exception and pass it to makeMove()
            try:
                game_action_dict[game_action]()
            except TypeError:
                makeMove(game_action_dict[game_action])
                valid_move = True
        else:
            print("Unknown command...")


def checkEncounters():
    # This function checks for any encounters on the board between the player/monster/item.

    if player.position == a_sword.position:
        if a_sword in player.inventory:
            pass
        else:
            print(f"You found a {a_sword.type}!")
            player.add_item(a_sword)
            print(f"{a_sword.name} was added to your inventory.")

    if player.position == monster.position:
        print("\nYou found the monster!")
        monster.found = True

        fight_flee = input("\nDo you want to fight? [y/n] > ")
        if fight_flee == "y":
            theBoard[monster.position] = monster.name
            cs.battle(monster)

        elif fight_flee == "n":
            pass

        else:
            print("You're so scared that you run away.")

    if monster.found:
        theBoard[monster.position] = monster.name


def makeMove(move):
    """
    This function defines movement on the board. When a player makes a move, it first moves the player to the new
    position, because now there are two instances of the player on board, it erases the previous position with
    an empty string -> ' '.

    Once the movements are complete, it updates the player object.player_position with the new pos. It then draws the
    board and loops back to take the gameAction() function to take the player input again.
    """

    # Place the player in a new position
    theBoard[player.position + move] = player.name

    # Reset the current position to empty
    theBoard[player.position] = " "

    # Update player position to the new position
    player.position = player.position + move

    checkEncounters()
    draw_board(theBoard)
    gameAction()


def printHelp():
    print("\nAvailable Menu Commands:\n"
          "help         Display help menu\n"
          "start        Start the game\n"
          "exit         Exit the game\n\n"
          "\nAvailable Game Commands:\n"
          "help         Display help menu\n"
          "exit         Exit the game\n"
          "inventory    Check your inventory\n\n"
          "up           Move up\n"
          "down         Move down\n"
          "left         Move left\n"
          "right        Move right\n")


def startGame():
    draw_board(theBoard)
    gameAction()


def menuAction():
    """
    Hold a dictionary with available commands in the menu of the game
    """
    menu_action_dict = {
        "help": printHelp, "start": startGame, "exit": sys.exit
    }
    while True:
        menu_action = input("What would you like to do? > ")
        if menu_action in menu_action_dict:
            menu_action_dict[menu_action]()
        else:
            print("Unknown command...")


def main():
    print("\nWelcome to the game.\n"
          "Your objective is to find a sword\n"
          "and defeat the monster!\n\n"
          "Available Commands:\n\n"
          "help     Display help menu\n"
          "start    Start the game\n"
          "exit     Exit the game\n")
    menuAction()


# --- Create the board --- #
theBoard = [
    " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ", " ", " ", " "
]

# Create a player and place on position 0
player = Player("P", 0, 100, 3, 5)
theBoard[player.position] = player.name

# Create the monster and place in a random position
random_monster_position = random.randrange(1, 2)
monster = Monster("M", random_monster_position, " ", False, 100, 2, 1)
theBoard[monster.position] = monster.hidden

# Create an item a sword and place it in player inventory
a_sword = Item("Monster Slayer Sword", "Sword", " ", None, 5, 0)
player.equipped_items["Weapon"] = a_sword

if __name__ == '__main__':
    main()
