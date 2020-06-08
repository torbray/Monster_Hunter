# Monster_Hunter Change Log

**Monster_Hunter Dev Change v1.0** 

* Added gold to the game
* Added gold to inventory display
* Changed inventory display
* Player class is now stored as a separate file
* Monster class is now stored as a separate file
* Item class is now stored as a separate file

**Monster_Hunter Dev Change v1.1**

* Game board is now stored as a separate file
* Main file code cleanup
* Player is now able to view item stats given that they are either in the inventory, or equipped

**Monster_Hunter Dev Change v1.2**

* Player is now able to equip/unequip items in the inventory
* Commands "equip", "unequip" added to the available game commands
* Bug fixes
* Changed Combat System diplay to allow more clarity

**Monster_Hunter Dev Change v1.3**

* Added "player stats" as a game command
* Player is now able to check player statistics. Total statistic displays stats including equipped item bonuses. 
* A Mystical Trader NCP added
* Player can now buy or sell items.
* Monsters will now drop a random amount of gold once defeated.

**Monster_Hunter Dev Change v1.4**

* Fixed player stats bug, where bonuses were not taken into account while in combat.
* Added HP bonus to items. Items with the hp bonus, will now increase Players overall health
* The Mystical Trader now has more items for sale.
* The Mystical Trader will now display the stats for all items that he sells as well as the price.
* Added The Healer NPC: Will heal for a small price
* Items can now be classified according to their rarirty: "Normal", "Rare", "Unique".
* Added a boss to the map
* First final objective introduced: Defeat the boss
* Minor bug fixes
* The Mystical Trader sells more items
* Minor bug fixes

**Monster_Hunter Dev Change v1.5**

* Simplified theBoard list
* Added few normal items to be found around the board
* Fixed item stats bug where looking up the Leather Armour breaks the game
* When placing items on the board, each item needed a separate if statement in the Monster_Hunter.py checkEncounters function. This has been replaced with a single for loop that iterates over items in a new list -> on_board_items located in ItemClass.py.

**Monster_Hunter Dev Change v1.6**

* Added player level and xp to PlayerClass
* Added a simple level up function
* Player is now able to pick a statistic to level up
* Adjusted Bald Orc and Destroyer Orc stats to account for items on the board

**Monster_Hunter Dev Change v1.7**

* NPCs will no longer spawn in the same position as monsters
* "save" and "load" commands added to the available game commands
* Players can now save the game progress and load the save at a later time
* Items that are placed on the board at the beginning still need to be updated with the new save/load functionality, for now they are probably duplicated.

**Monster_Hunter Dev Change v1.7.1**

* Items now work properly with the save/load functionality 
* Fixed the healer visibility issue where after a load, the healer if not found before the save, was visible after a load

**Monster_Hunter Dev Change v1.8**

* Added 'load' to available menu commands
* Starting the game will now prompt to create a character. There are 4 different races to pick from. Each race can select 1 of 4 specialties gifting additional bonuses
* Dexterity, Intelligence and Magic added as character statistics
* 'player stats' command will now display new statistics
* New stats added to all items and to the item_stats dictionary

**Monster_Hunter Dev Change v1.8.1**

* Fixed load from main menu by moving SaveProgress.py into Monster_Hunter.py. SaveProgress.py is no longer required
* Player can now level up dex, int and magic
* The above statistics are accounted for when the player is in combat
    * Dexterity increases the chance of avoiding a hit
    * Intelligence ~~increases the chance of rolling a higher dice number~~ will be required to cast spells. Different spells have different intelligence requirements
* Added spells to the game. Given that the spell is in the inventory and player meets intelligence requirement, he can cast a spell instead of a dice roll 
* Fixed a bug where the game wouldn't save and load all player statistics

**Monster_Hunter Dev Change v1.8.2**

* Monster_Hunter.py -> checkEncounters has been simplified. It now uses npcEncounters function to check for... npc encounters :)
* Spells now have a description
* Wizard NPC added. Sells Spells (only 1 for now :( and it's totally over-powered )
* Placing NPCs on cells without monsters is now simplified with loops
* Magic statistic is now accounted for when player is in combat. Magic increases damage from spells
* Blacksmith NPC added. He can upgrade items for a set price. 
* Items now have a level attribute. Can go from +0 all the way to +10

