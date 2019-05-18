""" Polynomial Time SEMI Algorithm

    This algorithm allows the computation of the central nodes of a network
    with a polynomial time complexity, differently from the classic exponential version.

    TODO:
        - explanation of semi_algorithm

"""
import numpy as np

from ALGORITHM.MATH_TOOLS.mathematical_tools import fast_binomial


def shapley_beta_function(game, k):
    return 1/len(game.matrix)


def semi_algorithm(game, centrality_measure_choice):
    """ Algorithm Application

        Method that applies the algorithm with different important part:
            - Definition of the centrality measure within the characteristic function.
            - Calculation of the marginal contribution:
                - MC1: first marginal contribution part, based on positive and neutral relation
                - MC2: second marginal contribution part, based on positive and negative relation
                - MC3: first marginal contribution part, based on
                    the sum of positive and neutral relation
            - Calculation of the weighted general marginal contribution
            - Update of the Shapley Values

        Args:
            game (Game): the game characterized by a matrix,
                a characteristic function and the input parameters for the SEMI algorithm.
            centrality_measure_choice (string): the centrality measure chosen by the user.

        Returns:
            no return is needed.

    """
    # Initialization
    # Shapley Value vector has size equals to the number of nodes.
    shapley_value_init = (len(game.matrix))
    shapley_value = np.zeros(shapley_value_init)
    # For each node considered in order to find its shapley value
    for evaluated_node in range(0, len(game.matrix)):
        # For each possible coalition size, starting from the empty and going to |V| - 1
        for k in range(0, len(game.matrix)):
            # Initialize each time the marginal contribution of that node to 0
            marginal_contribution = 0
            # For each l possible value that that the partition of set can assume
            for l_cardinality in range(1, max(game.item) + 1):
                # If there is not an item belonging to the partition of size l, just continue the cycle
                # avoiding all operations for that l and jumping to the l + 1 partition cardinality
                if game.item_class[l_cardinality - 1] == 0:
                    print("K:")
                    print(k)
                    print("L:")
                    print(l_cardinality)
                    print("NO CORRESPONDENCE")
                    continue
                # Otherwise, continue with the marginal contribution computation
                print("K:")
                print(k)
                print("L:")
                print(l_cardinality)
                # MC1 - FIRST PART COMPUTATION
                # Definition of f and g parameters
                (centrality_measure_f_parameter, centrality_measure_g_of_k_plus_1_parameter) = \
                    game.characteristic_function.centrality_measure(evaluated_node,
                                                                    k + 1,
                                                                    centrality_measure_choice)
                # Definition of the set of coalitions of size k
                # to which item ϑ is neutrally related
                neutral_contribution = game.neutral[game.item_class[l_cardinality - 1] - 1][k]
                # Definition of the first type marginal contribution, by the product of
                # the f and g parameters and the neutral matrix contribution
                marginal_contribution_first_type = \
                    centrality_measure_f_parameter * \
                    centrality_measure_g_of_k_plus_1_parameter * \
                    neutral_contribution
                # First type marginal contribution addition to the general marginal contribution,
                # weighted by the value that the set of items in group Θl
                # is positively related to C has
                marginal_contribution = \
                    marginal_contribution + \
                    game.positive_relation[evaluated_node][l_cardinality - 1] * \
                    marginal_contribution_first_type
                print("1 - FIRST MARGINAL CONTRIBUTION")
                print(marginal_contribution_first_type)
                print("1 - MARGINAL CONTRIBUTION")
                print(marginal_contribution)
                # MC2 - SECOND COMPUTATION
                # Definition of f and g parameters
                (centrality_measure_f_parameter, centrality_measure_g_of_k_parameter) = \
                    game.characteristic_function.centrality_measure(evaluated_node,
                                                                    k,
                                                                    centrality_measure_choice)
                # Definition of the set of coalitions of size k
                # to which item ϑ is positively related
                positive_contribution = game.positive[game.item_class[l_cardinality - 1] - 1][k]
                # Definition of the second type marginal contribution, by the product of
                # the f and g parameters and the positive matrix contribution
                marginal_contribution_second_type = \
                    centrality_measure_f_parameter * \
                    centrality_measure_g_of_k_parameter * \
                    positive_contribution
                # Second type marginal contribution subtraction to the general marginal contribution,
                # weighted by the value that the set of items in group Θl
                # is negatively related to C has
                marginal_contribution = \
                    marginal_contribution - \
                    game.negative_relation[evaluated_node][l_cardinality - 1] * \
                    marginal_contribution_second_type
                print("2 - SECOND MARGINAL CONTRIBUTION")
                print(marginal_contribution_second_type)
                print("2 - MARGINAL CONTRIBUTION")
                print(marginal_contribution)
                # MC3 - THIRD COMPUTATION
                # Definition of the third type marginal contribution, by the product of
                # the f parameter, the difference between the g parameter for k + 1 and k,
                # and the positive matrix contribution
                marginal_contribution_third_type = \
                    centrality_measure_f_parameter * \
                    (centrality_measure_g_of_k_plus_1_parameter -
                     centrality_measure_g_of_k_parameter) * \
                    positive_contribution
                # Third type marginal contribution addiction to the general marginal contribution,
                # weighted by the value that the set of items in group Θl
                # is negatively related to C has summed to the value that the set of items
                # in group Θl is positively related to C
                marginal_contribution = \
                    marginal_contribution + \
                    (game.positive_relation[evaluated_node][l_cardinality - 1] +
                     game.neutral_relation[evaluated_node][l_cardinality - 1]) * \
                    marginal_contribution_third_type
                print("3 - THIRD MARGINAL CONTRIBUTION")
                print(marginal_contribution_third_type)
                print("3 - MARGINAL CONTRIBUTION")
                print(marginal_contribution)
            # MC - END STEP
            # Final computation of the marginal contribution as the value previously calculated
            # weighted by the division between the Shapley Beta function and the Newton binomial
            # coefficient of |V| - 1 and k
            print("END STEP")
            marginal_contribution *= (shapley_beta_function(game, k) /
                                      fast_binomial(len(game.matrix) - 1, k))
            print("WEIGHTED MARGINAL CONTRIBUTION")
            print(marginal_contribution)
            # Update of the Shapley Value of the node evaluated with the sum of the previous value
            # and the weighted marginal contribution
            shapley_value[evaluated_node] += marginal_contribution
            print("SHAPLEY VALUES")
            print(shapley_value)
