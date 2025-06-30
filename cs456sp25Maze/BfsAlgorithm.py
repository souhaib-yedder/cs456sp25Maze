from collections import deque
import time
from set_get_functions import get_neighbors
         
def breadth_first_search(start, goal, maze):
    # Initialize visited list with all nodes as False, and queue with the given vertex
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    path_from = {}  # path dictionary: neighbor came from node 
    path = []  # to store the real path after constructing it 
    steps = 0  # This will represent the number of steps
    nodes_visited = 0  # To count the number of visited nodes
    
    start_time = time.perf_counter()  # Start time (using perf_counter for more precision)
    
    # Perform BFS traversal until the queue is empty or goal is found
    while queue:
        current = queue.popleft()
        nodes_visited += 1
        
        # If we find the goal, stop the algorithm
        if current == goal:
            path.append(current)
            while current in path_from:
                current = path_from[current]
                path.append(current)
            path.reverse()

            # Now, calculate the number of steps from the path
            steps = len(path) - 1  # Subtract 1 to exclude the starting point

            end_time = time.perf_counter()  # End time
            elapsed_time = end_time - start_time  # Calculate time taken
            
            # Print results
            print(f"Path found: {path}")
            print(f"Number of steps: {steps}")
            print(f"Nodes visited: {nodes_visited}")
            print(f"Time taken: {elapsed_time:.6f} seconds")  # Increased precision to 6 decimal places

            # Indicate completion
            print("Completed: Yes")
            return path
        
        # Loop through neighbors and add them to the queue if not visited
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                path_from[neighbor] = current

    # If no path is found, print Not Completed
    print("No path found")
    print("Completed: No")
    return None
