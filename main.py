# -*- coding: utf-8 -*-
from queue import *
from graph import *
from algorithm import *
from grid import *
from parse import *

# data from main article
DIAGRAM1_WALLS = [from_id_width(id, width=30) for id in [21,22,51,52,81,82,93,94,111,112,123,124,133,134,141,142,153,154,163,164,171,172,173,174,175,183,184,193,194,201,202,203,204,205,213,214,223,224,243,244,253,254,273,274,283,284,303,304,313,314,333,334,343,344,373,374,403,404,433,434]]

print(DIAGRAM1_WALLS)

diagram4 = GridWithWeights(10, 10)
diagram4.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
diagram4.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                       (4, 3), (4, 4), (4, 5), (4, 6),
                                       (4, 7), (4, 8), (5, 1), (5, 2),
                                       (5, 3), (5, 4), (5, 5), (5, 6),
                                       (5, 7), (5, 8), (6, 2), (6, 3),
                                       (6, 4), (6, 5), (6, 6), (6, 7),
                                       (7, 3), (7, 4), (7, 5)]}

came_from, cost_so_far = a_star_search(diagram4, (1, 4), (7, 8))
draw_grid(diagram4, width=3, point_to=came_from, start=(1, 4), goal=(7, 8))
print()
draw_grid(diagram4, width=3, number=cost_so_far, start=(1, 4), goal=(7, 8))




print("\n\nFrom boards!\n")


print([parse_board(get_board("1-1"))])
(

came_from, cost_so_far = a_star_search(parse_board(get_board("1-1")), [parse_board(get_board("1-1"),True,False)], [parse_board(get_board("1-1"),False,True)])
draw_grid(diagram4, width=20,height = 7, point_to=came_from, start=parse_board(get_board("1-1"),True,False), goal=parse_board(get_board("1-1"),False,True))
draw_grid(diagram4, width=20,height = 7, number=cost_so_far, start=parse_board(get_board("1-1"),True,False), goal=parse_board(get_board("1-1"),False,True))



'''

def main():
    ans = ""
    while ans != "q":
        ans = input("### Choose board!\n(eg. 1-1, 2-3, ..) \n(q => quit) \n-------\n >")
        if ans == "q":
            break
        astar(ans)

main()
'''
