from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)
        

    def dfs(self, vertex):
        self.visited.add(vertex)
        print('Visited: ' + vertex)
        for i in self.graph[vertex]:
            # print
            if i not in self.visited:
                self.dfs(i)
    

if __name__ == "__main__":
    g = Graph()
    while True:
        
        s = input("Enter the edge and q to stop: ")
        if s == 'q':
            break
        g.addEdge(*s.split())
    g.dfs('S')

