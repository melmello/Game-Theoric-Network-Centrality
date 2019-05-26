""" Degree Centrality Characteristic Function module

    GroupDegreeCentrality(GroupCentralityMeasure):
        degree version of the characteristic function.

"""
import numpy as np
from ALGORITHM.TOOLS.mathematical_tools import fast_binomial
from ALGORITHM.TOOLS.utility_tools import word_checker
from GAME.CHARACTERISTIC_FUNCTIONS.group_centrality_measure import GroupCentralityMeasure


class GroupDegreeCentrality(GroupCentralityMeasure):
    """ Degree Centrality Characteristic Function class

        <<Inheriting from group_centrality_measure>>

        Implementation of the characteristic function with the Degree Measure.

        Attributes:
            no attributes are needed.

    """

    def data_preparation(self):
        """ Data Preparation for the polynomial algorithm

            The method is based on the preparation of the data
            that will be the input of the polynomial algorithm.

            Args:
                self: the instance of the class itself.

            Returns:
                degree ([int]): vector with the degree of each node.
                    The degree is the value of the cell, the position is the node number - 1.
                degree_class ([int]): vector with the value of the node with the degree
                    equals to the position - 1.
                neutral ([int][int]): matrix representing the neutral relation
                    on the row the nodes and on the columns the cardinality k of the groups.
                positive ([int][int]): matrix representing the positive relation
                    on the row the nodes and on the columns the cardinality k of the groups.
                positive_relation ([int][int]): matrix representing the positive relation between
                    nodes (expressed by rows) and cardinality groups (expressed by columns).
                negative_relation ([int][int]): matrix representing the negative relation between
                    nodes (expressed by rows) and cardinality groups (expressed by columns).
                neutral_relation ([int][int]): matrix representing the neutral relation between
                    nodes (expressed by rows) and cardinality groups (expressed by columns).

        """
        # DEGREE
        # Initialization
        # Degree has length equal to the number of nodes
        degree_init = (len(self.matrix))
        degree = np.zeros(degree_init, dtype=int)
        # For each 1 in the row of the matrix,
        # just add one to the correspondent position in the degree vector
        # Note that there can't be 1 on the diagonal thanks to the previous matrix adaption
        for row in range(0, len(self.matrix)):
            for column in range(0, len(self.matrix)):
                degree[row] += self.matrix[row, column]
        print("Degree Vector")
        print(degree)

        # DEGREE CLASS
        # Initialization
        # Degree Class vector has length equal to the maximum degree
        degree_class_init = (max(degree))
        degree_class = np.zeros(degree_class_init, dtype=int)
        # For each node, put the degree if the cell is empty
        # In order to have the array position equals to the degree - 1
        # and the cell value correspondent to the node with that degree
        for row in range(0, len(self.matrix)):
            if degree_class[degree[row] - 1] == 0:
                degree_class[degree[row] - 1] = row + 1
        print("Degree Class")
        print(degree_class)

        # N & R
        # ***************************************************
        # Function cN_G(v, k)
        #   if |V| - 1 - deg(v) < k then 0
        #   else (|V| - 1 - deg(v) k)
        # Function cR_G(v, k)
        #   if |V| = k then 0
        #   else (|V| k) - cN_G(v, k) - (|V| - 1 k - 1)
        # ***************************************************
        # Initialization
        # Neutral and Positive matrix has size
        # number of nodes |V| x the max cardinality of the coalition k
        neutral_init = (len(self.matrix), self.max_cardinality + 1)
        neutral = np.zeros(neutral_init, dtype=int)
        positive_init = (len(self.matrix), self.max_cardinality + 1)
        positive = np.zeros(positive_init, dtype=int)
        # For each cardinality of the group possible, going from 0 to the max cardinality |V|
        for k in range(0, self.max_cardinality + 1):
            for row in range(0, len(self.matrix)):
                # NEUTRAL MATRIX
                # Initialize subtracting |V| (node numbers) - 1
                neutral_control_variable = len(self.matrix) - 1
                for column in range(0, len(self.matrix)):
                    if self.matrix[row, column] == 1:
                        # For each node linked to the node of the corresponding node, subtract 1
                        neutral_control_variable = neutral_control_variable - 1
                # If the quantity is greater or equal to k, apply the Newton Binomial Coefficient
                if neutral_control_variable >= k:
                    neutral[row][k] = fast_binomial(neutral_control_variable, k)
                # Otherwise, just set it to 0
                else:
                    neutral[row][k] = 0
                # POSITIVE MATRIX
                # If the cardinality k equals the number of the nodes |V|,
                # just set the cell value to 0
                if k == len(self.matrix):
                    positive[row][k] = 0
                # Otherwise set it to the Newton Binomial of (|V| k) -
                # the Newton Binomial of (|V|-1 k-1) -
                # the correspondent value of the Neutral Matrix
                else:
                    positive[row][k] = fast_binomial(len(self.matrix), k) - \
                                       fast_binomial(len(self.matrix) - 1, k - 1) - \
                                       neutral[row][k]
        print("Neutral Matrix")
        print(neutral)
        print("Positive Matrix")
        print(positive)

        # R, ~R and N
        # ***************************************************
        # for v in V do
        #   for u in E(v) do |RΘdeg(u)({v})| ← |RΘdeg(u)({v})| + 1
        #   for u not in E(v) do |NΘdeg(u)({v})| ← |NΘdeg(u)({v})| + 1
        #   |~RΘdeg(u)({v})| ← 1
        # ***************************************************
        # Initialization
        # All the matrix has size
        # number of nodes |V| x max degree of the nodes
        positive_relation_init = (len(self.matrix), max(degree))
        negative_relation_init = (len(self.matrix), max(degree))
        neutral_relation_init = (len(self.matrix), max(degree))
        positive_relation = np.zeros(positive_relation_init, dtype=int)
        negative_relation = np.zeros(negative_relation_init, dtype=int)
        neutral_relation = np.zeros(neutral_relation_init, dtype=int)
        # For each node
        for row in range(0, len(self.matrix)):
            for column in range(0, len(self.matrix)):
                # If there is a link with another node,
                # add 1 to the value of the cell corresponding to the node selected
                # and group cardinality of the node which the selected node is linked to
                if self.matrix[row][column] == 1:
                    positive_relation[row][degree[column] - 1] += 1
                # If there is not a link with another node (different from me),
                # add 1 to the value of the cell corresponding to the node selected
                # and group cardinality of the node which the selected node is not linked to
                if (self.matrix[row][column] == 0) & (row != column):
                    neutral_relation[row][degree[column] - 1] += 1
            # Put 1 in the cell corresponding to the node index as a row
            # and the group cardinality of the node as a column
            negative_relation[row][degree[row] - 1] = 1
        print("Positive Relation Matrix")
        print(positive_relation)
        print("Negative Relation Matrix")
        print(negative_relation)
        print("Neutral Relation Matrix")
        print(neutral_relation)
        return \
            degree, \
            degree_class, \
            neutral, \
            positive, \
            positive_relation, \
            negative_relation, \
            neutral_relation

    def centrality_measure(self, node, coalition_cardinality, centrality_measure_choice):
        """ Centrality Measure Application

            Method used to apply the chosen Centrality Measure
            of the Degree characteristic function.
            There are four types of Degree with different calculation and returns:
                - Degree
                - Weighted Degree
                - Impact Factor
                - Normalized Degree

            Args:
                node (int): the node which apply the centrality measure to.
                coalition_cardinality (int): the cardinality of the coalition C
                    where the node is in.
                centrality_measure_choice (string): the centrality measure chosen.

            Returns:
                (int,int): it is always returned a couple of int, the first used for the
                    SEMI-Algorithm f() function, and the second for the g() SEMI function.
                    Be aware that in case there is a wrong choice, the Degree version is returned.

        """
        # Degree of Everett and Borgatti (1999)
        # f(v) = 1
        # g(|C|) = 1
        if centrality_measure_choice == "degree":
            return 1, 1
        # Weighted Degree of Newman (2004)
        # f(v) = 1/deg(v)
        # g(|C|) = 1
        if centrality_measure_choice == "weighted":
            temp = 0
            for column in range(0, len(self.matrix)):
                temp += self.matrix[node][column]
            return 1 / temp, 1
        # Impact Factor of Bollen, Sompel, Smith, and Luce (2005)
        # f = 1
        # g = 1/|C|
        # if |C| is 0, return 1
        if centrality_measure_choice == "impact":
            if coalition_cardinality == 0:
                return 1, 1
            else:
                return 1, 1 / coalition_cardinality
        # Normalised Degree of Everett and Borgatti (1999)
        # f = 1
        # g = 1/(|V|-|C|)
        # if |C| = |V|, return 1
        if centrality_measure_choice == "normalised":
            if len(self.matrix) == coalition_cardinality:
                return 1, 1
            else:
                return 1, 1 / (len(self.matrix) - coalition_cardinality)
        # Classic Degree version is chosen
        else:
            return 1, 1

    def centrality_measure_selection(self):
        """ Centrality Measure Selection

            Method used to return all possible choices of the centrality
            measure related to the characteristic function chosen.

            Args:
                self: the instance itself.

            Returns:
                string: the choice of the user on the centrality measure possibilities.

        """
        return word_checker(input("Select the centrality measure:\n"
                                  " - \tDegree\n"
                                  " - \tWeighted Degree\n"
                                  " - \tImpact Factor\n"
                                  " - \tNormalised Degree"),
                            ["degree",
                             "weighted",
                             "impact",
                             "normalised"])
