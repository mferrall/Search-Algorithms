def DFS(g, origin, goalNode, visitCount = 0, frontier = []):
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