""" Summary of module here

    class list

"""


class GameCreator:
    """Summary of class here.

        Longer class information....
        Longer class information....

        Attributes:
            likes_spam: A boolean indicating if we like SPAM or not.
            eggs: An integer count of the eggs we have laid.
    """

    def new_game(self, matrix):
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
                game_type = input("Please, enter the game type you want to build\n")
                # Create GeneralType(matrix), the game searching the type of the class TYPEMASTER -> subtypes
            except Exception:
                print("You might have put a wrong file name or path")
                continue
            else:
                break
        return game_type
