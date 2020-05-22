import random
import sys


class Player:
    """
        Player class defines the name, position and whether a player has found the monster.
        The class also holds an inventory for a player.
        There are two methods, one which adds an item to the inventory
        and another which displays the content of the inventory
    """

    def __init__(self, player_name, player_position, player_found_monster):
        self.player_name = player_name
        self.player_position = player_position
        self.player_found_monster = player_found_monster
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print(self.inventory)


class Monster:
    # The monster class defines a name, position and whether the monster is currently hidden on the board

    def __init__(self, monster_name, monster_position, monster_hidden, monster_def, monster_attack):
        self.monster_name = monster_name
        self.monster_position = monster_position
        self.monster_hidden = monster_hidden


class Item:
    # The item class defines an item name, type, whether it is hidden on the board and its position

    def __repr__(self):
        return self.item_name

    def __init__(self, item_name, item_type, item_hidden, item_position):
        self.item_name = item_name
        self.item_type = item_type
        self.item_hidden = item_hidden
        self.item_position = item_position


def draw_board(board):
    """
    This function takes board as a parameter, which is a list of empty strings -> ' '. It holds 99 indices.
    This function also checks whether the player encountered a monster and if he did, it changes the position of the
    monster from hidden to monster_name.
    """

    if player.player_found_monster:
        theBoard[monster.monster_position] = monster.monster_name

    print('----------------------------------------')
    print('----------------------------------------')
    print('----------------------------------------')
    print(f' {board[90]} | {board[91]} | {board[92]} | {board[93]} | {board[94]} | {board[95]} | {board[96]} | {board[97]} | {board[98]} | {board[99]} |')
    print('----------------------------------------')
    print(f' {board[80]} | {board[81]} | {board[82]} | {board[83]} | {board[84]} | {board[85]} | {board[86]} | {board[87]} | {board[88]} | {board[89]} |')
    print('----------------------------------------')
    print(f' {board[70]} | {board[71]} | {board[72]} | {board[73]} | {board[74]} | {board[75]} | {board[76]} | {board[77]} | {board[78]} | {board[79]} |')
    print('----------------------------------------')
    print(f' {board[60]} | {board[61]} | {board[62]} | {board[63]} | {board[64]} | {board[65]} | {board[66]} | {board[67]} | {board[68]} | {board[69]} |')
    print('----------------------------------------')
    print(f' {board[50]} | {board[51]} | {board[52]} | {board[53]} | {board[54]} | {board[55]} | {board[56]} | {board[57]} | {board[58]} | {board[59]} |')
    print('----------------------------------------')
    print(f' {board[40]} | {board[41]} | {board[42]} | {board[43]} | {board[44]} | {board[45]} | {board[46]} | {board[47]} | {board[48]} | {board[49]} |')
    print('----------------------------------------')
    print(f' {board[30]} | {board[31]} | {board[32]} | {board[33]} | {board[34]} | {board[35]} | {board[36]} | {board[37]} | {board[38]} | {board[39]} |')
    print('----------------------------------------')
    print(f' {board[20]} | {board[21]} | {board[22]} | {board[23]} | {board[24]} | {board[25]} | {board[26]} | {board[27]} | {board[28]} | {board[29]} |')
    print('----------------------------------------')
    print(f' {board[10]} | {board[11]} | {board[12]} | {board[13]} | {board[14]} | {board[15]} | {board[16]} | {board[17]} | {board[18]} | {board[19]} |')
    print('----------------------------------------')
    print(f' {board[0]} | {board[1]} | {board[2]} | {board[3]} | {board[4]} | {board[5]} | {board[6]} | {board[7]} | {board[8]} | {board[9]} |')
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
        game_action = input("> ")
        if game_action in game_action_dict:
            # Try calling a function, if the action is not a function, catch the exception and pass it to makeMove()
            try:
                game_action_dict[game_action]()
            except TypeError:
                makeMove(game_action_dict[game_action])
                valid_move = True
        else:
            print("Unknown command...")


def makeMove(move):
    """
    This function defines movement on the board. When a player makes a move, it first moves the player to the new
    position, because now there are two instances of the player on board, it erases the previous position with
    an empty string -> ' '.

    Once the movements are complete, it updates the player object.player_position with the new pos. It then draws the
    board and loops back to take the gameAction() function to take the player input again.
    """

    # Place the player in a new position
    theBoard[player.player_position + move] = player.player_name

    # Reset the current position to empty
    theBoard[player.player_position] = " "

    # Update player position to the new position
    player.player_position = player.player_position + move

    if player.player_position == a_sword.item_position:
        if a_sword in player.inventory:
            pass
        else:
            print(f"You found a {a_sword.item_type}!")
            player.add_item(a_sword)
            print(f"{a_sword.item_name} was added to your inventory.")

    if player.player_position == monster.monster_position:
        player.player_found_monster = True
        if a_sword in player.inventory:
            print(f"You used the {a_sword.item_name} to defeat the monster. You win!")
            sys.exit()
        else:
            print("You found the monster! Find a sword to defeat the monster!")
            theBoard[monster.monster_position] = monster.monster_name

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
player = Player("P", 0, False)
theBoard[player.player_position] = player.player_name

# Create the monster and place in a random position
random_monster_position = random.randrange(1, 99)
monster = Monster("M", random_monster_position, " ")
theBoard[monster.monster_position] = monster.monster_hidden

# Create an item and place it in a random position
random_item_position = random.randrange(1, 99)
# If the position of the item is the same as that of the monster, pick a new position for the item
while random_item_position == random_monster_position:
    random_item_position = random.randrange(1, 9)
a_sword = Item("Monster Slayer Sword", "Sword", " ", random_item_position)

if __name__ == '__main__':
    main()
