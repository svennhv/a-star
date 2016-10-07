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
    grid = SquareGrid(board.width, board.height) # simple for loop, cound before newline, count number of newlines

    start = (0,0)
    goal = (0,0)
    # double for-loop, use enumerate -
    for tile in board:
        if tile == "#": # goal
            grid.walls.add(
    return board

def convert_to_list(board):
    # make [[row],
            [row],
            [row]
            ]

def parse_weighted_board(board):
    for tile in board:
        if tile == "B": # goal
            tile = Z
        if tile == "w":
            tile = ""
    return board
