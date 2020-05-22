# Monster_Hunter
Text-based RPG played within the command terminal.

This is a single-player text-based RPG, which purpose is to practice classes and simple game mechanics.

To start the game simply open your favourite command terminal and navigate to the directory of the Monster_Hunter.py. Once in the correct directory use:

    python Monster_Hunnter.py
    
We start in the main menu of the game, which welcomes the player and defines the objective. It also displayes available commands for the main menu.

    Available Commands:

    help     Display help menu
    start    Start the game
    exit     Exit the game

    What would you like to do? >
    
Help menu:

The help command calls the printHelp() function and its only purpose is to print available menu commands, game commands and             player movement.

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

# Future objectives:
(This list is not in order of any importance)

1. Enhance the item class to provide items with statistics such as attack, defence etc.
2. Enhance the monster class to include statistics such as health, defence, special abilities etc.
3. Enhance the player class to include statistics such as health, special abilities, strength, agility etc.

4. Create more monsters on the board.
5. Allow the player to start with simple equipment.
6. Create a fighting function, which will allow the player to battle monster in a more dynamic way. For example dice rolling.
7. Create more items.
8. Create monster loot.
9. Create NPCs with different functionalities, for example upgrading items.
10. TBC
