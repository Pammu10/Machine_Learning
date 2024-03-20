import heapq
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


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


# Example usage:
cities = {(0, 0), (1, 2), (3, 1), (2, 2), (1, 1)}
start_city = (0, 0)

path, total_cost = tsp(cities, start_city)
print("Path:", path)
print("Total cost:", total_cost)
