class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    # represent a graph as a dictionary of vertices mapping labels to edges
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        else:
            pass
    
    def add_edge(self, vertex_from, vertex_to):
        if vertex_from in self.vertices and vertex_to in self.vertices:
            self.vertices[vertex_from].add(vertex_to)
        else:
            pass

def earliest_ancestor(ancestors, starting_node):
    # make a graph
    graph = Graph()
    for pair in ancestors:
        # add vertex
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # add edges
        graph.add_edge(pair[1], pair[0])

    # traverse the graph BFS
    q = Queue()
    q.enqueue([starting_node])

    max_path_length = 1
    earliest_ancestor = -1


    while q.size() > 0:
        path = q.dequeue()
        node = path[-1]

        # we keep the path if it is longer or 
        if len(path) > max_path_length or len(path) == max_path_length and node < earliest_ancestor:
            earliest_ancestor = node
            max_path_length = len(path)

        for neighbor in graph.vertices[node]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return earliest_ancestor


    # looking for the shortest path between two nodes
    # keep track the length of these path
    # Return where the longest path ends
    # if no parents, return -1
    # if tie, return lowest node number


    