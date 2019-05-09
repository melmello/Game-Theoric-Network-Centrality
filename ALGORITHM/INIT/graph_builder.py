""" Graph Visualizer

    GraphBuilder:
        This class is used in order to have a feedback on the graph structure.
        The screen prints out the adjacency matrix as a directed graph.

    TODO: x,y in the for
        - names convention

"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class GraphBuilder:
    """ Graph builder and plotter

        The graph is built and plotted on the screen as a directed graph.

        Attributes:
            no attributes are required.

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

    def graph_construction(self):
        """ [OPTIONAL] Function crating the graph visualized

            The system takes the matrix object and builds the graph,
            specifying the nodes number and the edges.
            Notice that this is used only to have a graphic feedback
            and thus this function can be avoided speeding up the program.

            Args:
                self: the instance of the class itself.

            Returns:
                no return is required.
        """
        # Counting nodes
        nodes_number = self.matrix.shape[0]

        # Unpacking of the row and column coordinates where the ith and jth element is 1
        rows, cols = np.where(self.matrix == 1)

        # Rearranges the list of rows and columns into a list of edge tuples.
        # Printing all starting nodes
        # Printing all ending nodes
        # Printing all edges
        # F means FROM, T means TO
        edges = zip(rows.tolist(), cols.tolist())
        print("F nodes:", np.arange(self.matrix.shape[0]))
        print("T nodes:", np.arange(self.matrix.shape[1]))
        print("Edges:")
        for first_param, second_param in zip(rows.tolist(), cols.tolist()):
            print((first_param, second_param))
        # Create a Directed Graph Object adding the nodes and the edges previously calculated
        directed_graph = nx.DiGraph()
        directed_graph.add_nodes_from(range(nodes_number))
        directed_graph.add_edges_from(edges)
        # Printing
        pos = nx.drawing.layout.circular_layout(directed_graph)
        nx.draw_networkx(directed_graph, pos=pos)
        plt.axis('off')
        plt.show()
