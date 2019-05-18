""" Polynomial Time SEMI Algorithm

    This algorithm allows the computation of the central nodes of a network
    with a polynomial time complexity, differently from the classic exponential version.

    TODO:
        - explanation of semi_algorithm

"""
import numpy as np

from GAME.CHARACTERISTIC_FUNCTIONS.MATH_TOOLS.mathematical_tools import fast_binomial


def shapley_beta_function(game, k):
    #
    return 1/len(game.matrix)


def semi_algorithm(game, centrality_measure_choice):
    """ Algorithm Application

        Method that applies the algorithm with different important part:
            - Definition of the centrality measure within the characteristic function.
            -

        Args:
            game (Game): the game characterized by a matrix,
                a characteristic function and the input parameters for the SEMI algorithm.
            centrality_measure_choice (string): the centrality measure chosen by the user.

        Returns:
            no return is needed.

    """
    marginal_contribution_init = (len(game.matrix))
    marginal_contribution = np.zeros(marginal_contribution_init, dtype=int)
    shapley_value_init = (len(game.matrix))
    shapley_value = np.zeros(shapley_value_init, dtype=int)
    # marginal_contribution_third_type_init = ()
    # marginal_contribution_third_type = np.zeros(marginal_contribution_third_type_init, dtype=int)
    for shapley_node in shapley_value: 
        for k in range(1, len(game.matrix)):
            # MC(C,u,ϑ) is the Marginal Contribution of node u to coalition C\{u} through the item ϑ
            # MC(C,u) is the sum over ϑ belonging to ϑg of the MC(C,u,ϑ)
            marginal_contribution[k] = 0
            for l_cardinality in range(1, len(game.matrix)):
                for checked_node in range(0, len(game.matrix)):
                    if game.degree[checked_node] == l_cardinality:
                        # FIRST COMPUTATION
                        (first_centrality_measure_parameter, second_centrality_measure_parameter) = game.characteristic_function.centrality_measure(k + 1, checked_node, centrality_measure_choice)
                        neutral_contribution = game.neutral[checked_node][k - 1]
                        marginal_contribution_first_type = first_centrality_measure_parameter * second_centrality_measure_parameter * neutral_contribution
                        marginal_contribution[k - 1] = marginal_contribution[k - 1] + game.positive_relation[checked_node][l_cardinality - 1] * marginal_contribution_first_type
                        #SECOND COMPUTATION
                        (first_centrality_measure_parameter, second_centrality_measure_parameter) = game.characteristic_function.centrality_measure(k, checked_node, centrality_measure_choice)
                        positive_contribution = game.positive[checked_node][k-1]
                        marginal_contribution_second_type = first_centrality_measure_parameter * second_centrality_measure_parameter * positive_contribution
                        marginal_contribution[k - 1] = marginal_contribution[k - 1] + game.positive_relation[checked_node][l_cardinality - 1] * marginal_contribution_second_type
                        #THIRD COMPUTATION
                        marginal_contribution_third_type = first_centrality_measure_parameter * (second_centrality_measure_parameter - second_centrality_measure_parameter) * positive_contribution
                        marginal_contribution[k - 1] = marginal_contribution[k - 1] + game.positive_relation[checked_node][l_cardinality - 1] * marginal_contribution_third_type
                #END STEP
            marginal_contribution[k] = marginal_contribution[k] * shapley_beta_function(game, k) / fast_binomial(len(game.matrix) - 1, k)
            shapley_value[shapley_node] += marginal_contribution[k]
    print("Here are the Shapley Values")
    print(shapley_value)
