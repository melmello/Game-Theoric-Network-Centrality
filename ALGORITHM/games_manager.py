""" Manager of the games

    GamesManager:
        this class contains the core of the program in which all the actions are taken.
        An example is the import of the user's matrix, the graph visualization or the choice of the
        characteristic function.

"""
from INIT.matrix_uploader import MatrixUploader
from INIT.graph_builder import GraphBuilder
from GAME.game import Game


class GamesManager:
    """ Creator and manager of the game

        This class is used to build the game from the adjacency matrix and
        to manage the game created applying the algorithm.

        Attributes:
            no attributes are needed.

    """

    @staticmethod
    def initialization():
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
        # game = Game(adjacency_matrix, input("Select the characteristic function"))
