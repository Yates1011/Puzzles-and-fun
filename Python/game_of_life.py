# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 13:14:56 2022

@author: yates
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the initial grid
grid = np.random.randint(0, 2, (10, 10))

# Define a function to update the grid for the next generation
def update(data):
    global grid
    new_grid = grid.copy()
    for i in range(1, grid.shape[0]-1):  # Change this line to avoid out-of-bounds errors (rows)
        for j in range(1, grid.shape[1]-1):  # Change this line to avoid out-of-bounds errors
            # Count the number of live neighbors
            live_neighbours = (grid[i-1, j-1] + grid[i-1, j] + grid[i-1, j+1] +
                              grid[i, j-1] + grid[i, j+1] +
                              grid[i+1, j-1] + grid[i+1, j] + grid[i+1, j+1])
            # Apply the rules of the game of life
            if grid[i, j] == 0 and live_neighbours == 3:
                new_grid[i, j] = 1
            elif grid[i, j] == 1 and (live_neighbours < 2 or live_neighbours > 3):
                new_grid[i, j] = 0
    # Update the grid for the next generation
    grid = new_grid
    mat.set_data(grid)
    return [mat]

# Set up the figure and the plot
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap = 'inferno')

# Animate the game of life
ani = animation.FuncAnimation(fig, update, blit=True, interval=100, save_count=50)
plt.show()

# Save once a game is complete
ani.save('game_of_life.mp4', writer='ffmpeg', fps=30, bitrate=8000)
