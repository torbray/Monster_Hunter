# Monster_Hunter - Development branch (most up to date)
Text-based RPG played within the command terminal.

This is a single-player text-based RPG, which purpose is to practice classes and simple game mechanics.

To start the game you will need both Monster_Hunter.py and combatsystem.py in the same directory. Then simply open your favourite command terminal and navigate to the directory of the Monster_Hunter.py. Once in the correct directory use:

    python Monster_Hunnter.py
    
We start in the main menu of the game, which welcomes the player and defines the objective. It also displays available commands for the main menu.

    Available Commands:

    help     Display help menu
    start    Start the game
    exit     Exit the game

    What would you like to do? >
    
# Help menu:

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
          
# Start
The player starts with a basic sword already equipped (does not appear in inventory -> see bugs.md).
For testing purposes the monster is always on position 1 in the grid (first row/second column or simply just go 'right' once.)

If the player encounters a monster it can choose to fight or flee. If the player picks to fight, a choice between roll or flee appears. Flee is self explanatory, fight on the other hand starts the battle where the player and monster take turns in rolling the dice. Each time a dice is rolled, damage is calculated, dealt to the opposing party and the player is informed how much hp the monster has left as well as how much hp the player has left. After each roll the player can flee or keep rolling until the monster of the player has 0 hp. 

For testing purposes time.sleep() has been commented out to speed up the process.

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
