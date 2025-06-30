import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
def visualize_path_with_grid(maze, path, start, goal):
    rows, cols = len(maze), len(maze[0])
    fig, ax = plt.subplots()
    ax.axis('off')

    # Create a blank string grid to feed into the table
    text_grid = [['' for _ in range(cols)] for _ in range(rows)]

    # Create cell colors: white for paths, black for walls
    cell_colors = [['white' if maze[r][c] != '#' else 'black' for c in range(cols)] for r in range(rows)]

    # Create table
    table = plt.table(cellText=text_grid,
                      cellColours=cell_colors,
                      cellLoc='center',
                      loc='center',
                      colWidths=[0.1]*cols)

    # Make cells square
    table.scale(1, 1.5)

    # Thin black borders
    for key, cell in table.get_celld().items():
        cell.set_edgecolor('black')
        cell.set_linewidth(0.5)

    # Mark start and goal
    table[start].set_facecolor('lightgray')
    table[goal].set_facecolor('dimgray')

    def update(frame):
        if frame < len(path):
            r, c = path[frame]
            if (r, c) == goal:
                table[(r, c)].set_facecolor('green')
            else:
                table[(r, c)].set_facecolor('red')
        return []

    ani = animation.FuncAnimation(fig, update, frames=len(path), interval=300, repeat=False)
    plt.show()