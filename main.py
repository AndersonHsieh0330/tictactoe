##3X3 tictactoe
##0 -> empty
##1 -> X
##2 -> O

###################### dynamic variables ##########################
Game_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player1_x = ""
player1_y = ""
player2_x = ""
player2_y = ""

###################### condition booleans #########################
player1_win = False
player2_win = False
is_done = False
is_player1s_term = True


##################### Helper Functions ############################
def print_board(board):
    for row in range(3):
        for column in range(3):
            if board[(3 * row) + column] == 0:
                print("#", end="")
            elif board[(3 * row) + column] == 1:
                print("X", end="")
            else:
                print("O", end="")
        print("")


def get_coordinates(x, y):
    return (3 * y) + x


def check_win(board):
    global is_done
    global player1_win
    global player2_win

    # As long as there is one block that is 0, game is not tie
    is_done = True
    for i in range(len(board)):
        if board[i] == 0:
            is_done = False
            break

    ##there are six ways to win and we'll have to check for each
    if [board[0], board[1], board[2]] == [1, 1, 1] \
            or [board[3], board[4], board[5]] == [1, 1, 1] \
            or [board[6], board[7], board[8]] == [1, 1, 1] \
            or [board[0], board[3], board[6]] == [1, 1, 1] \
            or [board[1], board[4], board[7]] == [1, 1, 1] \
            or [board[2], board[5], board[8]] == [1, 1, 1] \
            or [board[0], board[4], board[8]] == [1, 1, 1] \
            or [board[2], board[4], board[6]] == [1, 1, 1]:
        is_done = True
        player1_win = True
    elif [board[0], board[1], board[2]] == [2, 2, 2] \
            or [board[3], board[4], board[5]] == [2, 2, 2] \
            or [board[6], board[7], board[8]] == [2, 2, 2] \
            or [board[0], board[3], board[6]] == [2, 2, 2] \
            or [board[1], board[4], board[7]] == [2, 2, 2] \
            or [board[2], board[5], board[8]] == [2, 2, 2] \
            or [board[0], board[4], board[8]] == [2, 2, 2] \
            or [board[2], board[4], board[6]] == [2, 2, 2]:
        is_done = True
        player2_win = True


def set_coordinates(x, y):
    global Game_board
    global is_player1s_term
    if is_player1s_term:
        Game_board[(get_coordinates(x, y))] = 1
        is_player1s_term = False
    else:
        Game_board[(get_coordinates(x, y))] = 2
        is_player1s_term = True

############################################################################

###################### Game execution starts here ##########################
print("\nWelcome to Tictactoe, coordinates starts from (1,1) to (3,3), ")

while is_done == False:

    print("--------------------------------------------------------------------")
    print_board(Game_board)

    if is_player1s_term:
        player1_x = int(input("player 1(X) please enter x coordinate(enter a single number): ")) - 1
        player1_y = int(input("player 1(X) please enter y coordinate(enter a single number): ")) - 1
        if 0 < (player1_x+1) < 4 and 0 < (player1_y+1) < 4:
            if Game_board[(get_coordinates(player1_x, player1_y))] == 0:
                set_coordinates(player1_x, player1_y)
            else:
                print("This blocks been taken, choose another one")
        else:
            print("Coordinates out of bounds, try another one")
    else:
        player2_x = int(input("player 2(O) please enter x coordinate(enter a single number): ")) - 1
        player2_y = int(input("player 2(O) please enter y coordinate(enter a single number): ")) - 1
        if 0 < (player2_x+1) < 4 and 0 < (player2_y+1) < 4:
            if Game_board[(get_coordinates(player2_x, player2_y))] == 0:
                set_coordinates(player2_x, player2_y)
            else:
                print("This blocks been taken, choose another one")
        else:
            print("Coordinates out of bounds, try another one")

    check_win(Game_board)
    print("--------------------------------------------------------------------\n")


print("--------------------------------------------------------------------")
print_board(Game_board)
if player1_win:
    print("Congrats! Player 1(X) wins!")
elif player2_win:
    print("Congrats! Player 2(O) wins!")
else:
    print("Tie game, no one wins")
print("--------------------------------------------------------------------")

###################################################################################
