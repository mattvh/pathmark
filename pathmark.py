from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import sys, random, time


silent = False


def load_matrix(filename):
    matrix = []
    with open(filename) as f:
        for line in f.readlines():
            row = []
            for n in line.split(" "):
                row.append(int(n))
            matrix.append(row)
    return matrix


def find_the_path(matrix):
    nodecount = len(matrix) - 1

    grid = Grid(matrix=matrix)

    start = grid.node(0, 0)
    end = grid.node(nodecount-1, nodecount-1)

    time_start = time.time()
    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, runs = finder.find_path(start, end, grid)
    seconds = time.time() - time_start
    
    if silent == False:
        print(grid.grid_str(path=path, start=start, end=end))
    print("Matrix size: %dx%d" % (len(matrix), len(matrix)))
    print("Operations:", runs)
    print("Path Length:", len(path))
    print("Run Time (Seconds):", seconds)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Enter a file name to load the matrix from.")
        exit()
    if len(sys.argv) > 2  and sys.argv[2] == "--nomap":
        silent = True
    filename = sys.argv[1]
    find_the_path(load_matrix(filename))
