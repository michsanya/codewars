# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved,
# wouldn't we? Our goal is to create a function that will check that for us!
#
# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or
# 2 if it is an "O", like so:
#
# [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]
# We want our function to return:
#
# -1 if the board is not yet finished AND no one has won yet (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).
# You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

def is_solved(board):
    set1 = {board[0][0], board[0][1], board[0][2]}
    set2 = {board[1][0], board[1][1], board[1][2]}
    set3 = {board[2][0], board[2][1], board[2][2]}
    set4 = {board[0][0], board[1][0], board[2][0]}
    set5 = {board[0][1], board[1][1], board[2][1]}
    set6 = {board[0][2], board[1][2], board[2][2]}
    set7 = {board[0][0], board[1][1], board[2][2]}
    set8 = {board[0][2], board[1][1], board[2][0]}
    is_x = set1 == {1} or set2 == {1} or set3 == {1} or set4 == {1} or set5 == {1} or set6 == {1} or set7 == {
        1} or set8 == {1}
    is_o = set1 == {2} or set2 == {2} or set3 == {2} or set4 == {2} or set5 == {2} or set6 == {2} or set7 == {
        2} or set8 == {2}
    if is_x:
        return 1
    if is_o:
        return 2
    if (0 in set1) or (0 in set2) or (0 in set3):
        return -1
    return 0


b = [[0, 0, 1],
     [0, 1, 2],
     [2, 1, 0]]
print(is_solved(b))
print(0 in {1, 0})
