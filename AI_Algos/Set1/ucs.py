import heapq

class Node:
    def __init__(self, value, cost=0):
        self.value = value
        self.children = []  # List of (child, cost) pairs
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def uniform_cost_search(root, goal):
    priority_queue = [(root.cost, root)]
    visited = set()

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node.value == goal:
            return True, current_node.cost  # Goal found

        if current_node.value not in visited:
            visited.add(current_node.value)

            for child, edge_cost in current_node.children:
                heapq.heappush(priority_queue, (current_node.cost + edge_cost, child))

    return False, None  # Goal not found

# Function to build the graph from user input
def build_weighted_graph():
    vertices = set()
    edges = []

    while True:
        edge_input = input("Enter weighted edge (vertex1 vertex2 cost) or 'done' to finish: ").split()

        if edge_input[0].lower() == 'done':
            break

        vertex1, vertex2, cost = edge_input
        cost = int(cost)
        vertices.add(vertex1)
        vertices.add(vertex2)
        edges.append((vertex1, vertex2, cost))

    nodes = {value: Node(value) for value in vertices}

    for edge in edges:
        nodes[edge[0]].children.append((nodes[edge[1]], edge[2]))

    root_vertex = input("Enter the root node: ")
    root = nodes[root_vertex]

    return root

# Example usage:
weighted_root = build_weighted_graph()
goal_node_value = input("Enter the goal node: ")

found, cost = uniform_cost_search(weighted_root, goal_node_value)

if found:
    print(f"\nGoal node {goal_node_value} found with cost {cost}.")
else:
    print(f"\nGoal node {goal_node_value} not found.")
