"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

# Vertex
# Identifier (int, name, string, etc)
# list of edges

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if not vertex in self.vertices:
            self.vertices[vertex] = set()
        else:
            print('Warning, vertex exists')
        
        
    def add_edge(self, vertex_from, vertext_to):
        """
        Add a directed edge to the graph.
        TODO: confirm intent is direction should be from v1 to v2
        """
        if vertex_from in self.vertices and vertext_to in self.vertices:
            self.vertices[vertex_from].add(vertext_to)
        else: 
            print('Error, vertex does not exist!')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        found = [starting_vertex]

        while q.size() > 0:
            for vertex in self.vertices[q.queue[0]]:
                if vertex not in found:
                    q.enqueue(vertex)
                    found.append(vertex)
            q.dequeue()
        print(found)
            # TODO: format this more nicely

        


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        """
        below is my solution
        stack, path = [starting_vertex], []
        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.append(vertex)
            for neighbor in self.vertices[vertex]:
                stack.append(neighbor)
        return path
        """
        s = Stack()
        s.push(starting_vertex)
        found = set()
        while s.size() > 0:
            cur = s.pop()
            if cur not in found:
                found.add(cur)
                for next_vert in self.vertices[cur]:
                    s.push(next_vert)
        print(f'DFT {found}')

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = []
        visited.append(starting_vertex)
        print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # my solution
        # explored = []
        # q = [[starting_vertex]]
        # if starting_vertex == destination_vertex:
        #     return starting_vertex
        # while q:
        #     path = q.pop(0)
        #     node = path[-1]
        #     if node not in explored:
        #         next_doors = self.vertices
        #         for next_door in next_doors:
        #             new_path = list(path)
        #             new_path.append(next_door)
        #             q.append(new_path)
        #             if next_door == destination_vertex:
        #                 return new_path
        #         explored.append(node)
        # print("Error, no connection exist")  
        q = Queue()
        q.enqueue([starting_vertex])
        found = []

        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in found:
                if v == destination_vertex:
                    return path
                found.append(v)
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)           
                   
        return None




    def dfs(self, starting_vertex, destination_vertex, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # my solution
        # graph = self.vertices
        # path = path + [starting_vertex]
        # if starting_vertex == destination_vertex:
        #     return [path]
        # if starting_vertex not in graph:
        #     return []
        # paths = []
        # for vertex in graph[starting_vertex]:
        #     if vertex not in path:
        #         ext_paths = self.dfs(vertex, destination_vertex, path)
        #         for p in ext_paths:
        #             paths.append(p)
        # return paths
        
        s = Stack()
        s.push([starting_vertex])
        found = []
        
        while s.size() > 0:
            path = s.pop()
            v = path[-1]
            if v not in found:
                if v == destination_vertex:
                    return path
                found.append(v)
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)           
                   
        return None






if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
