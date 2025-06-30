from maze import smallMaze
maze = smallMaze
from set_get_functions import get_neighbors ,display_maze
           
def depth_first_search(start,goal,maze):
        display_maze(maze)   
    # Initialize visited list with all nodes as False, and stack with the given vertex
        stack = [start]
        visited = set()
        visited.add(start)
        path_from = {} # path dictionary: neighbor came from node 
        path = [] # to store the real path after constructing it 
        
    # Perform DFS traversal until the stack is empty or goal is found
        while stack:
            current = stack.pop()
            if current == goal:
                
                path.append(current)
                while current in path_from:
                    current = path_from[current]
                    path.append(current)
                path.reverse()
                
                return path

            for neighbor in get_neighbors(current,maze):
                
                if neighbor not in visited:
                   stack.append(neighbor)
                   visited.add(neighbor)
                   path_from[neighbor] = current 
        return None    
