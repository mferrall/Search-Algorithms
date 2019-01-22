# Project 1
from proj1_graph import *
from dfs import *
from collections import deque

# To Solve the Map for BFS UCS, DFS, Greedy Best-First search, A* search, and Iterative deepening search, initialize a graph with edge weights N = 1, E = 2, W = 2, S = 3, starting position in the middle of the graph, and solve using each method

    # To Initialize the graph, create a vertex, edge, and graph data structure
        # To create a vertex, create a class that contains a spot for the  
    # To load the graph weights, call add edge for all edges


def initialize_vertices(g, E, directed=False):
    """Make a graph instance based on a sequence of edge tuples.
    Edges can be either of from (origin,destination) or
    (origin,destination,element). Vertex set is presume to be those
    incident to at least one edge.
    vertex labels are assumed to be hashable.
    """

    wallPos = (26, 27, 28, 29, 37, 40, 47, 48, 51, 61, 62)

    V = set()
    for e in E:
        V.add(e[0])
        V.add(e[1])

    verts = {}  # map from vertex label to Vertex instance
    for v in V:
        verts[v] = g.insert_vertex(v)
        if verts[v].get_id() in wallPos:
            verts[v].setVisitOrder('##')

    return (g, verts)
    
def construct_Graph_From_Edges(verts, E, g):
    for e in E:
        g.insert_edge(verts[e[0]],verts[e[1]], e[2], e[3])

    return g

def construct_Edge_List():
  #"""Return the weighted, undirected graph from Figure 14.14 of DSAP."""
    E = []

    for row in range(8):
        for column in range(11):
            vertexNumber = column + row * 11

            # West edge
            if column > 0:
                E.append((vertexNumber, vertexNumber - 1, 'West', 2))
            # North edge
            if row > 0:
                E.append((vertexNumber, vertexNumber - 11, 'North', 1))
            # East edge
            if column < 10:
                E.append((vertexNumber, vertexNumber + 1, 'East', 2))
            # South edge
            if row < 7:
                E.append((vertexNumber, vertexNumber + 11, 'South', 3))

    return E

def construct_graph():
    g = Graph()
    E = construct_Edge_List()
    graphAndVertices = initialize_vertices(g, E) 
    g = graphAndVertices[0]
    verts = graphAndVertices[1]

    E = remove_Wall_Edges(E)
    g = construct_Graph_From_Edges(verts, E, g)
    return g

def remove_Wall_Edges(E):
    #The cells that the wall is present in
    wallPos = (26, 27, 28, 29, 37, 40, 47, 48, 51, 61, 62)

    E = [e for e in E if not e[0] in wallPos]
    E = [e for e in E if not e[1] in wallPos]

    return E

def BFS(g, origin, goalNode, visitCount = 0, frontier = []):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    if origin == goalNode:
        return True
    
    if visitCount == 0:
        origin.setVisitOrder(visitCount)
        visitCount += 1 

    for e in g.incident_edges(origin):    # for every outgoing edge from u
        v = e.opposite(origin)
        if v.visitOrder() == '[]':
            frontier.append(v)
            v.setVisitOrder(visitCount)
            visitCount = visitCount + 1

    found = False
    while found == False:
        if frontier:       # recursively explore
            found = DFS(g, frontier.pop(), goalNode, visitCount, frontier)
    
    return found
    
def main():
    board = construct_graph()

    startPoint = board.getVertexAtPosition(49)
    endPoint = board.getVertexAtPosition(10)

    DFS(board, startPoint, endPoint)
    board.boardPrint()

    board.reset_board()
    board.boardPrint()




if __name__ == '__main__':
    main()

