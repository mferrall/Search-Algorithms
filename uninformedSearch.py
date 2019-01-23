from collections import deque
from PriorityQueue import *

def DFS(g, origin, frontier = deque()):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    if g.is_goal_vertex(origin):
        return True
    
    if g.get_visitNumber() == 0:
        origin.set_visitOrder(g.get_visitNumber())
        g.increment_visitNumber()

    for e in g.incident_edges(origin):    # for every outgoing edge from u
        v = e.opposite(origin)
        if v.visitOrder() == '[]':
            frontier.append(v)
            v.set_visitOrder(g.get_visitNumber())
            g.increment_visitNumber()

    found = False
    while found == False:
        if frontier:       # recursively explore
            found = DFS(g, frontier.pop(), frontier)
    
    return found

def BFS(g, origin, frontier = deque()):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    if g.is_goal_vertex(origin):
        return True
    
    if g.get_visitNumber() == 0:
        origin.set_visitOrder(g.get_visitNumber())
        g.increment_visitNumber()

    for e in g.incident_edges(origin):    # for every outgoing edge from u
        v = e.opposite(origin)
        if v.visitOrder() == '[]':
            frontier.append(v)
            v.set_visitOrder(g.get_visitNumber())
            g.increment_visitNumber()

    found = False
    while found == False:
        if frontier:       # recursively explore
            found = BFS(g, frontier.popleft(), frontier)
    
    return found

def progressive_deepening(g, origin, depth_limit, frontier = [], depth = 0):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    if g.is_goal_vertex(origin):
        return True
    
    if g.get_visitNumber() == 0:
        origin.set_visitOrder(g.get_visitNumber())
        g.increment_visitNumber()

    if depth < depth_limit:
        for e in g.incident_edges(origin):    # for every outgoing edge from u
            v = e.opposite(origin)
            if v.visitOrder() == '[]': 
                frontier.append(v)
                v.set_visitOrder(g.get_visitNumber())
                g.increment_visitNumber()

    found = False
    while found == False and depth < depth_limit and frontier:
        v = frontier.pop()
        found = progressive_deepening(g, v, depth_limit, frontier.copy(), depth + 1)

    return found

def UCS(g, origin, cost = 0, frontier = PriorityQueue()):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    if g.is_goal_vertex(origin):
        return True
    
    if g.get_visitNumber() == 0:
        origin.set_visitOrder(g.get_visitNumber())
        g.increment_visitNumber()

    for e in g.incident_edges(origin):    # for every outgoing edge from u
        v = e.opposite(origin)
        if v.visitOrder() == '[]':
            frontier.push(v, cost + e.weight())
            v.set_visitOrder(g.get_visitNumber())
            g.increment_visitNumber()

    found = False
    while found == False:
        if frontier:       # recursively explore
            topVertex = frontier.pop()
            found = UCS(g, topVertex[2], topVertex[0], frontier)
    
    return found