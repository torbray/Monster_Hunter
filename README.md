# Monster_Hunter
__(See Development branch for most up-to-date version of the game. Includes early combat system, character stats, item stats...)__

Text-based RPG played within the command terminal. 

This is a single-player text-based RPG, where the player can hunt a monster.

To start the game simply open your favourite command terminal and navigate to the directory of the Monster_Hunter.py. Once in the correct directory use:

    python Monster_Hunnter.py
    
We start in the main menu of the game, which welcomes the player and defines the objective. It also displays available commands for the main menu.

    Available Commands:

    help     Display help menu
    start    Start the game
    exit     Exit the game

    What would you like to do? >
    
# Help menu:

The help command calls the printHelp() function and its only purpose is to print available menu commands, game commands and             player movement.

    Available Menu Commands:
          "help         Display help menu"
          "start        Start the game"
          "exit         Exit the game"
          
    Available Game Commands:"
          "help         Display help menu"
          "exit         Exit the game"
          "inventory    Check your inventory"
          "up           Move up"
          "down         Move down"
          "left         Move left"
          "right        Move right"

# The board:

The player and the monster are displayed on a 10x10 grid board.

`----------------------------------------
----------------------------------------
----------------------------------------
   |   |   |   |   |   |   |   |   |   |
----------------------------------------
   |   |   |   |   |   |   |   |   |   |
----------------------------------------
   |   |   |   |   |   |   |   |   |   |
----------------------------------------
   |   |   |   |   |   |   |   |   |   |
----------------------------------------
   |   |   |   |   |   |   |   |   |   |
----------------------------------------
   |   |   |   |   |   |   |   |   |   |
----------------------------------------
   |   |   |   |   |   |   |   |   |   |
----------------------------------------
   |   |   |   |   |   |   |   |   |   |
----------------------------------------
   |   |   |   |   |   |   |   |   |   |
----------------------------------------
 P |   |   |   |   |   |   |   |   |   |
----------------------------------------
----------------------------------------
----------------------------------------`
