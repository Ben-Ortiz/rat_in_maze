import numpy as np

# constants
N = 4
STARTX = 0
STARTY = 0
GOALX = N - 1
GOALY = N - 1


# class Maze():
#
#     def __init__(self, dim, p):
#         self.maze = np.random.choice(a=[1, 0], size=(dim, dim), p=[p, 1 - p])
#         self.maze[0][0] = 0
#         self.maze[-1][-1] = 0
#         self.dim = dim
#         self.p = p
#
#     def __str__(self):  # this allows to call print on Maze object and it's readable
#         return "{self.maze} ".format(self=self)
#
#     def __getitem__(self, maze):
#         return self.maze


def printSolution(sol):
    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")

# helper method
def isSafe(maze, x, y):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True

    return False

# def solveMaze(maze):
#     # Creating a 4 * 4 2-D list
#     sol = [[0 for j in range(4)] for i in range(4)]
#
#     if solveMazeUtil(maze, 0, 0, sol) == False:
#         print("Solution doesn't exist")
#         return False
#
#     printSolution(sol)
#     print("Solution exist")
#     return True


def solveMaze(maze):
    # Creating a 4 * 4 2-D list
    sol = [[0 for j in range(4)] for i in range(4)]

    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Solution doesn't exist");
        return False

    printSolution(sol)
    print("solution found")
    return True

# a recursive function that solves a maze using backtracing
def solveMazeUtil(maze, x, y, sol):  # zero_maze is all zeroes. sol_maze has ones and zeroes
    # x and y are (0, 0) to represent the start of the board

    # if x and y are N-1, that's the goal and return true
    if x == GOALX and y == GOALY and maze[x][y] == 1:
        sol[x][y] = 1  # make the zeroes square equal 1 at GOALX and GOALY
        return True

    if isSafe(maze, x, y) == True:  # if the square is safe is solution maze
        if sol[x][y] == 1:  # if this square has already been checked in the zeroes board, 0 return false
            return False

        # else make the zero_maze a 0
        sol[x][y] = 1

        # if the square to the right is clear return true
        if solveMazeUtil(maze, x + 1, y, sol) == True:
            return True

        # if the square to the right is not clear then move down and return true
        if solveMazeUtil(maze, x, y + 1, sol) == True:
            return True

        # if the square to the down is not clear then move to the left and return true
        if solveMazeUtil(maze, x - 1, y, sol) == True:
            return True

        # if the square to the left is not clear then move up and return true
        if solveMazeUtil(maze, x, y - 1, sol) == True:
            return True

        # if none of the directions work, then backtrace down the call stack
        sol[x][y] = 0
        return False




def main():
    # maze1 = Maze(N, 0.2)  # zeroes are clear paths, ones, are walls
    # maze = maze1.maze.tolist()
    # sol_maze = [[1, 1, 0, 0],
    #         [0, 1, 0, 1],
    #         [0, 1, 0, 0],
    #         [1, 1, 1, 0]]


    maze = [[1, 0, 0, 1],
            [1, 1, 1, 1],
            [0, 1, 0, 1],
            [1, 1, 1, 1]]
    # print(sol_maze)
    print()
    printSolution(maze)
    print()
    solveMaze(maze)

    # maze2 = [[0, 0, 0, 1],
    #         [1, 0, 0, 0],
    #         [0, 0, 1, 0],
    #         [1, 0, 0, 0]]
    # print()
    # printSolution(maze2)
    # print()
    # solveMaze(maze2)
    # print()

    # zero_maze1 = Maze(N, 0)  # a maze with all zeroes
    # zero_maze = zero_maze1.maze.tolist()
    # print(zero_maze)
    # printSolution(zero_maze)
    #
    # print()

    # solve_maze(zero_maze, maze, STARTX, STARTY)
    # solveMaze(sol_maze, zero_maze)



if __name__ == "__main__":
    main()
