"""Defines functions to traverse a graph using uningormed search algorithms
"""

from collections import deque
from PriorityQueue import *

def DFS(g, origin):
    """Conducts a Depth First Search of the graph.  Goal vertex is stored in the graph object
    Returns true once the object is found.  Returns false if not in graph
    """

    frontier = deque()

    if g.is_goal_vertex(origin):
        return True
    
    if g.get_visitNumber() == 0:
        origin.set_visitOrder(g.get_visitNumber())
        g.increment_visitNumber()

    for e in g.incident_edges(origin):  
        v = e.opposite(origin)
        if v.visit_order() == '[]':
            frontier.append(v)
            v.set_visitOrder(g.get_visitNumber())
            g.increment_visitNumber()

    found = False
    while found == False:
        if frontier:       
            found = DFS(g, frontier.pop())
    
    return found

def BFS(g, origin, frontier = deque()):
    """Conducts a Breadth First Search of the graph.  Goal vertex is stored in the graph object
    Returns true once the object is found.  Returns false if not in graph
    """
    if g.is_goal_vertex(origin):
        return True
    
    if g.get_visitNumber() == 0:
        origin.set_visitOrder(g.get_visitNumber())
        g.increment_visitNumber()

    for e in g.incident_edges(origin):  
        v = e.opposite(origin)
        if v.visit_order() == '[]':
            frontier.append(v)
            v.set_visitOrder(g.get_visitNumber())
            g.increment_visitNumber()

    found = False
    while found == False:
        if frontier:    
            found = BFS(g, frontier.popleft(), frontier)
    
    return found

def progressive_deepening(g, origin, depth_limit, depth = 0):
    """Conducts a Progressive Deepening Search of the graph.  Goal vertex is stored in the graph object
    Returns true once the object is found.  Returns false if not in graph
    """
    frontier = []

    if g.is_goal_vertex(origin):
        return True
    
    if g.get_visitNumber() == 0:
        origin.set_visitOrder(g.get_visitNumber())
        g.increment_visitNumber()

    if depth < depth_limit:
        for e in g.incident_edges(origin):  
            v = e.opposite(origin)
            if v.visit_order() == '[]': 
                frontier.append(v)
                v.set_visitOrder(g.get_visitNumber())
                g.increment_visitNumber()

    found = False
    while found == False and depth < depth_limit and frontier:
        v = frontier.pop()
        found = progressive_deepening(g, v, depth_limit, depth + 1)

    return found

def UCS(g, origin, cost = 0, frontier = PriorityQueue()):
    """Conducts a Uniform Cost Search of the graph.  Goal vertex is stored in the graph object
    Returns true once the object is found.  Returns false if not in graph
    """
    if g.is_goal_vertex(origin):
        return True
    
    if g.get_visitNumber() == 0:
        origin.set_visitOrder(g.get_visitNumber())
        g.increment_visitNumber()

    for e in g.incident_edges(origin):
        v = e.opposite(origin)
        if v.visit_order() == '[]':
            frontier.push(v, cost + e.weight())
            v.set_visitOrder(g.get_visitNumber())
            g.increment_visitNumber()

    found = False
    while found == False:
        if frontier:      
            next_cost = frontier.peek_cost()
            next_vertex = frontier.pop()
            found = UCS(g, next_vertex, next_cost, frontier)
    
    return found