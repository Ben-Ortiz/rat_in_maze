import numpy as np

# constants
N = 5
STARTX = 0
STARTY = 0
GOALX = N - 1
GOALY = N - 1


class Maze():

    def __init__(self, dim, p):
        self.grid = np.random.choice(a=[1, 0], size=(dim, dim), p=[p, 1 - p])
        self.grid[0][0] = 0
        self.grid[-1][-1] = 0
        self.dim = dim
        self.p = p

    def __str__(self):  # this allows to call print on Maze object and it's readable
        return "{self.maze} \n".format(self=self)

    def __getitem__(self, maze):
        return self.grid


def printSolution(sol):
    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")

# helper method
def valid_square(sol_maze, x, y):
    # if x >= 0 and x < N and y >= 0 and y < N and sol_maze[x][y] == 0:
    #     return True

    # if x >= 0 and x < N and y >= 0 and y < N and sol_maze[x][y] == 0:
    #     return True
    #
    # return False

    if x >= 0 and x < N and y >= 0 and y < N and sol_maze[x][y] == 0:
        return True

    return False


# def isSafe(maze, x, y):
#     if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
#         return True
#
#     return False


# a recursive function that solves a maze using backtracing
def solve_maze(zero_maze, sol_maze, x, y):  # zero_maze is all zeroes. sol_maze has ones and zeroes
    # x and y are (0, 0) to represent the start of the board

    # if x and y are N-1, that's the goal and return true
    if x == GOALX and y == GOALY and sol_maze[x][y] == 0:
        zero_maze[x][y] = 0  # make the zeroes square equal 1 at GOALX and GOALY
        return True

    if valid_square(sol_maze, x, y) == True:  # if the square is safe in solution maze
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
        zero_maze[x][y] = 1
        return False

# def solveMazeUtil(maze, x, y, sol):
#     # if (x, y is goal) return True
#     if x == N - 1 and y == N - 1 and maze[x][y] == 1:
#         sol[x][y] = 1
#         return True
#
#     # Check if maze[x][y] is valid
#     if isSafe(maze, x, y) == True:
#         # Check if the current block is already part of solution path.
#         if sol[x][y] == 1:
#             return False
#
#         # mark x, y as part of solution path
#         sol[x][y] = 1
#
#         # Move forward in x direction
#         if solveMazeUtil(maze, x + 1, y, sol) == True:
#             return True
#
#         # If moving in x direction doesn't give solution
#         # then Move down in y direction
#         if solveMazeUtil(maze, x, y + 1, sol) == True:
#             return True
#
#         # If moving in y direction doesn't give solution then
#         # Move back in x direction
#         if solveMazeUtil(maze, x - 1, y, sol) == True:
#             return True
#
#         # If moving in backwards in x direction doesn't give solution
#         # then Move upwards in y direction
#         if solveMazeUtil(maze, x, y - 1, sol) == True:
#             return True
#
#         # If none of the above movements work then
#         # BACKTRACK: unmark x, y as part of solution path
#         sol[x][y] = 0
#         return False


# def solve_maze(sol_maze):
#     zero_maze = [[0 for j in range(N)] for i in range(N)]
#     # zero_maze = Maze(N, 0)  # a maze with all zeroes
#
#     if solve_maze(sol_maze, STARTX, STARTX, STARTY) == False:
#         print("no solution found")
#         return False
#
#     print(zero_maze)
#     print("solution found!")
#     return True

def solve_maze_helper(sol_maze):
    # Creating a 4 * 4 2-D list
    zero_maze = [[0 for j in range(N)] for i in range(N)]

    if solve_maze(zero_maze, sol_maze, STARTX, STARTY) == False:
        print("Solution doesn't exist")
        return False

    print("found solution")
    return True


def main():
    maze1 = Maze(N, 0.2)  # zeroes are clear paths, ones, are walls
    maze = maze1.grid.tolist()
    # maze = [[1, 0, 0, 0],
    #         [1, 1, 0, 1],
    #         [0, 1, 0, 0],
    #         [1, 1, 1, 1]]
    print(maze)
    printSolution(maze)

    print()

    zero_maze1 = Maze(N, 0)  # a maze with all zeroes
    zero_maze = zero_maze1.grid.tolist()
    print(zero_maze)
    printSolution(zero_maze)

    print()

    # solveMaze(maze)
    # solve_maze(zero_maze, maze, STARTX, STARTY)
    solve_maze_helper(maze)


if __name__ == "__main__":
    main()
