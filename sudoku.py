"""Sudoku by Zane D'Amico"""
from copy import deepcopy

#Currently set to Diabolical Level Sudoku problem from Los Angeles Times
board = [
    [0, 6, 0, 0, 8, 0, 0, 0, 0],
    [9, 0, 2, 0, 0, 0, 0, 0, 5],
    [0, 0, 1, 0, 0, 0, 9, 0, 2],
    [0, 0, 0, 0, 4, 6, 0, 0, 9],
    [0, 0, 0, 7, 0, 9, 0, 0, 0],
    [8, 0, 0, 0, 5, 0, 0, 0, 0],
    [2, 0, 7, 4, 0, 0, 3, 0, 0],
    [4, 0, 0, 0, 0, 0, 7, 0, 6],
    [0, 0, 0, 0, 0, 3, 0, 4, 0]
]

def solve(board):
    """Solves the Sudoku board.

    board - A 9x9 two-dimensional array representing a Sudoku board.
    """

    assert len(board) == 9 and False not in [len(board[i]) == 9 for i in range(len(board))], "Board isn't 9x9."
    loc = next_num(board)
    if loc is None:
        print_board(board)
        return True
    for i in range(1, 10):
        if is_valid(board, i, loc):
            new_board = deepcopy(board)
            new_board[loc[0]][loc[1]] = i
            if solve(new_board):
                return True
    return False

def is_valid(board, num, loc):
    """Returns True if placing num in loc is a valid move.

    board - A 9x9 two-dimensional array representing a Sudoku board.
    num - The number that will be added.
    loc - A tuple containing the location where the number will be added.
    """
    # Check if number is in row
    row = board[loc[0]]
    if num in row:
        return False

    # Check if number is in column
    for i in range(len(board)):
        if board[i][loc[1]] == num:
            return False

    # Check if number is in sub-box
    startx = (loc[0] // 3) * 3
    starty = (loc[1] // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[startx + i][starty + j] == num:
                return False
    return True

def next_num(board):
    """Returns a tuple containing the row and column of the
    next empty box to fill. If all are filled, returns False."""

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_board(board):
    """Prints a Sudoku board."""

    for i in range(len(board)):
        if i % 3 == 0:
            print("---------------------------")
        for j in range(len(board[i])):
            if j == len(board[i]) - 1:
                print(board[i][j], end=" | \n")
            elif (j == 0):
                print(" |", board[i][j], end=" ")
            elif ((j+1) % 3) == 0:
                print(board[i][j], end=" | ")
            else:
                print(board[i][j], end=" ")
    print("---------------------------")

solve(board)
