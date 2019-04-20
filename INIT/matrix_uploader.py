""" Summary of module here

    class list

"""
import numpy as np


class MatrixUploader:
    """Summary of class here.

        Longer class information....
        Longer class information....

        Attributes:
            likes_spam: A boolean indicating if we like SPAM or not.
            eggs: An integer count of the eggs we have laid.
    """

    def __init__(self):
        self.matrix = self.input_definition()

    @staticmethod
    def input_definition():
        """ Initial function creating the matrix in the software

            The system asks the user to specify the path or the file name of the matrix.
            Then this is read and transferred into a matrix.
            If the user specifies a wrong path or filename, the system underlines it asking again for the answer.
            Notice that this method is static.

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

    def get_matrix(self):
        """ Getter of the parameter matrix

            This is used as a getter of the parameter

            Args:
                no arguments are required

            Returns:
                matrix: The matrix is the adjacence matrix loaded from the file
        """
        return self.matrix
