class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs(node, goal, depth_limit, iteration):
    print(f"Iteration {iteration}: Visiting node {node.value} at depth {depth_limit}")

    if node.value == goal:
        return True

    if depth_limit == 0:
        return False

    for child in node.children:
        if dfs(child, goal, depth_limit - 1, iteration):
            return True

    return False

def iterative_deepening_dfs(root, goal):
    depth_limit = 0
    iteration = 0
    while True:
        print(f"\nStarting Iteration {iteration} with depth limit {depth_limit}")
        if dfs(root, goal, depth_limit, iteration):
            return True, depth_limit  # Goal found
        depth_limit += 1
        iteration += 1

# Function to build the graph from user input with vertex labels as letters
def build_graph():
    vertices = set()
    edges = []

    while True:
        edge_input = input("Enter edge (vertex1 vertex2) or 'done' to finish: ").split()

        if edge_input[0].lower() == 'done':
            break

        vertex1, vertex2 = edge_input
        vertices.add(vertex1)
        vertices.add(vertex2)
        edges.append((vertex1, vertex2))

    nodes = {label: Node(label) for label in vertices}

    for edge in edges:
        nodes[edge[0]].children.append(nodes[edge[1]])
        nodes[edge[1]].children.append(nodes[edge[0]])

    root_vertex = input("Enter the root node: ")
    root = nodes[root_vertex]

    return root

# Example usage:
root = build_graph()
goal_node_value = input("Enter the goal node: ")

found, depth = iterative_deepening_dfs(root, goal_node_value)

if found:
    print(f"\nGoal node {goal_node_value} found at depth {depth}.")
else:
    print(f"\nGoal node {goal_node_value} not found.")
