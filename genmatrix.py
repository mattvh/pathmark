import sys, random

def generate_matrix(nodecount):
    matrix = []
    for y in range(nodecount):
        line = []
        for x in range(nodecount):
            if x%2==0:
                line.append(1)
            else:
                if random.randrange(3) == 0:
                    line.append(0)
                else:
                    line.append(1)
        matrix.append(line)
    return matrix


def write_file(matrix):
    with open("matrix.txt", "w") as f:
        for line in matrix:
            f.write(" ".join(str(n) for n in line))
            f.write("\n")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Enter a node count in the form of one side of a square.")
        exit()
    nodecount = int(sys.argv[1])
    write_file(generate_matrix(nodecount))
    print("Done!")
