import matplotlib.pyplot as plt
import numpy as np
from queue import Queue
from math import sqrt

# Maze Generation
def getMaze(input_maze, ans=[]):
    
    # plot path on new_maze with answer(path taken)
    new_maze = []
    
    # From the answer(path taken), use rows and columns to mark path taken
    for r, c in ans:
        maze[r][c] = '.'            # '.' represents the path taken

    # Identify elements of maze: walls, empty path, and path taken
    for row in maze:
        elements = []
        for x in row:
            if x == 'W':            # 'W' represents the walls
                elements.append(0)
            elif x == 'P':          # 'P' represents the empty path
                elements.append(2)
            else:                   # actual path taken
                elements.append(1) 
                
        new_maze.append(elements)
        print(elements)
    
    # Plot maze with matplotlib
    h, ax = plt.subplots(figsize=(6,6))
    plt.pcolormesh(new_maze)
    plt.xticks([])  # remove axes
    plt.yticks([])  
    plt.title('MS1008 - Problem 4', fontweight ="bold")
    plt.gca().invert_yaxis()
    plt.show()

    
# Breadth First Search
def bfs():
    # Initialise the queue for Breadth First Search
    # Put exit coords in queue
    queue = Queue()
    queue.put((int(ext1[1]), int(ext1[0])))   
    while not queue.empty():
        # Get rows and columns to front of queue
        r, c = queue.get()
        # With the 4 possible moves (ver/hor), check if the next path taken is valid
        for move in range(4):
            new_r, new_c = r + ver[move], c + hor[move]
            
            # Put new rows and column into the queue if the next path is an empty spot and not visited before
            if maze[new_r][new_c] == 'P' and visited[new_r][new_c] == [-1, -1]:
                visited[new_r][new_c] = [r, c]
                queue.put((new_r, new_c))


# Find the solution path
def get_route(row, col):
        r, c = visited[row][col]
        ans = [(row , col)]
        if r == row and c == col:
            return(ans)
        else:
            ans.extend(get_route(r, c))
            return(ans)
 

### MAIN CODE ###        

with open('maze.txt') as file:
    maze_actual = file.readlines()

# Initialise the maze and visited array
maze = []
visited = []

ver = [1, 0, -1, 0] #possible moves
hor = [0, 1, 0, -1]

    
count = 0
for line in maze_actual:
    count += 1
side = int(sqrt(count)) #determine the width and height of square graph


print("If you can't see any of the points, you have selected a wall coordinate.")   
entinput = input("Coordinates for entrance (x,y) between 0 and " + str(side) + ": ")
extinput = input("Coordinates for exit (x,y) between 0 and " + str(side) + ": ")
ent1 = entinput.split(",")
ext1 = extinput.split(",")


# Dimensions of square maze: sidexside
row, col = side, side
count = 0

for x in range(row):
    maze_row = []
    visited_row = []

    for y in range(col):
        if maze_actual[count] == 'True\n':
            maze_row.append('W')  # 'W' Walls
        else:
            maze_row.append('P')  # 'P' Path
        visited_row.append([-1, -1]) 
        count += 1
    visited.append(visited_row)
    maze.append(maze_row)

# Transposing the matrix
maze = np.transpose(np.array(maze))

# Setting maze end location
maze[int(ext1[1])][int(ext1[0])] = 'x'
visited[int(ext1[1])][int(ext1[0])] = [int(ext1[1]), int(ext1[0])]

bfs()
ans = get_route(int(ent1[1]), int(ent1[0]))
getMaze(maze, ans)
print("Count = ", count, ", ", "Side: ", side) #to check
