from collections import OrderedDict


class NestedOrderedDict(OrderedDict):
    def __missing__(self, key):
        val = self[key] = NestedOrderedDict()
        return val

class Vertex:

    def __init__(self, inputID):
        self._id = inputID
        self._visitOrder = '[]'

    def setVisitOrder(self, inputOrder):
        self._visitOrder = inputOrder

    def visitOrder(self):
        return self._visitOrder

    def get_id(self):
        return self._id

    def __str__(self):
        return str(self._id)

    def resetVertex(self):
        if self._visitOrder != '##':
            self._visitOrder = '[]'

    __repr__ = __str__
        
    
class Edge:
    __slots__ = '_origin','_destination', '_direction', '_weight'

    def __init__(self, inputOrigin, inputDestination, inputDirection, inputWeight):
        self._origin = inputOrigin
        self._destination = inputDestination
        self._weight = inputWeight
        self._direction = inputDirection
    
    def endpoints(self):
        return (self._origin, self._destination)

    def opposite(self, v):
        # Returns the vertex opposite v on this edge
        return self._destination if v is self._origin else self._origin
    
    def element(self):
        # Returns the element associated with this edge
        return self._weight
    
    def __hash__(self):
        # allows edge to be a map/set key
        return hash( (self._origin, self._destination))

    def __str__(self):
        return '{' + self._direction + ' ' + str(self._destination) + ' w= ' + str(self._weight) + '}'

    __repr__ = __str__
    
    
class Graph:
    # Simple graph class using an adjacency list


    def __init__(self, directed = False):
        self._outgoing = NestedOrderedDict()
        # only create second map for directed graph; use alias for undirected
        #self._incoming = {} if directed else self._outgoing

    def insert_edge(self, inputOrigin, inputDestination, inputDirection, inputWeight):
        # Insert and return a new edge from u to v with auxillary element x
        
        e = Edge(inputOrigin, inputDestination, inputDirection, inputWeight)
        self._outgoing[inputOrigin][inputDestination] = e
        #self._incoming[inputDestination][inputOrigin] = e

    def reset_board(self):
        V = self.vertices()

        for v in V:
            v.resetVertex()

    
    def vertex_count(self):
        # Returns the number of vertices in the graph
        return len(self._outgoing)

    def vertices(self):
        # Returns the vertices in the graph
        return self._outgoing.keys()

    def edge_count(self):
        # Returns the number of edges in the graph
        total = sum(len(self._outgoing) for v in self._outgoing)
        return total

        # avoid double counting edges for undirected graph
        #return total if self.is_directed else total // 2
    
    def edges(self):
        # returns a set of all edges of the graph

        result = set()
        for e in self._outgoing.values():
            result.update(e.values())
        return result
    
    def get_edge(self, u, v):
        # Return edge from u to v, or none if not adjacent
        return self._outgoing.get(v)
    
    def degree(self, v, outgoing = True):
      # Returns number of outgoing edges incident to vertex v
      # If the graph is directed, optional parameter used to count incoming edges

      #adj = self._outgoing if outgoing else self._incoming
      adj = self._outgoing
      return len(adj[v])

    def incident_edges(self, v, outgoing = True):
        # Returns all outoing edges incident to vertex v
        # If graph is directed, optional parameter used to request incoming edge

        #adj = self._outgoing if outgoing else self._incoming
        for edge in self._outgoing[v].values():
            yield edge

    def insert_vertex(self, x = None):
        # insert and return a new Vertex with element x

        v = Vertex(x)
        self._outgoing[v] = {}
        #if self.is_directed():
        #    self._incoming[v] = {}
        return v        

    def getVertexAtPosition(self, posNumber):
        for v in self._outgoing.keys():
            if v.get_id() == posNumber:
                return v    

    def boardPrint(self):
        count = 0
        for v in self.vertices():
            print(str(v.visitOrder()).zfill(2) + '  ', end = ""),
            count += 1
            if count % 11 == 0:
                print('\n')
            
    
    def __str__(self):
        output = ""

        for v in self._outgoing:
            output = output + str(v) + ":" + str(self._outgoing[v]) + '\n'
        return output

    __repr__ = __str__


            
        