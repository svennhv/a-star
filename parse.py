#parser

from grid import *

def get_board(number):
    try:
        with open("boards/board-"+str(number)+".txt") as f:
            board = f.read();
    except FileNotFoundError:
        print("\n*** BOARD NOT FOUND!***\n")
        return
    return board

def parse_board(board):
    boardAsList = convert_to_list(board)
    grid = SquareGrid(len(boardAsList[0]), len(boardAsList)) # simple for loop, cound before newline, count number of newlines

    start = (0,0)
    goal = (0,0)
    # double for-loop, use enumerate -
    for tile in board:
        if tile == "#": # goal
           # grid.walls.add(
           break
    return board

def convert_to_list(board):
    return board.splitlines()


def parse_weighted_board(board):
    for tile in board:
        if tile == "B": # goal
            tile = Z
        if tile == "w":
            tile = ""
    return board
