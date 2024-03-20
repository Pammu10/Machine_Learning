import heapq

def heuristic(node, goal):
    return abs(node - goal)

def astar(start, goal, graph):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (0, start))
    came_from = {}

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1]

        closed_set.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in closed_set:
                new_cost = current_cost + graph[current_node][neighbor]
                heapq.heappush(open_list, (new_cost + heuristic(neighbor, goal), neighbor))
                came_from[neighbor] = current_node

    return None

# Take input from the user
start = int(input("Enter start node value: "))
goal = int(input("Enter goal node value: "))

# Define the graph
graph = {}
edges = int(input("Enter the number of edges: "))

# Build the graph
for _ in range(edges):
    node1, node2, cost = map(int, input("Enter node1 node2 cost: ").split())
    
    if node1 not in graph:
        graph[node1] = {}
    if node2 not in graph:
        graph[node2] = {}
    
    graph[node1][node2] = cost
    graph[node2][node1] = cost

print(astar(start, goal, graph))



# Enter start node value: 0
# Enter goal node value: 4
# Enter the number of edges: 8
# Enter node1 node2 cost: 0 1 2
# Enter node1 node2 cost: 0 2 3
# Enter node1 node2 cost: 1 3 4
# Enter node1 node2 cost: 1 2 1
# Enter node1 node2 cost: 2 3 2
# Enter node1 node2 cost: 2 4 3
# Enter node1 node2 cost: 3 4 2
# Enter node1 node2 cost: 4 5 1
# [1, 2, 3, 4]