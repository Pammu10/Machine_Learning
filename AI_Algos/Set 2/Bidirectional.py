class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices

    def add_edge(self, src, dest):
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

def bidirectional_search(graph, src, dest):
    src_visited = [False] * graph.vertices
    dest_visited = [False] * graph.vertices
    src_queue = [src]
    dest_queue = [dest]
    src_parent = [-1] * graph.vertices
    dest_parent = [-1] * graph.vertices

    while src_queue and dest_queue:
        current_src = src_queue.pop(0)
        current_dest = dest_queue.pop(0)

        src_visited[current_src] = True
        dest_visited[current_dest] = True

        src_node = graph.graph[current_src]
        while src_node:
            if not src_visited[src_node.vertex]:
                src_queue.append(src_node.vertex)
                src_visited[src_node.vertex] = True
                src_parent[src_node.vertex] = current_src
            src_node = src_node.next

        dest_node = graph.graph[current_dest]
        while dest_node:
            if not dest_visited[dest_node.vertex]:
                dest_queue.append(dest_node.vertex)
                dest_visited[dest_node.vertex] = True
                dest_parent[dest_node.vertex] = current_dest
            dest_node = dest_node.next

        intersecting_node = is_intersecting(src_visited, dest_visited)
        if intersecting_node != -1:
            print(f"Path exists between {src} and {dest}")
            print(f"Intersection at: {intersecting_node}")
            print_path(intersecting_node, src_parent, dest_parent, src, dest)
            return
    print(f"Path does not exist between {src} and {dest}")

def is_intersecting(src_visited, dest_visited):
    for i in range(len(src_visited)):
        if src_visited[i] and dest_visited[i]:
            return i
    return -1

def print_path(intersecting_node, src_parent, dest_parent, src, dest):
    path = []
    node = intersecting_node
    while node != -1:
        path.append(node)
        node = src_parent[node]
    path.reverse()
    node = dest_parent[intersecting_node]
    while node != -1:
        path.append(node)
        node = dest_parent[node]
    print("*****Path*****")
    print(' '.join(map(str, path)))

if __name__ == '__main__':
    n = 15
    src = 0
    dest = 14
    graph = Graph(n)
    graph.add_edge(0, 4)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 6)
    graph.add_edge(6, 7)
    graph.add_edge(7, 8)
    graph.add_edge(8, 9)
    graph.add_edge(8, 10)
    graph.add_edge(9, 11)
    graph.add_edge(9, 12)
    graph.add_edge(10, 13)
    graph.add_edge(10, 14)
    bidirectional_search(graph, src, dest)


