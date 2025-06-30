from GBFS import gready_best_first_search
from Astar import A_star
from dfsAlgorithm import depth_first_search
from BfsAlgorithm import breadth_first_search
from maze import bigMaze
from maze import smallMaze
from maze import Maze
from visualization import visualize_path_with_grid
from ucsAlgorithm import uniform_cost_search
from set_get_functions import get_path_legnth , calculte_heuristic

def main():
   
    flag = True

    while(flag):
       
       print("Select the maze\n")
       print("A: For small maze   \n")
       print("B: For Maze \n")
       print("C: For big maze \n")
       option = input("Enter your choice: ").upper()  # convert to uppercase to handle 'a' or 'A'
       
       if option == 'A':
            from maze import smallMaze as selected_maze 
            start=(0,0)
            goal=(4,4)
            smallMaze[start[0]][start[1]] = 0
            smallMaze[goal[0]][goal[1]] = 0 
            total_heuristic = calculte_heuristic(start,goal)

       elif option == 'B':
            from maze import Maze as selected_maze
            start=(0,0)
            goal=(6,6)
            Maze[start[0]][start[1]] = 0
            Maze[goal[0]][goal[1]] = 0 
            total_heuristic = calculte_heuristic(start,goal)
       elif option == 'C':
            from maze import bigMaze as selected_maze
            goal = (19,19)
            start = (0,0)
            bigMaze[start[0]][start[1]] = 0
            bigMaze[goal[0]][goal[1]] = 0 
            total_heuristic = calculte_heuristic(start,goal)
       else:
            print("Invalid option selected.")
            selected_maze = None

       print("Select the algorithm\n")
       print("1: for DFS \n")
       print("2: for BFS \n")
       print("3: for A* \n")
       print("4: for Greedy \n")
       print("5: for UCS \n")
       print("0: Exit")
       choice = input("Enter your choice: ")
    
       if choice == '1':
        print("Running Depth First Search...")
        path = depth_first_search(start, goal, selected_maze)
        print("path is : ",path)
        legnth = get_path_legnth(path)
        if(legnth <= total_heuristic):
          print("the DFS solution is Optimal \n")
        else: print("not optimal\n")  
        visualize_path_with_grid(selected_maze, path,start,goal)

       elif choice == '2':
        print("Running Breadth First Search...")
        path = breadth_first_search(start, goal,selected_maze)
        print("path is : ",path)
        legnth = get_path_legnth(path)
        if(legnth <= total_heuristic):
          print("the BFS solution is Optimal \n")
        else: print("not optimal\n")  
        visualize_path_with_grid(selected_maze, path,start,goal)

       elif choice == '3':
        print("Running A* Search...")
        path = A_star(selected_maze, start, goal)
        print("path is : ",path)
        legnth = get_path_legnth(path)
        if(legnth <= total_heuristic):
          print("the A* solution is Optimal \n")
        else: print("not optimal\n")    
        visualize_path_with_grid(selected_maze, path,start,goal)
       elif choice == '4':

        print("Running Greedy Best-First Search...")
        path = gready_best_first_search(selected_maze,start,goal)
        print("path is : ",path)
        if(legnth <= total_heuristic):
          print("the Greedy solution is Optimal \n")
        else: print("not optimal\n")  
        visualize_path_with_grid(selected_maze, path,start,goal)

       elif choice == '5':
        print("Running UCS Algorithm...")
        path = uniform_cost_search(selected_maze,start,goal)
        legnth = get_path_legnth(path)
        
        print("path is : ",path ,"path legnth is ",legnth)
        if(legnth <= total_heuristic):
          print("the UCS solution is Optimal \n")
        else: print("not optimal\n")  
        visualize_path_with_grid(selected_maze, path,start,goal)

       elif choice == '0':
        print("Exiting...")
        flag = False
       else:
        print("Invalid choice. Please enter a number between 0 and 5.")
    
if __name__ == "__main__":
     main()