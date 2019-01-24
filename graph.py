from collections import OrderedDict

# Custom class that ensures that any nested dictionaries are also ordered
# Maintains the order of edges
class NestedOrderedDict(OrderedDict):
    def __missing__(self, key):
        val = self[key] = NestedOrderedDict()
        return val

class Vertex:

    def __init__(self, input_ID = ""):
        self._id = input_ID
        self._visit_order = '[]'

    def visit_order(self):
        return self._visit_order

    def set_visitOrder(self, inputOrder):
        self._visit_order = inputOrder

    def get_id(self):
        return self._id

    def __str__(self):
        return str(self._id)

    def reset_vertex(self):
        if self._visit_order != '##':
            self._visit_order = '[]'

    __repr__ = __str__
        
    
class Edge:

    def __init__(self, input_origin, input_destination, input_weight):
        self._origin = input_origin
        self._destination = input_destination
        self._weight = input_weight
    
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
    # Simple graph class using an adjacency Map

    def __init__(self):
        self._outgoing = NestedOrderedDict()
        self._visit_number = 0 #tracks the number of nodes that have been added to frontier
        self._goal_vertex = Vertex()

    def set_goal_vertex(self, v):
        self._goal_vertex = v

    def goal_vertex(self):
        return self._goal_vertex
    
    def is_goal_vertex(self, v):
        if self._goal_vertex == v:
            return True
        else:
            return False

    def increment_visitNumber(self):
        self._visit_number += 1
    
    def get_visitNumber(self):
        return self._visit_number

    def _insert_edge(self, input_origin, input_destination, input_weight):
        # Insert and return a new edge from u to v with auxillary element x
        
        e = Edge(input_origin, input_destination, input_weight)
        self._outgoing[input_origin][input_destination] = e

    def reset_board(self):
        self._visit_number = 0
        
        V = self.vertices()
        for v in V:
            v.reset_vertex()

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

        for edge in self._outgoing[v].values():
            yield edge

    def _insert_vertex(self, input_id):
        # insert and return a new Vertex with element x

        v = Vertex(input_id)
        self._outgoing[v] = {}
        return v        

    def get_vertex_at_position(self, pos_number):
        for v in self.vertices():
            if v.get_id() == pos_number:
                return v    

    def graph_print(self, column_count):
        count = 0
        for v in self.vertices():
            print(str(v.visit_order()).zfill(2) + '  ', end = ""),
            count += 1
            if count % column_count == 0:
                print('\n')
        print('\n')
            
    def _initialize_vertices(self, E, wall_position):
        """Make a graph instance based on a sequence of edge tuples.
        Edges can be either of from (origin,destination) or
        (origin,destination,element). Vertex set is presume to be those
        incident to at least one edge.
        vertex labels are assumed to be hashable.
        """

        V = set()
        for e in E:
            V.add(e[0])
            V.add(e[1])

        verts = {}  # map from vertex label to Vertex instance
        for v in V:
            verts[v] = self._insert_vertex(v)
            if verts[v].get_id() in wall_position:
                verts[v].set_visitOrder('##')

        return (verts)        

    def construct_graph_from_edges(self, E, wall_position):
        verts = self._initialize_vertices(E, wall_position) 

        E = self.disconnect_vertices(E, wall_position)
        
        for e in E:
            self._insert_edge(verts[e[0]],verts[e[1]], e[2])
    
    def disconnect_vertices(self, E, wall_position):
        #The cells that the wall is present in

        E = [e for e in E if not e[0] in wall_position]
        E = [e for e in E if not e[1] in wall_position]

        return E

    def __str__(self):
        output = ""

        for v in self._outgoing:
            output = output + str(v) + ":" + str(self._outgoing[v]) + '\n'
        return output

    __repr__ = __str__


            
        