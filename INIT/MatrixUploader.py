import numpy as np


class MatrixUploader:

    def __init__(self, matrix):
        self.matrix = matrix


def input_definition():
    """ Initial function creating the matrix in the software

        The system asks the user to specify the path or the file name of the matrix.
        Then this is read and transferred into a matrix.
        If the user specifies a wrong path or filename, the system underlines it asking again for the answer.

        Args:
            no arguments are required

        Returns:
            matrix: The matrix is the adjacence matrix loaded from the file
    """
    while True:
        try:
            matrix_path = input("Please, enter the file name\n")
            loaded_matrix = np.loadtxt(matrix_path, dtype=int)
        except Exception:
            print("You might have put a wrong file name or path")
            continue
        else:
            break
    print("The Matrix is the following:")
    print(loaded_matrix)
    return loaded_matrix
