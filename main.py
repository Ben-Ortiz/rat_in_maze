import numpy as np

#constants
N = 5
GOALX = N - 1
GOALY = N - 1

class Maze():
    """
     Initializing properties of Maze.
     Maze: Generating maze using NUmpy with abritrary dim and obstacle density p.
     Start, End: Sets the starting and ending location to be true.
    """

    def __init__(self, dim, p):
        self.maze = np.random.choice(a=[1, 0], size=(dim, dim), p=[p, 1 - p])
        self.maze[0][0] = 0
        self.maze[-1][-1] = 0
        self.dim = dim
        self.p = p

    def __str__(self): #this allows to call print on Maze object and it's readable
        return "{self.maze} ".format(self=self)


def valid_square(sol_maze, x, y):
    if x >= 0 and x < N and y >= 0 and sol_maze[x][y] == 0:
        return True

    return False


def solve_maze(zero_maze, sol_maze, x, y): #zero_maze is all zeroes. sol_maze has ones and zeroes
    #x and y are (0, 0) to represent the start of the board
    #if x and y are N-1, that's the goal

    if x == GOALX and y == GOALY and sol_maze[x][y] == 0:
        zero_maze[x][y] = 1
        return True

    if valid_square(sol_maze, x, y) == True: #if the square is safe is solution maze





    pass




def main():


    maze = Maze(N, 0.7) #zeroes are clear paths, ones, are walls
    print(maze)

    print()

    zero_maze = Maze(N, 0) #a maze with all zeroes
    print(zero_maze)

    print()


if __name__ == "__main__":
    main()
