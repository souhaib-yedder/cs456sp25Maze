# calculating heuristic using manhantten distance      
def calculte_heuristic(current , goal):
        return abs(current[0]-goal[0]) + abs(current[1]-goal[1])

# total path legnth 
def get_path_legnth(path):
    if not path :
        return 0 
    return len(path)-1

# set cost values : heuristic + 1 
def set_cost(goal, maze):
    for row in range(len(maze)):
        for column in range(len(maze[0])):
            if maze[row][column] == 0:
                current = (row, column)
                cost = calculte_heuristic(current,goal)+1
                maze[row][column] = cost
            else:
                maze[row][column] = '#' # wall or unwalkable


# get the adjacent nodes of a particular node 
def get_neighbors(pos,maze):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # dirctions in maze up , down , left , right  
        neighbors = [] 
        rows = len(maze)  
        columns = len(maze[0])

        for d_rows, d_columns in directions:    # possible moves in directions 
            r, c = pos[0] + d_rows, pos[1] + d_columns # offest + current cell position
            if 0 <= r < rows and 0 <= c < columns and maze[r][c] != '#': # check if path is walkable
                neighbors.append((r, c))
        return neighbors

# display the maze 
def display_maze(maze):
    print("maze after setting cost values  :\n")
    for row in range(len(maze)):
        print()
        for column in range(len(maze[0])): 
            print(maze[row][column], end=' ')