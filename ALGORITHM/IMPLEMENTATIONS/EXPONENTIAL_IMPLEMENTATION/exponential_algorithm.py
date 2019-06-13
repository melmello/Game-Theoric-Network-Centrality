""" Exponential Time Algorithm

    This algorithm allows the computation of the central nodes in a network using
    the classical Shapley Value algorithm with a chosen characteristic function.

"""
from itertools import combinations
from math import factorial
import mpmath
import numpy as np


def classical_algorithm(game):
    """ Classical Shapley Calculus Algorithm

        Method that computes the Shapley Value for each node in the network
        using the characteristic function chosen as the way of obtaining the
        value that a coalition assume.

        Args:
            game (Game): the game characterized by a matrix,
                a characteristic function and the input parameters for the SEMI algorithm.

        Returns:
            no return is needed.

    """
    # Shapley Vector Initialization
    shapley_value = np.zeros(game.length)
    # Create a list of all the nodes
    node_list = list(range(0, game.length))
    # Create a list of all the nodes that will be manipulated for permutation
    permutable_nodes = list(range(0, game.length))
    # For each node in the network
    for node in range(0, game.length):
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("NODE EVALUATED: ", node)
        # Remove the node selected in order to obtain all the coalition not cointaing
        # the node selected in the cycle
        permutable_nodes.remove(node)
        # Initialize the total marginal contribution
        total_marginal_contribution = 0
        # For each coalition cardinality (s) going from 1 to |V|
        for coalition_cardinality in range(1, game.length):
            print("\tCOALITION CARDINALITY: ", coalition_cardinality)
            # For each permutation of all the nodes (except for the node selected)
            # of size coalition cardinality s
            for permutation_tuple in combinations(permutable_nodes, coalition_cardinality):
                # Cast the tuple to list
                permutation = list(permutation_tuple)
                # − v(S) + v(S ∪ {i})
                marginal_contribution = \
                    - game.characteristic_function.get_coalition_value(game,
                                                                       node_list,
                                                                       permutation) + \
                    game.characteristic_function.get_coalition_value(game,
                                                                     node_list,
                                                                     permutation + [node])
                print("\t\tMARGINAL CONTRIBUTION: ", marginal_contribution)
                # Weight the result by ((s!) * (n - s - 1)!) / (n!) with s
                # coalition size and n the number of all the vertex
                weighted_marginal_contribution = \
                    marginal_contribution * \
                    ((factorial(len(permutation)) *
                      factorial(game.length - len(permutation) - 1))
                     / (factorial(game.length)))
                print("\t\tWEIGHTED MARGINAL CONTRIBUTION: ", weighted_marginal_contribution)
                # Add this value to the marginal contribution of that node
                total_marginal_contribution += weighted_marginal_contribution
                print("\t\tTOTAL MARGINAL CONTRIBUTION: ", total_marginal_contribution)
        # Added contribution of V({i}) - V(∅)
        # Note that V(∅) = 0 in these games
        total_marginal_contribution += \
            (1 / game.length) * \
            game.characteristic_function.get_coalition_value(game,
                                                             node_list,
                                                             [node])
        # Reintroduce in list the node deleted before to cycle over the next node
        permutable_nodes.append(node)
        # Update the Shapley Value Vector
        shapley_value[node] = total_marginal_contribution
        print("\t\tTOTAL MARGINAL CONTRIBUTION: ", total_marginal_contribution)
        print("FINAL SHAPLEY VALUES: \n", shapley_value)
    print("\nSHAPLEY VALUES SUM: ", np.sum(shapley_value))
