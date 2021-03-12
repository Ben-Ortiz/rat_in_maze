import numpy as np

# constants
N = 5
STARTX = 0
STARTY = 0
GOALX = N - 1
GOALY = N - 1


class Maze():

    def __init__(self, dim, p):
        self.maze = np.random.choice(a=[1, 0], size=(dim, dim), p=[p, 1 - p])
        self.maze[0][0] = 0
        self.maze[-1][-1] = 0
        self.dim = dim
        self.p = p

    def __str__(self):  # this allows to call print on Maze object and it's readable
        return "{self.maze} ".format(self=self)

    def __getitem__(self, maze):
        return self.maze


# helper method
def valid_square(sol_maze, x, y):
    if x >= 0 and x < N and y >= 0 and y < N and sol_maze[x][y] == 0:
        return True

    return False


# a recursive function that solves a maze using backtracing
def solve_maze(zero_maze, sol_maze, x, y):  # zero_maze is all zeroes. sol_maze has ones and zeroes
    # x and y are (0, 0) to represent the start of the board

    # if x and y are N-1, that's the goal and return true
    if x == GOALX and y == GOALY and sol_maze[x][y] == 0:
        zero_maze[x][y] = 1  # make the zeroes square equal 1 at GOALX and GOALY
        return True

    if valid_square(sol_maze, x, y) == True:  # if the square is safe is solution maze
        if zero_maze[x][y] == 0:  # if this square has already been checked in the zeroes board, 0 return false
            return False

        # else make the zero_maze a 0
        zero_maze[x][y] = 0

        # if the square to the right is clear return true
        if solve_maze(zero_maze, sol_maze, x + 1, y) == True:
            return True

        # if the square to the right is not clear then move down and return true
        if solve_maze(zero_maze, sol_maze, x, y + 1) == True:
            return True

        # if the square to the down is not clear then move to the left and return true
        if solve_maze(zero_maze, sol_maze, x - 1, y) == True:
            return True

        # if the square to the left is not clear then move up and return true
        if solve_maze(zero_maze, sol_maze, x, y - 1) == True:
            return True

        # if none of the directions work, then backtrace down the call stack
        zero_maze[x][y] = 0
        print("solution doesn't exist!")
        return False


def main():
    maze = Maze(N, 0.7)  # zeroes are clear paths, ones, are walls
    print(maze)

    print()

    zero_maze = Maze(N, 0)  # a maze with all zeroes
    print(zero_maze)

    print()

    solve_maze(zero_maze, maze, STARTX, STARTY)


if __name__ == "__main__":
    main()
