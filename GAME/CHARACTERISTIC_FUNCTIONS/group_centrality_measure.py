""" Interface of the characteristic functions

    GroupCentralityMeasure:
        it is the interface and the parent of all characteristic functions type derived and used.
        This is done in order to have a scalable and extensible program.

"""


class GroupCentralityMeasure:
    """ Parent of all the centrality measure class

        This class is used as the superclass of each possible group centrality measure implemented.
        You can add your personal characteristic function taking this as superclass and overriding
        the get_items method, respecting obviously the return conventions.

        Attributes:
            no attributes are needed.

    """

    def __init__(self, matrix):
        """ Classical __init__ python method

            The method initialize the instance of the class.

            Args:
                self: the instance of the class itself.
                matrix (matrix): the adjacency matrix previously uploaded.

            Returns:
                no return is needed.

        """
        self.matrix = matrix
        self.max_cardinality = len(self.matrix)

    def data_preparation(self):
        """ Data Preparation

            This is the super-method that prepare the input of the SEMI Algorithm.

            Args:
                self: the instance of the class itself.

            Returns:
                None: since this is the super method.

        """
        return None

    def centrality_measure(self, node, coalition_cardinality, centrality_measure_choice):
        """ Centrality Measure Application

            Method used to apply the Centrality Measure in the correspondent
            characteristic function chosen.

            Args:
                node (int): the node which apply the centrality measure to.
                coalition_cardinality (int): the cardinality of the coalition C
                    where the node is in.
                centrality_measure_choice (string): the centrality measure chosen.

            Returns:
                None: since this is the super method

        """
        return None

    def centrality_measure_selection(self):
        """ Centrality Measure Selection

            Method used to return all possible choices of the centrality
            measure related to the characteristic function chosen.

            Args:
                self: the instance itself.

            Returns:
                None: since this is the super method

        """
        return None

    def get_coalition_value(self, game, node_list, permutation_list):
        """ Getter of the coalition value

            Method used to return the correspondent value of the coalition
            using the correspondent characteristic function chosen.

            Args:
                game (Game): the game characterized by a matrix,
                    a characteristic function and the input parameters for the SEMI algorithm.
                node_list ([int]): list with all the node in the network.
                permutation_list ([int]): coalition for which i want the characteristic value.

            Returns:
                None: since this is the super method

        """
        return None
