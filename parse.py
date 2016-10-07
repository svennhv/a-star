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

def parse_board(board, getStart=False, GetGoal=False):
    boardAsList = convert_to_list(board)
    grid = SquareGrid(len(boardAsList[0]), len(boardAsList)) # simple for loop, cound before newline, count number of newlines

    start = (0,0)
    goal = (0,0)
    row = 0
    coloumn = 0
    # double for-loop, use enumerate -
    for tile in board:
        if tile == "#": # wall
           grid.walls.append((row,coloumn))
        if tile == "A": #start
            start =(row,coloumn)
            if getStart == True:
                return start
        if tile == "B": #goal
            goal == (row,coloumn)
            if GetGoal == True:
                return goal
        coloumn += 1                           #Øker kolonnenr. for hver iterasjon
        if coloumn >= len(boardAsList[0]):      #Øker radnr, og setter kollonne til 0 når kolonnenummer er like lang som kolonnen.
            row += 1
            coloumn = 0
    return board

,

def convert_to_list(board):
    return board.splitlines()

def findWhichRowTileIsIn():

    pass

def findWhichColoumnRileIsIn():

    pass


def parse_weighted_board(board):
    for tile in board:
        if tile == "B": # goal
            tile = Z
        if tile == "w":
            tile = ""
    return board
