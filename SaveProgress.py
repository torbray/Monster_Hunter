import PlayerClass
import MonsterClass
import NPCClass
import ItemClass
import GameBoard
import pickle
import CombatSystem


def checkEncounters():
    # This function checks for any encounters on the board between the player/monster/item.

    # --- Check NPC encounters --- #
    if PlayerClass.char.position == NPCClass.the_trader.position:
        GameBoard.theBoard[NPCClass.the_trader.position] = NPCClass.the_trader.symbol
    else:
        GameBoard.theBoard[NPCClass.the_trader.position] = NPCClass.the_trader.hidden

    if PlayerClass.char.position == NPCClass.the_healer.position:
        GameBoard.theBoard[NPCClass.the_healer.position] = NPCClass.the_healer.symbol
    else:
        GameBoard.theBoard[NPCClass.the_healer.position] = NPCClass.the_healer.hidden

    # --- Check item encounters --- #
    for i in ItemClass.on_board_items:
        if not i.found:
            if PlayerClass.char.position == i.position:
                i.found = True
                PlayerClass.char.add_item(i)

    # --- Check monster encounters --- #
    # If an orc is found, leave a symbol on the board
    for orc in MonsterClass.army_of_orcs:
        if orc.found:
            GameBoard.theBoard[orc.position] = orc.symbol
        if orc.defeated:
            if PlayerClass.char.position == orc.position:
                GameBoard.theBoard[orc.position] = PlayerClass.char.name
            else:
                GameBoard.theBoard[orc.position] = " "

    # --- Check Boss encounter --- #
    if not MonsterClass.orc_boss.defeated and MonsterClass.orc_boss.position == PlayerClass.char.position:
        GameBoard.theBoard[MonsterClass.orc_boss.position] = MonsterClass.orc_boss.symbol


def makeSave():
    inventory_list = []
    for obj in PlayerClass.char.inventory:
        inventory_list.append(obj)

    save_dict = {
        # --- Player --- #
        "player_pos": PlayerClass.char.position,
        "player_inventory": inventory_list,
        "player_eq": PlayerClass.char.equipped_items,
        "player_hp": PlayerClass.char.hp,
        "player_gold": PlayerClass.char.gold,
        "player_xp": PlayerClass.char.xp,
        "player_lvl": PlayerClass.char.level,
        "player_def": PlayerClass.char.defence,
        "player_str": PlayerClass.char.strength,
        # --- NPC --- #
        "trader_pos": NPCClass.the_trader.position,
        "trader_found": NPCClass.the_trader.found,
        "healer_pos": NPCClass.the_healer.position,
        "healer_found": NPCClass.the_healer.found,
        # --- Items --- #
        "board_items": ItemClass.on_board_items
    }
    # --- Monsters (1 - 9) --- #
    for i in range(0, 9):
        save_dict[f'monster{i + 1}'] = army_of_orcs[i]

    pickle.dump(save_dict, open("save.p", "wb"))


def loadSave():
    load_dict = pickle.load(open("save.p", "rb"))

    # --- Player --- #
    # First reset old position to -> " "
    GameBoard.theBoard[PlayerClass.char.position] = " "
    # Now the position is updated
    PlayerClass.char.position = load_dict['player_pos']
    # Now place the player
    GameBoard.theBoard[PlayerClass.char.position] = PlayerClass.char.name

    PlayerClass.char.inventory = load_dict['player_inventory']
    PlayerClass.char.equipped_items = load_dict['player_eq']
    PlayerClass.char.hp = load_dict['player_hp']
    PlayerClass.char.gold = load_dict['player_gold']
    PlayerClass.char.xp = load_dict['player_xp']
    PlayerClass.char.lvl = load_dict['player_lvl']
    PlayerClass.char.defence = load_dict['player_def']
    PlayerClass.char.strength = load_dict['player_str']

    # --- NPC --- #
    # Set Found
    NPCClass.the_trader.found = load_dict['trader_found']
    # Now the position is updated
    NPCClass.the_trader.position = load_dict['trader_pos']

    NPCClass.the_healer.found = load_dict['healer_found']
    NPCClass.the_healer.position = load_dict['healer_pos']

    # --- Monsters --- #
    MonsterClass.army_of_orcs = []

    # Separate all monsters
    for i in range(1, 10):
        loaded = load_dict[f'monster{i}']
        MonsterClass.army_of_orcs += [MonsterClass.Monster("Bald Orc", "m", loaded.position, " ", loaded.found, loaded.hp, 32, 2, loaded.defeated, MonsterClass.gen_orc_gold(), 49)]

    # Place saved monsters on the board
    for monster in MonsterClass.army_of_orcs:
        if monster.found:
            GameBoard.theBoard[monster.position] = monster.symbol
        else:
            GameBoard.theBoard[monster.position] = monster.hidden

    # --- Items --- #
    # First reset on_board_items
    ItemClass.on_board_items = []
    GameBoard.theBoard[ItemClass.leather_cap.position] = " "
    # If item is already found, pass, else add the item to on_board_items, replace on the board and make hidden
    for i in load_dict['board_items']:
        if not i.found:
            ItemClass.on_board_items.append(i)
            GameBoard.theBoard[i.position] = i.hidden

    checkEncounters()

    # Finally draw the board
    GameBoard.draw_board(GameBoard.theBoard)
