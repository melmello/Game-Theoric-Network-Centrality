""" Game module

    Game:
        this class is the game built with
        a specified characteristic function type and an adjacency matrix.

"""

from GAME.CHARACTERISTIC_FUNCTIONS.centrality_type_dictionary import TYPE_TO_CLASS


class Game:
    """ Game Class

        This class has the basic information of the game created.

        Attributes:
            characteristic_function (group_centrality_measure):
                the type of the characteristic function used.

    """

    def __init__(self, matrix, characteristic_function):
        """ Classical __init__ python method

            The method initialize the instance of the class.

            Args:
                self: the instance of the class itself.
                matrix (matrix): the adjacency matrix previously uploaded.
                characteristic_function (group_centrality_measure):
                    the characteristic function type.

            Returns:
                no return is needed.

        """
        self.matrix = matrix
        self.length = len(matrix)
        self.characteristic_function = TYPE_TO_CLASS[characteristic_function](matrix)
        self.item, \
            self.item_class, \
            self.neutral, \
            self.positive, \
            self.positive_relation, \
            self.negative_relation, \
            self.neutral_relation = \
            self.characteristic_function.data_preparation()
