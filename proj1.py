# Project 1
from graph import *
from informedSearch import *
from uninformedSearch import *

# To Solve the Map for BFS UCS, DFS, Greedy Best-First search, A* search, and Iterative deepening search, initialize a graph with edge weights N = 1, E = 2, W = 2, S = 3, starting position in the middle of the graph, and solve using each method
    # To Initialize the graph, create a vertex, edge, and graph data structure
        # To create a vertex, create a class that contains a spot for the  
    # To load the graph weights, call add edge for all edges

def construct_edge_list(row_count, column_count):
  #"""Return the weighted, undirected graph from Figure 14.14 of DSAP."""
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

    print('BFS')
    BFS(board, start_point)
    board.graph_print(column_count)
    board.reset_board()

    print('DFS')
    DFS(board, start_point)
    board.graph_print(column_count)
    board.reset_board()

    print('Progressive Deepening')
    depth_limit = 0
    while (progressive_deepening(board, start_point, depth_limit) == False):
        board.reset_board()
        depth_limit += 1
    print('Level ' + str(depth_limit))
    board.graph_print(column_count)
    board.reset_board()

    print('UCS')
    UCS(board, start_point)
    board.graph_print(column_count)
    board.reset_board()

    print('Greedy')
    greedy_first(board, start_point)
    board.graph_print(column_count)
    board.reset_board()

    print('A*')
    a_star_search(board, start_point)
    board.graph_print(column_count)
    board.reset_board()

if __name__ == '__main__':
    main()

