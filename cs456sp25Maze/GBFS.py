from maze import smallMaze
import heapq
maze = smallMaze

# get neighbors of current position 
def get_neighbors(pos,maze):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # dirctions in maze up , down , left , right  
        neighbors = [] 
        rows = len(maze)  
        columns = len(maze[0])

        for d_rows, d_columns in directions:    # possible moves in directions 
            r, c = pos[0] + d_rows, pos[1] + d_columns # offest + current cell position
            if 0 <= r < rows and 0 <= c < columns and maze[r][c] == 0: # check if path is walkable
                neighbors.append((r, c))
        return neighbors


# calculating heuristic using manhantten distance      
def calculte_heuristic(current , goal):
        return abs(current[0]-goal[0]) + abs(current[1]-goal[1])
    

def gready_best_first_search(maze,start,goal):
        path_from = {} # path dictionary: neighbor came from node  
        path = [] # to store the real path after constructing it 
        visited = set() # visited set of nodes to avoid revisiting
        queue = [] # priority queue for right nodes order 
        heapq.heappush(queue,(calculte_heuristic(start,goal),start))  
        path_cost = 0

        while(queue):
            
            _, current = heapq.heappop(queue)
            if current in visited:
                continue
            
        # adding current node to a visited list 
            visited.add(current) 
            if(current == goal):
                path.append(current)
                while current in path_from :
                      current = path_from[current]
                      path.append(current) # constructs the real path after tracking backwards
                path.reverse() # reversing the path to get it in forward from 
                return path   
           
            for neighbor in get_neighbors(current,maze):
                if neighbor not in visited:
                   heapq.heappush(queue, (calculte_heuristic(neighbor, goal), neighbor))
                   path_from[neighbor] = current 

                    
        return None  # if no path was found    
            
            
   


        
        
