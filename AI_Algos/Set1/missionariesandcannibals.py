from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat_location):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat_location = boat_location

    def is_valid(self):
        # Check if the state is valid (no more cannibals than missionaries on either side)
        return (self.missionaries == 0 or self.missionaries >= self.cannibals) and \
               (3 - self.missionaries == 0 or (3 - self.missionaries) >= (3 - self.cannibals))

    def is_goal(self):
        # Check if the state is the goal state (0M, 0C, R)
        return self.missionaries == 0 and self.cannibals == 0 and self.boat_location == 'R'

def bfs(initial_state):
    visited_states = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if current_state.is_goal():
            return path + [current_state]

        visited_states.add(current_state)

        successors = generate_successors(current_state)
        for successor in successors:
            if successor not in visited_states:
                queue.append((successor, path + [current_state]))

    return None

def generate_successors(current_state):
    successors = []

    # Possible moves: 1M, 1C, 2M, 2C, 1M1C
    moves = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]

    for move in moves:
        new_state = State(current_state.missionaries - move[0],
                          current_state.cannibals - move[1],
                          'L' if current_state.boat_location == 'R' else 'R')

        if new_state.is_valid():
            successors.append(new_state)

    return successors

def print_solution(path):
    print("Solution:")
    for i, state in enumerate(path):
        boat_side = "Left" if state.boat_location == 'L' else "Right"
        print(f"Step {i + 1}: Boat at {boat_side}, {state.missionaries}M {state.cannibals}C on Left, {3 - state.missionaries}M {3 - state.cannibals}C on Right")

# Initial state: 3M, 3C, L
initial_state = State(3, 3, 'L')

# Find a solution using BFS
solution_path = bfs(initial_state)

# Print the solution
if solution_path:
    print_solution(solution_path)
else:
    print("No solution found.")
