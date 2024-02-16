from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()
        self.queue = []

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)
        
    
    def bfs(self, vertex):
        self.visited.add(vertex)
        self.queue.append(vertex)
        i = 0
        while i < len(self.queue):
            vertex = self.queue[i]
            for v in self.graph[vertex]:
                self.queue.append(v)
            
            print('Visited: ' + vertex)
            i += 1
            

if __name__ == "__main__":
    g = Graph()
    while True:
        
        s = input("Enter the edge and q to stop: ")
        if s == 'q':
            break
        g.addEdge(*s.split())

    g.bfs('S')

