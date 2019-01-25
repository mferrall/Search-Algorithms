import heapq

class PriorityQueue:
    """Priority queue data structure used for searches based on some priority value
    """

    def __init__(self):
        # Queue is a list of some object, starts empty
        # Index tracks the number of items that have been added, used to have regular behavior for items with same priority
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        # Pushes a tuptle of priority, the current index value, and object onto the heap
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
    
    def pop(self):
        # Pops the entire tuple from the queue, user must extract object on return, allows tracking of the priority value
        return heapq.heappop(self._queue)