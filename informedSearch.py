from PriorityQueue import *

def greedy_first(input_graph, origin, frontier = PriorityQueue()):
    """Conducts a greedy first search of the graph.  Goal vertex is stored in the graph object
    Returns true once the object is found
    Uses a manhattan distance that is weighted by directional cost
    """
    if input_graph.is_goal_vertex(origin):
        return True
    
    if input_graph.get_visitNumber() == 0:
        origin.set_visitOrder(input_graph.get_visitNumber())
        input_graph.increment_visitNumber()

    for e in input_graph.incident_edges(origin):  
        v = e.opposite(origin)
        if v.visit_order() == '[]':
            frontier.push(v, windy_manhattan_distance(v, input_graph.goal_vertex()))
            v.set_visitOrder(input_graph.get_visitNumber())
            input_graph.increment_visitNumber()

    found = False
    while found == False:
        if frontier:      
            top_vertex = frontier.pop()
            found = greedy_first(input_graph, top_vertex[2], frontier)
    
    return found

def windy_manhattan_distance(v, goal_vertex):
    # Manhattan distance that is weighted by directional cost
    # Moving north costs 1, south 3, east and west are both 2
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
    # Returns a row, column tuple from an input vertex id
    column = position % 11
    row = position // 11
    return (row, column)

def a_star_cost(cost, e, current_vertex, goal_vertex):
    return cost + e.weight() + windy_manhattan_distance(current_vertex, goal_vertex)


def a_star_search(input_graph, origin, cost = 0, frontier = PriorityQueue()):
    """Conducts an A* search of the graph.  Goal vertex is stored in the graph object
    Returns true once the object is found and the estimated cost of the top vertex in the queue is greater than the current cost
    """
    if input_graph.is_goal_vertex(origin):
        return True
    
    if input_graph.get_visitNumber() == 0:
        origin.set_visitOrder(input_graph.get_visitNumber())
        input_graph.increment_visitNumber()

    for e in input_graph.incident_edges(origin):    
        v = e.opposite(origin)
        if v.visit_order() == '[]':
            next_cost = a_star_cost(cost, e, v, input_graph.goal_vertex())
            frontier.push(v, next_cost)
            v.set_visitOrder(input_graph.get_visitNumber())
            input_graph.increment_visitNumber()

    found = False

    # If vertex is found, keep seraching until estimated cost of top priority item exceeds current cost
    while found == False or (found == True and frontier.peek_cost() < cost): 
        if frontier:     
            top_vertex = frontier.pop()
            found = a_star_search(input_graph, top_vertex[2], top_vertex[0] - windy_manhattan_distance(top_vertex[2], input_graph.goal_vertex()), frontier)
    
    return found