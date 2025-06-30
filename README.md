# cs456sp25Maze
"This project is for implementing mazes using AI algorithms."

Maze Solver using AI Algorithms (BFS, DFS, Greedy, A*, UCS)
Project Overview
This project focuses on solving mazes using a variety of AI search algorithms including:

BFS (Breadth-First Search)

DFS (Depth-First Search)

Greedy Search

A* (A-star)

UCS (Uniform Cost Search)

The goal is to apply these algorithms to solve mazes of different sizes (smallMaze, mediumMaze, and bigMaze), and compare their performance and efficiency in finding the optimal path from the start to the goal.

Students
Souhaib Yedder

hyder gritli

Project Objectives
Implement AI Algorithms: We applied several search algorithms to find the best path in a maze.

Different Maze Sizes: We tested the algorithms on mazes of different sizes: small, medium, and large.

Performance Comparison: We compared the performance, speed, and optimality of each algorithm in solving different mazes.

Pathfinding Visualization: Each algorithm is tested and visualized to show how it finds the path from the start to the goal.

Algorithms Used
BFS (Breadth-First Search): Explores the maze level by level to guarantee the shortest path.

DFS (Depth-First Search): Explores the maze by going deep into one path before backtracking.

Greedy Search: Chooses paths that appear to lead most directly toward the goal based on a heuristic.

A* (A-star): Uses both actual cost and heuristic to efficiently find the optimal path.

UCS (Uniform Cost Search): Finds the least-cost path, considering edge weights.

Maze Types
The project includes three different maze sizes:

smallMaze: A small maze with fewer obstacles and a simpler layout.

mediumMaze: A medium-sized maze with a moderate level of complexity.

bigMaze: A large maze with more obstacles and greater complexity, providing a challenge for the search algorithms.

Steps to Run the Program
1. Install Dependencies
First, you need to install the necessary Python libraries using pip:


"pip install matplotlib numpy"


matplotlib: A library for displaying the maze and the path found by the selected algorithm.

numpy: A library for handling arrays and matrices, used to represent the maze as a grid.

2. Select Maze Type
The program includes three different maze sizes:

smallMaze

Maze

bigMaze

When running the program, you will be prompted to choose the size of the maze you want to solve.

3. Select Search Algorithm
After selecting the maze size, you will be asked to choose one of the 5 available search algorithms:

BFS (Breadth-First Search)

DFS (Depth-First Search)

Greedy Search

A* (A-star)

UCS (Uniform Cost Search)

4. Run the Algorithm
Once you select an algorithm, the program will apply it to the chosen maze. The algorithm will compute the path from the start point to the goal. It will also check if the path found is optimal or not.

5. Display Results
After running the algorithm, the program will display the following:

The path found by the selected algorithm.

Whether the path is optimal or not.

The time taken by the algorithm to find the path.

6. Visualize the Maze and Path
The program will use matplotlib to display the maze, highlighting the path found by the chosen algorithm. The visualization will show the maze, with the path clearly marked from the start to the goal.

7. Compare Algorithms
After running the program, you can compare the performance of different algorithms on various maze sizes. The program will calculate the time taken for each algorithm and compare the efficiency of the algorithms.
