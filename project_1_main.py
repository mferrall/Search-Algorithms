""" CIS 579 Project 1
In this project, we aim to implement six major search algorithms (BFS, UCS, DFS, Iterative Deepeing, Greedy
Best-First search, and A* search) we learned in class.

Mark Ferrall
1/26/2019
"""
from graph import *
from informedSearch import *
from uninformedSearch import *
import datetime

def construct_edge_list(row_count, column_count):
    # Constructs an list of edges stored as tuples, each edge contains an origin, destination, and edge weight
    # The vertices only connect to edges one position away in a gride in the cardinal directions
    # North edge cost = 1, East = 2, South = 3, West = 2
    E = []
    east_west_cost = 2
    north_cost = 1
    south_cost = 3

    for row in range(row_count):
        for column in range(column_count):
            vertexNumber = column + row * column_count

            # West edge
            if column > 0:
                E.append((vertexNumber, vertexNumber - 1, east_west_cost))
            # North edge
            if row > 0:
                E.append((vertexNumber, vertexNumber - column_count, north_cost))
            # East edge
            if column < column_count - 1:
                E.append((vertexNumber, vertexNumber + 1, east_west_cost))
            # South edge
            if row < row_count - 1:
                E.append((vertexNumber, vertexNumber + column_count, south_cost))

    return E


def main():
    wall_pos = (26, 27, 28, 29, 37, 40, 47, 48, 51, 61, 62)
    column_count = 11
    row_count = 8
    start_pos = 49
    goal_pos = 10
    
    E = construct_edge_list(row_count, column_count)

    board = Graph()
    board.construct_graph_from_edges(E, wall_pos)

    start_point = board.get_vertex_at_position(start_pos)
    board.set_goal_vertex(board.get_vertex_at_position(goal_pos))

    now = datetime.datetime.now()

    print('BFS')
    BFS(board, start_point)
    print(now.strftime("%Y-%m-%d %H:%M"))
    print("uniqname: mdferral")
    board.graph_print(column_count)
    board.reset_board()

    print('DFS')
    DFS(board, start_point)
    print(now.strftime("%Y-%m-%d %H:%M"))
    print("uniqname: mdferral")
    board.graph_print(column_count)
    board.reset_board()

    print('Iterative Deepening')
    depth_limit = 0
    while (progressive_deepening(board, start_point, depth_limit) == False):
        
        print('Level ' + str(depth_limit))
        print(now.strftime("%Y-%m-%d %H:%M"))
        print("uniqname: mdferral")
        board.graph_print(column_count)
        depth_limit += 1
        board.reset_board()

    print('Level ' + str(depth_limit))
    print(now.strftime("%Y-%m-%d %H:%M"))
    print("uniqname: mdferral")
    board.graph_print(column_count)
    board.reset_board()
    
    print('UCS')
    UCS(board, start_point)
    print(now.strftime("%Y-%m-%d %H:%M"))
    print("uniqname: mdferral")
    board.graph_print(column_count)
    board.reset_board()

    print('Greedy')
    greedy_first(board, start_point)
    print(now.strftime("%Y-%m-%d %H:%M"))
    print("uniqname: mdferral")
    board.graph_print(column_count)
    board.reset_board()

    print('A*')
    a_star_search(board, start_point)
    print(now.strftime("%Y-%m-%d %H:%M"))
    print("uniqname: mdferral")
    board.graph_print(column_count)
    board.reset_board()

if __name__ == '__main__':
    main()

