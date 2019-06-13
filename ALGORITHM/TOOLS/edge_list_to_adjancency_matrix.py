""" Utility module

    Module used to create adjacency matrix from edge list.
    The edge matrix is so ready for the core of the program.
    It must be run with the following command:
        $ python edge_list_to_adjacency_matrix.py

    External Libraries Required:
    - numpy.py

    No class are needed.

"""
import numpy as np

# Open the file
file = open(input("Please, enter the INPUT file name\n"))
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
# Saving the file in a binary one
with open(input("Please, enter the OUTPUT file name\n"), 'wb') as f:
    np.savetxt(f, matrix)
