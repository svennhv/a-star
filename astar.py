import math
from queue import *
from graph import *
from algorithm import *
from grid import *


def astar(number):
    try:
        with open("boards/board-"+str(number)+".txt") as f:
            board = f.read();
    except FileNotFoundError:
        print("\n*** BOARD NOT FOUND!***\n")
        return
    open_list = []
    closed_list = []
    print("board:")
    print(board)

def main():
    ans = ""
    while ans != "q":
        ans = input("### Choose board!\n(eg. 1-1, 2-3, ..) \n(q => quit) \n-------\n >")
        astar(ans)

main()
