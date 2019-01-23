from collections import OrderedDict

# Custom class that ensures that any nested dictionaries are also ordered
# Maintains the order of edges
class NestedOrderedDict(OrderedDict):
    def __missing__(self, key):
        val = self[key] = NestedOrderedDict()
        return val

class Vertex:

    def __init__(self, inputID = ""):
        self._id = inputID
        self._visitOrder = '[]'

    def visitOrder(self):
        return self._visitOrder

    def set_visitOrder(self, inputOrder):
        self._visitOrder = inputOrder

    def get_id(self):
        return self._id

    def __str__(self):
        return str(self._id)

    def resetVertex(self):
        if self._visitOrder != '##':
            self._visitOrder = '[]'

    __repr__ = __str__
        
    
class Edge:

    def __init__(self, inputOrigin, inputDestination, inputWeight):
        self._origin = inputOrigin
        self._destination = inputDestination
        self._weight = inputWeight
    
    def endpoints(self):
        return (self._origin, self._destination)

    def opposite(self, v):
        # Returns the vertex opposite v on this edge
        return self._destination if v is self._origin else self._origin
    
    def weight(self):
        # Returns the element associated with this edge
        return self._weight
    
    def __hash__(self):
        # allows edge to be a map/set key
        return hash( (self._origin, self._destination))

    def __str__(self):
        return '{' + str(self._destination) + ' w= ' + str(self._weight) + '}'

    __repr__ = __str__
    
    
class Graph:
    # Simple graph class using an adjacency list

    def __init__(self, directed = False):
        self._outgoing = NestedOrderedDict()
        self._visitNumber = 0 #tracks the number of nodes that have been added to frontier
        self._goalVertex = Vertex()

    def set_goalVertex(self, v):
        self._goalVertex = v

    def goalVertex(self):
        return self._goalVertex
    
    def is_goal_vertex(self, v):
        if self._goalVertex == v:
            return True
        else:
            return False

    def increment_visitNumber(self):
        self._visitNumber += 1
    
    def get_visitNumber(self):
        return self._visitNumber

    def insert_edge(self, inputOrigin, inputDestination, inputWeight):
        # Insert and return a new edge from u to v with auxillary element x
        
        e = Edge(inputOrigin, inputDestination, inputWeight)
        self._outgoing[inputOrigin][inputDestination] = e

    def reset_board(self):
        self._visitNumber = 0
        
        V = self.vertices()
        for v in V:
            v.resetVertex()

    def vertices(self):
        # Returns the vertices in the graph
        return self._outgoing.keys()
    
    def edges(self):
        # returns a set of all edges of the graph

        result = set()
        for e in self._outgoing.values():
            result.update(e.values())
        return result

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
        print('\n')
            
    def initialize_vertices(self, E):
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
            verts[v] = self.insert_vertex(v)
            if verts[v].get_id() in wallPos:
                verts[v].set_visitOrder('##')

        return (verts)        

    def construct_graph_from_edges(self, E, vertexNumbers):
        verts = self.initialize_vertices(E) 

        E = self.disconnect_Vertices(E, vertexNumbers)
        
        for e in E:
            self.insert_edge(verts[e[0]],verts[e[1]], e[2])
    
    def disconnect_Vertices(self, E, vertexNumbers):
        #The cells that the wall is present in

        E = [e for e in E if not e[0] in vertexNumbers]
        E = [e for e in E if not e[1] in vertexNumbers]

        return E

    def __str__(self):
        output = ""

        for v in self._outgoing:
            output = output + str(v) + ":" + str(self._outgoing[v]) + '\n'
        return output

    __repr__ = __str__


            
        