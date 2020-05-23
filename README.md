# Monster_Hunter - Development branch (most up to date)
To start the game **_you will need both Monster_Hunter.py and combatsystem.py in the same directory._** Then simply open your favourite command terminal and navigate to the directory of the Monster_Hunter.py. Once in the correct directory use:

    python Monster_Hunnter.py
          
# Development Start
The player starts with a basic sword already equipped ~~(does not appear in inventory -> see bugs.md)~~.
For testing purposes the monster is always on position 1 in the grid **(first row - second column or simply just go 'right' once.)**

If the player encounters a monster it can choose to fight or flee. If the player picks to fight, a choice between roll or flee appears. Flee is self explanatory, fight on the other hand starts the battle where the player and monster take turns in rolling the dice. Each time a dice is rolled, damage is calculated, dealt to the opposing party and the player is informed of how much hp the monster has left as well as how much hp the player has left. After each roll the player can flee or keep rolling until the monster or the player has 0 hp. 

For testing purposes time.sleep() has been commented out to speed up the process.
