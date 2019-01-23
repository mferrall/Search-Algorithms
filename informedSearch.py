from PriorityQueue import *

def GreedyFirst(g, origin, frontier = PriorityQueue()):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    if g.is_goal_vertex(origin):
        return True
    
    if g.get_visitNumber() == 0:
        origin.setVisitOrder(g.get_visitNumber())
        g.increment_visitNumber()

    for e in g.incident_edges(origin):    # for every outgoing edge from u
        v = e.opposite(origin)
        if v.visitOrder() == '[]':
            frontier.push(v, windyManhattanDistance(v, g.goalVertex()))
            v.setVisitOrder(g.get_visitNumber())
            g.increment_visitNumber()

    found = False
    while found == False:
        if frontier:       # recursively explore
            topVertex = frontier.pop()
            found = GreedyFirst(g, topVertex[2], frontier)
    
    return found

def windyManhattanDistance(v, goalNode):
    currentPos = to_grid_coord(v.get_id())
    goalPos = to_grid_coord(goalNode.get_id())
    distance = 0

    # if the current potion is to south of the goal node, reflect wind at back
    if(currentPos[0] >= goalPos[0]):
        distance += 1 * abs(currentPos[0] - goalPos[0])
    else:
        distance += 3 * abs(currentPos[0] - goalPos[0])
    
    # Wind does not affect east/west cost
    distance += 2 * abs(currentPos[1] - goalPos[1])
    
    return distance

def to_grid_coord(position):
    column = position % 11
    row = position // 11
    return (row, column)

def a_star_search(g, origin, cost = 0, frontier = PriorityQueue()):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    if g.is_goal_vertex(origin):
        return True
    
    if g.get_visitNumber() == 0:
        origin.setVisitOrder(g.get_visitNumber())
        g.increment_visitNumber()

    for e in g.incident_edges(origin):    # for every outgoing edge from u
        v = e.opposite(origin)
        if v.visitOrder() == '[]':
            frontier.push(v, cost + e.weight() + windyManhattanDistance(v, g.goalVertex()))
            v.setVisitOrder(g.get_visitNumber())
            g.increment_visitNumber()

    found = False
    while found == False:
        if frontier:       # recursively explore
            topVertex = frontier.pop()
            found = a_star_search(g, topVertex[2], topVertex[0] - windyManhattanDistance(topVertex[2], g.goalVertex()), frontier)
    
    return found