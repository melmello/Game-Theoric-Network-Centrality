""" Runner script that starts the project

    <<This module has the starting and fundamental class used to start the program.>>
    It must be run with the following command:
        $ python runner.py

    External Libraries Required:
    - networkx.py
    - matplotlib.py

    No class are present

"""
from GAME.games_manager import GamesManager


def main():
    """ Classical main function

        This function is the fundamental one that starts all.
        Main parts:
            - game_manager initialization.
            - centrality_algorithm application.

        Args:
            no args are needed.

        Returns:
            no return is needed.

    """
    # Initialization
    game_manager = GamesManager()
    # Algorithm Application
    game_manager.centrality_algorithm(input("Select the algorithm complexity:\n"
                                            " - \tPolynomial\n"
                                            " - \tExponential (Working on it)"))


if __name__ == "__main__":
    main()
