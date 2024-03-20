import heapq

def heuristic(node, goal):
    return abs(node - goal)


def best_first_search(start, goal, v):
    visited = [False] * v
    node_list = []
    heapq.heappush(node_list, (0, start))
    visited[start] = True

    while node_list:
        current_cost, current_node = heapq.heappop(node_list)
        print(current_node, end=" ")
        if current_node == goal:
            break
       
        for v, c in graph[current_node]:
            if visited[v] == False:
                visited[v] = True
                heapq.heappush(node_list, (c, v))
        
    print()

start = 0
goal = 9
v = 14
graph = [[] for _ in range(v)]


def addedge(node1, node2, cost):
    graph[node1].append((node2, cost))
    graph[node2].append((node1, cost))


addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

best_first_search(start, goal, v)
