# Monster_Hunter
__(See Development branch for most up-to-date version of the game.)__

Text-based RPG played within the command terminal. 

This is a single-player text-based RPG, where the player can hunt monsters, gather loot, buy equipment and defeat the boss.

To start the game simply open your favourite command terminal and navigate to the directory of the Monster_Hunter.py. Once in the correct directory use: (**Note: To start the game, you will need all of the .py files in the same folder.**)

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
          "item stats   View stats of an item"
          "player stats View player statistics"
          "equip        Allows to equip an item"
          "unequip      Allows to unequip and item"
          "inventory    Check your inventory"
          "up           Move up"
          "down         Move down"
          "left         Move left"
          "right        Move right"

# The board:

The player and the monsters are displayed on a 10x10 grid board. Until the player encounters the monster, it remains invisible on the board. This is the same for the NPCs with the Boss being an exception. The Boss is visible from the start.

P - Player
B - Boss
m - Minor monsters
T - Trader NPC
H - Healer NPC

    ----------------------------------------
    ----------------------------------------
    ----------------------------------------
       |   |   |   |   |   |   |   |   | B |
    ----------------------------------------
       |   |   |   |   |   |   |   |   |   |
    ----------------------------------------
     m |   |   |   |   |   |   |   |   |   |
    ----------------------------------------
       |   |   |   |   |   |   |   |   |   |
    ----------------------------------------
       |   |   |   | T | m |   |   |   |   |
    ----------------------------------------
       |   |   | m |   |   |   |   |   |   |
    ----------------------------------------
     m |   |   |   |   | m |   |   |   |   |
    ----------------------------------------
       |   |   |   |   |   |   |   |   |   |
    ----------------------------------------
       |   | m |   |   |   |   |   |   |   |
    ----------------------------------------
     P |   |   |   |   |   | H |   |   |   |
    ----------------------------------------
    ----------------------------------------
    ----------------------------------------
    
 This is the inventory display. "Small Leather Bag" holds unequipped items

    ---------------------
    
    --Small Leather Bag--
    
    ---------------------
    
    [Wooden Shield]
    
    ---------------------
    
    ------Equipped-------
    
    ---------------------
    
           Helmet

           None
    ---------------------
           Armour

           None
    ---------------------
           Weapon

           Wooden Stick
    ---------------------
           Shield

           None
    ---------------------
    Gold: 0

The combat system looks like so

    You found the monster!

    Do you want to fight? [y/n] > y

    roll/flee? > roll

    It's your turn to roll the dice...

    You rolled 8

    -------------------------------------------------
    You hit m for 10.0 damage... m has 90.0hp remaining
    -------------------------------------------------

    The monster rolled 10

    -------------------------------------------------
    You get hit for 10 damage... You have 90hp remaining
    -------------------------------------------------

    roll/flee? >

The player statistics

    -----------------------
    --Character Statistic--
    -----------------------
    Your base Attack: 3
    -----------------------
    Your Total Health: 90
    Your Total Strength: 8
    Your Total Defence: 1
    -----------------------
    
    
# TBC
