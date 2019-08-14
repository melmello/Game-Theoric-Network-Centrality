""" Uploader of the User's Matrix

    MatrixUploader:
        this class is used to take the user's input (adjacency matrix)
        and save it into the program.

"""
import numpy as np

from ALGORITHM.TOOLS.utility_tools import word_checker


class MatrixUploader:
    """ Matrix .txt to Matrix Class

        The input is transferred to the program and saved as a matrix.
        Some checks on the file extension and name are done to ensure the correct process.
        It is ensured that the matrix is symmetric and binary, and so it
        represents an undirected unweighted graph.

        Attributes:
            no attributes are needed.

    """

    def __init__(self):
        """ Classic __init__ python function

            Initialization of the instance.

            Args:
                self: the instance of the class itself.

            Returns:
                no return is needed.

        """
        self.matrix = self.input_definition()

    @staticmethod
    def input_definition():
        """ Initial function creating the matrix in the software

            The system asks the user to specify the file name of the matrix or the
            corresponding edge list to create a RAM version of it.
            Then this is read and transferred into a matrix.
            If the user specifies a wrong path or filename,
            the system underlines it asking again for the answer.
            Notice that this method is static.

            Args:
                no arguments are required.

            Returns:
                matrix (matrix): The matrix is the adjacency matrix loaded from the file.

        """
        # Matrix initialization
        loaded_matrix = []
        if word_checker(input("Please, select if you want to upload an edge list or a matrix file\n"),
                        ["matrix", "list"]) == "list":
            # Open the file in the EXAMPLES/EDGES_LIST_EXAMPLES folder of the project
            file = open('EXAMPLES/EDGES_LIST_EXAMPLES/' + input("Please, enter the INPUT file name\n"))
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
            loaded_matrix = np.zeros((max_length + 1, max_length + 1), dtype=int)
            # For each row
            for row in file:
                # Results of the file line
                res = [int(i) for i in row.split() if i.isdigit()]
                # Set first direction arc
                loaded_matrix[res[0]][res[1]] = 1
                # Set the symmetric direction arc
                loaded_matrix[res[1]][res[0]] = 1
        else:
            while True:
                try:
                    loaded_matrix = np.loadtxt('EXAMPLES/MATRIX_EXAMPLES/' + input("Please, enter the file name\n"),
                                               dtype=int)
                except IOError:
                    print("You might have put a wrong file name or path")
                    continue
                else:
                    break
        print("The Matrix is the following:")
        print(loaded_matrix)
        # TODO - Uncomment to check symmetry
        # Check on matrix symmetry (to ensure the graph is undirected)
        # if not np.allclose(loaded_matrix, loaded_matrix.T):
        #    print("The matrix you have chosen is not suitable for this algorithm.")
        #    exit(0)
        # Ensure that the matrix is binary (and thus unweighted)
        if not np.array_equal(loaded_matrix, loaded_matrix.astype(bool)):
            print("The matrix you have chosen is not suitable for this algorithm.")
            exit(1)
        # This is used to clean out the loop cycles on the matrix,
        # precisely the 1 in the matrix that are on the diagonal
        for row in range(0, len(loaded_matrix)):
            for column in range(0, len(loaded_matrix)):
                if row == column:
                    loaded_matrix[row][column] = 0
        print("But we will use this one (without self-loops):")
        print(loaded_matrix)
        return loaded_matrix

    def get_matrix(self):
        """ Getter of the parameter matrix

            This method is used as a getter of the parameter.

            Args:
                self: the instance of the class.

            Returns:
                matrix (matrix): the matrix is the adjacency matrix loaded from the file.

        """
        return self.matrix
