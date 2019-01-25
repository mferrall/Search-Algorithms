from collections import OrderedDict


class NestedOrderedDict(OrderedDict):
    """Custom class that ensures that any nested dictionaries are also ordered
    Maintains the order of edges
    """

    def __missing__(self, key):
        val = self[key] = NestedOrderedDict()
        return val

class Vertex:
    """This is a Vertex object that stores the numbered ID of a vertex, the order a vertex has been
    visited, and operations to support this
    """

    def __init__(self, input_ID = ""):
        # On initializaiton updates the input id to the number provided
        # Visit Order has 3 possible values, a number indicating its visit order, [] to indicated unvisited, or ## to indicate a wall
        self._id = input_ID
        self._visit_order = '[]'

    def visit_order(self):
        # Returns the visit order
        return self._visit_order

    def set_visitOrder(self, inputOrder):
        # Sets visit order to the input
        self._visit_order = inputOrder

    def get_id(self):
        # Returns the vertex's ID
        return self._id

    def __str__(self):
        # Nice prining of a vertex object
        return str(self._id)

    def __hash__(self):
        # Supports using vertex objects as keys in dictionaries
        return hash(id(self))

    def reset_vertex(self):
        # For all non-wall vertices, resets order to []
        if self._visit_order != '##':
            self._visit_order = '[]'

    __repr__ = __str__
        
    
class Edge:
    """Edge class that stores and maintains the origin vertex, destination vertex, and weight of an edge
    Supports retrieval of vertices based on edges
    """
    def __init__(self, input_origin, input_destination, input_weight):
        # On initialization, sets origin node, destination node, and weight equal to arguments
        self._origin = input_origin
        self._destination = input_destination
        self._weight = input_weight
    
    def opposite(self, vert):
        # Returns the vertex opposite vert on the current edge
        return self._destination if vert is self._origin else self._origin
    
    def weight(self):
        # Returns the weight of the edge
        return self._weight
    
    def __hash__(self):
        # supports using edges as a dictionary key
        return hash( (self._origin, self._destination))

    def __str__(self):
        # Returns nicely formatted string for printing
        return '{' + str(self._destination) + ' w= ' + str(self._weight) + '}'

    __repr__ = __str__
    
    
class Graph:
    """Graph class that uses an adjaceny map as its data structure
    Supports creating nodes and edges and methods necessary to traverse the graph in a variety of methods
    """

    def __init__(self):
        # Initializes a graph object with an empty ordered nested dictionary, visit number as 0, and empty vertex object
        self._outgoing = NestedOrderedDict()
        self._visit_number = 0  #tracks the number of nodes that have been added to frontier
        self._goal_vertex = Vertex()

    def set_goal_vertex(self, v):
        # Sets goal vertex equal an input vertex
        self._goal_vertex = v

    def goal_vertex(self):
        # Returns the goal vertex
        return self._goal_vertex
    
    def is_goal_vertex(self, v):
        # Returns true if input vertex is the goal vertex, false otherwise
        if self._goal_vertex == v:
            return True
        else:
            return False

    def increment_visitNumber(self):
        # Increments the visit number as new vertices are added ot the frontier
        self._visit_number += 1
    
    def get_visitNumber(self):
        # Returns the visit number
        return self._visit_number

    def _insert_edge(self, input_origin, input_destination, input_weight):
        # Insert and return a new edge from input_origin to input_destination with weight input_weight
        
        e = Edge(input_origin, input_destination, input_weight)
        self._outgoing[input_origin][input_destination] = e

    def reset_board(self):
        # Resets the graph vertices to unvisited
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

    def incident_edges(self, v):
        # Returns all outoing edges incident to vertex v
        for edge in self._outgoing[v].values():
            yield edge

    def _insert_vertex(self, input_id):
        # insert and return a new Vertex with id of input_id, hashed as an item in dictionary outgoing
        v = Vertex(input_id)
        self._outgoing[v] = {}
        return v        

    def get_vertex_at_position(self, pos_number):
        # searches vertices for a vertex with id of pos_number and returns it
        for v in self.vertices():
            if v.get_id() == pos_number:
                return v    

    def graph_print(self, column_count):
        # Prints the graph visit numbes with column_count columns
        count = 0
        for v in self.vertices():
            print(str(v.visit_order()).zfill(2) + '  ', end = ""),
            count += 1
            if count % column_count == 0:
                print('\n')
        print('\n')
            
    def _initialize_vertices(self, E, wall_position):
        """From a set of edges, gets all unique vertices identified in the edges and
        initializes them as vertices in the graph
        Also initializes the wall segment
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
        """Primary function to construct the graph using an edge list and an input of a wall position.
        Which identifies locations that should not have valid edges in or out of them
        """
        verts = self._initialize_vertices(E, wall_position) 

        E = self.disconnect_vertices(E, wall_position)
        
        for e in E:
            self._insert_edge(verts[e[0]],verts[e[1]], e[2])
    
    def disconnect_vertices(self, E, wall_position):
        # Removes any edges incident on the wall

        E = [e for e in E if not e[0] in wall_position]
        E = [e for e in E if not e[1] in wall_position]

        return E

    def __str__(self):
        # Returns nice string for printhing the outgoing dictionary
        output = ""

        for v in self._outgoing:
            output = output + str(v) + ":" + str(self._outgoing[v]) + '\n'
        return output

    __repr__ = __str__


            
        