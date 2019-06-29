""" Utility module

    Script used to create adjacency matrix file .txt from edge list.
    The edge matrix is so ready for the core of the program.
    It must be run with the following command:
        $ python edge_list_to_adjacency_matrix.py

    CAVEAT: this may generate a physical version of the file with huge dimensions
    depending on the number of nodes in the edge list uploaded.
    The version of the file implements an edge list upload avoiding the file creation
    (if not needed). Although this, the RAM usage will be still expensive.

    External Libraries Required:
    - numpy.py

    No class are needed.

"""
import numpy as np


def main():
    # Open the file in the EXAMPLES/EDGES_LIST_EXAMPLES/ folder of the project
    file = open('../EXAMPLES/EDGES_LIST_EXAMPLES/' + input("Please, enter the INPUT file name\n"))
    # Initialize the max length of the file
    max_length = 0
    # Find the max to set the matrix cardinality
    for row in file:
        numbers = [int(i) for i in row.split() if i.isdigit()]
        # Set the max to the max between the previous value and the two integers
        max_length = max(max_length, numbers[0], numbers[1])
    # Come back to file beginning
    file.seek(0)
    # Initialize the matrix
    matrix = np.zeros((max_length + 1, max_length + 1), dtype=int)
    # For each row
    for row in file:
        # Results of the file line
        res = [int(i) for i in row.split() if i.isdigit()]
        # Set first direction arc
        matrix[res[0]][res[1]] = 1
        # Set the symmetric direction arc
        matrix[res[1]][res[0]] = 1
    print(matrix)
    # Saving the file in a binary one in the EXAMPLES/MATRIX_EXAMPLES directory
    output_path = input("Please, enter the OUTPUT file name\n")
    with open('../../EXAMPLES/MATRIX_EXAMPLES/' + output_path, 'wb') as f:
        np.savetxt(f, matrix)
    print("File created")


if __name__ == "__main__":
    main()
