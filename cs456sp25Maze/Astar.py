import heapq
from set_get_functions import get_neighbors, calculte_heuristic,display_maze , set_cost

# calculating the F(n) of the algorithm         
def calculate_fn(neighbor,goal,g_cost):
        return g_cost[neighbor] + calculte_heuristic(neighbor,goal)

def A_star(maze,start,goal):
        set_cost(goal,maze)
        display_maze(maze)
        path_from = {} # path dictionary: neighbor came from node 
        path = [] # to store the real path after constructing it 
        queue = [] # priority queue for right nodes order 
        visited = set() # visited set to avoid revisiting
        g_cost = {start: 0} # total cost from the start node 
        heapq.heappush(queue,(calculate_fn(start,goal,g_cost),start))
        
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
                tentative_g = g_cost[current] + 1  # cost from current to neighbor
                if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g
                    f = calculate_fn(neighbor, goal, g_cost)
                    heapq.heappush(queue, (f, neighbor))
                    path_from[neighbor] = current
        return None         
            
