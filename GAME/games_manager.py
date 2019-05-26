""" Manager of the games

    GamesManager:
        this class contains the core of the program in which all the actions are taken.
        An example is the import of the user's matrix, the graph visualization or the choice of the
        characteristic function.

"""
from ALGORITHM.IMPLEMENTATIONS.EXPONENTIAL_IMPLEMENTATION.exponential_algorithm \
    import classical_algorithm
from ALGORITHM.IMPLEMENTATIONS.POLYNOMIAL_IMPLEMENTATION.polynomial_algorithm \
    import semi_algorithm
from ALGORITHM.INIT.graph_builder import GraphBuilder
from ALGORITHM.INIT.matrix_uploader import MatrixUploader
from ALGORITHM.TOOLS.utility_tools import word_checker
from GAME.game import Game


class GamesManager:
    """ Creator and manager of the game

        This class is used to build the game from the adjacency matrix and
        to manage the game created applying the algorithm.

        Attributes:
            no attributes are needed.

    """

    def __init__(self):
        """ Initialization of the game

            Method that initialize the game by:
            - importing the adjacency matrix into the python script
            - visualize the adjacency matrix as a directed graph

            Args:
                no args are needed.

            Returns:
                no return is needed.

        """
        # Loading the adjacency matrix and printing it
        adjacency_matrix = MatrixUploader().get_matrix()
        # Graph construction and visualization
        GraphBuilder(adjacency_matrix).graph_construction()
        # New Game
        self.game = Game(adjacency_matrix,
                         word_checker(input("Select the characteristic function:\n"
                                            " - \tgroup_degree_centrality\n"
                                            " - \tgroup_betweenness_centrality\n"
                                            " - \tgroup_closeness_centrality"),
                                      ["group_degree_centrality",
                                       "group_betweenness_centrality",
                                       "group_closeness_centrality"]))

    def centrality_algorithm(self, choice):
        """ Application of the chosen algorithm

            There are basically two main choices to make a comparison:
                - Exponential: the classical Shapley Value algorithm.
                - Polynomial: the SEMI value application.

            Args:
                self: the instance itself that i can use to pass the game to the algorithm.
                choice (string): represent the choice of the user on the algorithm complexity.

            Returns:
                no return is needed.

        """
        if choice == "Polynomial":
            semi_algorithm(self.game,
                           self.game.characteristic_function.centrality_measure_selection())
        if choice == "Exponential":
            classical_algorithm(self.game,
                                self.game.characteristic_function.centrality_measure_selection())
