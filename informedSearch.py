from PriorityQueue import *

def greedy_first(input_graph, origin, frontier = PriorityQueue()):
    """Perform DFS of the undiscovered portion of Graph input_graph starting at Vertex u.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    if input_graph.is_goal_vertex(origin):
        return True
    
    if input_graph.get_visitNumber() == 0:
        origin.set_visitOrder(input_graph.get_visitNumber())
        input_graph.increment_visitNumber()

    for e in input_graph.incident_edges(origin):    # for every edge from origin
        v = e.opposite(origin)
        if v.visit_order() == '[]':
            frontier.push(v, windy_manhattan_distance(v, input_graph.goal_vertex()))
            v.set_visitOrder(input_graph.get_visitNumber())
            input_graph.increment_visitNumber()

    found = False
    while found == False:
        if frontier:       # recursively explore
            top_vertex = frontier.pop()
            found = greedy_first(input_graph, top_vertex[2], frontier)
    
    return found

def windy_manhattan_distance(v, goal_vertex):
    current_pos = to_grid_coord(v.get_id())
    goal_pos = to_grid_coord(goal_vertex.get_id())
    distance = 0

    # if the current potion is to south of the goal node, reflect wind at back
    if(current_pos[0] >= goal_pos[0]):
        distance += 1 * abs(current_pos[0] - goal_pos[0])
    else:
        distance += 3 * abs(current_pos[0] - goal_pos[0])
    
    # Wind does not affect east/west cost
    distance += 2 * abs(current_pos[1] - goal_pos[1])
    
    return distance

def to_grid_coord(position):
    column = position % 11
    row = position // 11
    return (row, column)

def a_star_search(input_graph, origin, cost = 0, frontier = PriorityQueue()):
    """Perform DFS of the undiscovered portion of Graph input_graph starting at Vertex u.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    if input_graph.is_goal_vertex(origin):
        return True
    
    if input_graph.get_visitNumber() == 0:
        origin.set_visitOrder(input_graph.get_visitNumber())
        input_graph.increment_visitNumber()

    for e in input_graph.incident_edges(origin):    # for every outgoing edge from u
        v = e.opposite(origin)
        if v.visit_order() == '[]':
            frontier.push(v, cost + e.weight() + windy_manhattan_distance(v, input_graph.goal_vertex()))
            v.set_visitOrder(input_graph.get_visitNumber())
            input_graph.increment_visitNumber()

    found = False
    while found == False:
        if frontier:       # recursively explore
            top_vertex = frontier.pop()
            found = a_star_search(input_graph, top_vertex[2], top_vertex[0] - windy_manhattan_distance(top_vertex[2], input_graph.goal_vertex()), frontier)
    
    return found