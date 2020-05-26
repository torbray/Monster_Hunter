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
