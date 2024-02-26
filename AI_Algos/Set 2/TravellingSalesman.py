import heapq
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def minimum_spanning_tree(cities, start_city):
    visited = set([start_city])
    mst_cost = 0
    min_heap = [(0, start_city)]

    while min_heap:
        cost, current_city = heapq.heappop(min_heap)
        if current_city not in visited:
            visited.add(current_city)
            mst_cost += cost
            for neighbor_city in cities:
                if neighbor_city not in visited:
                    heapq.heappush(min_heap, (euclidean_distance(current_city, neighbor_city), neighbor_city))

    return mst_cost

def tsp(cities, start_city):
    unvisited_cities = set(cities)
    unvisited_cities.remove(start_city)
    path = [start_city]
    total_cost = 0

    while unvisited_cities:
        nearest_neighbor = min(unvisited_cities, key=lambda city: euclidean_distance(path[-1], city))
        total_cost += euclidean_distance(path[-1], nearest_neighbor)
        path.append(nearest_neighbor)
        unvisited_cities.remove(nearest_neighbor)

    total_cost += euclidean_distance(path[-1], start_city)  # Returning to the start city
    return path, total_cost

def tsp_a_star(cities, start_city):
    open_list = [(0, [start_city])]
    closed_set = set()

    while open_list:
        current_cost, current_path = heapq.heappop(open_list)
        current_city = current_path[-1]

        if len(current_path) == len(cities) + 1:
            return current_path, current_cost

        if current_city not in closed_set:
            closed_set.add(current_city)

            for next_city in cities:
                if next_city not in current_path:
                    new_cost = current_cost + euclidean_distance(current_city, next_city) + minimum_spanning_tree(cities - set(current_path), next_city)
                    heapq.heappush(open_list, (new_cost, current_path + [next_city]))

    return None

# Example usage:
cities = {(0, 0), (1, 2), (3, 1), (2, 2), (1, 1)}
start_city = (0, 0)

path, total_cost = tsp(cities, start_city)
print("Path:", path)
print("Total cost:", total_cost)
